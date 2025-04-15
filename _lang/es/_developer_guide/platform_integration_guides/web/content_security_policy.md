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

|URL|Información|
|---|-----------|
|`connect-src https://sdk.iad-01.braze.com`|Permite al SDK comunicarse con las API Braze. Cambia esta URL para que coincida con el [punto final SDK de la API]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/) para la opción de inicialización `baseUrl` que hayas elegido.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### script-src {#script-src}

|URL|Información|
|---|-----------|
|`script-src https://js.appboycdn.com`|Necesario cuando se utiliza la integración alojada en CDN.|
|`script-src 'unsafe-eval'`|Necesario cuando se utiliza el fragmento de código de integración que contiene la referencia a `appboyQueue`. Para evitar el uso de esta directiva, [integra el SDK utilizando NPM]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/?tab=package%20manager).|
|`script-src 'nonce-...'`<br>o<br>`script-src 'unsafe-inline'`|Necesario para determinados mensajes dentro de la aplicación, como HTML personalizado.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### img-src {#img-src}

|URL|Información|
|---|-----------|
|`img-src: appboy-images.com braze-images.com cdn.braze.eu`|Necesario cuando se utilizan imágenes alojadas en CDN Braze. Los nombres de host pueden variar según el grupo de paneles.<br><br>**Importante:** Si utilizas fuentes personalizadas, también tienes que incluir `font-src`.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

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

- `font-src https://use.fontawesome.com`
- `style-src https://use.fontawesome.com`
- `style-src 'nonce-...'` o `style-src 'unsafe-inline'`
