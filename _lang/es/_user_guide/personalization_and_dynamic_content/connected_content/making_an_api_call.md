---
nav_title: Realizar una llamada a la API
article_title: Realización de una llamada a la API de contenidos conectados
page_order: 0
description: "Este artículo de referencia explica cómo hacer una llamada a la API de Contenidos conectados y proporciona ejemplos útiles y casos de uso avanzados de Contenidos conectados."
search_rank: 2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"}Hacer una llamada a la API

> Utiliza Contenido conectado para insertar cualquier información accesible mediante API directamente en los mensajes que envíes a los usuarios. Puede extraer contenidos directamente de su servidor web o de API de acceso público.<br><br>En esta página se explica cómo hacer llamadas a la API de Contenidos Conectados, casos de uso avanzados de Contenidos Conectados, gestión de errores y mucho más.

## Envío de una llamada de contenido conectado

{% raw %}

Para enviar una llamada de contenido conectado, utilice la etiqueta `{% connected_content %}`. Con esta etiqueta, puede asignar o declarar variables utilizando `:save`. Se puede hacer referencia a aspectos de estas variables más adelante en el mensaje con [Liquid][2].

Por ejemplo, el siguiente cuerpo de mensaje accederá a la URL `http://numbersapi.com/random/trivia` e incluirá un dato curioso en su mensaje:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is fun some trivia for you!: {{result.text}}
```

### Añadir variables

También puede incluir atributos de perfil de usuario como variables en la cadena URL al realizar solicitudes de Contenido Conectado. 

Por ejemplo, puede tener un servicio web que devuelva contenido basado en la dirección de correo electrónico y el ID de un usuario. Si pasa atributos que contienen caracteres especiales, como la arroba (@), asegúrese de utilizar el filtro Liquid `url_param_escape` para sustituir los caracteres no permitidos en las URL por sus versiones escapadas aptas para URL, como se muestra en el siguiente atributo de dirección de correo electrónico.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Los valores de los atributos deben ir rodeados de `${}` para que funcionen correctamente en nuestra versión de la sintaxis de Liquid.
{% endalert %}

Las solicitudes de contenido conectado sólo admiten solicitudes GET y POST.

## Tratamiento de errores

Si la URL no está disponible y llega a una página 404, Braze mostrará una cadena vacía en su lugar. Si la URL llega a una página HTTP 500 o 502, la URL fallará en la lógica de reintento.

Si el punto final devuelve JSON, puedes detectarlo comprobando si el valor `connected` es nulo, y entonces [anular condicionalmente el mensaje][1]. Braze solo permite URL que se comuniquen a través de los puertos 80 (HTTP) y 443 (HTTPS).

### Detección de host no sano

El Contenido conectado emplea un mecanismo de detección de host no saludable para detectar cuando el host de destino experimenta una alta tasa de lentitud significativa o una sobrecarga que da lugar a tiempos de espera, demasiadas solicitudes u otros resultados que impiden que Braze se comunique correctamente con el punto final de destino. Actúa como salvaguarda para reducir la carga innecesaria que pueda estar causando dificultades al host de destino. También sirve para estabilizar la infraestructura de Braze y mantener velocidades rápidas de mensajería.

Si el host de destino experimenta una alta tasa de lentitud o sobrecarga significativa, Braze detendrá temporalmente las peticiones al host de destino durante un minuto, simulando en su lugar respuestas que indiquen el fallo. Al cabo de un minuto, Braze sondeará la salud del anfitrión utilizando un pequeño número de peticiones antes de reanudar las peticiones a toda velocidad si se comprueba que el anfitrión está sano. Si el anfitrión sigue sin estar sano, Braze esperará otro minuto antes de volver a intentarlo.

Si las peticiones al anfitrión de destino se detienen por el detector de anfitrión insalubre, Braze continuará mostrando mensajes y siguiendo tu lógica Liquid como si hubiera recibido un código de respuesta de error. Si quieres asegurarte de que estas solicitudes de Contenido conectado se reintentan cuando son detenidas por el detector de host insalubre, utiliza la opción `:retry`. Para más información sobre la opción `:retry`, consulta [Reintentos de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Si crees que la detección de host no saludable puede estar causando problemas, ponte en contacto con [el soporte de Braze]({{site.baseurl}}/support_contact/).

{% alert tip %}
Visita [Solución de problemas de webhook y solicitudes de contenido conectado]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) para saber más sobre cómo solucionar los códigos de error más comunes.
{% endalert %}

## Permitir un rendimiento eficiente

Dado que Braze entrega mensajes a una tasa muy rápida, asegúrate de que tu servidor puede gestionar miles de conexiones simultáneas para que los servidores no se sobrecarguen al descargar contenidos. Cuando utilices API públicas, confirma que tu uso no infringe ningún límite de tasa que pueda emplear el proveedor de la API. Braze requiere que el tiempo de respuesta del servidor sea inferior a dos segundos por razones de rendimiento; si el servidor tarda más de dos segundos en responder, el contenido no se insertará.

Los sistemas Braze pueden realizar la misma llamada a la API de contenido conectado más de una vez por destinatario. Esto se debe a que Braze puede necesitar realizar una llamada a la API de contenido conectado para representar la carga útil de un mensaje, y las cargas útiles de los mensajes pueden representarse varias veces por destinatario para validación, lógica de reintento u otros fines internos. Sus sistemas deben ser capaces de tolerar que la misma llamada de Contenido Conectado se realice más de una vez por destinatario.

## Lo que hay que saber

* Braze no cobra por las llamadas a la API y no contarán para tu asignación de puntos de datos.
* Hay un límite de un MB para las respuestas de Contenido conectado.
* Las llamadas a Contenido Conectado se realizarán cuando se envíe el mensaje, excepto en el caso de los mensajes in-app, que realizarán esta llamada cuando se visualice el mensaje.
* Las llamadas de Contenido Conectado no siguen redireccionamientos.

## Tipos de autenticación

### Utilizar la autenticación básica

Si la URL requiere autenticación básica, Braze puede generar una credencial de autenticación básica para que la utilice en su llamada a la API. Puedes gestionar las credenciales de autenticación básica existentes y añadir otras nuevas desde **Configuración** > **Contenido conectado**.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar **Contenido conectado** en **Administrar configuración**.
{% endalert %}

![La configuración de "Contenido conectado" en el panel de Braze.][34]

Para añadir una nueva credencial, selecciona **Añadir credencial**. Dale un nombre a tu credencial e introduce el nombre de usuario y la contraseña.

![La ventana "Crear nuevas credenciales" con la opción de introducir un nombre, un nombre de usuario y una contraseña.][35]{: style="max-width:30%" }

A continuación, puede utilizar esta credencial de autenticación básica en sus llamadas a la API haciendo referencia al nombre del token:

{% raw %}
```
Hi there, here is fun some trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si eliminas una credencial, ten en cuenta que cualquier llamada de Contenido Conectado que intente utilizarla será abortada.
{% endalert %}

