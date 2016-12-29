from django.contrib import admin
# Register your models here.
from polls.models import Poll,Choice

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class PollAdmin(admin.ModelAdmin):
    #添加投票记录表单设置
    fieldsets = [
        (None,{'fields':['question']}),
        ('发布日期',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    #列表显示的项
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    #帅选条件
    list_filter = ['pub_date']
    #搜索
    search_fields = ['question']
    #根据日期来向下钻取记录
    date_hierarchy = 'pub_date'

#admin.site.register(Poll) #直接创建投票记录
admin.site.register(Poll,PollAdmin)  #创建投票记录同时还能创建投票选项
admin.site.register(Choice)
