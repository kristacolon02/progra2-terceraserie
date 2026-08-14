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

    def asignar_tecnico(self, tecnico):
        """Asigna un técnico al ticket si su rol es válido."""
        if tecnico.rol.lower() != "technician":
            print("Error: el usuario seleccionado no tiene rol technician.")
            return

        self.tecnico = tecnico
        print(f"Técnico {tecnico.nombre} asignado correctamente.")

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado del ticket si el valor es válido."""
        if nuevo_estado not in ESTADOS_VALIDOS:
            print("Error: estado no permitido.")
            return

        self._status = nuevo_estado
        print(f"Estado cambiado correctamente a: {self._status}")

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


if __name__ == "__main__":
    pass