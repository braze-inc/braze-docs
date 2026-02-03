---
nav_title: Configurar con Braze
article_title: Configurar con Braze
page_order: 1
description: "Aprende a configurar e integrar BrazeAI Decisioning <sup>StudioTM</sup> Go en Braze."
---

# Configurar con Braze

> Crea una campaña API en Braze diseñada para BrazeAI Decisioning Studio™ Go.

## Paso 1: Crea tu campaña 

1. En el panel de Braze, ve a **Mensajería** > Campañas.
2. Selecciona **Crear campaña**.
3. Para tu tipo de campaña, selecciona **Campaña API**.
4. Escribe un nombre para tu campaña. Un ejemplo es "Decisioning Studio Go Email".

![Una campaña API llamada "Decisioning Studio Go Email".]({% image_buster /assets/img/decisioning_studio_go/api_campaign_name.png %})

{: start="5"}
5\. Para tu canal de mensajería, selecciona **Correo electrónico**.

![Opción para seleccionar tu canal de mensajería para la campaña de API.]({% image_buster /assets/img/decisioning_studio_go/select_api_campaign.png %})

{: start="6"}
6\. En **Opciones adicionales**, selecciona la casilla **Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña**.
7\. Para el tiempo para volver a ser elegible, introduce **1** y selecciona **Horas** en el desplegable.

![Reelegibilidad para la campaña API seleccionada.]({% image_buster /assets/img/decisioning_studio_go/additional_options.png %})

{: start="8"}
8\. Selecciona **Guardar campaña**.

## Paso 2: Copia y pega el ID de tu campaña

En tu campaña API, copia el **ID de la campaña**. A continuación, ve al portal BrazeAI Decisioning Studio™ Go y pega el **ID de la campaña**.

![Un ejemplo de ID de variación de mensaje para copiar y pegar.]({% image_buster /assets/img/decisioning_studio_go/campaign_id.png %})

## Paso 3: Copia y pega tu ID de variación del mensaje

En tu campaña API, copia el **ID de variación del mensaje**. A continuación, ve al portal BrazeAI Decisioning Studio™ Go y pega el **ID de variación del mensaje**.
