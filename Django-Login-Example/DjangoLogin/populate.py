import os

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DjangoLogin.settings")

django.setup()

###
import random
from Login.models import Name
from faker import Faker

fakegen = Faker()
def create_entry():

    f_name = fakegen.name()
    f_last = fakegen.name()
    f_email = fakegen.email()
    webpg = Name.objects.get_or_create(top_name=f_name,last_name=f_last, email=f_email)[0]


if __name__ == '__main__':
    for x in range(100):
        create_entry()
    print("Populating Done")
