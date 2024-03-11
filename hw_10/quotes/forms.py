from django.forms import ModelForm, CharField, TextInput, DateField, ModelChoiceField, ModelMultipleChoiceField, CheckboxSelectMultiple

from .models import Author, Tag, Quote


class QuoteForm(ModelForm):
    
    quote = CharField()
    tags = ModelMultipleChoiceField(queryset=Tag.objects.all(), widget=CheckboxSelectMultiple)
    author = ModelChoiceField(queryset=Author.objects.all())

    class Meta:
        model = Quote
        fields = ['quote', 'tags', 'author']


class AuthorForm(ModelForm):

    fullname = CharField(max_length=100, required=True, widget=TextInput())
    born_date = DateField()
    born_location = CharField()
    description = CharField()

    class Meta:
        model = Author
        fields = ['fullname', 'born_date', 'born_location', 'description']
