
# Create your views here.
import datetime

from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views import generic

from .models import Choice, Question
from django.template import loader
from django.shortcuts import render


# def index(request):
#     return HttpResponse("Hello world")

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now: %s</body></html>" % now
    return HttpResponse(html)

# def detail(request, question_id):
#     return HttpResponse("You're looking at question %s" % question_id)

def index(request):
    latest_questions = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    all_questions = Question.objects.all()
    # output = ", ".join([q.question_text for q in latest_questions])
    context = {
        "latest_questions" : latest_questions,
        "all_questions" : all_questions
    }
    # return HttpResponse(template.render(context, request))
    return render(request, "polls/index.html", context)

def index2(request):
    latest_question_list = Question.objects.order_by("pub_date")[:5]
    all_questions = Question.objects.all()
    context={"latest_question_list":latest_question_list,"all_questions":all_questions}
    return render(request,"polls/index.html",context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        # questions = Question.objects.all()
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
    # return render(request, "polls/detail.html", {"questions": questions})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:result", args=(question_id,)))

def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/result.html",{"question":question})



class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "all_questions"

    def get_queryset(self):
        return Question.objects.all()

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/result.html"


