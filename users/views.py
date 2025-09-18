from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .forms import SignUpForm

def home(request):
    return render(request, 'users/home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # Encrypt password
            user.save()
            messages.success(request, "Account created successfully!")
            login(request, user)
            return redirect('home')  # redirect to home page
    else:
        form = SignUpForm()
    
    return render(request, 'users/signup.html', {'form': form})

