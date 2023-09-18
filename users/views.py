from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):

    # when form is submitted
    if request.method == 'POST':
        # now validate the form first by passing data in form
        form = RegisterForm(request.POST)
        if form.is_valid():

            # save user in database
            form.save()

            # get form data
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}, your account is created.')
            return redirect('login')

    else:
        form = RegisterForm()

    context = {
        "form": form
    }

    return render(request, 'users/register2.html', context)


# profile view
@login_required
def profile(request):
    return render(request, 'users/profile.html')


# def register(request):
#     if request.method == 'POST':

#         # if form.is_valid():
#         username = request.POST['username']
#         messages.success(request, f'Welcome {username}! Your account is activated!')

#         return redirect('food:items')
#     else:
#         form = UserCreationForm()

#     context = {
#         'form' : form
#     }
#     return render(request, 'users/register.html', context)