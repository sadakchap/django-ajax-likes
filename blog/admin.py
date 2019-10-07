from django.contrib import admin
from .models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','created','updated','status',)
    list_filter  = ('status','created','updated')
    prepopulated_fields = {'slug':('title',)}
