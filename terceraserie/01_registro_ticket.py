CATEGORIAS_VALIDAS = ["General", "Hardware", "Software", "Network"]
PRIORIDADES_VALIDAS = ["Low", "Medium", "High", "Critical"]


def main():
    """Ejecuta el registro de un ticket."""

    try:
        numero_ticket = int(input("Ingrese el número de ticket: ").strip())
    except ValueError:
        print("Error: el número de ticket debe ser un número entero.")
        return

    solicitante = input("Ingrese el nombre del solicitante: ").strip()
    titulo = input("Ingrese el título del ticket: ").strip()
    descripcion = input("Ingrese la descripción: ").strip()
    categoria = input("Ingrese la categoría: ").strip()
    prioridad = input("Ingrese la prioridad: ").strip()

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

    print("\n--- RESUMEN DEL TICKET ---")
    print(f"Número: {ticket['numero']}")
    print(f"Solicitante: {ticket['solicitante']}")
    print(f"Título: {ticket['titulo']}")
    print(f"Descripción: {ticket['descripcion']}")
    print(f"Categoría: {ticket['categoria']}")
    print(f"Prioridad: {ticket['prioridad']}")
    print(f"Status: {ticket['status']}")


if __name__ == "__main__":
    main()