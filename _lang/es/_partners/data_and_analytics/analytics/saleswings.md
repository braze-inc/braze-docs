---
nav_title: SalesWings
article_title: SalesWings
description: "Este artículo de referencia describe la asociación entre Braze y SalesWings. SalesWings es una solución de operaciones de ventas y marketing para Braze que te ayuda a cualificar clientes potenciales y cuentas, y proporciona información y alertas de ventas dentro de CRM como Salesforce, así como informes de atribución B2B. Puedes aprovechar los intereses y la interacción dentro de Braze para la personalización en Canvas y la segmentación. SalesWings también ofrece una forma de generar clientes potenciales desde un sitio web, similar a Digioh."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) es una solución SaaS B2B de operaciones de ventas y marketing que ayuda a gestionar la cualificación de clientes potenciales y cuentas mediante la puntuación y clasificación holística de clientes potenciales y proporciona información y alertas de ventas e informes de atributo B2B, junto con una estrecha integración con Salesforce CRM.  Un complemento de interacción con el sitio web, similar a Digioh, te permite generar clientes potenciales en el sitio web. Puedes aprovechar los intereses e interacciones dentro de Braze para la personalización en Canvas y la segmentación.

_Esta integración está mantenida por SalesWings._

## Sobre la integración

SalesWings permite a los equipos de marketing y a los administradores de operaciones de marketing cualificar clientes potenciales y cuentas para sus equipos de ventas, algo esencial para la alineación de ventas y marketing y la eficacia operativa. Además, SalesWings, junto con Braze, puede mostrar a los representantes de ventas el recorrido completo del cliente y los datos de interacción con los clientes potenciales y las campañas de marketing de Braze, lo que te permite aumentar las tasas de cualificación de clientes potenciales mediante conversaciones más informadas. SalesWings identifica las necesidades e intereses junto con otras señales, lo que permite el traspaso de compradores cualificados a equipos de ventas dentro de tu CRM de forma automatizada. Puedes utilizar las necesidades, intereses y disposición para las ventas identificados como atributos del usuario Braze para la personalización y segmentación.

## Requisitos previos
 
| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta SalesWings | Se necesita una cuenta de [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) para beneficiarse de esta asociación. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.export.ids` (y `users.track` si utilizas la característica push de información de SalesWings). <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
| Cuenta Segment.com (opcional) | Si eres usuario de Segment.com, puedes enviar todos los datos de interacción y perfil de los clientes potenciales e identificar eventos a través de Segment.com para crear perfiles de clientes potenciales. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

{% tabs %}
{% tab Lead and Account Scoring %}

SalesWings proporciona a los clientes de Braze [una forma flexible de cualificar prospectos, contactos y cuentas con capacidades de puntuación y clasificación de prospectos de última generación](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs). Todos tus datos de cualificación de clientes potenciales se envían de forma nativa a Salesforce CRM y a otros sistemas en los que desees gestionar e informar sobre clientes potenciales, contactos, cuentas y oportunidades.

![Ejemplo de un modelo sencillo de puntuación de clientes potenciales sin código de clic en SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Ejemplo de un modelo sencillo de puntuación de clientes potenciales sin código de clics en SalesWings_
{% endtab %}
{% tab Sales and Marketing Alignment %}
SalesWings permite a los equipos de marketing realizar un seguimiento de los clientes potenciales cualificados para marketing, cualificarlos y entregarlos a los equipos de ventas. Todos los datos de SalesWings se envían de forma nativa a Salesforce y pueden aprovecharse para ajustar cualquier proceso existente o crear nuevos procesos mediante listas, informes, flujos, etc.

![Ejemplo de cómo la puntuación de clientes potenciales de SalesWings prioriza una lista de clientes potenciales o contactos de forma nativa dentro de Salesforce]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Ejemplo de cómo la puntuación de contactos de SalesWings prioriza una lista de leads o contactos de forma nativa dentro de Salesforce_

![Ejemplo de cómo la puntuación de clientes potenciales de SalesWings prioriza una lista de cuentas de forma nativa en Salesforce]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Ejemplo de cómo la puntuación de clientes potenciales de SalesWings prioriza una lista de cuentas de forma nativa en Salesforce_
{% endtab %}
{% tab Lead and Account Grading %}
SalesWings permite a los clientes de Braze cualificar clientes potenciales y cuentas basándose en datos de perfil (normalmente datos de CRM). También se denomina "calificación de clientes potenciales", "puntuación de ajuste" o "puntuación firmográfica". Los clientes de Braze pueden enviar datos de atributos directamente a SalesWings, y SalesWings puede leer cualquier dato y registro de objetos estándar o personalizados de Salesforce CRM para la puntuación holística de perfiles.
{% endtab %}
{% tab Sales Insights for Sales Reps %}
SalesWings te habilita para mostrar a tus representantes de ventas información sobre sus clientes potenciales, contactos y cuentas (alternativa a Marketo Sales Insights). Básicamente, puedes mostrar a tu equipo de ventas cualquier dato de interacción de Braze y de la Web. La información está integrada de forma nativa en Salesforce CRM y puede enviarse a otros CRM o sistemas, o a través de un correo electrónico Braze como "alerta de ventas".

![Ejemplo de vista de información de ventas para representantes de ventas en Salesforce (también disponible para otros sistemas CRM)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Ejemplo de vista de información de ventas para representantes de ventas en Salesforce (también disponible para otros sistemas CRM)_
{% endtab %}
{% tab Sales Alerts %}
SalesWings ofrece alertas nativas por correo electrónico y Slack, y puedes configurar suscripciones a informes en Salesforce a las que tu equipo de ventas puede acceder para obtener informes diarios, semanales y mensuales por correo electrónico. Además, a través de una integración de Zapier, puedes crear flujos de trabajo adicionales basados en los datos de cualificación de clientes potenciales de SalesWings.

![Ejemplo de alerta de ventas a través del canal Slack]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Ejemplo de alerta de ventas a través del canal Slack_
{% endtab %}
{% tab Reporting in Salesforce CRM %}
A través de la integración nativa de SalesWings con Salesforce, puedes crear informes automatizados con clientes potenciales, contactos, cuentas y oportunidades basados en datos de interacción Web y cualquier interacción de campaña de Braze con una integración nativa de Currents. Por ejemplo, puedes mostrar una lista de clientes potenciales a un equipo de ventas, con todos los que hayan hecho clic en una campaña de correo electrónico específica o hayan realizado una acción concreta en tu aplicación o sitio web.

![Ejemplo de panel vinculado a la interacción de marketing por correo electrónico Braze & dentro de Salesforce, que analiza el impacto de las campañas Braze en los resultados y las ventas]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Ejemplo de panel vinculado al correo electrónico Braze & con la interacción de marketing en Salesforce, que analiza el impacto de las campañas Braze en los resultados y las ventas_
{% endtab %}
{% endtabs %}

## Integración

### Paso 1: Cuenta y configuración de SalesWings

[Programa una demostración](https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs) con el amable equipo de SalesWings para saber más sobre SalesWings.

### Paso 2: Instalar el seguimiento del comportamiento en tu sitio web o aplicación

Hay varias formas de recopilar datos de comportamiento en SalesWings para la puntuación de clientes potenciales y cuentas, la identificación de la intención del comprador y la información de ventas:
* [Despliega el JavaScript de seguimiento de SalesWings](https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script) en los sitios web y aplicaciones en los que quieras seguir e identificar clientes potenciales
* Ingesta de eventos Braze junto con propiedades del evento en SalesWings a través de Braze Currents
* Envía datos de actividad de los clientes potenciales basados en el comportamiento (y datos del perfil de los clientes potenciales) a través de [la integración de SalesWings con Segment](https://support.saleswingsapp.com/en/articles/9258905-segment-com-integration)
* Envía datos directamente a la [API de](https://support.saleswingsapp.com/en/articles/6930889-using-saleswings-open-api-to-send-events-to-saleswings) SalesWings desde una solución de terceros

### Paso 3: Conexión de SalesWings con Braze

Ve a la [página**Integraciones de SalesWings**](https://helium.saleswings.pro/integrations) y amplía la sección **Integración Braze**.

![La sección Integración Braze de la página Configuración de SalesWings.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %})

Copia el valor de la columna **Identificador** de la clave recién creada y pégalo en el campo **Clave de API Braze** de la sección **Integración Braze** de SalesWings.

Añade tu punto final de API Braze como se describe en [el artículo Puntos finales de API y SDK]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints), e introdúcelo en el campo **Punto final de API Braze**. Copia el valor de la columna **Punto final REST** e introdúcelo en el campo **Punto final API Braze** de la sección **Integración Braze** de SalesWings.

A continuación, selecciona **Guardar**.

### Paso 4: Habilitar el push de información de SalesWings a Braze (opcional)

Si quieres que la información de SalesWings esté disponible en tus perfiles de usuario de Braze para la segmentación, personalización u orquestación de la travesía de Canvas, visita [la página**Integraciones de SalesWings**](https://helium.saleswings.pro/integrations) y amplía la sección **Integración de Braze**.

Haz clic en **Iniciar push de datos** en **Push de datos de información de SalesWings a Braze**.

### Paso 5: Configurar una exportación personalizada de Currents a SalesWings (opcional)

Si quieres utilizar [el comportamiento del usuario]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events) y los eventos de [interacción de mensajes]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events) para la inteligencia de comportamiento, la puntuación de clientes potenciales y cuentas, producir información de ventas o generar informes en tu CRM, ve a la [página**Integraciones de SalesWings**](https://helium.saleswings.pro/integrations) y amplía la sección **Integración de Braze**.

Selecciona **Generar** en **Generar un token de API para configurar una Exportación de Currents personalizada**.

A continuación, [crea una nueva Corriente]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents) y selecciona **Exportación de Corrientes personalizada** como tipo de Corriente.

En la sección **Credenciales** del formulario de creación actual, introduce el token de API que has generado en la [página**Integraciones de SalesWings**](https://helium.saleswings.pro/integrations) para **Token de portador**, y `https://helium.saleswings.pro/api/braze/currents/events` para **Punto final**.

