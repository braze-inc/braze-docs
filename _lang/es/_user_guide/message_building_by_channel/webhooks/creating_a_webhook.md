---
nav_title: Crear un webhook
article_title: Crear un webhook
page_order: 1
channel:
  - webhooks
description: "Este artículo de referencia explica cómo crear y configurar una campaña webhook."
search_rank: 2
---

# Crear una campaña webhook

> Crear una campaña de webhook o incluir un webhook en una campaña multicanal te permite desencadenar acciones no relacionadas con la aplicación proporcionando a otros sistemas y aplicaciones información en tiempo real. 

Puedes utilizar webhooks para enviar información a sistemas, como Salesforce o Marketo, o a tus sistemas backend. Por ejemplo, puede que quieras acreditar una promoción en las cuentas de tus clientes después de que hayan realizado un evento personalizado un determinado número de veces.

{% alert tip %}
Para saber más sobre qué son los webhooks y cómo puedes utilizarlos en Braze, consulta [Acerca de los webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) antes de continuar.
{% endalert %}

## Paso 1: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y sencillas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

**Pasos:**

1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Selecciona **Webhook** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3. Pon a tu campaña un nombre claro y significativo.
4. (Opcional) Añade una descripción de cómo se utilizará esta campaña.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por determinadas etiquetas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plantillas de webhook para cada una de las variantes que añadas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o van a tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. A continuación, puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Pasos:**

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Nombra tu paso con algo claro y significativo.
3. Elige un [programa de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifica un retraso según sea necesario.
4. Filtra tu audiencia para este paso según sea necesario. Puedes afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso en el momento de enviar los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elige cualquier otro canal de mensajería que quieras asociar a tu mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Crea tu webhook

Puedes elegir crear un webhook desde cero, utilizar una plantilla existente o utilizar una de nuestras plantillas existentes. A continuación, crea tu webhook en la pestaña **Componer** del editor.

La pestaña **Componer** consta de los siguientes campos:

- Lengua
- URL del webhook
- Método HTTP
- Cuerpo de la solicitud

\![La pestaña "Componer" con una plantilla de webhook de ejemplo.]({% image_buster /assets/img_archive/webhook_compose.png %})

#### Lengua {#internationalization}

Se admite la [internacionalización]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) en la URL y en el cuerpo de la solicitud. Para internacionalizar tu mensaje, selecciona **Añadir idiomas** y rellena los campos obligatorios. 

Te recomendamos que selecciones tus idiomas antes de escribir el contenido, para que puedas rellenar el texto donde corresponda en el Liquid. Para consultar nuestra lista completa de idiomas disponibles que puedes utilizar, consulta [Idiomas admitidos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

Si añades texto en un idioma escrito de derecha a izquierda, ten en cuenta que el aspecto final de los mensajes escritos de derecha a izquierda depende en gran medida de cómo los rendericen los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha [a]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### URL del webhook

La URL del webhook, o URL HTTP, especifica tu punto final. El punto final es el lugar al que enviarás la información que estás capturando en el webhook. 

Si quieres enviar información a un proveedor, éste debe proporcionar esta URL en la documentación de su API. Si envías información a tus propios sistemas, comprueba con tu equipo desarrollador o de ingeniería que utilizas la URL correcta. 

Braze sólo permite URL que se comuniquen a través de los puertos estándar `80` (HTTP) y `443` (HTTPS).

##### Utilizar Liquid

Puedes personalizar las URL de tus webhooks utilizando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/). A veces, ciertos puntos finales pueden requerir que identifiques a un usuario o que proporciones información específica del usuario como parte de tu URL. Cuando utilices Liquid, asegúrate de incluir un [valor predeterminado]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) para cada dato específico del usuario que utilices en tu URL.

#### Método HTTP

El [método HTTP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods) que debes utilizar variará en función del endpoint al que envíes información. En la mayoría de los casos, utilizarás POST.

#### Cuerpo de la solicitud

El cuerpo de la solicitud es la información que se enviará a la URL que hayas especificado. Puedes crear el cuerpo de tu solicitud de webhook con pares clave-valor JSON o texto sin formato.

##### Pares clave-valor JSON

