#coding=utf-8
from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField(max_length=20)
    user_id.primary_key = True
    password = models.CharField(max_length=20, default='123456')
    name = models.CharField(max_length=50, default='未命名')
    score = models.BigIntegerField(default=0)
    is_inline = models.BooleanField(default=False)
    register_data = models.DateTimeField(auto_now_add=True)
    login_data = models.DateTimeField(auto_now_add=True)
    key = models.CharField(max_length=50, default='0')
    def __str__(self):              # __unicode__ on Python 2
        return '{user_id:%s, name:%s, score:%d, is_inline:%s, register_data:%s, login_data:%s}' % (self.user_id,
         self.name, self.score, ('在线' if self.is_inline else '离线'),
          self.register_data, self.login_data)
