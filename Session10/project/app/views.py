from django.shortcuts import render, redirect
from .models import Post, Comment, Re_Comment


def home(request):
   posts = Post.objects.all()


   return render(request, 'home.html', {'posts':posts})


def new(request):
   if request.method == "POST":
       title = request.POST['title']
       content = request.POST['content']


       new_post = Post.objects.create(
           title=title,
           content=content)
       return redirect('detail', new_post.pk)
  
   return render(request, 'new.html')


def detail(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   print(post)
   if request.method == 'POST':
       content = request.POST['content']
       Comment.objects.create(
           post = post,
           content = content
       )
       return redirect('detail', post_pk)

   return render(request, 'detail.html', {'post':post})




def edit(request, post_pk):
   post = Post.objects.get(pk=post_pk)


   if request.method == 'POST':
       title = request.POST['title']
       content = request.POST['content']
       Post.objects.filter(pk=post_pk).update(
           title=title,
           content=content
       )
       return redirect('detail', post_pk)


   return render(request, 'edit.html', {'post':post})




def delete(request, post_pk):
   post = Post.objects.get(pk=post_pk)
   post.delete()

   return redirect('home')

def delete_comment(request, post_pk, comment_pk):
   comment = Comment.objects.get(pk=comment_pk)
   comment.delete()

   return redirect('detail', post_pk)



# def recomment (request, post_pk, comment_pk):
#    post = Post.objects.get(pk=post_pk)
#    if request.method == 'POST':
#       comment = Comment.objects.get(pk=comment_pk)
#       content = request.POST['re_content']
#       Comment.objects.create(
#          post = post,
#          content = content,
#          parent_comment = comment,
#       )

def recomment(request, post_pk, comment_pk):
    comment=Comment.objects.get(id=comment_pk)
    if request.method=="POST":
        Re_Comment.objects.create(
            comment=comment,
            content=request.POST['content'],
        )
        return redirect('detail', post_pk)
    
def delete_recomment(request, post_pk, recomment_pk):
   recomment = Re_Comment.objects.get(pk = recomment_pk)
   recomment.delete()

   return redirect('detail', post_pk)


