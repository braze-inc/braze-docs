---
nav_title: Etiquetas de personalización admitidas
article_title: Etiquetas de personalización de Liquid compatibles
page_order: 1
description: "Este artículo de referencia incluye una lista completa de las etiquetas de personalización de Liquid compatibles."
search_rank: 1
---

# Etiquetas de personalización admitidas

> Este artículo de referencia incluye una lista completa de las etiquetas de personalización de Liquid compatibles.

## Resumen de etiquetas compatibles

Por comodidad, se proporciona un resumen de las etiquetas de personalización admitidas. Para más detalles sobre cada tipo de etiqueta y las mejores prácticas, sigue leyendo.

{% raw %}

| Tipo de etiqueta de personalización | Etiquetas |
| -------------  | ---- |
| Atributos estándar (predeterminados) | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Atributos del dispositivo | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions'>Atributos de la lista de correo electrónico</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Esta etiqueta sustituye a la anterior `{{${unsubscribe_url}}}`. Aunque la etiqueta antigua seguirá funcionando en los correos electrónicos creados anteriormente, te recomendamos que utilices en su lugar la etiqueta más reciente. <br><br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| <a href='/docs/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/#trigger-messages'>Atributos SMS</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/'>Atributos de WhatsApp</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` |
| Atributos de la campaña | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Atributos de Canvas | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Atributos de los pasos en Canvas | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Atributos de la tarjeta | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Eventos geovallados | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Propiedades del evento <br> (Están personalizados para tu espacio de trabajo).| `{{event_properties.${your_custom_event_property}}}` |
| Variables contextuales del Canvas | `{{context}}` |
| Atributos personalizados <br> (Están personalizados para tu espacio de trabajo). | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>Propiedades de la API desencadenante</a> |`{{api_trigger_properties}}` |
| Propiedades de entrada en Canvas | `{{canvas_entry_properties.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Atributos admitidos

Los atributos de Campaña, Tarjeta y Canvas sólo se admiten en sus correspondientes plantillas de mensajería (por ejemplo, `dispatch_id` no está disponible en las campañas de mensajería dentro de la aplicación).

Consulta este artículo de ayuda para saber más sobre [cómo difieren algunos de estos atributos entre las fuentes en Braze]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/).

### Diferencias entre las etiquetas de Canvas y de campaña 

El comportamiento de las siguientes etiquetas difiere entre Canvas y las campañas:
{% raw %}
- `dispatch_id` El comportamiento difiere porque Braze trata los pasos en Canvas como eventos desencadenados, incluso cuando están "programados" (excepto los pasos de entrada, que pueden programarse). Para saber más, consulta [Comportamiento del ID de Despacho]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- Si utilizas la etiqueta `{{campaign.${name}}}` con Canvas, aparecerá el nombre del componente Canvas. Cuando utilices esta etiqueta con campañas, mostrará el nombre de la campaña.
{% endraw %}

## Información del dispositivo utilizado más recientemente

Puedes plantillas los siguientes atributos para el dispositivo más reciente del usuario en todas las plataformas. Si un usuario no ha utilizado tu aplicación (por ejemplo, has importado al usuario a través de la API REST), entonces todos estos valores serán `null`.

{% raw %}

|Etiqueta | Descripción |
|---|---|
|`{{most_recently_used_device.${browser}}}` | El navegador utilizado más recientemente en el dispositivo del usuario. Algunos ejemplos son "Chrome" y "Safari". |
|`{{most_recently_used_device.${id}}}` | El identificador del dispositivo Braze. En iOS, puede ser el Identificador de Vendedor de Apple (IDFV) o un UUID. Para Android y otras plataformas, es un UUID generado aleatoriamente. |
| `{{most_recently_used_device.${carrier}}}` | El operador del servicio telefónico del dispositivo utilizado más recientemente, si está disponible. Algunos ejemplos son "Verizon" y "Orange". |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Si el dispositivo tiene habilitado el seguimiento de anuncios o no. Es un valor booleano (`true` o `false`). |
| `{{most_recently_used_device.${idfa}}}` | Para dispositivos iOS, este valor será el identificador para publicidad (IDFA) si tu aplicación está configurada con nuestra [colección opcional IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). Para dispositivos que no sean iOS, este valor será nulo. |
| `{{most_recently_used_device.${google_ad_id}}}` | Para dispositivos Android, este valor será el identificador de publicidad de Google Play si tu aplicación está configurada con nuestra recopilación opcional de ID de publicidad de Google Play. Para los dispositivos que no sean Android, este valor será nulo. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Para los dispositivos Roku, este valor será el identificador de publicidad Roku que se recopila cuando tu aplicación se configura con Braze. Para los dispositivos que no sean Roku, este valor será nulo. |
| `{{most_recently_used_device.${model}}}` | El nombre del modelo del dispositivo, si está disponible. Algunos ejemplos son "iPhone 6S", "Nexus 6P" y "Firefox". |
| `{{most_recently_used_device.${os}}}` | El sistema operativo del dispositivo, si está disponible. Algunos ejemplos son "iOS 9.2.1" y "Android (Lollipop)" y "Windows". |
| `{{most_recently_used_device.${platform}}}` | La plataforma del dispositivo, si está disponible. Si se establece, el valor será uno de los siguientes: `ios`, `android`, `kindle`, `android_china`, `web`, o `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Como existe una gama tan amplia de operadores de dispositivos, nombres de modelos y sistemas operativos, te aconsejamos que pruebes a fondo cualquier Liquid que dependa condicionalmente de cualquiera de esos valores. Estos valores serán `null` si no están disponibles en un dispositivo concreto.

