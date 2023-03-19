import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rate_my_recipe_project.settings')
import django
django.setup()
from django.contrib.auth.models import User

from rmr.models import Category, Page, Recipe, UserProfile, Rating
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
            'user': User.objects.get(username='john'),
            'image': 'images/pancakes.jpg'
        },
        {
            'title': 'Omelette',
            'description': 'A classic breakfast dish!',
            'instructions': 'Whisk the eggs and cook in a pan with toppings.',
            'category': breakfast,
            'user': User.objects.get(username='jane'),
            'image': 'images/omlette.jpg'
        }
    ]
    for recipe_data in breakfast_recipes:
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            description=recipe_data['description'],
            instructions=recipe_data['instructions'],
            category=recipe_data['category'],
            user=recipe_data['user'],
            image=recipe_data['image']
        )
        recipe.slug = slugify(recipe.title)
        recipe.save()

    lunch_recipes = [
        {
            'title': 'Grilled Cheese',
            'description': 'A classic sandwich!',
            'instructions': 'Put cheese between bread and grill.',
            'category': lunch,
            'user': User.objects.get(username='john'),
            'image': 'images/grilled_cheese.jpg'
        },
        {
            'title': 'BLT',
            'description': 'Bacon, lettuce, and tomato!',
            'instructions': 'Cook the bacon and assemble with lettuce and tomato on bread.',
            'category': lunch,
            'user': User.objects.get(username='jane'),
            'image': 'images/blt.jpg'
        }
    ]
    for recipe_data in lunch_recipes:
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            description=recipe_data['description'],
            instructions=recipe_data['instructions'],
            category=recipe_data['category'],
            user=recipe_data['user'],
            image=recipe_data['image']
        )
        recipe.slug = slugify(recipe.title)
        recipe.save()

    dinner_recipes = [
        {
            'title': 'Spaghetti Bolognese',
            'description': 'A classic Italian pasta dish.',
            'instructions': 'Boil the spaghetti. Cook the beef. Mix everything together.',
            'category': dinner,
            'user': User.objects.get(username='bob'),
            'image': 'images/bolognese.jpg'
        },
        {
            'title': 'Chicken Curry',
            'description': 'A spicy Indian dish.',
            'instructions': 'Cook the chicken. Mix with the curry sauce. Serve with rice.',
            'category': dinner,
            'user': User.objects.get(username='john'),
            'image': 'images/chicken_curry.jpg'
        }
    ]
    for recipe_data in dinner_recipes:
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            description=recipe_data['description'],
            instructions=recipe_data['instructions'],
            category=recipe_data['category'],
            user=recipe_data['user'],
            image=recipe_data['image']
        )
        recipe.slug = slugify(recipe.title)
        recipe.save()

    dessert_recipes = [
        {
            'title': 'Chocolate Cake',
            'description': 'A classic dessert.',
            'instructions': 'Mix the batter and cook in a pan.',
            'category': dessert,
            'user': User.objects.get(username='jane'),
            'image': 'images/cake.jpg'
        },
        {
            'title': 'Apple Pie',
            'description': 'A classic dessert.',
            'instructions': 'Mix the batter and cook in a pan.',
            'category': dessert,
            'user': User.objects.get(username='bob'),
            'image': 'images/ApplePie.jpg'
        }
    ]
    for recipe_data in dessert_recipes:
        recipe = Recipe.objects.create(
            title=recipe_data['title'],
            description=recipe_data['description'],
            instructions=recipe_data['instructions'],
            category=recipe_data['category'],
            user=recipe_data['user'],
            image=recipe_data['image']
        )
        recipe.slug = slugify(recipe.title)
        recipe.save()

    print('Recipes created successfully.')


if __name__ == '__main__':
    print('Starting rmr population script...')
    populate()