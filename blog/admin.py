from django.contrib import admin

# Register your models here.
from .models import Post

#admin.site.register(Post)
@admin.register(Post)#@admin.register()装饰器的功能与之前的admin.site.register()一样，用于将PostAdmin类注册成Post的管理类
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status',)#显示的字段
    list_filter = ('status', 'created', 'publish', 'author',)#筛选结果
    search_fields = ('title', 'body',)#可搜索的字段
    prepopulated_fields = {'slug': ('title',)}#设置了slug字段与title字段的对应关系
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish',)