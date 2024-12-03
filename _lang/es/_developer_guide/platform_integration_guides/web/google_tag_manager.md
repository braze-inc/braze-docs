---
nav_title: Google Tag Manager
article_title: Google Tag Manager para Web
platform: Web
page_order: 20
description: "Este artículo explica cómo utilizar Google Tag Manager para implementar Braze en tu sitio web."

---

# Google Tag Manager

> En este artículo se proporciona una guía paso a paso sobre cómo añadir el SDK Web de Braze a tu sitio web mediante Google Tag Manager (GTM). [Google Tag Manager](https://support.google.com/tagmanager/answer/6103696) te permite añadir, eliminar y editar etiquetas de forma remota en tu sitio web sin necesidad de liberar código de producción ni recursos de ingeniería.

Hay dos plantillas de Google Tag Manager creadas por Braze, la [etiqueta de inicialización](#initialization-tag) y la [etiqueta de acciones](#actions-tag).

Ambas etiquetas pueden añadirse a tu espacio de trabajo desde [la galería de la comunidad de Google](https://tagmanager.google.com/gallery/#/?filter=braze) o buscando Braze al añadir una nueva etiqueta desde las plantillas de la comunidad.

![imagen de búsqueda de la galería]({% image_buster /assets/img/web-gtm/gtm-community-gallery-search.png %})

## Política actualizada de consentimiento del usuario de la UE de Google

{% alert important %}
Google está actualizando su [Política de Consentimiento del Usuario de la UE](https://www.google.com/about/company/user-consent-policy/) en respuesta a los cambios en la [Ley de Mercados Digitales (DMA)](https://ads-developers.googleblog.com/2023/10/updates-to-customer-match-conversion.html), que entrará en vigor el 6 de marzo de 2024. Este nuevo cambio obliga a los anunciantes a revelar cierta información a sus usuarios finales del EEE y del Reino Unido, así como a obtener de ellos los consentimientos necesarios. Revisa la siguiente documentación para saber más.
{% endalert %}

Como parte de la Política de consentimiento del usuario de la UE de Google, los siguientes atributos personalizados booleanos deben registrarse en los perfiles de usuario:

- `$google_ad_user_data`
- `$google_ad_personalization`

Si los configuras a través de la integración GTM, los atributos personalizados requieren la creación de una etiqueta HTML personalizada. A continuación se muestra un ejemplo de cómo registrar estos valores como tipos de datos booleanos (no como cadenas):

```js
<script>
window.braze.getUser().setCustomUserAttribute("$google_ad_personalization", true);
</script>
```

Para más información, consulta [Sincronización de audiencias con Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/).

## Plantilla de etiquetas de inicialización {#initialization-tag}

Utiliza la etiqueta de inicialización para añadir el SDK Braze Web a tu sitio web.

### Paso 1: Configuración push (opcional)

Opcionalmente, si quieres poder enviar push a través de Google Tag Manager, sigue primero las directrices de [integración de push]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/) a:
1. Configura el prestador de servicios de tu sitio, colocándolo en el directorio raíz de tu sitio
2. Configurar el registro del navegador - Una vez configurado el prestador de servicios, debes establecer el método `braze.requestPushPermission()` de forma nativa en su aplicación o mediante una etiqueta HTML personalizada (a través del panel GTM). También tendrás que asegurarte de que la etiqueta se dispara después de inicializar el SDK.

### Paso 2: Selecciona la etiqueta de inicialización

Busca Braze en la galería de plantillas de la comunidad y selecciona la **etiqueta de inicialización Braze**.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de inicialización Braze. Las configuraciones incluidas son "tipo de etiqueta", "clave de API", "punto final de API", "versión de SDK", "ID de usuario externo" e "ID push web de Safari".]({% image_buster /assets/img/web-gtm/gtm-initialization-tag.png %})

### Paso 3: Configurar ajustes

Introduce la clave de identificador de tu aplicación API de Braze y el punto final SDK, que puedes encontrar en la página **Administrar configuración** de tu panel. Introduce la versión más reciente del SDK Web `major.minor`. Por ejemplo, si la última versión es `4.1.2`, introduce `4.1`. Puedes ver una lista de las versiones del SDK en nuestro [registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).

### Paso 4: Elige las opciones de inicialización

Elige entre el conjunto opcional de opciones de inicialización adicionales descritas en la guía [Configuración inicial]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/#step-2-initialize-braze).

### Paso 5: Verificación y control de calidad

Una vez que hayas desplegado esta etiqueta, hay dos formas de verificar una integración adecuada:

1. Utilizando la [herramienta de depuración](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager, deberías ver que la etiqueta de inicialización de Braze se ha desencadenado en tus páginas o eventos configurados.
2. Deberías ver que se hacen peticiones de red a Braze, y la biblioteca global `window.braze` debería estar ahora definida en tu página Web.

## Plantilla de etiquetas de acciones {#actions-tag}

La plantilla de etiqueta de acciones Braze te permite desencadenar eventos personalizados, realizar un seguimiento de las compras, cambiar los ID de usuario y detener o reanudar el seguimiento por motivos de privacidad.

![]({% image_buster /assets/img/web-gtm/gtm-actions-tag.png %})

### Cambiar el ID externo del usuario {#external-id}

El tipo de etiqueta **Cambiar usuario** llama al [método`changeUser` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). 

Utiliza esta etiqueta siempre que un usuario se conecte o se identifique de otro modo con su identificador único `external_id`.

Asegúrate de introducir el ID único del usuario actual en el campo **ID externo del usuario**, que normalmente se rellena utilizando una variable de capa de datos enviada por tu sitio web.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción Braze. Las configuraciones incluidas son "tipo de etiqueta" e "ID externo del usuario".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})

### Registrar eventos personalizados {#custom-events}

El tipo de etiqueta **Evento personalizado** llama al [método`logCustomEvent` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

Utiliza esta etiqueta para enviar eventos personalizados a Braze, incluyendo opcionalmente propiedades del evento personalizadas.

Introduce el **Nombre del Evento** utilizando una variable o escribiendo un nombre de evento.

Utiliza el botón **Añadir Fila** para añadir propiedades del evento.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción Braze. Las configuraciones incluidas son "tipo de etiqueta" (evento personalizado), "nombre del evento" (clic del botón) y "propiedades del evento".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})

