from django.urls import path
from . import views

app_name='blog'#�����ռ䣬������Ӧ��Ϊ������֯URL����ͨ�����ƶ�Ӧ��URL��
urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
    #�����Ŵ�URL�л�ȡ��Щ����
]