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

Tanto para los lienzos como para las campañas, todos los cambios deben guardarse antes de aprobarlos, aunque sean tus propios cambios. Cada sección del resumen debe ser aprobada por un usuario con los permisos adecuados antes de que el mensaje pueda lanzarse. El estado predeterminado de cada sección es **Pendiente de aprobación**.

{% tabs %}
{% tab campaign %}
Para lanzar una campaña, debes aprobar estos componentes:

- **Mensajes:** Éste es el mensaje de la campaña.
- **Entrega:** Es el tipo de entrega y determina cuándo recibirán los usuarios la campaña.
- **Público objetivo** Esto determina quién recibirá la campaña.
- **Eventos de conversión:** Esta es la métrica que estás siguiendo con fines de interacción y elaboración de informes.
{% endtab %}

{% tab canvas %}
Para lanzar un Canvas, debes aprobar estos componentes clave:

- **Eventos de conversión:** Esta es la métrica que estás siguiendo con fines de interacción y elaboración de informes.
- **Horario de entrada:** Esto incluye el tipo de horario de entrada y cuándo deben entrar los usuarios en el Canvas.
- **Público objetivo** Esto determina quién entrará en este Canvas.
- **Configuración de envío:** Estas son las opciones de envío para todos los pasos del Canvas. 
- **Construye Canvas:** Este es el recorrido del usuario de Canvas.
{% endtab %}
{% endtabs %}

## Activar el flujo de trabajo de aprobación

Por predeterminado, la configuración del flujo de trabajo de aprobación está desactivada para campañas y Lienzos. Para activar esta característica, ve a **Configuración** > **Flujo de trabajo de aprobación** y selecciona el alternador correspondiente:

- **Utiliza el flujo de aprobación para todas las campañas en [tu espacio de trabajo].**
- **Utiliza el flujo de trabajo de aprobación para todos los Lienzos en [tu espacio de trabajo].**

{% alert important %}
La aprobación de campañas no es compatible con las [campañas API]({{site.baseurl}}/api/api_campaigns) ni con [las campañas de correo electrónico transaccional]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Establecer permisos de usuario

Una vez activado el flujo de trabajo de aprobación, tendrás que configurar los permisos de usuario para que los usuarios de tu panel puedan aprobar o denegar las campañas y los lienzos inmediatamente. Ambos permisos también pueden aplicarse a espacios de trabajo o [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), o añadirse a un [conjunto de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
Debes tener el [ permiso "Aprobar y denegar campañas".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Este permiso controla quién puede actualizar el estado de aprobación de una campaña. Con este permiso, puedes hacer lo siguiente:

- Autoaprueba la campaña
- Aprobar y lanzar la campaña
- Aprobar pero no lanzar la campaña (otro usuario con el permiso "Enviar campañas, lienzos" puede lanzar la campaña)
- Ni aprobar ni lanzar la campaña

Una vez establecidos los estados de aprobación en el paso **Resumen**, cualquier cambio posterior realizado en la campaña restablecerá todos los estados de aprobación cuando se guarde. Esto se aplica a cualquier cambio realizado en un borrador de campaña o en una campaña posterior al lanzamiento. Por ejemplo, si sólo realiza cambios en el público objetivo, el paso **Resumen** revertirá los estados de aprobación de todas las secciones al estado predeterminado, pendiente.

{% endtab %}

{% tab canvas %}
Debes tener el [ permiso "Aprobar y denegar lienzos".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Este permiso controla quién puede actualizar el estado de aprobación de un Canvas. Con este permiso, puedes hacer lo siguiente:

- Autoaprueba el Canvas
- Aprobar y poner en marcha el lienzo
- Aprobar pero no lanzar el Canvas (otro usuario con el permiso "Enviar campañas, lienzos" puede lanzar el Canvas)
- Ni aprobar ni lanzar el Canvas

Una vez establecidos los estados de aprobación en el paso **en** Canvas, cualquier cambio posterior que se realice en el Canvas restablecerá todos los estados de aprobación cuando se guarde. Esto se aplica a cualquier cambio realizado tanto en un borrador de Canvas como en un Canvas posterior al lanzamiento. Por ejemplo, si sólo realiza cambios en el público objetivo, el paso **Resumen** revertirá los estados de aprobación de todas las secciones al estado predeterminado, pendiente. Ten en cuenta que si el Canvas ya estaba aprobado, pero lo vuelves a guardar, las aprobaciones se revertirán aunque no se hayan realizado cambios.
{% endtab %}
{% endtabs %}

{% alert important %}
Para editar una campaña en directo, necesitará el permiso "Aprobar y denegar campañas". El usuario deberá aprobar sus cambios, ya que aún no se dispone de una versión preliminar de las campañas. Este no es el caso de los Lienzos, ya que un usuario puede hacer cambios y guardarlos como borrador, y otro usuario puede aprobar y lanzar el Lienzo.
{% endalert %}
