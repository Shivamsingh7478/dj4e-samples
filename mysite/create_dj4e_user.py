from django.contrib.auth.models import User

username = 'dj4e_user'
password = 'Meow_dee7f5_42'

if not User.objects.filter(username=username).exists():
    User.objects.create_user(username, password=password)
    print('User created!')
else:
    print('User already exists.') 