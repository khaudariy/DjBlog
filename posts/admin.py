from django.contrib import admin
from django.utils import timezone 
from .models import Post ,Category, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.
class ProductAdmin(SummernoteModelAdmin):
    list_display = ['title','draft','publish_date','get_tags','author','category']
    list_filter = ['draft','tags','category']
    search_fields = ['title',]
    summernote_fields = ('content')
    def get_tags(self, post):
        tags = []
        for tag in post.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)
admin.site.register(Post,ProductAdmin)
admin.site.register(Category)
admin.site.register(Comment)
