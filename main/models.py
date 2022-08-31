from django.db import models
from datetime import datetime

# Create your models here.
class Ticket(models.Model):
    ticket_title = models.CharField(max_length=100)
    ticket_content = models.TextField()
    ticket_date = models.DateTimeField('date published', default=datetime.now)

    def __str__(self):
        return self.ticket_title
