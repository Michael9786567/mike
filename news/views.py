from django.shortcuts import render, redirect
from .models import Articles
from .froms import ArticlesForm,
from django.views.generic import DetailViews, UpdateView, DeleteView

def about(request):
    return render(request,"news/about.html")

def index(request):
    data= {
        'title':'Главная страница',
    }
    return render(request,"news/index.html",data)

def home(request):
    return render(request,'news/home.html')

def news_home(request):
    news = Articles.object.all()
    return render(request,'news/home.html',{'news':news})

class NewsDetailViews(DetailViews):
    models = Articles
    template_name = 'news/detail_views.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    models = Articles
    template_name = 'news/create.html'

    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    models = Articles
    ssuccess_url = '/news/'
    template_name = 'news/news-delete.html'

def create(request):
      error = ''
      if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_vallid():
            form.save()
            return redirect('home')
        else:
            error = 'The form is incorect'


    from = ArticlesForm()

    data = {
        'error' = error
        'form': form
    }

    return render(request, 'news/create.html', data)

