from django.shortcuts import render
from django.views.generic import ( ListView,
                                   DetailView,
                                )
from django.db.models import Q

from .models import Article
# Create your views here.

class ArticlesListView(ListView):

    model=Article
    context_object_name='articles_list'
    template_name='articles_list.html'

    def get_queryset(self):

        queryset=Article.objects.all()
        query=self.request.GET.get('query')
        print(query)
        if query not in ["",None]:
            queryset=queryset.filter(Q(title__icontains=query)|
                            Q(description__icontains=query)|
                            Q(author__username__icontains=query)
                            )
        return queryset
    
class ArticleView(DetailView):

    model=Article
    context_object_name='article'
    queryset=Article.objects.all()
    template_name='article.html'


