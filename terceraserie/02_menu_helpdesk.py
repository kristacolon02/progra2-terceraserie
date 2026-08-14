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


def ejecutar_menu():
    """Ejecuta el menú principal del programa."""
    tickets = []
    pass


if __name__ == "__main__":
    ejecutar_menu()