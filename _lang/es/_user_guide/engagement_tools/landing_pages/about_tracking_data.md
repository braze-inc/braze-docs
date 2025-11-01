---
nav_title: Acerca de los datos de seguimiento
article_title: Acerca de los datos de seguimiento de la página de destino
description: "Infórmate sobre el seguimiento y los datos anónimos de las páginas de destino en Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# Acerca de los datos de seguimiento de la página de destino

> Infórmate sobre el seguimiento y los datos anónimos de las páginas de destino en Braze.

## Métodos de seguimiento

### SDK Web

El SDK de la Web Braze sólo se inicializa cuando un usuario envía un formulario en la página de destino. Antes del envío del formulario, no se recopilan datos personales y el SDK no realiza un seguimiento activo de los usuarios. Una vez completada la inicialización, el SDK no almacena ningún dato en el navegador (como cookies, almacenamiento local u otros).

Cuando se envía un formulario, el SDK recogerá los siguientes datos:

- Evento de presentación del formulario (nombre del evento y hora de presentación)
- Datos especificados por tu equipo en el formulario (como nombre, correo electrónico y número de teléfono)
- Hora de inicio de la sesión
- ID del dispositivo (un ID único que se genera, pero no se almacena, para el dispositivo)
- País determinado por la dirección IP

### Datos anonimizados

Antes de que un usuario envíe un formulario, los datos rastreados en una página de destino consisten únicamente en información anonimizada y no identificable. Consiste en métricas agregadas estándar del sitio web, como el número de páginas vistas (impresiones) y clics que recibe una página de destino.

Dado que estos datos no están vinculados a usuarios identificables, no pueden utilizarse para reorientar o seguir el comportamiento de usuarios individuales.

