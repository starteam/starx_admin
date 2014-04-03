from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
    from django.contrib.auth import login

# Create your views here.
def index(request):
    email = request.environ['HTTP_SSL_EMAIL']
    try:
        user = User.objects.get(email=email)
        if user.is_active:
            # if user active make it authenticated
            login(request, user)
            print "User logged in"
            print user
        else:
            pass
    except User.DoesNotExist:
        print "User does not exist"
        print user
        pass

    return render_to_response("mit_accounts/index.html",  RequestContext(request))
