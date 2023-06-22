from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) #CASCADE:userが削除された際にtaskもすべて削除をする
    title = models.CharField(max_length=100) #CharField:文字列を書き込める
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    createdDate = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title #管理画面で見やすくするため
    
    class Meta:
        ordering = ["completed"]