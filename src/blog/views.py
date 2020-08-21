from django.shortcuts import render, get_object_or_404
from django.urls import reverse

# Create your views here.

from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
)

from .forms import ArticleModelForm
from .models import Article

class ArticleListView(ListView):
    template_name = 'articles/article_list.html' #set the template name
    queryset = Article.objects.all() #will look for <blog>/<modelname>_list.html

class ArticleCreateView(CreateView): #interact with get_absolute_url
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm #bring in the model form
    queryset = Article.objects.all()
    #success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    # def get_success_url(delf):
    #     return '/'

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    #queryset = Article.objects.all()

    def get_object(self): #overwrite the pk key word argument in urls(default set in class based views
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    #queryset = Article.objects.all()

    def get_object(self): #overwrite the pk key word argument in urls(default set in class based views
        id_ = self.kwargs.get("id")
        return get_object_or_404(Article, id=id_)

    def get_success_url(self):
        return reverse('articles:article-list')
