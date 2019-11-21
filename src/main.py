import data.mongo_setup as mongo_setup

from app import app, mongo

def main():
    """ Runs the application. """
    mongo_setup.global_init()

if __name__ == "__main__":
    main()
    app.run()