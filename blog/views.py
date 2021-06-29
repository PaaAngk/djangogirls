from django.shortcuts import render
from .models import Post
from django import template
from socket import socket
from .models import Сomments
from .models import SubСomments
from django.utils import timezone
from .forms import PostForm
from .forms import СommentsForm
from .forms import SubСommentsForm
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from anytree import Node, LevelOrderIter, PreOrderIter
from anytree.exporter import JsonExporter
from anytree.importer import JsonImporter

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

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

def post_detail(request, pk):
	post = get_object_or_404(Post, pk=pk)
	comments = Сomments.objects.filter(post__id=pk).order_by('published_date')
	max = 0
	for commlen in comments:
		if commlen.levels > max:
			max = commlen.levels
	notes = []
	commlist = []
	root = Node("Root")
	for commid in comments:
		if commid.levels == 1:
			notes.append(Node(commid, parent=root))
			commlist.append(commid.id)

	for x in range(2,max+1):
		for comm in comments:
			if comm.levels == x:
				notes.append(Node(comm, parent=notes[commlist.index(comm.comment)]))
				commlist.append(comm.id)
	exp = [node.name for node in PreOrderIter(root)]
	return render(request, 'blog/post_detail.html', {'post': post, "comments" : len(comments), "exp" : exp})

register = template.Library()
@register.filter
def mul(value):
    return value * 2

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def comment_new(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = СommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.levels = 1
            comment.comment = 0
            comment.published_date = timezone.now()
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = СommentsForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def sub_comment_new(request, postpk, commentpk):
    post = get_object_or_404(Post, pk=postpk)
    subcomment = get_object_or_404(Сomments, pk=commentpk)
    if request.method == "POST":
        form = СommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.levels = subcomment.levels + 1
            comment.comment = subcomment.id
            comment.parent = False
            comment.published_date = timezone.now()
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = СommentsForm()
    return render(request, 'blog/post_edit.html', {'form': form})