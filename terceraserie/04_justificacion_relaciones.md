# Justificación de Relaciones - HelpDesk

## User y Ticket como solicitante

Relación:

`User "1" -- "0..*" Ticket`

Un usuario puede solicitar cero o muchos tickets durante el uso del sistema. Cada ticket debe pertenecer a un único solicitante.

Esta relación es una asociación porque User y Ticket pueden existir de forma independiente.

## User y Ticket como técnico

Relación:

`User "0..1" -- "0..*" Ticket`

Un ticket puede no tener técnico asignado o puede tener un solo técnico. Un técnico puede atender cero o muchos tickets.

La multiplicidad `0..1` representa que la asignación del técnico es opcional.

## Ticket y Comment

Relación:

`Ticket "1" *-- "0..*" Comment`

Un ticket puede contener cero o muchos comentarios.

Se utiliza composición porque Comment depende del Ticket al que pertenece. El rombo negro se coloca del lado de Ticket, ya que Ticket representa el todo y Comment representa la parte dependiente.

## Ticket y History

Relación:

`Ticket "1" *-- "0..*" History`

Un ticket puede registrar cero o muchos eventos en su historial.

Se utiliza composición porque los registros de History están asociados al ciclo de vida del Ticket. El rombo negro se coloca del lado de Ticket porque es el objeto principal que contiene el historial.

## User y Article

Relación:

`User "1" -- "0..*" Article`

Un usuario puede publicar cero o muchos artículos.

Se utiliza una asociación porque User y Article conservan identidad propia y no existe dependencia total de ciclo de vida entre ambos.

## Criterio de ciclo de vida

Las relaciones Ticket-Comment y Ticket-History utilizan composición porque Comment y History representan información que pertenece directamente a un Ticket.

Las relaciones User-Ticket y User-Article se representan mediante asociaciones porque las entidades relacionadas pueden existir de forma independiente.