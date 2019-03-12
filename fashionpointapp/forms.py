from django import forms
from fashionpointapp.models import Post,Category,UserProfile
from django.contrib.auth.models import User
from django.forms.widgets import DateInput


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture','dateOfBirth')
        labels = {
            'dateOfBirth': ('D.O.B'),
        }
        widgets = {
            'dateOfBirth': DateInput(attrs={'type': 'date'})
        }
class PostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(Category.objects.all(), required=False)
    description = forms.CharField(max_length=128,required=False)
    photo = forms.ImageField()
    avgRating = forms.FloatField(widget=forms.HiddenInput(),required=False,initial=0)
    date = forms.DateTimeField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = Post
        fields=['photo','description','category']