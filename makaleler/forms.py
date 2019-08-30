from django import forms
from .models import Makale
class ArticleForm(forms.ModelForm):

    class Meta():

        model = Makale

        fields = ["title","content","article_media"]