### Paso 6: Configuración de la puntuación de clientes potenciales y cuentas de SalesWings para Braze, integración con CRM y mucho más

Consulta con el equipo de servicios de SalesWings para obtener un servicio completo de incorporación a través del [sitio web](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs).

## Uso de esta integración 

Para desencadenar la vinculación de datos de comportamiento y otros datos a clientes potenciales y cuentas, SalesWings debe identificar a un usuario en tu sitio web o aplicación, o a través de una integración de terceros. Esto puede ocurrir de las siguientes maneras:

- **Presentación de formularios:** Cuando un usuario envía un formulario Web, SalesWings identificará automáticamente todos tus tipos de formulario Web (como iniciar sesión, descargar, contactar con nosotros, etc.) y resolverá la identidad de un usuario cuando envíe un formulario. 
- **Clics en URL con un Braze ID o un ID externo:** Un usuario hace clic en una acción de marketing de Braze, normalmente clics de correo electrónico, clics de banner o similares, que conducen a una página que estás siguiendo con SalesWings.
- **Eventos de Braze Currents (opcional):** Si se configura la exportación de Currents personalizados a SalesWings, SalesWings creará un perfil identificador para cada usuario de Braze con un correo electrónico que tenga eventos enviados a la Corriente.
- **Seguimiento del correo electrónico de ventas mediante plugins de Gmail y Outlook (opcional):** Si decides dotar a tu representante de ventas de plugins de seguimiento de correo electrónico, pueden desencadenar el seguimiento completo del sitio web de los usuarios mediante el envío de enlaces rastreables.
- **Segment.com Identificador del evento (opcional):** Si eres usuario de Segment.com, también puedes resolver la identidad de un usuario con la integración de Segment.com.

### Identificación de usuarios a partir de clics en URL

Puedes identificar a los usuarios automáticamente cuando hagan clic en una URL rastreable (por ejemplo, envíos masivos por correo electrónico, banners con URL). Para hacer que una URL sea rastreable, hay dos formas de modificar las URL de tu sitio web en tus correos electrónicos, banners o SMS añadiendo el parámetro y el ID al final de tus enlaces.

