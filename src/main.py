import data.mongo_setup as mongo_setup

from client.app import app


def main():
    """ Runs the application. """
    mongo_setup.global_init()
    app.run()

if __name__ == "__main__":
    main()
