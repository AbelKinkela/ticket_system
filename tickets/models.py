from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

#USER MODEL
# class User(models.Model):
#     first_name=models.CharField(max_length=30,  blank=False)
#     last_name=models.CharField(max_length=30,  blank=False)
#     email=models.EmailField(blank=False)
#     def __str__(self):
#         return "%s %s" % (self.first_name, self.last_name)

#PASSWORD MODEL
# class Password(models.Model):
#     password=models.CharField(max_length=30, blank=False)
#     is_active=models.CharField(max_length=3,  blank=False)
#     created_date=models.DateField(auto_now=True)
#     created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
#     def __str__(self):
#         return "%s %s %s" % (self.pk, self.password, self.is_active)

#EVENT LOGS
TYPE_OF_EVENT=(("LOGIN","LOGIN"), ("LOGOUT", "LOGOUT"), ("REGISTER", "REGISTER"))
class Event_Logs(models.Model):
    user=models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    event_type=models.CharField(choices=TYPE_OF_EVENT, max_length=15)
    start_date=models.DateField(auto_now=True)
    def __str__(self):
        return "%s %s %s" % (self.pk, self.event_type, self.user.email)
#REQUEST MODEL
class Request(models.Model):
    equipment_name=models.CharField(max_length=60)
    event_date=models.DateField()
    description=models.TextField()
    user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    def __str__(self):
        return "%s %s %s" % (self.pk, self.equipment_name, self.user.first_name)
    def get_absolute_url(self): # new
        return reverse('request_detail', args=[str(self.pk)])

# TICKET MODEL
PRIORITY= (
    ('LOW',"LOW"),('MEDIUM',"MEDIUM"),('HIGH',"HIGH")
)
TICKET_STATUS = (("OPEN","OPEN"),("IN_PROGRESS","IN PROGRESS"),("CLOSED","CLOSED"))
TYPE_OF_TICKET = (("EQUIPMENT_AVAILABE","EQUIPMENT_AVAILABE"),("EQUIPMENT_NOT_AVAILABLE","EQUIPMENT NOT AVAILABLE"),("CLOSED","CLOSED"))
class Ticket(models.Model):
    ticket_type = models.CharField(choices=TYPE_OF_TICKET, max_length=23, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    item_collection_date = models.DateTimeField()
    item_collected=models.BooleanField(blank=True)
    status = models.CharField(choices=TICKET_STATUS, max_length=11)
    request = models.ForeignKey(Request, on_delete=models.CASCADE)
    priority = models.CharField(choices= PRIORITY,max_length=7)
    creator = models.ForeignKey(get_user_model(), related_name='%(class)s_requests_created', on_delete= models.DO_NOTHING)
    assigned_To = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    def __str__(self):
        return "%s %s %s %s %s" % (self.id, self.request.equipment_name, self.ticket_type, self.status, self.priority)
    
class Comments(models.Model):
    ticket = models.ForeignKey(Ticket,on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete= models.DO_NOTHING)
    def __str__(self):
        return "%s %s %s" % (self.ticket.number, self.user.first_name, self.body[:30])

