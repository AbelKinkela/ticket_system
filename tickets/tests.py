from django.test import Client, TestCase
from .models import Request, Ticket, Comments
from django.contrib.auth import get_user_model

# Create your tests here.


#TESTING PAGE REQUESTS
class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_about_page_status_code(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)




#TESTING DATABASE TABLES
class UserTestCase(TestCase):
    def setUp(self):
        get_user_model().objects.create_user(username='John',email='jbeti200@caledonian.ac.uk',password='qwertyuioP+1')
        get_user_model().objects.create(username="Papy", email="pmaye200@caledonian.ac.uk", password='qwertyuioP+2')
    
    def test_user_details(self):
        john=get_user_model().objects.get(username="John")
        papy=get_user_model().objects.get(username="Papy")
        self.assertEqual(john.username, 'John')
        self.assertEqual(papy.email, 'pmaye200@caledonian.ac.uk')

class RequestTestCase(TestCase):

    def setUp(self):
        john=get_user_model().objects.create(username='John',email='jbeti200@caledonian.ac.uk',password='qwertyuioP+1')
        Request.objects.create(equipment_name="Projector", event_date='2020-04-08', description="Projector is needed for the class on the topic of plagiarism", user=john)
    
    def test_request_details(self):
        projector=Request.objects.get(equipment_name="Projector")
        self.assertEqual(projector.user.username, 'John')


# PRIORITY= (
#     ('LOW',"LOW"),('MEDIUM',"MEDIUM"),('HIGH',"HIGH")
# )
# TICKET_STATUS = (("OPEN","OPEN"),("IN_PROGRESS","IN PROGRESS"),("CLOSED","CLOSED"))
# TYPE_OF_TICKET = (("EQUIPMENT_AVAILABE","EQUIPMENT_AVAILABE"),("EQUIPMENT_NOT_AVAILABLE","EQUIPMENT NOT AVAILABLE"),("CLOSED","CLOSED"))



# class TicketTestCase(TestCase):

#     def setUp(self):

#             abel=User.objects.create( username="Abel", email="akinke200@caledonian.ac.uk", password='qwertyuioP+1')
#             papy=User.objects.create( username="Papy",  email="pmaye200@caledonian.ac.uk", password='qwertyuioP+1')
#             john=User.objects.create( username="John", email="jbeti200@caledonian.ac.uk", password='qwertyuioP+1')
#             projector=Request.objects.create(equipment_name="Projector", event_date='2020-04-08', description="Projector is needed for the class on the topic of plagiarism", user=john)
#             Ticket.objects.create(number=Ticket_Number_Generator(), ticket_type=TYPE_OF_TICKET[0], date="2020-04-08", item_collection_date="2020-04-18", item_collected=False, status=TICKET_STATUS[0], request=projector, priority=PRIORITY[0], creator=papy, assigned_To=abel)

#     def test_ticket_details(self):
#             gcuavs11=Ticket.objects.get(number="gcuavs11")
#             self.assertEqual(gcuavs11.request.user.email, 'jbeti200@caledonian.ac.uk')
#             self.assertEqual(gcuavs11.creator.email, 'pmaye200@caledonian.ac.uk')
#             self.assertEqual(gcuavs11.assigned_To.email, 'pmaye200@caledonian.ac.uk')