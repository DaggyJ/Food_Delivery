from django.shortcuts import render,redirect
from django.views import View
from . import models
from . import forms
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'ecomapp/index.html')

def about(request):
    return render(request, 'ecomapp/about.html')

def contact(request):
    return render(request, 'ecomapp/contact.html')


class CategoryView(View):
    def get(self, request, val):
        product = models.Product.objects.filter(category=val)
        title = models.Product.objects.filter(category=val).values('title')
        return render(request, 'ecomapp/category.html', locals())
    
class CategoryTitle(View):
    def get(self, request, val):
        product = models.Product.objects.filter(title=val)
        title = models.Product.objects.filter(category=product[0].category).values('title')
        return render(request, 'ecomapp/category.html', locals())

class ProductDetailView(View):
    def get(self, request, pk):
        product = models.Product.objects.get(pk=pk)
        return render(request, 'ecomapp/productdetail.html',locals())
    
class CustomerRegistrationView(View):
    def get(self, request):
        form = forms.CustomUserCreationForm()
        return render(request, 'ecomapp/registration.html', locals())
    
    def post(self, request):
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful!')
            return redirect('home')
        else:
            messages.warning(request, 'Incorrect input!, Please try again')
            return render(request, 'ecomapp/registration.html', locals())
        

class ProfileView(View):
    def get(self, request):
        form = forms.CustomerProfileForm()
        return render(request, 'ecomapp/profile.html',locals())
    def post(self, request):
        form = forms.CustomerProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            zipcode = form.cleaned_data['zipcode']

            reg = models.Customer(name=name,locality=locality,city=city,mobile=mobile,zipcode=zipcode)
            reg.save()
            messages.success(request, 'Congratulations!, your profile is successfully saved')
        else:
            messages.warning(request, 'Incorrect input!, Please try again')
        return render(request, 'ecomapp/profile.html',locals())
                  