from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import BlogPost
from .serializers import BlogPostSerializer

# Create your views here.

class BlogPostViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows blog posts to be viewed or edited.
    """
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    
    def get_permissions(self):
        """
        Allow anyone to view published blog posts, but require authentication for other actions.
        """
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [permissions.AllowAny]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    
    def get_queryset(self):
        """
        Only show published posts to non-admin users.
        """
        if self.request.user.is_staff:
            return BlogPost.objects.all()
        return BlogPost.objects.filter(published=True)
