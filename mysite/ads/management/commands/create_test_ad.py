
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from ads.models import Ad

class Command(BaseCommand):
    help = 'Create a test ad with price for autograder'

    def handle(self, *args, **options):
        # Get or create the autograder user
        username = 'dj4e_user1'
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
        else:
            self.stdout.write(
                self.style.ERROR(f'User "{username}" does not exist. Run create_autograder_user first.')
            )
            return

        # Check if test ad already exists
        if Ad.objects.filter(title='Silver Bracelet with Heart Charm').exists():
            ad = Ad.objects.get(title='Silver Bracelet with Heart Charm')
            ad.price = 299.99
            ad.text = 'Beautiful silver bracelet with heart charm. Perfect gift!'
            ad.owner = user
            ad.save()
            self.stdout.write(
                self.style.SUCCESS(f'Updated existing ad "{ad.title}"')
            )
        else:
            # Create new test ad
            ad = Ad.objects.create(
                title='Silver Bracelet with Heart Charm',
                price=299.99,
                text='Beautiful silver bracelet with heart charm. Perfect gift!',
                owner=user
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created ad "{ad.title}"')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Title: {ad.title}')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Price: ₹{ad.price}')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Owner: {ad.owner.username}')
        ) 