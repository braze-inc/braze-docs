---
nav_title: The Trade Desk
article_title: Audience Sync de Canvas con The Trade Desk
description: "Este artículo de referencia explica cómo usar Braze Audience Sync con The Trade Desk para entregar anuncios basados en desencadenantes de comportamiento, segmentación y más."
alias: /trade_desk_audience_sync/
Tool:
  - Canvas
page_order: 7
---

# Audience Sync con The Trade Desk

> Con Braze Audience Sync con The Trade Desk, puedes sincronizar dinámicamente tus datos propios de usuario desde Braze directamente con The Trade Desk para reorientación de anuncios, modelado de audiencias similares y supresión.

**Los casos de uso comunes para la sincronización de audiencias incluyen:**

- Reorientar a tus usuarios existentes en The Trade Desk con campañas personalizadas.
- Enviar datos propios a The Trade Desk para segmentación por exclusión.
- Sincronizar usuarios con audiencias nuevas o existentes o segmentos de datos de CRM.

## Requisitos previos

Asegúrate de tener los siguientes elementos creados, completados o aceptados antes de configurar el paso de Audience Sync con The Trade Desk en Canvas.

| Requisito | Origin | Descripción |
| --- | --- | --- |
| Token de API | [The Trade Desk](https://partner.thetradedesk.com/v3/portal/api/doc/Authentication#ui-method-create) | Un token de API estándar creado en la plataforma de The Trade Desk. Recomendamos configurar la duración del token de API en hasta un año para evitar interrupciones mínimas en tus Canvas con The Trade Desk Audience Sync. |
| Términos y políticas de The Trade Desk | The Trade Desk | Debes aceptar una política de participación de UID2/CRM antes de que se te habilite para enviar datos a The Trade Desk. Ponte en contacto con tu representante en The Trade Desk para confirmar que tienes la firma adecuada para habilitar la entrega de datos a The Trade Desk.<br><br> {::nomarkdown}<ul><li>Confirma que el acceso a la gestión de datos de CRM está habilitado en tu cuenta&#8212tu representante en The Trade Desk puede ayudarte con esto. Debes tener tu ID de anunciante.</li><li>Ten listo tu token de API estándar. Puedes seguir las instrucciones de esta página para generar uno.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

### Paso 1: Conectar la cuenta de The Trade Desk

Para empezar, ve a **Integraciones de socios** > **Socios tecnológicos** > **The Trade Desk**. Proporciona los siguientes datos de tu cuenta de Trade Desk:

- **Token de API**
- **Nombre del ID de anunciante** (este nombre opcional identifica la cuenta de anunciante como referencia en el paso de Audience Sync de Canvas)
- **ID de anunciante**

Luego, selecciona **Conectar**.

![Un ejemplo de un Audience Sync no conectado para The Trade Desk.]({% image_buster /assets/img/audience_sync/trade_desk/connect_sync.png %}){: style="max-width:90%;"}

### Paso 2: Añadir un paso de Audience Sync con The Trade Desk

Añade un componente en tu Canvas y selecciona **Audience Sync**. Luego, selecciona **The Trade Desk** como socio de Audience Sync.

![Opción para seleccionar tu socio con el que sincronizar en el paso de Audience Sync.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step.png %}){: style="max-width:90%;"}

### Paso 3: Configurar tu sincronización

A continuación, configura los detalles de tu sincronización:

1. Selecciona una cuenta de anuncios.
2. Elige una audiencia existente o crea una nueva audiencia.

![Configuración de Audience Sync con un campo de audiencia que contiene el nombre "valentines2025".]({% image_buster /assets/img/audience_sync/trade_desk/choose_audience.png %}){: style="max-width:90%;"}

{: start="3"}
3. Selecciona una acción para **Añadir usuarios a la audiencia** o **Quitar usuarios de la audiencia**.

![Configuración de Audience Sync para añadir usuarios a la audiencia.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step2.png %}){: style="max-width:90%;"}

{: start="4"}
4. Elige uno de los siguientes campos para la coincidencia: **Correo electrónico**, **Teléfono** o **ID de anunciante móvil**.

{% alert note %}
Si estás sincronizando con una audiencia en The Trade Desk con una región configurada en la UE, el número de teléfono no es compatible con The Trade Desk. Ponte en contacto con The Trade Desk para obtener soporte de número de teléfono en la región de la UE.
{% endalert %}

### Paso 4: Lanzar tu Canvas

Después de configurar tu Audience Sync con The Trade Desk, ¡ya puedes lanzar el Canvas! La nueva audiencia se crea, y los usuarios que pasan por el paso de Audience Sync se incorporan a esta audiencia en The Trade Desk. Si tu Canvas contiene componentes posteriores, tus usuarios avanzan al siguiente paso en su recorrido de usuario.

## Preguntas frecuentes

### ¿Cuánto tiempo tardará en llenarse el tamaño de la audiencia en The Trade Desk?

Puede tardar hasta 24 horas.

### ¿Cuál es el tamaño mínimo de audiencia para que The Trade Desk la llene dentro de tu cuenta de anuncios?

No hay un tamaño mínimo de audiencia para las audiencias de CRM en The Trade Desk.

### ¿Cómo sé si los usuarios han coincidido después de enviarlos a The Trade Desk?

En The Trade Desk, los ID recibidos aparecen junto al segmento.

- Los ID recibidos son el número de ID que se recibieron en los últimos 30 días.
- Los ID activos son el número de ID que se han visto en pujas en los últimos siete días.

### ¿Cuántas audiencias puede admitir The Trade Desk?

No hay límite en la cantidad de audiencias que se pueden admitir en The Trade Desk.