---
nav_title: Diciembre
page_order: 0
noindex: true
page_type: update
description: "Este artículo contiene notas de la versión de diciembre de 2021."
alias: "/help/release_notes/2022/january/"
---
# Diciembre de 2021

## Actualización para exportar usuarios por punto final de segmento

A partir de diciembre de 2021, entrarán en vigor los siguientes cambios para el [punto final Exportar usuarios por segmento]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/):

1. El campo `fields_to_export` de esta solicitud API será obligatorio. Se eliminará la opción de predeterminar todos los campos.
2. Los campos de `custom_events`, `purchases`, `campaigns_received`, y `canvases_received` sólo contendrán datos de los últimos 90 días.

## Nuevas propiedades para los eventos de interacción de mensajes Currents

Se han añadido nuevas propiedades para seleccionar [eventos de interacción de mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). Esta actualización se aplica a los siguientes eventos de interacción de mensajes de Currents y a todos los socios que los utilizan:

- Añade `LINK_ID`, `LINK_ALIAS` a:
  - Clic en correo electrónico (todos los destinos)
- Añade `USER_AGENT` a:
  - Apertura del correo electrónico
  - Clic en correo electrónico
  - Correo electrónico Marcar como spam
- Añade `MACHINE_OPEN` a:
  - Apertura del correo electrónico

## Nueva etiqueta de personalización de Liquid

Ahora podemos dirigirnos a los usuarios que tienen habilitada la función push en primer plano en su dispositivo con las siguientes etiquetas de Liquid:

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targeted_device.${foreground_push_enabled}}}`
{% endraw %}

Para más información, consulta [Etiquetas de personalización compatibles]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

## Acerca de los webhooks

Los webhooks son herramientas potentes y flexibles, pero pueden resultar un poco confusas. Si te preguntas qué son los webhooks y cómo puedes utilizarlos en Braze, consulta nuestro nuevo artículo sobre [Acerca de los webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/).

## Amazon Personalize

Amazon Personalize es como tener tu propio sistema de recomendación de aprendizaje automático de Amazon durante todo el día. Basándose en más de 20 años de experiencia en recomendaciones, Amazon Personalize te habilita para mejorar la interacción con los clientes mediante recomendaciones de productos y contenidos personalizadas en tiempo real y promociones de marketing específicas. 

Si quieres saber más, visita nuestro nuevo artículo sobre [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalized_recommendations/amazon_personalize) para comprender los casos de uso que ofrece Amazon Personalize, los datos con los que funciona, cómo configurar el servicio y cómo integrarlo con Braze.

## Nuevas asociaciones Braze

### Yotpo - Comercio electrónico

La integración de [Yotpo]({{site.baseurl}}/partners/message_personalization/dynamic_content/visual_and_interactive_content/yotpo/) y Braze te permite extraer y mostrar dinámicamente valoraciones con estrellas, las mejores opiniones y contenido visual generado por usuarios sobre productos en correos electrónicos y otros canales de comunicación dentro de Braze. También puedes incluir datos de fidelización a nivel de cliente en correos electrónicos y otros métodos de comunicación para crear una interacción más personalizada, impulsando las ventas y la fidelización.

### Zeotap - Plataforma de datos de los clientes

Con la integración de [Zeotap]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/zeotap/) y Braze, puedes ampliar la escala y el alcance de tus campañas sincronizando los segmentos de clientes de Zeotap para mapear los datos de usuario de Zeotap con las cuentas de usuario de Braze. A continuación, puedes actuar a partir de estos datos, entregando experiencias de destino personalizadas a tus usuarios.