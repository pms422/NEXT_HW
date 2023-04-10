from django.shortcuts import render,redirect
from .models import Post
from datetime import date

# Create your views here.
def home(request):
    posts	= Post.objects.order_by('deadline')

    # post_dayleft2 = [count_dayleft(post.deadline) for post in posts]
    #unsupported operand type(s) for -; 기본연산 불가능한 타입끼리 연산 시도했을 때
    # box = {
        # 'posts': zip(posts, post_dayleft2)
    # }
    today = date.today()
    # deadline = request.POST.get['deadline']
    # dayleft = (deadline - today)
    # return render(request, 'home.html', box)
    return render(request,	'home.html',	{	'posts' :	posts, 'today' : today	})

# def dayleftleft(request):
#    posts = Post.objects.all()
#    dayleft2 = count_dayleft(posts.deadline)

#    return render(request, 'detail.html', {'posts': posts, 'dayleft2': dayleft2})

# def count_dayleft(request):
#     today = datetime.today().date()
#     post_deadline = request.POST['deadline']
#     dayleft = (post_deadline - today)
    # targetday = datetime.date(2010,10,10)
    # values = today - targetday
  

    #return dayleft
# dayleft에서 오류가 나는 이유는?


def new(request):
    if request.method == 'POST':
        new_post = Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )     
        return redirect('detail',	new_post.pk)

    return render(request,	'new.html')

def detail(request,	post_pk):
    post	= Post.objects.get(pk=post_pk)

    return render(request,	'detail.html',	{'post':	post})

def update(request,	post_pk):
    post	= Post.objects.get(pk=post_pk)
    
    if request.method == 'POST':
        Post.objects.filter(pk=post_pk).update(
            title = request.POST['title'],
            content = request.POST['content'],
            deadline = request.POST['deadline'],
        )
        return redirect('detail',	post_pk)
    
    return render(request,	'update.html',	{'post':	post})

def delete(request,	post_pk):
    post	= Post.objects.get(pk=post_pk)
    post.delete()
    
    return redirect('home')