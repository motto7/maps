from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User  #  FIXME : 그다지 좋지 않은 방법...?


class QuizAuthenticationForm(AuthenticationForm):
    answer = forms.CharField(label='3+3=?')

    def clean_answer(self):
        answer = self.cleaned_data.get('answer', '')
        if answer != '6':
            raise forms.ValidationError('땡 !!!')


class SignupForm(forms.Form):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data.get('username','')
        if username:
            if User.objects.filter(username=username).exists():
                raise forms.ValidationError("이미 있는 아이디ㅇㅇ")

        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if  password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password1']

        user=User()
        user.username = username
        user.password = password
        user.set_password(password)  #  해싱

        if commit:
            user.save()

        return user


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        if email:
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('이미등록된 이메일입니다. ')
        return email

    def save(self, commit=True):

        user= super(EmailUserCreationForm,self).save(commit=False)

        user.email=email = self.cleaned_data['email']

        if commit:
            user.save()
        return user