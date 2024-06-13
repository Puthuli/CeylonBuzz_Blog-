from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

posts = [
    {
        'author': 'P.P.S.Perera',
        'title': 'Blog_Post 1',
        'content': 'This is my first blog post',
        'date_posted': '12th June 2024'
    },
    {
        'author': 'B.A.S.D.Dayananda',
        'title': 'Blog_Post 2',
        'content': 'This is second first blog post',
        'date_posted': '12th April 2024'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'CeylonBuzz'})

def new_blog_post(request):
    return render(request, 'new_blog_post.html')

def profile(request):
    return render(request, 'blog/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

