from django.contrib import admin

from .models import User
from post.models import Post


class PostInline(admin.TabularInline):
    model = Post
    extra = 0
    ordering = ('id',)
    fields = ('title', 'status', 'created')
    readonly_fields = ('created',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_verified', 'is_staff')
    inlines = (PostInline,)
    list_filter = ('groups', 'is_verified', 'is_staff')
