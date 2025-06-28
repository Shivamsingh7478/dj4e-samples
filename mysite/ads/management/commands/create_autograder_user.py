from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Create the autograder user accounts'

    def handle(self, *args, **options):
        users_data = [
            {
                'username': 'dj4e_user1',
                'password': 'Meow_5a9bae_41',
                'email': 'dj4e_user1@example.com'
            },
            {
                'username': 'dj4e_user2',
                'password': 'Meow_42_5a9bae',
                'email': 'dj4e_user2@example.com'
            }
        ]
        
        for user_data in users_data:
            username = user_data['username']
            password = user_data['password']
            email = user_data['email']
            
            # Check if user already exists
            if User.objects.filter(username=username).exists():
                user = User.objects.get(username=username)
                user.set_password(password)
                user.email = email
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'Updated existing user "{username}" with new password')
                )
            else:
                # Create new user
                user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email
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
            self.stdout.write('---') 