import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FIRSTPROJECT.settings')

import django
django.setup()

from faker import Faker
from FIRSTAPPLICATION.models import User

fakegen = Faker()

def add_user(n):
    for i in range(n):
        name = fakegen.name()
        phone = fakegen.phone_number()
        address = fakegen.street_name()
        print(User.objects.get_or_create(first_name=name,Person_contact_No=phone,Person_address=address))

if __name__  ==  '__main__':
    a=add_user(30)
    print(a)