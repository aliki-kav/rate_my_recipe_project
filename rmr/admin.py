from django.contrib import admin
from rmr.models import Category, UserProfile, Recipe, Rating

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

class RatingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'rating_stars': ('rating',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(UserProfile)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Rating, RatingAdmin)