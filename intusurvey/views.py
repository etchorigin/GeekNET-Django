from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login
from crowdsourcing.models import Survey

def home(request):
    latest_survey = None
    surveys = Survey.live.order_by('-survey_date')
    if surveys:
        latest_survey = surveys[0]
    return render_to_response(
        "home.html",
        {"latest_survey": latest_survey},
        RequestContext(request))

def accounthome(request):
    if request.user.is_authenticated():
        return render_to_response('profile.html' , RequestContext(request))
    else:
        return render_to_response('accounthome.html')

@login_required
def profile(request):
    return render_to_response('profile.html' , RequestContext(request))