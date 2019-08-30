from django.shortcuts import render,redirect,get_object_or_404
from .models import Makale
from.forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def index(request):
    articles =Makale.objects.all()
    return render(request,"index.html",{"articles":articles})

def about(request):
    return render(request,"about.html")
@login_required()
def dashboard(request):

    articles = Makale.objects.all()
    return render(request,"dashboard.html",{"articles" : articles})
@login_required()
def update(request,id):
    article = get_object_or_404(Makale, id=id)
    form = ArticleForm(request.POST or None, request.FILES or None, instance=article)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request, "Başarıyla Başarıyla Güncellendi")
        return redirect("/dashboard")
    else:

        return render(request, "update.html", {"form": form})

@login_required()
def delete(request, id):
    article = get_object_or_404(Makale, id=id)
    article.delete()
    messages.success(request, "Makale Başarıyla Silindi")
    return redirect("/dashboard")
@login_required()
def add(request):
    form = ArticleForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        article = form.save()



        messages.success(request, "Başarıyla Kayıt Edildi")
        return redirect("/dashboard")
    else:
        return render(request, "addarticle.html", {"form": form})

def article(request,id):
    article = get_object_or_404(Makale,id = id)
    return render(request,"article.html",{"article":article})