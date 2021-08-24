from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
User = get_user_model()


class PostModel(models.Model):
    user = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    title = models.CharField(_("title"), max_length=400)
    caption = models.TextField(_("caption"), blank=True)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class PostMedia(models.Model):
    IMAGE = 0
    VIDEO = 1
    post = models.ForeignKey(PostModel, related_name="medias", on_delete=models.CASCADE)
    file_media = models.FileField(_("media file"), upload_to='post/files')
    choices = (
        (IMAGE, _("image")),
        (VIDEO, _("Video"))
    )
    type_choice = models.SmallIntegerField(_("media"), choices=choices)

    def __str__(self):
        return self.post.caption

    class Meta:
        verbose_name = _('PostMedia')
        verbose_name_plural = _('PostMedia')