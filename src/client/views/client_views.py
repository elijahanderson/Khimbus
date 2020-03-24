from flask import Blueprint, render_template, flash, jsonify, request, session, make_response, redirect, url_for
from flask_login import login_required
from os import environ

from src.client.forms.client_registration import ClientRegistration
from src.client.forms.client_search import ClientSearchForm
from src.client.forms.update_client import UpdateClient, UpdateClientBool, UpdateClientDate, UpdateClientDict, \
    UpdateClientSelect, UpdateClientSelectMultiple
from src.infrastructure.client_helper import client_choices
from src.infrastructure.longform_select import determine_longform_select, determine_employment, \
    determine_er_relationship, determine_guardian_type
from src.services.client_service import find_client_by_ssn, find_client_by_name, find_client_by_email, \
    find_client_by_phone, find_client_by_ID, find_all_clients, add_client, destroy_client, repopulate_client

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
        client_urls.append('/client/' + str(client.clientID))
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
    if client:
        delete_url = '/delete-client/' + str(clientID)
        update_url = '/update-client/' + str(clientID)
        return render_template('display_client.html', client=client, title=client.firstname, sidebar_header='Client',
                               href_var=href, links=links, delete_url=delete_url, update_url=update_url)
    return redirect(url_for('client_views.client_info'))


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
                    return render_template('client_info.html', title='Error', href_var=href,
                                           sidebar_header='Client', links=links, form=form, client_exists='False')
            elif search_by == 'SSN':
                client = find_client_by_ssn(criteria)
                if client:
                    return redirect(url_for('client_views.display_client', clientID=client.clientID))
                else:
                    return render_template('client_info.html', title='Error', href_var=href,
                                           sidebar_header='Client', links=links, form=form, client_exists='False')
            elif search_by == 'Phone Number':
                client = find_client_by_phone(criteria)
                if client:
                    return redirect(url_for('client_views.display_client', clientID=client.clientID))
                else:
                    return render_template('client_info.html', title='Error', href_var=href,
                                           sidebar_header='Client', links=links, form=form, client_exists='False')
            elif search_by == 'Email':
                client = find_client_by_email(criteria)
                if client:
                    return redirect(url_for('client_views.display_client', clientID=client.clientID))
                else:
                    return render_template('client_info.html', title='Error', href_var=href,
                                           sidebar_header='Client', links=links, form=form, client_exists='False')
            elif search_by == 'MyEvolve ID' or search_by == 'Other ID':
                try:
                    client = find_client_by_ID(criteria)
                except ValueError:
                    return render_template('client_info.html', title='Error', href_var=href, sidebar_header='Client',
                                           links=links, form=form, value_error='True')
                if client:
                    return redirect(url_for('client_views.display_client', clientID=client.clientID))
                else:
                    return render_template('client_info.html', title='Error', href_var=href,
                                           sidebar_header='Client', links=links, form=form, client_exists='False')
            else:
                return render_template('client_info.html', title='Error', href_var=href, sidebar_header='Client',
                                       links=links, form=form, client_exists='False')  # so change this...

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
            clientID = form.clientID.data
            client_exists = find_client_by_ID(clientID)
            if client_exists:
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
            guardian_info = {'0': {'guardian_name': form.guardian_name.data,
                                   'guardian_type': guardian_type,
                                   'guardian_phone': form.guardian_phone.data}}
            emergency_contacts = {'0': {'ER_name': form.ER_name.data,
                                        'ER_relationship': ER_relationship,
                                        'ER_phone': form.ER_phone.data,
                                        'ER_address': form.ER_address.data,
                                        'ER_email': form.ER_email.data,
                                        'ER_can_visit': form.can_visit.data,
                                        'ER_can_pickup': form.can_pickup.data}}
            marital_hist = {'marital_status': marital_status,
                            'marital_start_date': None,
                            'marital_end_date': None,
                            'div_reason': form.div_reason.data}
            disabilities = {'0': {'disability_name': form.disability.data,
                                  'disability_description': form.disability_desc.data,
                                  'disability_accommodations': form.accommodations.data}}

            add_client(form.clientID.data, form.firstname.data, form.lastname.data, form.middlename.data,
                       form.suffix.data, gender[1], gender[0], genderID, sexual_orientation, race, ethnicity,
                       form.ssn.data, form.dln.data, form.site_location.data, medicaid, form.phone_home.data, form.phone_cell.data,
                       form.phone_work.data, form.email.data, form.contact_pref.data, addresses, guardian_info,
                       emergency_contacts, form.dob.data, form.intake_date.data, form.discharge_date.data,
                       form.is_veteran.data, form.veteran_status.data, marital_hist, disabilities, employment_status,
                       education_level, form.spoken_langs.data, form.reading_langs.data)

            client = find_client_by_ID(form.clientID.data)
            if client:
                delete_url = '/delete-client/' + str(client.clientID)
                update_url = '/update-client/' + str(client.clientID)
                return render_template('display_client.html', client=client, title=client.firstname,
                                       sidebar_header='Client', href_var=href, links=links, delete_url=delete_url,
                                       update_url=update_url)
            else:
                return render_template('client_client.html', form=form, title='Register Client', href_var=href,
                                       sidebar_header='Client', links=links, success='False')

        else:
            flash('Enter the required fields.')
            return render_template('create_client.html', form=form, title='Register Client', href_var=href,
                                   sidebar_header='Client', links=links)

    return render_template('create_client.html', form=form, title='Register Client', href_var=href,
                           sidebar_header='Client', links=links)


