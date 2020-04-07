import mongoengine as me

from src.data.managing_offices import Office
from src.data.programs import Program


class Agency(me.Document):
    """
    Class used to represent an agency.

    agencyID : the friendly ID of the agency
    name : the name of the agency
    short_name : the name's abbreviation
    fiscal_year_start : the month in which the agency's fiscal year begins
    ceo : the CEO/executive of the agency
    main_contact : the name of the agency's main contact
    main_contact_email : the email address of the agency's main contact
    main_contact_phone : the phone number of the agency's main contact

    cutoff_date_services : services cutoff date
    curoff_date_billing : billing cutoff date
    cutoff_date_icd10 : services on or after this date will bill with the ICD-10 code
    delete_held_claims : delete held claims
    [ various other bools ]

    managing_offices : the embedded collection of offices that belong to an agency
    program_ids : list of the agency's programs
    """

    # general info
    agencyID = me.IntField(required=True)
    name = me.StringField(required=True)
    short_name = me.StringField(required=True)
    fiscal_year_start = me.StringField(required=True)  # selectable field
    ceo = me.StringField(required=False)
    main_contact = me.StringField(required=False)
    main_contact_email = me.StringField(required=False)
    main_contact_phone = me.StringField(required=False)

    # finance setups
    cutoff_date_services = me.DateField(required=False)
    cutoff_date_billing = me.DateField(required=False)
    cutoff_date_icd10 = me.DateField(required=False)
    delete_held_claims = me.BooleanField(required=False)
    held_claim_not_recognize_revenue = me.BooleanField(required=False)
    prevent_billed_services_from_billing_again = me.BooleanField(required=False)
    prevent_payroll_services_from_paying_again = me.BooleanField(required=False)
    billing_mirror_cutoff_num_years = me.IntField(required=False)
    enforce_one_active_insurance = me.BooleanField(required=False)
    validate_insurance_priority = me.BooleanField(required=False)

    # weak relationships and embedded collections
    managing_offices = me.EmbeddedDocumentListField(Office)
    program_ids = me.ListField()

    meta = {
        'db_alias': 'core',
        'collection': 'agencies'
    }
