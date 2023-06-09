from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
   title = models.CharField(max_length=50)
   content = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=1)

   def __str__(self):
       return self.title
   
class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()
   author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')

   def __str__(self):
       return self.content

class Re_Comment(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='re_comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='re_comments')


    
    def __str__(self):
        return self.content


