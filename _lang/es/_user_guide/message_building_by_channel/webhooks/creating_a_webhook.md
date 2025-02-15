---
nav_title: Creación de un Webhook
article_title: Creación de un Webhook
page_order: 1
channel:
  - webhooks
description: "Este artículo de referencia explica cómo crear y configurar una campaña webhook."
search_rank: 2
---

# Crear una campaña webhook

> Crear una campaña de webhook o incluir un webhook en una campaña multicanal te permite desencadenar acciones no relacionadas con la aplicación proporcionando a otros sistemas y aplicaciones información en tiempo real. 

Puedes utilizar webhooks para enviar información a sistemas, como Salesforce o Marketo, o a tus sistemas backend. Por ejemplo, es posible que desee abonar una promoción en las cuentas de sus clientes después de que hayan realizado un evento personalizado un determinado número de veces.

{% alert tip %}
Para saber más sobre qué son los webhooks y cómo puedes utilizarlos en Braze, consulta [Acerca de los webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) antes de continuar.
{% endalert %}

## Paso 1: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para mensajes sencillos y únicos, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaña %}

**Pasos:**

1. Vaya a **Mensajería** > **Campañas** y seleccione **Crear campaña**.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), puedes encontrar **Campañas** en **Interacción**.
{% endalert %}

{:start="2"}
2\. Selecciona **Webhook** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3\. Ponle a tu campaña un nombre claro y significativo.
4\. (Opcional) Añade una descripción de cómo se utilizará esta campaña.
4\. Añade [equipos]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [Generador de informes]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/), puede filtrar por etiquetas concretas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puede elegir diferentes plantillas de webhook para cada una de sus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si todos los mensajes de su campaña van a ser similares o van a tener el mismo contenido, redacte su mensaje antes de añadir variantes adicionales. A continuación, puede seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Pasos:**

