from rest_framework import serializers
from .models import *
from rest_framework import exceptions

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

class BlogPostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = BlogPost
        fields = '__all__'
    
    def create(self, validated_data):
        blog_tags = validated_data.pop('tags')
        blog = BlogPost.objects.create(**validated_data)
        for tag_data in blog_tags:
            tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            blog.tags.add(tag)
        return blog

    
    def update(self, instance, validated_data):
        blog_tags = validated_data.pop('tags', [])
        instance = super().update(instance, validated_data)
        instance.tags.clear()
        for tag_data in blog_tags:
            tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            instance.tags.add(tag)
        return instance 