### Eventos de comercio electrónico {#ecommerce}

Si tu sitio registra las compras utilizando el elemento estándar de la capa de datos de [eventos de comercio electrónico](https://developers.google.com/analytics/devguides/collection/ga4/ecommerce?client_type=gtm) de Google Tag Manager, entonces puedes utilizar el tipo de etiqueta **Compra de comercio electrónico**. Este tipo de acción registrará una "compra" separada en Braze para cada artículo enviado en la lista de `items`.

También puedes especificar nombres de propiedades adicionales que quieras incluir como propiedades de la compra especificando sus claves en la lista Propiedades de la compra. Ten en cuenta que Braze buscará en el `item` individual que se está registrando cualquier propiedad de la compra que añadas a la lista.

Por ejemplo, supongamos que la carga útil de tu comercio electrónico contiene lo siguiente `items`:

```
items: [{
  item_name: "5 L WIV ECO SAE 5W/30",
  item_id: "10801463",
  price: 24.65,
  item_brand: "EUROLUB",
  quantity: 1
}]
```

Si sólo quieres que `item_brand` y `item_name` se pasen como propiedades de la compra, sólo tienes que añadir esos dos campos a la tabla de propiedades de la compra. Si no proporcionas ninguna propiedad, no se enviará ninguna propiedad de la compra en la [`logPurchase`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase) llamada a Braze.

### Seguimiento de la compra {#purchases}

El tipo de etiqueta **Compra** llama al [método`logPurchase` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logpurchase).

Utiliza esta etiqueta para hacer un seguimiento de las compras a Braze, incluyendo opcionalmente las propiedades de la compra.

Los campos **ID de producto** y **Precio** son obligatorios.

Utiliza el botón **Añadir fila** para añadir propiedades de la compra.

![Un cuadro de diálogo que muestra los ajustes de configuración de la etiqueta de acción Braze. Las configuraciones incluidas son "tipo de etiqueta", "ID externo", "precio", "código de moneda", "cantidad" y "propiedades de la compra".]({% image_buster /assets/img/web-gtm/gtm-purchase.png %})

### Detener y reanudar el seguimiento {#stop-tracking}

A veces, es posible que tengas que deshabilitar o volver a habilitar el seguimiento de Braze en tu sitio web, por ejemplo, después de que un usuario indique que ha optado por no participar en el seguimiento web por motivos de privacidad.

Utiliza el tipo de etiqueta **Deshabilitar seguimiento** o **Reanudar seguimiento** para deshabilitar o volver a habilitar el seguimiento Web, respectivamente. Estas dos opciones llaman [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) y [`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk).

### Atributos personalizados del usuario {#custom-attributes}

Los atributos personalizados de usuario no están disponibles debido a una limitación del lenguaje de programación de Google Tag Manager. Para registrar atributos personalizados, crea una etiqueta HTML personalizada con el siguiente contenido:

```html
<script>
  // Note: If using SDK version 3.x or below, use `window.appboy` instead of `window.braze`
  // Version 4 or greater should use `window.braze`
window.braze.getUser().setCustomUserAttribute("attribute name", "attribute value");
</script>
```

{% alert important %}
La plantilla GTM no admite propiedades anidadas sobre eventos o compras. Puedes utilizar el HTML anterior para registrar cualquier evento o compra que requiera propiedades anidadas.
{% endalert %}

### Atributos estándar del usuario {#standard-attributes}

Los atributos estándar de usuario, como el nombre de pila de un usuario, deben registrarse del mismo modo que los atributos personalizados de usuario. Asegúrate de que los valores que pasas para los atributos estándar coinciden con el formato esperado especificado en la documentación de [la clase Usuario](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html).

Por ejemplo, el atributo género puede aceptar cualquiera de los siguientes valores: `"m" | "f" | "o" | "u" | "n" | "p"`. Por lo tanto, para establecer el sexo de un usuario como femenino, crea una etiqueta HTML personalizada con el siguiente contenido:

```html
<script>
window.braze.getUser().setGender("f")
</script>
```

## Integración de tarjetas de contenido

Hay algunos pasos adicionales para integrar el canal de mensajería [de las tarjetas de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/) mediante Google Tag Manager. Google Tag Manager funciona inyectando la [CDN de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup#install-cdn) (una versión de nuestro SDK Web) directamente en el código de tu sitio web, lo que significa que todos los métodos del SDK están disponibles igual que si hubieras integrado el SDK sin Google Tag Manager, excepto al implementar tarjetas de contenido.

### Opción 1: Integración mediante GTM

Para una integración estándar de la fuente de la tarjeta de contenido, puedes utilizar una etiqueta **HTML personalizada** en Google Tag Manager. Añade lo siguiente a tu etiqueta HTML personalizada, que activará la fuente estándar de la tarjeta de contenido:

```html
<script>
   window.braze.showContentCards();
</script>
```

![Configuración en Google Tag Manager de una etiqueta HTML personalizada que muestra la fuente de la tarjeta de contenido.]({% image_buster /assets/img/web-gtm/gtm_content_cards.png %})

### Opción 2: Integración directa en tu sitio web

Para tener más libertad a la hora de personalizar el aspecto de las tarjetas de contenido y su fuente, puedes integrar directamente las tarjetas de contenido en tu sitio web nativo. Puedes hacerlo de dos formas: utilizando la interfaz de usuario estándar o creando una interfaz de usuario personalizada.

#### Fuente estándar

Al implementar la [IU de fuente estándar]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/integration/#standard-feed-ui), los métodos de Braze deben tener `window.` añadido al principio del método. Por ejemplo, `braze.showContentCards` debería ser `window.braze.showContentCards`.

#### IU de fuente personalizada

Para el estilo [personalizado de la fuente]({{site.baseurl}}/developer_guide/platform_integration_guides/web/content_cards/customization/custom_styling), los pasos son los mismos que si hubieras integrado el SDK sin GTM. Por ejemplo, si quieres personalizar la anchura de la fuente de la tarjeta de contenido, puedes pegar lo siguiente en tu archivo CSS:

{% raw %}
```css
body .ab-feed { 
    width: 800px;
}
```
{% endraw %}

## Mejora y actualización de plantillas {#upgrading}

Para actualizar a la última versión del SDK de la Web de Braze, sigue los tres pasos siguientes en tu panel de Google Tag Manager:

1. **Actualizar plantilla de etiquetas**<br>Ve a la página **Plantillas** dentro de tu espacio de trabajo. Aquí deberías ver un icono que indica que hay una actualización disponible.<br><br>![Página de plantillas que muestra que hay una actualización disponible]({% image_buster /assets/img/web-gtm/gtm-update-available.png %})<br><br>Haz clic en ese icono y, tras revisar el cambio, haz clic en **Aceptar actualización**.<br><br>![Una pantalla comparando las plantillas de etiquetas antigua y nueva con un botón para "Aceptar la actualización"]({% image_buster /assets/img/web-gtm/gtm-accept-update.png %})<br><br>
2. **Actualizar número de versión**<br>Una vez actualizada tu plantilla de etiquetas, edita la etiqueta de inicialización de Braze y actualiza la versión del SDK a la versión más reciente de `major.minor`. Por ejemplo, si la última versión es `4.1.2`, introduce `4.1`. Puedes ver una lista de las versiones del SDK en nuestro [registro de cambios](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md).<br><br>![Plantilla de inicialización de Braze con un campo de entrada para cambiar la versión del SDK]({% image_buster /assets/img/web-gtm/gtm-version-number.png %})<br><br>
3. **Control de calidad y publicación**<br>Comprueba que la nueva versión del SDK funciona utilizando la [herramienta de depuración](https://support.google.com/tagmanager/answer/6107056?hl=en) de Google Tag Manager antes de publicar una actualización en tu contenedor de etiquetas.

## Pasos para la solución de problemas {#troubleshooting}

### Habilitar la depuración de etiquetas {#debugging}

Cada plantilla de etiqueta Braze tiene una casilla de verificación opcional **Depuración de etiquetas GTM** que puede utilizarse para registrar mensajes de depuración en la consola JavaScript de tu página Web.

![Herramienta de depuración de Google Tag Manager]({% image_buster /assets/img/web-gtm/gtm-tag-debugging.png %})

### Entrar en modo depuración

Otra forma de ayudar a depurar tu integración con Google Tag Manager es utilizar la característica de [modo de vista previa](https://support.google.com/tagmanager/answer/6107056) de Google.

Esto ayudará a identificar qué valores se envían desde la capa de datos de tu página Web a cada etiqueta Braze desencadenada y también explicará qué etiquetas se desencadenaron o no.

![La página de resumen de la etiqueta de inicialización Braze proporciona un resumen de la etiqueta, incluyendo información sobre qué etiquetas se desencadenaron.]({% image_buster /assets/img/web-gtm/gtm-debug-mode.png %})

### Habilitar el registro detallado

Para permitir que el soporte técnico de Braze acceda a los registros durante las pruebas, puedes habilitar el registro detallado en tu integración con Google Tag Manager. Estos registros aparecerán en la pestaña **Consola** de las [herramientas del desarrollador](https://developer.mozilla.org/en-US/docs/Learn/Common_questions/What_are_browser_developer_tools) de tu navegador.

En tu integración de Google Tag Manager, navega hasta tu etiqueta de inicialización de Braze y selecciona **Habilitar registro SDK Web**.

![La página de resumen de la etiqueta de inicialización de Braze con la opción de habilitar el registro del SDK Web activada.]({% image_buster /assets/img/web-gtm/gtm_verbose_logging.png %})

[changelog]: https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md
