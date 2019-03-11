from django import forms
from fashionpointapp.models import Post,Category,UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    description = forms.CharField(max_length=256)
    avgRating = forms.FloatField(widget=forms.HiddenInput(), initial=0)
    photo = forms.ImageField()
    date = forms.DateTimeField(widget=forms.HiddenInput())
    category = forms.MultipleChoiceField(choices=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    class Meta:
        model = Post
        fields = ('description','photo','category')