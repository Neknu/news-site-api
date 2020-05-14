from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'author', 'status', 'created']
    fieldsets = [
        ('User content', {'fields': ['title', 'content', 'author']}),
        ('Admin info', {'fields': ['status', 'slug', 'created']}),
    ]
    readonly_fields = ['created', 'slug']
    search_fields = ['title', 'content']
    list_filter = ['status', 'created', 'author']
    ordering = ('created',)


admin.site.site_header = "News Site Admin"
admin.site.site_title = "Portal to post your news here"
admin.site.index_title = "News Site Admin"
