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
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),required=False )
    description = forms.CharField(max_length=128,required=False)
    photo = forms.ImageField()
<<<<<<< HEAD
    date = forms.DateTimeField(widget=forms.HiddenInput(),required=False)
    avgRating = forms.FloatField(widget=forms.HiddenInput(),required=False,initial=0)
=======
    date = forms.DateTimeField(widget=forms.HiddenInput())
    category = forms.MultipleChoiceField(choices=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
>>>>>>> aa431a088a0f9f258115b64f04f71426d52bab1c
    class Meta:
        model = Post
        fields=['photo','description','category']
