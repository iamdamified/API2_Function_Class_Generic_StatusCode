from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ["post", "name", "message"]

admin.site.register(Comment, CommentAdmin)

# Register your models here.
