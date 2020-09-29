from rest_framework import viewsets

from blog.models import Blog, Comment
from blog.permissons import BlogPermission, CommentPermission
from blog.serializers import BlogSerializer, CommentSerializer


class BlogViewSet(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    permission_classes = (BlogPermission,)
    queryset = Blog.objects.filter(is_active=True)

    def perform_create(self, serializer):
        serializer.save(related_user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (CommentPermission,)
    queryset = Comment.objects.filter()

    def perform_create(self, serializer):
        serializer.save(related_user=self.request.user)