## Información específica sobre la aplicación

Para los mensajes dentro de la aplicación, puedes utilizar los siguientes atributos dentro de la aplicación Liquid. Los valores se basan en qué clave de API de SDK utilizan tus aplicaciones para solicitar mensajería.

|Etiqueta | Descripción |
|------------------|---|
| `{{app.${api_id}}}` | La clave de API de la aplicación que solicita el mensaje. Por ejemplo, utiliza esta clave junto con `abort_message()` Liquid para evitar enviar mensajes dentro de la aplicación a determinadas aplicaciones, como plataformas de TV o compilaciones de desarrollo que utilizan una clave de API de SDK distinta.|
| `{{app.${name}}}` | El nombre de la aplicación (como se define en el panel de Braze) que solicita el mensaje. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por ejemplo, este código Liquid abortará un mensaje si la aplicación solicitante no es una de las dos claves de API de la lista:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Información específica del dispositivo

Para las notificaciones push y los canales de mensajería dentro de la aplicación, puedes introducir en la plantilla los siguientes atributos para el dispositivo al que se envía un mensaje. Es decir, una notificación push o un mensaje dentro de la aplicación pueden incluir atributos del dispositivo en el que se está leyendo el mensaje. Ten en cuenta que estos atributos no funcionarán para las tarjetas de contenido. 

|Etiqueta | Descripción |
|------------------|---|
| `{{targeted_device.${id}}}` | Este es el identificador del dispositivo Braze. En iOS, puede ser el Identificador de Vendedor de Apple (IDFV) o un UUID. Para Android y otras plataformas, es un UUID generado aleatoriamente. Por ejemplo, si un usuario tiene cinco dispositivos, se produce un intento de envío para los cinco dispositivos, cada uno utilizando el identificador de dispositivo correspondiente. Si un mensaje está configurado para enviarse al dispositivo utilizado más recientemente por un usuario, sólo se producirá un intento de envío al dispositivo utilizado más recientemente identificado a través de Braze. |
| `{{targeted_device.${carrier}}}` | El operador del servicio telefónico del dispositivo utilizado más recientemente, si está disponible. Algunos ejemplos son "Verizon" y "Orange". |
| `{{targeted_device.${idfa}}}` | Para dispositivos iOS, este valor será el identificador para publicidad (IDFA) si tu aplicación está configurada con nuestra [colección opcional IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). Para dispositivos que no sean iOS, este valor será nulo. |
| `{{targeted_device.${google_ad_id}}}` | Para dispositivos Android, este valor será el identificador de publicidad de Google Play si tu aplicación está configurada con nuestra [recopilación opcional de ID de publicidad de Google Play]. Para los dispositivos que no sean Android, este valor será nulo. |
| `{{targeted_device.${roku_ad_id}}}` | Para los dispositivos Roku, este valor será el identificador de publicidad Roku que se recopila cuando tu aplicación se configura con Braze. Para los dispositivos que no sean Roku, este valor será nulo. |
| `{{targeted_device.${model}}}` | El nombre del modelo del dispositivo, si está disponible. Algunos ejemplos son "iPhone 6S", "Nexus 6P" y "Firefox". |
| `{{targeted_device.${os}}}` | El sistema operativo del dispositivo, si está disponible. Algunos ejemplos son "iOS 9.2.1" y "Android (Lollipop)" y "Windows". |
| `{{targeted_device.${platform}}}` | La plataforma del dispositivo, si está disponible. Si se establece, el valor será uno de los siguientes: `ios`, `android`, `kindle`, `android_china`, `web`, o `tvos`. También puedes utilizar la etiqueta de personalización `most_recently_used_device`. |
| `{{targeted_device.${foreground_push_enabled}}}` | Este valor será `true` cuando el dispositivo objetivo esté habilitado para push en primer plano, `false` en caso contrario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

