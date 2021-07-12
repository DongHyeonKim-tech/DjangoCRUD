from django import forms
from .models import BidCrawling


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = BidCrawling
        fields = ['title', 'writer', 'bid', 'isbn']


class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = BidCrawling
        fields = ['title', 'writer', 'bid', 'isbn', 'intro']