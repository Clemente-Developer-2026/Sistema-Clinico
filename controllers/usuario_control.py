from flask import request, redirect, url_for, Blueprint,session
from models.usuario_model import Usuario
from views import usuario_view

usuario_bp = Blueprint('usuario',__name__,url_prefix="/usuarios")

@usuario_bp.route("/")
def index():
    usuarios = Usuario.get_all()
    return usuario_view.list(usuarios)

@usuario_bp.route("/create",methods=['GET','POST'])
def create():
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']

        usuario = Usuario(nombre,username,password,rol)
        usuario.save()
        return redirect(url_for('usuario.index'))

    return usuario_view.create()

@usuario_bp.route("/edit/<int:id>",methods=['GET','POST'])
def edit(id):
    usuario = Usuario.get_by_id(id)
    if request.method == 'POST':
        nombre = request.form['nombre']
        username = request.form['username']
        password = request.form['password']
        rol = request.form['rol']

        usuario.update(nombre = nombre, username = username, password = password, rol = rol)
        return redirect(url_for('usuario.index'))

    return usuario_view.edit(usuario)

@usuario_bp.route("/delete/<int:id>")
def delete(id):
    usuario = Usuario.get_by_id(id)
    usuario.delete()
    return redirect(url_for('usuario.index'))



@usuario_bp.route("/login", methods=['GET', 'POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        usuario = Usuario.get_by_username(username)

        if usuario and usuario.verify_password(password):

            session['usuario_id'] = usuario.id
            session['usuario_nombre'] = usuario.nombre
            session['usuario_rol'] = usuario.rol


            # ADMIN
            if usuario.rol == "admin":

                return redirect(
                    url_for('admin_panel')
                )


            # MEDICO
            elif usuario.rol == "medico":

                return redirect(
                    url_for('medico.index')
                )


            # PACIENTE
            elif usuario.rol == "paciente":

                return redirect(
                    url_for('paciente.index')
                )


        else:

            return "Usuario o contraseña incorrectos"


    return usuario_view.login()