@client_views.route('/update-client/<clientID>', methods=['GET'])
@login_required
def update_client(clientID):
    """ REST endpoint for updating client information. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    client = find_client_by_ID(clientID)
    return render_template('update_client.html', title='Update Client', href_var=href, sidebar_header='Client',
                           links=links, client=client)


@client_views.route('/update-client-field/<clientID>-<field>', methods=['GET', 'POST'])
@login_required
def update_field(clientID, field):
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    form = UpdateClientSelect()
    client = find_client_by_ID(clientID)

    if field == 'gender' or field == 'genderID' or field == 'sexual_orientation' or field == 'race' \
            or field == 'ethnicity' or field == 'education_level' or field == 'contact_pref' \
            or field == 'veteran_status' or field == 'employment_status':
        form.cvalue.data = client[field]
        form.nvalue.choices = client_choices[field]
    elif field == 'dob' or field == 'intake_date' or field == 'discharge_date':
        form = UpdateClientDate()
        form.cvalue.data = client[field]
    elif field == 'is_veteran':
        form = UpdateClientBool()
        form.cvalue.data = client[field]
    elif field == 'spoken_langs' or field == 'reading_langs':
        form = UpdateClientSelectMultiple()
        form.cvalue.data = client[field]
        form.nvalue.choices = client_choices[field]
    else:
        form = UpdateClient()
        form.cvalue.data = client[field]

    if request.method == 'POST':
        if form.validate_on_submit():
            return repopulate_client_helper(clientID, field, form.nvalue.data)

    return render_template('update_field.html', title='Update Client', href_var=href, sidebar_header='Client',
                           links=links, form=form)


@client_views.route('/update-dictfield/<clientID>-<field>-<to_update>', methods=['GET', 'POST'])
@login_required
def update_dictfield(clientID, field, to_update):
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    client = find_client_by_ID(clientID)

    if to_update == 'type' or to_update == 'marital_status' or to_update == 'guardian_type' \
            or to_update == 'ER_relationship' or to_update == 'ER_can_visit' or to_update == 'ER_can_pickup':
        return redirect(url_for('client_views.update_dict_select', clientID=clientID, dict_field=field,
                                field=to_update))
    else:
        form = UpdateClient()
        if field == 'marital_hist' or field == 'medicaid':
            form.cvalue.data = client[field][to_update]
        else:
            form.cvalue.data = client[field]['0'][to_update]

    if request.method == 'POST':
        if form.validate_on_submit():
            curr_dict = client[field]
            if field == 'marital_hist' or field == 'medicaid':
                curr_dict[to_update] = form.nvalue.data
            else:
                curr_dict['0'][to_update] = form.nvalue.data

            return repopulate_client_helper(clientID, field, curr_dict)

    return render_template('update_field.html', title='Update Client', href_var=href, sidebar_header='Client',
                           links=links, form=form)


@client_views.route('/update-dict-select/<clientID>-<dict_field>-<field>', methods=['GET', 'POST'])
@login_required
def update_dict_select(clientID, dict_field, field):
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    form = UpdateClientSelect()
    client = find_client_by_ID(clientID)

    if field == 'ER_can_visit' or field == 'ER_can_pickup':
        form = UpdateClientBool()
        form.cvalue.data = client[dict_field]['0'][field]
    elif field == 'marital_status':
        form.cvalue.data = client[dict_field][field][1]
        form.nvalue.choices = client_choices[field]
    else:
        form.cvalue.data = client[dict_field]['0'][field][1]
        form.nvalue.choices = client_choices[field]

    if request.method == 'POST':
        if form.validate_on_submit():
            nlist = determine_longform_select(form.nvalue.data)
            if field == 'guardian_type':
                nlist = determine_guardian_type(form.nvalue.data)
            elif field == 'ER_relationship':
                nlist = determine_er_relationship(form.nvalue.data)

            curr_dict = client[dict_field]
            if field == 'marital_status':
                curr_dict[field] = nlist
            else:
                curr_dict['0'][field] = nlist
            return repopulate_client_helper(clientID, dict_field, curr_dict)

    return render_template('update_field.html', title='Update Client', href_var=href, sidebar_header='Client',
                           links=links, form=form)


@client_views.route('/delete-client/<clientID>', methods=['GET'])
@login_required
def delete_client(clientID):
    """ REST endpoint to handle client destruction. """
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']

    delete_successful = destroy_client(clientID)
    if delete_successful:
        return render_template('client_deleted.html', title='Client', href_var=href, sidebar_header='Client',
                               links=links)

    return redirect(url_for('client_views.client_dashboard'))


def repopulate_client_helper(clientID, field_to_update, nvalue):
    href = ''
    if 'username' in session:
        href = '/user/' + session['username']
    delete_url = '/delete-client/' + str(clientID)
    update_url = '/update-client/' + str(clientID)
    updated_client = repopulate_client(clientID, field_to_update, nvalue)
    if updated_client:
        return render_template('display_client.html', client=updated_client, title=updated_client.firstname,
                               sidebar_header='Client', href_var=href, links=links, delete_url=delete_url,
                               update_url=update_url, update_successful='True')
    client = find_client_by_ID(clientID)
    return render_template('display_client.html', client=client, title=client.firstname,
                           sidebar_header='Client', href_var=href, links=links, delete_url=delete_url,
                           update_url=update_url, update_successful='False')
