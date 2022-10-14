from django.shortcuts import render
from AHT20.models import Data

# Create your views here.
# ~/projects/django-web-app/merchex/listings/views.py

def hello(request):
    datas = Data.objects.all()
    return render(request, 'AHT20/hello.html', {"datas" : datas})

