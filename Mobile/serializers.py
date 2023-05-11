from rest_framework import serializers
from Blog.models import Post
from .models import Comment


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "content", "author", "date_posted"]# NOTE: 


        # fields = "__all__"


class CommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"