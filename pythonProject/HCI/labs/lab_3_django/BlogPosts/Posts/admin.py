from django.contrib import admin

# Register your models here.
from .models import *


class BlogPostUserAdmin(admin.ModelAdmin):

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "content",)
    list_filter = ("date_created",)
    search_fields = ("title", "content")

    # fields = ("author", "title",)

    def has_change_permission(self, request, obj=None):
        if obj and obj.author == request.user or request.user.is_superuser:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if obj and obj.author == request.user or request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        # if obj and request.user.is_superuser or \
        all_blockers = Block.objects.all()
        # ako NE postoi blokiran, togash so not kje mi dade True priviledija
        if not Block.objects.filter(user_blocked__user=request.user).exists() or request.user.is_superuser:
            return True
        return False

    def has_add_permission(self, request):
        return True


class CommentAdmin(admin.ModelAdmin):
    list_display = ("content", "date_created",)

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.author.user or \
                obj and ((request.user == obj.author.user) or (request.user == obj.post.author)) or \
                request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.author.user or \
                request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        # if obj and request.user.is_superuser or \
        # ako NE postoi blokiran, togash so not kje mi dade True priviledija
        if not Block.objects.filter(user_blocked__user=request.user).exists() or request.user.is_superuser:
            return True
        return False


def has_add_permission(self, request):
    if not request.user.is_superuser:
        return True
    return False


class BlockAdmin(admin.ModelAdmin):
    def has_change_permission(self, request, obj=None):
        if obj and request.user == obj.user_blocker.user:
            return True
        return False

    def has_add_permission(self, request):
        return True

    def has_view_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        if obj and request.user == obj.user_blocker.user:
            return True
        return False


admin.site.register(BlogPostUser, BlogPostUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Block, BlockAdmin)
