from django.db import models
from Blog.models import Post


# Create your models here.


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    message = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.post.title}"
    

PRODUCT_CATEGORY_CHOICES = (
    ("D", "Discounted"),
    
)