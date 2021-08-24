from django.urls import path
from post.api.view import get_posts, create_post, get_single_post

urlpatterns = [
    path('userdetail/<str:username>', get_posts, name="GetPost"),
    path('create/', create_post, name="CreatePost"),
    path('postdetail/<int:post_id>', get_single_post, name="GetSinglePost")
]
