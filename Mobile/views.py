from django.shortcuts import render
from Blog.models import Post
from .models import Comment
from .serializers import PostSerializers
from .serializers import CommentSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny

#generic class based views
class api_home_page(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    pagination_class = PageNumberPagination
    filter_backends = [SearchFilter]
    search_fields = ["title", "content", "author"]
    # permission_classes =[AllowAny]

class api_detail_page(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializers
    lookup_field = "id" #You must specify id, slug or uuid if you are not using pk in your urls because pk is the default so for this case lookup_field is necessary

# function based views

# @api_view(["GET", "POST"])
# def api_home_page(request):
#     if request.method == "GET":
#         all_posts = Post.objects.all() # A query set
#         serializer = PostSerializers(all_posts, many=True)# Serializers converts one object at a time, in this case we have a more than one, hence many=True must be added
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     else:
#         serializer = PostSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"Success": "Nice work!!",
#                              "data": serializer.data}, status=status.HTTP_201_CREATED)
#         return Response("Invalid data entered")


# @api_view(["GET", "PUT", "DELETE"])
# def api_detail_page(request, id):
#     if request.method == "GET":
#         single_detail = Post.objects.get(id=id) # A query set
#         serialized_post = PostSerializers(single_detail)# Serializers converts one object at a time, in this case we have a more than one, hence many=True must be added
#         return Response(serialized_post.data, status=status.HTTP_200_OK)
#     elif request.method == "PUT":
#         single_detail = Post.objects.get(id=id) # A query set
#         serialized_post = PostSerializers(single_detail, data=request.data, partial=True)# Serializers converts one object at a time, in this case we have a more than one, hence many=True must be added
#         if serialized_post.is_valid():
#             serialized_post.save()
#             return Response(serialized_post.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serialized_post.errors, status=status.HTTP_400_BAD_REQUEST)
        
#     else:
#         single_post = Post.objects.get(id=id)
#         single_post.delete()
#         return Response("Post has been deleted", status=status.HTTP_204_NO_CONTENT)
    


#NOTE: When using class basedview as below, ensure to add .as_view() to your page call name in urls.py
class mobile_home_page(APIView):
    def get(self, request):
        if request.method == "GET":
            all_posts = Comment.objects.all()
            serializers = CommentSerializers(all_posts, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        
    def post(self, request):
        serializer = CommentSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Nice work!!",
                             "date": serializer.data}, status=status.HTTP_201_CREATED)
        return Response("Invalid entery")
    

class mobile_detail_page(APIView):
    def get(self, request, id):
        if request.method == "GET":
            single_comment = Comment.objects.get(id=id)
            serialized_post = CommentSerializers(single_comment)
            return Response(serialized_post.data, status=status.HTTP_200_OK)
        

    def put(self, request, id):
        single_comment = Post.objects.get(id=id)
        serialized_comment = CommentSerializers(single_comment, data=request.data, partial=True)
        if serialized_comment.is_valid():
            serialized_comment.save()
            return Response(serialized_comment.data, status=status.HTTP_202_ACCEPTED)
        return Response(serialized_comment.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        single_comment = Comment.objects.get(id=id)
        single_comment.delete()
        return Response("Post has been deleted", status=status.HTTP_204_NO_CONTENT)