Como hay una gama tan amplia de operadores de dispositivos, nombres de modelos y sistemas operativos, te aconsejamos que pruebes a fondo cualquier lógica que dependa condicionalmente de cualquiera de esos valores. Estos valores serán `null` si no están disponibles en un dispositivo concreto. 

Además, para las notificaciones push, es posible que Braze no pueda discernir el dispositivo conectado a la notificación push en determinadas circunstancias, como si el token de notificaciones push se importó a través de la API, lo que hace que los valores de esos mensajes sean `null`.

\![Ejemplo de uso de un valor predeterminado de "allí" al utilizar una variable de nombre en un mensaje push.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Utilizar la lógica condicional en lugar de un valor predeterminado

En algunas circunstancias, puedes optar por utilizar [la lógica condicional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) en lugar de establecer un valor predeterminado. La lógica condicional te permite enviar mensajes que difieren en función del valor de un atributo personalizado. Además, puedes utilizar la lógica condicional para [abortar los mensajes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) a clientes con valores de atributos nulos o en blanco. 

#### Casos de uso

Por ejemplo, supongamos que envías una notificación de saldo de recompensas a los clientes. No hay una buena forma de tener en cuenta a los clientes con saldos bajos y nulos utilizando valores predeterminados.

En este caso, hay dos opciones que pueden funcionar mejor que establecer un valor predeterminado:

1. Aborta el mensaje para clientes con saldos bajos, nulos y en blanco.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Envía un mensaje completamente distinto a estos clientes, por ejemplo

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

En este caso de uso, un usuario con un nombre en blanco o nulo recibirá el mensaje "Gracias por descargar". Debes incluir un [valor predeterminado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/) para el nombre para asegurarte de que tu cliente no vea Liquid en caso de error.

{% endraw %}

## Etiquetas variables

Puedes utilizar la etiqueta `assign` para crear una variable en el creador de mensajes. Te recomendamos que utilices un nombre único para tu variable. Si creas una variable con un nombre similar al de las etiquetas de personalización admitidas (como `language`), esto puede afectar a tu lógica de mensajería.

Después de crear una variable, puedes hacer referencia a esa variable en tu lógica de mensajería o mensaje. Esta etiqueta es útil cuando quieres reformatear contenido devuelto por nuestra característica [Contenido conectado]({% image_buster /assets/img_archive/personalized_firstname_.png %}) ]. Puedes leer más en la documentación de Shopify sobre [etiquetas variables](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert tip %}
¿Te encuentras asignando las mismas variables en cada mensaje? En lugar de escribir la etiqueta `assign` una y otra vez, puedes guardar esa etiqueta como bloque de contenido y colocarla en la parte superior de tu mensaje.

