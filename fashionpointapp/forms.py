from django import forms
from fashionpointapp.models import Post,Category



class PostForm(forms.ModelForm):
    category = forms.ModelMultipleChoiceField(queryset=Category.objects.all(),required=False )
    description = forms.CharField(max_length=128,required=False)
    photo = forms.ImageField()
    date = forms.DateTimeField(widget=forms.HiddenInput(),required=False)
    avgRating = forms.FloatField(widget=forms.HiddenInput(),required=False,initial=0)
    class Meta:
        model = Post
        fields=['photo','description','category']
