---
nav_title: Extensiones del navegador
article_title: Integración de extensiones de navegador para Web
platform: Web
page_order: 20
page_type: reference
description: "Este artículo describe cómo utilizar el SDK Web de Braze dentro de las extensiones de tu navegador (Google Chrome, Firefox)."

---

# Extensión del navegador

> Este artículo describe cómo utilizar el SDK Web de Braze dentro de las extensiones de tu navegador (Google Chrome, Firefox).

Integra el SDK de Braze Web en la extensión de tu navegador para recopilar análisis y mostrar mensajes enriquecidos a los usuarios. Esto incluye tanto **las extensiones de Google Chrome** como **los complementos de Firefox**.

## Qué se admite

En general, dado que las extensiones son HTML y JavaScript, puedes usar Braze para lo siguiente:

* **Análisis**: Captura eventos personalizados, atributos e incluso identifica a usuarios recurrentes dentro de tu extensión. Usa estos rasgos de perfil para potenciar la mensajería multicanal.
* **Mensajes dentro de la aplicación**: Desencadena mensajes dentro de la aplicación cuando los usuarios realicen una acción dentro de tu extensión, utilizando nuestra mensajería nativa o HTML personalizada.
* **Tarjetas de contenido**: Añade una fuente de tarjetas nativas a tu extensión para la incorporación o el contenido promocional.
* **Notificaciones push web**: Envía notificaciones puntuales aunque tu página Web no esté abierta en ese momento.

## Lo que no se admite

* Los prestadores de servicios no son compatibles con el SDK de la Web de Braze, sin embargo, esto está en la hoja de ruta para considerarlo en el futuro.

## Tipos de extensión

Braze puede incluirse en las siguientes áreas de tu extensión:

| Área | Detalles | Qué se admite |
|--------|-------|------|
| Página emergente | La página [emergente](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Popups) es un diálogo que puede mostrarse a los usuarios al hacer clic en el icono de tu extensión en la barra de herramientas del navegador.| Análisis, mensajes dentro de la aplicación y tarjetas de contenido |
| Guiones de fondo | [Los scripts de fondo](https://developer.chrome.com/extensions/background_pages) (sólo Manifiesto v2) permiten a tu extensión inspeccionar e interactuar con la navegación del usuario o modificar páginas web (por ejemplo, cómo los bloqueadores de anuncios detectan y cambian el contenido de las páginas). | Análisis, mensajes dentro de la aplicación y tarjetas de contenido.<br><br>Los scripts de fondo no son visibles para los usuarios, por lo que para la mensajería, necesitarías comunicarte con las pestañas del navegador o con tu página emergente al mostrar los mensajes. |
| Páginas de opciones | La [Página de Opciones](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages) permite a tus usuarios alternar configuraciones dentro de tu extensión. Es una página HTML independiente que abre una nueva pestaña. | Análisis, mensajes dentro de la aplicación y tarjetas de contenido |
{: .reset-td-br-1 .reset-td-br-2, .reset-td-br-3 role="presentation" }

## Permisos

No se requieren permisos adicionales en tu `manifest.json` cuando se integra el SDK de Braze (`braze.min.js`) como un archivo local incluido con tu extensión. 

Sin embargo, si utilizas [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/), o haces referencia al SDK de Braze desde una URL externa, o has establecido una Política de seguridad de contenidos estricta para tu extensión, tendrás que ajustar la opción [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) configuración en tu `manifest.json` para permitir fuentes de scripts remotas.

## Cómo empezar

{% alert tip %}
Antes de empezar, asegúrate de haber leído la [guía de configuración inicial del SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web) Web para saber más sobre nuestra integración de JavaScript en general.  <br><br>También puedes marcar la [referencia del SDK de](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) JavaScript para obtener información detallada sobre los distintos métodos y opciones de configuración del SDK.
{% endalert %}

Para integrar el SDK Braze Web, primero tendrás que descargar una copia de la biblioteca JavaScript más reciente. Esto puede hacerse utilizando NPM o descargándolo directamente de la [CDN de Braze](https://js.appboycdn.com/web-sdk/latest/braze.min.js).

Alternativamente, si prefieres utilizar [Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) o utilizar una copia alojada externamente del SDK de Braze, ten en cuenta que cargar recursos externos requerirá que ajustes tu [`content_security_policy`](https://developer.chrome.com/extensions/contentSecurityPolicy) configuración en tu `manifest.json`.

Una vez descargado, asegúrate de copiar el archivo `braze.min.js` en algún lugar del directorio de tu extensión.

### Extensiones emergentes {#popup}

Para añadir Braze a una extensión emergente, haz referencia al archivo JavaScript local en tu `popup.html`, como harías en un sitio web normal. Si utilizas Google Tag Manager, puedes añadir Braze utilizando nuestras [plantillas de Google Tag Manager]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/google_tag_manager/) en su lugar.

```html
<html>
    <title>popup.html</title>
    <!-- Add the Braze library -->
    <script src="/relative/path/to/braze.min.js"></script>
    <script>
    // Initialize Braze here
    </script>
</html>
```

### Script de fondo (sólo Manifiesto v2) {#background-script}

Para utilizar Braze dentro del script de fondo de tu extensión, añade la biblioteca Braze a tu `manifest.json` en la matriz `background.scripts`. Esto hará que la variable global `braze` esté disponible en el contexto de tu guión en segundo plano.


```json
{
    "manifest_version": 2,
    "background": {
        "scripts": [
            "relative/path/to/braze.min.js",
            "background.js"
        ],
    }
}
```

### Página de opciones {#options-page}

Si utilizas una página de opciones (a través de las propiedades del manifiesto `options` o `options_ui` ), puedes incluir Braze tal y como lo harías en [las instrucciones de`popup.html` ](#popup).

## Inicialización

Una vez incluido el SDK, puedes inicializar la biblioteca como de costumbre. 

Dado que las extensiones del navegador no admiten cookies, puedes desactivarlas inicializando con `noCookies: true`.

```javascript
braze.initialize("YOUR-API-KEY-HERE", {
    baseUrl: "YOUR-API-ENDPOINT",
    enableLogging: true,
    noCookies: true
});
```

Para más información sobre las opciones de inicialización admitidas, visita la [referencia del SDK Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).

## Push

Los diálogos emergentes de las extensiones no permiten las solicitudes push (no tienen la barra de URL en la navegación). Así que para registrarte y solicitar permiso push en el cuadro de diálogo emergente de una extensión, tendrás que utilizar una solución alternativa para el dominio, como se describe en [Dominio push alternativo]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain).

