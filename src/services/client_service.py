from mongoengine.queryset.visitor import Q

from src.data.clients import Client
from src.infrastructure.longform_select import determine_longform_select, determine_employment


def add_client(clientID, firstname, lastname, middlename, suffix, gender, genderID, sexual_orientation, race, ethnicity,
               religion, ssn, dln, site_location, medicaid, phone_home, phone_cell, phone_work, email, contact_pref,
               addresses, guardian_info, emergency_contacts, dob, intake_date, discharge_date, is_veteran,
               veteran_status, marital_hist, disabilities, employment_status, education_level, spoken_langs,
               reading_langs):

    client = Client()
    client.clientID = clientID
    client.other_id_no = clientID
    client.firstname = firstname
    client.lastname = lastname
    client.middlename = middlename
    client.suffix = suffix
    client.gender = gender[1]
    client.gender_code = gender[0]
    client.genderID = genderID[1]
    client.genderID_code = genderID[0]
    client.sexual_orientation = sexual_orientation[1]
    client.sexual_orientation_code = sexual_orientation[0]
    client.race = race[1]
    client.race_code = race[0]
    client.ethnicity = ethnicity[1]
    client.ethnicity_code = ethnicity[0]
    client.religion = religion[1]
    client.religion_code = religion[0]
    client.ssn = ssn
    client.driver_license_number = dln
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
    client.employment_status = employment_status[1]
    client.employment_status_code = employment_status[0]
    client.education_level = education_level[1]
    client.education_level_code = education_level[0]
    client.spoken_langs = spoken_langs
    client.reading_langs = reading_langs
    client.save(validate=False)  # validation in front-end
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


def find_client_by_ID(id_no) -> Client:
    client = Client.objects(clientID=id_no).first()
    if client:
        return client
    return Client.objects(other_id_no=id_no).first()


def find_all_clients():
    clients = Client.objects()
    return clients


def repopulate_client(clientID, field_to_update, nvalue):
    client = Client.objects(clientID=clientID).first()
    print('Updating client...')
    if field_to_update == 'lastname':
        client.update(set__lastname=nvalue)
    elif field_to_update == 'firstname':
        client.update(set__firstname=nvalue)
    elif field_to_update == 'middlename':
        client.update(set__middlename=nvalue)
    elif field_to_update == 'suffix':
        client.update(set__suffix=nvalue)
    elif field_to_update == 'ssn':
        client.update(set__ssn=nvalue)
    elif field_to_update == 'phone_home':
        client.update(set__phone_home=nvalue)
    elif field_to_update == 'phone_cell':
        client.update(set__phone_cell=nvalue)
    elif field_to_update == 'phone_work':
        client.update(set__phone_work=nvalue)
    elif field_to_update == 'email':
        client.update(set__email=nvalue)
    elif field_to_update == 'contact_pref':
        client.update(set__contact_pref=nvalue)
    elif field_to_update == 'veteran_status':
        client.update(set__veteran_status=nvalue)
    elif field_to_update == 'site_location':
        client.update(set__site_location=nvalue)
    elif field_to_update == 'gender':
        gvalue = determine_longform_select(nvalue)
        client.update(set__gender=gvalue[1])
        client.update(set__gender_code=gvalue[0])
    elif field_to_update == 'genderID':
        gvalue = determine_longform_select(nvalue)
        client.update(set__genderID=gvalue[1])
        client.update(set__genderID_code=gvalue[0])
    elif field_to_update == 'sexual_orientation':
        svalue = determine_longform_select(nvalue)
        client.update(set__sexual_orientation=svalue[1])
        client.update(set__sexual_orientation_code=svalue[0])
    elif field_to_update == 'race':
        rvalue = determine_longform_select(nvalue)
        client.update(set__race=rvalue[1])
        client.update(set__race_code=rvalue[0])
    elif field_to_update == 'ethnicity':
        evalue = determine_longform_select(nvalue)
        client.update(set__ethnicity=evalue[1])
        client.update(set__ethnicity_code=evalue[0])
    elif field_to_update == 'religion':
        rvalue = determine_longform_select(nvalue)
        client.update(set__religion=rvalue[1])
        client.update(set__religion_code=rvalue[0])
    elif field_to_update == 'education_level':
        evalue = determine_longform_select(nvalue)
        client.update(set__education_level=evalue[1])
        client.update(set__education_level_code=evalue[0])
    elif field_to_update == 'employment_status':
        evalue = determine_employment(nvalue)
        client.update(set__employment_status=evalue[1])
        client.update(set__employment_status_code=evalue[0])
    elif field_to_update == 'spoken_langs':
        client.update(set__spoken_langs=nvalue)
    elif field_to_update == 'reading_langs':
        client.update(set__reading_langs=nvalue)
    elif field_to_update == 'dob':
        client.update(set__dob=nvalue)
    elif field_to_update == 'intake_date':
        client.update(set__intake_date=nvalue)
    elif field_to_update == 'discharge_date':
        client.update(set__discharge_date=nvalue)
    elif field_to_update == 'is_veteran':
        client.update(set__is_veteran=nvalue)
    elif field_to_update == 'addresses':
        client.update(set__addresses=nvalue)
    elif field_to_update == 'marital_hist':
        client.update(set__marital_hist=nvalue)
    elif field_to_update == 'guardian_info':
        client.update(set__guardian_info=nvalue)
    elif field_to_update == 'emergency_contacts':
        client.update(set__emergency_contacts=nvalue)
    elif field_to_update == 'disabilities':
        client.update(set__disabilities=nvalue)
    elif field_to_update == 'medicaid':
        client.update(set__medicaid=nvalue)
    elif field_to_update == 'driver_license_number':
        client.update(set__driver_license_number=nvalue)
    else:
        return False

    client.reload()
    return client


def destroy_client(clientID):
    print('Deleting...')
    client = Client.objects(clientID=clientID).first()
    if client:
        client.delete()
        print('Successfully deleted client!')
        return True
    return False