1. [Cree su lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de lienzos.
2. Una vez que haya configurado su lienzo, añada un paso en el constructor de lienzos. Nombra tu paso con algo claro y significativo.
3. Elija un [programa de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifique un retraso según sea necesario.
4. Filtra tu audiencia para este paso, según sea necesario. Puede afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso en el momento de enviar los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elija cualquier otro canal de mensajería que desee asociar a su mensaje.

{% endtab %}
{% endtabs %}

## Paso 2: Crea tu webhook

Puedes elegir crear un webhook desde cero, utilizar una plantilla existente o utilizar una de nuestras plantillas existentes. A continuación, crea tu webhook en la pestaña **Redactar** del editor.

La pestaña **Componer** consta de los siguientes campos:

- Idioma
- URL del webhook
- Método HTTP
- Cuerpo de la solicitud

![La pestaña "Redactar" con una plantilla de webhook de Facebook Messenger de ejemplo.]({% image_buster /assets/img_archive/webhook_compose.png %})

#### Idioma {#internationalization}

Se admite la [internacionalización][16] en la URL y en el cuerpo de la solicitud. Para internacionalizar tu mensaje, selecciona **Añadir idiomas** y rellena los campos obligatorios. 

Le recomendamos que seleccione sus idiomas antes de escribir el contenido para que pueda rellenar el texto donde corresponda en el Líquido. Para consultar nuestra lista completa de idiomas disponibles que puedes utilizar, consulta [Idiomas admitidos]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

#### URL del webhook

La URL del webhook, o URL HTTP, especifica tu punto final. El endpoint es el lugar donde enviarás la información que estás capturando en el webhook. 

Si desea enviar información a un proveedor, éste debe proporcionar esta URL en la documentación de su API. Si envías información a tus propios sistemas, comprueba con tu equipo desarrollador o de ingeniería que utilizas la URL correcta. 

Braze sólo permite URL que se comuniquen a través de los puertos estándar `80` (HTTP) y `443` (HTTPS).

##### Utilizar Liquid

Puede personalizar las URL de sus webhooks utilizando [Liquid][15]. En ocasiones, ciertos puntos finales pueden requerir que identifique a un usuario o que proporcione información específica del usuario como parte de su URL. Cuando utilices Liquid, asegúrate de incluir un [valor predeterminado][19] para cada dato específico del usuario que utilices en tu URL.

#### Método HTTP

El [método HTTP]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#methods) que debes utilizar variará en función del punto final al que envíes información. En la mayoría de los casos, utilizarás POST.

#### Cuerpo de la solicitud

El cuerpo de la solicitud es la información que se enviará a la URL especificada. Puedes crear el cuerpo de tu solicitud de webhook con pares clave-valor JSON o texto sin formato.

##### Pares clave-valor JSON

Los pares clave-valor JSON te permiten escribir fácilmente una solicitud para un punto final que espera un formato JSON. Sólo puedes utilizarlo con un punto final que espere una petición JSON. Por ejemplo, si tu clave es `message_body`, el valor correspondiente podría ser `Your order just arrived!`. Una vez introducido el par clave-valor, el compositor configurará la solicitud en sintaxis JSON y se mostrará automáticamente una vista previa de la solicitud JSON.

![Cuerpo de la solicitud configurado con pares clave-valor JSON.]({% image_buster /assets/img/webhook_json_1.png %})

Puedes personalizar tus pares clave-valor utilizando Liquid, por ejemplo, incluyendo en tu solicitud cualquier atributo del usuario, [atributo personalizado][17] o [propiedad del evento][18]. Por ejemplo, puedes incluir el nombre y el correo electrónico de un cliente en tu solicitud. Asegúrate de incluir un [valor predeterminado][19] para cada atributo.

##### Texto bruto

La opción de texto sin formato le ofrece la flexibilidad de escribir una solicitud para un punto final que espera un cuerpo de cualquier formato. Por ejemplo, podrías utilizarlo para escribir una solicitud para un punto final que espera que tu solicitud esté en formato XML. 

Tanto la [personalización][15] como la [internacionalización][16] mediante Liquid son compatibles con el texto sin formato.

![Un ejemplo de un cuerpo de solicitud con texto sin procesar utilizando Liquid.]({% image_buster /assets/img_archive/webhook_rawtext.png %})

Si establece el [encabezado de solicitud](#request-headers-optional) `Content-Type` en `application/x-www-form-url-encoded`, el cuerpo de la solicitud debe tener formato de cadena codificada en URL. Por ejemplo:

{% raw %}
```
to={{custom_attribute.${example}}}&text=Your+order+just+arrived
```
{% endraw %}

![Cuerpo de la solicitud con cadena codificada en URL.]({% image_buster /assets/img_archive/webhook_rawtext_URL-encoded.png %})

## Paso 3: Configurar ajustes adicionales

#### Encabezados de solicitud (opcional)

Algunos puntos finales pueden requerir que incluya cabeceras en su solicitud. En la sección **Componer** del compositor, puedes añadir tantas cabeceras como necesites.

![Ejemplos de encabezados de solicitud para las claves "Autorización" y "Tipo de contenido".]({% image_buster /assets/img_archive/webhook_request_headers_example.png %})

Las cabeceras de solicitud comunes son `Content-Type` especificaciones (que describen qué tipo de datos esperar en el cuerpo, como XML o JSON) y cabeceras de autorización que contienen sus credenciales con su proveedor o sistema. 

Las especificaciones de tipo de contenido deben utilizar la clave `Content-Type`. Los valores más comunes son `application/json` o `application/x-www-form-urlencoded`.

Las cabeceras de autorización deben utilizar la clave `Authorization`. Los valores habituales son {% raw %} `Bearer {{YOUR_TOKEN}}` o `Basic {{YOUR_TOKEN}}` {% endraw %}, donde `YOUR_TOKEN` son las credenciales proporcionadas por tu proveedor o sistema.

## Paso 4: Pruebe a enviar su mensaje

Antes de lanzar la campaña, Braze recomienda probar el webhook para asegurarse de que el formato de la solicitud es correcto.

Para ello, cambie a la pestaña **Prueba** y envíe un webhook de prueba. Puede probar el webhook como un usuario aleatorio, un usuario específico (introduciendo su dirección de correo electrónico o ID de usuario externo) o un usuario personalizado con los atributos que usted elija.  

Después de enviar el webhook de prueba, aparecerá un diálogo con el mensaje de respuesta. Si la solicitud de webhook no tiene éxito, consulte el mensaje de error para obtener ayuda en la solución de problemas de su webhook. El siguiente ejemplo detalla la respuesta de un webhook con una URL de webhook inválida.

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
{% tab Campaña %}

A continuación, ¡construye el resto de tu campaña! Consulte las secciones siguientes para obtener más información sobre la mejor manera de utilizar nuestras herramientas para crear webhooks.

#### Elige la programación o desencadenante de la entrega

Los webhooks se pueden entregar en función de una hora programada, de una acción o de un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes configurar la duración de la campaña y [las horas tranquilas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

En este paso también puede especificar controles de entrega, como permitir que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña o activar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Elige los usuarios a los que dirigirte

A continuación, tienes que [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. En este paso, seleccionará la audiencia más amplia de sus segmentos, y reducirá aún más ese segmento con nuestros filtros, si así lo desea. Automáticamente obtendrá una instantánea de cómo es la población de ese segmento aproximado en este momento. Tenga en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

#### Elegir eventos de conversión

Braze le permite realizar un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), tras recibir una campaña. Tiene la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

{% endtab %}

{% tab Canvas %}

Si aún no lo ha hecho, complete las secciones restantes de su paso a Canvas. Para más detalles sobre cómo construir el resto de su Canvas, implementar pruebas multivariantes y Selección Inteligente, y más, consulte el paso [Construya su Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación de Canvas.

{% endtab %}
{% endtabs %}

## Paso 6: Revisar y desplegar

Cuando hayas terminado de crear lo último de tu campaña o Canvas, revisa sus detalles, pruébala y ¡envíala!

## Lo que hay que saber

### Errores, lógica de reintentos y tiempos de espera

Los webhooks dependen de que los servidores Braze realicen solicitudes a un punto final externo, por lo que pueden producirse errores de sintaxis y de otro tipo. El primer paso para evitar errores de webhook es probar tu campaña webhook en busca de errores de sintaxis y asegurarte de que las variables personalizadas tienen un valor por defecto. Sin embargo, los webhooks pueden fallar debido a problemas como claves de API caducadas, límites de velocidad o errores inesperados del servidor. Si tu webhook no se envía, se registra un mensaje de error en el [Registro de actividad de mensajes][42].

Esta descripción contiene la hora en que se produjo el error, el nombre de la aplicación y el mensaje de error:

![Error de webhook con el mensaje "Debe utilizarse un token de acceso activo para consultar información sobre el usuario actual".]({% image_buster /assets/img_archive/webhook-error.png %})

Si el cuerpo del mensaje no es lo suficientemente claro en cuanto al origen del error, debes consultar la documentación del punto final de la API que estás utilizando. Suelen ofrecer una explicación de los códigos de error que utiliza el punto final, así como su causa habitual.

Al igual que otras campañas, Braze realiza un seguimiento de la entrega de sus campañas webhook y de las conversiones resultantes. Cuando se envía la solicitud de webhook, el servidor receptor devolverá un código de respuesta indicando qué ha ocurrido con la solicitud. 

La siguiente tabla resume las diferentes respuestas que puede enviar el servidor, cómo afectan a los análisis de la campaña y si, en caso de error, Braze intentará volver a entregar la campaña:

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
Para los errores de `5XX`, Braze reintentará el envío del webhook hasta 5 veces en 30 minutos utilizando la retirada exponencial. Para todos los demás errores, Braze seguirá reintentándolo durante un máximo de 24 horas.<br><br>Cada webhook dispone de 90 segundos antes de que se agote su tiempo de espera.
{% endalert %}

### Lista de IP permitidas {#ip-allowlisting}

Cuando se envía un webhook desde Braze, los servidores Braze realizan solicitudes de red a nuestros clientes o a servidores de terceros. Con listas de direcciones IP permitidas, puedes verificar que las solicitudes de webhook proceden de Braze, añadiendo una capa de seguridad.

Braze enviará webhooks desde las siguientes IPs. Las IP de la lista se añaden automática y dinámicamente a cualquier clave de API que haya sido objeto de adhesión voluntaria a la lista permitida.

{% alert important %}
Si estás haciendo un webhook de Braze a Braze y utilizas una lista permitida, debes permitir todas las IP siguientes, incluida `127.0.0.1`.
{% endalert %}

| Para las instancias `US-01`, `US-02`, `US-03`, `US-04`, `US-05`, `US-06` y `US-07`: |
|---|
| `127.0.0.1`
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
| `127.0.0.1`
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

### Utilizar webhooks con socios Braze {#utilizing-webhooks}

Hay muchas maneras de utilizar webhooks, y con nuestros socios tecnológicos (Alloys), puede utilizar webhooks para nivelar su comunicación directamente con sus clientes y usuarios.

Consulta:
* [Messenger]({{site.baseurl}}/partners/message_orchestration/additional_channels/instant_chat/messenger/)
* [Remerge]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/remerge)
* [Lob.com]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/lob)
* ¡Y muchos más de nuestros [socios tecnológicos]({{site.baseurl}}/partners/home/)!


[15]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[16]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/#additional-notes-and-best-practices
[18]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/
[42]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/
