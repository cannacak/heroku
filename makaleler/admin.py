from django.contrib import admin
from .models import Makale



@admin.register(Makale)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","created_date"]
    list_display_links = ["created_date"]
    search_fields = ["title"]
    list_filter = ["created_date"]
    class Meta:

        model = Makale



