from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
# from .forms import MyUserCreationForm

# Create your views here.
def user_login(request):
    return render(request,'login.html')

def user_register(request):
    # form = MyUserCreationForm()
    # context={'form':form}
    return render(request,'user_registeration.html',context)
