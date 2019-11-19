from django.shortcuts import render
from .models import Post
from django.shortcuts import render,get_object_or_404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import EmailPostForm
# Create your views here.

def post_list(request):
    posts = Post.published.all()
    object_list = Post.published.all()
    paginator = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # 如果page参数不是一个整数就返回第一页
        posts = paginator.page(1)
    except EmptyPage:
        # 如果页数超出总页数就返回最后一页
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',{'page':page,"posts":posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
def post_share(request, post_id):
    # 通过id 获取 post 对象
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == "POST":
        # 表单被提交
        form = EmailPostForm(request.POST)#使用request.POST中包含的表单数据创建一个表单对象
        if form.is_valid():# 验证表单数据

            cd = form.cleaned_data #访问表单内所有通过验证的数据
            # 发送邮件......
    else:
        form = EmailPostForm() #创建一个空白的form对象
    return render(request, 'blog/post/share.html', {'post': post, 'form': form})
