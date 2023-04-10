from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.

# View de Home

def home(request):
    return TemplateResponse(request, 'home.html')