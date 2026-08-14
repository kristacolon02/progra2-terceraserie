from modelos import Ticket


def registrar_ticket(
    tickets,
    id_ticket,
    titulo,
    categoria,
    prioridad,
    solicitante
):
    """Crea un ticket y lo agrega a la lista."""
    nuevo_ticket = Ticket(
        id_ticket,
        titulo,
        categoria,
        prioridad,
        solicitante
    )

    tickets.append(nuevo_ticket)

    print("Ticket registrado correctamente.")

    return nuevo_ticket


def listar_tickets(tickets):
    """Muestra todos los tickets registrados."""
    if len(tickets) == 0:
        print("No hay tickets registrados.")
        return

    print("\n--- LISTA DE TICKETS ---")

    for ticket in tickets:
        print(ticket)


def buscar_ticket(tickets, id_ticket):
    """Busca un ticket por su identificador."""
    for ticket in tickets:
        if ticket.id == id_ticket:
            return ticket

    return None


def asignar_tecnico(tickets, id_ticket, tecnico):
    """Busca un ticket y le asigna un técnico."""
    ticket = buscar_ticket(tickets, id_ticket)

    if ticket is None:
        print("Error: ticket no encontrado.")
        return False

    if not ticket.asignar_tecnico(tecnico):
        print("Error: el usuario no tiene rol technician.")
        return False

    print(f"Técnico {tecnico.nombre} asignado correctamente.")
    return True


def cambiar_estado(tickets, id_ticket, nuevo_estado):
    """Busca un ticket y cambia su estado."""
    ticket = buscar_ticket(tickets, id_ticket)

    if ticket is None:
        print("Error: ticket no encontrado.")
        return False

    if not ticket.cambiar_estado(nuevo_estado):
        print("Error: estado no permitido.")
        return False

    print(f"Estado cambiado correctamente a: {ticket.status}")
    return True
