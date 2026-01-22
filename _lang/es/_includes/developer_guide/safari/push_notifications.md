{% multi_lang_include developer_guide/prerequisites/web.md %} También tendrás que [configurar]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) las [notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=web) para el SDK Web. Ten en cuenta que sólo puedes enviar notificaciones push a usuarios de iOS y iPadOS que utilicen [Safari v16.4](https://developer.apple.com/documentation/safari-release-notes/safari-16_4-release-notes) o posterior.

## Configuración de Safari push para móviles

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

Los navegadores más populares (como Safari, Chrome, FireFox y Edge) admiten notificaciones push web en sus versiones posteriores. Para solicitar permiso push en iOS o iPadOS, tu sitio web debe añadirse a la pantalla **de** inicio del usuario seleccionando **Compartir en** > **Añadir a pantalla de inicio**. [Añadir a la](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) pantalla de [inicio](https://support.apple.com/guide/iphone/bookmark-favorite-webpages-iph42ab2f3a7/ios#iph4f9a47bbc) permite a los usuarios marcar tu sitio web, añadiendo tu icono a su valioso espacio en la pantalla de inicio.

![Un iPhone mostrando opciones para marcar un sitio web y guardarlo en la pantalla de inicio]({% image_buster /assets/img/push_implementation_guide/add-to-homescreen.png %}){: style="max-width:40%"}

### Paso 5: Mostrar el mensaje push nativo {#push-prompt}
Una vez añadida la aplicación a tu pantalla de inicio, ahora puedes solicitar permiso push cuando el usuario realice una acción (como hacer clic en un botón). Esto puede hacerse utilizando el método [`requestPushPermission`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestpushpermission) o con un [mensaje dentro de la aplicación como push primer sin código]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

{% alert note %}
Después de aceptar o rechazar el aviso, tienes que borrar y volver a instalar el sitio web en tu pantalla de inicio para poder volver a mostrar el aviso.
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

A continuación, envíate un [mensaje de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) para validar la integración. Una vez completada la integración, puedes utilizar nuestros [mensajes push sin código]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para optimizar tus tasas de adhesión voluntaria push.
