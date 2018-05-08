from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# 글목록 조회
def post_list(request):
    #name = 'Django~~'
    #return HttpResponse('''<h1>Hello {myname}</h1>'''.format(myname=name))
    #queryset 사용해서 Post 목록 가져오기
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all().order_by('published_date')
    return render(request,'blog/post_list.html',{'posts':posts})

# 글상세조회
def post_detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'blog/post_detail.html',{'post':post})

