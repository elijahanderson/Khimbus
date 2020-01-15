from setuptools import setup, find_packages

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='Khimbus',
    version='0.1.0',
    description='A cloud-based database management system for KHIT consulting',
    long_description=long_description,
    author='Eli Anderson',
    author_email='dispentia@gmail.com',
    url='https://github.com/elijahanderson/Khimbus',
    install_requires=[ 'bson','dnspython', 'flask', 'flask-login', 'flask-pymongo', 'flask-mongoengine', 'mock', 'mongoengine',
                       'pymongo', 'pyyaml', 'werkzeug','wtforms'],
    packages=find_packages()
)
