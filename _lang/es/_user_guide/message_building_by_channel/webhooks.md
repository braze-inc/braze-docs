---
nav_title: Webhooks
article_title: Webhooks
page_order: 4
layout: dev_guide
alias: /about_webhooks/
guide_top_header: "Webhooks"
guide_top_text: "Los webhooks son una forma habitual de comunicación entre aplicaciones, para compartir datos en tiempo real. En los tiempos que corren, rara vez tenemos una aplicación independiente que pueda hacerlo todo. La mayoría de las veces, trabajas con muchas aplicaciones o sistemas diferentes especializados en realizar determinadas tareas, y todas estas aplicaciones tienen que poder comunicarse entre sí. Ahí es donde entran en juego los webhooks. <br><br> Un webhook es un mensaje automatizado de un sistema a otro después de que se hayan cumplido determinados criterios. En Braze, este criterio suele ser el desencadenamiento de un evento personalizado. <br><br>En esencia, un webhook es un método basado en eventos para que dos sistemas distintos tomen medidas eficaces basadas en datos transmitidos en tiempo real. Ese mensaje contiene instrucciones que indican al sistema receptor cuándo y cómo realizar una tarea concreta. Por ello, los webhooks pueden proporcionarte un acceso más dinámico y flexible a los datos y a la funcionalidad programática, y te permiten configurar recorridos del cliente que agilizan los procesos. <br><br>**La disponibilidad de los webhooks depende de tu paquete Braze. Ponte en contacto con tu director de cuentas o administrador del éxito del cliente para empezar."
description: "Esta página de inicio alberga webhooks. Aquí puedes encontrar artículos sobre la creación de webhooks, la creación de plantillas de webhooks y webhooks Braze to Braze."
channel:
  - webhooks
search_rank: 3
guide_featured_title: "Artículos de sección"
guide_featured_list:
- name: Crear un webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: Crear una plantilla webhook
  link: /docs/user_guide/message_building_by_channel/webhooks/webhook_template/
  image: /assets/img/braze_icons/table.svg
- name: Webhooks Braze to Braze
  link: /docs/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
  image: /assets/img/braze_icons/switch-horizontal-01.svg
- name: Informar
  link: /docs/user_guide/message_building_by_channel/webhooks/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Solución de problemas de las peticiones webhook 
  link: /docs/help/help_articles/api/webhook_connected_content_errors/
  image: /assets/img/braze_icons/check-square-broken.svg
---

## [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"} Casos de uso

Los webhooks son una forma excelente de conectar tus sistemas; al fin y al cabo, los webhooks son la forma en que se comunican las aplicaciones. He aquí algunos escenarios generales en los que los webhooks pueden ser especialmente útiles:

- Envío de datos a y desde Braze
- Envío de mensajes a tus clientes a través de canales no soportados directamente por Braze
- Contabilización en las API Braze

Algunos casos de uso más específicos son los siguientes:

- Si un usuario cancela la suscripción a un correo electrónico, puedes hacer que un webhook actualice tu base de datos de análisis o CRM con esa misma información, garantizando una visión holística del comportamiento de ese usuario.
- Envía [mensajes transaccionales]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) a usuarios dentro de Facebook Messenger o Line.
- Envía correo directo a los clientes en respuesta a su actividad en la aplicación y en la Web utilizando webhooks para comunicarte con servicios de terceros como [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- Si un jugador alcanza un determinado nivel o acumula un determinado número de puntos, utiliza webhooks y tu configuración de API existente para enviar una mejora de personaje o monedas directamente a su cuenta. Si envías el webhook como parte de una campaña de mensajería multicanal, puedes enviar un push u otro mensaje para informar al jugador de la recompensa al mismo tiempo.
- Si eres una aerolínea, puedes utilizar webhooks y tu configuración de API existente para acreditar un descuento en la cuenta de un cliente después de que haya reservado un determinado número de vuelos.
- Un sinfín de recetas "If This Then That"[(IFTTT](https://ifttt.com/about)): por ejemplo, si un cliente se registra en la aplicación por correo electrónico, esa dirección puede configurarse automáticamente en Salesforce.

## Anatomía de un webhook

Un webhook consta de las siguientes partes.

| Parte de Webhook | Descripción |
| --- | --- |
| [Método HTTP](#methods) | Al igual que las API, los webhooks necesitan métodos de solicitud. Se facilitan a la URL a la que accede el webhook, y le indican al punto final qué hacer con la información facilitada. Puedes especificar cuatro métodos HTTP: POST, GET, PUT y DELETE. |
| URL HTTP | La dirección URL del punto final de tu webhook. El punto final es el lugar al que enviarás la información que estás capturando en el webhook. |
| Cuerpo de la solicitud | Esta parte del webhook contiene la información que estás comunicando al endpoint. El cuerpo de la solicitud puede ser pares clave-valor JSON o texto sin formato. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\![Ejemplo de webhook con un método HTTP, una URL HTTP y un cuerpo de solicitud.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### Métodos HTTP {#methods}

La siguiente tabla describe los cuatro métodos HTTP diferentes que puedes especificar en tu webhook.

| Método HTTP | Descripción |
| ----------- | ----------- |
| POST | Este método escribe nueva información en el servidor receptor. Un ejemplo común del método POST en una aplicación del mundo real es un [formulario de contacto](https://www.braze.com/company/contact) en un sitio web. Cualquier información que introduzcas en el formulario pasa a formar parte de un cuerpo de solicitud y se envía a un receptor. Es el método más utilizado para enviar datos.
| OBTENER | Este método recupera información existente, en lugar de escribir información nueva. Por definición, una petición GET no admite un cuerpo de petición. Es el método más utilizado para pedir datos a un servidor. Por ejemplo, considera el [punto final`/segments/list` ]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Si hicieras una petición GET, te devolvería una lista de tus segmentos.
| PUT | Este método actualiza la información del punto final, sustituyendo cualquier información existente por lo que hay en el cuerpo de la solicitud. 
| BORRAR | Este método borra el recurso de la URL HTTP. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Webhooks en Braze

En Braze, puedes crear un webhook como campaña de webhook, campaña API o componente Canvas.

{% tabs %}
{% tab Webhook Campaign %}

1. En el panel de Braze, ve a **Campañas**.
2. Haz clic en **Crear campaña** y selecciona **Webhook**.

Consulta [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para más información.

{% endtab %}
{% tab API Campaign %}

1. En el panel de Braze, ve a **Campañas**.
2. Haz clic en **Crear campaña** y selecciona **Campaña API**.
3. Haz clic en **Añadir mensajes** y selecciona **Webhook**.
4. Da formato a tu llamada a la API para incluir un [objeto webhook]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Consulta [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para más información.

{% endtab %}
{% tab Canvas Component %}

1. En tu Canvas, crea un nuevo componente.
2. En la sección **Mensaje** de tu componente, selecciona **Webhook**.

Consulta [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para más información.

{% endtab %}
{% endtabs %}

## Gestión de errores de webhook y límite de tasa

Cuando Braze recibe una respuesta de error de una llamada de webhook, ajustamos automáticamente el comportamiento de envío de ese webhook basándonos en estas cabeceras de respuesta:

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

Estas cabeceras nos ayudan a interpretar los límites de velocidad y a ajustar la velocidad de envío en consecuencia para evitar más errores. También aplicamos una estrategia de retirada exponencial para los reintentos, que ayuda a reducir el riesgo de saturar tus servidores espaciando los intentos de reintento en el tiempo.

Si detectamos que la mayoría de las solicitudes de webhook a un host específico están fallando, aplazaremos temporalmente todos los intentos de envío a ese host. Después, reanudaremos el envío tras un periodo de enfriamiento definido, permitiendo que tu sistema se recupere.


