from database import db


class Consulta(db.Model):

    __tablename__ = "consultas"

    id_consulta = db.Column(
        db.Integer,
        primary_key=True
    )

    fecha = db.Column(
        db.String(20),
        nullable=False
    )

    diagnostico = db.Column(
        db.String(300),
        nullable=False
    )

    tratamiento = db.Column(
        db.String(300),
        nullable=False
    )


    # CLAVES FORANEAS
    id_medico = db.Column(
        db.Integer,
        db.ForeignKey('medicos.id_medico'),
        nullable=False
    )

    id_paciente = db.Column(
        db.Integer,
        db.ForeignKey('pacientes.id_paciente'),
        nullable=False
    )


    def __init__(
        self,
        fecha,
        diagnostico,
        tratamiento,
        id_medico,
        id_paciente
    ):

        self.fecha = fecha
        self.diagnostico = diagnostico
        self.tratamiento = tratamiento
        self.id_medico = id_medico
        self.id_paciente = id_paciente


    def save(self):

        db.session.add(self)
        db.session.commit()


    @staticmethod
    def get_all():

        consultas = Consulta.query.all()

        return consultas if consultas else []


    @staticmethod
    def get_by_id(id_consulta):

        return Consulta.query.get(id_consulta)


    def update(
        self,
        fecha=None,
        diagnostico=None,
        tratamiento=None,
        id_medico=None,
        id_paciente=None
    ):

        if fecha:
            self.fecha = fecha

        if diagnostico:
            self.diagnostico = diagnostico

        if tratamiento:
            self.tratamiento = tratamiento

        if id_medico:
            self.id_medico = id_medico

        if id_paciente:
            self.id_paciente = id_paciente

        db.session.commit()


    def delete(self):

        db.session.delete(self)
        db.session.commit()