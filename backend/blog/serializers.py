from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'slug', 'content', 'summary', 'image', 'created_at', 'updated_at', 'published']
        read_only_fields = ['id', 'created_at', 'updated_at'] 