Los pares clave-valor JSON te permiten escribir fácilmente una solicitud para un punto final que espera un formato JSON. Sólo puedes utilizarlo con un punto final que espere una petición JSON. Por ejemplo, si tu clave es `message_body`, el valor correspondiente podría ser `Your order just arrived!`. Una vez que hayas introducido tu par clave-valor, el compositor configurará tu solicitud en sintaxis JSON, y se rellenará automáticamente una vista previa de tu solicitud JSON.

\![Cuerpo de la solicitud establecido en pares clave-valor JSON.]({% image_buster /assets/img/webhook_json_1.png %})

Puedes personalizar tus pares clave-valor utilizando Liquid, por ejemplo, incluyendo en tu solicitud cualquier atributo del usuario, [atributo personalizado]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices) o [propiedad del evento]({{site.baseurl}}/user_guide/data/custom_data/custom_events/). Por ejemplo, puedes incluir el nombre y el correo electrónico de un cliente en tu solicitud. Asegúrate de incluir un [valor predeterminado]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=web) para cada atributo.

##### Texto bruto

La opción de texto sin formato te da la flexibilidad de escribir una petición para un punto final que espera un cuerpo de cualquier formato. Por ejemplo, podrías utilizarlo para escribir una solicitud para un punto final que espera que tu solicitud esté en formato XML. 

Tanto la [personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) como la [internacionalización]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) mediante Liquid son compatibles con el texto sin formato.

