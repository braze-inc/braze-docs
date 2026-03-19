---
nav_title: Aprobaciones
article_title: Aprobaciones
page_order: 1
page_type: reference
description: "Este artículo de referencia ofrece un resumen de los distintos estados que pueden tener una campaña y Canvas, y lo que significan."
tool:
    - Campaigns
    - Canvas
---

# Aprobaciones para campañas y lienzos

> Utiliza las aprobaciones para añadir un punto de control final a tus campañas y lienzos antes de su lanzamiento. Con este flujo de trabajo, puedes verificar y aprobar el contenido de todas las secciones obligatorias de tu mensaje.

## Cómo funciona

Puedes revisar los detalles de tu campaña o Canvas en el último paso de la edición. 

Tanto en los lienzos como en las campañas, debes guardar todos los cambios antes de aprobarlos, incluso si son cambios propios. Un usuario con los permisos adecuados debe aprobar cada sección del resumen antes de que se pueda enviar el mensaje. El estado predeterminado de cada sección es **«Pendiente de aprobación**».

{% tabs %}
{% tab campaign %}
Para lanzar una campaña, debes aprobar los siguientes componentes:

- **Mensajes:** Este es el mensaje de la campaña.
- **Entrega:** Este es el tipo de entrega y determina cuándo reciben los usuarios la campaña.
- **Público objetivo** Esto determina quién recibirá la campaña.
- **Eventos de conversión:** Esta es la métrica que estás realizando el seguimiento con fines de interacción y generación de informes.
{% endtab %}

{% tab canvas %}
Para lanzar un Canvas, debes aprobar estos componentes clave:

- **Eventos de conversión:** Esta es la métrica que estás realizando el seguimiento con fines de interacción y generación de informes.
- **Horario de entrada:** Esto incluye el tipo de calendario de entradas y cuándo los usuarios entran en Canvas.
- **Público objetivo** Esto determina quién entrará en este Canvas.
- **Enviar configuración:** Estas son las opciones de envío para todos los pasos en Canvas. 
- **Crear Canvas:** Este es el recorrido del usuario de Canvas.
{% endtab %}
{% endtabs %}

## Activación del flujo de trabajo de aprobación

De forma predeterminada, la configuración del flujo de trabajo de aprobación está desactivada para las campañas y los lienzos. Para activar esta característica, ve a **Configuración** > **Flujo de trabajo de aprobación** y selecciona la opción correspondiente para alternarla:

- **Utiliza el flujo de trabajo de aprobación para todas las campañas en [tu espacio de trabajo].**
- **Utiliza el flujo de trabajo de aprobación para todos los lienzos en [tu espacio de trabajo].**

{% alert important %}
La aprobación de campañas no es compatible con [las campañas API]({{site.baseurl}}/api/api_campaigns) y [las campañas de correo electrónico transaccional]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Establecer permisos de usuario

Después de activar el flujo de trabajo de aprobación, debes configurar los permisos de usuario para que los usuarios de tu empresa puedan aprobar o rechazar campañas y lienzos. Ambos permisos también se pueden aplicar a espacios de trabajo o [equipos,]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) o añadirse a un [conjunto de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
Debes tener el [permiso «Aprobar y rechazar campañas]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)». Este permiso controla quién puede actualizar el estado de aprobación de una campaña. Con este permiso, puedes hacer lo siguiente:

- Autoaprueba la campaña
- Aprobar y lanzar la campaña.
- Aprobar la campaña, pero no lanzarla (otro usuario con permiso para «Enviar campañas y encuestas» puede lanzar la campaña).
- No aprobar ni lanzar la campaña.

Una vez establecidos los estados de aprobación en el paso **Resumen**, cualquier cambio posterior que se realice en la campaña restablecerá todos los estados de aprobación al guardarlo. Esto se aplica a cualquier cambio realizado tanto en un borrador de campaña como en una campaña posterior al lanzamiento. Por ejemplo, si solo realizas cambios en la audiencia objetivo, el paso **Resumen** restablece el estado de aprobación de todas las secciones al estado predeterminado, **Pendiente de aprobación**.

{% endtab %}

{% tab canvas %}
Debes tener el [permiso «Aprobar y rechazar lienzos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions)». Este permiso controla quién puede actualizar el estado de aprobación de un Canvas. Con este permiso, puedes hacer lo siguiente:

- Autoaprueba el Canvas
- Aprobar y poner en marcha el lienzo
- Aprobar pero no lanzar el Canvas (otro usuario con permiso para «Enviar campañas, Canvases» puede lanzar el Canvas).
- No aprobar ni lanzar Canvas

Una vez establecidos los estados de aprobación en el paso **Resumen**, cualquier cambio posterior realizado en el Canvas restablecerá todos los estados de aprobación al guardarlo. Esto se aplica a cualquier cambio realizado tanto en un borrador de Canvas como en un Canvas posterior al lanzamiento. Por ejemplo, si solo realizas cambios en la audiencia objetivo, el paso **Resumen** revierte los estados de aprobación de todas las secciones al estado predeterminado, **Pendiente de aprobación**.

{% alert note %}
**Estado de aprobación y guardado**

- Cuando haces clic en **Aprobar** para una sección en el paso **Resumen**, esa aprobación se guarda inmediatamente.
- El botón **Guardar** guarda los cambios realizados en el contenido y la configuración del Canvas, pero no el estado de aprobación.

Para evitar perder las aprobaciones:

1. Realiza los cambios que necesites en Canvas y, a continuación, haz clic en **Guardar**.
2. Una vez que Canvas haya terminado de guardar, aprueba las secciones pertinentes en el paso **Resumen**.
3. Vuelve a hacer clic en **Guardar** solo si realizas cambios adicionales en Canvas después de la aprobación. Si cambias el Canvas y guardas los cambios, todos los estados de aprobación se restablecerán a **«Pendiente de aprobación**».
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Para editar una campaña en vivo, necesitas el permiso «Aprobar y rechazar campañas». Los usuarios deben aprobar sus cambios porque aún no hay disponible una versión preliminar de Campañas. Este no es el caso de los Lienzos, ya que un usuario puede hacer cambios y guardarlos como borrador, y otro usuario puede aprobar y lanzar el Lienzo.
{% endalert %}