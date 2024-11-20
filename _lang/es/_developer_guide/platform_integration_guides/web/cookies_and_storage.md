---
nav_title: Cookies y almacenamiento
article_title: Cookies y almacenamiento para Web
platform: Web
page_order: 15
page_type: reference
description: "Este artículo de referencia describe las diferentes cookies que utiliza el SDK Web de Braze."

---

# Cookies y almacenamiento

> Este artículo describe las diferentes cookies que utiliza el SDK Web de Braze.

Antes de seguir leyendo, ten en cuenta que el SDK para la Web de Braze no almacenará ningún dato en el navegador (cookies o de otro tipo) hasta que tu sitio web [inicialice](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) el SDK.

Además, estos valores están sujetos a cambios y no se debe acceder a ellos directamente a través de tu integración. En su lugar, consulta nuestra [documentación de JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html) para conocer nuestras interfaces API públicas.

{% multi_lang_include archive/web-v4-rename.md %}

## Cookies {#cookies}

Esta sección proporciona información sobre cómo se pueden configurar y administrar las cookies en el SDK Web de Braze. El SDK para Web de Braze está diseñado para ofrecerte la máxima flexibilidad, cumplimiento legal y relevancia de los mensajes.

Cuando Braze crea cookies, éstas se almacenan con una caducidad de 400 días que se renueva automáticamente en nuevas sesiones.

### Desactivar cookies {#disable-cookies}

Para desactivar todas las cookies, utiliza la opción [`noCookies`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) al inicializar el SDK Web.
Deshabilitar las cookies te impedirá asociar usuarios anónimos que naveguen a través de subdominios y dará lugar a un nuevo usuario en cada subdominio.

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    noCookies: true
});
```

Para detener el seguimiento de Braze en general, o para borrar todos los datos almacenados del navegador, consulta los métodos del SDK [`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disableSDK) y [`wipeData`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#wipedata), respectivamente. Estos dos métodos pueden ser útiles si un usuario revoca su consentimiento o si quieres detener toda la funcionalidad de Braze después de que el SDK se haya inicializado.

### Lista de cookies

|Cookie|Descripción|Tamaño|
|---|----|---|---|
|`ab.storage.userId.[your-api-key]`|Se utiliza para determinar si el usuario conectado actualmente ha cambiado y para asociar eventos con el usuario actual.|En función del tamaño del valor pasado a `changeUser`|
|`ab.storage.sessionId.[your-api-key]`|Cadena generada aleatoriamente que se utiliza para determinar si el usuario está iniciando una sesión nueva o existente para sincronizar mensajes y calcular los análisis de la sesión.|~200 bytes|
|`ab.storage.deviceId.[your-api-key]`|Cadena generada aleatoriamente que se utiliza para identificar a los usuarios anónimos y para diferenciar los dispositivos de los usuarios y habilita la mensajería basada en dispositivos.|~200 bytes|
|`ab.optOut`|Se utiliza para almacenar la preferencia de adhesión voluntaria de un usuario cuando se llama a `disableSDK` |~40 bytes|
|`ab._gd`|Creado temporalmente (y luego eliminado) para determinar el dominio de la cookie de nivel raíz, que permite que el SDK funcione correctamente a través de subdominios.|n/a|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Propiedades del dispositivo

De forma predeterminada, Braze recopilará las siguientes propiedades a nivel de dispositivo para permitir la personalización de mensajes basada en el dispositivo, el idioma y la zona horaria:

* BROWSER
* VERSIÓN_DEL_NAVEGADOR
* LANGUAGE
* OS
* RESOLUTION
* TIME_ZONE
* USER_AGENT

Puedes desactivar o especificar las propiedades que deseas recopilar configurando la opción de inicialización `devicePropertyAllowlist` en una lista de [`DeviceProperties`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.deviceproperties.html). 

```javascript
import * as braze from"@braze/web-sdk";
braze.initialize("API-KEY", {
    baseUrl: "BASE-URL",
    devicePropertyAllowlist: [ braze.DeviceProperties.LANGUAGE ] // list of `DeviceProperties` you want to collect
});
```

Por defecto, todos los campos están habilitados. Ten en cuenta que, sin algunas propiedades, no todas las funciones funcionarán correctamente. Por ejemplo, la entrega según la zona horaria local no funcionará sin la zona horaria.

Para saber más sobre las propiedades del dispositivo recopiladas automáticamente, visita [Opciones de recopilación de datos del SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/). 


