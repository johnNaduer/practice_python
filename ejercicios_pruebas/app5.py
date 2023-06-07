#!/usr/bin/python3
from flask import Flask, request, render_template, make_response
from models.state2 import state
from models.administrador2 import administrador
from models.propiedad2 import propiedad
from models.espacio2 import espacio
import models
from flask_weasyprint import HTML, render_pdf

#from sqlalchemy.orm import session

app = Flask(__name__)

@app.route('/espacios', methods=['GET', 'POST'])
def crud_espacios():
    propiedades = models.estorage.all(propiedad)
    if request.method == 'POST':
        action = request.form['action']

        if action == 'search':
            id = int(request.form['id'])
            searched_espacio = models.estorage.get(espacio, id)

            if searched_espacio:
                return f'El espacio con ID {id} es: {searched_espacio.descripcion}'
            else:
                return f'No se encontró ningún espacio con ID {id}'

        elif action == 'update':
            id = int(request.form['id'])
            new_descripcion = request.form['new_descripcion']

            espacio_to_update = models.estorage.get(espacio, id)

            if espacio_to_update is None:
                return 'El espacio con el ID {} no existe'.format(id)

            espacio_to_update.descripcion = new_descripcion
            models.estorage.save()

            return 'Datos actualizados correctamente'

        elif action == 'delete':
            id = int(request.form['id'])

            obj = models.estorage.all(espacio)
            for item in obj:
                if item.id == id:
                    models.estorage.delete(item)
                    models.estorage.save()
                    return f'Espacio con ID {id} eliminado correctamente'
            return f'No se encontró un espacio con ID {id}'

        elif action == 'add':
            id = int(request.form['id'])
            id_propiedad = int(request.form['id_propiedad'])
            numero = int(request.form['numero'])
            descripcion = request.form['descripcion']
            precio = request.form['precio']
            disponibilidad = request.form['disponibilidad']
            new_espacio = espacio(id=id, id_propiedad=id_propiedad, numero=numero, descripcion=descripcion, precio=precio, disponibilidad=disponibilidad)
            models.estorage.new(new_espacio)
            models.estorage.save()
            return 'Datos agregados correctamente'

        elif action == 'select_property':
            propiedad_nombre = request.form.get('propiedad_nombre')

            if not propiedad_nombre:
                return 'Error: No se proporcionó el nombre de la propiedad'

            propiedad2 = models.estorage.get_propiedad_by_nombre(propiedad_nombre)

            if propiedad2 is None:
                return f'La propiedad con nombre {propiedad_nombre} no existe'

            espacios = models.estorage.get_espacios_by_propiedad_id(propiedad2.id)

            return render_template('espacios_crud.html', propiedad2=propiedad2, espacios=espacios, propiedades=propiedades)


        elif action == 'update_disponibilidad':
            id = int(request.form['id'])
            disponibilidad = request.form['disponibilidad']
            espacio_to_update = models.estorage.get(espacio, id)
    
            if espacio_to_update is None:
                return 'El espacio con el ID {} no existe'.format(id)
    
            espacio_to_update.disponibilidad = disponibilidad
            models.estorage.save()
    
            return 'Disponibilidad actualizada correctamente'

        """
        elif action == 'select_property':
            
            propiedad_id = int(request.form.get('propiedad_id'))

            if propiedad_id == 0:
                return 'Error: No se proporcionó el ID de propiedad'
            
            propiedad2 = models.estorage.get(propiedad, propiedad_id)

            if propiedad2 is None:
                return f'La propiedad con ID {propiedad_id} no existe'

            espacios = models.estorage.get_espacios_by_propiedad_id(propiedad_id)

            return render_template('espacios_crud.html', propiedad2=propiedad2, espacios=espacios, propiedades=propiedades)
            """

    else:
        espacios_all = models.estorage.all(espacio)
        propiedades = models.estorage.all(propiedad)
        return render_template('espacios_crud.html', espacios_all=espacios_all, propiedades=propiedades)

        """
        propiedades = models.estorage.all(propiedad)  # Agrega esta línea para actualizar la lista de propiedades
        """

@app.route('/propiedades', methods=['GET', 'POST'])
def crud_propiedades():

    resultados = None

    if request.method == 'POST':
        action = request.form['action']

        if action == 'search':
            # Obtener el ID ingresado en el formulario
            id = int(request.form['id'])

            if id == 0:
                # Mostrar todos los datos de la tabla propiedades
                all_propiedades = models.estorage.all(propiedad)
                resultados = []
                for prop in all_propiedades:
                    resultados.append({
                        'id': prop.id,
                        'nombre': prop.nombre,
                        'direccion': prop.direccion,
                        'numero_telefono': prop.numero_telefono,
                        'descripcion': prop.descripcion
                    })

            else:
                # Buscar la propiedad en la base de datos por ID
                searched_propiedad = models.estorage.get(propiedad, id)

                if searched_propiedad:
                    resultados = [{
                        'id': searched_propiedad.id,
                        'nombre': searched_propiedad.nombre,
                        'direccion': searched_propiedad.direccion,
                        'numero_telefono': searched_propiedad.numero_telefono,
                        'descripcion': searched_propiedad.descripcion
                    }]
                else:
                    resultados = []

            return render_template('propiedades_crud.html', resultados=resultados)


        elif action == 'update':
            # Obtener los datos enviados desde el formulario
            id = int(request.form['id'])
            new_nombre = request.form['new_nombre']

            # Obtener la propiedad a actualizar
            propiedad_to_update = models.estorage.get(propiedad, id)

            if propiedad_to_update is None:
                return 'La propiedad con el ID {} no existe'.format(id)

            # Actualizar el nombre de la propiedad
            propiedad_to_update.nombre = new_nombre
            models.estorage.save()

            return 'Datos actualizados correctamente'

        elif action == 'delete':
            # Obtener el ID de la propiedad a eliminar desde el formulario
            id = int(request.form['id'])

            # Buscar la propiedad en la base de datos
            propiedad_a_eliminar = models.estorage.get(propiedad, id)

            if propiedad_a_eliminar:
                # Eliminar la propiedad
                models.estorage.delete(propiedad_a_eliminar)
                models.estorage.save()
                return f'Propiedad con ID {id} eliminada correctamente'
            else:
                return f'No se encontró una propiedad con ID {id}'

        elif action == 'add':
            # Obtener los datos enviados desde el formulario
            id = request.form['id']
            id_administrador = request.form['id_administrador']
            nombre = request.form['nombre']
            direccion = request.form['direccion']
            numero_telefono = request.form['numero_telefono']
            descripcion = request.form['descripcion']

            # Crear una nueva instancia de la clase propiedad con los datos recibidos
            nueva_propiedad = propiedad(
                id=id,
                id_administrador = id_administrador, 
                nombre=nombre,
                direccion=direccion,
                numero_telefono=numero_telefono,
                descripcion=descripcion
            )

            # Agregar la nueva instancia a la base de datos
            models.estorage.new(nueva_propiedad)
            models.estorage.save()

            return 'Datos agregados correctamente'

    else:
        return render_template('propiedades_crud.html')


