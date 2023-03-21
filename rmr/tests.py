from django.test import TestCase
import os
from rmr.models import Recipe,Category,UserProfile
import importlib
from django.urls import reverse

FAILURE_HEADER = f"{os.linesep}{os.linesep}{os.linesep}================{os.linesep}TwD TEST FAILURE =({os.linesep}================{os.linesep}"
FAILURE_FOOTER = f"{os.linesep}"

class PopulationScriptTests(TestCase):
    def setUp(self):
        """
        Imports and runs the population script, calling the populate() method.
        """
        try:
            import populate_rmr
        except ImportError:
            raise ImportError(f"{FAILURE_HEADER}Could not import the populate_rmr. Check it's in the right location (the rate_my_recipe_project directory).{FAILURE_FOOTER}")
        
        if 'populate' not in dir(populate_rmr):
            raise NameError(f"{FAILURE_HEADER}The populate() function does not exist in the populate_rmr module. This is required.{FAILURE_FOOTER}")
        
        # Call the population script -- any exceptions raised here do not have fancy error messages to help readers.
        populate_rmr.populate()
        print("setup test")
    
    def test_users(self):
        users = UserProfile.objects.filter()
        users_len = len(users)
        users_strs = map(str, users)
        
        self.assertEqual(users_len, 3, f"{FAILURE_HEADER}Expecting 3 users to be created from the populate_rmr module; found {users_len}.{FAILURE_FOOTER}")
        self.assertTrue('john' in users_strs, f"{FAILURE_HEADER}The user 'John' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('jane' in users_strs, f"{FAILURE_HEADER}The user 'Jane' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('bob' in users_strs, f"{FAILURE_HEADER}The user 'Bob' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
    
    def test_recipes(self):
        recipes = Recipe.objects.filter()
        recipes_len = len(recipes)
        recipes_strs = map(str, recipes)
        
        self.assertEqual(recipes_len, 9, f"{FAILURE_HEADER}Expecting 8 recipes to be created from the populate_rmr module; found {recipes_len}.{FAILURE_FOOTER}")
        self.assertTrue('Pancakes' in recipes_strs, f"{FAILURE_HEADER}The recipe 'Pancakes' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('Omelette' in recipes_strs, f"{FAILURE_HEADER}The recipe 'Omelette' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('Grilled Cheese' in recipes_strs, f"{FAILURE_HEADER}The recipe 'Grilled Cheese' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('BLT' in recipes_strs, f"{FAILURE_HEADER}The recipe 'BLT' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('pasta carbonara' in recipes_strs, f"{FAILURE_HEADER}The recipe 'pasta carbonara' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('Spaghetti Bolognese' in recipes_strs, f"{FAILURE_HEADER}The recipe 'Spaghetti Bolognese' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('Chicken Curry' in recipes_strs, f"{FAILURE_HEADER}The recipe 'Chicken Curry' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('Chocolate Cake' in recipes_strs, f"{FAILURE_HEADER}The recipe 'Chocolate Cake' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('Apple Pie' in recipes_strs, f"{FAILURE_HEADER}The recipe 'Apple Pie' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
    
    def test_categories(self):
        categories = Category.objects.filter()
        categories_len = len(categories)
        categories_strs = map(str, categories)
        
        self.assertEqual(categories_len, 4, f"{FAILURE_HEADER}Expecting 4 categories to be created from the populate_rmr module; found {categories_len}.{FAILURE_FOOTER}")
        self.assertTrue('Breakfast' in categories_strs, f"{FAILURE_HEADER}The category 'Breakfast' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('Lunch' in categories_strs, f"{FAILURE_HEADER}The category 'Breakfast' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('Dinner' in categories_strs, f"{FAILURE_HEADER}The category 'Breakfast' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        self.assertTrue('Dessert' in categories_strs, f"{FAILURE_HEADER}The category 'Breakfast' was expected but not created by populate_rmr.{FAILURE_FOOTER}")
        
class ViewsTests(TestCase):
    def setUp(self):
        self.views_module = importlib.import_module('rmr.views')
        self.views_module_listing = dir(self.views_module)
        
    def test_views_exist(self):
        self.assertTrue('index' in self.views_module_listing, f"{FAILURE_HEADER}The index() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.index), f"{FAILURE_HEADER}Check that you have created the index() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('about' in self.views_module_listing, f"{FAILURE_HEADER}The about() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.about), f"{FAILURE_HEADER}Check that you have created the about() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('show_category' in self.views_module_listing, f"{FAILURE_HEADER}The show_category() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.show_category), f"{FAILURE_HEADER}Check that you have created the show_category() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('register' in self.views_module_listing, f"{FAILURE_HEADER}The register() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.register), f"{FAILURE_HEADER}Check that you have created the register() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('user_login' in self.views_module_listing, f"{FAILURE_HEADER}The user_login() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.user_login), f"{FAILURE_HEADER}Check that you have created the user_login() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('user_logout' in self.views_module_listing, f"{FAILURE_HEADER}The user_logout() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.user_logout), f"{FAILURE_HEADER}Check that you have created the user_logout() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('get_server_side_cookie' in self.views_module_listing, f"{FAILURE_HEADER}The get_server_side_cookie() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.get_server_side_cookie), f"{FAILURE_HEADER}Check that you have created the get_server_side_cookie() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('visitor_cookie_handler' in self.views_module_listing, f"{FAILURE_HEADER}The visitor_cookie_handler() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.visitor_cookie_handler), f"{FAILURE_HEADER}Check that you have created the visitor_cookie_handler() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('userprofile' in self.views_module_listing, f"{FAILURE_HEADER}The userprofile() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.userprofile), f"{FAILURE_HEADER}Check that you have created the userprofile() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('add_recipe' in self.views_module_listing, f"{FAILURE_HEADER}The add_recipe() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.add_recipe), f"{FAILURE_HEADER}Check that you have created the add_recipe() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('show_recipe' in self.views_module_listing, f"{FAILURE_HEADER}The show_recipe() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.show_recipe), f"{FAILURE_HEADER}Check that you have created the show_recipe() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('goto_url' in self.views_module_listing, f"{FAILURE_HEADER}The goto_url() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.goto_url), f"{FAILURE_HEADER}Check that you have created the goto_url() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('get_recipe_data' in self.views_module_listing, f"{FAILURE_HEADER}The get_recipe_data() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.get_recipe_data), f"{FAILURE_HEADER}Check that you have created the get_recipe_data() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
        self.assertTrue('search' in self.views_module_listing, f"{FAILURE_HEADER}The search() view for rmr does not exist.{FAILURE_FOOTER}")
        self.assertTrue(callable(self.views_module.search), f"{FAILURE_HEADER}Check that you have created the search() view correctly. It doesn't seem to be a function!{FAILURE_FOOTER}")
    
    def test_views_use_templates(self):
        self.assertTemplateUsed(self.client.get(reverse('rmr:index')), 'rmr/index.html', f"{FAILURE_HEADER}Your index() view does not use the expected index.html template.{FAILURE_FOOTER}")
        self.assertTemplateUsed(self.client.get(reverse('rmr:show_category', args=('breakfast',))), 'rmr/category.html', f"{FAILURE_HEADER}Your show_category() view does not use the expected category.html template.{FAILURE_FOOTER}")
        self.assertTemplateUsed(self.client.get(reverse('rmr:register')), 'rmr/register.html', f"{FAILURE_HEADER}Your register() view does not use the expected register.html template.{FAILURE_FOOTER}")
        self.assertTemplateUsed(self.client.get(reverse('rmr:login')), 'rmr/login.html', f"{FAILURE_HEADER}Your user_login() view does not use the expected login.html template.{FAILURE_FOOTER}")
        self.assertTemplateUsed(self.client.get(reverse('rmr:show_recipe', args=('breakfast', 'pancakes'))), 'rmr/recipe.html', f"{FAILURE_HEADER}Your show_recipe() view does not use the expected recipe.html template.{FAILURE_FOOTER}")
        self.assertTemplateUsed(self.client.get(reverse('rmr:search')), 'rmr/search.html', f"{FAILURE_HEADER}Your search() view does not use the expected search.html template.{FAILURE_FOOTER}")
