class User:
    """Representa un usuario del sistema HelpDesk."""

    def __init__(self, id_user, name, email, role):
        self.id = id_user
        self.name = name
        self.email = email
        self.role = role

    def verificar_credenciales(self, password):
        """Esqueleto para verificar las credenciales del usuario."""
        pass


class Ticket:
    """Representa un ticket de soporte."""

    def __init__(
        self,
        id_ticket,
        title,
        category,
        priority,
        requester,
        technician=None
    ):
        self.id = id_ticket
        self.title = title
        self.category = category
        self.priority = priority
        self.status = "Open"
        self.requester = requester
        self.technician = technician

        self.comments = []
        self.history = []

    def asignar_tecnico(self, technician):
        """Asigna un técnico al ticket."""
        self.technician = technician

    def cambiar_estado(self, new_status):
        """Cambia el estado actual del ticket."""
        self.status = new_status


class Comment:
    """Representa un comentario asociado a un ticket."""

    def __init__(self, id_comment, body, created_at):
        self.id = id_comment
        self.body = body
        self.created_at = created_at

    def mostrar_comentario(self):
        """Devuelve el contenido del comentario."""
        return self.body


class History:
    """Representa un evento del historial de un ticket."""

    def __init__(self, id_history, event_type, detail, created_at):
        self.id = id_history
        self.event_type = event_type
        self.detail = detail
        self.created_at = created_at

    def mostrar_evento(self):
        """Devuelve una descripción del evento."""
        return f"{self.event_type}: {self.detail}"


class Article:
    """Representa un artículo de la base de conocimiento."""

    def __init__(self, id_article, title, body, category, author):
        self.id = id_article
        self.title = title
        self.body = body
        self.category = category
        self.author = author

    def mostrar_articulo(self):
        """Devuelve el título y la categoría del artículo."""
        return f"{self.title} - {self.category}"