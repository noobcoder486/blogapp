from django.shortcuts import render

post=[
    {
        'title': "Shubham's First Blog",
        'author': "Shubham Dubey",
        'content': "My First Post",
        'date_posted': "30, August",
    },
    {
        'title': "Shubham's Second Blog",
        'author': "Shubham Dubey",
        'content': "My Second Post",
        'date_posted': "29, August",
    }
]

def home(request):
    context={
        'posts':post,
    }
    return render(request, 'blog/home.html/', context)

def about(request):
    return render(request,'blog/about.html', {'title': "About"})
