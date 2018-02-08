from django.db import models
from user import models as md
# Create your models here.
class Message(models.Model):
    from_user_id = models.CharField(max_length=20)
    to_user_id = models.CharField(max_length=20)
    text = models.CharField(max_length=200)
    message_date = models.DateTimeField(auto_now_add=True)
    is_show = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=False)
    def __str__(self):
        return '{from: %s, to: %s, text: %s, date: %s, is_show: %s, is_read: %s, is_delete: %s}' % (self.from_user_id, self.to_user_id,
        self.text, self.message_date, '已经展示' if self.is_show else '暂未展示', '已经阅读' if self.is_read else '暂未阅读', '已经删除' if self.is_delete else '暂未删除')