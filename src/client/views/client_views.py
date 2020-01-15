from flask import Blueprint, render_template, flash, jsonify, request, session, make_response, redirect, url_for
from flask_login import login_required
from os import environ

from src.client.forms.client_registration import ClientRegistration
from src.client.forms.client_search import ClientSearchForm
from src.infrastructure.longform_select import determine_longform_select, determine_employment, \
    determine_er_relationship, determine_guardian_type
from src.services.client_service import find_client_by_ssn, find_client_by_name, find_client_by_email, \
    find_client_by_phone, find_client_by_ID, find_all_clients, add_client

client_views = Blueprint('client_views', __name__, template_folder='templates')
links = {'My Client': '/my-client',
         'Client Information': '/client-info',
         'Client Management': '/client-mgmt',
         'Referrals': '/referrals',
         'Reports': '/client-reports',
         'State Reporting': '/state-reporting',
         'Register New Client': '/create-client'
         }


@client_views.route('/client')
@login_required
def client_dashboard():
    """ REST endpoint for the client dashboard. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    clients = find_all_clients()
    client_urls = []
    for client in clients:
        client_urls.append('/client/' + client.clientID)
    return render_template('client_dashboard.html',
                           href_var=href,
                           title='Client Dashboard',
                           clients=clients,
                           client_urls=client_urls,
                           links=links,
                           sidebar_header='Client')


@client_views.route('/my-client')
@login_required
def my_client():
    """ REST endpoint for the my client page. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    return render_template('my_client.html', title='My Client', sidebar_header='Client', href_var=href, links=links)


@client_views.route('/client-mgmt')
@login_required
def client_mgmt():
    """ REST endpoint for the client management page. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    return render_template('client_mgmt.html', title='Client Management', sidebar_header='Client',
                           href_var=href, links=links)


@client_views.route('/client-reports')
@login_required
def client_reports():
    """ REST endpoint for the client reports page. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    return render_template('client_reports.html', title='Client Reports', sidebar_header='Client',
                           href_var=href, links=links)


@client_views.route('/state-reporting')
@login_required
def state_reporting():
    """ REST endpoint for the state reporting page. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    return render_template('state_reporting.html', title='State Reporting', sidebar_header='Client',
                           href_var=href, links=links)


@client_views.route('/referrals')
@login_required
def referrals():
    """ REST endpoint for the referrals page. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    return render_template('referrals.html', title='Referrals', sidebar_header='Client', href_var=href, links=links)


@client_views.route('/client/<clientID>', methods=['GET'])
def display_client(clientID):
    """ REST endpoint for a specific client. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    client = find_client_by_ID(clientID)
    return render_template('display_client.html', client=client, title=client.firstname, sidebar_header='Client',
                           href_var=href, links=links)


@client_views.route('/client-info', methods=['GET', 'POST'])
@login_required
def client_info():
    """ REST endpoint for the client info page. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    form = ClientSearchForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            search_by = form.search_by.data
            criteria = form.search.data

            if search_by == 'Name':
                client = find_client_by_name(criteria)
                if client:
                    return redirect(url_for('client_views.display_client', clientID=client.clientID))
                else:
                    return render_template('error_client_dne.html', title='Error', href_var=href,
                                           sidebar_header='Client', links=links)
            elif search_by == 'SSN':
                client = find_client_by_ssn(criteria)
                if client:
                    return redirect(url_for('client_views.display_client', clientID=client.clientID))
                else:
                    return render_template('error_client_dne.html', title='Error', href_var=href,
                                           sidebar_header='Client', links=links)
            elif search_by == 'Phone Number':
                client = find_client_by_phone(criteria)
                if client:
                    return redirect(url_for('client_views.display_client', clientID=client.clientID))
                else:
                    return render_template('error_client_dne.html', title='Error', href_var=href,
                                           sidebar_header='Client', links=links)
            elif search_by == 'Email':
                client = find_client_by_email(criteria)
                if client:
                    return redirect(url_for('client_views.display_client', clientID=client.clientID))
                else:
                    return render_template('error_client_dne.html', title='Error', href_var=href,
                                           sidebar_header='Client', links=links)
            elif search_by == 'MyEvolve ID':
                client = find_client_by_ID(criteria)
                if client:
                    return redirect(url_for('client_views.display_client', clientID=client.clientID))
                else:
                    return render_template('error_client_dne.html', title='Error', href_var=href,
                                           sidebar_header='Client', links=links)
            else:
                # render template to display all clients
                return render_template('error_client_dne.html', title='Error', href_var=href, sidebar_header='Client',
                                       links=links)  # so change this...

    return render_template('client_info.html', form=form, title='Client Info', href_var=href, sidebar_header='Client',
                           links=links)


@client_views.route('/create-client', methods=['GET', 'POST'])
@login_required
def create_client():
    """ REST endpoint for client creation. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
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

            gender = determine_longform_select(form.gender.data)
            genderID = determine_longform_select(form.genderID.data)
            sexual_orientation = determine_longform_select(form.sexual_orientation.data)
            race = determine_longform_select(form.race.data)
            ethnicity = determine_longform_select(form.ethnicity.data)
            guardian_type = determine_guardian_type(form.guardian_type.data)
            address_type = determine_longform_select(form.address_type.data)
            employment_status = determine_employment(form.employment_status.data)
            ER_relationship = determine_er_relationship(form.ER_relationship.data)
            marital_status = determine_longform_select(form.marital_status.data)
            education_level = determine_longform_select(form.education_level.data)
            medicaid = {'medicaid_number': form.medicaid_number.data, 'effective_date': None, 'expiration_date': None}
            addresses = {'0': {'type': address_type,
                             'street_address': form.street_address.data,
                             'city': form.city.data,
                             'state': form.state.data,
                             'zip_code': form.zip_code.data}}
            guardian_info = {'0': {'name': form.guardian_name.data,
                                 'type': guardian_type,
                                 'phone': form.guardian_phone.data}}
            emergency_contacts = {'0': {'name': form.ER_name.data,
                                      'relationship': ER_relationship,
                                      'phone': form.ER_phone.data,
                                      'address': form.ER_address.data,
                                      'email': form.ER_email.data,
                                      'can_visit': form.can_visit.data,
                                      'can_pickup': form.can_pickup.data}}
            marital_hist = {'status': marital_status,
                            'start_date': None,
                            'end_date': None,
                            'div_reason': form.div_reason.data}
            disabilities = {'0': {'name': form.disability.data,
                                'description': form.disability_desc.data,
                                'accomodations': form.accomodations.data}}

            add_client(form.clientID.data, form.firstname.data, form.lastname.data, form.middlename.data,
                       form.suffix.data, gender, genderID, sexual_orientation, race, ethnicity, ssn,
                       form.site_location.data, medicaid, form.phone_home.data, form.phone_cell.data,
                       form.phone_work.data, form.email.data, form.contact_pref.data, addresses, guardian_info,
                       emergency_contacts, form.dob.data, form.intake_date.data, form.discharge_date.data,
                       form.is_veteran.data, form.veteran_status.data, marital_hist, disabilities, employment_status,
                       education_level, form.spoken_langs.data, form.reading_langs.data)

            return render_template('registration_success.html', title='Register', href_var=href,
                                   sidebar_header='Client', links=links)
        else:
            flash('Enter the required fields.')
            return render_template('create_client.html', form=form, title='Register Client', href_var=href,
                                   sidebar_header='Client', links=links)

    return render_template('create_client.html', form=form, title='Register Client', href_var=href,
                           sidebar_header='Client', links=links)
