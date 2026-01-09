from django.shortcuts import render
from .forms import input_form 
# Create your views here.
def home(request):
    good=input_form()

    return render(request,'input.html',{'form':good})