---
nav_title: Hacer una llamada de contenido conectado
article_title: Hacer una llamada a la API de contenido conectado
page_order: 0
description: "Este artículo de referencia explica cómo hacer una llamada a la API de Contenidos Conectados, así como ejemplos útiles y casos de uso avanzados de Contenidos Conectados."
search_rank: 2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"} Hacer una llamada a la API de contenido conectado

> Utiliza Contenido conectado para insertar cualquier información accesible mediante API directamente en los mensajes que envíes a los usuarios. Puedes extraer contenidos directamente de tu servidor Web o de API de acceso público.<br><br>En esta página se explica cómo hacer llamadas a la API de Contenidos Conectados, casos de uso avanzados de Contenidos Conectados, gestión de errores y mucho más.

## Envío de una llamada de contenido conectado

{% raw %}

Para enviar una llamada de Contenido conectado, utiliza la etiqueta `{% connected_content %}`. Con esta etiqueta, puedes asignar o declarar variables utilizando `:save`. Se puede hacer referencia a aspectos de estas variables más adelante en el mensaje con [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

Por ejemplo, el siguiente cuerpo de mensaje accederá a la URL `http://numbersapi.com/random/trivia` e incluirá un dato curioso en tu mensaje:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Añadir variables

También puedes incluir atributos del perfil de usuario como variables en la cadena URL cuando hagas solicitudes de Contenido conectado. 

Por ejemplo, puedes tener un servicio Web que devuelva contenido basado en la dirección de correo electrónico y el ID de un usuario. Si pasas atributos que contienen caracteres especiales, como la arroba (@), asegúrate de utilizar el filtro Liquid `url_param_escape` para sustituir los caracteres no permitidos en las URL por sus versiones escapadas aptas para URL, como se muestra en el siguiente atributo de dirección de correo electrónico.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Los valores de los atributos deben ir rodeados de `${}` para que funcionen correctamente en nuestra versión de la sintaxis Liquid.
{% endalert %}

Las solicitudes de Contenido conectado sólo admiten solicitudes GET y POST.

## Tratamiento de errores

Si la URL no está disponible y llega a una página 404, Braze mostrará una cadena vacía en su lugar. Si la URL llega a una página HTTP 500 o 502, la URL fallará en la lógica de reintento.

Si el endpoint devuelve JSON, puedes detectarlo comprobando si el valor `connected` es nulo, y entonces [abortar condicionalmente el mensaje]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/). Braze sólo permite URLs que se comuniquen a través de los puertos 80 (HTTP) y 443 (HTTPS).

### Detección de host no sano

El contenido conectado emplea un mecanismo de detección de host no saludable para detectar cuando el host de destino experimenta una alta tasa de lentitud o sobrecarga significativa, lo que provoca tiempos de espera, demasiadas solicitudes u otros resultados que impiden que Braze se comunique correctamente con el punto final de destino. Actúa como salvaguarda para reducir la carga innecesaria que pueda estar causando dificultades al host de destino. También sirve para estabilizar la infraestructura de Braze y mantener velocidades rápidas de mensajería.

Si el host de destino experimenta una alta tasa de lentitud o sobrecarga significativa, Braze detendrá temporalmente las peticiones al host de destino durante un minuto, simulando en su lugar respuestas que indiquen el fallo. Al cabo de un minuto, Braze sondeará la salud del anfitrión utilizando un pequeño número de peticiones antes de reanudar las peticiones a toda velocidad si se comprueba que el anfitrión está sano. Si el anfitrión sigue sin estar sano, Braze esperará otro minuto antes de volver a intentarlo.

Si las peticiones al anfitrión de destino se detienen por el detector de anfitrión insalubre, Braze continuará mostrando mensajes y siguiendo tu lógica Liquid como si hubiera recibido un código de respuesta de error. Si quieres asegurarte de que estas solicitudes de Contenido conectado se reintentan cuando son detenidas por el detector de host insalubre, utiliza la opción `:retry`. Para más información sobre la opción `:retry`, consulta [Reintentos de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Si crees que la detección de host no saludable puede estar causando problemas, ponte en contacto con [el soporte de Braze]({{site.baseurl}}/support_contact/).

{% alert tip %}
Visita [Solución de problemas de webhook y solicitudes de contenido conectado]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) para saber más sobre cómo solucionar los códigos de error más comunes.
{% endalert %}

