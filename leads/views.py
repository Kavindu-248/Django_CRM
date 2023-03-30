from django.shortcuts import render
from django.http import HttpResponse
from .models import Lead

# Create your views here.

def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    # return HttpResponse("Hello World")
    return render(request, "leads/lead_list.html", context)

