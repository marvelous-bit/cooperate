from django.forms import ModelForm
from .models import ContactModel, Comment
from django import forms

class CONTACTFORM(forms.ModelForm):
    class Meta:
        model = ContactModel
        fields = ('name', 'subject', 'email', 'messagess')
        exclude = ['created']
        widgets={
            'name': forms.TextInput(attrs={'class':"form-control"}),
            'subject': forms.TextInput(attrs={'class':"form-control"}),
            'email': forms.TextInput(attrs={'class':"form-control"}),
            'messagess': forms.TextInput(attrs={'class':"form-control"}),
            
        }



class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets={
            'name': forms.TextInput(attrs={'class':"form-control"}),
            'email': forms.TextInput(attrs={'class':"form-control"}),
            'body': forms.TextInput(attrs={'class':"form-control"}),
            
        }

