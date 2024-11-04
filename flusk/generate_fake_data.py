from faker import Faker
import random
from datetime import datetime

fake = Faker()

def generate_fake_staff():
    return {
        'name': fake.name(),
        'email': fake.email(),
        'position': random.choice(['Doctor', 'Nurse', 'Administrator', 'Technician']),
        'staff_id': random.randint(1, 9999),
        'hire_date': fake.date_this_decade()  # This will return a datetime.date object
    }

def generate_fake_patient():
    return {
        'name': fake.name(),
        'email': fake.email(),
        'dob': fake.date_of_birth(minimum_age=0, maximum_age=100),  # datetime.date object
        'patient_id': random.randint(1, 9999),
        'appointment_date': fake.future_date(end_date="+30d")  # datetime.date object
    }
