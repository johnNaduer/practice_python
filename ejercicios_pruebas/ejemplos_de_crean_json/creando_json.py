#!/usr/bin/python3
import json
from sys import argv
import uuid

if __name__=='__main__':

    try:
        with open("persona1.json", "r") as f:
            save_dato = json.load(f)
    except FileNotFoundError:
        save_dato = {}

    persona = {"nombre":argv[1], "apellido":argv[2], "edad": argv[3]}
    n_id = str(uuid.uuid4())
    """ dato_convert_json = json.dumps(persona) """
    save_dato[n_id]=persona
    """print(type(dato_convert_json)) """

    with open("persona1.json", "w", encoding = 'utf-8') as f:
        json.dump(save_dato, f, ensure_ascii=False, indent=4)
    with open("persona1.json", "r") as f:
        dato_json = f.read()

    print(dato_json)
