from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post

admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin): # When used in this way, some JavaScript is inserted into the admin page so that the slug field updates when the title field changes. It will automatically “slugify” the title. But, there are many other ways to customise the ModelAdmin.
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('slug', 'published_at')

admin.site.register(Post, PostAdmin)