### Utilizar la autenticación mediante token

Al utilizar Braze Connected Content, es posible que determinadas API requieran un token en lugar de un nombre de usuario y una contraseña. En la siguiente llamada se incluye un fragmento de código que puede utilizar como referencia y modelo para sus mensajes.

{% raw %}
```
{% assign campaign_name="New Year Sale" %}
{% connected_content
     https://your_API_link_here/
     :method post
     :headers {
       "X-App-Id": "YOUR-APP-ID",
       "X-App-Token": "YOUR-APP-TOKEN"
     }
     :body campaign={{campaign_name}}&customer={{${user_id}}}&channel=Braze
     :content_type application/json
     :save publication
%}
```
{% endraw %}

### Utilizar la autenticación abierta (OAuth)

Algunas configuraciones de la API requieren la obtención de un token de acceso que luego se puede utilizar para autenticar el punto final de la API al que quieres acceder.

#### Paso 1: Recuperar el token de acceso

El siguiente ejemplo ilustra la recuperación y el almacenamiento de un token de acceso en una variable local que puede utilizarse para autenticar la siguiente llamada a la API. Se puede añadir un parámetro `:cache_max_age` para que coincida con el tiempo de validez del token de acceso y reducir el número de llamadas salientes de Connected Content. Consulte [Caché configurable][36] para obtener más información.

