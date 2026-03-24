---
nav_title: Etiquetas de personalización admitidas
article_title: Etiquetas de personalización de Liquid compatibles
page_order: 1
description: "Este artículo de referencia incluye una lista completa de las etiquetas de personalización de Liquid compatibles."
search_rank: 1
---

# Etiquetas de personalización admitidas

> Este artículo de referencia incluye una lista completa de las etiquetas de personalización de Liquid compatibles.

## Resumen de las etiquetas admitidas

Para mayor comodidad, se proporciona un resumen de las etiquetas de personalización admitidas. Para obtener más información sobre cada tipo de etiqueta y las prácticas recomendadas, sigue leyendo.

{% raw %}

| Tipo de etiqueta de personalización | Etiquetas |
| -------------  | ---- |
| Atributos estándar (predeterminados) | `{{${city}}}` <br> `{{${country}}}` <br> `{{${date_of_birth}}}` <br> `{{${email_address}}}` <br> `{{${first_name}}}` <br> `{{${gender}}}` <br> `{{${language}}}` <br> `{{${last_name}}}` <br> `{{${last_used_app_date}}}` <br> `{{${most_recent_app_version}}}` <br> `{{${most_recent_locale}}}` <br> `{{${most_recent_location}}}` <br> `{{${phone_number}}}` <br> `{{${time_zone}}}` <br> `{{${user_id}}}` <br> `{{${braze_id}}}` <br> `{{${random_bucket_number}}}` <br> `{{subscribed_state.${email_global}}}` <br> `{{subscribed_state.${subscription_group_id}}}` |
| Atributos de dispositivo | `{{most_recently_used_device.${carrier}}}` <br> `{{most_recently_used_device.${id}}}` <br> `{{most_recently_used_device.${idfa}}}` <br> `{{most_recently_used_device.${model}}}` <br> `{{most_recently_used_device.${os}}}` <br> `{{most_recently_used_device.${platform}}}` <br> `{{most_recently_used_device.${google_ad_id}}}` <br> `{{most_recently_used_device.${roku_ad_id}}}` <br> `{{most_recently_used_device.${foreground_push_enabled}}}`|
| <a href='/docs/user_guide/message_building_by_channel/email/managing_user_subscriptions/#managing-user-subscriptions'>Atributos de la lista de correo electrónico</a> | `{{${set_user_to_unsubscribed_url}}}` <br>Esta etiqueta sustituye a la anterior `{{${unsubscribe_url}}}`. Aunque la etiqueta antigua seguirá funcionando en los correos electrónicos creados anteriormente, te recomendamos que utilices en su lugar la etiqueta más reciente. <br><br> `{{${set_user_to_subscribed_url}}}` <br> `{{${set_user_to_opted_in_url}}}`|
| <a href='/docs/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/#trigger-messages'>Atributos SMS</a> | `{{sms.${inbound_message_body}}}` <br> `{{sms.${inbound_media_urls}}}` |
| <a href='/docs/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/'>Atributos de WhatsApp</a> | `{{whats_app.${inbound_message_body}}}` <br> `{{whats_app.${inbound_media_urls}}}` <br> `{{whats_app.${inbound_flow_response}}}` <br> `{{whats_app.${inbound_product_id}}}` <br> `{{whats_app.${inbound_catalog_id}}}` |
| Atributos de campaña y atributos de paso en Canvas | `{{campaign.${api_id}}}` <br> `{{campaign.${dispatch_id}}}` <br> `{{campaign.${name}}}` <br> `{{campaign.${message_name}}}` <br> `{{campaign.${message_api_id}}}` |
| Atributos de Canvas | `{{canvas.${name}}}` <br> `{{canvas.${api_id}}}` <br> `{{canvas.${variant_name}}}` <br> `{{canvas.${variant_api_id}}}` |
| Atributos de la tarjeta | `{{card.${api_id}}}` <br> `{{card.${name}}}` |
| Eventos de geovallado | `{{event_properties.${geofence_name}}}` <br> `{{event_properties.${geofence_set_name}}}` |
| Propiedades del evento <br> (Son personalizadas para tu espacio de trabajo.) | `{{event_properties.${your_custom_event_property}}}` |
| Variables de contexto de Canvas | `{{context}}` |
| Atributos personalizados <br> (Son personalizados para tu espacio de trabajo.) | `{{custom_attribute.${your_custom_attribute}}}` |
| <a href='/docs/api/objects_filters/trigger_properties_object/'>Propiedades del desencadenante de la API</a> |`{{api_trigger_properties}}` |
| Propiedades de entrada de Canvas | `{{context.${property_name}}}` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Atributos admitidos

