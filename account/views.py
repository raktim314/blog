from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from account.forms import SignUpForm


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_form_db()
            user.profile.birth_date = form.cleaned_data_get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request,  user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', {'form': form})




