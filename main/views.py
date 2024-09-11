from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from main.models import News, Author, Category
from django.contrib.auth import authenticate, login
from django.shortcuts import  render, redirect
from .forms import AuthorForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render


# Create your views here.



class HomePageView(TemplateView):
    template_name = 'index.html'


class NewsList(ListView):
    model = News
    template_name = 'news_list.html'

class AuthorsList(ListView):
    model = Author
    template_name = 'authors_list.html'

    
def dodaj_clanak(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=News()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.publication_date = request.POST.get('publication_date')

                post.save()
                
                return render(request, 'new_post.html')  

        else:
                return render(request,'new_post.html')

def izbrisi_clanak(request, news_id):
    news = News.objects.get(pk=news_id)
    news.delete()
    return redirect('news')



def azuriraj_autor(request, author_id):
    author = Author.objects.get(pk=author_id)
    form = AuthorForm(request.POST or None, instance=author)
    if form.is_valid():
        form.save()
        return redirect('authors')
    return render(request, 'update_author.html', 
        {'author': author,
        'form':form})



