from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    #글작성자
    author = models.ForeignKey('auth.User')
    #글제목
    title = models.CharField(max_length=200)
    #글내용
    text = models.TextField()
    #migrate test
    #test=models.TextField()
    #글작성일자
    created_date = models.DateTimeField(default=timezone.now)
    #글게시일자
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()