## Permitir un rendimiento eficiente

Dado que Braze entrega mensajes a una tasa muy rápida, asegúrate de que tu servidor puede gestionar miles de conexiones simultáneas para que los servidores no se sobrecarguen al descargar contenidos. Cuando utilices API públicas, confirma que tu uso no infringe ningún límite de tasa que pueda emplear el proveedor de la API. Braze requiere que el tiempo de respuesta del servidor sea inferior a dos segundos por razones de rendimiento; si el servidor tarda más de dos segundos en responder, el contenido no se insertará.

Los sistemas Braze pueden realizar la misma llamada a la API de contenido conectado más de una vez por destinatario. Esto se debe a que Braze puede necesitar hacer una llamada a la API de contenido conectado para representar la carga útil de un mensaje, y las cargas útiles de los mensajes pueden representarse varias veces por destinatario para validación, lógica de reintento u otros fines internos. Tus sistemas deben poder tolerar que la misma llamada de contenido conectado se realice más de una vez por destinatario.

## Lo que debes saber

* Braze no cobra por las llamadas a la API y no contarán para tu uso de punto de datos.
* Hay un límite de 1 MB para las respuestas de Contenido conectado.
* Las llamadas a Contenido conectado se producirán cuando se envíe el mensaje, excepto en el caso de los mensajes dentro de la aplicación, que realizarán esta llamada cuando se visualice el mensaje.
* Las llamadas de contenido conectado no siguen las redirecciones.

## Tipos de autenticación

### Utilizar la autenticación básica

Si la URL requiere autenticación básica, Braze puede almacenar una credencial de autenticación básica para que la utilices en tu llamada a la API. Puedes administrar las credenciales de autenticación básica existentes y añadir otras nuevas en **Configuración** > **Contenido** conectado **.**

