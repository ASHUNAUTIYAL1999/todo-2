from django.shortcuts import render
from . forms import login
# Create your views here.
def home(request):
    form=login()
    return render(request,'login.html',{'form':form})