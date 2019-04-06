import os

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "FORMS.settings")

django.setup()

###
import random
from app.models import AccessRecord, WebPage, Topic
from faker import Faker

fakegen = Faker()

topics = ["search", 'social', 'Marketplace', 'News']

def add_topic():

    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get topics
        top = add_topic()
        # create fake data

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #Create wpage entry
        webpg = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        #Create fake A-AccessRecord
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]


if __name__ == '__main__':

    print("Populating...")
    populate(20)
    print("Done.")
