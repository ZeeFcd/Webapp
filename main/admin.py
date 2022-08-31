from django.contrib import admin
from .models import Ticket
from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class TicketAdmin(admin.ModelAdmin):
    fieldsets = [
         ("Title/date", {'fields': ["ticket_title", "ticket_date"]}),
         ("Content", {"fields": ["ticket_content"]})
    ]

    formfield_overrides = {
         models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Ticket, TicketAdmin)
