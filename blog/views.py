from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.utils import timezone
from .models import Post
from django.template import RequestContext
from .forms import PostForm


# Create your views here.
def post_list(request):
	posts = Post.objects.all()#.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post':post})

def post_new(request):
    if request.method == "POST":
    	form = PostForm(request.POST)
    	if form.is_valid():
    		post = form.save(commit=False)
    		post.author = request.user
    		post.published_date = timezone.now()
    		post.save()
    		return redirect('post_detail', pk=post.pk)
    else:
    	form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

# def handler404(request, exception, template_name="404.html"):
#  	response = render_to_responce('404.html')
#  	response.status_code = 404
#  	return response

