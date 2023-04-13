from django.shortcuts import render, redirect
from .models import Article, Comment

# Create your views here.
def new(request):
    # return render(request, 'new.html')
    if request.method == 'POST':

        print(request.POST)

        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
            category = request.POST['category'], #Reverse for 'category' with no arguments not found. 1 pattern(s) tried:
        )
        return redirect('list')
    
    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    categories = []
    cate_num = []
    for article in articles:
        if article.category not in categories:
            categories.append(article.category)
            cate_list = Article.objects.filter(category=article.category)      

            cate_num.append( len(cate_list) )
    category_num = zip(categories, cate_num)
    return render(request, 'list.html', {'articles': articles, 'category_num': category_num})

def detail(request, article_id):
    article = Article.objects.get(id=article_id)

    if request.method == 'POST':
        content = request.POST['content']
        Comment.objects.create(
            article = article,
            content = content
        )
        return redirect('datail', article_id)

    return render(request, 'detail.html', {'article': article})

def category(request, category):
    articles = Article.objects.filter(category = category) #파이썬의 내장 함수인 filter()는 여러 개의 데이터로 부터 일부의 데이터만 추려낼 때 사용
    return render(request, 'category.html', {'articles': articles, 'category': category})