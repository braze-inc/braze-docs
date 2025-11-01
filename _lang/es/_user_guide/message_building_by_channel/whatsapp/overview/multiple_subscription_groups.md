---
nav_title: Múltiples cuentas de empresa
article_title: Múltiples cuentas de WhatsApp Business y números de teléfono
page_order: 2
description: "Este artículo de referencia cubre los pasos para añadir cuentas y números de teléfono de WhatsApp Business."
page_type: reference
channel:
  - WhatsApp
---

# Varias cuentas y números de teléfono de WhatsApp Business

> Puedes añadir varias cuentas de WhatsApp Business y grupos de suscripción (y números de teléfono) a cada espacio de trabajo. <br><br>Cada grupo de suscripción está conectado a un único número de teléfono, por lo que no puedes conectar el mismo número de teléfono a varios grupos de suscripción ni conectar varios números de teléfono a un grupo de suscripción.

## Varias cuentas de WhatsApp Business 

Tener varias cuentas de WhatsApp Business es útil si quieres enviar mensajes de WhatsApp a usuarios de un espacio de trabajo Braze que tenga varias marcas. Esto se debe a que cada cuenta de empresa funciona por separado dentro de WhatsApp y tiene su propio número de teléfono, plantilla de mensaje y tasa de calidad.

Las cuentas de empresa que estén anidadas dentro del mismo Meta Business Manager también compartirán la gestión de permisos de acceso de usuario y los catálogos (aún no se admite en Braze).

\![Diagrama del ecosistema de Braze y WhatsApp, que muestra cómo se conectan entre sí los espacios de trabajo y las cuentas de WhatsApp Business: puedes conectar un grupo de suscripción a un número de teléfono, varias cuentas de WhatsApp Business a un espacio de trabajo, y un espacio de trabajo a varias carteras Meta Business.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### Añadir una cuenta de WhatsApp Business

Puedes añadir hasta 10 cuentas de WhatsApp Business por espacio de trabajo. Las cuentas de empresa pueden estar anidadas en distintos Metaadministradores de empresa. Para añadir una cuenta:

1. Ve a **Socios tecnológicos** > **WhatsApp** y selecciona **Añadir cuenta de WhatsApp Business**. 

\![Sección de integración de mensajería de WhatsApp con opciones para añadir una cuenta de empresa o añadir un grupo de suscripción y un número.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. Sigue el proceso de registro. Para una guía detallada paso a paso, consulta [el registro integrado de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/).

{% alert important %}
Tu número de teléfono debe cumplir todos los requisitos de cualquier número de teléfono de WhatsApp, incluido el de no estar registrado en ninguna otra cuenta de WhatsApp.
{% endalert %}

## Múltiples grupos de suscripción y números de teléfono

Las plantillas de mensajes se comparten entre todos los números de teléfono de la misma cuenta de WhatsApp Business. Para obtener más información sobre los grupos de suscripción de WhatsApp, consulta [Grupos de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).

Cada número de teléfono de WhatsApp aparecerá como un chat de WhatsApp independiente para los usuarios. Cada número de teléfono de una cuenta de WhatsApp Business funciona independientemente de los demás, por lo que pueden tener los mismos o distintos valores para lo siguiente: 
- Mostrar nombre 
- Estado 
- Tasa de calidad 
- Límite de mensajería 

### Añadir un grupo de suscripción y un número de teléfono

Puedes añadir hasta 20 grupos de suscripción (y números de teléfono de envío) por cuenta de WhatsApp Business. Para añadir un grupo de suscripción y un número de teléfono:

1. Ve a **Socios tecnológicos** > **WhatsApp** y selecciona **Añadir grupo de suscripción y número**.

\![Sección de integración de mensajería de WhatsApp con opciones para añadir una cuenta de empresa o añadir un grupo de suscripción y un número.]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\. Sigue el proceso de registro. <br><br> En el paso **Selecciona tu cuenta de WhatsApp** Business, selecciona tu cuenta de WhatsApp Business existente y añade un nuevo número de teléfono. Este número debe cumplir todos los requisitos de cualquier número de teléfono de WhatsApp, incluido el de no estar registrado en ninguna otra cuenta de WhatsApp.

### Eliminar un grupo de suscripción y un número de teléfono 

1. Ve a **Audiencia** > **Suscripciones** y archiva el grupo de suscripción.
2. Ve a tu administrador de Meta Business y elimina el número de teléfono.
