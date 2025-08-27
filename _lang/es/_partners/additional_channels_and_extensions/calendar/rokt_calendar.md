---
nav_title: Rokt Calendar
article_title: Rokt Calendar
alias: /partners/rokt_calendar/
description: "Este artículo de referencia describe la asociación entre Braze y Rokt Calendar, una tecnología de marketing de calendario dinámico que permite a las marcas impulsar eventos 1:1 y comunicaciones promocionales, en forma de eventos de calendario y notificaciones."
page_type: partner
search_tag: Partner
---

# Rokt Calendar

> [Rokt Calendar](https://www.rokt.com/rokt-calendar/) es una tecnología de marketing de calendario dinámico que permite a las marcas impulsar eventos 1:1 y comunicaciones promocionales en forma de eventos de calendario y notificaciones.

_Esta integración está mantenida por Rokt Calendar._

## Sobre la integración

La integración de Braze y Rokt Calendar permite que tus suscriptores de Rokt Calendar y sus datos sean enviados a Braze a través de Braze webhook. A continuación, puede utilizar estos datos en Braze Canvases para la segmentación de la audiencia y la segmentación de viajes utilizando cualquiera de los siguientes [atributos de Rokt Calendar](#audience-segmentation) personalizados. 

## Requisitos previos

| Requisito  | Descripción |
| ------------ | ----------- |
| Cuenta Rokt Calendar | Para beneficiarse de esta asociación es necesario disponer de una cuenta de Rokt Calendar específica para cada cliente. Póngase en contacto con [sales-calendar@rokt.com](mailto:sales-calendar@rokt.com) para hablar con un gestor de cuentas  |
| Configuración del Calendario Rokt | Tu gestor de cuentas de Rokt Calendar trabajará contigo para configurar el calendario de la forma que mejor se adapte a tus necesidades, incluyendo ajustes como:<br>\- Indicador de fusión<br>\- Indicador de error de ID de abonado<br>\- Captura de correo electrónico, si es necesario |
| Credenciales OAuth de Rokt Calendar | Esta clave proporcionada por el gestor de tu cuenta de Rokt Calendar te permitirá conectar tus cuentas de Braze y Rokt Calendar.<br><br>Puede crearse en el salpicadero de Braze, en **Configuración** > **Contenido conectado**. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. Deberás proporcionar esta clave al gestor de tu cuenta de Rokt Calendar.<br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| [Punto final REST Braze]({{site.baseurl}}/api/basics/#endpoints) | La URL de tu punto final REST. Tu punto final dependerá de la URL Braze de tu instancia. |
| ID de abonado externo | Es el identificador utilizado por el proceso de suscripción al Calendario Rokt para emparejar al suscriptor del calendario con el usuario Braze. Esto es algo que pasas a Rokt Calendar.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Segmentación de la audiencia {#audience-segmentation}

Cuando Rokt Calendar crea un nuevo usuario o hace coincidir un suscriptor existente con un usuario Braze, Rokt Calendar enviará los siguientes atributos de suscripción personalizados que puede filtrar dentro de Braze:

| Atributo personalizado  | Definición       | Ejemplo          |
| ----------------  | ---------------- | ---------------- |
| `rokt:account_code` | Código de la cuenta del Calendario Rokt | `brazetest/f5733866ade2` y `brazetest/ff10919f1078` |
| `rokt:account_id` |ID de la cuenta de Rokt Calendar | `d0ce4299-7d6c-4888-bfd8-c7e867a0fa6c/f5733866ade2` |
| `rokt:account_name` | Nombre de la cuenta de Rokt Calendar | `Braze Test/f5733866ade2` |
| `rokt:calendar_code` | Código del calendario Rokt | `test-calendar-1/f5733866ade2` |
| `rokt:calendar_id` | ID del calendario Rokt | `9a9007c7-f5a4-e811-b13c-06424c4f2724/f5733866ade2` |
| `rokt:calendar_title` | Título del calendario Rokt | `Test Calendar 1/f5733866ade2` |
| `rokt:country_code` | Código de país relacionado con la suscripción creada | `AU/f5733866ade2` |
| `rokt:device_name` | Tipo de dispositivo relacionado con la suscripción creada | `Desktop/f5733866ade2` |
| `rokt:geo_country` | País de origen relacionado con la suscripción creada | `Australia/f5733866ade2` |
| `rokt:optIn1` | Si el usuario ha optado por el primero de los 2 opt-ins relacionados con la suscripción creada | `True/f5733866ade2` |
| `rokt:optIn2` | Si el usuario ha optado por el segundo de los 2 opt-ins relacionados con la suscripción creada | `True/f5733866ade2` |
| `rokt:source` | La fuente de la suscripción creada | `brazetest.Rokt Calendarapp.com/f5733866ade2` |
| `rokt:subscriber_email` | La dirección de correo electrónico introducida por el usuario durante el proceso de suscripción | `test@email.com/f5733866ade2` |
| `rokt:subscription_id` | El ID de suscripción, que sirve como identificador único, relacionado con la suscripción creada | `06423672-b6ba-4536-aa36-70788a7a0a36` |
| `rokt:subscription_method` | Método de suscripción (webcal/Google) relacionado con la suscripción creada. | `WebCal/f5733866ade2` |
| `rokt:tags` | Etiquetas de calendario utilizadas relacionadas con la suscripción creada. | `Test Calendar 1/All Teams/f5733866ade2 and Test Calendar 1/TeamI//f5733866ade2` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Rokt Calendar también activará un evento personalizado `subscribe` tan pronto como el usuario se haya suscrito a su calendario Rokt que se puede utilizar tanto en la segmentación Braze o ser utilizado como un disparador para una campaña o componente Canvas.

## Integración

### Paso 1: Crear una audiencia de suscriptores del calendario

Para enviar eventos de calendario desde Canvas, primero debes tener configurado un calendario Rokt con usuarios ya suscritos. Para ello, deberá informar a sus usuarios de dónde y cómo suscribirse al calendario. Rokt Calendar te recomienda que:

#### Proporcionar puntos de integración de suscripciones
Para crear una audiencia de suscriptores al calendario, tendrá que ofrecer un destino al que el usuario pueda navegar y suscribirse. Algunos ejemplos de puntos de integración de suscripciones son:
  - Añada un botón de calendario a su sitio web
  - Añadir un enlace de calendario en un correo electrónico o SMS 
  - Añade un botón de calendario a tu aplicación
  - Añadir un enlace al calendario en las redes sociales

#### Promocionar el calendario
Para crear una audiencia de suscriptores, tendrás que promocionar el calendario entre tu público para que sepan cómo suscribirse. Algunos ejemplos de promoción de calendarios son:
  - Publicaciones en las redes sociales
  - Boletines y actualizaciones por correo electrónico
  - Entradas de blog
  - Notificaciones en la aplicación

### Paso 2: Crear un webhook de Calendario Rokt en Braze

En Braze, puede configurar una campaña webhook o un webhook dentro de un Canvas para cualquiera de los dos:

- Enviar un nuevo evento personalizado: Permite añadir nuevos eventos a un segmento de los calendarios de los abonados.
- Actualizar un evento personalizado: Permitir la actualización de un evento existente en los calendarios de los abonados.

Para crear una plantilla de webhook de Calendario Rokt para usar en futuras campañas o Lienzos, navega a **Plantillas** > **Plantillas de Webhook** en la plataforma Braze. 

Si desea crear una campaña de webhook de Calendario Rokt única o utilizar una plantilla existente, seleccione **Webhook** en Braze al crear una nueva campaña.

{% tabs %}
{% tab Enviar un nuevo evento %}
Una vez que hayas seleccionado la plantilla de webhook Rokt Calendar, deberías ver lo siguiente:
- **URL del webhook**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}`{% endraw %}
- **Cuerpo de la solicitud**: Texto sin procesar
{% endtab %}
{% tab Actualizar un evento existente %}
Una vez que hayas seleccionado la plantilla de webhook Rokt Calendar, deberías ver lo siguiente:
- **URL del webhook**: {% raw %}`{% assign accountCode = {{custom_attribute.${rokt:account_code}}}[0] | split: '/' | first %}https://api.roktcalendar.com/v1/subscriptionevent/{{accountCode}}/update`{% endraw %}
- **Cuerpo de la solicitud**: Texto sin procesar
{% endtab %}
{% endtabs %}

#### Encabezados de solicitud y método

Rokt Calendar requiere un `HTTP Header` para la autorización que incluya tu nombre de credencial de contenido conectado de Rokt Calendar. Lo siguiente ya estará incluido dentro de la plantilla como pares clave-valor, pero en la pestaña **Configuración**, debe sustituir `<Rokt-Calendar-API>` por el nombre de la credencial que se encuentra en `Manage Settings > Connected Content > Credential`.

{% raw %}
- **Método HTTP**: POST
- **Encabezado de solicitud**:
  - **Autorización**: Portador `{% connected_content https://api.roktcalendar.com/oauth2/token :method post :basic_auth <Rokt-Calendar-API> :body grant_type=client_credentials :save token :retry %}{{token.access_token}}`
  - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud

{% tabs local %}
{% tab Enviar un nuevo evento %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  },
  "subscriptionIds": ["{{custom_attribute.${rokt:subscription_id}| join: '","'  }}"]
}
```
{% endraw %}
{% endtab %}
{% tab Actualizar un evento existente %}
{% raw %}
```javascript
{% capture eventId %}Event_0001{% endcapture %}
{% capture eventTitle %}Event Title{% endcapture %}
{% capture eventDescr %}Event Description{% endcapture %}
{% capture eventLocation %}Event Location{% endcapture %}
{% capture eventStart %}2019-02-21T15:00:00{% endcapture %}
{% capture eventEnd %}2019-02-21T15:00:00{% endcapture %}
{% capture notifyBefore %}15{% endcapture %}
{% capture eventTZ %}Eastern Standard Time{% endcapture %}

{
  "event": {
    "eventId": "{{eventId}}_{{${user_id}}}",
    "title": "{{eventTitle}}",
    "description": "{{eventDescr}}",
    "location": "{{eventLocation}}",
    "start": "{{eventStart}}",
    "end": "{{eventEnd}}",
    "timezone": "{{eventTZ}}",
    "notifyBefore": "{{notifyBefore}}"
  }
}
```
{% endraw %}
{% endtab %}
{% tab Detalles del evento %}
Los siguientes campos incluyen información que puede personalizarse a nivel de evento.

| Campo             | Definición       | Ejemplo          |
| ----------------  | ---------------- | ---------------- |
| `eventId` <br>**\*Requerido** | Un identificador único para el evento que se va a añadir o actualizar | `Event_00001`
| `eventTitle` <br>**\*Requerido** | El título del evento tal y como aparecería en el calendario | Rebajas de verano 2019
| `eventDescr` | La descripción del acontecimiento tal y como aparecería en el calendario | La venta dura tres días; haz clic en este enlace `www.mybusiness.com/sale` para ver las ofertas. |
| `eventLocation` | La ubicación del evento tal y como aparecería en el calendario, tenga en cuenta que esto se utiliza a menudo como una segunda llamada a la acción, que es complementaria a la eventTitle. | Abre el evento para obtener un 50 % de descuento |
| `eventStart` <br>**\*Requerido**  | La fecha y hora de inicio del evento tal y como aparecerían en el calendario | `2019-02-21T15:00:00` |
| `eventEnd` <br>**\*Requerido**  | La fecha y hora de inicio del evento tal y como aparecerían en el calendario | `2019-02-21T16:00:00` |
| `eventTz` <br>**\*Requerido**  | La zona horaria del evento tal y como aparecería en el calendario, tenga en cuenta que la lista de zonas horarias aplicables se puede encontrar [aquí](https://roktcalendar-api.readme.io/docs/timezones). | `Eastern Standard Time` |
| `notifyBefore` <br>**\*Requerido**  | La hora de recordatorio del evento tal y como aparecería en el calendario, tenga en cuenta que se expresa en minutos | `15` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

{% alert tip %}
Para obtener una lista de zonas horarias válidas, consulta [https://roktcalendar-api.readme.io](https://roktcalendar-api.readme.io/reference/timezones)/reference/timezones.
{% endalert %}

### Paso 3: Vista previa de su solicitud

Previsualiza tu solicitud en el panel de **Previsualización** o navega a la pestaña de **Prueba**, donde puedes seleccionar un usuario al azar, un usuario existente, o personalizar el tuyo propio para probar tu webhook.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas webhook actualizadas pueden encontrarse en la lista **Plantillas webhook guardadas** al crear una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

