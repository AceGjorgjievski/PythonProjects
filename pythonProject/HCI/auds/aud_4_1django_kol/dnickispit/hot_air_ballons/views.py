from django.shortcuts import render

# Create your views here.
from .models import Flight
from .forms import FlightForm


def index(request):
    return render(request, "index.html")

def flight(request):
    if request.method == "POST":
        form_data = FlightForm(data=request.POST, file=request.FILE)
        if form_data.is_valid():
            ...

    #airways_name = {"Serbia", "JAR"}
    # airways__name__in=airways_name = "Serbia -> na nadvoreshen kluch, go zemame atributot, inaku so tochka nemame pristap

    query_set = Flight.objects.filter(user=request.user, takeoff_airport="Skopje").all() # site shto go zadovoluvaat ova
                                                                                        #zemi gi site
    context = {"query_set":query_set, "form":FlightForm}
    return render(request, "flights.html", context)
