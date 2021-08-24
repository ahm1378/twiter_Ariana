from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from post.models import PostModel

user = get_user_model()


class CommentLike(models.Model):
    user = models.ForeignKey(user, verbose_name=_(
        "Author"), on_delete=models.CASCADE)
    comment = models.ForeignKey('Comment', verbose_name=_(
        'Comment'),  related_name='comment_like', related_query_name='comment_like', on_delete=models.CASCADE)
    condition = models.BooleanField(_("Condition"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    class Meta:
        unique_together = [['user', 'comment']]
        verbose_name = _("CommentLike")
        verbose_name_plural = _("CommentLikes")

    def __str__(self):
        return str(self.condition)


class Comment(models.Model):
    content = models.TextField(_("Content"))
    post = models.ForeignKey(PostModel, verbose_name=_(
        "Post"), on_delete=models.CASCADE)
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)
    user = models.ForeignKey(user, verbose_name=_(
        "user"), on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(_("confirm"), default=True)


    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")
        ordering = ['-create_at']

    def __str__(self):
        return self.content

    @property
    def like_count(self):
        q = CommentLike.objects.filter(comment=self, condition=True)
        return q.count()

    @property
    def dislike_count(self):
        q = self.comment_like.filter(condition=False)
        return q.count()


class PostLike(models.Model):
    user = models.ForeignKey(user, verbose_name=_(
        "Author"), on_delete=models.CASCADE)
    post = models.ForeignKey(PostModel, verbose_name=_(
        'Comment'), related_name='comment_like', related_query_name='comment_like', on_delete=models.CASCADE)
    condition = models.BooleanField(_("Condition"))
    create_at = models.DateTimeField(_("Create at"), auto_now_add=True)
    update_at = models.DateTimeField(_("Update at"), auto_now=True)

    def __str__(self):
        return str(self.condition)
