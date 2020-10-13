from data.agencies import Agency


def add_agency(agencyID, managing_offices, programs, name, short_name, fiscal_year_start, ceo, main_contact,
               main_contact_email, main_contact_phone, cutoff_date_services, cutoff_date_billing, cutoff_date_icd10,
               delete_held_claims, held_claim_not_recognize_revenue, prevent_billed_services_from_billing_again,
               prevent_payroll_services_from_paying_again, billing_mirror_cutoff_num_years,
               enforce_one_active_insurance, validate_insurance_priority):

    agency = Agency()
    agency.agencyID = agencyID
    agency.managing_offices = managing_offices
    agency.programs = programs
    agency.name = name
    agency.short_name = short_name
    agency.fiscal_year_start = fiscal_year_start
    agency.ceo = ceo
    agency.main_contact = main_contact
    agency.main_contact_email = main_contact_email
    agency.main_contact_phone = main_contact_phone
    agency.cutoff_date_services = cutoff_date_services
    agency.cutoff_date_billing = cutoff_date_billing
    agency.cutoff_date_icd10 = cutoff_date_icd10
    agency.delete_held_claims = delete_held_claims
    agency.held_claim_not_recognize_revenue = held_claim_not_recognize_revenue
    agency.prevent_billed_services_from_billing_again = prevent_billed_services_from_billing_again
    agency.prevent_payroll_services_from_paying_again = prevent_payroll_services_from_paying_again
    agency.billing_mirror_cutoff_num_years = billing_mirror_cutoff_num_years
    agency.enforce_one_active_insurance = enforce_one_active_insurance
    agency.validate_insurance_priority = validate_insurance_priority

    agency.save()
    print('New agency created and saved!')
    return agency


def get_agency():
    agency = Agency.objects().first()
    if agency:
        return agency
    return None


def repopulate_agency(field_to_update, nvalue):
    agency = get_agency()
    print('Updating agency...')
    if field_to_update == 'fiscal_year_start':
        agency.update(set__fiscal_year_start=nvalue)
    elif field_to_update == 'name':
        agency.update(set__name=nvalue)
    elif field_to_update == 'short_name':
        agency.update(set__short_name=nvalue)
    elif field_to_update == 'ceo':
        agency.update(set__ceo=nvalue)
    elif field_to_update == 'main_contact':
        agency.update(set__main_contact=nvalue)
    elif field_to_update == 'main_contact_email':
        agency.update(set__main_contact_email=nvalue)
    elif field_to_update == 'main_contact_phone':
        agency.update(set__main_contact_phone=nvalue)
    elif field_to_update == 'cutoff_date_services':
        agency.update(set__cutoff_date_services=nvalue)
    elif field_to_update == 'cutoff_date_billing':
        agency.update(set__cutoff_date_billing=nvalue)
    elif field_to_update == 'cutoff_date_icd10':
        agency.update(set__cutoff_date_icd10=nvalue)
    elif field_to_update == 'delete_held_claims':
        agency.update(set__delete_held_claims=nvalue)
    elif field_to_update == 'held_claim_not_recognize_revenue':
        agency.update(set__held_claim_not_recognize_revenue=nvalue)
    elif field_to_update == 'prevent_billed_services_from_billing_again':
        agency.update(set__prevent_billed_services_from_billing_again=nvalue)
    elif field_to_update == 'prevent_payroll_services_from_paying_again':
        agency.update(set__prevent_payroll_services_from_paying_again=nvalue)
    elif field_to_update == 'billing_mirror_cutoff_num_years':
        agency.update(set__billing_mirror_cutoff_num_years=nvalue)
    elif field_to_update == 'enforce_one_active_insurance':
        agency.update(set__enforce_one_active_insurance=nvalue)
    elif field_to_update == 'validate_insurance_priority':
        agency.update(set__validate_insurance_priority=nvalue)
    else:
        return False

    agency.reload()
    return agency


def destroy_agency(agencyID):
    print('Deleting agency...')
    agency = Agency.objects(agencyID=agencyID).first()
    if agency:
        agency.delete()
        print('Successfully deleted agency!')
        return True
    return False
