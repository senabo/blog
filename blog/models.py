from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='автор')
    title = models.CharField(max_length=200, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='дата створення')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='дата публікації')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'