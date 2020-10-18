from django.http import HttpResponse,Http404
from django.shortcuts import render
from .models import Voter
# Create your views here.

def home(request):
    # return HttpResponse("<h1>hiyah !</h1>")
    return render(request,"home.html",{})

def view_candidates(request,pk):
    try:
        obj = Voter.objects.get(pk=pk)
    except Voter.DoesNotExist:
        raise Http404
    return HttpResponse(f"username : {obj.username}"+"<br>"+f"number : {obj.number}")