# Briskly-MongoDB Database

This database was created to use with our project called Briskly.

## Description

This database was created using python. 
I was familiar with python, so I chose to start with that and learn how to create a nodeJS version to apply to our Briskly app.
The CRUD operations that this database can do is adding an applicant, retrieving applicant data, updating current applicnats, and deleting applicants.

## Getting Started

### Dependencies

* fastapi, uvicorn, pydantic[email], motor, python-decouple
* Python environment, MacOS, Windows 10/11.


### Without installing:
* You can visit and play with the database at https://afternoon-reaches-38340.herokuapp.com/docs#/
* Database access: Still working on how to give visual access to entire database

### Installing

* Clone this repository to your local machine and save to an empty file.
* Make sure you have python installed. https://www.python.org/downloads/
* On mac, open terminal and change directories to where the cloned repository lives. 
* On Windows, you can use a text editor like VS-Code to open the repo (you will utilize the console there)


### Executing program

* Creating a virtual environment for app
```
$ python3.9 -m venv venv
$ source venv/bin/activate
$ export PYTHONPATH=$PWD```
```
* Installing dependencies
```
$ pip install -r requirements.txt
```
* To run the app:
```
$ python3 app/main.py
```
* Navigate to http://localhost:8000/docs in your browser to access



## Authors

Jonathan Bernardi

## Version History

* 0.1
    * Initial Release
