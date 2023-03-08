from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

from rmr.models import Category, Page, UserProfile, Recipe, Rating
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


class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Page
        exclude = ('category',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        if url and not url.startswith('http://') and not url.startswith('https://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        return cleaned_data


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


class RatingForm(forms.ModelForm):
    comment = forms.CharField(max_length=1000, help_text="Please enter your comment: ", required=False)
    rating = forms.IntegerField(validators=[MinValueValidator(0),
                                MaxValueValidator(5)], help_text="Rate the recipe: ")

    class Meta:
        model = Rating
        fields = ('rating', 'comment')


class RecipeForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Recipe
        fields = ('title', 'description', 'image', 'instructions', 'category', 'views')

