---
nav_title: Obtención de datos a través del Contenido conectado
article_title: Obtención de datos a través de Contenido conectado con Voucherify
page_order: 2
alias: /partners/voucherify/connected_content/
description: "Este artículo de referencia describe cómo puedes obtener datos de la API de Voucherify a través de los scripts de contenido conectado de Braze y enviar mensajes a segmentos específicos de Braze."
page_type: partner
search_tag: Partner
---

# Obtención de datos a través del Contenido conectado

> Con el contenido conectado Braze, puedes obtener datos de la API de Voucherify y enviar mensajes a segmentos específicos de Braze. Este artículo de referencia te mostrará cómo configurar los scripts de Contenido conectado para publicar cupones de Voucherify, invitar a nuevos referidos, recuperar el saldo de las tarjetas de fidelización y mucho más.

_Esta integración es mantenida por Voucherify._

## Sobre la integración

El esquema básico del guion es el siguiente:
{% raw %}
```json
{% connected content
  "voucherify-API-ENDPOINT-url"
  :method post
  :headers {
    "X-App-Id": "Voucherify-API-key",
    "X-App-Token": "Voucherify-Secret-key",
  }
  :content_type application/json
  :retry
  :save {{result_variable}}
}
```
{% endraw %}

Visita el [repositorio GitHub](https://github.com/voucherifyio/braze-connected-content) de Voucherify para ver ejemplos de scripts de Contenido conectado.

## Configuración de seguridad

Sin la siguiente configuración, cada vez que se desencadene un mensaje de Contenido conectado, se llamará a la API de Voucherify al menos dos veces. Estas configuraciones reducen el número de llamadas a la API facturadas a Braze y reducen el riesgo de alcanzar el límite de bloqueo duro de la API, que puede interrumpir la entrega de mensajes.

{% tabs %}
{% tab Limitador de velocidad %}

**Limitador de velocidad**

Asegúrate de [limitar el número de mensajes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) enviados por Braze por minuto. Esto asegura tanto la API de Braze como la de Voucherify para que no reciban demasiado tráfico de tu campaña. Cuando te dirijas a los usuarios durante la configuración de la campaña, limita la tasa de envío a 500 mensajes por minuto.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

{% endtab %}
{% tab Almacenamiento en caché %}

**Almacenamiento en caché en llamadas POST**

Las llamadas a Contenido conectado realizadas mediante HTTP POST no se almacenan en caché por predeterminado y realizarán dos solicitudes a la API por cada código publicado. Este comportamiento puede forzar los límites de tu API. El mecanismo de almacenamiento en caché te permitirá limitarlo a una llamada a la API por publicación de cupón. 

{% alert important %}
Todos los ejemplos de Contenido conectado de este tutorial incluyen el almacenamiento en caché predeterminado para reducir el número de llamadas a la API desencadenadas por Braze.
{% endalert %}

Para añadir caché a las llamadas POST:

1. Añade un atributo {% raw %}`:cache_max_age`{% endraw %}. Por defecto, la duración de la caché es de 5 minutos. Puedes personalizar la duración en segundos. Se puede ajustar entre 5 minutos y 4 horas. Ejemplo: {% raw %}`:cache_max_age 3600`{% endraw %} almacenará en caché durante 1 hora.
2. Proporciona una clave de caché {% raw %}`cache_id={{cache_id}}`{% endraw %} en el parámetro de consulta del punto final de destino para que Braze pueda identificar una publicación única. Primero, define la variable y luego añade la cadena de consulta única a tu punto final. Esto diferenciará cada publicación por el {% raw %}`source_id`{% endraw %}.

![]({% image_buster /assets/img/voucherify/voucherify_cc_cache.png %})

_Nota las consecuencias:_ Braze almacena en caché las llamadas a la API en función de la URL. Voucherify ignora la cadena única utilizada como parámetro de consulta, pero distingue las diferentes solicitudes de API para Braze y permite almacenar en caché cada intento único por separado. Sin ese parámetro de consulta, todos los clientes recibirán el mismo código de cupón para la duración de la caché.

{% endtab %}
{% tab Atributo de reintento %}

**Atributo de reintento**

El contenido conectado no valida la respuesta de Voucherify, por lo que recomendamos además añadir un atributo [de reintento]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries) en la secuencia de comandos del contenido conectado. La lógica del Contenido conectado intentará reintentarlo cinco veces antes de abortar el mensaje (respetará el límite de velocidad). Este método ayudará a evitar casos de publicación de código fallida cuando se tarde un poco más en obtener los datos de Voucherify.

