from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Blog

from .forms import BlogForm

# Create your views here.


def blog(request):
    """ A view to return the blog page """

    blogs = Blog.objects.all()

    context = {
        'blogs': blogs,
    }

    return render(request, 'blog/blog.html', context)


def blog_post(request, slug):
    """ A view to return individual blog post page """

    blog = get_object_or_404(Blog, slug=slug)

    context = {
        'blog': blog,
    }

    return render(request, 'blog/blog_post.html', context)


@login_required
def add_blog(request):
    """ Add a blog post to the blog """
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save()
            messages.success(request, 'Successfully added a blog post!')
            return redirect(reverse('blog_post', args=[blog.slug]))
        else:
            messages.error(request, 'Failed to add the blog post. Please ensure the form is valid.')
    else:
        form = BlogForm()

    template = 'blog/add_blog.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_blog(request, slug):
    """ Edit a product in the store """
    blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated blog post!')
            return redirect(reverse('blog_post', args=[blog.slug]))
        else:
            messages.error(request, 'Failed to update blog post. Please ensure the form is valid.')
    else:
        form = BlogForm(instance=blog)
        messages.info(request, f'You are editing {blog.title}')

    template = 'blog/edit_blog.html'
    context = {
        'form': form,
        'blog': blog,
    }

    return render(request, template, context)