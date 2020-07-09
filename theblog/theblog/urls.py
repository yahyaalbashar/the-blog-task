from django.contrib import admin
from django.urls import path,re_path
from articles.views import (ArticlesListView,
                            ArticleView
                            )
from articles.api.viewset import (ArticleLikeAPI,
                                  ListArticlesAPIView,
                                  RetrieveArticleAPIView,
                                 
                                )
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", ArticlesListView.as_view(), name="articles-list"),
    re_path(r'^get-article/(?P<pk>[0-9])/', ArticleView.as_view(), name='get-article'),
    path("api/list-articles/", ListArticlesAPIView.as_view(), name="list-articles-api"),
    re_path(r'^api/get-article/(?P<pk>[0-9])/', RetrieveArticleAPIView.as_view(), name='get-article-api'),
    re_path(r'^api/(?P<id>[0-9])/like/$', ArticleLikeAPI.as_view(), name='like-article'),
    
]


    