Si no utilizas {% raw %}`:retry`{% endraw %}, independientemente de la respuesta devuelta por Voucherify, Braze intentará enviar la distribución, lo que puede dar lugar a la generación de correos electrónicos sin código publicado.

![]({% image_buster /assets/img/voucherify/voucherify_cc_retry.png %})

{% endtab %}
{% tab Publicaciones únicas %}

**Publicación única por cliente**

El parámetro {% raw %}`source_id`{% endraw %} del cuerpo del script establece que cada cliente sólo puede recibir un código único en una única campaña Braze. Como resultado, aunque Braze multiplique involuntariamente la solicitud, cada usuario recibirá el mismo código único que se le publicó en el primer mensaje.

![]({% image_buster /assets/img/voucherify/voucherify_cc_sourceId_unique_publication.png %})

Puedes modificar {% raw %}`{{source_id}}`{% endraw %} y su efecto en las publicaciones utilizando las siguientes configuraciones:

| Configuración | Efecto |
| ------------- | ------ |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} | Los clientes de un mismo envío utilizarán la misma publicación. |
| {% raw %}`{{campaign.${api_id}}}`{% endraw %} | Todos los clientes de una misma campaña utilizarán la misma publicación. |
| {% raw %}`{{${user_id}}}`{% endraw %} o {% raw %}`{{${braze_id}}}`{% endraw %} | Comprueba que cada cliente utilizará la misma publicación independientemente de la campaña que se envíe (puedes utilizar {% raw %}`${user_id}`{% endraw %} que es un {% raw %}`external_id`{% endraw %} y {% raw %}`${braze_id}`{% endraw %} que es un ID interno). |
| {% raw %}`{{campaign.${dispatch_id}}}`{% endraw %} y {% raw %}`{{campaign.${user_id}}}`{% endraw %} | Cada cliente de un mismo envío utilizará la misma publicación única. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Únete una vez %}

**Únete una vez**

Si tu campaña de Voucherify tiene un límite _Los clientes sólo pueden unirse una vez_, elimina el ID de la fuente de publicación del cuerpo del script. Voucherify confirmará que cada mensaje Braze al mismo cliente entregará el mismo código publicado en primer lugar.

![]({% image_buster /assets/img/voucherify/voucherify_cc_join_once.png %}){: style="max-width:50%;"}

Tu guion de Contenido conectado debe ser el siguiente:

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign cache_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}
{% endtab %}
{% endtabs %}

## Casos prácticos

Ten en cuenta que todos los casos de uso siguientes utilizan el ID de origen de publicación de Voucherify y los parámetros de caché y reintento de Braze para limitar las llamadas a la API invocadas por una campaña Braze. Debes ser consciente de las siguientes consecuencias:

- No es posible publicar y enviar códigos diferentes al mismo cliente en una sola campaña Braze.
- Si tu campaña de Voucherify utiliza la _característica de unirse sólo una vez_, tienes que eliminar `source_id` del cuerpo del contenido conectado, tal y como se describe en la pestaña de unirse sólo una vez anterior.

Visita el [repositorio GitHub](https://github.com/voucherifyio/braze-connected-content) de Voucherify para ver ejemplos de scripts de Contenido conectado.

### Publica y envía un código de cupón único

En este caso de uso, el script Contenido conectado llama a la API de Voucherify para publicar un código de cupón único y enviarlo en el mensaje Braze. Cada usuario de Braze recibe un único código.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Invita a nuevos referidos

Si quieres que un cliente se una a un programa de referidos, tienes que asignarle un código de referidos. El Contenido conectado sigue siendo el mismo que en el ejemplo anterior. Este script de contenido conectado te habilita para publicar y enviar códigos únicos de referidos a usuarios seleccionados de Braze. Cada usuario recibe un único código de referidos para compartirlo con otros usuarios y conseguir nuevos referidos. 

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Consultar el saldo de la tarjeta de fidelización

Este es un caso de uso de un script de Contenido conectado que extrae el saldo de fidelización actual basándose en el código de la tarjeta de fidelización que se envió previamente a Braze como atributo personalizado. Ten en cuenta que debes almacenar el código de la tarjeta de fidelización como un atributo personalizado en el perfil de usuario de Braze antes de utilizar este script.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign cache_id = source_id %}

