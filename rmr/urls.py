from django.urls import path
from rmr import views


app_name = 'rmr'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('category/breakfast-recipes/', views.breakfast, name='breakfast'),
    path('category/lunch-recipes/', views.lunch, name='lunch'),
    path('category/dinner-recipes/', views.dinner, name='dinner'),
    path('category/dessert-recipes/', views.dessert, name='dessert'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),

    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('userprofiles/<str:username>/', views.userprofile, name='userprofile'),
    path('userprofiles/<str:username>/add_recipe/', views.add_recipe, name='add_recipe'),
    path('category/<slug:category_name_slug>/<slug:recipe_title_slug>/',
         views.show_recipe, name='show_recipe'),
    path('goto/', views.goto_url, name='goto'),
    path('search/', views.search, name='search'),

]