---
nav_title: Octubre
page_order: 4
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de octubre de 2018."
---
# Octubre de 2018

{% comment %}
  Añádelos más adelante...
  Alternar grupo de control de Intelligent Selection
  El cuadro Selección Inteligente tiene ahora una casilla de verificación que te permite [alternar entre activar o desactivar el uso de un grupo de control]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#including-a-control-group). Cuando esté activado, el grupo de control será el 20% del tamaño de la audiencia y cambiará a medida que la característica Intelligent Selection optimice los tamaños de audiencia por variante.
  Asistente de configuración de entrada en Canvas (Beta)
  La interfaz de usuario de Canvas se simplificará para evitar la omisión de tareas y los errores resultantes. Las configuraciones de Canvas, en concreto, se mostrarán ahora en un asistente, similar al diseño del asistente de campañas. Esto no se refleja actualmente en nuestra documentación, ya que se está implementando gradualmente. ¡Vuelve pronto para saber más sobre esto!
  API de grupo de suscripción (oculta)
  Braze ha puesto a tu disposición una nueva llamada GET para habilitar la solicitud basada en un ID externo o en una dirección de correo electrónico. A continuación, se te proporcionarán todos los grupos de suscripción asociados a ese usuario.
{% endcomment %}

## Calcula las estadísticas exactas de audiencia de las campañas

Ahora puedes ir a **Análisis de campaña** y calcular las estadísticas exactas de tu audiencia. Haz clic en **Calcular estadísticas exactas** en el pie de página de la sección **Audiencias objetivo**, y aparecerán las estadísticas exactas de la audiencia. Tendrás que guardar la campaña antes de calcularla (los borradores de campaña se guardarán como borradores).

## Windows 8 obsoleto

Braze ya no es compatible con Windows 8 desde el 10 de octubre de 2018.

## Centro de asociaciones

Ahora puedes encontrar una lista de tus integraciones en la plataforma Braze, en **Integraciones**, junto con las claves de integración y las instrucciones.

## Cálculos de análisis de correo electrónico

Braze calcula ahora todos los análisis de correo electrónico utilizando los datos de eventos de nuestro socio de envío por correo electrónico (ESP) para mejorar enormemente la precisión de nuestros análisis de correo electrónico. Esta solución utiliza Postgres, una solución de base de datos de código abierto, para garantizar la integridad de los datos.

{% alert important %}
Actualmente, las Aperturas Únicas y los Clics Únicos siguen dependiendo de los datos agregados proporcionados por nuestros socios de envío por correo electrónico. Se está trabajando para calcular estas estadísticas de unicidad utilizando la misma infraestructura introducida en esta versión.
{% endalert %}

## Controles del panel de creación

Se han renovado los controles del Creador de mensajes para incluir texto asociado a los iconos, a fin de habilitar una mejor usabilidad y navegación.

## Azure para Currents

Los clientes de Braze que utilicen Currents pueden ver ahora [Azure]({{site.baseurl}}/partners/data_and_infrastructure_agility/cloud_storage/microsoft_azure_blob_storage_for_currents#microsoft-azure-blob-storage) como una integración potencial.

## Ampliaciones del campo de entrada

Ahora puedes ampliar los cuadros de entrada para las líneas del asunto del correo electrónico y los títulos push.