Los atributos de campaña, tarjeta y Canvas solo se admiten en sus correspondientes plantillas de mensajería (por ejemplo, `dispatch_id` no está disponible en las campañas de mensajes dentro de la aplicación).

Consulta este artículo de ayuda para obtener más información sobre [cómo difieren algunos de estos atributos entre las fuentes en Braze]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/).

### Diferencias entre las etiquetas de Canvas y de campaña 

El comportamiento de las siguientes etiquetas difiere entre Canvas y las campañas:
{% raw %}
- El comportamiento de `dispatch_id` difiere porque Braze trata los pasos en Canvas como eventos desencadenados, incluso cuando están "programados" (excepto los pasos de entrada, que sí se pueden programar). Para obtener más información, consulta [Comportamiento del ID de envío]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- El uso de la etiqueta `{{campaign.${name}}}` con Canvas mostrará el nombre del componente de Canvas. Al utilizar esta etiqueta con campañas, se mostrará el nombre de la campaña.
{% endraw %}

## Información sobre el dispositivo utilizado más recientemente

Puedes crear plantillas con los siguientes atributos para el dispositivo más reciente del usuario en todas las plataformas. Si un usuario no ha utilizado tu aplicación (por ejemplo, importaste al usuario a través de la API REST), entonces todos estos valores serán `null`.

{% raw %}

|Etiqueta | Descripción |
|---|---|
|`{{most_recently_used_device.${browser}}}` | El navegador utilizado más recientemente en el dispositivo del usuario. Algunos ejemplos son "Chrome" y "Safari". |
|`{{most_recently_used_device.${id}}}` | El identificador del dispositivo de Braze. En iOS, puede ser el identificador de proveedor de Apple (IDFV) o un UUID. Para Android y otras plataformas, es un UUID generado aleatoriamente. |
| `{{most_recently_used_device.${carrier}}}` | El operador del servicio telefónico del dispositivo utilizado más recientemente, si está disponible. Algunos ejemplos son "Verizon" y "Orange". |
| `{{most_recently_used_device.${ad_tracking_enabled}}}` | Si el dispositivo tiene activado el seguimiento de anuncios o no. Se trata de un valor booleano (`true` o `false`). |
| `{{most_recently_used_device.${idfa}}}` | En los dispositivos iOS, este valor será el identificador para publicidad (IDFA) si tu aplicación está configurada con nuestra [recopilación opcional de IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). Para dispositivos que no sean iOS, este valor será nulo. |
| `{{most_recently_used_device.${google_ad_id}}}` | Para dispositivos Android, este valor será el identificador de publicidad de Google Play si tu aplicación está configurada con nuestra recopilación opcional del identificador de publicidad de Google Play. Para dispositivos que no sean Android, este valor será nulo. |
| `{{most_recently_used_device.${roku_ad_id}}}` | Para dispositivos Roku, este valor será el identificador de publicidad de Roku que se recopila cuando tu aplicación se configura con Braze. Para dispositivos que no sean Roku, este valor será nulo. |
| `{{most_recently_used_device.${model}}}` | El nombre del modelo del dispositivo, si está disponible. Algunos ejemplos son "iPhone 6S", "Nexus 6P" y "Firefox". |
| `{{most_recently_used_device.${os}}}` | El sistema operativo del dispositivo, si está disponible. Algunos ejemplos son "iOS 9.2.1", "Android (Lollipop)" y "Windows". |
| `{{most_recently_used_device.${platform}}}` | La plataforma del dispositivo, si está disponible. Si se establece, el valor será uno de los siguientes: `ios`, `android`, `kindle`, `android_china`, `web` o `tvos`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Debido a que existe una gran variedad de operadores, nombres de modelos y sistemas operativos, te recomendamos que pruebes exhaustivamente cualquier Liquid que dependa condicionalmente de cualquiera de esos valores. Estos valores serán `null` si no están disponibles en un dispositivo concreto.

## Información de la aplicación objetivo

Para los mensajes dentro de la aplicación, puedes utilizar los siguientes atributos de aplicación dentro de Liquid. Los valores se basan en la clave de API de SDK que tus aplicaciones utilizan para solicitar mensajería.

