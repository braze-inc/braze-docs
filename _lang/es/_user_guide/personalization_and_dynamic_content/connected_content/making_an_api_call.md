---
nav_title: Hacer una llamada de contenido conectado
article_title: Realización de una llamada a la API de contenido conectado
page_order: 0
description: "Este artículo de referencia explica cómo hacer una llamada a la API de contenido conectado, así como ejemplos útiles y casos de uso avanzados de contenido conectado."
search_rank: 2
---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/connected-content){: style="float:right;width:120px;border:0;" class="noimgborder"} Hacer una llamada a la API de contenido conectado

> Utiliza contenido conectado para insertar cualquier información accesible mediante API directamente en los mensajes que envíes a los usuarios. Puedes extraer contenido directamente de tu servidor web o de API de acceso público.<br><br>En esta página se explica cómo hacer llamadas a la API de contenido conectado, casos de uso avanzados de contenido conectado, tratamiento de errores y más.

## Comprender el volumen de llamadas de contenido conectado

{% alert important %}
Un envío no equivale a una llamada de contenido conectado. Braze no garantiza una relación 1:1 entre los envíos de mensajes y las solicitudes de contenido conectado. El sistema está diseñado para priorizar la representación y entrega correcta de los mensajes por encima de minimizar el número de llamadas. Tus puntos de conexión deben estar preparados para gestionar más solicitudes que el número de destinatarios o mensajes enviados.
{% endalert %}

Braze puede realizar la misma llamada a la API de contenido conectado más de una vez por destinatario. Las razones más comunes incluyen:

- **Correo electrónico con múltiples partes:** Un solo correo electrónico puede desencadenar pases de representación separados para el cuerpo HTML, el cuerpo de texto plano y la versión de páginas móviles aceleradas (AMP) (si está presente). Cada pase puede desencadenar contenido conectado en esa parte, por lo que un destinatario puede generar múltiples llamadas idénticas o similares.
- **Validación y reintentos:** Las cargas útiles de los mensajes pueden representarse varias veces por destinatario para validación, lógica de reintento u otros fines internos.
- **Comportamiento del canal:** El contenido conectado se ejecuta cuando se representa el mensaje. Para los mensajes dentro de la aplicación, el mensaje se representa en el momento de la impresión.

Si ves más llamadas de contenido conectado en tus registros que envíos o destinatarios, ese comportamiento es esperado. Para orientación sobre cómo reducir la carga y planificar la escalabilidad, consulta [Mejores prácticas para puntos de conexión de alto volumen](#best-practices-for-high-volume-endpoints).

## Envío de una llamada de contenido conectado

{% raw %}

Para enviar una llamada de contenido conectado, utiliza la etiqueta `{% connected_content %}`. Con esta etiqueta, puedes asignar o declarar variables utilizando `:save`. Se puede hacer referencia a aspectos de estas variables más adelante en el mensaje con [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid).

Por ejemplo, el siguiente cuerpo de mensaje accederá a la URL `http://numbersapi.com/random/trivia` e incluirá un dato curioso en tu mensaje:

```
{% connected_content http://numbersapi.com/random/trivia :save result %}
Hi there, here is some fun trivia for you!: {{result.text}}
```

### Añadir variables

También puedes incluir atributos de perfil de usuario como variables en la cadena URL al realizar solicitudes de contenido conectado. 

Por ejemplo, puedes tener un servicio web que devuelva contenido basado en la dirección de correo electrónico y el ID de un usuario. Si pasas atributos que contienen caracteres especiales, como la arroba (@), asegúrate de utilizar el filtro Liquid `url_param_escape` para sustituir los caracteres no permitidos en las URL por sus versiones escapadas aptas para URL, como se muestra en el siguiente atributo de dirección de correo electrónico.

```
Hi, here are some articles that you might find interesting:

{% connected_content http://www.yourwebsite.com/articles?email={{${email_address} | url_param_escape}}&user_id={{${user_id}}} %}
```
{% endraw %}
{% alert note %}
Los valores de los atributos deben ir rodeados de `${}` para que funcionen correctamente en nuestra versión de la sintaxis de Liquid.
{% endalert %}

Las solicitudes de contenido conectado solo admiten solicitudes GET y POST.

## Tratamiento de errores

Si la URL no está disponible y llega a una página 404, Braze mostrará una cadena vacía en su lugar. Si la URL llega a una página HTTP 500 o 502, la URL fallará en la lógica de reintento.

Si el punto de conexión devuelve JSON, puedes detectarlo comprobando si el valor `connected` es nulo, y entonces [anular condicionalmente el mensaje]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content/). Braze solo permite URL que se comuniquen a través de los puertos 80 (HTTP) y 443 (HTTPS).

### Detección de host no saludable

