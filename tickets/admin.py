from django.contrib import admin
from .models import Request, Ticket, Comments, Event_Logs


# Register your models here.
#admin.site.register(Password)
admin.site.register(Request)
admin.site.register(Ticket)
admin.site.register(Comments)
admin.site.register(Event_Logs)

