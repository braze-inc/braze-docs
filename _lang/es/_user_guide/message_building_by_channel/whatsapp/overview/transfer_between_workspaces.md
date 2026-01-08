---
nav_title: Transferencia entre espacios de trabajo
article_title: Transfiere números de teléfono y grupos de suscripción entre espacios de trabajo
page_order: 4
description: "Este artículo de referencia explica cómo transferir tu número de teléfono de WhatsApp y tus grupos de suscripción entre espacios de trabajo."
page_type: reference
channel:
  - WhatsApp
---

# Transfiere números de teléfono de WhatsApp y grupos de suscripción entre espacios de trabajo

> Esta página explica cómo puedes mover un número de teléfono de una cuenta de WhatsApp Business (WABA) y su grupo de suscripción asociado de un espacio de trabajo a otro dentro de Braze. Este proceso agiliza tu experiencia de uso de WhatsApp con Braze, y reduce la necesidad de ayuda de ingeniería.

## Requisitos previos

- Confirma que tienes el [permiso de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) "Gestionar grupos de suscripción" tanto en el espacio de trabajo original como en el nuevo.
- La WABA no puede atravesar varios [grupos de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints). Es poco probable que esto ocurra si trabajas en una sola empresa. 

## Transferir un número de teléfono y un grupo de suscripción

### Paso 1: Archiva el grupo de suscripción

Para archivar un grupo de suscripción de WhatsApp, sigue estos pasos:

1. Ve al espacio de trabajo donde existe actualmente el grupo de suscripción.
2. Ve a **Audiencia** > **Gestión de grupos de suscripción** y busca el grupo de suscripción asociado al número de teléfono de WhatsApp que quieres mover.
3. Pasa el ratón por encima del estado del grupo de suscripción y selecciona <i class="fa-solid fa-box-archive"></i> **Archivo**, que marcará el grupo de suscripción como inactivo pero no lo eliminará.

Aparece el botón "Archivar" al pasar el ratón por encima del estado "Activo" de un grupo de suscripción.]({% image_buster /assets/img/whatsapp/archive_subscription_group.png %}){: style="max-width:70%;"}

### Paso 2: Integrar el número de teléfono de WhatsApp en el nuevo espacio de trabajo

1. Ve al espacio de trabajo al que quieras mover el número de teléfono de WhatsApp.
2. Ve a **Integraciones de socios** > **Socios tecnológicos** > **WhatsApp** y, a continuación, desplázate hasta la sección **Integración de mensajería de WhatsApp**. 
3. Selecciona la opción **Crear nuevo grupo de suscripción y número de teléfono**
4. Comienza el proceso de integración, durante el cual puedes seleccionar el número de teléfono del grupo de suscripción archivado.

### Paso 3: Verifica la integración

1. Tras completar la integración, confirma que el número de teléfono de WhatsApp está ahora asociado al grupo de suscripción en el nuevo espacio de trabajo.
2. Prueba para confirmar que se pueden enviar y recibir mensajes a través de ese número de teléfono de WhatsApp.

## Consideraciones

- Si necesitas volver a transferir el número de teléfono de WhatsApp al espacio de trabajo original, repite los pasos. Archiva el grupo de suscripción en el espacio de trabajo de destino, y luego intégralo en el espacio de trabajo original.
- No necesitas eliminar el número de teléfono de WhatsApp de tu administrador de Meta Business durante la transferencia.