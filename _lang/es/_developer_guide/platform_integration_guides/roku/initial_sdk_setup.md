---
nav_title: Configuración inicial del SDK
article_title: Configuración inicial del SDK de Roku
platform: Roku
page_order: 0
page_type: reference
description: "Esta página describe los pasos de configuración inicial del SDK de Roku de Braze."
search_rank: 1
---

# Integración de SDK inicial

> En este artículo de referencia se explica cómo instalar el SDK de Braze para Roku. La instalación del SDK de Roku de Braze te proporcionará funciones básicas de análisis y segmentación.

{% alert tip %}
Consulta nuestra aplicación Roku de muestra en GitHub: [TorchieTV](https://github.com/braze-inc/braze-roku-sdk/tree/main/torchietv).
{% endalert %}

## Paso 1: Añadir archivos

Los archivos del SDK de Braze se encuentran en el directorio `sdk_files` del [repositorio del SDK de Roku de Braze](https://github.com/braze-inc/braze-roku-sdk).

1. Añade `BrazeSDK.brs` a tu aplicación en el directorio `source`.
2. Añade `BrazeTask.brs` y `BrazeTask.xml` a tu aplicación en el directorio `components`.

## Paso 2: Añadir referencias

Añade una referencia a `BrazeSDK.brs` en tu escena principal utilizando el siguiente elemento `script`:

```
<script type="text/brightscript" uri="pkg:/source/BrazeSDK.brs"/>
```

## Paso 3: Configura

En `main.brs`, establece la configuración de Braze en el nodo global:

```brightscript
globalNode = screen.getGlobalNode()
config = {}
config_fields = BrazeConstants().BRAZE_CONFIG_FIELDS
config[config_fields.API_KEY] = {YOUR_API_KEY}
' example endpoint: "https://sdk.iad-01.braze.com/"
config[config_fields.ENDPOINT] = {YOUR_ENDPOINT}
config[config_fields.HEARTBEAT_FREQ_IN_SECONDS] = 5
globalNode.addFields({brazeConfig: config})
```

Puedes encontrar tu [punto final SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) y tu clave de API en el panel de Braze.

## Paso 4: Inicializar Braze

Inicializa la instancia de Braze:

```brightscript
m.BrazeTask = createObject("roSGNode", "BrazeTask")
m.Braze = getBrazeInstance(m.BrazeTask)
```

## Habilitar registro (opcional) {#logging}

Para depurar tu integración Braze, puedes ver los registros de la consola de depuración de Roku para Braze. Consulta el [código de depuración](https://developer.roku.com/docs/developer-program/debugging/debugging-channels.md) de los desarrolladores de Roku para obtener más información.

## Integración de SDK básica completa

Ahora Braze debería estar recopilando datos de tu aplicación con el SDK de Roku de Braze. 

Consulta los siguientes artículos sobre cómo [registrar atributos]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/setting_custom_attributes/), [eventos]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_custom_events/) y [compras]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/) en nuestro SDK.

Para obtener más información sobre la mensajería dentro de la aplicación en Roku, consulta nuestra [guía de integración de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/).


