from django.contrib import admin

# Register your models here.
from student.models import Student,StudentDetail



class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','age','sex','qq','phone','c_time']
    list_display_links = ['name','sex'] #默认id 可设置多个跳转
    list_filter = ['sex']# 可设置多个 and 关系
    search_fields = ['name','qq','phone']#自定义搜索字段条件
    list_per_page = 3 #每页显示数量
    #详情页面
    #fields = ['name','sex'] #只允许修改的字段
    fieldsets = [
        (None,{'fields':['name','sex']}),
        ('详细信息',{'fields':['qq','phone','grade']}),
        ('设置',{'fields':['is_delete']}),
    ]

admin.site.register(Student,StudentAdmin)
admin.site.register(StudentDetail)