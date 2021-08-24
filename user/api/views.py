from django.http import JsonResponse
from django.contrib.auth import authenticate

from django.contrib.auth import login
from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model
User = get_user_model()


@api_view(['POST'])
def login_view(request):
    username = request.data['username']
    password = request.data['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return JsonResponse({"login_status": 1, 'username': username}, safe=False)

    else:
        JsonResponse({
            "login_staus": 0,
            "message": "login failed"
        }, safe=False)


@api_view(['POST'])
def register_view(request):
    if request.data['password'] != request.data['password2']:
        return JsonResponse(
                {'message': "passwords are not match"},
                safe=False
            )
    if User.objects.filter(username=request.data['username']).exists():
        return JsonResponse(
                {'message': 'user_name exists'},
                safe=False
            )
    User.objects.create_user(username=request.data['username'], password=request.data['password'])
    return JsonResponse(
        {"message": 'user created successfully'},
        safe=False
    )
