'''
Description: 
Author: limaochao
Date: 2020-12-30 22:51:50
LastEditTime: 2020-12-31 09:58:11
'''
from django.db import models
from django.contrib.auth.models import User
class FixedCharField(models.Field):
    """
    自定义的 char 类型的字段类
    """
    def __init__(self, max_length, *args, **kwargs):
        self.max_length = max_length
        super(FixedCharField, self).__init__(max_length=max_length, *args, **kwargs)
 
    def db_type(self, connection):
        """
        限定生成数据库表的字段类型为 char，长度为 max_length 指定的值
        """
        return 'char(%s)' % self.max_length

# Create your models here.
class Cameras(models.Model):
    camera_id = models.CharField(max_length=32, verbose_name="标识", primary_key=True)
    camera_name = models.CharField(max_length=128, verbose_name="标签", blank=True)
    access_key_id = models.CharField(max_length=32, verbose_name="令牌", blank=True)
    access_key_secret = models.CharField(max_length=128, verbose_name="令牌密码", blank=True)
    link = models.CharField(max_length=1024, name='link', verbose_name="地址", blank=False)
    region = models.CharField(max_length=128, name='region', verbose_name="区域", blank=False)
    user = models.ForeignKey(
        User, 
        related_name='user_cameras',
        verbose_name="用户", 
        on_delete=models.CASCADE
    )

    class Meta:
        db_table = 'Cameras'
        managed = True
        verbose_name = '摄像头'
        verbose_name_plural = '摄像头'

