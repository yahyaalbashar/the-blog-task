from rest_framework.views import APIView
from rest_framework.generics import (ListAPIView,
                                     RetrieveAPIView
                                    )
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.shortcuts import get_object_or_404
from django.db.models import Q

from articles.models import Article
from .serializers import ArticleSerializer
from theblog.utils import send_mail

class ListArticlesAPIView(ListAPIView):

    serializer_class=ArticleSerializer

    def get_queryset(self):
        queryset=Article.objects.all()
        query=self.request.data['query']
        
        if query not in ["",None]:
            queryset=queryset.filter(Q(title__icontains=query)|
                            Q(description__icontains=query)|
                            Q(author__username__icontains=query)
                            )

        return queryset
    


class RetrieveArticleAPIView(RetrieveAPIView):

    queryset=Article.objects.all()
    serializer_class=ArticleSerializer

class ArticleLikeAPI(APIView):

    authentication_classes = (authentication.SessionAuthentication,authentication.BasicAuthentication)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id=None, format=None):

        article = get_object_or_404(Article, id=id)     
        user = self.request.user
        liked = False
        likes=article.likes.all()
      
        if user.is_authenticated:
            if not user in likes:
                liked = True
                article.likes.add(user)
                send_mail(user.username,article.title)
        
            
        data = {
            "liked": liked,
            "count":likes.count(),

        }
        return Response(data)