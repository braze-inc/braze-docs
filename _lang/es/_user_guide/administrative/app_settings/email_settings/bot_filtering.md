---
nav_title: Filtrado de bots para correos electrónicos
article_title: Filtrado de bots para correos electrónicos
page_type: reference
page_order: 1
toc_headers: h2
alias: "/bot_filtering/"
description: "Este artículo ofrece un resumen del filtrado de bots para el correo electrónico."
---

# Bot para filtrar correos electrónicos

> Configura el filtrado de bots en tus [Preferencias de correo electrónico]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) para excluir todos los clics sospechosos de máquina o bot. Un "clic de bot" en correo electrónico se refiere a un clic en hipervínculos dentro de un correo electrónico generado por un programa automatizado. Al filtrar estos clics de bot, puedes desencadenar y entregar mensajes intencionadamente a destinatarios que estén interactuando.

{% alert important %}
A partir del 9 de julio de 2025, todos los espacios de trabajo nuevos que se creen tendrán activada la configuración de filtrar bots para obtener informes de clics más precisos en Braze.
{% endalert %}

## Sobre los clics de los robots

Braze tiene un sistema de detección que emplea múltiples entradas para identificar presuntos clics de bots, también denominados interacciones no humanas (NHI). Los clics de los bots pueden distorsionar tus métricas de interacción por correo electrónico inflando artificialmente las tasas de clics. Este enfoque nos permite diferenciar entre las interacciones humanas auténticas y la actividad sospechosa de los bots, para mantener la integridad de las métricas y la información sobre la interacción de los clics.

## Métricas afectadas por los clics de los robots

Las siguientes métricas de Braze pueden verse afectadas por los clics de los robots:

- Tasa de clics totales
- Tasa de clics únicos
- Tasa de clics de apertura
- Tasa de conversión (si se selecciona "Campaña de clics" como evento de conversión)
- Mapa de calor
- Algunos filtros de segmento

[Las características de Braze Intelligence]({{site.baseurl}}/user_guide/brazeai/intelligence) que aprovechan los datos de los clics sobre nuestros sistemas de detección pueden verse afectadas. Activar la configuración tiene el potencial de perturbar temporalmente nuestros sistemas de detección, lo que puede dar lugar a una disminución de la métrica o de la entrada debido a esta exclusión de los clics sospechosos de ser bots:

- Intelligent Selection
- Canal inteligente
- Intelligent Timing
- Paso del experimento
    - Recorrido ganador
    - Recorrido personalizado
- Campaña
    - Variante ganadora
    - Variante personalizada
- Estimación de la tarifa abierta real

Las cancelaciones de suscripción por presuntos clics de bots no se verán afectadas. Braze seguirá procesando todas las solicitudes de cancelar suscripción como de costumbre. Si quieres que Braze bloquee estas cancelaciones de suscripción, envía [tus comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal).

## Filtros de segmentación afectados por el filtrado de bots

Los siguientes [filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) pueden verse afectados por el filtrado de bots para mensajes de correo electrónico:

- [Campaña o Canvas que se abrió o en la que se hizo clic con etiqueta]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-campaign-or-canvas-with-tag)
- [Paso que se abrió o en el que se hizo clic]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-opened-step)
- [Alias al que se hizo clic en la campaña]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-campaign)
- [Alias en que se hizo clic en paso en Canvas]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-canvas-step)
- [Alias con clic en cualquier paso de campaña o lienzo]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#clicked-alias-in-any-campaign-or-canvas-step)
- [Última interacción con un mensaje]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#last-engaged-with-message)
- [Canal inteligente]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#intelligent-channel)

## Activar el filtrado de bots

Vaya a **Configuración** > **Preferencias de correo electrónico**. A continuación, selecciona **Eliminar clics de bot**. Esta configuración se aplica a nivel de espacio de trabajo.

Los presuntos clics de bots sólo se eliminarán una vez activada la configuración, y no se aplica retroactivamente a las métricas de tu espacio de trabajo.

![Configuración de filtrar correo electrónico activada en Preferencias de correo electrónico.]({% image_buster /assets/img/bot_tracking_email.png %})

{% alert important %}
Si activas esta configuración y luego la desactivas, Braze no podrá restaurar en tus análisis ninguna actividad bot eliminada previamente.
{% endalert %}

## Campos en los eventos de clic de correo electrónico para Currents y Snowflake

Braze enviará los campos `is_suspected_bot_click` y `suspected_bot_click_reason` en Currents y Snowflake para un evento de clic de correo electrónico.

| Campo Tipo de datos Descripción
| `is_suspected_bot_click` | Booleano | Indica que se trata de un presunto clic de bot. Esto se enviará como valores nulos hasta que actives la configuración **Eliminar bots hace clic en** el espacio de trabajo. Este enfoque te permite comprender programáticamente cuándo se ha iniciado el filtrado de los clics de bot sospechosos en tu espacio de trabajo, de forma que puedas compararlo con precisión con los datos de Currents y Snowflake. |
| `suspected_bot_click_reason` | Array | Indica la razón por la que se sospecha que es un clic de bot. Se rellenará con valores, como `user_agent` y `ip_address`, aunque la configuración del espacio de trabajo para filtrar bots esté desactivada. Este campo puede proporcionar información sobre el impacto potencial de activar esta configuración, comparando el número de clics derivados de presuntos clics de bots con las interacciones humanas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Preguntas más frecuentes

### ¿Cómo afectará el filtrado de bots al rendimiento de mi campaña?

Esto no afectará a las métricas de ninguna campaña anterior ya enviada. Cuando el filtrado de bots esté activado en tu espacio de trabajo, Braze empezará a filtrar los clics sospechosos de bots de entre todos los clics. Puede que notes un descenso en las tasas de clics, pero la tasa de clics es una representación más precisa de la interacción de tus usuarios con sus mensajes de correo electrónico.

### ¿El filtrado de bots evitará que los bots que hagan clic en el enlace de cancelar suscripción de Braze se den de baja?

No. Se seguirán procesando todas las solicitudes de cancelar suscripción.

### ¿Se tienen en cuenta las aperturas de máquina en el filtrado de clics del bot?

No.
