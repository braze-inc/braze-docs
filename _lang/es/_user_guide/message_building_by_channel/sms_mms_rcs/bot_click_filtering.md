---
nav_title: "Bot clic filtrar"
article_title: "Filtrado de clics de SMS y RCS Bot"
description: "Este artículo de referencia cubre el filtrado de clics de bots SMS y RCS."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 11
channel:
  - SMS
  - RCS
---

# Filtrado de clics de bots SMS y RCS

> Filtrar los clics de bots de SMS y RCS mejora el análisis y los flujos de trabajo de las campañas al excluir los clics sospechosos de bots. Un "clic de bot" se refiere a los clics automatizados en enlaces acortados en mensajes SMS y RCS, como los de rastreadores web, previsualizaciones de enlaces de Android e iOS o software de seguridad CPaaS. Esta característica facilita la elaboración de informes precisos, la segmentación y la orquestación para captar usuarios reales. <br><br> Para filtrar los clics de bots de campañas de correo electrónico, consulta [Filtrado de bots para correos electrónicos]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/bot_filtering/).

## Cómo funciona

Braze tiene un sistema de detección propio que utiliza múltiples entradas para identificar presuntos clics de bots, también conocidos como interacciones no humanas (NHI). Los clics de los bots pueden inflar las tasas de clics, sesgando las métricas de interacción. Al filtrarlos, Braze facilita la obtención de datos fiables para la toma de decisiones.

Nuestro sistema analiza los agentes de usuario asociados a rastreadores Web, vistas previas de enlaces de Android e iOS, o software de seguridad CPaaS. Algunos ejemplos de agentes de usuario filtrados son `GoogleBot`, `python-requests/2.32.3` y `Barracuda Sentinel (EE)`.

## Métricas y flujos de trabajo afectados

Las siguientes métricas y flujos de trabajo de Braze se ven afectados por los clics de los robots:

- **_Clics totales_:** Los análisis de campaña y los análisis de Canvas excluirán los clics de bots, reflejando sólo las interacciones humanas.
- **Filtros de segmentación:** Los filtros de segmento que hacen referencia a las interacciones con enlaces SMS excluirán los clics de bots para reorientar con más precisión las campañas y los Canvases.
- **Orquestación:** Los clics de los robots se filtran de los desencadenantes basados en acciones y de las rutas de acción de Canvas que hacen referencia a interacciones de enlaces SMS, lo que permite que los desencadenantes reflejen el comportamiento humano.
- **Inteligencia Braze:**
    - **Intelligent Selection:** Excluye los clics de los robots al optimizar la selección de variantes.
    - **Canal inteligente:** Excluye los clics de bots cuando se selecciona SMS o RCS para una selección precisa del canal.
    - **Pasos del experimento:** Excluye los clics de los robots para obtener resultados fiables del experimento.
    - **Exportación de datos de Currents:** Incluye los campos `is_suspected_bot_click` y `suspected_bot_click_reason` para ayudar a analizar los clics humanos frente a los de los robots. Estos campos están disponibles en [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), [Compartir datos de Snowflake]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) y [Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/).

Las cancelaciones de suscripción por presuntos clics de bots no se ven afectadas. Braze procesa todas las solicitudes de cancelar suscripción como de costumbre. Para bloquear estas cancelaciones de suscripción, [envía comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Currents campos en eventos de clic de SMS

Braze incluye los siguientes campos Currents para eventos de clic de SMS:

| Campo | Tipo de datos | Descripción |
| --- | --- | --- |
| `is_suspected_bot_click` | Booleano | Indica si el clic es un presunto clic de bot. Vuelve a `null` para todos los usuarios hasta que se habilite el filtrado de clics de bot para tu empresa. Cuando se habilite, se rellenará con `true` o `false` para todos los nuevos clics en adelante. |
| `suspected_bot_click_reason` | Cadena, matriz | Indica el motivo de un presunto clic de bot (como `user_agent`). Se rellena incluso si el filtrado está desactivado, proporcionando información sobre posibles actividades de bots. Este campo está disponible globalmente y se rellena con un motivo para todos los usuarios, aunque el filtrado de clics de bot no esté habilitado todavía. Esto proporciona información sobre la posible actividad de los bots antes de habilitar el filtrado de clics de bots. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Plantilla del Generador de consultas

Si necesitas ayuda para analizar tus datos, puedes utilizar la plantilla móvil prediseñada **Eventos de clics de SMS por bots** en [el Generador de consultas]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/).

## Preguntas más frecuentes

### ¿Cómo influye el filtrado de clics del bot en el rendimiento de la campaña?

Filtrar no afecta a las campañas enviadas anteriormente. Cuando se habilita, reduce la tasa de clics a partir de ese momento al excluir los clics de bots.

### ¿El filtrado de clics de bots impide que los bots hagan clic en los enlaces de cancelar suscripción?

No. Todas las solicitudes de cancelar suscripción se procesan como de costumbre.

### ¿Se incluyen las vistas previas de los enlaces en el filtrado de clics del bot?

Sí. Las vistas previas de enlaces (como las vistas previas de enlaces de Android e iOS) se marcan como clics de bots y se filtran.

### ¿Cómo habilito el filtrado de clics de bot?

Debes ponerte en contacto con el equipo de tu cuenta Braze para habilitar el filtrado de clics de bot durante el acceso anticipado. Cuando el filtrado de clics de bot tenga disponibilidad general, la característica estará activada por predeterminado para todos los usuarios de SMS y RCS.

Asegúrate también de haber habilitado el seguimiento avanzado de clics para [acortar enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/). Esto te permite recibir el análisis de clics del bot, ya que hacemos un seguimiento de estos datos a nivel de usuario individual. 

{% alert note %}
Si necesitas más ayuda, [ponte en contacto con el Servicio de Asistencia]({{site.baseurl}}/braze_support/).
{% endalert %}