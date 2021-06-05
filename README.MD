# Brenco Code challenge
The challenge follows modern application-design standards of having a centralized back-end with separate clients. You will be required to build the following:
1. A RESTful backend API
2. A mobile application (Android or iOS)
 
## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

```
$ git clone ..
$ pipenv --python 3.9
$ pipenv install
$ pipenv run python manage.py makemigrations
$ pipenv run python manage.py migrate
$ pipenv run python manage.py createsuperuser
```

### Prerequisites

* Tested on linux
* Install pipenv :
    ```
    python3 -m pip install pipenv
    ```
## Running the tests

To run the automated tests for this system:

    ```
    $ pipenv run python manage.py test
    ```
### Coding style

* autopep8
* black

## Deployment

This project is deployed to [Heroku](https://keygenerator.herokuapp.com/)

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/MahamdiAmine/key-generator-backend-/tags).

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details