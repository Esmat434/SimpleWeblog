from functools import wraps
from django.shortcuts import redirect

def login_required(view_fun):
    @wraps(view_fun)
    def wrapper(request,*args,**kwargs):
        if not request.user.is_authenticated:
            return redirect('login')
        return view_fun(request,*args,**kwargs)
    return wrapper

def logout_required(view_func):
    @wraps(view_func)
    def wrapper(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request,*args,**kwargs)
    return wrapper