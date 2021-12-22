from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserForm

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView
from django.urls import reverse_lazy


# Create your views here.
def welcomefunc(request):
    return render(request, 'welcome.html', {})

def signupfunc(request):
    user = UserModel()
    form = UserForm()
    if request.method == 'POST':
        username2 = request.POST['username']#DBからデータ項目、インデックスを引っ張り出すイメージ
        password2 = request.POST['password']
        #signupで重複した際、エラー表示
        try:#新規登録した時にアカウントがすでに存在している場合
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error':'このユーザは既に存在しているわ。他のにして頂戴。'})
        except:#存在していない場合
            user = User.objects.create_user(username2, '', password2)#ここで初めて新規アカウントが作られる！
            if request.method == 'POST':
                form = UserForm(request.POST)
                form.username = request.user.get_username()
                if form.is_valid():
                    form.save()
            return redirect('login')
        #functionを使う場合は、renderでtemplate(引数2)とDB(引数3)を組み合わせる
    return render(request, 'signup.html', {'some':100})

def loginfunc(request):
    if request.method == 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request, username=username2, password=password2)
        if user is not None:#そのユーザがいる場合はログイン処理をする
            user_id = request.user.id
            users = UserModel.objects.all()
            login(request, user)
            return redirect('home')
            #return render(request, 'home.html', {'username':username2, 'users':users, 'user_id':user_id,})
        else:#いない場合は
            return render(request, 'login.html', {'error':'名前かパスワードが間違っていない？'})
    return render(request, 'login.html', {})

def logoutfunc(request):
    return redirect('welcome')

def homefunc(request):
    
    #context = {'username':username}
    username = request.user.get_username()
    user_id = request.user.id
    print("user-name:{} type:{}".format(username,type(username)))
    print("user-id:{} type:{}".format(request.user.id, type(request.user.id)))
    #main.user = UserModel.objects.get(id=request.user.id)
    users = UserModel.objects.all()
    #print(user.id)
    form = UserForm()
    if request.method == 'POST':
        #username = request.POST['username']
        form = UserForm(request.POST)
        form.username = request.user.get_username()

        if form.is_valid():
            form.save()
        return redirect('home.html')
    context = {'username':username, 'users':users, 'user_id':user_id, 'form':form}
    return render(request, 'home.html', context)


def createfunc(request):
    username = request.user.get_username()
    print(username)
    print(request.user.id)

    user = UserModel.objects.get(pk=request.user.id)
    #user = UserModel.objects.all()
    #form = UserForm(instance=user)
    form = UserForm(instance=user)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        #form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('home')
    context = {'username':username, 'user':user, 'form':form}
    return render(request, 'create.html', context)

def viewfunc(request, pk):
    user = UserModel.objects.get(id=pk)
    context = {'user':user}
    return render(request, 'view.html', context)