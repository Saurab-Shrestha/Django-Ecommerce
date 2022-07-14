from django.contrib.auth import login
from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.contrib.auth.decorators import login_required
from product.models import Category
# Create your views here.
def signup(request):
    categories = Category.objects.all()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()

    return render(request, 'customer/signup.html', {'form':form,'categories':categories})

@login_required
def profile(request):
    categories = Category.objects.all()
    return render(request,'customer/profile.html',{'categories':categories})


@login_required
def edit_profile(request):
    categories = Category.objects.all()
    if request.method == "POST":
        user = request.user
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.email = request.POST.get('email')

        user.save()
        return redirect('profile')


    return render(request,'customer/edit-profile.html',{'categories':categories})