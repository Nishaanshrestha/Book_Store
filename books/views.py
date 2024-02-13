from django.shortcuts import render
from django.http import Http404
from. models import Book

# Create your views here.
def index(request):
    books=Book.objects.all()
    return render(request,'index.html',{'books':books})

def book_detail(request,slug):
   try:
        book=Book.objects.get(slug=slug)
        return render(request,'book_details.html',{'book':book})
   except:
       raise Http404('404 not found')