El contenido conectado emplea un mecanismo de detección de host no saludable para detectar cuando el host de destino experimenta una alta tasa de lentitud o sobrecarga significativa, lo que provoca tiempos de espera, demasiadas solicitudes u otros resultados que impiden que Braze se comunique correctamente con el punto de conexión de destino. Actúa como salvaguarda para reducir la carga innecesaria que pueda estar causando dificultades al host de destino. También sirve para estabilizar la infraestructura de Braze y mantener velocidades rápidas de mensajería.

Si el host de destino experimenta una alta tasa de lentitud o sobrecarga significativa, Braze detendrá temporalmente las solicitudes al host de destino durante un minuto, simulando en su lugar respuestas que indiquen el fallo. Al cabo de un minuto, Braze sondeará la salud del host utilizando un pequeño número de solicitudes antes de reanudar las solicitudes a toda velocidad si se comprueba que el host está sano. Si el host sigue sin estar sano, Braze esperará otro minuto antes de volver a intentarlo.

Si las solicitudes al host de destino se detienen por el detector de host no saludable, Braze continuará representando mensajes y siguiendo tu lógica Liquid como si hubiera recibido un código de respuesta de error. Si quieres asegurarte de que estas solicitudes de contenido conectado se reintentan cuando son detenidas por el detector de host no saludable, utiliza la opción `:retry`. Para más información sobre la opción `:retry`, consulta [Reintentos de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries).

Si crees que la detección de host no saludable puede estar causando problemas, ponte en contacto con [soporte de Braze]({{site.baseurl}}/support_contact/).

{% alert note %}
Puedes incluir en la lista de permitidos URL específicas para utilizarlas con contenido conectado. Para acceder a esta característica, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

{% alert tip %}
Visita [Solución de problemas de solicitudes de webhook y contenido conectado]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors#unhealthy-host-detection) para saber más sobre cómo solucionar los códigos de error más comunes.
{% endalert %}

### Límites de velocidad (429) frente a detección de host no saludable

Los siguientes son mecanismos diferentes:

- **429 Too Many Requests:** Tu punto de conexión (o un servicio ascendente) está devolviendo esta respuesta. Significa que tu servidor o middleware está rechazando tráfico, a menudo porque tiene su propio límite de velocidad. Braze no aplica un límite de velocidad separado al contenido conectado; el volumen de solicitudes de contenido conectado escala directamente con tu [límite de velocidad de entrega de mensajes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting). Dado que los mensajes pueden representarse varias veces por destinatario (por ejemplo, para HTML de correo electrónico, texto plano y AMP), el número de solicitudes de contenido conectado puede superar ese límite de velocidad; no asumas que será menor o igual a los mensajes por minuto que configures. Si ves errores 429, escala tu punto de conexión o middleware para gestionar el volumen de solicitudes esperado, o reduce el límite de velocidad de la campaña o paso en Canvas para que se envíen menos mensajes (y por tanto menos llamadas de contenido conectado) por minuto.
- **Detección de host no saludable:** Una salvaguarda del lado de Braze que se activa tras una alta tasa y volumen de *fallos* en una ventana de un minuto. El recuento de fallos incluye los códigos de estado `408`, `429`, `502`, `503`, `504` y `529`. Cuando se activa, Braze detiene temporalmente las solicitudes a ese host y simula una respuesta de fallo. Esto es independiente de tu propio límite de velocidad. Para los umbrales de detección y más detalles, consulta [Solución de problemas de solicitudes de webhook y contenido conectado]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/#unhealthy-host-detection). Para evitar activar la detección de host no saludable, asegúrate de que tu punto de conexión pueda gestionar el volumen de llamadas descrito en [Comprender el volumen de llamadas de contenido conectado](#understanding-connected-content-call-volume) y [Mejores prácticas para puntos de conexión de alto volumen](#best-practices-for-high-volume-endpoints).

## Permitir un rendimiento eficiente

Dado que Braze entrega mensajes a una tasa muy rápida, asegúrate de que tu servidor pueda gestionar miles de conexiones simultáneas para que no se sobrecargue al descargar contenido. Cuando utilices API públicas, confirma que tu uso no infringe ningún límite de velocidad que pueda emplear el proveedor de la API. Braze requiere que el tiempo de respuesta del servidor sea inferior a dos segundos por razones de rendimiento; si el servidor tarda más de dos segundos en responder, el contenido no se insertará.

