from django.db import models
from django.contrib.auth.models import User


class Transit(models.Model):
    title = models.CharField(max_length=20)
    cost = models.IntegerField()

    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # 비행기표, 숙소 비용 등은 manytomanyfield로 처리 하도록=>정보공개시 타인과 정보공유 가능하도록.
    # tags = models.ManyToManyField()
    image = models.ImageField(null=True, blank=True)
    transits = models.ManyToManyField('Transit', blank=True)
    author = models.ForeignKey(User)
    lnglat = models.CharField(max_length=200, blank=True, null=True)

    @property
    def lng(self):
        if self.lnglat:
            return self.lnglat.split(',')[0]

    @property
    def lat(self):
        if self.lnglat:
            return self.lnglat.split(',')[1]

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User)

    class Meta:
        ordering = ('-id',)
