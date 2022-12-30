from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("author", "expense", "description")


admin.site.register(Post, PostAdmin)
