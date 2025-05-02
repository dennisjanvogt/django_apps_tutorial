from django.http import Http404
from django.shortcuts import render
from .models import Goal

# Create your views here.
def all_goals(request):

    try:
        goals = Goal.objects.all()
    except:
        raise Http404("Poll does not exist")

    context = {'goals': goals}

    return render(request=request, template_name="tracking/home.html", context=context)
