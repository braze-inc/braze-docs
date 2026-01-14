---
nav_title: Crear una plantilla webhook
article_title: Crear una plantilla webhook
page_order: 2
tool:
  - Templates
channel:
  - webhooks
description: "Este artículo de referencia explica cómo crear y personalizar plantillas de webhook para su uso posterior en la plataforma Braze."

---

# Crear una plantilla webhook

> A medida que construyes y personalizas tus webhooks, puedes crear y aprovechar plantillas de webhook para su uso posterior dentro de la plataforma Braze. De esta forma, puedes crear de forma coherente una variedad de webhooks en tus diferentes campañas.

## Paso 1: Ir al editor de plantillas webhook

En el panel de Braze, ve a **Plantillas** > **Plantillas webhook**.

La página "Plantillas de webhook" con plantillas de webhook prediseñadas y guardadas.]({% image_buster /assets/img_archive/webhook_template_campaign.png %})

## Paso 2: Elige tu plantilla

Desde aquí, puedes elegir crear una plantilla nueva, utilizar una de las plantillas de webhook prediseñadas o editar una plantilla existente.

Por ejemplo, si utilizas [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line) como canal de mensajería, puedes configurar varios webhooks utilizando las plantillas prediseñadas para **LINE Carousel** o **LINE Image**.

## Paso 3: Rellena los datos de la plantilla

1. Dale un nombre único a tu plantilla de webhook.
2. (Opcional) Añade una descripción de la plantilla para explicar cómo se va a utilizar esta plantilla.
3. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario para ayudar a encontrar y filtrar tu plantilla.

## Paso 4: Construye tu plantilla

1. Introduce la URL del webhook.
2. Selecciona el método HTTP.
3. Añade un cuerpo de solicitud. Puede ser **un par clave-valor JSON** o un **texto sin formato**.
4. (Opcional) Añade un encabezado de solicitud. Esto puede ser requerido por el destino de tu webhook.

\![La pestaña "Componer" al crear una plantilla de webhook. Los campos disponibles son la URL del webhook, el método HTTP, el cuerpo de la solicitud y los encabezados de solicitud. También puedes añadir idiomas.]({% image_buster /assets/img_archive/Webhook_template_test.png %}){: style="max-width:90%"}

## Paso 5: Prueba tu plantilla

Para ver cómo queda tu webhook antes de enviarlo a tus usuarios, puedes enviar un webhook de prueba utilizando la pestaña **Prueba**. Aquí, puedes seleccionar previsualizar el mensaje como usuario aleatorio, usuario existente o usuario personalizado.

## Paso 6: Guarda tu plantilla

Asegúrate de guardar tu plantilla seleccionando **Guardar plantilla**. Ahora estás listo para utilizar esta plantilla en cualquier campaña que elijas.

{% alert note %}
Las modificaciones realizadas en una plantilla existente no se reflejan en las campañas creadas con versiones anteriores de esa plantilla.
{% endalert %}

## Administrando tus plantillas

Puedes [duplicar y archivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) plantillas de webhook para organizar y gestionar mejor tu lista de plantillas.

Obtén más información sobre cómo crear y administrar plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