|Etiqueta | Descripción |
|------------------|---|
| `{{app.${api_id}}}` | La clave de API de la aplicación que solicita el mensaje. Por ejemplo, puedes utilizar esta clave junto con `abort_message()` de Liquid para evitar el envío de mensajes dentro de la aplicación a determinadas aplicaciones, como plataformas de TV o versiones de desarrollo que utilizan una clave de API de SDK independiente.|
| `{{app.${name}}}` | El nombre de la aplicación (tal y como se define en el panel de Braze) que solicita el mensaje. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por ejemplo, este código de Liquid abortará un mensaje si las aplicaciones solicitantes no son una de las dos claves de API de la lista:

```liquid
{% assign allowed_api_keys = 'sdk_api_key_1,sdk_api_key_2' | split: ',' %}
{% if allowed_api_keys contains {{app.${api_id}}} %}
User is in list of apps
{% else %}
{% abort_message("User not in list of apps") %}
{% endif %}
```

## Información del dispositivo objetivo

Para las notificaciones push, los mensajes dentro de la aplicación y los banners, puedes crear plantillas con los siguientes atributos para el dispositivo que recibe el mensaje. Una notificación push, un mensaje dentro de la aplicación o un banner pueden incluir atributos del dispositivo en el que el usuario lee el mensaje. Estos atributos no funcionan para Tarjetas de contenido ni correos electrónicos. En el caso de los correos electrónicos, los mensajes se procesan antes de enviarse, por lo que en ese momento se desconoce el dispositivo en el que el usuario abrirá el correo electrónico.

|Etiqueta | Descripción |
|------------------|---|
| `{{targeted_device.${id}}}` | Es el identificador del dispositivo de Braze. En iOS, puede ser el identificador de proveedor de Apple (IDFV) o un UUID. Para Android y otras plataformas, es un UUID generado aleatoriamente. Por ejemplo, si un usuario tiene cinco dispositivos, se realiza un intento de envío para los cinco dispositivos, cada uno utilizando el identificador de dispositivo correspondiente. Si un mensaje está configurado para enviarse al dispositivo utilizado más recientemente por el usuario, solo se realizará un intento de envío al dispositivo utilizado más recientemente identificado a través de Braze. |
| `{{targeted_device.${carrier}}}` | El operador del servicio telefónico del dispositivo utilizado más recientemente, si está disponible. Algunos ejemplos son "Verizon" y "Orange". |
| `{{targeted_device.${idfa}}}` | En los dispositivos iOS, este valor será el identificador para publicidad (IDFA) si tu aplicación está configurada con nuestra [recopilación opcional de IDFA]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/other_sdk_customizations/). Para dispositivos que no sean iOS, este valor será nulo. |
| `{{targeted_device.${google_ad_id}}}` | Para dispositivos Android, este valor será el identificador de publicidad de Google Play si tu aplicación está configurada con nuestra [recopilación opcional del identificador de publicidad de Google Play]. Para dispositivos que no sean Android, este valor será nulo. |
| `{{targeted_device.${roku_ad_id}}}` | Para dispositivos Roku, este valor será el identificador de publicidad de Roku que se recopila cuando tu aplicación se configura con Braze. Para dispositivos que no sean Roku, este valor será nulo. |
| `{{targeted_device.${model}}}` | El nombre del modelo del dispositivo, si está disponible. Algunos ejemplos son "iPhone 6S", "Nexus 6P" y "Firefox". |
| `{{targeted_device.${os}}}` | El sistema operativo del dispositivo, si está disponible. Algunos ejemplos son "iOS 9.2.1", "Android (Lollipop)" y "Windows". |
| `{{targeted_device.${platform}}}` | La plataforma del dispositivo, si está disponible. Si se establece, el valor será uno de los siguientes: `ios`, `android`, `kindle`, `android_china`, `web` o `tvos`. También puedes utilizar la etiqueta de personalización `most_recently_used_device`. |
| `{{targeted_device.${foreground_push_enabled}}}` | Este valor será `true` cuando el dispositivo objetivo esté habilitado para push en primer plano, `false` en caso contrario. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

Debido a que existe una gran variedad de operadores de dispositivos, nombres de modelos y sistemas operativos, te recomendamos que compruebes minuciosamente cualquier lógica que dependa condicionalmente de cualquiera de esos valores. Estos valores serán `null` si no están disponibles en un dispositivo concreto. 

Además, para las notificaciones push, es posible que Braze no pueda discernir el dispositivo asociado a la notificación push en determinadas circunstancias, como si el token de notificaciones push se importó a través de la API, lo que hace que los valores de esos mensajes sean `null`.

