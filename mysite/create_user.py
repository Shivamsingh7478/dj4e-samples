from django.contrib.auth.models import User

username = 'dj4e_user'
password = 'Meow_dee7f5_42'

if not User.objects.filter(username=username).exists():
    print(f"Creating user '{username}'...")
    user = User.objects.create_user(username=username, password=password)
    user.save()
    print("User created successfully.")
else:
    print(f"User '{username}' already exists.") 