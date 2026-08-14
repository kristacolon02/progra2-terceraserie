CATEGORIAS_VALIDAS = ["General", "Hardware", "Software", "Network"]
PRIORIDADES_VALIDAS = ["Low", "Medium", "High", "Critical"]


def pedir_opcion():
    """Solicita una opción del menú al usuario."""
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

    if not solicitante or not titulo or not descripcion:
        print("Error: los campos obligatorios no pueden estar vacíos.")
        return

    if categoria not in CATEGORIAS_VALIDAS:
        print("Error: categoría no válida.")
        return

    if prioridad not in PRIORIDADES_VALIDAS:
        print("Error: prioridad no válida.")
        return

    ticket = {
        "numero": numero_ticket,
        "solicitante": solicitante,
        "titulo": titulo,
        "descripcion": descripcion,
        "categoria": categoria,
        "prioridad": prioridad,
        "status": "Open"
    }

    tickets.append(ticket)
    print("Ticket registrado correctamente.")


def ejecutar_menu():
    """Ejecuta el menú principal del programa."""
    tickets = []
    pass


if __name__ == "__main__":
    ejecutar_menu()