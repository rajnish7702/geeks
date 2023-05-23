from django.shortcuts import render
from Geeks.forms import GeeksForms
# Create your views here.

def home(request):
    context = {}
    form = GeeksForms(request.POST or None)
    context['form']=form
    return render(request, 'home.html',context)
