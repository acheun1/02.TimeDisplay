from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
# djangohw02: time stamp
def index(request):
    context = {
        "time": strftime("%Y-%m-%d %H:%M %p", gmtime())
    }
    return render(request,'app_01/index.html', context)