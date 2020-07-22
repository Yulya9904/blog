from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import  User


class Post(models.Model):
    class Meta():
        verbose_name:"Статья"
        verbose_name_plural:"Статьи"
        ordering=["created"]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,verbose_name='Автор')
    title = models.CharField('Заголовок',max_length=200, )
    text = models.TextField('Текст записи')
    image= models.ImageField('Картинка', upload_to="post/")
    created= models.DateTimeField('Дата создания', auto_now_add=True)
    update= models.DateTimeField('Дата обновления', auto_now=True)
    moder= models.BooleanField("Модерация", default=False)


    def __str__(self):
        return self.title

