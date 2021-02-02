# os
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# django
import django
django.setup()

# random
import random, decimal, string

# faker
from faker import Faker
fake_data = Faker()

# custom app models
from dushanbe.models import Bill


unit_choices = ['m', 'kits', 'sum', 'n']


# random string generator for project_ID and site_ID
def random_string_id(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


# populating the other classes
def populate(n):
    for entry in range(n):

        # creating objects
        # topics = Topic.objects.create(
        #     topic_name=random_string_id(10)
        # )

        # creating objects
        # materials = Material.objects.create(
        #     material_name=random_string_id(10),
        #     item_serial_no=random_string_id(6),
        #     unit=random.choice(unit_choices),
        #     quantity=decimal.Decimal(random.randrange(155, 389))/100,
        # )

        # creating objects]
        Bill.objects.create(
            bill_name=random_string_id(10),
            topic_name=random_string_id(10),
            material_name=random_string_id(10),
            item_serial_no=random_string_id(6),
            unit=random.choice(unit_choices),
            quantity=decimal.Decimal(random.randrange(155, 389)) / 100,
            submission_date=fake_data.date(),
            work_progress=random.randint(0, 10),
        )


# calling the populate() method
if __name__ == '__main__':
    print("** Populating the Database, Please Wait...")
    populate(10)
    print('** Populating Complete!')


