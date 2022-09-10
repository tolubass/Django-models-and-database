import datetime

from django.contrib import messages
from django.shortcuts import render
# create your views here
from myapp.models import Books


def index(request):
    if request.method == 'POST':
        if request.POST.get('name'):
            #table = Books()
            #table.author = request.POST.get('name')
            #table.title = request.POST.get('title')
            #table.body = request.POST.get('body')
            #table.timestamp = datetime.date.today()
            #b = "It is very ok....";
            #table.objects.filter(body = b).update(title = request.POST.get('title'))
            #table.save()
            k = Books.objects.filter(author__contains=request.POST.get('name'))
            messages.success(request,"saved successfully")
            return render(request,"index.html",{"info" : k})
    n = Books.objects.all()[:10]
    return render(request,"index.html",{"info" : n})