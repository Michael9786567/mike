from django.db import models
from django.utils.translation import gettext_lazy as _
    
class Articles(models.Model):
    title = models.CharField(_('Название'),max_length=50)
    intro = models.CharField(_('Анонс'), max_length=250)
    full_text = models.TextField(_('Статья'))
    date = models.DateTimeField(_('Дата публикации'))

    def __str__(self):
        return f'Новость: {self.title}'


    def get_absolute_url(self):
        return f'/news/{self.id}'


    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'