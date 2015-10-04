from django.shortcuts import redirect, render
from django.contrib.auth.views import login as auth_login
from accounts.forms import QuizAuthenticationForm, SignupForm, EmailUserCreationForm
from django.contrib.auth.forms import UserCreationForm


def login(request):
    return auth_login(request, authentication_form=QuizAuthenticationForm)


def signup(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            next_url = request.GET.get('next', 'magazine:index')
            return redirect(next_url)
    else:
        form = EmailUserCreationForm()
    return render(request, 'accounts/signup.html', {
        'form': form,
        })
