from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import *
from .forms import *


def index(request):
    qs = Book.objects.all()
    context = {"books": qs, "Date": datetime.now().date(), "form": BookForm}
    return render(request, 'index.html', context)


def detail(request, isbn):
    book = Book.objects.get(isbn=isbn)
    return HttpResponse(f"You're looking at book with id = {isbn} and title {book.title}")


def list(request):
    books = Book.objects.all()
    return HttpResponse(f"<i>You're looking at books list.</i><br/>" + ", ".join([str(b) for b in books]))


def add(request):
    if request.method == "POST":
        form_data = BookForm(data=request.POST, files=request.FILES)
        if form_data.is_valid():
            book = form_data.save(commit=False)
            book.user = request.user
            book.cover_image = form_data.cleaned_data["cover_image"]
            book.save()
            return redirect("index")
    else:
        form_data = BookForm()
    return render(request, "add.html",context={"form":form_data})


def add_author(request):
    if request.method == "POST":
        form_data = AuthorForm(request.POST)
        if form_data.is_valid():
            author = Author(
                name_surname=form_data.data["name_surname"],
                year_birth=form_data.data["year_birth"],
                country=form_data.data["country"],
                biography=form_data.data["biography"]
            )
            author.save()
            return redirect("/")
    else:
        form_data = AuthorForm
    return render(request, "add_author.html", context={"form": form_data})
