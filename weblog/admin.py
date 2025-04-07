from django.contrib import admin
from .models import (
    Post,Contact
)
# Register your models here.

def make_published(modeladmin,request,queryset):
    queryset.update(status = "Published")

make_published.short_descriptions = 'Published Post'

def make_draft(modeladmin,request,queryset):
    queryset.update(status = 'Draft')

make_draft.short_descriptions = 'Draft Post'

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','status','slug','published_date']

    actions = [make_published,make_draft]

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['username','email']