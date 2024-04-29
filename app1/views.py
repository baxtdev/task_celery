from django.shortcuts import render
from .tasks import add
from app2.models import Bid
# Create your views here.


def home(request):
    result = add(2,3)
    return render(request,'index.html',{'result':result,})

