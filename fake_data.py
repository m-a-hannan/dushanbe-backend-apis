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

# models
from django.contrib.auth.models import User, Group
from dushanbe.models import Bill, Material, Type, WorkSubmission


# unit choices for material
unit_choices = ['m', 'kits', 'sum', 'n', 'kits', 't', 'nr']


# 1st, creating the priority object with fake data
def add_user():
    user = User.objects.get_or_create(
        username=fake_data.user_name(),
        email=fake_data.email(),
        password=fake_data.password(),
        first_name=fake_data.first_name(),
        last_name=fake_data.last_name()
    )[0]
    # note: [0] = Usage of get_or_create() method, if priority object already exists then get from first index.
    # if not, then create the priority object.
    user.save()
    return user


# random string generator
def random_string_id(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


# populating the other classes
def populate(n):
    for entry in range(n):

        # 1st, calling priority method for creating priority object first
        user = add_user()

        # creating objects
        Group.objects.create(name=random_string_id(4))

        # creating objects
        bill = Bill.objects.create(
            bill_name=random_string_id(10)
        )

        # creating objects
        type = Type.objects.create(
            bill=bill,
            type_name=random_string_id(10)
        )

        # creating objects
        material = Material.objects.create(
            type=type,
            material_name=fake_data.sentence(),
            serial_no=random.randint(1, 100),
            unit=random.choice(unit_choices),
            quantity=decimal.Decimal(random.randrange(155, 389)) / 100,
        )

        # creating objects
        WorkSubmission.objects.create(
            bill=bill,
            type=type,
            material=material,
            submission_date=fake_data.date(),
            work_progress=random.randint(0, 100),
            created_by=user
        )


# calling the populate() method
if __name__ == '__main__':
    print("** Populating the Database, Please Wait...")
    populate(5)
    print('** Populating Complete **')


