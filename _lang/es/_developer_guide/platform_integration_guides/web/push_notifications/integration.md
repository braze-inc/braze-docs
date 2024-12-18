---
nav_title: Integración
article_title: Integración push para Web
platform: Web
channel: push
page_order: 0
page_type: reference
description: "En este artículo se describe cómo integrar las notificaciones push web de Braze a través del SDK de Braze."

local_redirect: #soft-push-prompts
  soft-push-prompts: '/docs/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/'
search_rank: 3
---

# Integración de notificaciones push

> Una notificación push es una alerta que aparece en la pantalla del usuario cuando se produce una actualización importante. Las notificaciones push pueden recibirse aunque tu página Web no esté abierta en ese momento en el navegador del usuario. Las notificaciones push son una forma valiosa de proporcionar a tus usuarios contenido relevante y urgente, o de reactivar su interacción con tu sitio web. En este artículo de referencia se explica cómo integrar las notificaciones push web de Braze con el SDK de Braze.

Consulta nuestras [mejores prácticas de notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/) para obtener más recursos.

![]({{site.baseurl}}/assets/img_archive/web_push2.png)

Las notificaciones push web se implementan utilizando el [estándar push del W3C](http://www.w3.org/TR/push-api/), compatible con la mayoría de los principales navegadores.

Para obtener más información sobre las normas del protocolo push y la compatibilidad de los navegadores, puedes consultar los recursos de [AppleSafari](https://developer.apple.com/notifications/safari-push-notifications/ "Push Notifications") [MozillaMozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility "Push API compatibilidad con navegadores") y [MicrosoftMicrosoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/ "Push API")

{% multi_lang_include archive/web-v4-rename.md %}

## Integración

### Paso 1: Configura el prestador de servicios de tu sitio web

- Si aún no tienes un prestador de servicios, crea un nuevo archivo llamado `service-worker.js` con el siguiente fragmento de código, y colócalo en el directorio raíz de tu sitio web.
- De lo contrario, si tu sitio ya registra un prestador de servicios, añade el siguiente fragmento de código al archivo del prestador de servicios y establece la opción de inicialización [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) a `true` al inicializar el SDK Web.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

Si el nombre de archivo de tu prestador de servicios no es `service-worker.js`, debes utilizar la [opción de inicialización](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `serviceWorkerLocation`.

{% alert important %}
Tu servidor Web debe devolver un `Content-Type: application/javascript` al servir tu archivo de prestador de servicios.
{% endalert %}

#### ¿Qué pasa si no puedo registrar un prestador de servicios en el directorio raíz?

Por defecto, un prestador de servicios sólo puede utilizarse dentro del mismo directorio en el que está registrado. Por ejemplo, si tu archivo de prestador de servicios existe en `/assets/service-worker.js`, sólo sería posible registrarlo en `example.com/assets/*` o en un subdirectorio de la carpeta `assets`, pero no en tu página de inicio (`example.com/`). Por esta razón, se recomienda alojar y registrar el prestador de servicios en el directorio raíz (como `https://example.com/service-worker.js`).

Si no puedes registrar un prestador de servicios en tu dominio raíz, una alternativa es utilizar el encabezado HTTP [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) al servir el archivo de tu prestador de servicios. Configurando tu servidor para que devuelva `Service-Worker-Allowed: /` en la respuesta para el prestador de servicios, esto indicará al navegador que amplíe el alcance y permita utilizarlo desde un directorio diferente.

#### ¿Puedo crear un prestador de servicios utilizando un administrador de etiquetas?

No, los prestadores de servicios deben estar alojados en el servidor de tu sitio web y no pueden cargarse a través del administrador de etiquetas.

### Paso 2: Registro del navegador

Para que un navegador reciba notificaciones push, debes registrarlo para push llamando a `braze.requestPushPermission()`. Esto solicitará inmediatamente permiso push al usuario. 

Si deseas mostrar tu propia interfaz de usuario relacionada con push al usuario antes de solicitarle permiso push (lo que se conoce como solicitud de push suave), puedes comprobar si el navegador del usuario admite push con `braze.isPushSupported()`. Consulta el [ejemplo de aviso push suave]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) utilizando mensajes dentro de la aplicación.

Si deseas cancelar la suscripción de un usuario, puedes hacerlo llamando a `braze.unregisterPush()`.

{% alert important %}
Las versiones recientes de Safari y Firefox requieren que llames a este método desde un controlador de eventos de corta duración (por ejemplo, desde un controlador de clic en un botón o un aviso push suave). Esto es coherente con [las mejores prácticas de experiencia del usuario de Chrome](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) para el registro push.
{% endalert %}

### Paso 3: Configurar Safari push (opcional) {#safari}

{% alert important %}
Este paso ya no es necesario a partir de Safari 16 en macOS 13. Completa este paso sólo si quieres dar soporte a versiones antiguas de Safari para macOS.
{% endalert %}

Si deseas admitir notificaciones push para Safari en Mac OS X, sigue estas instrucciones adicionales:

- Genera un certificado push de Safari siguiendo las instrucciones de [Registro con Apple](https://developer.apple.com/library/mac/documentation/NetworkingInternet/Conceptual/NotificationProgrammingGuideForWebsites/PushNotifications/PushNotifications.html#//apple_ref/doc/uid/TP40013225-CH3-SW33).
- En el panel de Braze, en la página **Configuración** (donde se encuentran tus claves de API), selecciona tu aplicación Web. Haz clic en **Configurar Safari Push** y sigue las instrucciones, subiendo el certificado push que acabas de generar.
- Cuando llames a `braze.initialize`, proporciona la opción de configuración opcional `safariWebsitePushId` con el ID push del sitio web que utilizaste al generar tu certificado push de Safari. Por ejemplo `braze.initialize('YOUR-API-KEY', {safariWebsitePushId: 'web.com.example.domain'})`

## Notificaciones push para móvil en Safari {#safari-mobile}

Safari 16.4+ en iOS y iPadOS es compatible con la función push web para aplicaciones que se hayan [añadido a la pantalla de inicio](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) y tengan un archivo de [manifiesto de aplicación web](https://developer.mozilla.org/en-US/docs/Web/Manifest). Una vez que hayas completado los pasos para integrar las notificaciones push web, puedes proporcionar soporte para notificación push para móvil también en Safari. 

Para admitir la notificación push web de Safari móvil, sigue nuestra [guía aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/).

## Aviso push suave

Un aviso push suave (también conocido como "push primer") ayuda a optimizar tu tasa de adhesión voluntaria cuando se trata de solicitar permisos.

Visita [Aviso de pulsación suave]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/soft_push_prompt/) para saber más sobre la configuración de un aviso de pulsación suave.

## Requisito HTTPS

Las normas web exigen que el dominio que solicita el permiso de notificación push sea seguro.

### ¿Qué define un sitio seguro?

Un sitio se considera seguro si coincide con uno de los siguientes patrones de origen seguros:

- (https, , \*)
- (wss, \*, \*)
- (, localhost, )
- (, .localhost, \*)
- (, 127/8, )
- (, ::1/128, \*)
- (file, \*, —)
- (chrome-extension, \*, —)

Este requisito de seguridad de la especificación de estándares abiertos en la que se basa Braze Web push evita los ataques de intermediario.

### ¿Qué pasa si no está disponible un sitio seguro?

Aunque la mejor práctica del sector es hacer que todo tu sitio sea seguro, los clientes que no puedan asegurar el dominio de su sitio pueden eludir el requisito utilizando un modal seguro. Lee más en nuestra guía sobre el uso de [Dominio push alternativo]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) o ve una [demostración en funcionamiento](http://appboyj.com/modal-test.html).

## Configuración avanzada del prestador de servicios

Nuestro archivo de prestador de servicios llamará automáticamente a `skipWaiting` al instalarlo. Si quieres evitarlo, añade el siguiente código a tu archivo de prestador de servicios, antes de importar Braze:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Solución de problemas

**He seguido las instrucciones de integración, pero sigo sin recibir ninguna notificación push.**
- Las notificaciones push web requieren que tu sitio sea HTTPS.
- No todos los exploradores pueden recibir mensajes push. Asegúrate de que `braze.isPushSupported()` devuelve `true` en el navegador.
- Si un usuario ha denegado el acceso push a un sitio, no se le volverá a pedir permiso a menos que elimine el estado denegado de las preferencias de su navegador.

