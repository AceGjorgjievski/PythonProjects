from django.contrib import admin

# Register your models here.
from .models import Book, Author, PublicationAuthor, PublishHouse


class AuthorAdmin(admin.ModelAdmin):

    list_display = ("name_surname", "year_birth", "country", "count_book")
    list_filter = ("name_surname", "year_birth", "country")
    search_fields = ("name_surname__startswith",)

    def count_book(self, author):
        from django.utils.html import format_html
        books_filtered = Book.objects.filter(author=author).count()
        return format_html(f"<b>{books_filtered}</b>")

    count_book.description = "Number of books by author"

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish_house")

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(author=request.user)

admin.site.register(Book, BookAdmin)

class PublicationAuthorAdmin(admin.StackedInline):
    model = PublicationAuthor
    extra = 2

class PublicationBookAdmin(admin.TabularInline):
    model = Book
    readonly_fields = ('title', 'isbn', )
    extra = 2

class PublicationAdmin(admin.ModelAdmin):
    inlines = [PublicationAuthorAdmin, PublicationBookAdmin, ]


admin.site.register(PublishHouse, PublicationAdmin)
