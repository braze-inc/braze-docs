--- 
nav_title: SesiónM
article_title: SesiónM
description: "Este artículo de referencia describe la asociación entre Braze y SessionM, una plataforma de interacción con los clientes y fidelización."
alias: /partners/sessionm/
page_type: partner
search_tag: Partner
--- 

# Plataforma de fidelización SessionM

> [SessionM](https://www.mastercardservices.com/en/capabilities/sessionm) es una plataforma de interacción con los clientes y fidelización que proporciona características de gestión de campañas y soluciones de gestión de la fidelización para ayudar a los especialistas en marketing a impulsar el alcance específico para aumentar la interacción y la ganancia.

## Requisitos previos

| Fuente | Requisito | Descripción |
| --- | --- | --- |
| Braze | Una clave de API REST Braze | Una clave de API REST de Braze con permisos `trigger_send`. Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Braze | Un punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la URL Braze de [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
| Braze y SessionM | Identificador coincidente | Para utilizar la integración, asegúrate de que tanto SessionM como Braze tienen un registro de los identificadores utilizados por cada plataforma. Las referencias a `user_id` corresponden al identificador de usuario de SessionM generado en el momento de la creación del perfil en SessionM. |
| SesiónM | Una cuenta de SessionM | Se necesita una cuenta de SessionM para beneficiarse de esta asociación. |
| SesiónM | Un punto final REST de SessionM Core | Tu punto final dependerá de la URL SessionM de tu instancia. Se puede crear en el panel SesiónM desde **Propiedades Digitales**. |
| SesiónM | Una clave de API REST SessionM Core | La clave de API SessionM asociada a tu instancia y a la integración Braze. Esta clave puede utilizarse para todas las llamadas basadas en el núcleo, incluidas las etiquetas. Se puede crear en el panel SesiónM desde **Propiedades Digitales**. |
| SesiónM | Un secreto de la API REST del núcleo SessionM | El secreto de la API SessionM asociado a tu instancia y a la integración de Braze. Esta clave puede utilizarse para todas las llamadas basadas en el núcleo, incluidas las etiquetas. Se puede crear en el panel SesiónM desde **Propiedades Digitales**. |
| SesiónM | Un punto final REST de SessionM Connect | Tu punto final dependerá de la URL SessionM de tu instancia. Ponte en contacto con tu director de cuentas técnico de SessionM o con el equipo de entrega para que te lo proporcione. |
| SesiónM | Una cadena de autorización REST de SessionM Connect | La cadena de autorización básica de SessionM Connect asociada a tu instancia. Esta cadena de autenticación se puede utilizar para todas las llamadas basadas en connect, incluida get_user_offers. Ponte en contacto con tu director de cuentas técnico de SessionM o con el equipo de entrega para que te lo proporcione. |
| SesiónM | A SesiónM Connect REST ID de minorista | Un guid único que identifica al cliente específico asociado a tu instancia. Ponte en contacto con tu director de cuentas técnicas de SessionM o con el equipo de entrega. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/), puede crear una clave de API en **Consola de desarrollador** > **Configuración de API**.
{% endalert %} 

## Ejemplos

Los siguientes casos de uso muestran algunas formas de aprovechar la integración de SessionM y Braze.

- Crea una segmentación que incorpore datos de todas las plataformas de fidelización, gestión de clientes y mensajería.
- Utiliza una sólida segmentación para dirigirte a grupos específicos de usuarios con ofertas y promociones.
- Aprovecha la información más actualizada sobre usuarios, ofertas y fidelización al enviar mensajes.
- Proporciona notificaciones detalladas a los clientes sobre el progreso y la finalización de las actividades promocionales y de fidelización.
- Notifica a los clientes cuando se conceda una nueva oferta y proporciona los detalles de la misma.

## Integración de SessionM con Braze

### Paso 1: Crear un segmento en Braze

En Braze, crea un segmento de usuarios al que dirigirte con promociones y ofertas de SessionM. 

![Creador de segmentos con el filtro "Atributos personalizados" seleccionado.]({% image_buster /assets/img/sessionm/CreateSegment.png %})

### Paso 2: Importar segmentos Braze a SessionM

#### Opción 1: Exportar al punto final de la etiqueta SessionM (recomendado)

Primero, crea una campaña webhook en Braze y configura la URL del webhook en {% raw %}`{{endpoint_core}}/priv/v1/apps/{{appkey_core}}/users/{{${user_id}}}/tags`{% endraw %}. Utiliza Liquid para definir la dirección `user_id` dentro de la URL. 

Utilizando un **cuerpo de solicitud de** texto sin formato, compón el cuerpo del webhook para incluir las etiquetas deseadas que se añadirán al perfil de usuario en SessionM y el tiempo de vida deseado. Un ejemplo:

 ```
 {
   "tags":[
    "braze_test"
   ],
   "ttl":2592000
}
 ```

![]({% image_buster /assets/img/sessionm/SessionMWebhookComposer.png %}){: style="max-width:85%;"}

En la pestaña **Configuración**, añade los pares clave-valor para cada campo del encabezado de solicitud:
    \- Crea una clave `Content-Type` con su valor correspondiente `application/json`
    \- Crea una clave `Authorization` con un valor correspondiente `Basic YOUR-ENCODED-STRING-KEY`. Ponte en contacto con tu equipo de SessionM para obtener la clave de cadena codificada para tu punto final. 

![Configuración del webhook.]({% image_buster /assets/img/sessionm/SessionMWebhookSettings.png %}){: style="max-width:85%;"}

Programa tu entrega, configura tus **Audiencias** objetivo para que se dirijan al segmento [que creaste anteriormente](#step-1-create-a-segment-in-braze) y, a continuación, lanza tu campaña.

{% alert important %}
Este proceso también puede realizarse a través de un cliente API, como Postman, haciendo una solicitud directamente al [punto final de la etiqueta SessionM](https://docs.sessionm.com/developer/APIs/Core/Customers/customers_tags.htm#create-or-increment-a-customer-tag) especificando el cliente, el nombre de la etiqueta y un tiempo de vida para cada usuario en la llamada (un único usuario por llamada).
<br><br>
El siguiente ejemplo de petición utiliza cURL. 

{% raw %}
```bash
curl --location -g --request POST '{{endpoint_core}}/priv/v1/apps/{{apikey_core}}/users/{{user_id}}/tags' \
--header 'Content-Type: application/json' \
--header 'Authorization: Basic {{base64_encoded_string}}' \
--data-raw '{
"tags":[
"tagname1",
"tagname2"
],
"ttl":20000
}'
```
{% endraw %}
{% endalert %}

#### Opción 2: Importación CSV

Exporta tu segmento Braze utilizando el segmentador Braze y proporciona un archivo CSV a SessionM que contenga los clientes a etiquetar, el nombre de la etiqueta y un tiempo de vida para cada usuario del archivo.

## Recuperar la cartera de ofertas en tiempo real con Braze

La integración de SessionM con Braze permite extraer en tiempo real los datos de usuario de SessionM en el momento del envío del mensaje, mediante Contenido conectado, para eliminar el riesgo de comunicar a los clientes ofertas de fidelización caducadas, vencidas o ya canjeadas. 

El siguiente ejemplo muestra cómo se utiliza el Contenido conectado para crear una plantilla de datos de monedero de ofertas en un mensaje. Sin embargo, el Contenido conectado puede utilizarse con cualquiera de los puntos finales de Conexión de SessionM. 

### Paso 1: Emitir oferta en SesiónM

SessionM emite ofertas a los clientes a partir de varias palancas internas diferentes que pueden configurarse. Una vez emitidas, las ofertas pasan a un estado que SessionM denomina "cartera de ofertas".

Un cliente debe completar la acción requerida o cumplir el objetivo y se le emite la oferta dentro de SessionM.

A continuación, SessionM añade la oferta al monedero del cliente en el estado emitido.

### Paso 2: Llamar a la API del monedero de oferta SessionM

En el paso en Canvas o campaña con las ofertas de SessionM, utiliza [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/) para hacer una llamada a la API al [punto final de SessionM `get_user_offers` ](https://domains-connecteast1.ent-sessionm.com/offers/swagger/ui/index#!/InfoV232583210323232323232323232323232This32API32allows32for32the32querying32of32information32about32offers32in32a32read45only32fashion4610323232323232323232323232May32be32initiated32by32the32dashboard32or32the32mobile32app4610323232323232323232323232/InfoV2_GetUserOffers/).

En la solicitud de contenido conectado, especifica la SessionM `user_id` del usuario y tu `retailer_id` para recuperar la lista completa de ofertas activas que el cliente tiene en su monedero. Cada solicitud a este punto final puede incluir un único usuario. Ponte en contacto con el equipo de SessionM para obtener la clave de cadena codificada para la cabecera de autorización básica en tu llamada de contenido conectado.

En el cuerpo de la solicitud, `culture` está predeterminado a `en-US`, pero puedes utilizar Liquid para crear una plantilla con el idioma del usuario para las ofertas multilingües de SessionM (por ejemplo, utilizando {% raw %}`"culture":"{{${language}}}"`{% endraw %}).

{% raw %}
```
{% capture postbody %}
{"retailer_id":"YOUR-RETAIL-ID","user_id":"{{${user_id}}}","skip":0,"take":1000,"include_pending_extended_data":false,"culture":"en-US"}
{% endcapture %}

{% connected_content
     {{endpoint_connect}}/offers/api/2.0/offers/get_user_offers
:method post     
:headers {
       "Content-Type": "application/json",
       "Authorization": "Basic YOUR-BASE64-ENCODED-KEY"
  }
     :body {{postbody}}
     :save wallet
%}
```
{% endraw %}

### Paso 3: Rellenar el monedero de ofertas a la mensajería Braze

Tras realizar una solicitud al punto final, SessionM devuelve la lista completa de ofertas en el estado emitido, junto con los detalles completos de cada oferta. Este es un ejemplo de respuesta devuelta:

{% raw %}
```
{
    "status": "ok",
    "payload": {
      "user": {
        "opted_in": false,
        "activated": false,
        ...
      },
      "user_id": "00000000-0000-0000-0000-000000000000",
      "user_offers": [
        {
          "offer_id": "1a2b3324-1da6-4e49-b921-afc386dabb60",
          "offer_group_id": "00000000-0000-0000-0000-000000000000",
          "offer_type": "manual_fulfillment",
          ...
        }
      ],
      "total_records": 1,
      "offer_groups": [
        {
          "id": "00000000-0000-0000-0000-000000000000",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "offer_categories": [
        {
          "id": "9a82f973-aae6-4e10-839b-7117a852cf9e",
          "name": "All Offers",
          "sort_order": 0
        }
      ],
      "total_points": 1000,
      "available_points": 100
    }
}
```
{% endraw %}

Utilizando la notación de puntos Liquid, esto se puede introducir en el mensaje. Por ejemplo, para personalizar el mensaje con el resultado `offer_id`, podrías aprovechar la carga útil de retorno utilizando {% raw %}`{{wallet.payload.available_points}`{% endraw %}, que devuelve `100`.

{% alert note %}
Se trata de una API individual. Si tienes intención de enviar un lote de más de 500 usuarios, ponte en contacto con tu equipo de cuenta de SessionM para informarte sobre cómo incorporar datos masivos en la integración.
{% endalert %}

## Configuración de la mensajería desencadenada

La integración entre SessionM y Braze permite que los datos de perfil de usuario, los detalles de la oferta y los saldos de puntos se rellenen dinámicamente en los mensajes y se envíen en tiempo real al cliente en el punto de acción.

### Paso 1: El equipo de entrega de SessionM configura las plantillas

Colabora con tu equipo de entrega de SessionM para desarrollar plantillas que puedas utilizar en tu mensajería desencadenada. SessionM insertará datos de perfil de usuario, detalles de la oferta y saldos de puntos en la mensajería y los desencadenará en Braze para la mensajería de clientes en tiempo real.

Los campos estándar presentes en todas las plantillas de SessionM incluyen:
- `canvas_id`
- `campaign_id`
- `broadcast flag`
- `customer identifier`
- `email address`

{% alert note %}
Al configurar `broadcast flag` en `true`, el mensaje se enviará a todo el segmento al que se dirija la campaña o Canvas en Braze.
{% endalert %}

Se pueden configurar campos adicionales en función de necesidades específicas:

- **Ofrecer datos:** `offer_id`, `offer title`, `user offer id`, `description`, `terms and conditions`, `logo`, `pos discount id`, `expiration date`
- **Punto de datos de adjudicación:** `point award amount`, `point account name`
- **Datos del evento desencadenante:** Cualquier dato del evento desencadenante que utilice el resultado de desencadenar/enviar webhook
- **Datos específicos de la campaña:** `campaign runtime`, `campaign_id`, `campaign name`, `campaign custom data`

Los campos adicionales se envían a Braze como `trigger_properties` para personalizar el mensaje. 

### Paso 2: Crea una campaña o Canvas de Braze

Crea una campaña activada por la API o un Canvas en Braze para que lo desencadene SessionM. Si se han configurado campos adicionales, como `offer_id` o `offer title`, utiliza Liquid (como {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %}) para añadir los campos personalizados a tu mensajería.

![Propiedades de desencadenar API.]({% image_buster /assets/img/sessionm/apiTriggerProperties.png %})

En la pestaña **Programar entrega**, anota el ID de la campaña o del Canvas, ya que se añadirá a la **Configuración avanzada de** la campaña SessionM.

![Campaña desencadenada por la API.]({% image_buster /assets/img/sessionm/apiTriggerCampaign.png %})

Finaliza los detalles de tu campaña o Canvas y selecciona **Lanzar**. 

### Paso 3: Crea una campaña promocional o de mensajería de SessionM

A continuación, crea tu campaña en SessionM.

![SesiónM Creación de campaña.]({% image_buster /assets/img/sessionm/SessionMCampaignCreation.png %})

Actualiza la configuración avanzada de la campaña SessionM para incluir la siguiente carga útil JSON que contiene la dirección `braze_campaign_id` o `braze_canvas_id`.

{% raw %}
```
{
"braze_campaign_id": "{{CAMPAIGN ID}}",
"braze_canvas_id": "{{CANVAS ID}}",
}
```
{% endraw %}

![Configuración avanzada de SessionM.]({% image_buster /assets/img/sessionm/SessionMAdvancedSettings.png %}){: style="max-width:85%;"}

Crea un desencadenador de mensajes en el horario o comportamiento deseado. A continuación, selecciona **Variante de mensajería Braze** como **Variante de mensajería** en el menú **Mensaje externo** para utilizar la plantilla.

![SesiónM mensaje externo.]({% image_buster /assets/img/sessionm/SessionMExternalMessage.png %})

Esta plantilla extrae los atributos estáticos y dinámicos relevantes y llama al punto final Braze.

![SesiónM Plantilla Braze.]({% image_buster /assets/img/sessionm/SessionMBrazeTemplate.png %}){: style="max-width:85%;"}
