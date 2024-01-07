from django.urls import path


from . import views

app_name="polls"

urlpatterns = [
    # /polls/
    path("", views.IndexView.as_view(), name="index"),

    # /polls/5/
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),

    # /polls/index2
    path("index2/", views.index2, name="index2"),

    # /polls/vote
    path("<int:question_id>/vote", views.vote, name="vote"),

    path("<int:pk>/result", views.ResultView.as_view(), name="result")
]
