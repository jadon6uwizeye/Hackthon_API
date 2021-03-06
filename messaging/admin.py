from django.contrib import admin

from .models import Message, UserThread


class UserThreadAdmin(admin.ModelAdmin):
    list_display = ["thread", "user", "unread", "deleted"]
    list_filter = ["unread", "deleted"]



class MessageAdmin(admin.ModelAdmin):
    list_display = ["thread", "sender", "sent_at"]
    list_filter = ["sent_at", "thread"]
    raw_id_fields = ["sender"]


admin.site.register(UserThread, UserThreadAdmin)
admin.site.register(Message, MessageAdmin)
