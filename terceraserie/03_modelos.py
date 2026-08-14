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
            print(f"Error: '{nuevo_estado}' no es un estado permitido.")
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


def main():
    """Crea usuarios y tickets para demostrar el funcionamiento."""

    solicitante = Usuario(
        1,
        "Ana López",
        "ana@email.com",
        "requester"
    )

    tecnico = Usuario(
        2,
        "Carlos Pérez",
        "carlos@email.com",
        "technician"
    )

    ticket_1 = Ticket(
        101,
        "Computadora no enciende",
        "Hardware",
        "High",
        solicitante
    )

    ticket_2 = Ticket(
        102,
        "Error en programa",
        "Software",
        "Medium",
        solicitante
    )

    ticket_3 = Ticket(
        103,
        "Sin conexión a internet",
        "Network",
        "Critical",
        solicitante
    )

    tickets = [ticket_1, ticket_2, ticket_3]

    print("\n--- USUARIOS ---")
    print(solicitante)
    print(tecnico)

    print("\n--- TICKETS INICIALES ---")
    for ticket in tickets:
        print(ticket)

    print("\n--- ASIGNACIÓN DE TÉCNICO ---")
    ticket_1.asignar_tecnico(tecnico)

    print("\n--- CAMBIO DE ESTADO ---")
    ticket_1.cambiar_estado("In Progress")

    print("\n--- INTENTO DE ESTADO NO PERMITIDO ---")
    ticket_1.cambiar_estado("Pending")

    print("\n--- TICKETS FINALES ---")
    for ticket in tickets:
        print(ticket)


if __name__ == "__main__":
    main()
    