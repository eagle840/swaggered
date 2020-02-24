import connexion
import six
import mysql.connector

from swagger_server.models.people import People  # noqa: E501
from swagger_server.models.person import Person  # noqa: E501
from swagger_server.models.person_data import PersonData  # noqa: E501
from swagger_server import util


mydb = mysql.connector.connect(
   host="localhost",
   user="root",
   passwd="1234",
   auth_plugin="mysql_native_password",
   database="titanic"
   )

# print(mydb)



def people_add(person):  # noqa: E501
    """Add a person to the database

     # noqa: E501

    :param person: 
    :type person: dict | bytes

    :rtype: Person
    """
    if connexion.request.is_json:
        person = PersonData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def people_list():  # noqa: E501
    """Get a list of all people

     # noqa: E501


    :rtype: People
    """
    return 'do some magic!'


def person_delete(uuid):  # noqa: E501
    """Delete this person

     # noqa: E501

    :param uuid: 
    :type uuid: 

    :rtype: None
    """
    return 'do some magic!'


def person_get(uuid):  # noqa: E501
    """Get information about one person

     # noqa: E501

    :param uuid: 
    :type uuid: 

    :rtype: Person
    """
    return 'do some magic!'


def person_update(uuid, person):  # noqa: E501
    """Update information about one person

     # noqa: E501

    :param uuid: 
    :type uuid: 
    :param person: 
    :type person: dict | bytes

    :rtype: Person
    """
    if connexion.request.is_json:
        person = PersonData.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
