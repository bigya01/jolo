from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import LoginForm, SignUpForm
from shop.models import Shop


def login_view(request):
    if request.user.id:
        if Shop.objects.filter(user_id = request.user.id).exists():
            shop_slug = Shop.objects.get(user_id = request.user.id).slug
            return redirect(f"/dashboard/{shop_slug}/")
        return redirect("/shop/setup")
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if Shop.objects.filter(user_id = request.user.id).exists():
                    shop_slug = Shop.objects.get(user_id = request.user.id).slug
                    return redirect(f"/dashboard/{shop_slug}/")
                return redirect("/shop/setup")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'
    
    return render(request, "accounts/login.html", {"form": form, "msg": msg})

# Create your views here


def register_user(request):
    if request.user.id:
        if Shop.objects.filter(user_id = request.user.id).exists():
            shop_slug = Shop.objects.get(user_id = request.user.id).slug
            return redirect(f"/dashboard/{shop_slug}/")
        return redirect("/shop/setup")
    msg = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = 'User created - please <a href="/shop/setup">login</a>.'
            success = True
            return redirect("/shop/setup")
            #return render(request, "accounts/setup_shop.html", {})
        else:
            msg = 'Form is not valid'
    else:
        form = SignUpForm()

    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})


# def setup_shop(request):
#     return render(request, "accounts/setup_shop.html", {})