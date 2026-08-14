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


def ejecutar_menu():
    """Ejecuta el menú principal del sistema."""
    tickets = []
    pass


if __name__ == "__main__":
    ejecutar_menu()