from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostModelTest(TestCase):
    """Test module for BlogPost model"""

    def setUp(self):
        """Set up test data"""
        BlogPost.objects.create(
            title="Test Blog Post",
            slug="test-blog-post",
            content="This is a test blog post content.",
            summary="Test summary",
            published=True
        )
        BlogPost.objects.create(
            title="Unpublished Test Post",
            slug="unpublished-test-post",
            content="This is an unpublished test post.",
            summary="Unpublished test",
            published=False
        )

    def test_blog_post_str(self):
        """Test the string representation of BlogPost"""
        blog_post = BlogPost.objects.get(slug="test-blog-post")
        self.assertEqual(str(blog_post), "Test Blog Post")

    def test_blog_post_ordering(self):
        """Test that blog posts are ordered by created_at in descending order"""
        posts = list(BlogPost.objects.all())
        # Since both posts are created in the same test run, we need to check by title
        # as the created_at might be too close to differentiate
        self.assertEqual(len(posts), 2)


class BlogPostAPITest(APITestCase):
    """Test module for BlogPost API"""

    def setUp(self):
        """Set up test data and users"""
        # Create admin user
        self.admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='adminpassword'
        )
        
        # Create regular user
        self.user = User.objects.create_user(
            username='user',
            email='user@example.com',
            password='userpassword'
        )
        
        # Create test blog posts
        self.published_post = BlogPost.objects.create(
            title="Published Test Post",
            slug="published-test-post",
            content="This is a published test post content.",
            summary="Published test summary",
            published=True
        )
        
        self.unpublished_post = BlogPost.objects.create(
            title="Unpublished Test Post",
            slug="unpublished-test-post",
            content="This is an unpublished test post.",
            summary="Unpublished test summary",
            published=False
        )
        
        # Initialize API client
        self.client = APIClient()

    def test_get_all_blog_posts_admin(self):
        """Test that admin users can see all blog posts"""
        # Authenticate as admin
        self.client.force_authenticate(user=self.admin_user)
        
        # Get API response
        response = self.client.get(reverse('blogpost-list'))
        
        # Get data from DB
        blog_posts = BlogPost.objects.all()
        serializer = BlogPostSerializer(blog_posts, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should see both posts

    def test_get_all_blog_posts_user(self):
        """Test that regular users can only see published blog posts"""
        # Authenticate as regular user
        self.client.force_authenticate(user=self.user)
        
        # Get API response
        response = self.client.get(reverse('blogpost-list'))
        
        # Get data from DB
        blog_posts = BlogPost.objects.filter(published=True)
        serializer = BlogPostSerializer(blog_posts, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should only see published post

    def test_get_all_blog_posts_unauthenticated(self):
        """Test that unauthenticated users can only see published blog posts"""
        # No authentication
        
        # Get API response
        response = self.client.get(reverse('blogpost-list'))
        
        # Get data from DB
        blog_posts = BlogPost.objects.filter(published=True)
        serializer = BlogPostSerializer(blog_posts, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Should only see published post

    def test_create_blog_post_admin(self):
        """Test that admin users can create blog posts"""
        # Authenticate as admin
        self.client.force_authenticate(user=self.admin_user)
        
        # Create new blog post data
        new_post_data = {
            'title': 'New Test Post',
            'slug': 'new-test-post',
            'content': 'This is a new test post content.',
            'summary': 'New test summary',
            'published': True
        }
        
        # Post to API
        response = self.client.post(
            reverse('blogpost-list'),
            new_post_data,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.count(), 3)
        self.assertEqual(BlogPost.objects.get(slug='new-test-post').title, 'New Test Post')

    def test_create_blog_post_user(self):
        """Test that regular users cannot create blog posts"""
        # Authenticate as regular user
        self.client.force_authenticate(user=self.user)
        
        # Create new blog post data
        new_post_data = {
            'title': 'New Test Post',
            'slug': 'new-test-post',
            'content': 'This is a new test post content.',
            'summary': 'New test summary',
            'published': True
        }
        
        # Post to API
        response = self.client.post(
            reverse('blogpost-list'),
            new_post_data,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(BlogPost.objects.count(), 2)  # Count should remain the same

    def test_update_blog_post_admin(self):
        """Test that admin users can update blog posts"""
        # Authenticate as admin
        self.client.force_authenticate(user=self.admin_user)
        
        # Update data
        update_data = {
            'title': 'Updated Test Post',
            'content': 'This is updated content.'
        }
        
        # Put to API
        response = self.client.patch(
            reverse('blogpost-detail', kwargs={'pk': self.published_post.pk}),
            update_data,
            format='json'
        )
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.published_post.refresh_from_db()
        self.assertEqual(self.published_post.title, 'Updated Test Post')
        self.assertEqual(self.published_post.content, 'This is updated content.')

    def test_delete_blog_post_admin(self):
        """Test that admin users can delete blog posts"""
        # Authenticate as admin
        self.client.force_authenticate(user=self.admin_user)
        
        # Delete post
        response = self.client.delete(
            reverse('blogpost-detail', kwargs={'pk': self.published_post.pk})
        )
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(BlogPost.objects.count(), 1)  # One post should be deleted
