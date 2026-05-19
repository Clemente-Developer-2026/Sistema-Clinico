from flask import Blueprint,redirect,request,url_for
from models.consulta_model import Consulta
from models.medico_model import Medico
from models.paciente_model import Paciente

from views import consulta_view


consulta_bp = Blueprint(
    'consulta',
    __name__,
    url_prefix='/consultas'
)

@consulta_bp.route("/")
def index():

    consultas = Consulta.get_all()

    return consulta_view.list(consultas)


@consulta_bp.route("/create", methods=['GET', 'POST'])
def create():

    medicos = Medico.get_all()
    pacientes = Paciente.get_all()

    if request.method == 'POST':

        fecha = request.form['fecha']
        diagnostico = request.form['diagnostico']
        tratamiento = request.form['tratamiento']
        id_medico = request.form['id_medico']
        id_paciente = request.form['id_paciente']

        consulta = Consulta(
            fecha,
            diagnostico,
            tratamiento,
            id_medico,
            id_paciente
        )

        consulta.save()

        return redirect(
            url_for('consulta.index')
        )

    return consulta_view.create(
        medicos,
        pacientes
    )


@consulta_bp.route("/edit/<int:id_consulta>", methods=['GET', 'POST'])
def edit(id_consulta):

    consulta = Consulta.get_by_id(id_consulta)

    medicos = Medico.get_all()
    pacientes = Paciente.get_all()

    if request.method == 'POST':

        consulta.update(
            fecha=request.form['fecha'],
            diagnostico=request.form['diagnostico'],
            tratamiento=request.form['tratamiento'],
            id_medico=request.form['id_medico'],
            id_paciente=request.form['id_paciente']
        )

        return redirect(
            url_for('consulta.index')
        )

    return consulta_view.edit(
        consulta,
        medicos,
        pacientes
    )


@consulta_bp.route("/delete/<int:id_consulta>")
def delete(id_consulta):

    consulta = Consulta.get_by_id(id_consulta)

    consulta.delete()

    return redirect(
        url_for('consulta.index')
    )