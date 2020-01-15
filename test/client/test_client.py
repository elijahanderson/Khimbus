from flask import Flask, jsonify, session
from flask_login import LoginManager
from os import environ
import mock
import sys
import unittest
import yaml

from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.client.views.home_page import home_page
from src.client.views.about_page import about_page
from src.client.views.user_views import user_views
from src.client.views.client_views import client_views

class FlaskClientTest(unittest.TestCase):
    """ Testing class used to test the REST endpoints of the Flask app. """

    def setUp(self):
        """ Setup. """
        with open('D:/Programming/KHIT/Khimbus/src/config/application.yml', 'r') as yml:
            self.conf = yaml.safe_load(yml)
            self.username = self.conf['mongouser']['username']
            self.pwd = self.conf['mongouser']['password']

        self.app = Flask(__name__, template_folder='C:/Programming/Khimbus/src/client/templates/')
        self.app.register_blueprint(home_page)
        self.app.register_blueprint(about_page)
        self.app.register_blueprint(user_views)
        self.app.register_blueprint(client_views)
        self.app.secret_key = 'test'
        self.login_manager = LoginManager()
        self.app.config['MONGODB_DB'] = 'test'
        self.app.config['MONGODB_ALIAS'] = 'core'
        self.app.config['TESING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config["MONGODB_HOST"] = "mongodb+srv://" + self.username + ":" + self.pwd + \
                                     "@khimbus-fphpr.gcp.mongodb.net/khimbus_db-dev?retryWrites=true&w=majority"
        self.login_manager.init_app(self.app)
        self.login_manager.login_view = 'user_views.login'
        self.test_app = self.app.test_client()
        self.test_app.testing = True
        environ['TEST_FLAG'] = 'true'

    def test_home_page_redirect_renders_successfully(self):
        """ Test home page redirects to login page if user not in session. """
        response = self.test_app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Log In', response.data)

    def test_about_page_renders_successfully(self):
        """ Test about page renders correctly. """
        response = self.test_app.get('/about')
        self.assertEqual(response.status_code, 200)

    @mock.patch('src.client.views.user_views.find_all_users')
    def test_users_page_renders_successfully(self, users_mock):
        """ Test users page renders successfully. """
        users_mock.return_value = 'user'
        response = self.test_app.get('/users')
        users_mock.assert_called()
        self.assertEqual(response.status_code, 200)

    def test_create_user_page_renders_successfully(self):
        """ Test create-user page renders successfully. """
        response = self.test_app.get('/create-user', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    @mock.patch('src.client.views.user_views.login_user')
    def test_valid_user_logged_in_home_page_redirect(self, login_mock, user_mock):
        """ Test user login success behaves correctly. """
        user_mock.return_value = ('testuser', 'password')
        response = self.test_app.post('/login',
                                      data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                      follow_redirects=True)
        user_mock.assert_called_once()
        login_mock.assert_called_once()
        self.assertIn(b'Khimbus', response.data)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    def test_login_user_not_found(self, user_mock):
        """ Test user cannot login if not found in database. """
        user_mock.return_value = None
        response = self.test_app.post('/login',
                                      data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                      follow_redirects=True)
        user_mock.assert_called_once()
        self.assertIn(b'Server could not find specified username.', response.data)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    def test_login_incorrect_password(self, user_mock):
        """ Test user cannot login with incorrect password. """
        user_mock.return_value = ('testuser', 'password123')
        response = self.test_app.post('/login',
                                      data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                      follow_redirects=True)
        user_mock.assert_called_once()
        self.assertIn(b'Password is incorrect.', response.data)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    @mock.patch('src.client.views.user_views.login_user')
    def test_logout(self, login_mock, user_mock):
        """ Test logout behaves correctly. """
        user_mock.return_value = ('testuser', 'password123')
        response_login = self.test_app.post('/login',
                                data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                follow_redirects=True)
        user_mock.assert_called_once()
        login_mock.assert_called_once()
        self.assertIn(b'Khimbus', response_login.data)
        response = self.test_app.get('/logout', follow_redirects=True)
        self.assertIn(b'Log In', response.data)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    @mock.patch('src.client.views.user_views.login_user')
    def test_client_dashboard_renders_successfully(self, login_mock, user_mock):
        """ Test client dashboard renders correctly. """
        user_mock.return_value = ('testuser', 'password123')
        login_response = self.test_app.post('/login',
                                      data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                      follow_redirects=True)
        user_mock.assert_called_once()
        login_mock.assert_called_once()
        response = self.test_app.get('/client', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    @mock.patch('src.client.views.user_views.login_user')
    def test_myclient_renders_successfully(self, login_mock, user_mock):
        """ Test my client page renders correctly. """
        user_mock.return_value = ('testuser', 'password')
        login_response = self.test_app.post('/login',
                                            data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                            follow_redirects=True)
        user_mock.assert_called_once()
        login_mock.assert_called_once()
        response = self.test_app.get('/my-client', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    @mock.patch('src.client.views.user_views.login_user')
    def test_client_info_renders_successfully(self, login_mock, user_mock):
        """ Test client info page renders correctly. """
        user_mock.return_value = ('testuser', 'password')
        login_response = self.test_app.post('/login',
                                            data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                            follow_redirects=True)
        user_mock.assert_called_once()
        login_mock.assert_called_once()
        response = self.test_app.get('/client-info', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    @mock.patch('src.client.views.user_views.login_user')
    def test_client_mgmt_renders_successfully(self, login_mock, user_mock):
        """ Test client management page renders correctly. """
        user_mock.return_value = ('testuser', 'password')
        login_response = self.test_app.post('/login',
                                            data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                            follow_redirects=True)
        user_mock.assert_called_once()
        login_mock.assert_called_once()
        response = self.test_app.get('/client-mgmt', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    @mock.patch('src.client.views.user_views.login_user')
    def test_referrals_renders_successfully(self, login_mock, user_mock):
        """ Test referrals page renders correctly. """
        user_mock.return_value = ('testuser', 'password')
        login_response = self.test_app.post('/login',
                                            data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                            follow_redirects=True)
        user_mock.assert_called_once()
        login_mock.assert_called_once()
        response = self.test_app.get('/referrals', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    @mock.patch('src.client.views.user_views.login_user')
    def test_client_reports_renders_successfully(self, login_mock, user_mock):
        """ Test client reports page renders correctly. """
        user_mock.return_value = ('testuser', 'password')
        login_response = self.test_app.post('/login',
                                            data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                            follow_redirects=True)
        user_mock.assert_called_once()
        login_mock.assert_called_once()
        response = self.test_app.get('/client-reports', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    @mock.patch('src.client.views.user_views.find_user_by_username')
    @mock.patch('src.client.views.user_views.login_user')
    def test_state_reporting_renders_successfully(self, login_mock, user_mock):
        """ Test state reporting page renders correctly. """
        user_mock.return_value = ('testuser', 'password')
        login_response = self.test_app.post('/login',
                                            data=dict(username='testuser',
                                                password='password',
                                                firstname='firstname',
                                                lastname='lastname',
                                                work_email='email@email.com',
                                                phone='000000000000',
                                                job_title='job title',
                                                supervisor='supervisor'),
                                            follow_redirects=True)
        user_mock.assert_called_once()
        login_mock.assert_called_once()
        response = self.test_app.get('/state-reporting', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_create_client_page_renders_successfully(self):
        """ Test create-client page renders successfully. """
        response = self.test_app.get('/create-client', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_logout_requires_login(self):
        """ Test logout first requires user to login. """
        response = self.test_app.get('/logout', follow_redirects=True)
        self.assertIn(b'Log In', response.data)

    def test_page_not_found_error(self):
        """ Test random endpoint returns page not found error. """
        response = self.test_app.get('/asdf')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    unittest.main()
