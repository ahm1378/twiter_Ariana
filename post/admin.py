from django.contrib import admin
from post.models import PostModel, PostMedia
# Register your models here.


class PostMediaInline(admin.TabularInline):
    model = PostMedia
    extra = 1


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user']
    search_fields = ('title',)
    inlines = [PostMediaInline]


admin.site.register(PostModel, PostAdmin)
