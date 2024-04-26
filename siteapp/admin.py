from django.contrib import admin
from .models import Post, Category
from django_summernote.admin import SummernoteModelAdmin##add suumernote

    
#below add summernote
class BlogAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'
###

admin.site.register(Post,BlogAdmin)#Blogadminを追加 summernote
admin.site.register(Category)

