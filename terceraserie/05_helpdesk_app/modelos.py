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

    def es_tecnico(self):
        """Indica si el usuario tiene el rol de técnico."""
        return self.rol.lower() == "technician"

    def __str__(self):
        return (
            f"Usuario #{self.id} | "
            f"Nombre: {self.nombre} | "
            f"Email: {self.email} | "
            f"Rol: {self.rol}"
        )


class Ticket:
    """Representa un ticket de soporte."""

    def __init__(
        self,
        id_ticket,
        titulo,
        categoria,
        prioridad,
        solicitante
    ):
        self.id = id_ticket
        self.titulo = titulo
        self.categoria = categoria
        self.prioridad = prioridad
        self.solicitante = solicitante
        self.tecnico = None
        self._status = "Open"

    @property
    def status(self):
        """Devuelve el estado actual del ticket."""
        return self._status

    def asignar_tecnico(self, tecnico):
        """Asigna un técnico válido al ticket."""
        if not tecnico.es_tecnico():
            return False

        self.tecnico = tecnico
        return True

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado si pertenece a los estados permitidos."""
        if nuevo_estado not in ESTADOS_VALIDOS:
            return False

        self._status = nuevo_estado
        return True

    def __str__(self):
        tecnico_nombre = (
            self.tecnico.nombre
            if self.tecnico is not None
            else "Sin asignar"
        )

        return (
            f"Ticket #{self.id} | "
            f"Título: {self.titulo} | "
            f"Categoría: {self.categoria} | "
            f"Prioridad: {self.prioridad} | "
            f"Solicitante: {self.solicitante.nombre} | "
            f"Técnico: {tecnico_nombre} | "
            f"Estado: {self._status}"
        )