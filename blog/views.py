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
        # ���page��������һ�������ͷ��ص�һҳ
        posts = paginator.page(1)
    except EmptyPage:
        # ���ҳ��������ҳ���ͷ������һҳ
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',{'page':page,"posts":posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})
def post_share(request, post_id):
    # ͨ��id ��ȡ post ����
    post = get_object_or_404(Post, id=post_id, status='published')
    if request.method == "POST":
        # �����ύ
        form = EmailPostForm(request.POST)#ʹ��request.POST�а����ı����ݴ���һ��������
        if form.is_valid():# ��֤������

            cd = form.cleaned_data #���ʱ�������ͨ����֤������
            # �����ʼ�......
    else:
        form = EmailPostForm() #����һ���հ׵�form����
    return render(request, 'blog/post/share.html', {'post': post, 'form': form})
