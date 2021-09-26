from django import forms
from app.models import Book
from app.models import Author

class CustomM2MField(forms.ModelMultipleChoiceField):
    def label_from_instance(self, author):
        return '%s' % author.name

class CreateBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors']
    
    title = forms.CharField()
    authors = CustomM2MField(
        queryset=Author.objects.all(),        
        widget=forms.CheckboxSelectMultiple
    )