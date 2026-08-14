from modelos import Usuario
from servicios import (
    registrar_ticket,
    listar_tickets,
    buscar_ticket,
    asignar_tecnico,
    cambiar_estado
)


def pedir_opcion():
    """Muestra el menú principal y solicita una opción."""
    print("\n--- HELPDESK APP ---")
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar ticket")
    print("4. Asignar técnico")
    print("5. Cambiar estado")
    print("6. Salir")

    return input("Seleccione una opción: ").strip()


def pedir_id_ticket():
    """Solicita y valida el identificador de un ticket."""
    try:
        return int(input("Ingrese el ID del ticket: ").strip())
    except ValueError:
        print("Error: el ID debe ser un número entero.")
        return None


def ejecutar_menu():
    """Ejecuta el menú principal del sistema HelpDesk."""
    tickets = []

    solicitante = Usuario(
        1,
        "Ana López",
        "ana@gmail.com",
        "requester"
    )

    tecnico = Usuario(
        2,
        "Carlos Pérez",
        "carlos@gmail.com",
        "technician"
    )

    print("\n--- USUARIOS DEL SISTEMA ---")
    print(solicitante)
    print(tecnico)

    while True:
        opcion = pedir_opcion()

        if opcion == "1":
            id_ticket = pedir_id_ticket()

            if id_ticket is None:
                continue

            titulo = input("Título: ").strip()
            categoria = input("Categoría: ").strip()
            prioridad = input("Prioridad: ").strip()

            registrar_ticket(
                tickets,
                id_ticket,
                titulo,
                categoria,
                prioridad,
                solicitante
            )

        elif opcion == "2":
            listar_tickets(tickets)

        elif opcion == "3":
            id_ticket = pedir_id_ticket()

            if id_ticket is None:
                continue

            ticket = buscar_ticket(tickets, id_ticket)

            if ticket is None:
                print("Ticket no encontrado.")
            else:
                print("\n--- TICKET ENCONTRADO ---")
                print(ticket)

        elif opcion == "4":
            id_ticket = pedir_id_ticket()

            if id_ticket is not None:
                asignar_tecnico(
                    tickets,
                    id_ticket,
                    tecnico
                )

        elif opcion == "5":
            id_ticket = pedir_id_ticket()

            if id_ticket is None:
                continue

            nuevo_estado = input(
                "Nuevo estado "
                "(Open, In Progress, Resolved, Closed, Cancelled): "
            ).strip()

            cambiar_estado(
                tickets,
                id_ticket,
                nuevo_estado
            )

        elif opcion == "6":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_menu()