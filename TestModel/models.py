from django.db import models

# # Create your models here.
# class Test(models.Model):
#     name = models.CharField(max_length=20)

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)




# from django.contrib.auth.models import AbstractUser
# from django.db import models

# class CustomUser(AbstractUser):
#     # 添加自定义字段（可选）
#     # my_custom_field = models.CharField(max_length=100)
#     pass
