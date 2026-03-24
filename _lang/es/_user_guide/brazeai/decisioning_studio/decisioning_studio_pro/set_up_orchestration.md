---
nav_title: Configurar la orquestación
article_title: Configurar la orquestación
page_order: 2
description: "Aprende a configurar la orquestación para los agentes de Decisioning Studio Pro con el fin de habilitar la personalización de las comunicaciones."
toc_headers: h2
---

# Configurar la orquestación

> Los agentes encargados de la toma de decisiones deben conectarse a una plataforma de interacción con los clientes (CEP) para realizar la orquestación de las comunicaciones una vez que hayan recopilado los datos de los clientes y los hayan personalizado a nivel individual. Este artículo explica cómo configurar la integración para cada CEP compatible.

## CEP compatibles

Decisioning Studio Pro es compatible con las siguientes plataformas de interacción con los clientes:

| CEP | Tipo de integración | Complejidad de la configuración |
|-----|-----------------|------------------|
| **Braze** | Integración con API nativa | Bajo (recomendado) |
| **Salesforce Marketing Cloud** | Eventos API nativos + Recorridos | Media |
| **Klaviyo** | Eventos API nativos + Flujos | Media |
| **Otros CEP** | Personalizado (archivo de recomendaciones) | Alta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Selecciona tu CEP a continuación para comenzar con la configuración de la integración.

{% tabs %}
{% tab Braze %}

## Configuración de la integración con Braze

Sigue estos pasos para realizar la integración de un agente de Braze Decisioning Studio con las capacidades de orquestación de Braze (el equipo de servicios de Braze estará disponible para ayudarte):

### Paso 1: Crear una clave de API

Ve a **Configuración** > **Claves de API** y crea una nueva clave con los siguientes permisos:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Paso 2: Configurar campañas activadas por API

Configura una campaña activada por API para cada plantilla base con propiedades de activación de API para todas las dimensiones optimizadas.

Una plantilla base es cualquier plantilla que el agente de decisión puede utilizar para la orquestación de mensajes. Un agente de toma de decisiones puede tener una o varias plantillas base, en cuyo caso elegir la plantilla base adecuada para cada cliente será una de las decisiones que el agente realizará mediante personalización.

### Paso 3: Configurar la reelegibilidad

Asegúrate de que todas las campañas desencadenadas por API permitan a los usuarios volver a ser elegibles en un plazo de 15 minutos.

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Aunque el agente de Decisioning Studio nunca enviará la misma campaña más de una vez al día, es posible que desees tener la posibilidad de enviar las mismas campañas varias veces al día con fines de prueba.
{% endalert %}

### Paso 4: Añadir marcadores de posición dinámicos

Estos sirven como marcadores de posición dinámicos para las decisiones que el agente de Decisioning Studio está optimizando.

#### Ejemplo 1: Campaña de correo electrónico

Supongamos que el agente de Decisioning Studio está optimizando una campaña de correo electrónico. Esto se podría configurar así:

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Suponiendo que el agente está optimizando la elección de plantillas y el mensaje de llamada a la acción (CTA), entonces se debe crear una campaña activada por API para cada plantilla, y la sección CTA de una plantilla podría tener el siguiente aspecto:

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Ejemplo 2: Campaña de promoción

Supongamos que un agente de Decisioning Studio está optimizando el mensaje de una campaña Push. Esto se podría configurar así:

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

Lo que da como resultado el siguiente mensaje:

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Ejemplo 3: Campaña de SMS

Supongamos que el agente de Decisioning Studio está optimizando los campos de una campaña de SMS. Esto se podría configurar así:

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

Lo que da como resultado el siguiente mensaje:

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configuración de la integración con SFMC

Decisioning Studio Pro es compatible con la integración nativa con Salesforce Marketing Cloud. Decisioning Studio desencadena eventos API en un recorrido con los datos necesarios para rellenar elementos dinámicos.

La configuración de la orquestación para SFMC es similar tanto para Decisioning Studio Pro como para Decisioning Studio Go. Para obtener información detallada sobre cómo configurar la integración de SFMC, sigue las [instrucciones de SFMC]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) que se incluyen en la documentación de Decisioning Studio Go.

{% endtab %}
{% tab Klaviyo %}

## Configuración de la integración con Klaviyo

Decisioning Studio Pro es compatible con la integración nativa con Klaviyo. Decisioning Studio desencadena eventos API en un flujo con los datos necesarios para rellenar elementos dinámicos.

La configuración de la orquestación para Klaviyo es similar tanto para Decisioning Studio Pro como para Decisioning Studio Go. Para obtener información detallada sobre cómo configurar la integración de Klaviyo, sigue las [instrucciones de Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) que se incluyen en la documentación de Decisioning Studio Go.

{% endtab %}
{% tab Other CEPs %}

## Configuración de otras integraciones CEP

Decisioning Studio se puede integrar con cualquier plataforma de interacción con los clientes. Sin embargo, esto puede requerir cierto trabajo de ingeniería personalizado por parte de tu equipo, ya que Decisioning Studio no puede desencadenar las comunicaciones directamente.

En este caso, el agente entregará un «archivo de recomendaciones». Este archivo contiene filas para cada cliente, con columnas que indican todas las decisiones de personalización para ese cliente.

Por ejemplo, el siguiente archivo de recomendaciones:

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Se puede utilizar para optimizar una campaña de envío por correo electrónico como la siguiente:

![Diagrama de toma de decisiones Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Próximos pasos

Después de configurar la orquestación, procede a diseñar tu agente:

- [Diseña tu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

