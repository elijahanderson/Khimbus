import mongoengine as me

from data.managing_offices import Office
from data.programs import Program


class Agency(me.Document):
    """
    Class used to represent an agency.

    name : the name of the agency
    managing_offices : the embedded collection of offices that belong to an agency
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

    # embedded collections
    managing_offices = me.EmbeddedDocumentListField(Office)
    programs = me.EmbeddedDocumentListField(Program)

    meta = {
        'db_alias': 'core',
        'collection': 'agencies'
    }