Para más información sobre la planificación de la capacidad de los puntos de conexión y la reducción del volumen de llamadas, consulta [Mejores prácticas para puntos de conexión de alto volumen](#best-practices-for-high-volume-endpoints).

## Lo que hay que saber

* Braze no cobra por las llamadas a la API y no contarán para tu uso de puntos de datos.
* Hay un límite de 1 MB para las respuestas de contenido conectado.
* El contenido conectado se ejecuta cuando se representa el mensaje. Para los mensajes dentro de la aplicación, el mensaje se representa en el momento de la impresión.
* Las llamadas de contenido conectado no siguen redireccionamientos.

## Mejores prácticas para puntos de conexión de alto volumen

Si tus mensajes utilizan contenido conectado y envías a alto volumen, planifica más solicitudes que el número de destinatarios o envíos:

1. **Estima la carga máxima:** Utiliza un multiplicador conservador al dimensionar tu punto de conexión o middleware: las solicitudes de contenido conectado pueden superar el número de destinatarios o mensajes enviados. Por ejemplo, para correo electrónico un solo destinatario puede generar múltiples llamadas (HTML, texto plano y AMP), por lo que destinatarios × 2 o × 3 se utiliza a menudo como estimación conservadora.
2. **Utiliza caché cuando sea apropiado:** Las solicitudes GET se almacenan en caché de forma predeterminada. Para solicitudes POST, añade `:cache_max_age` cuando la respuesta pueda reutilizarse durante un período (por ejemplo, un token o contenido que no cambia por solicitud). Consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/) y las [preguntas frecuentes sobre caché POST](#what-is-caching-behavior) a continuación.
3. **Configura el límite de velocidad de entrega:** El [límite de velocidad de entrega]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) en campañas o pasos en Canvas es la única palanca para limitar indirectamente el volumen de solicitudes de contenido conectado: Braze no limita la velocidad del contenido conectado en sí. Es solo un proxy, y no uno perfecto, porque las solicitudes de contenido conectado no son 1:1 con los mensajes. Úsalo para mantener el volumen de mensajes (y por tanto de contenido conectado) dentro de lo que tu punto de conexión pueda gestionar.
4. **Diseña para idempotencia y reintentos:** Braze puede llamar a tu punto de conexión más de una vez por destinatario. Asegúrate de que tu punto de conexión pueda tolerar solicitudes duplicadas sin efectos secundarios incorrectos.

## Tipos de autenticación

### Utilizar la autenticación básica

Si la URL requiere autenticación básica, Braze puede almacenar una credencial de autenticación básica para que la utilices en tu llamada a la API. Puedes administrar las credenciales de autenticación básica existentes y añadir otras nuevas en **Configuración** > **Contenido conectado**.

![La configuración del contenido conectado en el panel de Braze.]({% image_buster /assets/img/connected_content/basic_auth_mgmt.png %})

Para añadir una nueva credencial, selecciona **Añadir credencial** > **Autenticación básica**. 

![Desplegable "Añadir credencial" con la opción de utilizar autenticación básica o autenticación por token.]({% image_buster /assets/img/connected_content/add_credential_button.png %}){: style="max-width:60%"}

Dale un nombre a tu credencial e introduce el nombre de usuario y la contraseña.

![La ventana "Crear nueva credencial" con la opción de introducir un nombre, un nombre de usuario y una contraseña.]({% image_buster /assets/img/connected_content/basic_auth_token.png %}){: style="max-width:60%"}

A continuación, puedes utilizar esta credencial de autenticación básica en tus llamadas a la API haciendo referencia al nombre del token:

{% raw %}
```
Hi there, here is some fun trivia for you!: {% connected_content https://yourwebsite.com/random/trivia :basic_auth credential_name %}
```
{% endraw %}

{% alert note %}
Si eliminas una credencial, ten en cuenta que cualquier llamada de contenido conectado que intente utilizarla será abortada.
{% endalert %}

### Utilizar la autenticación por token

Al utilizar contenido conectado de Braze, es posible que determinadas API requieran un token en lugar de un nombre de usuario y una contraseña. Braze también puede almacenar credenciales que contengan valores de encabezado de autenticación por token.

Para añadir una credencial que contenga valores de token, selecciona **Añadir credencial** > **Autenticación por token**. A continuación, añade los pares clave-valor para tus encabezados de llamada a la API y el dominio permitido.

![Un ejemplo de token "token_credential_abc" con los detalles de autenticación por token.]({% image_buster /assets/img/connected_content/token_auth.png %}){: style="max-width:60%"}

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

Algunas configuraciones de la API requieren la obtención de un token de acceso que luego se puede utilizar para autenticar el punto de conexión de la API al que quieres acceder.

#### Paso 1: Recuperar el token de acceso

El siguiente ejemplo ilustra la recuperación y almacenamiento de un token de acceso en una variable local, que puede utilizarse para autenticar la llamada a la API subsiguiente. Se puede añadir un parámetro `:cache_max_age` para que coincida con el tiempo de validez del token de acceso y reducir el número de llamadas salientes de contenido conectado. Para más información, consulta [Caché configurable]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/local_connected_content_variables/#configurable-caching).

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

#### Paso 2: Autorizar la API utilizando el token de acceso recuperado

