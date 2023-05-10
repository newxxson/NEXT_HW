from django.contrib import admin
from Blog.models import Post, Comment
# Register your models here.

class CommentInLine(admin.TabularInline):
    model = Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','create_dt']
    list_display_links = ['id','title']
    list_filter = ['create_dt', 'author']
    search_fields = ['title', 'author']
    inlines = [CommentInLine,]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id' ,'post','comment', 'author']
