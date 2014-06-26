from django.shortcuts import render
from django.conf import settings
import pickle
from django.shortcuts import render,render_to_response,redirect
from django.template import RequestContext
from ims_lti_py.tool_provider import DjangoToolProvider
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
import oauth2

@csrf_exempt
def index(request):
    print "REQUEST START"
    if settings.LTI_DEBUG:
        print "META"
        print request.META
        print "PARAMS"
        print request.POST
    consumer_key = settings.CONSUMER_KEY
    secret = settings.LTI_SECRET
    request_dict = dict()
    for r in request.POST.keys():
        request_dict[r] = request.POST[r]
    request_dict['lis_outcome_service_url'] = fix_url(request_dict['lis_outcome_service_url'])

    tool = DjangoToolProvider(consumer_key, secret, request_dict)
    session = request.session
    session.clear()
    try:
        is_valid = tool.is_valid_request(request)
    except oauth2.MissingSignature,e:
        is_valid = False
        pass
    except oauth2.Error,e:
        is_valid = False
        pass

    session['is_valid'] = is_valid
    # import pudb
    # pudb.set_trace()
    post_result = tool.post_replace_result(.5,{'message_identifier':'edX_fix'})
    session['is_success'] = post_result.is_success()
#    post_delete = tool.post_delete_result()
#    session['is_delete_success'] = post_delete.is_success()
    if settings.LTI_DEBUG:
        print "SESSSION"
        for k in session.keys():
            print "{}={}".format( k, session[k])
    session['LTI_POST'] = pickle.dumps( request.POST )
    return redirect('AddProblem')

@csrf_exempt
def add_problem(request):
    print "Add problem session"
    session = request.session
    # request_post = dict(pickle.loads(session['LTI_POST']))
    # print request_post['lis_outcome_service_url']
    # request_post['lis_outcome_service_url'] = fix_url(request_post['lis_outcome_service_url'][0])
    # print request_post['lis_outcome_service_url']
    # consumer_key = settings.CONSUMER_KEY
    # secret = settings.LTI_SECRET
    # print "Add problem session 2"
    # import pudb; pudb.set_trace()
    #
    # tool = DjangoToolProvider(consumer_key, secret, request_post)
    # post_result = tool.post_replace_result(50)
    # print "Add problem session 3"
    # session['is_success'] = post_result.is_success()
    # post_delete = tool.post_delete_result()
    # session['is_delete_success'] = post_delete.is_success()
    session['LTI_POST'] = ''
    print "Add problem session 4"
    if settings.LTI_DEBUG:
        print "SESSSION"
        for k in session.keys():
            print "{}={}".format( k, session[k])

    return render_to_response("ims_lti/index.html",  RequestContext(request))

def fix_url(str):
    old = "https://localhost/"
    new = "http://192.168.33.10/"
    if str.find(old) == 0:
        return u"{}{}".format( new , str[len(old):])
    return str