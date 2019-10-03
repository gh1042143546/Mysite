from django.urls import path
from . import views

app_name='blog'#命名空间，方便以应用为中心组织URL并且通过名称对应到URL上
urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    #尖括号从URL中获取这些参数
]