{% connected_content
   YOUR API ENDPOINT/v1/loyalties/members/{{custom_attribute.${loyalty.card}}}?cache_id={{cache_id}}
   :method get
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age
   :retry
   :save member
 %}
```

{% endraw %}

### Crear código personalizado

Connected Content (contenido conectado) es una potente herramienta que permite introducir escenarios creativos. Puedes crear un código de cupón personalizado basado en la información del perfil del cliente.

Aquí tienes un fragmento de código que tendrá en cuenta el número de teléfono del cliente para generar un código único. En este caso de uso, el script de Contenido conectado llama a la API de Voucherify para publicar un código de cupón personalizado.

1.  Primero, define todas las variables necesarias. A continuación, crea un código de cupón que empiece por el prefijo "SummerTime-" y el resto del código será el número de teléfono del cliente. Puedes decidir en qué atributo personalizado quieres basar tus códigos de cupón.  
    
    {% raw %}
    
    ```liquid
    {% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
    {% assign customer_id = {{${user_id}}} %}
    {% assign phoneNumber = {{${phone_number}}} %}
    {% assign source_id = braze_campaign_id | append: customer_id %}
    {% assign cache_id = source_id %}
    {% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
    {% assign prefix = "SummerTime-" %}
    ```
    
    {% endraw %}
    
2.  A continuación, solicita a Voucherify que genere un código único en la campaña. Proporcionamos el nombre del código del cupón que se creará en la URL:  
    
    {% raw %}
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
       :method post
       :headers {
            "X-App-Id": "VOUCHERIFY-APP-ID",
            "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :content_type application/json
       :cache_max_age 
       :save voucher_created
       :retry
    %}  
    ```  
    
    {% endraw %}  

3.  Por último, publica el código que acabas de crear. El fragmento de código es prácticamente igual al que utilizaste para generar un vale aleatorio a partir de una campaña. Sin embargo, esta vez nos dirigimos a un código de cupón específico.  
    
    {% raw %}  
    
    ```liquid
    {% connected_content
       YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
       :method post
       :headers {
           "X-App-Id": "VOUCHERIFY-APP-ID",
           "X-App-Token": "VOUCHERIFY-APP-TOKEN"
       }
       :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
       :content_type application/json
       :cache_max_age 
       :save publication
       :retry
    %}
    ```
    
    {% endraw %}

Como resultado, el cliente recibe el siguiente correo electrónico:  

![]({% image_buster /assets/img/voucherify/voucherify_cc_custom_code_email.png %})

Aquí tienes el fragmento de código completo utilizado en este ejemplo:

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${dispatch_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign phoneNumber = {{${phone_number}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign cache_id = source_id %}
{% assign voucherify_campaign_id = "VOUCHERIFY-CAMPAIGN_ID" %}
{% assign prefix = "Your Prefix" %}

{% connected_content
   YOUR-API-ENDPOINT/v1/campaigns/{{voucherify_campaign_id}}/vouchers/{{prefix}}{{phoneNumber}}?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "VOUCHERIFY-APP-ID",
        "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :content_type application/json
   :cache_max_age 
   :save voucher_created
   :retry
%} 

{% connected_content
   YOUR-API-ENDPOINT/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
       "X-App-Id": "VOUCHERIFY-APP-ID",
       "X-App-Token": "VOUCHERIFY-APP-TOKEN"
   }
   :body voucher={{prefix}}{{phoneNumber}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age 
   :save publication
   :retry
%}
```

{% endraw %}

## Mostrar datos obtenidos en mensajes Braze

Suponemos que ya tienes una campaña Braze o un Canvas en el que quieres utilizar el script de Contenido conectado.

### Paso 1: Añadir secuencia de comandos de contenido conectado a la plantilla de mensajes

1.  Copia y pega el script Contenido conectado bajo la etiqueta {% raw %}`<body>`{% endraw %} en una plantilla HTML de mensaje. Sustituye **CAMPAIGN_ID** por un {% raw %}`campaign_id`{% endraw %} de Voucherify copiado de la dirección URL del panel de campaña de Voucherify.<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_campaignId.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}  
    ```
    assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce"
    ```
    {% endraw %}

2. Proporciona tu punto final de la API de Voucherify. Si no sabes cuál es tu punto final de API, puedes comprobarlo en la **configuración del proyecto** > **General** > **Punto final de API**.<br>
    {% raw %}
    ```
    YOUR API ENDPOINT/v1/publications?cache_id={{cache_id}}
    ```
    {% endraw %}
    
    | Clúster compartido   | Punto final para contenido conectado Braze          |
    | ---------------- | --------------------------------------------- |
    | Europa (predeterminado) | https://api.voucherify.io/v1/publications     |
    | Estados Unidos    | https://us1.api.voucherify.io/v1/publications |
    | Asia (Singapur) | https://as1.api.voucherify.io/v1/publications |
    {: .reset-td-br-1 .reset-td-br-2 role="presentation" }
    
3.  Añade tus claves de API para la autenticación. Puedes encontrar `Voucherify-App-Id` y `Voucherify-App-Token` en tu **Configuración del proyecto > General >Teclas de aplicación.**<br>![]({% image_buster /assets/img/voucherify/voucherify_cc_app_keys.png %}){: style="margin-top:15px;margin-bottom:15px;"}
    {% raw %}
    ```
    "X-App-Id": "VOUCHERIFY-APP-ID",
    "X-App-Token": "VOUCHERIFY-APP-TOKEN"
    ```
    {% endraw %}
    
Ahora tu guión de Contenido conectado está listo para funcionar.

{% raw %}

```liquid
{% assign braze_campaign_id = {{campaign.${api_id}}} %}
{% assign customer_id = {{${user_id}}} %}
{% assign source_id = braze_campaign_id | append: customer_id %}
{% assign voucherify_campaign_id = "camp_Y7h1meBSyybsNs7UpSVVZZce" %}
{% assign cache_id = source_id %}

{% connected_content
   https://api.voucherify.io/v1/publications?cache_id={{cache_id}}
   :method post
   :headers {
        "X-App-Id": "490a3fb6-a",
        "X-App-Token": "328099d5-a"
   }
   :body campaign={{voucherify_campaign_id}}&customer={{customer_id}}&channel=Braze&source_id={{source_id}}
   :content_type application/json
   :cache_max_age
   :retry
   :save publication
 %}
```

{% endraw %}

### Paso 2: Crea un fragmento de código para mostrar los datos obtenidos

Las respuestas de la API de Voucherify son almacenadas por el Contenido Conectado bajo el valor del parámetro {% raw %}`:save`{% endraw %}. Por ejemplo:

{% raw %}

```liquid
:save member
```
{% endraw %}

Esto te permite recuperar y mostrar datos de una respuesta de Voucherify en mensajes Braze.

Puedes crear fragmentos de código que muestren el código publicado, el saldo de la tarjeta de fidelización, la fecha de caducidad y otros parámetros incluidos en la respuesta en formato JSON de la API de Voucherify.

Por ejemplo, para mostrar el código publicado en una plantilla de mensajes, debes crear un fragmento de código que obtenga un código único del objeto vale.

Script de contenido conectado:

![Script de contenido conectado que muestra cómo guardar una respuesta de Voucherify al final de la llamada de contenido conectado]({% image_buster /assets/img/voucherify/voucherify_cc_save_parameter.png %})

Fragmento de plantilla de mensaje Braze:

{% raw %}

```liquid
{{publication.voucher.code}}
```

{% endraw %}

Como resultado, cada cliente recibe un mensaje con un código único asignado automáticamente a su perfil. Cada vez que el usuario recibe un código, este se publica en su perfil de Voucherify.

Para mostrar el saldo de una tarjeta de fidelización obtenida de la API de Voucherify, tienes que crear el siguiente fragmento de código:

{% raw %}

```liquid
{{member.loyalty_card.balance}}
```

{% endraw %}

donde el miembro es un valor del parámetro {% raw %}`:save`{% endraw %} del guion Contenido conectado.

{% raw %}

```liquid
:save member
```

{% endraw %}

Te aconsejamos encarecidamente que no dependas totalmente del "modo vista previa" y que envíes varios mensajes de prueba para confirmar que todo funciona como debería.

### Paso 3: Configurar el límite de velocidad

Cuando configures un objetivo de campaña, utiliza la configuración avanzada para limitar el número de mensajes enviados por minuto.

![]({% image_buster /assets/img/voucherify/voucherify_cc_limiter.png %})

Más información sobre el limitador de tasa y la limitación de frecuencia en [la documentación]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting) de Braze.

