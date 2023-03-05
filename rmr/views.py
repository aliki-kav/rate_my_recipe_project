from datetime import datetime

from django.conf.global_settings import MEDIA_URL
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from rmr.models import UserProfile
from rmr.models import Recipe
from rmr.models import Category, Page,Rating
from rmr.forms import CategoryForm, PageForm, UserForm, UserProfileForm,RecipeForm,RatingForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404


def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    page_list = Page.objects.order_by('-views')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    context_dict['pages'] = page_list

    visitor_cookie_handler(request)

    response = render(request, 'rmr/index.html', context=context_dict)
    return response


def about(request):
    visitor_cookie_handler(request)
    visits = request.session['visits']
    context_dict = {'boldmessage': 'Simone',
                    'visits': visits}

    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED!")
        request.session.delete_test_cookie()

    return render(request, 'rmr/about.html', context=context_dict)


def show_category(request, category_name_slug):
    print(category_name_slug)
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        recipes = Recipe.objects.filter(category=category)
        context_dict['recipes'] = recipes
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['recipes'] = None
        context_dict['category'] = None
    return render(request, 'rmr/category.html', context=context_dict)


@login_required
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            cat = form.save(commit=True)
            print(cat, cat.slug)
            return redirect('/rmr/')
        else:
            print(form.errors)
    return render(request, 'rmr/add_category.html', {'form': form})


@login_required
def add_page(request, category_name_slug):
    try:
        print(category_name_slug)
        category = Category.objects.get(slug=category_name_slug)

    except Category.DoesNotExist:
        category = None

    if category is None:
        print('category is none')
        return redirect('/rmr/')

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            page = form.save(commit=False)
            page.category = category
            page.views = 0
            page.save()

            return redirect(reverse('rmr:show_category', kwargs={'category_name_slug': category_name_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'category': category}
    return render(request, 'rmr/add_page.html', context=context_dict)


def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'rmr/register.html', context={'user_form': user_form,
                                                           'profile_form': profile_form,
                                                           'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('rmr:index'))
            else:
                return HttpResponse("Your rmr account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'rmr/login.html', context={})


def user_logout(request):
    logout(request)
    return redirect(reverse('rmr:index'))


@login_required
def restricted(request):
    return render(request, 'rmr/restricted.html')

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
    userprofile = get_object_or_404(UserProfile, user__username=username)
    if request.user.username == username:
        ratings = Rating.objects.filter(user=userprofile.user)
        recipes = Recipe.objects.filter(user=userprofile.user)
        return render(request, 'rmr/user_profile.html', {'userprofile': userprofile, 'ratings': ratings, 'recipes': recipes})
    else:
        return render(request, '403.html')


def add_recipe(request, username):
    username = request.user.username
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
    return render(request, 'rmr/add_recipe.html', {'form': form, 'username': username})


def show_recipe(request, category_name_slug, recipe_title_slug):
    print(recipe_title_slug)
    context_dict = {}
    try:
        recipe = Recipe.objects.get(slug=recipe_title_slug)
        context_dict['recipe'] = recipe
        if request.user.is_anonymous:
            context_dict['rating'] = None
        else:
            rating = Rating.objects.filter(user=request.user, recipe=recipe).first()
            context_dict['rating'] = rating

        if request.method == 'POST':
            form = RatingForm(request.POST)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.user = request.user
                rating.recipe = recipe
                rating.save()
                return redirect(reverse('rmr:show_recipe', kwargs={'category_name_slug': recipe.category.slug,
                                                                   'recipe_title_slug': recipe.slug}))
            else:
                print(form.errors)
        else:
            form = RatingForm()
        context_dict['form'] = form;
    except Recipe.DoesNotExist:
        context_dict['recipe'] = None
    return render(request, 'rmr/recipe.html', context=context_dict)

def breakfast(request):
    return render(request, 'rmr/breakfast.html')

def lunch(request):
    return render(request, 'rmr/lunch.html')
    
def dinner(request):
    return render(request, 'rmr/dinner.html')

def dessert(request):
    return render(request, 'rmr/dessert.html')