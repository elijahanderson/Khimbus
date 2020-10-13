# Use the Python 3.8.1 image
FROM python:3.8.1

WORKDIR /client

# Copy current directory contents into the container at /client
ADD . /client

# Install the dependencies
RUN pip install -r requirements.txt

# start uWSGI
CMD ["uwsgi", "app.ini"]
