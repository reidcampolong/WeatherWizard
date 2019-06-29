from django.core.management.base import BaseCommand, CommandError
from signup.models import Subscriber

class Command(BaseCommand):
    help = 'Send emails to registered users'

    def handle(self, *args, **options):
        subscribers = Subscriber.objects.all()
        for subscriber in subscribers:
          print("Sending email to " + str(subscriber))