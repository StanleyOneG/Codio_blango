from django.contrib import admin
from blog.models import Tag, Post, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    # fields = ('author', 'published_at',
    #           'slug', 'title', 'summary',
    #           'content')
    # list_display = ('slug', 'published_at')



admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)