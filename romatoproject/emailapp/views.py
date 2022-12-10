
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from .forms import RegisterForm
from django.contrib import messages
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from emailapp.models import *
# Create your views here.
def home(request):
    category = Category.objects.all()
    return render(request,'home.html',{"category":category})


#register
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'')
    else:
        form = RegisterForm()

    context = {'form': form}
    return render(request, 'register.html', context)




@csrf_exempt
@login_required
def send(request):
    if request.method == 'POST':
        email = Email()
        email.to = request.POST['to']
        email.frm = request.user
        email.subject = request.POST['subject']
        email.body = request.POST['body']
        category = request.POST['category']

        email.category = Category.objects.get(name=category)
        email.save()
        
        messages.success(request,'Email Has Been Sent !')
       
    return render(request,'home.html')

@login_required
def compose(request):
 
    category = Category.objects.all()


    return render(request,'send.html',{'category':category})


@login_required
def email_list(request):
    email = Email.objects.all()
    category = Category.objects.all()
    return render(request,'email_list.html',{'email':email,'category':category})

#email_detail
@login_required
def email_detail(request,id):
    ed = get_object_or_404(Email, id=id)
    print('id',id,ed)
    return render(request, 'email_detail.html',{'ed':ed})

