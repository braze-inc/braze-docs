---
nav_title: Cabeceras de la Política de Seguridad de Contenidos
article_title: Cabeceras de Política de Seguridad de Contenidos para la Web
platform: Web
page_order: 25
page_type: reference
description: "Este artículo cubre los encabezados de políticas de seguridad de contenidos que se necesitan con el SDK Web de Braze."

---

# Cabeceras de la política de seguridad de contenidos

> La política de seguridad de contenidos proporciona seguridad añadida al restringir cómo y dónde se puede cargar contenido en tu sitio web. Este artículo de referencia cubre qué encabezados de políticas de seguridad de contenidos son necesarios con el SDK Web.

{% alert important %}
Este artículo está dirigido a los desarrolladores que trabajan en sitios web que aplican reglas CSP y se integran con Braze. No pretende ser un consejo sobre cómo debes enfocar la seguridad.
{% endalert %}

{% multi_lang_include archive/web-v4-rename.md %}

## Atributos nonce {#nonce}

Si utilizas un valor `nonce` en tus directivas `script-src` o `style-src`, pasa ese valor a la opción de inicialización `contentSecurityNonce` para propagarlo a los scripts recién creados y a los estilos generados por el SDK:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  contentSecurityNonce: "YOUR-NONCE-HERE", // assumes a "nonce-YOUR-NONCE-HERE" CSP value
});
```

## Directivas {#directives}

### conectar-src {#connect-src}

- `connect-src https://sdk.iad-01.braze.com`: permite al SDK comunicarse con las API de Braze.
  - Cambia esta URL para que coincida con [el punto final del SDK de la API de]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) tu opción de inicialización `baseUrl`.

### script-src {#script-src}

- `script-src https://js.appboycdn.com`: necesario cuando se utiliza la integración alojada en CDN.
- `script-src 'unsafe-eval'`: necesario cuando se utiliza el fragmento de código de integración que contiene una referencia a `appboyQueue`
  - Para evitar el uso de esta directiva, realiza la integración mediante NPM.
- `script-src 'nonce-...'` o `script-src 'unsafe-inline'`: necesario para determinados mensajes dentro de la aplicación (por ejemplo, HTML personalizado).

### img-src {#img-src}
- `img-src: appboy-images.com braze-images.com cdn.braze.eu`: necesario cuando se utilizan imágenes alojadas en CDN de Braze. Estos nombres de host pueden variar según el grupo de paneles.

## Font Awesome {#font-awesome}

Para desactivar la inclusión automática de Font Awesome, utiliza la opción de inicialización `doNotLoadFontAwesome`:

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize(apiKey, {
  baseUrl: baseUrl,
  doNotLoadFontAwesome: true,
});
```

Si decides utilizar Font Awesome, se requieren las siguientes directivas CSP:

- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` o `style-src 'unsafe-inline'`
- `font-src https://use.fontawesome.com`
