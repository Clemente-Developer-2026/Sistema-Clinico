from flask import Blueprint, redirect,request,url_for
from models.paciente_model import Paciente
from views import paciente_view


paciente_bp = Blueprint(
    'paciente',
    __name__,
    url_prefix='/pacientes'
)


@paciente_bp.route("/")
def index():

    pacientes = Paciente.get_all()

    return paciente_view.list(pacientes)


@paciente_bp.route("/create", methods=['GET', 'POST'])
def create():

    if request.method == 'POST':

        nombre = request.form['nombre']
        edad = request.form['edad']
        direccion = request.form['direccion']
        telefono = request.form['telefono']

        paciente = Paciente(
            nombre,
            edad,
            direccion,
            telefono
        )

        paciente.save()

        return redirect(
            url_for('paciente.index')
        )

    return paciente_view.create()


@paciente_bp.route("/edit/<int:id_paciente>", methods=['GET', 'POST'])
def edit(id_paciente):

    paciente = Paciente.get_by_id(id_paciente)

    if request.method == 'POST':

        paciente.update(
            nombre=request.form['nombre'],
            edad=request.form['edad'],
            direccion=request.form['direccion'],
            telefono=request.form['telefono']
        )

        return redirect(
            url_for('paciente.index')
        )

    return paciente_view.edit(paciente)


@paciente_bp.route("/delete/<int:id_paciente>")
def delete(id_paciente):

    paciente = Paciente.get_by_id(id_paciente)

    paciente.delete()

    return redirect(
        url_for('paciente.index')
    )