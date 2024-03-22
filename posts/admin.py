from django.contrib import admin
from django.utils import timezone 
from .models import Post
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','draft','publish_date','get_tags','author']
    list_filter = ['draft','tags']
    search_fields = ['title',]
    def get_tags(self, post):
        tags = []
        for tag in post.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)
admin.site.register(Post,ProductAdmin)