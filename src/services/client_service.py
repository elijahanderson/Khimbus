from src.data.clients import Client

def add_client(firstname, lastname, middlename, gender, genderID, sexual_orientation, race, ethnicity, ssn,
               site_location, medicaid, phone_home, phone_cell, phone_work, email, contact_pref,
               addresses, guardian_info, emergency_contacts, dob, intake_date, discharge_date, is_veteran,
               veteran_status, marital_hist, disabilities, employoment_status, education_level, spoken_langs,
               reading_langs):
    client = Client()
    client.firstname = firstname
    client.lastname = lastname
    client.middlename = middlename
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
    client.employment_status = employoment_status
    client.education_level = education_level
    client.spoken_langs = spoken_langs
    client.reading_langs = reading_langs
    client.save()
    print('New client saved!')
    return client

def find_client_by_name(name) -> Client:
    client = Client.objects(name=name).first()
    return client

def find_client_by_ssn(ssn) -> Client:
    client = Client.objects(ssn=ssn).first()
    return client

def find_all_clients():
    clients = Client.objects()
    return clients
