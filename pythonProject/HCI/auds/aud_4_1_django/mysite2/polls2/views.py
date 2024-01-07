from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.template import loader


def index(request):
    ace = 1
    context = {"ace":123}
    print("inside index")
    template = loader.get_template("polls2/index.html")

    # return render(request, "polls2/index.html", {"ace":ace})
    return HttpResponse(template.render(context, request))