{% raw %}
```
{% connected_content
     https://your_API_access_token_endpoint_here/
     :method post
     :headers {
       "Content-Type": "YOUR-CONTENT-TYPE",
       "Authorization": "Bearer YOUR-APP-TOKEN"
     }
     :cache_max_age 900
     :save token_response
%}
```
{% endraw %}

#### Paso 2: Autorizar la API utilizando el token de acceso recuperado

Ahora que el token está guardado, se puede introducir dinámicamente en la siguiente llamada a Contenido conectado para autorizar la solicitud:

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

## Lista de IP permitidas de Contenido conectado

Cuando se envía un mensaje que utiliza contenido conectado desde Braze, los servidores de Braze realizan automáticamente solicitudes de red a los servidores de nuestros clientes o de terceros para recuperar datos. Con las listas de IP permitidas, puedes verificar que las solicitudes de Contenido conectado proceden realmente de Braze, lo que añade una capa adicional de seguridad.

Braze enviará solicitudes de Contenido Conectado desde los siguientes rangos de IP. Los rangos de la lista se añaden automática y dinámicamente a cualquier clave API que haya optado por permitir la inclusión en la lista. 

Braze tiene un conjunto reservado de IPs que se utilizan para todos los servicios, no todos los cuales están activos en un momento dado. Esto está diseñado para que Braze envíe desde un centro de datos diferente o realice tareas de mantenimiento, si es necesario, sin afectar a los clientes. Braze puede utilizar una, un subconjunto o todas las siguientes IP enumeradas al realizar solicitudes de Contenido conectado.

| Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06`, `US-07`: |
|---|
| `23.21.118.191`
| `34.206.23.173`
| `50.16.249.9`
| `52.4.160.214`
| `54.87.8.34`
| `54.156.35.251`
| `52.54.89.238`
| `18.205.178.15`

| Para las instancias `EU-01` y `EU-02`: |
|---|
| `52.58.142.242`
| `52.29.193.121`
| `35.158.29.228`
| `18.157.135.97`
| `3.123.166.46`
| `3.64.27.36`
| `3.65.88.25`
| `3.68.144.188`
| `3.70.107.88`

| Para la instancia `US-08`: |
|---|
| `52.151.246.51`
| `52.170.163.182`
| `40.76.166.157`
| `40.76.166.170`
| `40.76.166.167`
| `40.76.166.161`
| `40.76.166.156`
| `40.76.166.166`
| `40.76.166.160`
| `40.88.51.74`
| `52.154.67.17`
| `40.76.166.80`
| `40.76.166.84`
| `40.76.166.85`
| `40.76.166.81`
| `40.76.166.71`
| `40.76.166.144`
| `40.76.166.145`

## Solución de problemas

Utilice [Webhook.site](https://webhook.site/) para solucionar los problemas de las llamadas de Contenido Conectado. 

1. Cambia la URL en tu llamada a Contenido Conectado por la URL única generada en el sitio.
2. Previsualice y pruebe su campaña o paso de Canvas para ver las solicitudes que llegan a este sitio web.

Con esta herramienta, puede diagnosticar problemas con las cabeceras de la solicitud, el cuerpo de la solicitud y otra información que se envía en la llamada.

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#liquid-usage-use-cases--overview
[16]: [success@braze.com](mailto:success@braze.com)
[34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %}
[35]: {% image_buster /assets/img_archive/basic_auth_token.png %}
[36]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching
