#from modi.models import modi
from django.shortcuts import render, redirect
from django.http import HttpResponse
#from modi.forms import modiForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'template/index.html')