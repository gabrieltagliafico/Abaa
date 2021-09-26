
from typing import ContextManager
from django.shortcuts import render

def landingView(request):
    return render(request,'landing/landing.html')