from django.contrib import admin


#先引入我们的数据表模型
from .models import Temperature    #写相对路径 引入温度数据表

# Register your models here.
admin.site.register(Temperature)
