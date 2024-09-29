import random
import hashlib
import csv
from faker import Faker

fake = Faker()

password_list = [
    "PEACHKEY690", "elreguetonero", "babydestiny", "jcjtcclsbcj", "happyliving", "Memphis2007", "HPL];HLG010",
    "PEACHES2007", "elpunkestamuerto", "babydesiree", "jcjlwon2129", "happylilbitch", "Melrose1990", "HOWIROLL666",
    "PAssword123!!", "elpoderdetres", "babyderrick", "jcismine101", "happylife9699", "MellieMoo07", "HOVOGLIADITE",
    "PAY2005431629", "elpentagono", "babydamulag", "jcinthehouse", "happylesson", "MelissaenAnna", "HOUSEKEEPING",
    "PAULORICO4529", "elpapidelacasa", "babycomeback", "jchompukoon", "happylesson", "MelissaCubillo", "HOTTIECUPID",
    "elpapadeloshelados", "babycinnamon", "happyleng0706", "Melisita020496", "HOODSTAR105",
    "MejiaKwanJesus", "HONEYBUNCHES", "Meguelisnr1", "HOMIES4LIFE",
    "123456", "password", "123456789", "12345678", "12345", "1234567", "1234567890", "qwerty", "abc123", "111111",
    "iloveyou", "admin", "letmein", "welcome", "monkey", "sunshine", "princess", "charlie", "password1", "1234abcd",
    "taylor2david1", "taylor2connor", "taylor280704", "taylor2690623", "taylor25292",
    "ALREAYKNOWN", "ALRASHODI12", "ALRAK1209MV", "ALRAK,LEBIRAM,2006", "ALRACoran!20.031", "ALR3ADY-TAG3N",
    "ALQUIMISTANGEL", "ALQIANE!@#!@#", "themaster123", "themaster#1", "themasquerade", "themasketers",
    "themanonthemoon", "themanofsteel", "myspacenerd", "myspacemanta", "myspacejumpoff", "myspacegurl", "myspacefilm",
    "prinsesatopi", "prinsesastar", "prinsesaemo", "prinsesabella", "prinsesa2005", "prinsenbeek",
    "crystalshyannwright", "phoebemolly", "phoebejudea", "phoebegrace", "phoebe26397760", "phoebe170806"
]

names = set()
while len(names) < 100:
    full_name = fake.name()
    names.add(full_name)

names_list = list(names)
emails_list = [f"{name.split()[0][0].lower()}.{name.split()[1].lower()}@gmail.com" for name in names_list]
random.shuffle(password_list)

hashed_passwords = [hashlib.sha256(password.encode()).hexdigest() for password in password_list]

csv_file_path = "data.csv"
with open(csv_file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["email", "password"])
    for i in range(100):
        writer.writerow([emails_list[i], hashed_passwords[i]])

print(f"CSV file '{csv_file_path}' generated successfully.")