1. [Crea un bloque de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Dale un nombre a tu bloque de contenido (sin espacios ni caracteres especiales).
3. Selecciona **Editar** en la parte inferior de la página.
4. Introduce tus etiquetas `assign`.

Mientras el bloque de contenido esté en la parte superior de tu mensaje, cada vez que la variable se inserte en tu mensaje como un objeto, ¡hará referencia al atributo personalizado que hayas elegido!
{% endalert %}

### Casos de uso

Digamos que permites a tus clientes canjear sus puntos de recompensa por premios después de acumular 100 puntos de recompensa. Por tanto, sólo quieres enviar mensajes a los clientes que tendrían un saldo de puntos mayor o igual a 100 si hicieran esa compra adicional:

{% raw %}
```liquid
{% assign new_points_balance = {{custom_attribute.${current_rewards_balance} | plus: 50}} %}
{% if new_points_balance >= 100 %}
Make a purchase to bring your rewards points to {{new_points_balance}} and cash in today!
{% else %}
{% abort_message('not enough points') %}
{% endif %}
```
{% endraw %}

## Etiquetas Iterate

{% raw %}
Las etiquetas de Iteración pueden utilizarse para ejecutar un bloque de código repetidamente. El siguiente caso de uso presenta la etiqueta `for`.

### Casos de uso

Supongamos que estás de rebajas en zapatillas Nike y quieres enviar mensajes a los clientes que han expresado interés en Nike. Tienes una serie de marcas de productos que se ven en el perfil de cada cliente. Esta matriz podría contener hasta 25 marcas de producto, pero sólo quieres enviar mensajes a los clientes que vieron un producto Nike como una de sus 5 vistas de producto más recientes.

```liquid
{% for items in {{custom_attribute.${Brands Viewed}}} limit:5 %}
{% if {{items}} contains 'Converse' %}
{% assign converse_viewer = true %}
{% endif %}
{% endfor %}
{% if converse_viewer == true %}
Sale on Converse!
{% else %}
{% abort_message() %}
{% endif %}
```

En este caso de uso, comprobamos los cinco primeros elementos de la matriz de marcas de zapatillas vistas. Si uno de esos elementos es converso, creamos la variable `converse_viewer` y le damos el valor verdadero.

A continuación, enviamos el mensaje de venta cuando `converse_viewer` es verdadero. De lo contrario, abortamos el mensaje.

Éste es un ejemplo sencillo de cómo pueden utilizarse las etiquetas de iteración en el creador de mensajes Braze. Puedes encontrar más información en la documentación de Shopify sobre [las etiquetas de iteración](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Etiquetas sintácticas

Las etiquetas de sintaxis pueden utilizarse para controlar cómo se muestra Liquid. Puedes utilizar la etiqueta `echo` para devolver una expresión. Es lo mismo que encerrar una expresión entre llaves, pero puedes utilizar esta etiqueta dentro de etiquetas de Liquid. También puedes utilizar la etiqueta `liquid` para tener un bloque de Liquid sin delimitadores en cada etiqueta. Cada etiqueta debe ir en su propia línea cuando utilices la etiqueta `liquid`. Consulta la documentación de Shopify sobre [las etiquetas de sintaxis](https://shopify.dev/api/liquid/tags#syntax-tags) para obtener más información y ejemplos.

Con [el control de espacios](https://shopify.github.io/liquid/basics/whitespace/) en blanco, puedes eliminar los espacios en blanco alrededor de tus etiquetas, lo que te ayudará a controlar aún más el aspecto de la salida de Liquid.

## Códigos de estado HTTP {#http-personalization}

Puedes utilizar el estado HTTP de una llamada a [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) guardándolo primero como variable local y utilizando después la tecla `__http_status_code__`. Por ejemplo:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Esta clave sólo se añadirá automáticamente al objeto Contenido conectado si el punto final devuelve un objeto JSON. Si el punto final devuelve una matriz u otro tipo, entonces esa clave no puede establecerse automáticamente en la respuesta.
{% endalert %}

## Envío de mensajes en función del idioma, la localización más reciente y la zona horaria

En algunas situaciones, puede que desees enviar mensajes que sean específicos para determinadas localizaciones. Por ejemplo, el portugués brasileño suele ser diferente del portugués europeo.

### Casos de uso: Localización basada en la localización reciente

Aquí tienes un caso de uso de cómo puedes utilizar la configuración regional más reciente para localizar mejor un mensaje internacionalizado.

{% raw %}

```liquid
{% if ${language} == 'en' %}
Message in English
{% elsif  ${language} == 'fr' %}
Message in French
{% elsif  ${language} == 'ja' %}
Message in Japanese
{% elsif  ${language} == 'ko' %}
Message in Korean
{% elsif  ${language} == 'ru' %}
Message in Russian
{% elsif ${most_recent_locale} == 'pt_BR' %}
Message in Brazilian Portuguese
{% elsif ${most_recent_locale} == 'pt_PT' %}
Message in European Portuguese
{% elsif  ${language} == 'pt' %}
Message in default Portuguese
{% else %}
Message in default language
{% endif %}
```

En este caso de uso, los clientes con una localización más reciente de `pt_BR` recibirán un mensaje en portugués brasileño, y los clientes con una localización más reciente de `pt_PT` recibirán un mensaje en portugués europeo. Los clientes que no cumplan las dos primeras condiciones, pero que tengan el idioma portugués, recibirán un mensaje en el idioma portugués predeterminado.

### Casos de uso: Usuarios objetivo por zona horaria

También puedes dirigirte a los usuarios por su zona horaria. Por ejemplo, envía un mensaje si viven en EST y otro si viven en PST. Para ello, guarda la hora actual en UTC, y compara una sentencia if/else con la hora actual del usuario para enviar el mensaje correcto para la zona horaria correcta. Debes configurar la campaña para que se envíe en la zona horaria local del usuario, para que reciba la campaña a la hora adecuada. 

Mira el siguiente caso de uso para saber cómo escribir un mensaje que saldrá entre las 14:00 y las 15:00 y que tendrá un mensaje específico para cada zona horaria.

```liquid
{% assign hour_in_utc = 'now' | date: '%H' | plus:0 %}
{% if hour_in_utc >= 19 && hour_in_utc < 20 %}
It is between 2:00:00 pm and 2:59:59 pm ET!
{% elsif hour_in_utc >= 22 && hour_in_utc < 23 %}
It is between 2:00:00 pm and 2:59:59 pm PT!
{% else %}
{% abort_message %}
{% endif %}
```

{% endraw %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
