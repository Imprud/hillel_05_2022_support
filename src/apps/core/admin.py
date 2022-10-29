from django.contrib import admin

from apps.core.models import Comment, Ticket

# Register your models here.
# admin.site.register(User)


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ["__str__", "id", "operator", "client", "theme"]
    list_filter = ("operator",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["id", "ticket", "ticket_text"]
    list_display_links = ["ticket"]

    @admin.display(description="Ticket text")
    def ticket_text(self, obj):
        return f"{obj.text[:20]}"
