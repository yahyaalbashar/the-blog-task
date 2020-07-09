from rest_framework.serializers import (ModelSerializer,
                                        SerializerMethodField    
                                        )
from articles.models import Article

class ArticleSerializer(ModelSerializer):
    likes_count=SerializerMethodField()
    categories=SerializerMethodField()
    author=SerializerMethodField()
    publish_date=SerializerMethodField()

    def get_likes_count(self,obj):
        counter=len(obj.likes.all())
        return counter

    def get_categories(self,obj):
        response={}
        categories_list=obj.category.all()
        for category in categories_list:
            response[category.title]={'id':category.id,'description':category.description}
        return response
    
    def get_author(self,obj):
        response={}
        author=obj.author
        response['author-name']=author.username
        response['author-email']=author.email
        response['id']=author.id
        return response

    def get_publish_date(self,obj):
        date=obj.publish_date.date()
        return date

    
    class Meta:
        model=Article
        fields=[
            'id',
            'title',
            'description',
            'author',
            'likes_count',
            'publish_date',
            'categories'
        ]
