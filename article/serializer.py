from rest_framework import serializers
from .models import Article
#serializers
class ArticleSerializer(serializers.Serializer):
  author_id = serializers.IntegerField()
  title = serializers.CharField(max_length=120)
  description = serializers.CharField()
  body = serializers.CharField()

  def create(self, validated_data):
    return Article.objects.create(**validated_data)

  def update(self, instance, validate_data):
    instance.author_id = validate_data.get('author_id', instance.author_id)
    instance.title = validate_data.get('title',instance.title)
    instance.description = validate_data.get('description',instance.description)
    instance.body = validate_data.get('body',instance.body) 

    instance.save()
    return instance