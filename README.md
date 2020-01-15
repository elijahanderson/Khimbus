# Khimbus
Khimbus is a cloud-based database management system for KHIT consulting, designed for easy use and access to real-time information.

## Getting Started
First version still in development. There will eventually be a webpage to navigate to for normal users.

### Prerequisites
* Python 3.8.* (any Python 3 version is probably fine, but 3.8.1 is recommended)
* Pip 19.*
* MongoDB Database Server 4.* ([Link to download](https://www.mongodb.com/download-center/community) -- must also 
edit your system environment PATH variable to include `C:\<Path to installed mongo server>\bin`)

### Installing & Running
1. Run `mongod.exe`
2. Navigate to `https://github.com/elijahanderson/` in your browser, then switch to the dev branch
3. Click the green "Clone or download" button and copy the repository address: `https://github.com/elijahanderson/Khimbus.git`
4. Open your command line/terminal, `cd` to the directory you want the project in, then `git clone https://github.com/elijahanderson/Khimbus.git`
5. Install the required packages: `pip install -r requirements.txt`
6. Once everything is installed correctly, `cd src`
7. Now run the application: `python main.py`
8. Open `http://127.0.0.1:5000/` in a web browser. You should now be able to use the latest development version of the site.


## Built With
* Python 3.8.1
* Flask 1.1.1
* MongoDB, PyMongo, & monogoengine
* PyCharm

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/elijahanderson/Khimbus/tags).

Current development version: 0.1.0

## Authors
* **Eli Anderson**

## License
This project is licensed under the GNU Affero General Public License v3.0. See LICENSE.md for more details or go [here](https://choosealicense.com/licenses/agpl-3.0/).
