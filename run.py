from flask import Flask, render_template,redirect,url_for,Blueprint

from database import db

from controllers import usuario_control,paciente_control,medico_control,consulta_control

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///clinica.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(usuario_control.usuario_bp)
app.register_blueprint(paciente_control.paciente_bp)
app.register_blueprint(medico_control.medico_bp)
app.register_blueprint(consulta_control.consulta_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(
        debug=True
    )