Una vez guardado el token, puede introducirse dinámicamente en la siguiente llamada de contenido conectado para autorizar la solicitud:

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
- Para la autenticación por token, puedes actualizar los pares clave-valor del encabezado y el dominio permitido. Ten en cuenta que los valores de encabezado configurados anteriormente no serán visibles.

![La opción de editar credenciales.]({% image_buster /assets/img/connected_content/edit_credentials.png %}){: style="max-width:60%"}

## Lista de IP permitidas de contenido conectado

Cuando se envía un mensaje que utiliza contenido conectado desde Braze, los servidores de Braze realizan automáticamente solicitudes de red a los servidores de nuestros clientes o de terceros para recuperar datos. Con las listas de IP permitidas, puedes verificar que las solicitudes de contenido conectado proceden realmente de Braze, lo que añade una capa de seguridad.

Braze enviará solicitudes de contenido conectado desde los siguientes rangos de IP. Los rangos enumerados se añaden automática y dinámicamente a cualquier clave de API que haya sido incluida en la lista de permitidos. 

Braze tiene un conjunto reservado de IP que se utilizan para todos los servicios, no todos los cuales están activos en un momento dado. Esto está diseñado para que Braze pueda enviar desde un centro de datos diferente o realizar tareas de mantenimiento, si es necesario, sin afectar a los clientes. Braze puede utilizar una, un subconjunto o todas las siguientes IP enumeradas al realizar solicitudes de contenido conectado.

{% multi_lang_include data_centers.md datacenters='ips' %}

### Encabezado `User-Agent`

Braze incluye un encabezado `User-Agent` en todas las solicitudes de contenido conectado y webhook que es similar al siguiente:

```text
Braze Sender 75e404755ae1270441f07eb238f0faf25e44dfdc
```

{% alert tip %}
Ten en cuenta que el valor hash cambia regularmente. Si estás filtrando el tráfico por `User-Agent`, permite todos los valores que empiecen por `Braze Sender`.
{% endalert %}

## Solución de problemas

Utiliza [Webhook.site](https://webhook.site/) para solucionar los problemas de tus llamadas de contenido conectado. 

1. Cambia la URL en tu llamada de contenido conectado por la URL única generada en el sitio.
2. Previsualiza y prueba tu campaña o paso en Canvas para ver las solicitudes que llegan a este sitio web.

Con esta herramienta, puedes diagnosticar problemas con los encabezados de la solicitud, el cuerpo de la solicitud y otra información que se envía en la llamada.

## Preguntas frecuentes

### ¿Por qué hay más llamadas de contenido conectado que usuarios o envíos? 

Este es un comportamiento esperado. Braze puede realizar la misma llamada a la API de contenido conectado más de una vez por destinatario porque las cargas útiles de los mensajes pueden representarse varias veces (por ejemplo, para HTML de correo electrónico, texto plano y AMP; para validación o lógica de reintento; u otros fines internos). No hay una relación garantizada 1:1 entre envíos y llamadas de contenido conectado. Consulta [Comprender el volumen de llamadas de contenido conectado](#understanding-connected-content-call-volume) y [Mejores prácticas para puntos de conexión de alto volumen](#best-practices-for-high-volume-endpoints) para más detalles y mitigación.

### ¿Cómo funciona el límite de velocidad con el contenido conectado?

El contenido conectado no tiene su propio límite de velocidad. En cambio, el límite de velocidad se basa en la tasa de envío de mensajes. Te recomendamos que configures el límite de velocidad de mensajería por debajo del límite de velocidad previsto para tu contenido conectado si hay más llamadas de contenido conectado que mensajes enviados.  

### ¿Cuál es el comportamiento de caché?

Las solicitudes GET se almacenan en caché de forma predeterminada (consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/)). **Las solicitudes POST no se almacenan en caché de forma predeterminada**, pero puedes habilitar el almacenamiento en caché añadiendo `:cache_max_age` a la llamada de contenido conectado. Esto puede reducir la carga del punto de conexión cuando la misma solicitud POST (por ejemplo, una solicitud de token o contenido) se realizaría repetidamente dentro de la ventana de caché.

{% raw %}
```liquid
{% connected_content https://api.example.com/token :method post :body grant_type=client_credentials :cache_max_age 900 :save token %}
```
{% endraw %}

El almacenamiento en caché puede ayudar a reducir las llamadas duplicadas de contenido conectado, pero no se garantiza que resulte en una única llamada por usuario. La duración de la caché es de entre cinco minutos y cuatro horas. Para más detalles, consulta [Almacenamiento en caché de respuestas]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/caching_responses/).

### ¿Cuál es el comportamiento HTTP predeterminado de contenido conectado? 

{% multi_lang_include connected_content.md section='default behavior' %}

{% multi_lang_include connected_content.md section='http post' %}