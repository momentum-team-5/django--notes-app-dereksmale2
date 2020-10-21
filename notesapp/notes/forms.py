from django import forms
from django.core.exceptions import ValidationError
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = [
            'title',
            'body',
        ]


class ContactForm(forms.Form):
    email = forms.EmailField(required=True)
    title = forms.CharField(required=True, max_length=255)
    body = forms.CharField(label="Your message", widget=forms.Textarea(attrs={'required': True}))


class SearchForm(forms.Form):
    SEARCH_TYPES_CHOICES = (
        ("starts with", "starts with"),
        ("includes", "includes"),
        ("exact match", "exact match"),
    )

    ORDER_CHOICES = (
        ("title", "title"),
        ("body", "body"),
    )

    title = forms.CharField(max_length=255, required=True)
    title_search_type = forms.ChoiceField(choices=SEARCH_TYPES_CHOICES, label="Search title for", widget=forms.RadioSelect, required=True)
    body = forms.CharField(widget=forms.Textarea, required=False)
    body_search_type = forms.ChoiceField(choices=SEARCH_TYPES_CHOICES, label="Search body for", widget=forms.RadioSelect, required=False)
    order_by = forms.ChoiceField(choices=ORDER_CHOICES, widget=forms.RadioSelect, required=True)
    
def clean(self):
    cleaned_data = super().clean()
    cleaned_title = cleaned_data['title']
    cleaned_body = cleaned_data['body']

    if cleaned_title or cleaned_body:
        return cleaned_data

    raise ValidationError('At least one search field must be specified', code='invalid')