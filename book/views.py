from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

book_item=[
    {"id":1,"name":"compound effect","writer":"darren hardey"}
]

def books(request):
    data=""
    for item in book_item:
        data=data+f"id:{item['id']} , name:{item['name']} , writer:{item['writer']}"+"<br>"
    return HttpResponse(data)
def detail(request):
    return HttpResponse("book details")