@app.route('/crud_admin/generate_pdf', methods=['POST'])
def generate_pdf():
    # Obtener la lista de administradores desde tu base de datos o cualquier otra fuente
    administradores = models.estorage.all(administrador)

    # Generar el contenido HTML para el PDF utilizando una plantilla
    rendered_template = render_template('admin_pdf.html', administradores=administradores)

    # Generar el PDF utilizando flask_weasyprint
    pdf = HTML(string=rendered_template).write_pdf()

    # Devolver el PDF como una respuesta al cliente
    response = make_response(pdf)
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=administradores.pdf'
    return response

@app.route('/crud_admin', methods=['GET', 'POST'])
def crud_data2():
    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'search':
            # Obtener el ID ingresado en el formulario
            id = int(request.form['id'])

            # Buscar el administrador en la base de datos por ID
            searched_admin = models.estorage.get(administrador, id)

            if searched_admin:
                return f'El administrador con ID {id} es: {searched_admin.name_aministrador}'
            else:
                return f'No se encontró ningún administrador con ID {id}'
        
        elif action == 'update':
            # Obtener los datos enviados desde el formulario
            id = int(request.form['id'])
            new_name = request.form['new_name']

            # Obtener el administrador a actualizar
            admin_to_update = models.estorage.get(administrador, id)

            if admin_to_update is None:
                return 'El administrador con el ID {} no existe'.format(id)

            # Actualizar el nombre del administrador
            admin_to_update.name_aministrador = new_name
            models.estorage.save()

            return 'Datos actualizados correctamente'
        
        elif action == 'delete':
            # Obtener el ID del administrador a eliminar desde el formulario
            id = int(request.form['id'])

            # Buscar el administrador en la base de datos
            admin = models.estorage.get(administrador, id)

            if admin:
                # Eliminar el administrador
                models.estorage.delete(admin)
                models.estorage.save()
                return f'Administrador con ID {id} eliminado correctamente'
            else:
                return f'No se encontró ningún administrador con ID {id}'
        
        else:
            return 'Acción no válida'
    
    else:
        return render_template('crud_admin.html')

@app.route('/crud', methods=['GET', 'POST'])
def crud_data():    

    if request.method == 'POST':
        action = request.form['action']
        
        if action == 'search':
            # Obtener el ID ingresado en el formulario
            id = int(request.form['id'])

            # Buscar el dato en la base de datos por ID
            searched_state = models.estorage.get(state, id)

            if searched_state:
                return f'El nombre con ID {id} es: {searched_state.name}'
            else:
                return f'No se encontró ningún estado con ID {id}'
        
        elif action == 'update':
            # Obtener los datos enviados desde el formulario
            id = int(request.form['id'])
            new_name = request.form['new_name']

            # Obtener el objeto state a actualizar
            state_to_update = models.estorage.get(state, id)

            if state_to_update is None:
                return 'El nombre con el ID {} no existe'.format(id)

            # Actualizar el nombre del estado
            state_to_update.name = new_name
            models.estorage.save()

            return 'Datos actualizados correctamente'
        
        elif action == 'delete':
            # Obtener el ID del objeto a eliminar desde el formulario
            id = int(request.form['id'])

            # Buscar el objeto en la base de datos
            obj = models.estorage.all(state)
            for item in obj:
                if item.id == id:
                    # Eliminar el objeto
                    models.estorage.delete(item)
                    models.estorage.save()
                    return f'nombre con ID {id} eliminado correctamente'
            return f'No se encontró un nombre con ID {id}'
        
        elif action == 'add':
            # Obtener los datos enviados desde el formulario
            name = request.form['name']
            id = int(request.form['id'])

            # Crear una nueva instancia de la clase state con los datos recibidos
            new_state = state(id=id, name=name)

            # Agregar la nueva instancia a la base de datos
            models.estorage.new(new_state)
            models.estorage.save()

            return 'Datos agregados correctamente'

    else:
        return render_template('crud.html')

@app.route("/")
def index():
    states = models.estorage.all(state)
    return render_template("index.html", states=states)

if __name__ == '__main__':
    app.run(debug=True)