![Ejemplo de uso de un valor predeterminado de "there" cuando se utiliza una variable de nombre en un mensaje push.]({% image_buster /assets/img_archive/personalized_firstname_.png %})

### Utilizar la lógica condicional en lugar de un valor predeterminado

En algunas circunstancias, puedes optar por utilizar [lógica condicional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/) en lugar de establecer un valor predeterminado. La lógica condicional permite enviar mensajes que difieren en función del valor de un atributo personalizado. Además, puedes utilizar la lógica condicional para [abortar mensajes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) a clientes con valores de atributos nulos o en blanco. 

#### Caso de uso

Por ejemplo, supongamos que envías una notificación de saldo de recompensas a los clientes. No hay una buena forma de tener en cuenta a los clientes con saldos bajos y nulos utilizando valores predeterminados.

En este caso, hay dos opciones que pueden funcionar mejor que establecer un valor predeterminado:

1. Abortar el mensaje para clientes con saldos bajos, nulos y en blanco.

{% raw %}

   ```liquid
   {% if {{custom_attribute.${balance}}} > 0 %}
   Your rewards balance is {{custom_attribute.${balance}}}
   {% else %}
   {% abort_message() %}
   {% endif %}
   ```

{% endraw %}

2. Enviar un mensaje completamente distinto a estos clientes, por ejemplo:

{% raw %}

   ```liquid
   {% if ${first_name} != blank and ${first_name} != null %}
   Hello {{${first_name} | default: 'there'}}, thanks for downloading!
   {% else %}
   Thanks for downloading!
   {% endif %}
   ```

En este caso de uso, un usuario con un nombre en blanco o nulo recibirá el mensaje "Thanks for downloading!". Debes incluir un [valor predeterminado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/setting_default_values/) para el nombre para asegurarte de que tu cliente no vea Liquid en caso de error.

{% endraw %}

## Etiquetas de variables

Puedes utilizar la etiqueta `assign` para crear una variable en el creador de mensajes. Te recomendamos utilizar un nombre único para tu variable. Si creas una variable con un nombre similar al de las etiquetas de personalización admitidas (como `language`), esto puede afectar a la lógica de tu mensajería.

