from django.shortcuts import render,redirect
from django.http import HttpResponse,request,HttpResponseRedirect
from django.template.loader import get_template
from .forms import Msgform,InfoForm
from . import models
from django.contrib import messages
from django.utils import timezone
from django.contrib import auth
from . import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
    try:
        msgs = models.msg.objects.order_by('-ddate')
        count = 0
    except:
         messages.add_message(request,messages.WARNING,'出现未知错误...')
    for msg in msgs:
        msg.ddate = (timezone.now() - msg.ddate ).total_seconds()
        count = count + 1
    template = get_template('index.html')
    messages.get_messages(request)
    html = template.render(locals())
    return HttpResponse(html)

def post(request):
    if request.method == 'POST':
        msg = Msgform(request.POST)
        if msg.is_valid:
            messages.add_message(request,messages.SUCCESS,'成功发布!')
            models.msg.objects.create(name=request.user,text=request.POST['text'])
            return HttpResponseRedirect('/')
    else:
        msg = Msgform()

    template = get_template('post.html')
    html = template.render(request = request,context =locals())
    return HttpResponse(html)
# def index(request,pid = None,del_pass=None):
#     if request.user.is_authenticated:
#         username = request.user.username
#         useremail = request.user.email
#     try:
#         user = models.User.objects.get(username = username )
#         diaries = models.Diary.objects.filter(user = user).order_by('-ddate')
#     except:
#         pass
#     messages.get_messages(request)
#     template = get_template('index.html')
#     html = template.render(locals())
#     return HttpResponse(html)


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password']
            user = authenticate(username=login_name,password = login_password)
            if user:
                if user.is_active:
                    auth.login(request,user)
                    print('ds')
                    messages.add_message(request,messages.SUCCESS,'成功登陆')
                    return HttpResponseRedirect('/')
                else:
                    messages.add_message(request,messages.WARNING,'账号尚未启用')
            else:
                messages.add_message(request, messages.WARNING, '登录失败')
        else:
            messages.add_message(request,messages.INFO,'请检查输入的字段内容')
    else:
        print('2')
        login_form = forms.LoginForm()
    template = get_template('login.html')
    html = template.render(context=locals(),request = request)
    return HttpResponse(html)

def logout(request):
    auth.logout(request)
    messages.add_message(request,messages.INFO,'成功注销')
    return HttpResponseRedirect('/')

@login_required(login_url='/login/')
def information(request):
    if request.method == 'POST':
        info_form = InfoForm(request.POST)
        if info_form.is_valid:
            user = request.user
            data = request.POST['data']
            sexy = request.POST['sexy']
            love = request.POST['love']
            try:
                exsit= User.objects.get(username=love)
            except:
                messages.add_message(request, messages.WARNING, '不存在')
                return redirect('/information')
            else:
                info_form = models.information.objects.create(user=user,data=data,sexy=sexy,love=love)
                info_form.save()
        else:
            messages.add_message(request, messages.WARNING, '修改失败')
    else:
        info_form = InfoForm()
    template = get_template('information.html')
    html = template.render(context=locals(),request = request)
    return HttpResponse(html)
