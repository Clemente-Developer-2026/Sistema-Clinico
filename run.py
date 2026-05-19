from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import session

from database import db


# IMPORTAR CONTROLADORES
from controllers.usuario_control import usuario_bp
from controllers.medico_control import medico_bp
from controllers.paciente_control import paciente_bp
from controllers.consulta_control import consulta_bp


# IMPORTAR MODELOS
from models.usuario_model import Usuario
from models.medico_model import Medico
from models.paciente_model import Paciente
from models.consulta_model import Consulta


app = Flask(__name__)


# CONFIGURACION
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinica.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


# CLAVE PARA SESIONES
app.secret_key = "clave_super_secreta_clinica"


# INICIALIZAR DB
db.init_app(app)


# REGISTRAR BLUEPRINTS
app.register_blueprint(usuario_bp)

app.register_blueprint(medico_bp)

app.register_blueprint(paciente_bp)

app.register_blueprint(consulta_bp)


# RUTA PRINCIPAL
@app.route("/")
def index():

    return render_template(
        "index.html"
    )


# PANEL ADMINISTRADOR
@app.route("/admin")
def admin_panel():

    # VALIDAR LOGIN
    if 'usuario_id' not in session:

        return redirect(
            url_for('usuario.login')
        )


    # VALIDAR ROL
    if session['usuario_rol'] != "admin":

        return redirect(
            url_for('index')
        )


    usuarios = Usuario.get_all()

    medicos = Medico.get_all()

    pacientes = Paciente.get_all()

    consultas = Consulta.get_all()


    return render_template(

        "administrador/admin.html",

        usuarios=usuarios,

        medicos=medicos,

        pacientes=pacientes,

        consultas=consultas
    )


# CERRAR SESION
@app.route("/logout")
def logout():

    session.clear()

    return redirect(
        url_for('usuario.login')
    )


# EJECUTAR
if __name__ == "__main__":

    with app.app_context():

        db.create_all()

    app.run(
        debug=True
    )