\![Ejemplo de un cuerpo de solicitud con texto sin procesar utilizando Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Si estableces el [encabezado de solicitud](#request-headers-optional) `Content-Type` en `application/x-www-form-url-encoded`, el cuerpo de la solicitud debe formatearse como una cadena codificada en URL. Por ejemplo:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

\![Cuerpo de la solicitud con cadena codificada en URL.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Paso 3: Configurar ajustes adicionales

#### Encabezados de solicitud (opcional)

Algunos puntos finales pueden requerir que incluyas encabezados en tu solicitud. En la sección **Componer** del compositor, puedes añadir tantas cabeceras como necesites.

\![Ejemplos de encabezados de solicitud para la clave "Autorización" y la clave "Tipo de contenido".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Los encabezados de solicitud más comunes son las especificaciones `Content-Type` (que describen qué tipo de datos esperar en el cuerpo, como XML o JSON) y los encabezados de autorización que contienen tus credenciales con tu proveedor o sistema. 

Las especificaciones del tipo de contenido deben utilizar la clave `Content-Type`. Los valores habituales son `application/json` o `application/x-www-form-urlencoded`.

Las cabeceras de autorización deben utilizar la clave `Authorization`. Los valores habituales son {% raw %} `Bearer {{YOUR_TOKEN}}` o `Basic {{YOUR_TOKEN}}` {% endraw %}, donde `YOUR_TOKEN` son las credenciales proporcionadas por tu proveedor o sistema.

## Paso 4: Prueba envía tu mensaje

Antes de poner en marcha tu campaña, Braze recomienda que pruebes el webhook para asegurarte de que la solicitud tiene el formato adecuado.

Para ello, pasa a la pestaña **Prueba** y envía un webhook de prueba. Puedes probar el webhook como un usuario aleatorio, un usuario específico (introduciendo su dirección de correo electrónico de ID de usuario externo), o un usuario personalizado con atributos de tu elección.  

Tras enviar el webhook de prueba, aparecerá un diálogo con el mensaje de respuesta. Si la solicitud del webhook no tiene éxito, consulta el mensaje de error para obtener ayuda en la solución de problemas de tu webhook. El siguiente ejemplo detalla la respuesta de un webhook con una URL de webhook no válida.

```json
404 Not Found

{
  "error": {
    "message": "Unrecognized request URL. Please see https://lob.com/docs or email us at support@lob.com.",
    "status_code": 404
  }
}

```

## Paso 5: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

A continuación, construye el resto de tu campaña. Consulta las secciones siguientes para obtener más detalles sobre la mejor manera de utilizar nuestras herramientas para crear webhooks.

#### Elige el calendario o desencadenar la entrega

Los webhooks pueden entregarse en función de una hora programada, de una acción o de un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes configurar la duración de la campaña y las horas tranquilas.

En este paso también puedes especificar controles de entrega, como permitir que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña, o habilitar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Elige los usuarios a los que dirigirte

A continuación, tienes que [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. En este paso, seleccionarás la audiencia más amplia de tus segmentos, y reducirás aún más ese segmento con nuestros filtros, si así lo deseas. Automáticamente recibirás una vista previa de cómo es la población aproximada de ese segmento en este momento. Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

{% multi_lang_include target_audiences.md %}

#### Elige eventos de conversión

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu paso en Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariantes e Intelligent Selection, y mucho más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación sobre Canvas.

{% endtab %}
{% endtabs %}

## Paso 6: Revisar y desplegar

Cuando hayas terminado de construir la última parte de tu campaña o Canvas, revisa sus detalles, pruébala y ¡envíala!

## Lo que debes saber

### Errores, lógica de reintento y tiempos de espera

Los webhooks dependen de que los servidores Braze realicen solicitudes a un punto final externo, y ocasionalmente pueden producirse errores. Los errores más comunes incluyen errores de sintaxis, claves de API caducadas, límites de tasa y problemas inesperados del lado del servidor. Antes de enviar una campaña webhook:

- Comprueba si hay errores de sintaxis en tu webhook
- Garantizar que las variables personalizadas tengan valores predeterminados

Si tu webhook no se envía, se registra un mensaje de error en el [Registro de actividad de mensajes]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/), e incluye detalles como la marca de tiempo del error, el nombre de la aplicación y detalles sobre el error.

Error de webhook con el mensaje "Debe utilizarse un token de acceso activo para consultar información sobre el usuario actual".]({% image_buster /assets/img_archive/webhook-error.png %})

Si el mensaje de error no es lo suficientemente claro en cuanto al origen del error, debes consultar la documentación del punto final de la API que estás utilizando. Suelen ofrecer una explicación de los códigos de error que utiliza el punto final, así como su causa habitual.

#### Códigos de respuesta y lógica de reintento

Cuando se envíe la solicitud de webhook, el servidor receptor devolverá un código de respuesta que indicará qué ha ocurrido con la solicitud. La siguiente tabla resume las diferentes respuestas que puede enviar el servidor, cómo afectan a los análisis de la campaña y si, en caso de error, Braze intentará volver a entregar la campaña:

| Código de respuesta | ¿Marcado como recibido? | ¿Reintentos? |
|---------------|-----------|----------|
| `20x` (éxito)  | Sí |   N/A  |
| `30x` (redirección)  | No | No |
| `408` (tiempo de espera de la solicitud)  | No | Sí |
| `429` (tasa limitada)  | No | Sí |
| `Other 4XX` (error del cliente)  | No | No |
| `5XX` (error del servidor)   | No | Sí |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Braze reintenta los códigos de estado anteriores hasta cinco veces en 30 minutos utilizando la retirada exponencial. Si no podemos llegar a tu punto final, los reintentos pueden extenderse durante un periodo de 24 horas.<br><br>Cada webhook dispone de 90 segundos antes de que se agote su tiempo de espera.
{% endalert %}

#### Solución de problemas y detalles adicionales sobre errores

Para obtener explicaciones detalladas, pasos para la solución de problemas y orientación para resolver errores específicos de webhook, consulta [Solución de problemas de webhook y solicitudes de contenido conectado]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors/). También encontrarás más explicaciones sobre cómo funciona nuestro sistema de detección de host insalubre y cómo Braze proporciona notificaciones de errores mediante correos electrónicos automatizados y registro adicional en Braze Currents.

### Lista de IP permitidas {#ip-allowlisting}

Cuando se envía un webhook desde Braze, los servidores Braze realizan solicitudes de red a nuestros clientes o a servidores de terceros. Con IP allowlisting, puedes verificar que las solicitudes de webhook proceden de Braze, añadiendo una capa de seguridad.

Braze enviará webhooks desde las siguientes IP. Las IP de la lista se añaden automática y dinámicamente a cualquier clave de API que haya sido objeto de adhesión voluntaria a la lista permitida.

{% alert important %}
Si estás haciendo un webhook Braze to Braze y utilizas allowlisting, debes permitir todas las IP siguientes, incluida `127.0.0.1`.
{% endalert %}

{% multi_lang_include data_centers.md datacenters='ips' %}

### Utilizar webhooks con socios Braze {#utilizing-webhooks}

Hay muchas formas de utilizar webhooks, y con nuestros socios tecnológicos (Alloys), puedes utilizar webhooks para subir el nivel de tu comunicación directamente con tus clientes y usuarios.

Compruébalo:
* [Messenger]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/remerge/)
* [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/)
* ¡Y muchos más de nuestros [socios tecnológicos]({{site.baseurl}}/partners/home/)!