\![La configuración del Contenido conectado en el panel de Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Para añadir una nueva credencial, selecciona **Añadir credencial** > **Autenticación básica**. 

\!["Añadir credenciales" desplegable con la opción de utilizar autenticación básica o autenticación token.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Dale un nombre a tu credencial e introduce el nombre de usuario y la contraseña.

\![La ventana "Crear nueva credencial" con la opción de introducir un nombre, un nombre de usuario y una contraseña.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

A continuación, puedes utilizar esta credencial de autenticación básica en tus llamadas a la API haciendo referencia al nombre del token:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si eliminas una credencial, ten en cuenta que se abortará cualquier llamada de Contenido conectado que intente utilizarla.
{% endalert %}

### Utilizar la autenticación por token

{% alert important %}
El tipo de credenciales de autenticación token está actualmente en acceso temprano. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

Al utilizar el contenido conectado Braze, es posible que determinadas API requieran un token en lugar de un nombre de usuario y una contraseña. Braze también puede almacenar credenciales que contengan valores de encabezado de autenticación de token.

Para añadir una credencial que contenga valores token, selecciona **Añadir credencial** > **Autenticación token**. A continuación, añade los pares clave-valor para tus cabeceras de llamada a la API y el dominio permitido.

\![Un ejemplo de token "token_credential_abc" con los detalles de autentificación del token.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

A continuación, puedes utilizar esta credencial en tus llamadas a la API haciendo referencia al nombre de la credencial:

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://api.endpoint.com/your_path
     :method post
     :auth_credentials token_credential_abc
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Utilizar la autenticación abierta (OAuth)

Algunas configuraciones de la API requieren la obtención de un token de acceso que luego se puede utilizar para autenticar el punto final de la API al que quieres acceder.

#### Paso 1: Recuperar el token de acceso

El siguiente ejemplo ilustra la recuperación y almacenamiento de un token de acceso en una variable local, que puede utilizarse para autenticar la llamada a la API subsiguiente. Se puede añadir un parámetro `:cache_max_age` para que coincida con el tiempo de validez del token de acceso y reducir el número de llamadas salientes de Contenido conectado. Para más información, consulta [Caché configurable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching).

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :auth_credentials access_token_credential_abc
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Paso 2: Autoriza la API utilizando el token de acceso recuperado

Una vez guardado el token, puede introducirse dinámicamente en la siguiente llamada a Contenido conectado para autorizar la solicitud:

{% raw %}
```
{% connected_content
     https://your_API_endpoint_here/
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "{{token_response}}"
     }
     :body key1=value1&key2=value2
     :save response
%}
```
{% endraw %}

### Edición de credenciales

Puedes editar el nombre de las credenciales para los tipos de autenticación.

- Para la autenticación básica, puedes actualizar el nombre de usuario y la contraseña. Ten en cuenta que la contraseña introducida anteriormente no será visible.
- Para la autenticación con token, puedes actualizar los pares clave-valor del encabezamiento y el dominio permitido. Ten en cuenta que los valores de cabecera configurados anteriormente no serán visibles.

\![La opción de editar credenciales.]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## Contenido conectado Lista de IP permitidas

Cuando se envía desde Braze un mensaje que utiliza Contenido conectado, los servidores Braze realizan automáticamente solicitudes de red a los servidores de nuestros clientes o de terceros para recuperar datos. Con las listas de IP permitidas, puedes verificar que las solicitudes de contenido conectado proceden realmente de Braze, lo que añade una capa adicional de seguridad.

Braze enviará solicitudes de Contenido conectado desde los siguientes rangos de IP. Los rangos enumerados se añaden automática y dinámicamente a cualquier clave de API que haya sido objeto de adhesión voluntaria a la lista permitida. 

Braze tiene un conjunto reservado de IPs utilizadas para todos los servicios, no todas las cuales están activas en un momento dado. Esto está diseñado para que Braze pueda enviar desde un centro de datos diferente o realizar tareas de mantenimiento, si es necesario, sin afectar a los clientes. Braze puede utilizar una, un subconjunto o todas las siguientes IP enumeradas al realizar solicitudes de Contenido conectado.

{% multi_lang_include data_centers.md datacenters='ips' %}

### `User-Agent` cabecera

Braze incluye un encabezado `User-Agent` en todas las solicitudes de Contenido conectado y webhook que es similar al siguiente:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Ten en cuenta que el valor hash cambia regularmente. Si estás filtrando el tráfico por `User-Agent`, permite todos los valores que empiecen por `Braze Sender`.
{% endalert %}

## Solución de problemas

Utiliza [Webhook.site](https://webhook.site/) para solucionar los problemas de tus llamadas de Contenido conectado. 

1. Cambia la URL de tu llamada a Contenido conectado por la URL única generada en el sitio.
2. Vista previa y prueba tu campaña o paso en Canvas para ver las solicitudes que llegan a este sitio web.

Con esta herramienta, puedes diagnosticar problemas con los encabezados de solicitud, el cuerpo de la solicitud y otra información que se envía en la llamada.

## Preguntas más frecuentes

### ¿Por qué hay más llamadas de Contenido conectado que usuarios o envíos? 

Braze puede hacer la misma llamada a la API de contenido conectado más de una vez por destinatario porque puede que necesitemos hacer una llamada a la API de contenido conectado para representar la carga útil de un mensaje. Las cargas útiles de los mensajes se pueden representar varias veces por destinatario para validación, lógica de reintento u otros fines internos.

Se espera que una llamada a la API de contenido conectado pueda hacerse más de una vez por destinatario, aunque no se utilice la lógica de reintento en la llamada. Te recomendamos que establezcas el límite de velocidad de los mensajes que contengan Contenido conectado o que configures tus servidores para que puedan gestionar mejor el volumen previsto.

### ¿Cómo funciona el límite de velocidad con el contenido conectado?

El contenido conectado no tiene su propio límite de velocidad. En cambio, el límite de velocidad se basa en la tasa de envío de mensajes. Te recomendamos que configures el límite de velocidad de mensajería por debajo del límite de velocidad de tu Contenido conectado si hay más llamadas de Contenido conectado que mensajes enviados.  

### ¿Qué es el comportamiento en caché?

Por predeterminado, las peticiones POST no se almacenan en caché. Sin embargo, puedes añadir el parámetro `:cache_max_age` para forzar la llamada POST a la caché.

El almacenamiento en caché puede ayudar a reducir las llamadas duplicadas de Contenido conectado. Sin embargo, no está garantizado que siempre resulte en una única llamada de Contenido conectado por usuario.

### ¿Cuál es el comportamiento predeterminado HTTP de Contenido conectado? 

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}
