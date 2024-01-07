from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *
from .models import *

# Create your views here.


def posts(request):
    blocked_users = Block.objects.filter(user_blocker__user=request.user).values_list("user_blocked__user")
    visible_posts = Post.objects.get_queryset().exclude(author__user__in=blocked_users)

    context = {
        "visible_posts" : visible_posts
    }
    return render(request,"posts.html", context=context)


def add_post(request):
    if request.method == "POST":
        form_data = PostForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            new_post = form_data.save(commit=False)
            new_post.author = BlogPostUser.objects.get(user=request.user)
            new_post.save()

            return redirect("posts")

    return render(request, "add_post.html", context={"form":PostForm})


def profile(request):
    try:
        current_user = BlogPostUser.objects.get(user=request.user)
        posts = Post.objects.filter(author=current_user)

        context = {
            "current_user": current_user,
            "posts": posts,
            "current_logged_in": request.user
        }
        return render(request, "profile.html", context=context)
    except BlogPostUser.DoesNotExist:
        # Handle the case where the BlogPostUser does not exist for the current user
        return HttpResponse("User profile not found.")

def blockedUsers(request):
    if request.method == "POST":
        form_data = BlockForm(data=request.POST, files=request.FILES)

        if form_data.is_valid():
            new_block = form_data.save(commit=False)
            new_block.user_blocker = BlogPostUser.objects.get(user=request.user)
            new_block.save()
            return redirect("blockedUsers")

    blocks = Block.objects.filter(user_blocker__user=request.user)
    blocked_users = BlogPostUser.objects.filter(user__in=blocks.values_list("user_blocked__user"))
    context = {
        "form" : BlockForm,
        "blocked" : blocked_users,
        "current_logged_in" : request.user
    }
    return render(request, "blockedUsers.html", context=context)



