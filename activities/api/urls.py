from django.urls import path
from activities.api.views import like_post, create_comment, like_comment

urlpatterns = [
    path('like/post/<int:post_id>', like_post, name="LikePost"),
    path('create/comment/<int:post_id>', create_comment, name="CreateCommet"),
    path('like/comment/<int:comment_id>', like_comment, name="LikePost")
]