---
nav_title: Dominio push web alternativo
article_title: Dominio push web alternativo
platform: Web
page_order: 20
page_type: reference
description: "Este artículo explica cómo integrar Braze Web Push en un dominio alternativo."
channel: push

---

# Dominio alternativo de notificación push web

> Para integrar el push web, tu dominio debe ser [seguro](https://w3c.github.io/webappsec-secure-contexts/), lo que generalmente significa `https`, `localhost` y otras excepciones definidas en [el estándar push del W3C](https://www.w3.org/TR/service-workers/#security-considerations). También necesitarás poder registrar un prestador de servicios en la raíz de tu dominio, o al menos poder controlar las cabeceras HTTP de ese archivo. Este artículo explica cómo integrar Braze Web Push en un dominio alternativo.

_Si no puedes cumplir todos esos criterios_, utiliza esta guía para configurar una solución que te permita añadir un diálogo de solicitud push a tu sitio web. Por ejemplo, este artículo sería útil si quieres que el usuario se adhiera voluntariamente desde un sitio web `http` (inseguro) o desde una ventana emergente de una extensión del navegador que impida que se muestre el mensaje push.

## Advertencias
Ten en cuenta que, al igual que muchas soluciones en la Web, los navegadores evolucionan continuamente y, en el futuro, puede que esto no funcione como se pretende.

- Esto requiere lo siguiente:
  - Posees un dominio seguro independiente (`https://`) y tienes acceso para registrar un prestador de servicios en ese dominio.
  - Los usuarios deben iniciar sesión en tu sitio web para garantizar que los tokens de notificaciones push están vinculados a los mismos perfiles.

{% alert note %}
Push para Shopify no puede implementarse de esta forma. Shopify toma medidas para eliminar los encabezados necesarios para entregar notificaciones push.
{% endalert %}

## Integración

Para que el siguiente ejemplo quede claro, utilizaremos `http://insecure.com` y `https://secure.com` como nuestros dos dominios con el objetivo de conseguir que los visitantes se registren para push en `http://insecure.com`. Este ejemplo también podría aplicarse a un esquema `chrome-extension://` para la página emergente de una extensión del navegador.

### Paso 1: Iniciar flujo de avisos

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

### Paso 2: Registro para push

En este punto, `secure.com` abrirá una ventana emergente en la que podrás inicializar el SDK Braze Web para el mismo ID de usuario y solicitar el permiso del usuario para el push Web.

**https://secure.com/push-registration.html**

<script src="{{site.baseurl}}/assets/js/embed.js?target=https%3A%2F%2Fgithub.com%2Fbraze-inc%2Fbraze-web-sdk%2Fblob%2Fmaster%2Fsnippets%2Falternate-push-domain-registration.html&style=github&showBorder=on&showLineNumbers=on&showFileMeta=on&showCopy=on"></script>

### Paso 3: Comunicarse entre dominios (opcional)

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