1. Añadiendo `?braze_id=` seguido de {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Ejemplo de enlace:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Añadiendo `?br_user_id=` seguido de {% raw %}`{{${user_id}}}`{% endraw %}
  - **Ejemplo de enlace:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

La variable `braze_id` se establece en un identificador del usuario generado por Braze y está siempre disponible. La variable `br_user_id` se establece con el identificador del usuario en su sistema y puede faltar en ciertos escenarios (por ejemplo, para usuarios anónimos creados por el SDK Braze). Si en un enlace se utilizan tanto `braze_id` como `br_user_id`, SalesWings sólo tiene en cuenta el parámetro `braze_id`.

### Push de información de SalesWings a Braze

Si habilitas el push de información de SalesWings a Braze, SalesWings actualiza tus perfiles de usuario de Braze con los siguientes [atributos personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes):

| Atributo personalizado | Tipo | Descripción |
| ----------- | ----------- | ----------- |
| `sw_favorite` | booleano | Si el cliente potencial se marcó como favorito en SalesWings o Salesforce CRM |
| `sw_last_active_at` | date | El momento de la última actividad del cliente potencial en tu sitio web |
| `sw_lead_link_open` | cadena | El enlace para acceder al perfil de un cliente potencial en SalesWings (sin una cuenta en el panel de SalesWings) |
| `sw_lead_link_protected` | cadena | El enlace para acceder al perfil de un cliente potencial en SalesWings (con una cuenta en el panel de SalesWings) |
| `sw_lead_owner` | cadena | El propietario establecido para el cliente potencial en SalesWings o Salesforce CRM |
| `sw_lead_score` | float | El valor de la puntuación principal de clientes potenciales de SalesWings configurada en [el motor de reglas de](https://helium.saleswings.pro/falcon) SalesWings. |
| `sw_predictive_score` | cadena | El valor de [la puntuación predictiva](https://support.saleswingsapp.com/en/articles/581795-the-predictive-lead-score) de SalesWings que evalúa la interacción del cliente potencial en función del número y la frecuencia de las actividades de seguimiento. Los valores posibles son `HOT`, `WARM`, `NORMAL`, `COLD` o `FROZEN` |
| `sw_salesforce_record_id` | cadena | ID del registro de cliente potencial o contacto en Salesforce CRM |
| `sw_salesforce_record_url` | cadena | La URL del registro de cliente potencial o contacto en Salesforce CRM |
| `sw_session_count` | entero | El número de sesiones de seguimiento en tu sitio web para este cliente potencial |
| `sw_tags` | matriz de cadenas | Las necesidades e intereses que SalesWings identificó, representados como "etiquetas". Los nombres de las etiquetas SalesWings configuradas en [el motor de reglas](https://helium.saleswings.pro/falcon) SalesWings que se aplican a este cliente potencial |
| Atributos adicionales de puntuación de clientes potenciales | float | Un atributo personalizado por cada puntuación adicional de clientes potenciales configurada en el [motor de reglas de](https://helium.saleswings.pro/falcon) SalesWings. El nombre del atributo se deriva del nombre de la puntuación de SalesWings, por ejemplo, una puntuación llamada `Likeliness to meet` se envía como Atributo personalizado `sw_likeliness_to_meet`. Si cambias el nombre de una puntuación después de que el sistema la cree, SalesWings continúa la sincronización con el nombre inicial del atributo personalizado. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Cuando se habilita el push, SalesWings empieza a enviar inmediatamente atributos personalizados a Braze en cuanto cambian los puntos de datos subyacentes en los perfiles de clientes potenciales de SalesWings, y sincroniza progresivamente todos los clientes potenciales existentes aunque no tengan nuevas actualizaciones.

SalesWings actualiza cada usuario de Braze con un correo electrónico que coincide con la dirección de correo electrónico del perfil de cliente potencial de SalesWings. Si no hay usuarios coincidentes en Braze, SalesWings no crea uno nuevo. 

### Utilizar eventos Braze Currents en tu CRM

Si conectas una Braze Current a SalesWings, SalesWings creará perfiles de clientes potenciales identificados para cada usuario de Braze con un correo electrónico y registrará los eventos de Braze soportados como actividad de clientes potenciales. En tu CRM, todos los datos pueden agregarse automáticamente en el nivel de cuenta del cliente potencial. La actividad y los datos registrados podrían combinarse además con los datos de comportamiento recopilados con el script de seguimiento de SalesWings o Segment.com, o enviando otros datos a la API de SalesWings, y luego utilizarse para identificar las necesidades y la preparación para las ventas de tus clientes potenciales para tus procesos de gestión de clientes potenciales y cuentas.

La siguiente tabla muestra los tipos de eventos Braze admitidos por SalesWings y su representación en el historial de actividad de clientes potenciales y el motor de reglas de SalesWings:

| Categoría del evento | Tipo de evento | Nombre del evento en SalesWings |
| ----------- | ----------- | ----------- |
| Eventos de Canvas | Entradas | `[Nurturing] Added by marketing team onto the journey $canvas_name` |
| Eventos de comportamiento del cliente | Eventos personalizados | `[Custom Event tracked] $name` |
| Eventos de comportamiento del cliente | Primera sesión | `[User Action] Today marks the user's first session` |
| Eventos de comportamiento del cliente | Atribución de instalación | `[User Action] User installed app from $source` |
| Eventos de comportamiento del cliente | Eventos de compra | `[Purchase] Customer purchased $product_id for $price $currency` |
| Eventos de mensajes | Clic en tarjeta de contenido | `[Content Card engagement] Clicked on $campaign_name content card` |
| Eventos de mensajes | Rebote de correo electrónico | `[Alerting or negative] Email hard-bounced. This person's email appears to be no longer valid` |
| Eventos de mensajes | Clic en correo electrónico | `[Email campaign engagement] Clicked in email $campaign_name on $url` |
| Eventos de mensajes | Entrega del correo electrónico | `[Nurturing] Received email $campaign_name` |
| Eventos de mensajes | Apertura del correo electrónico | `[Email campaign engagement] Opened email $campaign_name` |
| Eventos de mensajes | Cancelación de suscripción del correo electrónico | `[Subscription status change] Unsubscribed from $campaign_name` |
| Eventos de mensajes | Clic en mensaje dentro de la aplicación | `[In-app campaign engagement] Clicked on message $campaign_name` |
| Eventos de mensajes | Apertura de notificaciones push | `[Push notification engagement] Clicked on notification $campaign_name` |
| Eventos de mensajes | SMS/MMS entrantes recibidos | `[SMS/mobile campaign engagement] We received a message from this person to our internal number $inbound_phone_number: $message_body` |
| Eventos de mensajes | Clic en enlace corto de SMS/MMS | `[SMS/mobile campaign engagement] Clicked on $short_url` |
| Eventos de mensajes | Recepción de WhatsApp | `[WhatsApp engagement] We received a message from this person to our WhatsApp number $inbound_phone_number: $message_body` |
| Eventos de mensajes | Lectura de WhatsApp | `[WhatsApp engagement] Lead read our message from the $campaign_name campaign` |
| Suscripciones | Cambio de estado de suscripción global | `[Subscription status change] Global marketing subscription setting set to $subscription_status` |
| Suscripciones | Cambio de estado de grupo de suscripción | `[Subscription status change] $subscription_status to/from $campaign_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

A continuación, puedes configurar las condiciones **Evento personalizado** > **Nombre del evento** y **Evento personalizado** > **Propiedad del evento** para las etiquetas y puntuaciones de SalesWings con los nombres de eventos de SalesWings de la tabla anterior. La lista de propiedades del evento disponibles para las condiciones se rellena previamente con algunas de las entradas más utilizadas, y siempre puedes añadir otras nuevas en la sección **Propiedad del evento** de la [página de configuración del motor de reglas](https://helium.saleswings.pro/falcon).

![Ejemplo de una condición de Nombre de Evento.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_custom_event_condition.png %})

Para la configuración y la solución de problemas adicionales, ponte en contacto con el [equipo de servicios de SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) para obtener ayuda sobre la incorporación.

