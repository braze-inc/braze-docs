---
nav_title: Datadog
article_title: "Datadog"
description: "Este artículo de referencia describe la asociación con Braze y Datadog, un servicio de observabilidad para aplicaciones a escala de nube, que proporciona supervisión de servidores, bases de datos, herramientas y servicios a través de una plataforma de análisis de datos basada en SaaS."
alias: /partners/datadog/
page_type: partner
search_tag: Partner


---

# Datadog

> [Datadog](https://www.datadoghq.com/) es un servicio de observabilidad para aplicaciones a escala de nube, que proporciona supervisión de servidores, bases de datos, herramientas y servicios a través de una plataforma de análisis de datos basada en SaaS.

La integración de Braze y Datadog permite a los clientes recopilar datos de Braze en Datadog y crear alertas sobre los datos que enviamos. Por ejemplo, configurar un monitor y alertar si su campaña de boletín semanal envía un volumen anormalmente bajo de mensajes o si un paso de Canvas que normalmente sólo envía unos pocos mensajes al día empieza a enviar miles. 

## Requisitos previos 

| Requisito | Descripción |
|---|---|
| Cuenta Datadog | Se necesita una cuenta de Datadog para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Generar clave Datadog

En Datadog, tendrás que crear una [clave de API](https://docs.datadoghq.com/account_management/api-app-keys/#api-keys). Para añadir una clave API, vaya a **Configuración de la organización** > **Claves API** > **Nueva clave**.

### Paso 2: Añadir una clave a Braze

En el panel Braze, vaya a **Integraciones de socios** > **Socios tecnológicos** y busque **Datadog**. En la página del socio de Datadog, proporciona la clave de API de Datadog. Esto creará una conexión que permitirá a Braze enviar datos a Datadog.

## Eventos Braze

Una vez integrada la conexión, Braze enviará los siguientes eventos a Datadog:

- `braze.messaging.sent` - El recuento de envíos

Cada uno de estos eventos tendrá metadatos en forma de etiquetas Datadog para darle información como:

- `app_group_id`
- `app_group_name`
- `campaign_id` / `campaign_name` (si está disponible)
- `canvas_id` / `canvas_name` / `canvas_step_id` / `canvas_step_name` (si está disponible)

Estos eventos y etiquetas pueden supervisarse en la página **Explorador de métricas** de Datadog. Estas métricas se registran como [distribuciones](https://docs.datadoghq.com/metrics/distributions/) a DataDog. Dada la naturaleza de las métricas y la imprecisión de las agregaciones y rollups de DataDog, Braze no reintenta errores de red intermitentes u otros errores de API de DataDog que puedan encontrarse durante la transmisión. Esto significa que estos recuentos métricos pueden diferir ligeramente de los recuentos vistos en el tablero Braze y/o a través de Currents.

![]({% image_buster /assets/img/datadog.png %})