Después de crear una variable, puedes hacer referencia a ella en tu lógica de mensajería o mensaje. Esta etiqueta resulta útil cuando quieres reformatear el contenido devuelto por nuestra función de [contenido conectado]({% image_buster /assets/img_archive/personalized_firstname_.png %}). Puedes leer más en la documentación de Shopify sobre [etiquetas de variables](https://docs.shopify.com/themes/liquid/tags/variable-tags).

{% alert tip %}
¿Te encuentras asignando las mismas variables en todos los mensajes? En lugar de escribir la etiqueta `assign` una y otra vez, puedes guardarla como un bloque de contenido y colocarla en la parte superior del mensaje.

1. [Crea un bloque de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block).
2. Asigna un nombre al bloque de contenido (sin espacios ni caracteres especiales).
3. Selecciona **Editar** en la parte inferior de la página.
4. Introduce tus etiquetas `assign`.

Mientras el bloque de contenido esté en la parte superior del mensaje, cada vez que la variable se inserte en el mensaje como un objeto, hará referencia al atributo personalizado que hayas elegido.
{% endalert %}

### Caso de uso

Digamos que permites a tus clientes canjear sus puntos de recompensa por premios después de acumular 100 puntos de recompensa. Por lo tanto, solo debes enviar mensajes a los clientes que tendrían un saldo de puntos superior o igual a 100 si realizaran esa compra adicional:

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

## Etiquetas de iteración

{% raw %}
Las etiquetas de iteración pueden utilizarse para ejecutar un bloque de código repetidamente. El siguiente caso de uso presenta la etiqueta `for`.

### Caso de uso

Supongamos que tienes una oferta de zapatillas Nike y quieres enviar mensajes a los clientes que han expresado interés por Nike. Tienes un array de marcas de productos vistas en el perfil de cada cliente. Este array podría contener hasta 25 marcas de producto, pero solo quieres enviar mensajes a los clientes que vieron un producto Nike como una de sus 5 vistas de producto más recientes.

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

En este caso de uso, comprobamos los cinco primeros elementos del array de marcas de zapatillas vistas. Si uno de esos elementos es Converse, creamos la variable `converse_viewer` y le asignamos el valor verdadero.

A continuación, enviamos el mensaje de oferta cuando `converse_viewer` es verdadero. En caso contrario, abortamos el mensaje.

Este es un ejemplo sencillo de cómo pueden utilizarse las etiquetas de iteración en el creador de mensajes de Braze. Puedes encontrar más información en la documentación de Shopify sobre [etiquetas de iteración](https://docs.shopify.com/themes/liquid/tags/iteration-tags).

## Etiquetas de sintaxis

Las etiquetas de sintaxis pueden utilizarse para controlar cómo se renderiza Liquid. Puedes utilizar la etiqueta `echo` para devolver una expresión. Esto es lo mismo que envolver una expresión con llaves, excepto que puedes utilizar esta etiqueta dentro de etiquetas de Liquid. También puedes utilizar la etiqueta `liquid` para tener un bloque de Liquid sin delimitadores en cada etiqueta. Cada etiqueta debe ir en su propia línea cuando utilices la etiqueta `liquid`. Consulta la documentación de Shopify sobre [etiquetas de sintaxis](https://shopify.dev/api/liquid/tags#syntax-tags) para obtener más información y ejemplos.

Con el [control de espacios en blanco](https://shopify.github.io/liquid/basics/whitespace/), puedes eliminar los espacios en blanco alrededor de tus etiquetas, lo que te ayuda a controlar aún más el aspecto de la salida de Liquid.

## Códigos de estado HTTP {#http-personalization}

Puedes utilizar el estado HTTP de una llamada a [contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) guardándolo primero como una variable local y utilizando después la clave `__http_status_code__`. Por ejemplo:

```html
{% connected_content https://example.com/api/endpoint :save connected %}
{% if connected.__http_status_code__ != 200 %}
{% abort_message('Connected Content returned a non-200 status code') %}
{% endif %}
```
{% endraw %}

{% alert note %}
Esta clave solo se añadirá automáticamente al objeto de contenido conectado si el punto de conexión devuelve un objeto JSON. Si el punto de conexión devuelve un array u otro tipo, esa clave no se puede establecer automáticamente en la respuesta.
{% endalert %}

## Envío de mensajes en función del idioma, la configuración regional más reciente y la zona horaria

En algunas situaciones, es posible que desees enviar mensajes específicos para determinadas configuraciones regionales. Por ejemplo, el portugués brasileño suele ser diferente del portugués europeo.

### Caso de uso: localización basada en la configuración regional reciente

A continuación se muestra un caso de uso sobre cómo puedes utilizar la configuración regional más reciente para localizar aún más un mensaje internacionalizado.

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

En este caso de uso, los clientes con una configuración regional más reciente de `pt_BR` recibirán un mensaje en portugués brasileño, y los clientes con una configuración regional más reciente de `pt_PT` recibirán un mensaje en portugués europeo. Los clientes que no cumplan las dos primeras condiciones, pero que tengan el idioma configurado como portugués, recibirán un mensaje en el tipo de portugués predeterminado que elijas.

### Caso de uso: dirigirse a usuarios por zona horaria

También puedes dirigirte a los usuarios por su zona horaria. Por ejemplo, envía un mensaje si están en EST y otro si están en PST. Para ello, guarda la hora actual en UTC y compara una sentencia if/else con la hora actual del usuario para enviar el mensaje correcto para la zona horaria correcta. Debes configurar la campaña para que se envíe en la zona horaria local del usuario, para que reciba la campaña a la hora adecuada. 

Mira el siguiente caso de uso para saber cómo escribir un mensaje que se enviará entre las 14:00 y las 15:00 y tendrá un mensaje específico para cada zona horaria.

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

## Envío de mensajes con un número aleatorio

{% raw %}
La etiqueta `{% random %}` devuelve un número aleatorio. Puedes utilizarla para lógica de tipo A/B, muestreo o para variar el contenido de los mensajes.

| Etiqueta | Descripción |
|-------|--------------|
| `{% random %}` | Un número decimal entre 0 y 1 (incluye el 0, excluye el 1). |
| `{% random 10 %}` (argumento entero) | Un número entero que va desde 0 hasta, pero sin incluir, el entero especificado. Por ejemplo, `{% random 10 %}` devuelve un entero del 0 al 9. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}

### Caso de uso: enviar variantes aleatorias a los usuarios

{% raw %}
```liquid
{% capture roll_str %}{% random %}{% endcapture %}
{% assign roll = roll_str | plus: 0 %}
{% if roll < 0.5 %}
Show variant A
{% else %}
Show variant B
{% endif %}
```
{% endraw %}


[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags