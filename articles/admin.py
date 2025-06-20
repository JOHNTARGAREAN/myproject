from django.contrib import admin
from .models import Article, Comment

class CommentInline(admin.StackedInline):  # new
    model = Comment

class ArticleAdmin(admin.ModelAdmin):  # new
    inlines = [
        CommentInline,
    ]

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment) 
# Register your models here.
