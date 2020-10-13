from django.shortcuts import render


#导入数据表模型 以便增删查改
from .models import Temperature


# Create your views here.

#用于展示温度 正演图和反演图等细节信息
def details(request):
    print(request.POST.get("daterange"))

    #import response from django.http
    # from django.http import HttpResponse, JsonResponse
    # return HttpResponse('hello world')

    value = range(5)

    #获取数据表中对应日期的所有记录
    #result用于储存最终返回到模板中的结果
    result = []
    
    #先获得所有的记录对象
    temperatures = Temperature.objects.all()

    #导入python中的日期模块
    import datetime

    #开始对所有记录中按满足要求的进行检查
    for tem in temperatures:
        if tem.time == datetime.date.today():
            result.append(tem)

    context = {             
            "value":value,
            "result":result     #注意 返回的result是一个列表 在页面中使用的使用应该先把元素取出来再用哦！！！
            }

    return render(request, "details.html", context)

def details1(request):
    res = request.POST.get("daterange")
    print("dsadsa", res)
    
    dates = res.split(" ")
    print(dates)
    
    
    date1 = dates[0].split("/")
    date2 = dates[2].split("/")

    print(date1, date2)
    
    #获取数据表中对应日期的所有记录
    #result用于储存最终返回到模板中的结果
    result = []
    
    #先获得所有的记录对象
    temperatures = Temperature.objects.all()

    #导入python中的日期模块
    import datetime

    # 开始对所有记录中按满足要求的进行检查
    for tem in temperatures:
        if tem.time >= datetime.date((int)(date1[0]),(int)(date1[1]),(int)(date1[2])) and tem.time <= datetime.date((int)(date2[0]),(int)(date2[1]),(int)(date2[2])):
            result.append(tem)
            print(tem)
    from django.core import serializers
    context = {             
            "result":serializers.serialize("json", result)     #注意 返回的result是一个列表 在页面中使用的使用应该先把元素取出来再用哦！！！
            }
    print("hello world")
    print(serializers.serialize("json", result))

    # from django.http import HttpResponseRedirect
    # return HttpResponse("hello world")
    # return HttpResponseRedirect("/show/details1/")
    # return render(request, "details1.html", context)
    from django.http import JsonResponse
    return JsonResponse({
        "result":serializers.serialize("json", result)
    })