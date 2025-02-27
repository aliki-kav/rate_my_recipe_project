from datetime import datetime

from django.conf.global_settings import MEDIA_URL
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.db.models import Avg, Sum
from rmr.models import Category, Rating, UserProfile, Recipe
from rmr.forms import CategoryForm, UserForm, UserProfileForm, RecipeForm, RatingForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404


def index(request):
    category_list_sorted = Category.objects.order_by('-likes')[:5]
    category_list = Category.objects.all()
    recipe_list = Recipe.objects.order_by('-views')[:5]
    search_recipe = request.GET.get('search')

    if search_recipe:
        request.session['keyword'] = search_recipe
        return redirect(reverse('rmr:search'))

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories_sorted'] = category_list_sorted
    context_dict['categories'] = category_list
    context_dict['recipes'] = recipe_list

    visitor_cookie_handler(request)

    response = render(request, 'rmr/index.html', context=context_dict)
    return response


@login_required
def delete_user(request, username):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('rmr:index')

    return render(request, 'rmr/delete_user.html', {'username': username})

def show_category(request, category_name_slug):
    print(category_name_slug)
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        recipes = Recipe.objects.filter(category=category)
        category_list = Category.objects.all()
        context_dict['recipes'] = recipes
        context_dict['category'] = category
        context_dict['categories'] = category_list
    except Category.DoesNotExist:
        context_dict['recipes'] = None
        context_dict['category'] = None

    if request.method == 'POST':
        if request.method == 'POST':
            query = request.POST['query'].strip()

            if query:
                context_dict['result_list'] = run_query(query)

    return render(request, 'rmr/category.html', context=context_dict)


def register(request):
    registered = False
    category_list = Category.objects.all()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            registered = True
            profile.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rmr/register.html', context={'user_form': user_form,
                                                           'profile_form': profile_form,
                                                           'registered': registered,
                                                         'categories': category_list})


def user_login(request):
    category_list = Category.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return JsonResponse({'success': True})
            else:
                return HttpResponse("Your rmr account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return JsonResponse({'success': False})
    else:
        return render(request, 'rmr/login.html', context={'categories': category_list})



def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        messages.success(request, 'Your account has been successfully deleted.')
        logout(request)
        return redirect('rmr:index')

    return render(request, 'rmr/user_profile.html')



def user_logout(request):
    logout(request)
    return redirect(reverse('rmr:index'))





def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val

    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie

    request.session['visits'] = visits


def userprofile(request, username):
    category_list = Category.objects.all()
    userprofile = get_object_or_404(UserProfile, user__username=username)
    if request.user.username == username:
        ratings = Rating.objects.filter(user=userprofile.user)
        recipes = Recipe.objects.filter(user=userprofile.user)
        if recipes:
            max_views = recipes.aggregate(Sum('views'))['views__sum']
        else:
            max_views = -1
        return render(request, 'rmr/user_profile.html', {'userprofile': userprofile,
                                                         'ratings': ratings,
                                                         'recipes': recipes,
                                                         'max_views': max_views,
                                                         'categories': category_list})
    else:
        return render(request, '403.html')

@login_required
def add_recipe(request, username):
    username = request.user.username
    category_list = Category.objects.all()
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect(reverse('rmr:show_recipe', kwargs={'category_name_slug': recipe.category.slug,
                                    'recipe_title_slug': recipe.slug}))
    else:
        form = RecipeForm()
    return render(request, 'rmr/add_recipe.html', {'form': form, 'username': username, 'categories': category_list})

@login_required
def delete_recipe(request, username, slug):
    toDelete=Recipe.objects.get(slug=slug)
    toDelete.delete()
    return redirect(reverse('rmr:userprofile', kwargs={'username':username}))


def show_recipe(request, category_name_slug, recipe_title_slug):
    category_list = Category.objects.all()
    context_dict = {}
    try:
        recipe = Recipe.objects.get(slug=recipe_title_slug)
        context_dict['recipe'] = recipe
        ratings = Rating.objects.filter(recipe=recipe).order_by('-rating')
        if ratings:
            average = ratings.aggregate(Avg('rating'))['rating__avg']
            context_dict['average'] = round(average, 2)
            context_dict['width'] = int(float(context_dict['average'])/5*100)
        else:
            context_dict['average'] = 0
            context_dict['width'] = 0
        context_dict['comments'] = ratings
        if request.user.is_anonymous:
            context_dict['user_rating'] = None
        else:
            rating = Rating.objects.filter(user=request.user, recipe=recipe).first()
            context_dict['user_rating'] = rating

        if request.method == 'POST':
            rating_value = request.POST.get('rating', None)
            rating_comment = request.POST.get('comment', None)
            raing_obj = Rating(recipe=recipe,user=request.user,rating=rating_value, comment=rating_comment)
            raing_obj.save()
            return redirect(reverse('rmr:show_recipe', kwargs={'category_name_slug': recipe.category.slug,
                                                               'recipe_title_slug': recipe.slug}))
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None
    context_dict['categories'] = category_list
    return render(request, 'rmr/recipe.html', context=context_dict)


def goto_url(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')

        try:
            selected_recipe = Recipe.objects.get(id=recipe_id)
        except Recipe.DoesNotExist:
            return redirect(reverse('rmr:index'))

        selected_recipe.views = selected_recipe.views + 1
        selected_recipe.save()
        return redirect(reverse('rmr:show_recipe', kwargs={'category_name_slug': selected_recipe.category.slug,
                                                           'recipe_title_slug': selected_recipe.slug}))
    return redirect(reverse('rmr:index'))


def get_recipe_data(request, recipe_id):
    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return JsonResponse({'error': 'Recipe not found'}, status=404)

    data = {
        'title': recipe.title,
        'description': recipe.description,
        'instructions': recipe.instructions,
    }

    return JsonResponse(data)


def search(request):
    keyword = request.GET.get('search', '')
    category_list = Category.objects.all()
    recipe_list = Recipe.objects.filter(Q(title__icontains=keyword) | Q(description__icontains=keyword))
    context_dict = {'categories': category_list,
                    'recipes': recipe_list,
                    'keyword': keyword}
    return render(request, 'rmr/search.html', context=context_dict)


