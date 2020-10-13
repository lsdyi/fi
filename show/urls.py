from django.conf.urls import url

#导入views模块以便使用其中的函数
from . import views

urlpatterns = [
    #所有的url指向的函数都写在这里
    url(r"^details/$", views.details, name="details"),
    url(r"^details1/$", views.details1, name="details1"),
]
