import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dawajobs.settings')

import django
django.setup()

from testapp.models import HydJobs, PuneJobs, BngJobs
from faker import Faker
from random import randint

# Initialize Faker instance
fake = Faker()

# Function to generate a random phone number
def generate_phonenumber():
    """Generate a random phone number starting with digits 6-9."""
    first_digit = randint(6, 9)
    remaining_digits = ''.join(str(randint(0, 9)) for _ in range(9))
    return f"{first_digit}{remaining_digits}"

# Function to populate job data for any model
def populate_jobs(model, n):
    """Populate n job records in the given model."""
    for _ in range(n):
        date = fake.date()
        company = fake.company()
        title = fake.random_element(elements=('Project Manager', 'Team Lead', 'Software Engineer', 'Associate Engineer'))
        eligibility = fake.random_element(elements=('BCA', 'MCA', 'BTech', 'MTech', 'PhD'))
        address = fake.address()
        email = fake.email()
        phone = generate_phonenumber()
        
        # Create or get the job record
        model.objects.get_or_create(
            date=date,
            company=company,
            title=title,
            eligibility=eligibility,
            address=address,
            email=email,
            phonenumber=phone,
        )

# Populate data for each city
def populate_hydjobs(n):
    populate_jobs(HydJobs, n)

def populate_punejobs(n):
    populate_jobs(PuneJobs, n)

def populate_bngjobs(n):
    populate_jobs(BngJobs, n)

# Run population scripts
if __name__ == "__main__":
    num_records = int(input("Enter the number of records to populate: "))
    print("Populating Hyderabad Jobs...")
    populate_hydjobs(num_records)
    print("Populating Pune Jobs...")
    populate_punejobs(num_records)
    print("Populating Bangalore Jobs...")
    populate_bngjobs(num_records)
    print(f"{num_records} records inserted successfully for each city!")
