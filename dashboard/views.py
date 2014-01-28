from django.shortcuts import render,render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    return render_to_response("dashboard/index.html",  RequestContext(request))