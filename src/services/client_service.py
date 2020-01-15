from mongoengine.queryset.visitor import Q

from src.data.clients import Client


def add_client(clientID, firstname, lastname, middlename, suffix, gender, genderID, sexual_orientation, race, ethnicity,
               ssn, site_location, medicaid, phone_home, phone_cell, phone_work, email, contact_pref,
               addresses, guardian_info, emergency_contacts, dob, intake_date, discharge_date, is_veteran,
               veteran_status, marital_hist, disabilities, employment_status, education_level, spoken_langs,
               reading_langs):
    client = Client()
    client.clientID = clientID
    client.firstname = firstname
    client.lastname = lastname
    client.middlename = middlename
    client.suffix = suffix
    client.gender = gender
    client.genderID = genderID
    client.sexual_orientation = sexual_orientation
    client.race = race
    client.ethnicity = ethnicity
    client.ssn = ssn
    client.site_location = site_location
    client.medicaid = medicaid
    client.phone_home = phone_home
    client.phone_cell = phone_cell
    client.phone_work = phone_work
    client.email = email
    client.contact_pref = contact_pref
    client.addresses = addresses
    client.guardian_info = guardian_info
    client.emergency_contacts = emergency_contacts
    client.dob = dob
    client.is_veteran = is_veteran
    client.intake_date = intake_date
    client.discharge_date = discharge_date
    client.veteran_status = veteran_status
    client.marital_hist = marital_hist
    client.disabilities = disabilities
    client.employment_status = employment_status
    client.education_level = education_level
    client.spoken_langs = spoken_langs
    client.reading_langs = reading_langs
    client.save(validate=False)
    print('New client saved!')
    return client


def find_client_by_name(name) -> Client:
    name = name.split(' ')
    if len(name) == 1:
        client = Client.objects(Q(firstname=name[0]) | Q(lastname=name[0])).first()
    elif len(name) == 2:
        client = Client.objects(Q(firstname=name[0]) & Q(lastname=name[1])).first()
    else:
        client = Client.objects(Q(firstname=name[0]) & Q(middlename=name[1]) & Q(lastname=name[2])).first()
    return client


def find_client_by_ssn(ssn) -> Client:
    client = Client.objects(ssn=ssn).first()
    return client


def find_client_by_phone(phone) -> Client:
    client = Client.objects(Q(phone_home=phone) | Q(phone_cell=phone) | Q(phone_work=phone)).first()
    return client


def find_client_by_email(email) -> Client:
    client = Client.objects(email=email).first()
    return client


def find_client_by_ID(clientID) -> Client:
    client = Client.objects(clientID=clientID).first()
    return client


def find_all_clients():
    clients = Client.objects()
    return clients
