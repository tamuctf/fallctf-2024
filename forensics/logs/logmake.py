import csv
import random
import string
from datetime import datetime, timedelta
import names

def generate_random_id():
    numbers = ''.join(random.choices(string.digits, k=4))
    letters = ''.join(random.choices(string.ascii_uppercase, k=4))
    return numbers + letters

def generate_random_email():
    domains = ['tamu.edu', 'cmu.edu', 'mit.edu', 'sans.edu']
    first_name = names.get_first_name().lower()
    last_name = names.get_last_name().lower()
    return f"{first_name}.{last_name}@{random.choice(domains)}"

def generate_random_phone():
    return f"979-{random.randint(100, 999)}-{random.randint(1000, 9999)}"

def generate_code():
    return 'F' if random.random() < 0.03 else 'S'

num_records = 100 
email_phone_mapping = {}

for _ in range(num_records):
    sender_email = generate_random_email()
    sender_phone = generate_random_phone()
    email_phone_mapping[sender_email] = sender_phone

start_date = datetime(2011, 1, 1)
date_increment = timedelta(days=1)
log_entries = []
date_index = 0
email_counts = []

for email, phone in email_phone_mapping.items():
    num_entries = random.randint(3, 15)
    email_counts.extend([(email, phone)] * num_entries)

random.shuffle(email_counts)

for i, (email, phone) in enumerate(email_counts):
    while log_entries and log_entries[-1]['Sender Email'] == email:
        random.shuffle(email_counts)
        email, phone = email_counts[i]

    record_date = start_date + date_increment * date_index

    code = generate_code()

    record_id = generate_random_id()

    receiver_email = generate_random_email()
    receiver_phone = generate_random_phone()

    log_entries.append({
        'ID': record_id,
        'Sender Email': email,
        'Sender Phone': phone,
        'Receiver Email': receiver_email,
        'Receiver Phone': receiver_phone,
        'Date': record_date.strftime('%Y-%m-%d'),
        'Code': code
    })

    if code == 'F':
        log_entries.append({
            'ID': generate_random_id(),
            'Sender Email': email,
            'Sender Phone': phone,
            'Receiver Email': receiver_email,
            'Receiver Phone': receiver_phone, 
            'Date': record_date.strftime('%Y-%m-%d'),
            'Code': 'S'
        })

    date_index += 1

file_name = 'log.csv'

with open(file_name, 'w', newline='') as csvfile:
    fieldnames = ['ID', 'Sender Email', 'Sender Phone', 'Receiver Email', 'Receiver Phone', 'Date', 'Code']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for entry in log_entries:
        writer.writerow(entry)

print("CSV log generated:", file_name)
