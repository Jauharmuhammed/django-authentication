
from django. shortcuts import redirect, render
from django.contrib.auth import authenticate,login, logout
from django.views.decorators.cache import never_cache
from django.contrib import messages


@never_cache
def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method == 'POST':
            username = request.POST['username']
            password= request.POST['password']
            
            user= authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")
                return redirect(login_page)
        return render(request, 'login/index.html')

def logout_page(request):
    logout(request)
    return redirect('login')

