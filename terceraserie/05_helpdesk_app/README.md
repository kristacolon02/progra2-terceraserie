# HelpDesk App

## Descripción

Aplicación de consola que integra programación orientada a objetos, modularidad y gestión de tickets.

El programa permite registrar tickets, buscarlos, asignar un técnico, cambiar su estado y mostrar los tickets registrados.

## Estructura

- `modelos.py`: contiene las clases `Usuario` y `Ticket`.
- `servicios.py`: contiene las funciones para registrar, listar, buscar, asignar técnicos y cambiar estados.
- `main.py`: contiene el menú principal y conecta los modelos con los servicios.

## Ejecución

Ejecutar el programa desde la carpeta `05_helpdesk_app` con:

```bash
python main.py