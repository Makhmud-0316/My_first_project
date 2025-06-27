from django.contrib import admin
from .models import Member

@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'joined_date')
    search_fields = ('first_name', 'last_name')
    prepopulated_fields = {"slug": ("first_name", "last_name")}

