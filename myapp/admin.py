from django.contrib import admin
from .models import ContactMessage
from django.utils.html import format_html

# Correct Admin class
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('cname', 'email', 'message', 'file_photo', 'submitted_at')
    readonly_fields = ('submitted_at',)

    # Method to display file as a thumbnail (optional)
    def file_photo(self, obj):
        if obj.file:
            return format_html('<a href="{}">Download</a>', obj.file.url)
        return "-"
    file_photo.short_description = "File"

# Register the model
admin.site.register(ContactMessage, ContactMessageAdmin)
