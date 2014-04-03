from django.shortcuts import render,render_to_response
from django.template import RequestContext

# Create your views here.
def index(request):
    import pudb
    pudb.set_trace()
    return render_to_response("mit_accounts/index.html",  RequestContext(request))
