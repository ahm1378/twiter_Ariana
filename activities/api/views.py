from django.http import JsonResponse

from activities.models import Comment, PostLike
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import authentication_classes, api_view,permission_classes

from activities.tasks import send_email
from post.models import PostModel

User=get_user_model()


@api_view(["POST"])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request, post_id):
    content = request.data['content']
    id = post_id
    user = PostModel.objects.get(id=post_id)
    if user==request.user:
        return JsonResponse({
            "message": "you cant comment your self",
        }, status=404)
    else:
        post = Comment.objects.create(user=request.user, content=content, post=id)
        response_data = {'status' : 'comment create succesfully'}
        return JsonResponse(response_data, safe=False)


@api_view(["POST"])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_post(request, post_id):
    # if condition True means like else means dislike
    content = request.data['condition']
    id = post_id
    post = PostModel.objects.get(id=post_id)
    if post.user == request.user:
        return JsonResponse({
            "message": "you cant like/dislike your post",
        }, safe=False, status=404)
    else:
        post = PostLike.objects.create(user=request.user, content=content, post=id)
        send_email.delay(post.user.username)
        response_data = {'status' : 'comment create succesfully'}
        return JsonResponse(response_data, safe=False)


@api_view(["POST"])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_comment(request, comment_id):
    # if condition True means like else means dislike
    content = request.data['condition']
    id = comment_id
    comment = Comment.objects.get(id=comment_id)
    if comment.user == request.user:
        return JsonResponse({
            "message": "you cant like your comment",
        }, safe=False, status=404)
    else:
        post = PostLike.objects.create(user=request.user, content=content, post=id)
        send_email.delay(comment.user.username)
        response_data = {'status': 'comment create succesfully'}
        return JsonResponse(response_data, safe=False)