from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from rmr.models import Category, UserProfile, Recipe, Rating
from django.contrib.auth.models import User


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128,
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)


class RecipeForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0, required=False)
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'image', 'instructions', 'category', 'views')

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ( )


class RatingForm(forms.ModelForm):
    comment = forms.CharField(widget=forms.Textarea(attrs={
        'cols': 200,
        'rows': 3,
        'style': 'width: 100%',
        'required': False,
        'placeholder': "Comment...",}), label="")
    rating = forms.ChoiceField(choices=[[5, "5"], [4, "4"], [3, "3"], [2, "2"], [1, "1"]])

    class Meta:
        model = Rating
        fields = ('rating', 'comment')






