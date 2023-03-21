from django.urls import path
from rmr import views


app_name = 'rmr'

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('userprofiles/<str:username>/', views.userprofile, name='userprofile'),
    path('userprofiles/<str:username>/add_recipe/', views.add_recipe, name='add_recipe'),
    path('userprofiles/<str:username>/<slug:slug>/', views.delete_recipe, name='delete_recipe'),
    path('category/<slug:category_name_slug>/<slug:recipe_title_slug>/',
         views.show_recipe, name='show_recipe'),
    path('goto/', views.goto_url, name='goto'),
    path('search/', views.search, name='search'),
    path('get_recipe_data/<int:recipe_id>/', views.get_recipe_data, name='get_recipe_data'),

]