from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate, logout
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
# Create your views here.

class UpdateAll(UpdateView):
    model = ''
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    template_name_suffix = '_form'



# class HomePage(TemplateView):
#     template_name = 'index.html'





def homepage(request):
    return render(request, "myprint/index.html")



def gift_productpage(request):
    return render(request, "myprint/gift_products.html")

def product(request):
    return render(request, 'myprint/products.html')

    
def top_product(request):
    return render(request, 'myprint/top_products.html')






def user_order_view(request):
    if request.method == 'POST':
        print("POST----> ", request.POST)
        form = OrderForm(request.POST)
        form.save()
        # if form:
        #     form.save()
        # else:
        #     return render(request, template_name='layout.html', context={'form': form})
        
    else:
        print("GET ---> ", request.method)
    context={'form': form}
    return render(request, template_name='layout.html', context=context)

def logoutView(request):
    logout(request)
    return redirect('login')