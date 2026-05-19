from flask import Blueprint,request,redirect,url_for

from models.medico_model import Medico
from views import medico_view


medico_bp = Blueprint(
    'medico',
    __name__,
    url_prefix='/medicos'
)

@medico_bp.route("/")
def index():

    medicos = Medico.get_all()

    return medico_view.list(medicos)


@medico_bp.route("/create", methods=['GET', 'POST'])
def create():

    if request.method == 'POST':

        nombre = request.form['nombre']
        especialidad = request.form['especialidad']
        telefono = request.form['telefono']
        correo = request.form['correo']

        medico = Medico(
            nombre,
            especialidad,
            telefono,
            correo
        )

        medico.save()

        return redirect(
            url_for('medico.index')
        )

    return medico_view.create()


@medico_bp.route("/edit/<int:id_medico>", methods=['GET', 'POST'])
def edit(id_medico):

    medico = Medico.get_by_id(id_medico)

    if request.method == 'POST':

        medico.update(
            nombre=request.form['nombre'],
            especialidad=request.form['especialidad'],
            telefono=request.form['telefono'],
            correo=request.form['correo']
        )

        return redirect(
            url_for('medico.index')
        )

    return medico_view.edit(medico)


@medico_bp.route("/delete/<int:id_medico>")
def delete(id_medico):

    medico = Medico.get_by_id(id_medico)

    medico.delete()

    return redirect(
        url_for('medico.index')
    )