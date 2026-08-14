CATEGORIAS_VALIDAS = ["General", "Hardware", "Software", "Network"]
PRIORIDADES_VALIDAS = ["Low", "Medium", "High", "Critical"]


def pedir_opcion():
    """Muestra el menú y solicita una opción al usuario."""
    print("\n--- MENÚ HELPDESK ---")
    print("1. Registrar ticket")
    print("2. Listar tickets")
    print("3. Buscar por solicitante")
    print("4. Resumen por prioridad")
    print("5. Salir")

    return input("Seleccione una opción: ").strip()


def registrar_ticket(tickets):
    """Registra un nuevo ticket y lo agrega a la lista."""
    try:
        numero_ticket = int(input("Número de ticket: ").strip())
    except ValueError:
        print("Error: el número de ticket debe ser un número entero.")
        return

    solicitante = input("Solicitante: ").strip()
    titulo = input("Título: ").strip()
    descripcion = input("Descripción: ").strip()
    categoria = input("Categoría: ").strip()
    prioridad = input("Prioridad: ").strip()

    if (
        not solicitante
        or not titulo
        or not descripcion
        or not categoria
        or not prioridad
    ):
        print("Error: los campos obligatorios no pueden estar vacíos.")
        return

    categoria_correcta = None

    for opcion in CATEGORIAS_VALIDAS:
        if opcion.lower() == categoria.lower():
            categoria_correcta = opcion
            break

    if categoria_correcta is None:
        print("Error: categoría no válida.")
        return

    prioridad_correcta = None

    for opcion in PRIORIDADES_VALIDAS:
        if opcion.lower() == prioridad.lower():
            prioridad_correcta = opcion
            break

    if prioridad_correcta is None:
        print("Error: prioridad no válida.")
        return

    ticket = {
        "numero": numero_ticket,
        "solicitante": solicitante,
        "titulo": titulo,
        "descripcion": descripcion,
        "categoria": categoria_correcta,
        "prioridad": prioridad_correcta,
        "status": "Open"
    }

    tickets.append(ticket)
    print("Ticket registrado correctamente.")


def listar_tickets(tickets):
    """Muestra todos los tickets registrados."""
    if len(tickets) == 0:
        print("No hay tickets registrados.")
        return

    print("\n--- LISTA DE TICKETS ---")

    for ticket in tickets:
        print(
            f"Ticket #{ticket['numero']} | "
            f"Solicitante: {ticket['solicitante']} | "
            f"Título: {ticket['titulo']} | "
            f"Prioridad: {ticket['prioridad']} | "
            f"Status: {ticket['status']}"
        )


def buscar_por_solicitante(tickets):
    """Busca tickets por el nombre del solicitante."""
    nombre = input("Ingrese el nombre del solicitante: ").strip().lower()

    encontrados = []

    for ticket in tickets:
        if ticket["solicitante"].lower() == nombre:
            encontrados.append(ticket)

    if len(encontrados) == 0:
        print("No se encontraron tickets para ese solicitante.")
        return

    print("\n--- TICKETS ENCONTRADOS ---")

    for ticket in encontrados:
        print(
            f"Ticket #{ticket['numero']} | "
            f"Título: {ticket['titulo']} | "
            f"Prioridad: {ticket['prioridad']} | "
            f"Status: {ticket['status']}"
        )


def mostrar_resumen(tickets):
    """Muestra la cantidad de tickets por prioridad."""
    if len(tickets) == 0:
        print("No hay tickets registrados.")
        return

    print("\n--- RESUMEN POR PRIORIDAD ---")

    for prioridad in PRIORIDADES_VALIDAS:
        cantidad = 0

        for ticket in tickets:
            if ticket["prioridad"].lower() == prioridad.lower():
                cantidad += 1

        print(f"{prioridad}: {cantidad}")

    print(f"Total de tickets: {len(tickets)}")


def ejecutar_menu():
    """Ejecuta el menú principal del sistema HelpDesk."""
    tickets = []

    while True:
        opcion = pedir_opcion()

        if opcion == "1":
            registrar_ticket(tickets)

        elif opcion == "2":
            listar_tickets(tickets)

        elif opcion == "3":
            buscar_por_solicitante(tickets)

        elif opcion == "4":
            mostrar_resumen(tickets)

        elif opcion == "5":
            print("Programa finalizado.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    ejecutar_menu()
    