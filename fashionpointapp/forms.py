from django import forms
from fashionpointapp.models import Post,Category,UserProfile,Poll
from django.contrib.auth.models import User
from django.forms.widgets import DateInput
from django.utils.translation import ugettext_lazy as _

class UserForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name', 'password')
    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")
        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password do not match")

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture','dateOfBirth')
        labels = {
            'dateOfBirth': 'Date of Birth',
        }
        widgets = {
            'dateOfBirth': DateInput(attrs={'type': 'date'})
        }
class PostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(Category.objects.all(), required=False,label='Select categories:',
                                              help_text='hold control or </br> command to select </br> more than one')
    description = forms.CharField(max_length=128,required=False,label='Write a caption:')
    photo = forms.ImageField(label='Upload a picture:')
    avgRating = forms.FloatField(widget=forms.HiddenInput(),required=False,initial=0)
    date = forms.DateTimeField(widget=forms.HiddenInput(),required=False)
    class Meta:
        model = Post
        fields=['description','photo','category']

class PollForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(Category.objects.all(), required=False,label='Select categories:',
                                              help_text='hold control or </br> command to select </br> more than one')
    description = forms.CharField(max_length=128, required=False,label='Write a caption:')
    picture1 = forms.ImageField(label='Upload the first picture:')
    picture2=forms.ImageField(label='Upload the second picture:')
    date = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    picture1Clicks = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    picture2Clicks = forms.IntegerField(widget=forms.HiddenInput(),required=False)
    class Meta:
            model = Poll
            fields = ['description','picture1','picture2','category']
