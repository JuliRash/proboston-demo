from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from example.forms import UserInformationForm
from example.models import UserInformation


def index(request):
    form = UserInformationForm()
    if request.method == 'POST':
        form = UserInformationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'User Information saved successfully to the database')
            form = UserInformationForm()
    return render(request, 'index.html', {'form': form})
