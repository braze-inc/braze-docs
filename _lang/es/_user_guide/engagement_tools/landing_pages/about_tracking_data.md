---
nav_title: Acerca del seguimiento de datos
article_title: Acerca de los datos de seguimiento de la página de destino
description: "Infórmate sobre el seguimiento y los datos anónimos de las páginas de destino en Braze."
page_order: 10
alias: /landing_pages/data_tracking/
---

# Acerca de los datos de seguimiento de la página de destino

> Infórmate sobre el seguimiento y los datos anónimos de las páginas de destino en Braze.

## Métodos de seguimiento

### SDK Web

El SDK Web de Braze se inicializa cuando un usuario envía un formulario en una página de destino. Antes del envío del formulario, no se recopilan datos personales y el SDK no realiza un seguimiento activo de los usuarios. Una vez completada la inicialización, el SDK no almacena ningún dato en el navegador (como cookies, almacenamiento local u otros). 

El SDK web de Braze se inicializa inmediatamente cuando un usuario navega a la página de destino a través de un enlace generado por una etiqueta{% raw %}`{% landing_page_url %}`{% endraw %} de Liquid en un mensaje de Braze.

Cuando se envía un formulario, el SDK recopilará los siguientes datos:

- Evento de presentación del formulario (nombre del evento y hora de presentación)
- Datos especificados por tu equipo en el formulario (como nombre, correo electrónico y número de teléfono)
- Hora de inicio de la sesión
- ID del dispositivo (un ID único que se genera, pero no se almacena, para el dispositivo)
- País determinado por la dirección IP

### Datos anonimizados

Antes de que un usuario envíe un formulario, los datos rastreados en una página de destino consisten únicamente en información anonimizada y no identificable. Consiste en métricas agregadas estándar del sitio web, como el número de páginas vistas (impresiones) y clics que recibe una página de destino.

Dado que estos datos no están vinculados a usuarios identificables, no pueden utilizarse para reorientar o seguir el comportamiento de usuarios individuales.

## Fusión de perfiles de usuario duplicados

Braze no fusiona automáticamente a los usuarios en función de atributos, como el correo electrónico o el teléfono, cuando se envía un formulario de la página de destino. Si se envía un formulario con un correo electrónico o un número de teléfono que coincide con un perfil de usuario existente, Braze crea un perfil de usuario independiente.

Para fusionar perfiles de usuario duplicados, puedes:

- Desencadena el[`/users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)[punto final]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) cuando se envíe un formulario de la página de destino para fusionar el nuevo perfil con uno ya existente.
- Programar [la fusión masiva]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging) para fusionar periódicamente los perfiles duplicados basándose en identificadores coincidentes.

