from django.core.management.base import BaseCommand, CommandError
from ..appServices.EmailService import sendEmailTo
from signup.models import Subscriber

class Command(BaseCommand):
    help = 'Send emails to registered users'

    def handle(self, *args, **options):
        subscribers = Subscriber.objects.all()
        sendEmailTo(subscribers)