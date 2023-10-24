from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from .models import BlogComment

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def Bloghome(request):
    allPosts = Post.objects.all()
    # print(allPosts)
    return render(request, "bloghome.html", {'allPosts': allPosts})


def Blogpost(request, slug):
    post = Post.objects.filter(slug=slug)
    comments = BlogComment.objects.all()
    totalcomments = BlogComment.objects.all().count()
    Commentss = list(comments)
    Commentss.reverse()
    # print(type(Comments))
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        posti = Post.objects.filter(sno=postSno)
        comment = BlogComment(comment=comment, user=user, post=post)
        comment.save()
        messages = "Your comment has been posted successfully"
        messages = {"messages": messages, "A": "success"}
        Comments = BlogComment.objects.all()
        TotalComments = BlogComment.objects.all().count()
        allComments = list(Comments)
        allComments.reverse()
        return render(request, 'blogpost.html',
                      {"messages": messages, "post": posti, "comments": allComments, "count": TotalComments})
    return render(request, "blogpost.html", {'post': post, "comments": Commentss, "count": totalcomments})


def search(request):
    query = request.POST['query']
    print(query)

    if len(query) == 0:
        messages = "please enter any query in search."
        messages = {"messages": messages, "A": "warning"}
        return render(request, 'search.html', {"messages": messages})


    else:
        allPostsTitle = Post.objects.filter(title__icontains=query)
        allPostsAuthor = Post.objects.filter(author__icontains=query)
        allPostsContent = Post.objects.filter(content__icontains=query)
        allPosts = allPostsTitle.union(allPostsContent, allPostsAuthor)
        if allPosts.count() == 0:
            message = "No search results found. Please refine your query."
            messages = {"messages": message, "A": "warning"}
            print(0)
            return render(request, 'search.html', {"messages": messages, "query": query})

        else:
            print(12)
        return render(request, 'search.html', {"allPosts": allPosts})
    return render(request, 'search.html')


def Signof(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['username']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        checkuser = User.objects.filter(email=email)
        checkusername = User.objects.filter(username=username)
        if len(checkuser) == 0 and len(checkusername) == 0:
            if pass2 == pass1:
                creatinguser = User.objects.create_user(username=username, email=email, password=pass1)
                messages = "Your iCoder has been successfully created."
                messages = {"messages": messages, "A": "success"}
                return render(request, "home.html", {"messages": messages})


        else:
            message = "You have already registered."
            messages = {"messages": message, "A": "warning"}
            return render(request, "home.html", {"messages": messages})


def login(request):
    if request.method == "POST":
        # Get the post parameters
        username = request.POST['loginusername']
        password = request.POST['pass']
        checkuser = authenticate(request, username=username, password=password)
        print(checkuser)
        if checkuser is not None:
            message = "You have logged in."
            messages = {"messages": message, "A": "success"}
            return render(request, "home.html", {"messages": messages, "user": checkuser})

        else:
            message = "You are not registred till now,please registered first."
            messages = {"messages": message, "A": "danger"}
            return render(request, "home.html", {"messages": messages})


def logout(request):
    logout(request)
    message = "You are logged out."
    # messages = {"messages": message, "A": "success"}
    return redirect("home")
