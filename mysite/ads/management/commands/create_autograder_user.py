from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create the autograder user account'

    def handle(self, *args, **options):
        username = 'dj4e_user1'
        password = 'Meow_5a9bae_41'
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            user.set_password(password)
            user.save()
            self.stdout.write(
                self.style.SUCCESS(f'Updated existing user "{username}" with new password')
            )
        else:
            # Create new user
            user = User.objects.create_user(
                username=username,
                password=password,
                email='dj4e_user1@example.com'
            )
            self.stdout.write(
                self.style.SUCCESS(f'Successfully created user "{username}"')
            )
        
        self.stdout.write(
            self.style.SUCCESS(f'Username: {username}')
        )
        self.stdout.write(
            self.style.SUCCESS(f'Password: {password}')
        ) 