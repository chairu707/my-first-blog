from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField('カテゴリ名', max_length=255)

    def __str__(self):
        return self.name

class PostQuerySet(models.QuerySet):

    def published(self):
        return self.filter(published__lte=timezone.now())


class Post(models.Model):
    title = models.CharField(max_length=100)
    published = models.DateTimeField('作成日', default=timezone.now)
    #YouTube消し
    #youtube = models.TextField()
    text = models.TextField(blank=True, null=True)
    category = models.ForeignKey(Category, verbose_name='カテゴリ', on_delete=models.PROTECT)

    objects = PostQuerySet.as_manager()


    def __str__(self):
        return self.title

    def summary(self):
        return self.text[:100]

