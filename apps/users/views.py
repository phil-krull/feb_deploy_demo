from django.shortcuts import render, HttpResponse, redirect
from .models import User

# Create your views here.

def index(request):
    context = {
        'users': User.objects.get_users()
    }
    return render(request, 'users/index.html', context)

def new(request):
    return render(request, 'users/new.html')

def edit(request, user_id):
    context = {
        'user': User.objects.get_user(user_id)
    }
    return render(request, 'users/edit.html', context)

def show(request, user_id):
    context = {
        'user': User.objects.get_user(user_id)
    }
    return render(request, 'users/show.html', context)

def create(request):
    print 'from users:create'
    if request.method == 'POST':
        print request.POST
        # send post info to the UserManager through the User class
        user_just_created = User.objects.add_user(request.POST)
        request.session['user_id'] = user_just_created['id']
    return redirect('users:index')

def destroy(request, user_id):
    print 'from users:destory'
    User.objects.delete_user(user_id)
    return redirect('users:index')

def update(request, user_id):
    print 'from user:update'
    User.objects.update_user(user_id, request.POST)
    return redirect('users:show', user_id=user_id)