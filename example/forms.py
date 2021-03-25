from django import forms

from example.models import UserInformation


class UserInformationForm(forms.ModelForm):

    field_style = 'form-control'

    name = forms.CharField(
        widget=forms.TextInput(attrs={'class': field_style,
                                      'placeholder': 'Name'}))

    email = forms.CharField(
        widget=forms.EmailInput(attrs={'class': field_style,
                                       'placeholder': 'Email Address'}))

    ico = forms.CharField(
        widget=forms.TextInput(attrs={'class': field_style,
                                      'placeholder': 'ICO'}))

    class Meta:
        model = UserInformation
        fields = ['name', 'email', 'ico']
