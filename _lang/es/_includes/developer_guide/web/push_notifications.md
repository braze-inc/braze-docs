{% multi_lang_include archive/web-v4-rename.md %}

{% multi_lang_include developer_guide/prerequisites/web.md %}

## Protocolos push

Las notificaciones push web se implementan utilizando el [estándar push del W3C](http://www.w3.org/TR/push-api/), compatible con la mayoría de los principales navegadores. Para más información sobre las normas específicas de los protocolos push y la compatibilidad de los navegadores, puedes consultar los recursos de [Apple](https://developer.apple.com/notifications/safari-push-notifications/) [, Mozilla](https://developer.mozilla.org/en-us/docs/web/api/push_api#browser_compatibility) y [Microsoft](https://developer.microsoft.com/en-us/microsoft-edge/status/pushapi/).

## Configuración de las notificaciones push

### Paso 1: Configura tu prestador de servicios

En el archivo `service-worker.js` de tu proyecto, añade el siguiente fragmento de código y establece la opción de inicialización [`manageServiceWorkerExternally`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize) a `true` al inicializar el SDK Web.

<script src="{{site.baseurl}}/assets/js/embed.js?target=https://github.com/braze-inc/braze-web-sdk/blob/master/sample-builds/cdn/service-worker.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

{% alert important %}
Tu servidor Web debe devolver un `Content-Type: application/javascript` al servir tu archivo de prestador de servicios. Además, si el archivo de tu prestador de servicios no tiene el nombre `service-worker.js`, tendrás que utilizar la [opción de inicialización](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) `serviceWorkerLocation`.
{% endalert %}

### Paso 2: Registra el navegador

Para solicitar inmediatamente permisos push a un usuario para que su navegador pueda recibir notificaciones push, llama a `braze.requestPushPermission()`. Para comprobar primero si se admite push en su navegador, llama a `braze.isPushSupported()`.

También puedes [enviar un aviso push suave]({{site.baseurl}}/developer_guide/push_notifications/soft_push_prompts/?sdktab=web) al usuario antes de solicitar el permiso push para mostrar tu propia interfaz de usuario relacionada con push.

{% alert important %}
En macOS, tanto **Google Chrome** como **Google Chrome Helper (Alertas)** deben ser habilitados por el usuario final en **Configuración del sistema > Notificaciones** antes de que puedan mostrarse las notificaciones push, incluso si se conceden permisos.
{% endalert %}

### Paso 3: Desactiva `skipWaiting` (opcional)

El archivo del prestador de servicios Braze llamará automáticamente a `skipWaiting` al instalarlo. Si quieres desactivar esta funcionalidad, añade el siguiente código a tu archivo de prestador de servicios, después de importar Braze:

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Fservice-worker-skip-waiting.js&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Cancelar suscripción de un usuario

Para cancelar la suscripción de un usuario, llama a `braze.unregisterPush()`.

{% alert important %}
Las versiones recientes de Safari y Firefox requieren que llames a este método desde un controlador de eventos de corta duración (como desde un controlador de clic en un botón o un indicador push suave). Esto es coherente con [las mejores prácticas de experiencia del usuario de Chrome](https://docs.google.com/document/d/1WNPIS_2F0eyDm5SS2E6LZ_75tk6XtBSnR1xNjWJ_DPE) para el registro push.
{% endalert %}

## Dominios alternativos

Para integrar el push web, tu dominio debe ser [seguro](https://w3c.github.io/webappsec-secure-contexts/), lo que generalmente significa `https`, `localhost` y otras excepciones definidas en [el estándar push del W3C](https://www.w3.org/TR/service-workers/#security-considerations). También necesitarás poder registrar un prestador de servicios en la raíz de tu dominio, o al menos poder controlar las cabeceras HTTP de ese archivo. Este artículo explica cómo integrar Braze Web Push en un dominio alternativo.

### Ejemplos

Si no puedes cumplir todos los criterios descritos en [el estándar push del W3C](https://www.w3.org/TR/service-workers/#security-considerations), puedes utilizar este método para añadir un cuadro de diálogo push a tu sitio web. Esto puede ser útil si quieres que tus usuarios se adhieran voluntariamente desde un sitio web `http` o desde una ventana emergente de una extensión del navegador que impide que se muestre tu mensaje push.

### Consideraciones

Ten en cuenta que, al igual que muchas soluciones en la Web, los navegadores evolucionan continuamente, y este método puede no ser viable en el futuro. Antes de continuar, asegúrate de que

- Posees un dominio seguro independiente (`https://`) y permisos para registrar un prestador de servicios en ese dominio.
- Los usuarios han iniciado sesión en tu sitio web, lo que garantiza que los tokens de notificaciones push coinciden con el perfil correcto.

{% alert important %}
No puedes utilizar este método para implementar notificaciones push para Shopify. Shopify eliminará automáticamente las cabeceras necesarias para entregar push de esta forma.
{% endalert %}

### Configurar un dominio push alternativo

Para que el siguiente ejemplo quede claro, utilizaremos `http://insecure.com` y `https://secure.com` como nuestros dos dominios con el objetivo de conseguir que los visitantes se registren para push en `http://insecure.com`. Este ejemplo también podría aplicarse a un esquema `chrome-extension://` para la página emergente de una extensión del navegador.

#### Paso 1: Iniciar flujo de avisos

En `insecure.com`, abre una nueva ventana a tu dominio seguro utilizando un parámetro URL para pasar el ID externo de Braze del usuario actualmente conectado.

**http://insecure.com**
```html
<button id="opt-in">Opt-In For Push</button>
<script>
// the same ID you would use with `braze.changeUser`:
const user_id = getUserIdSomehow();
// pass the user ID into the secure domain URL:
const secure_url = `https://secure.com/push-registration.html?external_id=${user_id}`;

// when the user takes some action, open the secure URL in a new window
document.getElementById("opt-in").onclick = function(){
    if (!window.open(secure_url, 'Opt-In to Push', 'height=500,width=600,left=150,top=150')) {
        window.alert('The popup was blocked by your browser');
    } else {
        // user is shown a popup window
        // and you can now prompt for push in this window
    }
}
</script>
```

#### Paso 2: Registro para push

En este punto, `secure.com` abrirá una ventana emergente en la que podrás inicializar el SDK Braze Web para el mismo ID de usuario y solicitar el permiso del usuario para el push Web.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

#### Paso 3: Comunicarse entre dominios (opcional)

Ahora que los usuarios pueden adherirse voluntariamente desde este flujo de trabajo originado en `insecure.com`, puede que quieras modificar tu sitio en función de si el usuario ya está adherido o no. No tiene sentido pedir al usuario que se registre en push si ya lo está.

Puedes utilizar iFrames y la API [`postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) para comunicarte entre tus dos dominios. 

**insecure.com**

En nuestro dominio `insecure.com`, pediremos al dominio seguro (donde se registra _realmente_ push) información sobre el registro push del usuario actual:

```html
<!-- Create an iframe to the secure domain and run getPushStatus onload-->
<iframe id="push-status" src="https://secure.com/push-status.html" onload="getPushStatus()" style="display:none;"></iframe>

<script>
function getPushStatus(event){
    // send a message to the iframe asking for push status
    event.target.contentWindow.postMessage({type: 'get_push_status'}, 'https://secure.com');
    // listen for a response from the iframe's domain
    window.addEventListener("message", (event) => {
        if (event.origin === "http://insecure.com" && event.data.type === 'set_push_status') {
            // update the page based on the push permission we're told
            window.alert(`Is user registered for push? ${event.data.isPushPermissionGranted}`);
        }
    }   
}
</script>
```

**secure.com/push-status.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-status.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

## Preguntas más frecuentes (FAQ)

### Prestadores de servicios

#### ¿Qué pasa si no puedo registrar un prestador de servicios en el directorio raíz?

Por defecto, un prestador de servicios sólo puede utilizarse dentro del mismo directorio en el que está registrado. Por ejemplo, si tu archivo de prestador de servicios existe en `/assets/service-worker.js`, sólo sería posible registrarlo en `example.com/assets/*` o en un subdirectorio de la carpeta `assets`, pero no en tu página de inicio (`example.com/`). Por esta razón, se recomienda alojar y registrar el prestador de servicios en el directorio raíz (como `https://example.com/service-worker.js`).

Si no puedes registrar un prestador de servicios en tu dominio raíz, una alternativa es utilizar el encabezado HTTP [`Service-Worker-Allowed`](https://w3c.github.io/ServiceWorker/#service-worker-script-response) al servir el archivo de tu prestador de servicios. Configurando tu servidor para que devuelva `Service-Worker-Allowed: /` en la respuesta para el prestador de servicios, esto indicará al navegador que amplíe el alcance y permita utilizarlo desde un directorio diferente.

#### ¿Puedo crear un prestador de servicios utilizando un administrador de etiquetas?

No, los prestadores de servicios deben estar alojados en el servidor de tu sitio web y no pueden cargarse a través del administrador de etiquetas.

### Seguridad del sitio

#### ¿Se requiere HTTPS?

Sí. Las normas web exigen que el dominio que solicita el permiso de notificación push sea seguro.

#### ¿Cuándo se considera que un sitio es "seguro"?

Un sitio se considera seguro si coincide con uno de los siguientes patrones de origen seguro. Las notificaciones push de la Web Braze se basan en esta norma abierta, por lo que se evitan los ataques de intermediario.

- `(https, , *)`
- `(wss, *, *)`
- `(, localhost, )`
- `(, .localhost, *)`
- `(, 127/8, )`
- `(, ::1/128, *)`
- `(file, *, —)`
- `(chrome-extension, *, —)`

#### ¿Qué pasa si no está disponible un sitio seguro?

Aunque la mejor práctica del sector es hacer que todo tu sitio sea seguro, los clientes que no puedan asegurar el dominio de su sitio pueden eludir el requisito utilizando un modal seguro. Lee más en nuestra guía sobre el uso de [Dominio push alternativo]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/push_notifications/alternate_push_domain) o ve una [demostración en funcionamiento](http://appboyj.com/modal-test.html).
