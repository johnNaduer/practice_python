#!/usr/bin/python3

from requests import get
from sys import argv

id_user = argv[1]

#hacemos una peticion a la web
response = get('https://api.github.com/users/{}'.format(id_user))

#comprobamos si la peticion fue exitosa
if response.status_code == 200:
    # obtenemos la informacion del id en formato json
    user_info = response.json()

    if user_info is None:
        print("nose encontro usuario")
    print("nombre es : {}".format(user_info["name"]))
    print("compañia es : {}".format(user_info["company"]))
    print("location es : {}".format(user_info["location"]))
