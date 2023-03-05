import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'rate_my_recipe_project.settings')
import django
django.setup()
from rmr.models import Category, Page, Recipe


def populate():
    
   

    cats = {
            'Breakfast Recipes': {},
            'Lunch Recipes': {},
            'Dinner Recipes': {},
            'Dessert Recipes':{} }

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
