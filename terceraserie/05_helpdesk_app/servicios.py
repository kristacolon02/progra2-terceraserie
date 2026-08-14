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