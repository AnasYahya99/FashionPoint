from django import forms
from fashionpointapp.models import Post,Category



class PostForm(forms.ModelForm):
    description = forms.CharField(max_length=256)
    avgRating = forms.FloatField(widget=forms.HiddenInput(), initial=0)
    photo = forms.ImageField()
    date = forms.DateTimeField(widget=forms.HiddenInput())
    category = forms.MultipleChoiceField(choices=Category.objects.all(), widget=forms.CheckboxSelectMultiple, required=False)
    #userPofile = forms.HiddenInput(intial = user)
    class Meta:
        model = Post
        fields = ('description','photo','category')