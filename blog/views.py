from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.

def post_list(request):
    object_list = Post.published.all()
    paginator   = Paginator(object_list,3)
    page = request.GET.get('page')
    try:
        posts   = paginator.page(page)
    except EmptyPage:
        posts   = paginator.page(1)
    except PageNotAnInteger:
        posts   = paginator.page(paginator.num_pages)

    context = {
        'posts':posts,
        'page':page,
        'section':'blog',
    }

    return render(request,'blog/post_list.html',context)


def post_detail(request,pk,slug):
    post    = get_object_or_404(Post,pk=pk,slug=slug)
    return render(request,'blog/post_detail.html',{'section':'blog','post':post})

@login_required
@require_POST
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    print(post_id,action)
    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                print("adding")
                post.user_likes.add(request.user)
            else:
                print("removing")
                post.user_likes.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})
