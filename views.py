from audioop import reverse
from cgitb import reset
import email
from multiprocessing import context
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import *
from .forms import *
from django.contrib.auth.models import Group
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import PasswordResetForm

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.contrib import messages #import messages
from django.views.decorators.csrf import csrf_exempt
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





def login(request):
    return render(request, "accounts/login.html")


def password_new(request):
    return render(request, 'accounts/password_new.html')

def password_reset(request):
    return render(request, 'accounts/password_reset.html')

def user_orders(request):
    return render(request, 'accounts/user_orders.html')

def user_products(request):
    return render(request, 'accounts/user_products.html')




def user_login(request):
    if request.method == 'GET':
        form = UserLoginForm()
        context={'form': form}
        return render(request, template_name='accounts/login.html', context=context)
    else:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            full_name = request.POST['full_name']
            password = request.POST['password']

            user = authenticate(full_name=full_name, password=password)

            if user:
                login(request=request, user=user)
                return redirect('user_product')
            else:
                return render(request, template_name='accounts/login.html', context={'login': login})


def success(request):
    context = {}
    context['user'] = request.user
    return render(request, "myprint/products.html", context)



def logout(request):
    if request.method == "POST":
        logout(request)
        return HttpResponseRedirect(reverse('user_login'))






def register(request):
    
    if request.method == 'POST':
        print("POST----> ", request.POST)
        form = UserRegisterModelForm(request.POST)
        password = request.POST['password']
        confirm = request.POST['confirm']
        if form.is_valid() and password == confirm:
            print(password, confirm)
            form.save()
            user = form.instance
            user.groups.add(Group.objects.get(name='all'))
            user.save()

            login(request, user)

            return redirect('')
        else:
            return render(request, template_name='accounts/register.html', context={'form': form})
        
    else:
        print("GET ---> ", request.method)
        form = UserRegisterModelForm()
    context={'form': form}
    return render(request, template_name='accounts/register.html', context=context)





@csrf_exempt
def password_reset(request):
    reset = ResetForm()
    context = {}
    if request.method == "POST":
        print("POST ----------->",request.method)
        print("POST123 ----> ",request.POST.get('email'))
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        print("user", user)
        print("user email", user.email)
        if user is not None:
            print("---------------------------------sending --------------------------------------")
            send_mail(
                "This email is sending by moderator ",
                "dasjfdhkjfsdjd", 
                'alharamin1004@gmail.com' , 
                [user.email], 
                fail_silently=False
            )
    else:
        context = {'reset' : reset}
    return render(request, 'accounts/password_reset.html', context=context)





# def password_reset_request(request):
#     print("POST -------> ", request.POST)
    
# 	if request.method == "POST":
        
# 		email = request.data.get('email')
#         print("email---> ",email)

#     return 0
	# 	if password_reset_form.is_valid():
	# 		email = password_reset_form.cleaned_data['email']
	# 		associated_users = User.objects.filter(email=email)
	# 		if associated_users.exists():
	# 			for user in associated_users:
	# 				subject = "Password Reset Requested"
	# 				# email_template_name = "main/password/password_reset_email.txt"
	# 				c = {
	# 				"email":user.email,
	# 				'domain':'127.0.0.1:8000',
	# 				'site_name': 'Website',
	# 				"uid": urlsafe_base64_encode(force_bytes(user.pk)),
	# 				'token': default_token_generator.make_token(user),
	# 				'protocol': 'http',
	# 				}
	# 				# message = render_to_string(email_template_name, c)
                    
	# 				try:
	# 					send_mail(
    #                         subject, 
    #                         "dasd", 
    #                         'alharamin1004@gmail.com' , 
    #                         [user.email], 
    #                         fail_silently=False
    #                     )
                        
	# 				except BadHeaderError:
	# 					return HttpResponse('Invalid header found.')
						
	# 				messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
	# 				return redirect ("myprint:home")
	# password_reset_form = PasswordResetForm()
	# return render(request=request, template_name="accounts/password_reset.html", context={"password_reset_form":password_reset_form})