---
nav_title: Soporte de AMP
article_title: Soporte de AMP para web
platform: Web
page_order: 5
page_type: reference
description: "En este artículo de referencia se describe el soporte de AMP para web y cómo integrar Braze en una página AMP."

---

# Soporte de AMP

{% alert note %}
Esta sección no es necesaria para la integración, a menos que intentes integrar Braze en una página AMP.
{% endalert %}

> En este artículo de referencia se describe el soporte de AMP para web y cómo integrar Braze en una página AMP. Las páginas móviles aceleradas (AMP) es un proyecto respaldado por Google y diseñado para mejorar el tiempo de carga de las páginas en los dispositivos móviles mediante la aplicación de determinadas normas, como la restricción del uso de JavaScript.

Como resultado, el SDK de Braze no puede cargarse en una página AMP. Sin embargo, el proyecto AMP proporciona un componente compatible con la notificación push web. Las [siguientes instrucciones](https://www.ampproject.org/docs/reference/components/amp-web-push) detallan cómo configurar ese componente y hacen referencia a la siguiente documentación sobre el componente `amp-web-push`.

## Paso 1: Incluir script de notificación push web AMP

Añade la siguiente etiqueta de script asíncrono a tu cabecera:

```js
<script async custom-element="amp-web-push" src="https://cdn.ampproject.org/v0/amp-web-push-0.1.js"></script>
```

## Paso 2: Añadir un widget de suscripción y desuscripción

Tendrás que añadir un widget que permita a los usuarios suscribirse y cancelar suscripción desde push. Debe estar en vivo dentro del cuerpo de tu HTML y se le puede aplicar el estilo que mejor te parezca.

```js
<!-- A subscription widget -->
<amp-web-push-widget visibility="unsubscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.subscribe">Subscribe to Notifications</button>
</amp-web-push-widget>

<!-- An unsubscription widget -->
<amp-web-push-widget visibility="subscribed" layout="fixed" width="250" height="80">
  <button on="tap:amp-web-push.unsubscribe">Unsubscribe from Notifications</button>
</amp-web-push-widget>
```

## Paso 3: Descargar iFrame de ayuda y diálogo de permiso

El componente AMP de la notificación push web funciona creando una ventana emergente que gestiona la suscripción push. Como resultado, necesitarás incluir un par de archivos de ayuda en tu proyecto. Descarga el archivo [helper-iframe.html](https://cdn.ampproject.org/v0/amp-web-push-helper-frame.html) y el archivo [permission-dialog.html](https://cdn.ampproject.org/v0/amp-web-push-permission-dialog.html) y guárdalos en tu sitio.

## Paso 4: Crear un archivo de prestador de servicios

Crea un archivo `service-worker.js` con el siguiente contenido, y colócalo en el directorio raíz de tu sitio web:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Paso 5: Configurar el elemento HTML de notificación push web de AMP

Ahora tendrás que añadir el elemento HTML `amp-web-push` a tu página. Coloca el siguiente código HTML en el cuerpo de tu documento:

```js
<amp-web-push
layout="nodisplay"
id="amp-web-push"
helper-iframe-url="FILE_PATH_TO_YOUR_HELPER_IFRAME"
permission-dialog-url="FILE_PATH_TO_YOUR_PERMISSION_DIALOG"
service-worker-url="FILE_PATH_TO_YOUR_SERVICE_WORKER?apiKey={YOUR_API_KEY}&baseUrl={YOUR_BASE_URL}"
>
```

En concreto, el `service-worker-URL` requiere añadir tu `apiKey` y `baseUrl` (https://dev.appboy.com/api/v3) como parámetros de consulta.

Ahora deberías estar configurado para la suscripción push y la cancelación de suscripción en tu página AMP.
