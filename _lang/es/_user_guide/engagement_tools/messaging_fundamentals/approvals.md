---
nav_title: Homologaciones
article_title: Homologaciones
page_order: 2
page_type: reference
description: "Este artículo de referencia ofrece un resumen de los distintos estados que pueden tener una campaña y Canvas y lo que significan."
tool:
    - Campaigns
    - Canvas
---

# Aprobación de campañas y lonas

> El proceso de aprobación de campañas y Lienzos añade un proceso de revisión a tu flujo de trabajo antes del lanzamiento. De esta forma, puedes comprobar que cada sección del editor final de la campaña o Canvas está aprobada para poder lanzarla.

## Cómo funciona

Puedes revisar los detalles de tu campaña o Canvas en el último paso de tu editor. Para las campañas, es **Resumen de la revisión**, y para los Lienzos, es **Resumen**. 

Si tu administrador ha activado el flujo de trabajo de aprobación, cada sección del resumen debe ser aprobada por un usuario con los permisos adecuados antes de que el mensaje pueda lanzarse. El estado predeterminado de cada sección es **Pendiente de aprobación**.

{% tabs %}
{% tab campaign %}
Para lanzar una campaña, debes aprobar estos componentes clave:

- **Mensajes:** Éste es el mensaje de la campaña.
- **Entrega:** Es el tipo de entrega y determina cuándo recibirán los usuarios la campaña.
- **Audiencia objetivo:** Esto determina quién recibirá la campaña.
- **Eventos de conversión:** Esta es la métrica que estás siguiendo con fines de interacción y elaboración de informes.
{% endtab %}

{% tab canvas %}
Para lanzar un Canvas, debes aprobar estos componentes clave:

- **Eventos de conversión:** Esta es la métrica que estás siguiendo con fines de interacción y elaboración de informes.
- **Horario de entrada:** Esto incluye el tipo de horario de entrada y cuándo deben entrar los usuarios en el Canvas.
- **Audiencia objetivo:** Esto determina quién entrará en este Canvas.
- **Configuración de envío:** Estas son las opciones de envío para todos los pasos del Canvas. 
- **Construye Canvas:** Este es el recorrido del usuario de Canvas.
{% endtab %}
{% endtabs %}

## Activar el flujo de trabajo de aprobación

Por defecto, la configuración del flujo de trabajo de aprobación está desactivada para las campañas y los Lienzos. Para activar esta característica, ve a **Configuración** > **Flujo de trabajo de aprobación** y selecciona el alternador correspondiente:
- **Utiliza el flujo de aprobación para todas las campañas en [tu espacio de trabajo].**
- **Utiliza el flujo de trabajo de aprobación para todos los Lienzos en [tu espacio de trabajo].**

{% alert important %}
La aprobación de campañas no es compatible con el flujo de trabajo de creación de [campañas API]({{site.baseurl}}/api/api_campaigns) y [campañas de correo electrónico transaccional]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign).
{% endalert %}

## Configuración de permisos de usuario

Una vez activado el flujo de trabajo de aprobación, tendrás que configurar los permisos de usuario para que los usuarios de tu panel puedan aprobar o denegar las campañas y los lienzos inmediatamente. Ambos permisos también pueden aplicarse a espacios de trabajo o [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), o añadirse a un [conjunto de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets).

{% tabs %}
{% tab campaign %}
Debes tener el [ permiso "Aprobar y denegar campañas".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Este permiso controla quién puede actualizar el estado de aprobación de una campaña. Es posible autoaprobar componentes de una campaña.
{% endtab %}

{% tab canvas %}
Debes tener el [ permiso "Aprobar y denegar lienzos".]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) Un usuario con este permiso puede realizar cualquiera de las siguientes acciones en el flujo de trabajo Canvas:

- Aprobar pero no lanzar el Canvas
- Iniciar pero no aprobar el Canvas
- Aprueba y lanza el Canvas
- Ni aprobar ni lanzar el Canvas

Una vez establecidos los estados de aprobación en el paso **en** Canvas, cualquier cambio posterior que se realice en el Canvas restablecerá todos los estados de aprobación cuando se guarde. Esto se aplica a cualquier cambio realizado en un borrador de Canvas o en un Canvas posterior al lanzamiento. Por ejemplo, si sólo realizas cambios en la audiencia objetivo, el paso **Resumen** revertirá los estados de aprobación de todas las secciones al estado predeterminado, pendiente.
{% endtab %}
{% endtabs %}

{% alert important %}
Para editar una campaña en vivo, necesitarás el permiso "Aprobar y denegar campañas". Un usuario tendrá que aprobar sus cambios, ya que todavía no está disponible una versión preliminar de las campañas. Este no es el caso de los Canvas, ya que un usuario puede hacer cambios y guardarlos como borrador, y otro usuario puede aprobar y lanzar el Canvas.
{% endalert %}
