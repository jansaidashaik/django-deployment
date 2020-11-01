import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'udemy_project.settings')

import django

django.setup()

## FAKE POP_SCRIPT


import random
from udemy_app.models import Topic, Webpage, AccessRecord
from faker import Faker

fakegen = Faker()
topics = ["Search", "Social", "Marketplace", "News", "Games"]


def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t


def populate(N=5):
    for entry in range(N):
        # get the topic for the entry
        topic = add_topic()

        # Create the fake data for the entry
        fake_url = fakegen.url
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create the new Webpage Entry
        webpage = Webpage.objects.get_or_create(topic=topic, name=fake_name, url=fake_url)[0]

        # Create a fake access record for that webpage
        access_record = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)


if __name__ == '__main__':
    print("Populating Script")
    populate(20)
    print("Populating Complete")