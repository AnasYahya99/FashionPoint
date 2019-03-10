from django import forms
from fashionpointapp.models import Post,Category
class PostForm(forms.ModelForm):
    description = forms.CharField(max_length=256, help_text="Write a caption..")
    avgRating = forms.floatField(widget=forms.HiddenInput(), initial=0)
    photo = forms.ImageField(upload_to="posts/")
    date = forms.DateTimeField(widget=forms.HiddenInput(),auto_now=True)
    cats = forms.ModelChoiceField(queryset=Category.object.all())
    class Meta:
        model = Post
        fields = ('description','photo','cats')