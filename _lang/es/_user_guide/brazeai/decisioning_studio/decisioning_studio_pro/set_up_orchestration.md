---
nav_title: Configurar la orquestación
article_title: Configurar la orquestación
page_order: 2
description: "Aprende a configurar la orquestación para que los agentes de Decisioning Studio Pro habiliten comunicaciones personalizadas."
toc_headers: h2
---

# Configurar la orquestación

> Los agentes decisores necesitan conectarse a una plataforma de interacción con los clientes (CEP) para orquestar las comunicaciones una vez que han ingerido los datos de los clientes y las han personalizado a un nivel 1:1. Este artículo explica cómo configurar la integración para cada CEP compatible.

## PEC apoyados

Decisioning Studio Pro es compatible con las siguientes plataformas de interacción con los clientes:

| CEP | Tipo de integración | Complejidad de la instalación |
|-----|-----------------|------------------|
| **Braze** | Integración API nativa | Bajo (recomendado) |
| **Salesforce Marketing Cloud** | Eventos API nativos + Viajes | Media |
| **Klaviyo** | Eventos nativos de la API + Flujos | Media |
| **Otros PEC** | Personalizado (archivo de recomendación) | Alta |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Selecciona tu CEP a continuación para empezar a configurar la integración.

{% tabs %}
{% tab Braze %}

## Configuración de la integración Braze

Sigue estos pasos para integrar un agente Braze Decisioning Studio con las capacidades de orquestación de Braze (el equipo de servicios de Braze estará disponible para ayudarte):

### Paso 1: Crear una clave de API

Ve a **Configuración** > **Claves de API** y, a continuación, crea una nueva clave con los siguientes permisos:

{% multi_lang_include decisioning_studio/api_key_permissions.md %}

### Paso 2: Configura campañas desencadenadas por la API

Configura una campaña desencadenada por la API para cada plantilla base con propiedades de desencadenamiento de la API para todas las dimensiones optimizadas.

Una plantilla base es cualquier plantilla que el Agente de Decisión pueda utilizar para la orquestación de mensajes. Un Agente Decisor puede tener 1 plantilla base o varias, en cuyo caso elegir la plantilla base adecuada para cada cliente será una de las decisiones que el agente personalice.

### Paso 3: Configurar la readmisibilidad

Asegúrate de que todas las campañas desencadenadas por la API permitan a los usuarios volver a ser elegibles en 15 minutos.

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_frequency_cap.png %})

{% alert note %}
Aunque el agente de Decisioning Studio nunca enviará la misma campaña más de una vez al día, querrás tener la posibilidad de enviar las mismas campañas varias veces en un día con fines de prueba.
{% endalert %}

### Paso 4: Añadir marcadores de posición dinámicos

Sirven como marcadores de posición dinámicos para las decisiones que el agente de Decisioning Studio está optimizando.

#### Ejemplo 1: Campaña de correo electrónico

Supongamos que el agente Decisioning Studio está optimizando una campaña de correo electrónico. Esto podría configurarse así:

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_email_example_1.png %})

Suponiendo que el agente esté optimizando la elección de plantillas y mensajes de Llamada a la Acción (CTA), entonces debería crearse una campaña desencadenada por API para cada plantilla, y la sección CTA de una plantilla podría tener este aspecto:

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_braze_email_example_2.png %})

#### Ejemplo 2: Campaña push

Supongamos que un agente de Decisioning Studio está optimizando el mensaje de una campaña push. Esto podría configurarse así:

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_1.png %})

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_2.png %})

El resultado es el siguiente mensaje:

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_push_example_3.png %})

#### Ejemplo 3: Campaña de SMS

Supongamos que el agente de Decisioning Studio está optimizando los campos de una campaña de SMS. Esto podría configurarse así:

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_1.png %})

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_2.png %})

El resultado es el siguiente mensaje:

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_sms_example_3.png %})

{% endtab %}
{% tab Salesforce Marketing Cloud %}

## Configuración de la integración SFMC

Decisioning Studio Pro admite la integración nativa con Salesforce Marketing Cloud. Decisioning Studio desencadena eventos API en un viaje con los datos necesarios para rellenar los elementos dinámicos.

La configuración de la orquestación para SFMC es similar tanto para Decisioning Studio Pro como para Decisioning Studio Go. Para conocer los pasos detallados para configurar la integración de SFMC, sigue las [instrucciones de SFMC]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) en la documentación de Decisioning Studio Go.

{% endtab %}
{% tab Klaviyo %}

## Configuración de la integración de Klaviyo

Decisioning Studio Pro admite la integración nativa con Klaviyo. Decisioning Studio desencadena eventos API en un flujo con los datos necesarios para rellenar los elementos dinámicos.

La configuración de la orquestación para Klaviyo es similar tanto para Decisioning Studio Pro como para Decisioning Studio Go. Para conocer los pasos detallados para configurar la integración de Klaviyo, sigue las [instrucciones de Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/) en la documentación de Decisioning Studio Go.

{% endtab %}
{% tab Other CEPs %}

## Configuración de otras integraciones CEP

Decisioning Studio puede integrarse con cualquier plataforma de interacción con los clientes. Sin embargo, esto puede requerir algún trabajo de ingeniería personalizado por parte de tu equipo, ya que Decisioning Studio no puede desencadenar las comunicaciones directamente.

En este caso, el agente entregará un "archivo de recomendación". Este archivo contiene filas para cada cliente, con columnas que indican todas las decisiones personalizadas para ese cliente.

Por ejemplo, el siguiente archivo de recomendación:

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_2.png %})

Puede utilizarse para optimizar una campaña de correo electrónico que tenga el siguiente aspecto:

![Diagrama Decision Pro]({% image_buster /assets/img/decisioning_studio/decisioning_studio_custom_example_1.png %})

{% endtab %}
{% endtabs %}

## Próximos pasos

Tras configurar la orquestación, procede a diseñar tu agente:

- [Diseña tu agente]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/design_your_agent/)

