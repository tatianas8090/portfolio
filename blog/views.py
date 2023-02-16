from django.shortcuts import render, get_object_or_404
from .models import post
# Create your views here.



def posts(request):
    posts=post.objects.all()
    return render(request, 'posts.html', {'posts': posts})


def post_detail(request, post_id):
    posts=get_object_or_404(post, pk=post_id )
    return render(request, 'post_detail.html', {'posts': posts})    
