---
nav_title: Acerca de Webhooks
article_title: Acerca de Webhooks
page_order: 0
channel:
  - webhooks
description: "Este artículo de referencia cubre los aspectos básicos de los webhooks, incluidos los casos de uso comunes, la anatomía de los webhooks y cómo utilizarlos en Braze."

---

# [![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}Acerca de los Webhooks

> Este artículo de referencia cubre los aspectos básicos de los webhooks para darte los bloques de construcción que necesitas para crear los tuyos propios. ¿Busca pasos para crear un webhook en Braze? Consulte [Creación de un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

Los webhooks son una forma habitual de comunicación entre aplicaciones para compartir datos en tiempo real. En los tiempos que corren, rara vez disponemos de una aplicación independiente que pueda hacerlo todo. La mayoría de las veces, trabajas con muchas aplicaciones o sistemas diferentes que están especializados en realizar determinadas tareas, y todas estas aplicaciones tienen que poder comunicarse entre sí. Ahí es donde entran en juego los webhooks.

Un webhook es un mensaje automatizado de un sistema a otro cuando se cumplen determinados criterios. En Braze, este criterio suele ser la activación de un evento personalizado.

En esencia, un webhook es un método basado en eventos para que dos sistemas distintos tomen medidas eficaces basadas en datos transmitidos en tiempo real. Ese mensaje contiene instrucciones que indican al sistema receptor cuándo y cómo realizar una tarea específica. Por este motivo, los webhooks pueden proporcionarle un acceso más dinámico y flexible a los datos y a la funcionalidad programática, y permitirle configurar recorridos del cliente que agilicen los procesos.

## Ejemplos

Los webhooks son una forma excelente de conectar tus sistemas entre sí; al fin y al cabo, los webhooks son la forma en que se comunican las aplicaciones. He aquí algunos escenarios generales en los que los webhooks pueden resultar especialmente útiles:

- Envío de datos a y desde Braze
- Envío de mensajes a sus clientes a través de canales no compatibles directamente con Braze
- Publicar en las API Braze

Algunos casos de uso más específicos son los siguientes:

- Si un usuario se da de baja del correo electrónico, puede hacer que un webhook actualice su base de datos de análisis o CRM con esa misma información, garantizando una visión holística del comportamiento de ese usuario.
- Envía [mensajes transaccionales]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) a los usuarios dentro de Facebook Messenger o Line.
- Envíe correo directo a los clientes en respuesta a su actividad en la aplicación y en la Web utilizando webhooks para comunicarse con servicios de terceros como [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- Si un jugador alcanza un determinado nivel o acumula un cierto número de puntos, utilice webhooks y su configuración API existente para enviar una mejora de personaje o monedas directamente a su cuenta. Si envías el webhook como parte de una campaña de mensajería multicanal, puedes enviar un mensaje push o de otro tipo para informar al jugador de la recompensa al mismo tiempo.
- Si es una aerolínea, puede utilizar webhooks y su configuración de API existente para acreditar un descuento en la cuenta de un cliente después de que haya reservado un determinado número de vuelos.
- Un sinfín de recetas "If This Then That"[(IFTTT](https://ifttt.com/about)): por ejemplo, si un cliente inicia sesión en la aplicación a través del correo electrónico, esa dirección puede configurarse automáticamente en Salesforce.

## Anatomía de un webhook

Un webhook consta de las siguientes partes.

| Parte de Webhook | Descripción |
| --- | --- |
| [Método HTTP](#methods) | Al igual que las API, los webhooks necesitan métodos de solicitud. Se facilitan a la URL a la que accede el webhook, y le indican al punto final qué hacer con la información facilitada. Hay cuatro métodos HTTP que puede especificar: POST, GET, PUT y DELETE. |
| HTTP URL | La dirección URL del punto final de tu webhook. El endpoint es el lugar donde enviarás la información que estás capturando en el webhook. |
| Cuerpo de la solicitud | Esta parte del webhook contiene la información que estás comunicando al endpoint. El cuerpo de la solicitud puede ser pares clave-valor JSON o texto sin formato. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Ejemplo de webhook con un método HTTP, una URL HTTP y un cuerpo de solicitud.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### Métodos HTTP {#methods}

La siguiente tabla describe los cuatro métodos HTTP diferentes que puede especificar en su webhook.

| Método HTTP | Descripción |
| ----------- | ----------- |
| POST | Este método escribe nueva información en el servidor receptor. Un ejemplo común del método POST en una aplicación del mundo real es un [formulario de contacto](https://www.braze.com/company/contact) en un sitio web. Cualquier información que introduzcas en el formulario pasa a formar parte de un cuerpo de solicitud y se envía a un receptor. Es el método más utilizado para enviar datos.
| GET | Este método recupera información existente, en lugar de escribir información nueva. Por definición, una petición GET no admite un cuerpo de petición. Es el método más utilizado para pedir datos a un servidor. Por ejemplo, considera el [punto final `/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Si hiciera una petición GET, le devolvería una lista de sus segmentos.
| PUT | Este método actualiza la información en el endpoint, reemplazando cualquier información existente con lo que hay en el cuerpo de la solicitud. 
| ELIMINAR | Este método elimina el recurso de la URL HTTP. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Webhooks en Braze

En Braze, puedes crear un webhook como campaña de webhook, campaña API o componente Canvas.

{% tabs %}
{% tab Campaña de webhook %}

1. En el panel de control de Braze, vaya a **Campañas**.
2. Haga clic en **Crear campaña** y seleccione **Webhook**.

Consulte [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para obtener más información.

{% endtab %}
{% tab Campaña de API %}

1. En el panel de control de Braze, vaya a **Campañas**.
2. Haga clic en **Crear campaña** y seleccione **Campaña API**.
3. Haga clic en **Añadir mensajes** y seleccione **Webhook**.
4. Formatee su llamada a la API para incluir un [objeto webhook]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Consulte [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para obtener más información.

{% endtab %}
{% tab Componente de lienzo %}

1. En tu Canvas, crea un nuevo componente.
2. En la sección **Mensaje** de su componente, seleccione **Webhook**.

Consulte [Crear un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) para obtener más información.

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


