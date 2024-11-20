---
nav_title: Notificaciones push web para móvil en Safari
article_title: Notificaciones push web para móvil en Safari
platform: Web
channel: push
page_order: 5
page_type: reference
description: "Este artículo de referencia explica cómo integrar la notificación push web en tus navegadores Safari de iOS y iPad."
search_rank: 3
---

# Notificaciones push web para móvil en Safari (iOS y iPadOS)

> [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) es compatible con push web móvil, lo que significa que ahora puedes reactivar la interacción de los usuarios móviles con notificaciones push en iOS y iPadOS.<br><br>Este artículo te guiará a través de los pasos necesarios para configurar push móvil para Safari.

## Pasos de la integración

Primero, lee y sigue nuestra [guía estándar de integración push web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/). Los siguientes pasos solo son necesarios para admitir la notificación push web en Safari para iOS y iPadOS.

### Paso 1: Crear un archivo de manifiesto {#manifest}

Un [Manifiesto de Aplicación Web](https://developer.mozilla.org/en-US/docs/Web/Manifest) es un archivo JSON que controla cómo se presenta tu sitio web cuando se instala en la pantalla de inicio de un usuario.

Por ejemplo, puedes configurar el color del tema de fondo y el icono que utiliza [el Conmutador de Aplicaciones](https://support.apple.com/en-us/HT202070), si se representa a pantalla completa para parecerse a una aplicación nativa, o si la aplicación debe abrirse en modo horizontal o vertical.

Crea un nuevo archivo `manifest.json` en el directorio raíz de tu sitio web, con los siguientes campos obligatorios. 

```json
{
  "name": "your app name",
  "short_name": "your app name",
  "display": "fullscreen",
  "icons": [{
    "src": "favicon.ico",
    "sizes": "128x128",
  }]
}
```

La lista completa de campos admitidos se encuentra [aquí](https://developer.mozilla.org/en-US/docs/Web/Manifest).

### Paso 2: Enlaza el archivo de manifiesto {#manifest-link}

Añade la siguiente etiqueta `<link>` al elemento `<head>` de tu sitio web, indicando dónde está alojado tu archivo de manifiesto.

```html
<link rel="manifest" href="/manifest.json" />
```

### Paso 3: Añadir un prestador de servicios {#service-worker}

Tu sitio web debe tener un archivo de prestador de servicios que importe la biblioteca de prestadores de servicios Braze, como se describe en nuestra [guía de integración push web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-1-configure-your-sites-service-worker).

### Paso 4: Añadir a la pantalla de inicio {#add-to-homescreen}

A diferencia de los principales navegadores como Chrome y Firefox, no puedes solicitar permiso push en Safari iOS/iPadOS a menos que tu sitio web haya sido añadido a la pantalla de inicio del usuario. 

La característica [Añadir a la pantalla de inicio](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) permite a los usuarios marcar tu sitio web, añadiendo tu icono a su valioso espacio en la pantalla de inicio.

![Un iPhone mostrando opciones para marcar un sitio web y guardarlo en la pantalla de inicio]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Paso 5: Mostrar el mensaje push nativo {#push-prompt}
Una vez añadida la aplicación a tu pantalla de inicio, ahora puedes solicitar permiso push cuando el usuario realice una acción (como hacer clic en un botón). Esto puede hacerse utilizando el método [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) o con un [mensaje dentro de la aplicación como push primer sin código]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/).

{% alert note %}
Una vez que aceptes o rechaces la petición, tendrás que borrar y volver a instalar el sitio web en tu pantalla de inicio para poder volver a mostrar la petición.
{% endalert %}

![Un aviso push preguntando "permitir" o "no permitir" Notificaciones]({% image_buster /assets/img/push_implementation_guide/safari-mobile-push-prompt.png %}){: style="max-width:40%"}

Por ejemplo:

```typescript
import { requestPushPermission } from "@braze/web-sdk";

button.onclick = function(){
    requestPushPermission(() => {
        console.log(`User accepted push prompt`);
    }, (temporary) => {
        console.log(`User ${temporary ? "temporarily dismissed" : "permanently denied"} push prompt`);
    });
};
```


## Próximos pasos

A continuación, envíate un [mensaje de prueba]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) para validar la integración. Una vez completada la integración, puedes utilizar nuestros [mensajes push sin código]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/) para optimizar tus tasas de adhesión voluntaria push.

