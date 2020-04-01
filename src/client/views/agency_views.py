from flask import Blueprint, render_template, flash, jsonify, request, session, make_response, redirect, url_for
from flask_login import login_required

from src.client.forms.update_agency import UpdateAgency, UpdateAgencyBool, UpdateAgencyDate, UpdateAgencySelect
from src.infrastructure.agency_helper import agency_choices
from src.services.agency_service import get_agency, add_agency, repopulate_agency

import datetime

agency_views = Blueprint('agency_views', __name__, template_folder='templates')
links = {
    'Agency Information': '/agency-info',
    'Programs Operated': '/programs',
    'Materials Provided': '/materials-provided',
    'Holiday Schedule': '/holiday-schedule'
}


@agency_views.route('/agency-info')
@login_required
def agency_info():
    """ REST endpoint for the agency dashboard/info page. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    agency = get_agency()
    if agency:
        update_url = '/update-agency'
        return render_template('agency_information.html', href_var=href, title=agency.name, sidebar_header='Agency',
                               links=links, agency=agency, update_url=update_url)
    return render_template('agency_information.html', href_var=href, title=agency.name, sidebar_header='Agency',
                           links=links, agency=agency)


@agency_views.route('/update-agency', methods=['GET'])
@login_required
def update_agency():
    """ REST endpoint for updating agency information (accessible only by admins). """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    agency = get_agency()
    return render_template('update_agency.html', title='Update Agency', href_var=href, sidebar_header='Agency',
                           links=links, agency=agency)


@agency_views.route('/update-agency-field/<field>', methods=['GET', 'POST'])
@login_required
def update_field(field):
    """ REST endpoint to update an agency's field. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    form = UpdateAgencyBool()
    agency = get_agency()

    if field == 'fiscal_year_start':
        form = UpdateAgencySelect()
        form.cvalue.data = agency[field]
        form.nvalue.choices = agency_choices[field]
    elif field == 'cutoff_date_services' or field == 'cutoff_date_billing' or field == 'cutoff_date_icd10':
        form = UpdateAgencyDate()
        form.cvalue.data = agency[field]
    elif field == 'name' or field == 'short_name' or field == 'ceo' or field == 'main_contact' or \
            field == 'main_contact_email' or field == 'main_contact_phone' or \
            field == 'billing_mirror_cutoff_num_years':
        form = UpdateAgency()
        form.cvalue.data = agency[field]
    else:
        form.cvalue.data = agency[field]

    if request.method == 'POST':
        if form.validate_on_submit():
            return repopulate_agency_helper(field, form.nvalue.data)

    return render_template('update_field.html', title='Update Agency', href_var=href, sidebar_header='Agency',
                           links=links, form=form)


@agency_views.route('/create-agency')
@login_required
def create_agency():
    """ REST endpoint for agency creation. NOT accessible to any user. """
    id = 1
    name = 'Test Agency'
    short_name = 'TA'
    fiscal_year_start = 'January'
    ceo = 'Eli Anderson'
    main_contact = 'Test Lee Testerson'
    main_contact_email = 'test@ogtest.com'
    main_contact_phone = '(555)-100-1000'
    cutoff_date_services = datetime.date(2020, 1, 1)
    cutoff_date_billing = datetime.date(2020, 1, 1)
    cutoff_date_icd10 = datetime.date(2020, 1, 1)
    delete_held_claims = False
    held_claim_not_recognize_revenue = False
    prevent_billed_services_from_billing_again = False
    prevent_payroll_services_from_paying_again = False
    billing_mirror_cutoff_num_years = 3
    enforce_one_active_insurance = False
    validate_insurance_priority = False
    managing_offices = None
    programs = None

    add_agency(id, managing_offices, programs, name, short_name, fiscal_year_start, ceo, main_contact,
               main_contact_email, main_contact_phone, cutoff_date_services, cutoff_date_billing, cutoff_date_icd10,
               delete_held_claims, held_claim_not_recognize_revenue, prevent_billed_services_from_billing_again,
               prevent_payroll_services_from_paying_again, billing_mirror_cutoff_num_years,
               enforce_one_active_insurance, validate_insurance_priority)


def repopulate_agency_helper(field_to_update, nvalue):
    """ Helper function for agency updating. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    update_url = '/update-agency'
    updated_agency = repopulate_agency(field_to_update, nvalue)
    if updated_agency:
        return render_template('agency_information.html', agency=updated_agency, title=updated_agency.name,
                               sidebar_header='Agency', href_var=href, links=links, update_url=update_url,
                               update_successful='True')
    agency = get_agency()
    return render_template('agency_information.html', agency=agency, title=agency.name,
                           sidebar_header='Agency', href_var=href, links=links, update_url=update_url,
                           update_successful='False')
