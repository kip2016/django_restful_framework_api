from webbrowser import get
from django.shortcuts import get_object_or_404, render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Article
from .serializer import ArticleSerializer
# Create your views here.

class ArticleView(APIView):
  def get(self,request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response({
      "articles": serializer.data
    })

  def post(self, request):
    article = request.data.get('article')

    #create an article from the above data
    serializer = ArticleSerializer(data=article)
    if serializer.is_valid(raise_exception=True):
      article_saved = serializer.save()
    return Response({
      "success": "Article '{}' created successfully".format(article_saved)
    })

    #update method
  def put(self, request, pk):
    saved_article = get_object_or_404(Article.objects.all(), pk=pk)
    data = request.data.get('article')
    serializer = ArticleSerializer(instance=saved_article, data=data, partial=True)
    if serializer.is_valid(raise_exception=True):
      article_saved = serializer.save()
    return Response({"success": "Article '{}' updated successfully". format(article_saved)})

  #delete method
  def delete(self, request, pk):
    #get object with this pk
    article = get_object_or_404(Article.objects.all(), pk=pk)
    article.delete()
    return Response({"message": "Article with id'{}' has been deleted.".format(pk)})