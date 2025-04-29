---
nav_title: Seguimiento de datos
article_title: Seguimiento de datos
description: "Este artículo trata de los datos de seguimiento de las páginas de destino."
page_order: 3
alias: /landing_pages/data_tracking/
---

# Seguimiento de datos

> Las páginas de destino de Braze utilizan una versión del SDK Web de Braze para hacer un seguimiento de los datos de usuario sólo cuando se envía un formulario de página de destino. La información que no está asociada a un usuario concreto, incluidas las visitas a páginas y los recuentos agregados de clics en botones, se recopila sin el SDK de la Web.<br><br>Esta página cubre los datos del SDK de la Web y los datos anonimizados que se rastrean en las páginas de destino.

## Métodos de seguimiento

### SDK Web

El SDK de la Web Braze sólo se inicializa cuando un usuario envía un formulario en la página de destino. Antes del envío del formulario, no se recopilan datos personales y el SDK no realiza un seguimiento activo de los usuarios. Una vez completada la inicialización, el SDK no almacena ningún dato en el navegador (como cookies, almacenamiento local u otros).

Cuando se envía un formulario, el SDK recopilará los siguientes datos:

- Evento de presentación del formulario (nombre del evento y hora de presentación)
- Datos especificados por tu equipo en el formulario (como nombre, correo electrónico y número de teléfono)
- Hora de inicio de la sesión
- ID del dispositivo (un ID único que se genera, pero no se almacena, para el dispositivo)
- País determinado por la dirección IP

### Datos anonimizados

Antes de que un usuario envíe un formulario, los datos rastreados en una página de destino consisten únicamente en información anonimizada y no identificable. Consiste en métricas agregadas estándar del sitio web, como el número de páginas vistas (impresiones) y clics que recibe una página de destino.

Dado que estos datos no están vinculados a usuarios identificables, no pueden utilizarse para reorientar o seguir el comportamiento de usuarios individuales.

