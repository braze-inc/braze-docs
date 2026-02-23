---
nav_title: Aprobaciones
article_title: Aprobaciones
page_order: 1
page_type: reference
description: "Este artículo de referencia ofrece un resumen de los distintos estados que pueden tener una campaña y Canvas y lo que significan."
tool:
    - Campaigns
    - Canvas
---

# Aprobación de campañas y lonas

> Utiliza las aprobaciones para añadir un punto de control final a tus campañas y Lienzos antes de su lanzamiento. Con este flujo de trabajo, puedes verificar y aprobar el contenido de todas las secciones necesarias de tu mensaje.

## Cómo funciona

Puedes revisar los detalles de tu campaña o Canvas en el último paso de la edición. 

Tanto para los lienzos como para las campañas, debes guardar todos los cambios antes de aprobarlos, aunque sean cambios tuyos. Un usuario con los permisos adecuados debe aprobar cada sección del resumen antes de que el mensaje pueda lanzarse. El estado predeterminado de cada sección es **Pendiente de aprobación**.

{% tabs %}
{% tab campaign %}
Para lanzar una campaña, debes aprobar estos componentes:

- **Mensajes:** Éste es el mensaje de la campaña.
- **Entrega:** Es el tipo de entrega y determina cuándo los usuarios reciben la Campaña.
- **Público objetivo** Esto determina quién recibirá la Campaña.
- **Eventos de conversión:** Esta es la métrica que estás siguiendo con fines de interacción y elaboración de informes.
{% endtab %}

{% tab canvas %}
Para lanzar un Canvas, debes aprobar estos componentes clave:

- **Eventos de conversión:** Esta es la métrica que estás siguiendo con fines de interacción y elaboración de informes.
- **Horario de entrada:** Esto incluye el tipo de horario de entrada y cuándo entran los usuarios en el Canvas.
- **Público objetivo** Esto determina quién entrará en este Canvas.
- **Configuración de envío:** Estas son las opciones de envío para todos los pasos del Canvas. 
- **Construye Canvas:** Este es el recorrido del usuario de Canvas.
{% endtab %}
{% endtabs %}

## Activar el flujo de trabajo de aprobación

Por defecto, la configuración del flujo de trabajo de aprobación está desactivada para Campañas y Lienzos. Para activar esta característica, ve a **Configuración** > **Flujo de trabajo de aprobación** y selecciona el alternador correspondiente:

- **Utiliza el flujo de aprobación para todas las campañas en [tu espacio de trabajo].**
- **Utiliza el flujo de trabajo de aprobación para todos los Lienzos en [tu espacio de trabajo].**

{% alert important %}
La aprobación de campañas no es compatible con las [campañas API]({{site.baseurl}}/api/api_campaigns) ni con [las campañas de correo electrónico transaccional]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Establecer permisos de usuario

Después de activar el flujo de trabajo de aprobación, debes establecer permisos de usuario para que los usuarios de tu empresa puedan aprobar o denegar Campañas y Lienzos. Ambos permisos también pueden aplicarse a Espacios de trabajo o [Equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), o añadirse a un [conjunto de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
Debes tener el [ permiso "Aprobar y denegar campañas".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Este permiso controla quién puede actualizar el estado de aprobación de una campaña. Con este permiso, puedes hacer lo siguiente:

- Autoaprobar la campaña
- Aprobar y lanzar la Campaña
- Aprobar pero no lanzar la campaña (otro usuario con el permiso "Enviar campañas, lienzos" puede lanzar la campaña)
- Ni aprobar ni lanzar la Campaña

Una vez establecidos los estados de aprobación en el paso **Resumen**, cualquier cambio posterior realizado en la campaña restablecerá todos los estados de aprobación cuando se guarde. Esto se aplica a cualquier cambio realizado en un borrador de Campaña o en una campaña posterior a su lanzamiento. Por ejemplo, si sólo realizas cambios en la audiencia objetivo, el paso **Resumen** devuelve los estados de aprobación de todas las secciones al estado predeterminado, **Pendiente de aprobación**.

{% endtab %}

{% tab canvas %}
Debes tener el [ permiso "Aprobar y denegar lienzos".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Este permiso controla quién puede actualizar el estado de aprobación de un Canvas. Con este permiso, puedes hacer lo siguiente:

- Autoaprueba el Canvas
- Aprobar y poner en marcha el lienzo
- Aprobar pero no lanzar el Canvas (otro usuario con el permiso "Enviar campañas, lienzos" puede lanzar el Canvas)
- Ni aprobar ni lanzar el Canvas

Una vez configurados los estados de aprobación en el paso **en** Canvas, cualquier cambio posterior que se realice en el Canvas restablecerá todos los estados de aprobación cuando se guarde. Esto se aplica a cualquier cambio realizado tanto en un borrador de Canvas como en un Canvas posterior al lanzamiento. Por ejemplo, si sólo realizas cambios en la audiencia objetivo, el paso **Resumen** devuelve los estados de aprobación de todas las secciones al estado predeterminado, **Pendiente de aprobación**.

{% alert note %}
**Estado de aprobación y guardado**

- Cuando haces clic en **Aprobar** para una sección en el paso **Resumen**, esa aprobación se guarda inmediatamente.
- El botón **Guardar** guarda los cambios en el contenido y la configuración del Canvas, no el estado de aprobación.

Para evitar perder aprobaciones:

1. Realiza las modificaciones de Canvas que necesites y, a continuación, haz clic en **Guardar**.
2. Cuando el Canvas termine de guardarse, aprueba las secciones pertinentes en el paso **en Resumen**.
3. Vuelve a hacer clic en **Guardar** sólo si realizas cambios adicionales en el Canvas después de la aprobación. Si cambias el Canvas y guardas, todos los estados de aprobación se restablecen a **Pendiente de aprobación**.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Para editar una campaña en vivo, necesitas el permiso "Aprobar y denegar campañas". Un usuario debe aprobar sus cambios porque todavía no está disponible una versión preliminar de Campañas. Este no es el caso de los Lienzos, ya que un usuario puede hacer cambios y guardarlos como borrador, y otro usuario puede aprobar y lanzar el Lienzo.
{% endalert %}