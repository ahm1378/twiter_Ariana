from django.contrib import admin

# Register your models here.
from activities.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post',  'user',
                    'like_count', 'dislike_count')
    search_fields = ('content',)
