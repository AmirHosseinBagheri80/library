from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Create your views here.

def google(request):
    return HttpResponseRedirect("https://www.google.com")
def list_st(request):
    url=reverse('book-list')
    return HttpResponseRedirect(url)

book_item=[
    {"id":1,"name":"compound effect","writer":"darren hardey"},
    {"id":2,"name":"Mein Kampf","writer":"Adolf Hittler"}
]

def books(request):
    data=""
    for item in book_item:
        url=reverse('book-detail',args=[item['id']])
        data=data+f"<a href='{url}' target='_blank'>{item['name']}</a>"+"<br>"
    return HttpResponse(data)

def standard_book_list(request):
    return render(request,'book/list.html')

def detail(request,id):
    return HttpResponse(f"book details of book:{id}")