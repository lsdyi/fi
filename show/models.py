from django.db import models

# Create your models here.

#创建温度的数据表 模型
class Temperature(models.Model):
    time = models.DateField(auto_now_add=True)      #时间属性
    tem = models.FloatField()   #温度属性
    pic1 = models.CharField(max_length=100, null=True, blank=True)      #正演图属性
    pic2 = models.CharField(max_length=100, null=True, blank=True)      #反演图属性

    def __str__(self):
        return "时间："+(str)(self.time)+"\n温度："+(str)(self.tem)
    
    class Meta:
        ordering = ['-id']
