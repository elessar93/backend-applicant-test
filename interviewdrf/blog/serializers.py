from rest_framework import serializers

from blog.models import Blog, Comment


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['title', 'published_date', 'is_active', 'related_user', 'content', 'related_tags']
        read_only_fields = ('published_date', 'is_active', 'related_user')


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['title', 'comment', 'send_date', 'related_user','related_blog']
        read_only_fields = ('send_date','related_user',)
