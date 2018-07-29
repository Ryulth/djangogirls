from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # 다른 모델에 대한 링크 의미
    title = models.CharField(max_length=200) # 길이제한 걸어줌
    text = models.TextField() # 길이제한 ㄴ
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title