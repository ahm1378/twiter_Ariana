from django.http import JsonResponse
from django.contrib.auth import get_user_model, authenticate
from post.models import PostModel
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.decorators import authentication_classes, api_view,permission_classes

User = get_user_model()

@api_view(["GET"])
def get_posts(request,username):
    response = []
    posts = PostModel.objects.filter(user__username=username).values_list('id', 'title','caption')
    for post in posts:
        response.append(
            {
                "post_id": post[0],
                "title": post[1],
                "caption": post[2],

            })

    return JsonResponse(response, safe=False)


@api_view(["POST"])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_post(request):
    title = request.data['title']
    caption = request.data['caption']
    post = PostModel.objects.create(user=request.user, title=title, caption=caption)
    response_data = {'status' : 'post create succesfully'}
    return JsonResponse(response_data, safe=False)


@api_view(["GET"])
def get_single_post(request, post_id):
    try:
        post = PostModel.objects.get(id=post_id)
        response = {
        "user": post.user.username,
        "title": post.title,
        "caption": post.caption
    }
        return JsonResponse(response, safe=False)
    except:
        response ={
            "message" : "post not found"
        }
        return JsonResponse(response, safe=False, status=404)