from django.shortcuts import render,HttpResponse
from django.views.generic import View

# Create your views here.


class Home(View):
    def get(self,request):
        return HttpResponse('Hello Python')