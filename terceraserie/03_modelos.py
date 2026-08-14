ESTADOS_VALIDOS = [
    "Open",
    "In Progress",
    "Resolved",
    "Closed",
    "Cancelled"
]


class Usuario:
    """Representa un usuario del sistema HelpDesk."""

    def __init__(self, id_usuario, nombre, email, rol):
        self.id = id_usuario
        self.nombre = nombre
        self.email = email
        self.rol = rol


class Ticket:
    """Representa un ticket de soporte."""

    def __init__(
        self,
        id_ticket,
        titulo,
        categoria,
        prioridad,
        solicitante,
        tecnico=None
    ):
        self.id = id_ticket
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = tecnico
        self._status = "Open"


if __name__ == "__main__":
    pass