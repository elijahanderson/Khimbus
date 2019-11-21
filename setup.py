from setuptools import setup

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
    install_requires=[ 'dnspython', 'flask', 'flask-pymongo', 'mongoengine', 'pymongo']
)
