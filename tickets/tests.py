from django.test import SimpleTestCase, TestCase
from .models import Request, Ticket, Comments, Ticket_Number_Generator
from django.core.exceptions import ValidationError

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
        User.objects.create(first_name="John", last_name="Betilson", email="jbeti200@caledonian.ac.uk")
        User.objects.create(first_name="Papy", last_name="Mayela", email="pmaye200@caledonian.ac.uk")
    
    def test_user_details(self):
        john=User.objects.get(first_name="John")
        papy=User.objects.get(first_name="Papy")
        self.assertEqual(john.first_name, 'John')
        self.assertEqual(papy.last_name, 'Mayela')

class RequestTestCase(TestCase):

    def setUp(self):
        john=User.objects.create(first_name="John", last_name="Betilson", email="jbeti200@caledonian.ac.uk")
        Request.objects.create(equipment_name="Projector", event_date='2020-04-08', description="Projector is needed for the class on the topic of plagiarism", user=john)
    
    def test_request_details(self):
        projector=Request.objects.get(equipment_name="Projector")
        self.assertEqual(projector.user.first_name, 'John')


# PRIORITY= (
#     ('LOW',"LOW"),('MEDIUM',"MEDIUM"),('HIGH',"HIGH")
# )
# TICKET_STATUS = (("OPEN","OPEN"),("IN_PROGRESS","IN PROGRESS"),("CLOSED","CLOSED"))
# TYPE_OF_TICKET = (("EQUIPMENT_AVAILABE","EQUIPMENT_AVAILABE"),("EQUIPMENT_NOT_AVAILABLE","EQUIPMENT NOT AVAILABLE"),("CLOSED","CLOSED"))



# class TicketTestCase(TestCase):

#     def setUp(self):
#         with self.assertRaises(ValidationError):
#             abel=User.objects.create(first_name="Abel", last_name="Kinkela", email="akinke200@caledonian.ac.uk")
#             papy=User.objects.create(first_name="Papy", last_name="Mayela", email="pmaye200@caledonian.ac.uk")
#             john=User.objects.create(first_name="John", last_name="Betilson", email="jbeti200@caledonian.ac.uk")
#             projector=Request.objects.create(equipment_name="Projector", event_date='2020-04-08', description="Projector is needed for the class on the topic of plagiarism", user=john)
#             Ticket.objects.create(number=Ticket_Number_Generator(), ticket_type=TYPE_OF_TICKET[0], date="2020-04-08", item_collection_date="2020-04-18", item_collected=False, status=TICKET_STATUS[0], request=projector, priority=PRIORITY[0], creator=papy, assigned_To=abel)

#     def test_ticket_details(self):
#         with self.assertRaises(ValidationError):
#             gcuavs11=Ticket.objects.get(number="gcuavs11")
#             self.assertEqual(gcuavs11.request.user.email, 'jbeti200@caledonian.ac.uk')
#             self.assertEqual(gcuavs11.creator.email, 'pmaye200@caledonian.ac.uk')
#             self.assertEqual(gcuavs11.assigned_To.email, 'pmaye200@caledonian.ac.uk')