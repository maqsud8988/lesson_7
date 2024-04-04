from django.contrib import admin
from .models import Book, Author, BookingBook, Comments
from import_export.admin import ImportExportModelAdmin


@admin.register(Author)
class AuthorAdmin(ImportExportModelAdmin):
    search_fields = ['name', 'country']

@admin.register(Book)
class BookAdmin(ImportExportModelAdmin):
    list_display =("id", "title", "description", "price", "count", "author", "create_date")
    list_display_links =("id", "title", "description", "price", "count", "author", "create_date")
    search_fields = ['title', 'author__name']
    ordering = ("title", "author")
    autocomplete_fields = ("author", )

@admin.register(BookingBook)
class BookingBookAdmin(ImportExportModelAdmin):
    list_display = ("id", "student", "book", "take_date", "returned_date")

    def student(self):
        return self.count()

    def book(self):
        return self.count()

@admin.register(Comments)
class BookAdmin(admin.ModelAdmin):
    list_display = ("id", "text", "student")





# admin.site.register(Author)
# admin.site.register(BookingBook)
# admin.site.register(Comments)