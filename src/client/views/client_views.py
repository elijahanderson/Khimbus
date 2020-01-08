from flask import Blueprint, render_template, flash, jsonify, request, session, make_response, redirect, url_for
from flask_login import login_required
from os import environ

from src.client.forms.client_registration import ClientRegistration
from src.services.client_service import find_client_by_ssn, find_all_clients, add_client

client_views = Blueprint('client_views', __name__, template_folder='templates')

@client_views.route('/client')
@login_required
def client_dashboard():
    """ REST endpoint for the client dashboard. """
    return render_template('client_dashboard.html', title='Client Dashboard')

@client_views.route('/client-info')
@login_required
def client_info():
    """ REST endpoint for the client info page. """
    return render_template('client_info.html', title='Client Info')

@client_views.route('/my-client')
@login_required
def my_client():
    """ REST endpoint for the my client page. """
    return render_template('my_client.html', title='My Client')

@client_views.route('/client-mgmt')
@login_required
def client_mgmt():
    """ REST endpoint for the client management page. """
    return render_template('client_mgmt.html', title='Client Management')

@client_views.route('/client-reports')
@login_required
def client_reports():
    """ REST endpoint for the client reports page. """
    return render_template('client_reports.html', title='Client Reports')

@client_views.route('/state-reporting')
@login_required
def state_reporting():
    """ REST endpoint for the state reporting page. """
    return render_template('state_reporting.html', title='State Reporting')

@client_views.route('/referrals')
@login_required
def referrals():
    """ REST endpoint for the referrals page. """
    return render_template('referrals.html', title='Referrals')

@client_views.route('/create-client', methods=['GET', 'POST'])
@login_required
def create_client():
    """ REST endpoint for client creation. """
    form = ClientRegistration()
    if request.method == 'POST':
        if form.validate_on_submit() or environ.get('TEST_FLAG') == 'true':
            name = form.firstname.data + ' ' + form.lastname.data
            print('Creating client', name, '...')
            ssn = form.ssn.data.replace('-', '')
            client_exists = find_client_by_ssn(ssn)
            if isinstance(client_exists, str):  # for testing purposes
                if client_exists == ssn:
                    return render_template('error_client_exists.html', title='Error')
                pass
            elif client_exists:
                return render_template('error_client_exists.html', title='Error')

            medicaid = {'medicaid_number': form.medicaid_number.data, 'effective_date': None, 'expiration_date': None}
            addresses = {'0': {'type': form.address_type.data,
                             'street_address': form.street_address.data,
                             'city': form.city.data,
                             'state': form.state.data,
                             'zip_code': form.zip_code.data}}
            guardian_info = {'0': {'name': form.guardian_name.data,
                                 'type': form.guardian_type.data,
                                 'phone': form.guardian_phone.data}}
            emergency_contacts = {'0': {'name': form.ER_name.data,
                                      'relationship': form.ER_relationship.data,
                                      'phone': form.ER_phone.data,
                                      'address': form.ER_address.data,
                                      'email': form.ER_email.data,
                                      'can_visit': form.can_visit.data,
                                      'can_pickup': form.can_pickup.data}}
            marital_hist = {'status': form.marital_status.data,
                            'start_date': None,
                            'end_date': None,
                            'div_reason': form.div_reason.data}
            disabilities = {'0': {'name': form.disability.data,
                                'description': form.disability_desc.data,
                                'accomodations': form.accomodations.data}}

            add_client(form.firstname.data, form.lastname.data, form.middlename.data, form.gender.data,
                       form.genderID.data, form.sexual_orientation.data, form.race.data, form.ethnicity.data,
                       ssn, form.site_location.data, medicaid, form.phone_home.data,
                       form.phone_cell.data, form.phone_work.data, form.email.data, form.contact_pref.data, addresses,
                       guardian_info, emergency_contacts, form.dob.data, form.intake_date.data, form.discharge_date.data,
                       form.is_veteran.data, form.veteran_status.data, marital_hist, disabilities,
                       str(form.employment_status.data), form.education_level.data, form.spoken_langs.data,
                       form.reading_langs.data)

            return render_template('registration_success.html', title='Register')
        else:
            flash('Enter the required fields.')
            return render_template('create_client.html', form=form, title='Register Client')

    return render_template('create_client.html', form=form, title='Register Client')
