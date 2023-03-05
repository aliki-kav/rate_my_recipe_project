import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rate_my_recipe_project.settings')
import django
django.setup()
from django.contrib.auth.models import User

from rmr.models import Category, Page, Recipe,UserProfile, Rating
from django.utils.text import slugify



def populate():
    # Create users and user profiles
    users = [
        {'username': 'john', 'email': 'john@example.com', 'password': 'password'},
        {'username': 'jane', 'email': 'jane@example.com', 'password': 'password'},
        {'username': 'bob', 'email': 'bob@example.com', 'password': 'password'}
    ]
    for user_data in users:
        user = User.objects.create_user(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        profile = UserProfile.objects.create(user=user)

    # Create categories
    breakfast = Category.objects.get_or_create(name='Breakfast')[0]
    lunch = Category.objects.get_or_create(name='Lunch')[0]
    dinner = Category.objects.get_or_create(name='Dinner')[0]
    dessert = Category.objects.get_or_create(name='Dessert')[0]

    # Create recipes
    breakfast_recipes = [
        {
            'title': 'Pancakes',
            'description': 'A delicious breakfast treat!',
            'instructions': 'Mix the batter and cook in a pan.',
            'category': breakfast,
            'user': User.objects.get(username='john')
        },
        {
            'title': 'Omelette',
            'description': 'A classic breakfast dish!',
            'instructions': 'Whisk the eggs and cook in a pan with toppings.',
            'category': breakfast,
            'user': User.objects.get(username='jane')
        }
    ]
    for recipe_data in breakfast_recipes:
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            description=recipe_data['description'],
            instructions=recipe_data['instructions'],
            category=recipe_data['category'],
            user=recipe_data['user']
        )
        recipe.slug = slugify(recipe.title)
        recipe.save()

    lunch_recipes = [
        {
            'title': 'Grilled Cheese',
            'description': 'A classic sandwich!',
            'instructions': 'Put cheese between bread and grill.',
            'category': lunch,
            'user': User.objects.get(username='john')
        },
        {
            'title': 'BLT',
            'description': 'Bacon, lettuce, and tomato!',
            'instructions': 'Cook the bacon and assemble with lettuce and tomato on bread.',
            'category': lunch,
            'user': User.objects.get(username='jane')
        }
    ]
    for recipe_data in lunch_recipes:
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            description=recipe_data['description'],
            instructions=recipe_data['instructions'],
            category=recipe_data['category'],
            user=recipe_data['user']
        )
        recipe.slug = slugify(recipe.title)
        recipe.save()

    dinner_recipes = [
        {
            'title': 'Spaghetti Bolognese',
            'description': 'A classic Italian pasta dish.',
            'instructions': 'Boil the spaghetti. Cook the beef. Mix everything together.',
            'category': dinner,
            'user': User.objects.get(username='bob')
        },
        {
            'title': 'Chicken Curry',
            'description': 'A spicy Indian dish.',
            'instructions': 'Cook the chicken. Mix with the curry sauce. Serve with rice.',
            'category': dinner,
            'user': User.objects.get(username='john')
        }
    ]
    for recipe_data in dinner_recipes:
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            description=recipe_data['description'],
            instructions=recipe_data['instructions'],
            category=recipe_data['category'],
            user=recipe_data['user']
        )
        recipe.slug = slugify(recipe.title)
        recipe.save()

    dessert_recipes = [
        {
            'title': 'Chocolate Cake',
            'description': 'A classic dessert.',
            'instructions': 'Mix the batter and cook in a pan.',
            'category': dessert,
            'user': User.objects.get(username='jane')
        },
        {
            'title': 'Apple Pie',
            'description': 'A classic dessert.',
            'instructions': 'Mix the batter and cook in a pan.',
            'category': dessert,
            'user': User.objects.get(username='bob')
        }
    ]
    for recipe_data in dessert_recipes:
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            description=recipe_data['description'],
            instructions=recipe_data['instructions'],
            category=recipe_data['category'],
            user=recipe_data['user']
        )
        recipe.slug = slugify(recipe.title)
        recipe.save()

    print('Recipes created successfully.')
    
   

    # cats = {
    #         'Breakfast Recipes': {},
    #         'Lunch Recipes': {},
    #         'Dinner Recipes': {},
    #         'Dessert Recipes':{} }

    # for cat, cat_data in cats.items():
    #     c = add_cat(cat, cat_data['views'], cat_data['likes'])
    #     for p in cat_data['pages']:
    #         add_page(c, p['title'], p['url'])

#     for c in Category.objects.all():
#         for p in Page.objects.filter(category=c):
#             print(f'- {c}: {p}')


# def add_page(cat, title, url, views=0):
#     p = Page.objects.get_or_create(category=cat, title=title)[0]
#     p.url=url
#     p.views=random.randint(1, 100)
#     p.save()
#     return p




# def add_cat(name, views, likes):
#     c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
#     c.save()
#     return c


if __name__ == '__main__':
    print('Starting rmr population script...')
    populate()
