---
nav_title: SalesWings
article_title: SalesWings
description: "Este artículo de referencia describe la asociación entre Braze y SalesWings, una plataforma de análisis, que te ayuda a realizar un seguimiento de la puntuación y la clasificación, información y alertas de ventas, alineación de marketing e informes de atribución B2B."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings][1] es un complemento de perfiles de clientes potenciales de B2B SaaS creado para equipos de marketing y ventas, que ayuda a gestionar la cualificación de clientes potenciales y cuentas mediante la puntuación y clasificación de clientes potenciales, información y alertas de ventas, alineación de marketing e informes de atribución B2B, junto con una estrecha integración con Salesforce CRM.

SalesWings permite a los equipos de marketing y a los directores de operaciones de marketing cualificar clientes potenciales y cuentas para sus equipos de ventas, algo esencial para la alineación y la eficacia de las ventas y el marketing. Además, SalesWings, junto con Braze, puede mostrar a los representantes de ventas el recorrido del cliente de un cliente potencial y los datos de interacción con la campaña de marketing de Braze, lo que te permite aumentar las tasas de cualificación de clientes potenciales mediante conversaciones más informadas.

## Requisitos previos
 
| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta SalesWings | Se necesita una cuenta de [SalesWings][1] para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.export.ids`. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST][2]. Tu punto final dependerá de la URL Braze de tu instancia. |
| Cuenta Segment.com (opcional) | Si eres usuario de Segment.com, puedes enviar todos los datos de interacción y perfil de los clientes potenciales e identificar eventos a través de Segment.com para crear perfiles de clientes potenciales. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

{% tabs %}
{% tab Puntuación de clientes potenciales %}

SalesWings proporciona a los clientes de Braze [una forma flexible de cualificar prospectos, contactos y cuentas con capacidades de puntuación y clasificación de prospectos de última generación](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs). Todos tus datos de cualificación de clientes potenciales se envían de forma nativa a Salesforce CRM y a otros sistemas en los que desees gestionar e informar sobre clientes potenciales, contactos, cuentas y oportunidades.

![Ejemplo de un sencillo modelo de puntuación de clientes potenciales sin código de clics en SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Ejemplo de un modelo sencillo de puntuación de clientes potenciales sin código de clics en SalesWings_
{% endtab %}
{% tab Alineación de ventas y marketing %}
SalesWings permite a los equipos de marketing realizar un seguimiento de los clientes potenciales cualificados para marketing, cualificarlos y entregarlos a los equipos de ventas. Todos los datos de SalesWings se envían de forma nativa a Salesforce y pueden aprovecharse para ajustar cualquier proceso existente o crear nuevos procesos mediante listas, informes, flujos, etc.

![Ejemplo de cómo la puntuación de contactos de SalesWings prioriza una lista de leads o contactos de forma nativa dentro de Salesforce]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Ejemplo de cómo la puntuación de contactos de SalesWings prioriza una lista de leads o contactos de forma nativa dentro de Salesforce_

![Ejemplo de cómo la puntuación de contactos de SalesWings prioriza una lista de leads o contactos de forma nativa dentro de Salesforce]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Ejemplo de cómo la puntuación de clientes potenciales de SalesWings prioriza una lista de cuentas de forma nativa en Salesforce_
{% endtab %}
{% tab Clasificación de clientes potenciales y cuentas %}
SalesWings permite a los clientes de Braze cualificar clientes potenciales y cuentas basándose en datos de perfil (normalmente datos de CRM). También se denomina "calificación de clientes potenciales", "puntuación de ajuste" o "puntuación firmográfica". Los clientes de Braze pueden enviar datos de atributos directamente a SalesWings, y SalesWings puede leer cualquier dato y registro de objetos estándar o personalizados de Salesforce CRM para la puntuación holística de perfiles.
{% endtab %}
{% tab Información sobre ventas para comerciales %}
SalesWings te habilita para mostrar a tus representantes de ventas información sobre sus clientes potenciales, contactos y cuentas (alternativa a Marketo Sales Insights). Básicamente, puedes mostrar a tu equipo de ventas cualquier dato de interacción de Braze y de la Web. La información está integrada de forma nativa en Salesforce CRM y puede enviarse a otros CRM o sistemas, o a través de un correo electrónico Braze como "alerta de ventas".

![Ejemplo de vista de información de ventas para representantes de ventas en Salesforce (también disponible para otros sistemas CRM)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Ejemplo de vista de información de ventas para representantes de ventas en Salesforce (también disponible para otros sistemas CRM)_
{% endtab %}
{% tab Alertas de ventas %}
SalesWings ofrece alertas nativas por correo electrónico y Slack, y puedes configurar suscripciones a informes en Salesforce a las que tu equipo de ventas puede acceder para obtener informes diarios, semanales y mensuales por correo electrónico. Además, a través de una integración de Zapier, puedes crear flujos de trabajo adicionales basados en los datos de cualificación de clientes potenciales de SalesWings.

![Ejemplo de alerta de ventas a través del canal Slack]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Ejemplo de alerta de ventas a través del canal Slack_
{% endtab %}
{% tab Informes en Salesforce CRM %}
Mediante la integración de SalesWings con Salesforce, puedes crear informes automatizados con clientes potenciales, contactos, cuentas y oportunidades basados en los datos de interacción Web y en la interacción de la campaña Braze. Por ejemplo, puedes mostrar una lista de clientes potenciales a un equipo de ventas, con todos los que hicieron clic en una campaña de correo electrónico específica o realizaron una acción concreta en tu aplicación o sitio web.

![Ejemplo de panel de control vinculado a la participación del correo electrónico y el marketing de Braze en Salesforce, que analiza el impacto de las campañas de Braze en los resultados de ventas]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Ejemplo de panel vinculado a la interacción de correo electrónico y marketing de Braze en Salesforce, que analiza el impacto de las campañas de Braze en los resultados de las ventas_
{% endtab %}
{% endtabs %}

## Integración

### Paso 1: Cuenta y configuración de SalesWings

[Programa una demostración][4] con el amable equipo de SalesWings para saber más sobre SalesWings.

### Paso 2: Instalar el seguimiento del comportamiento en tu sitio web o aplicación

Actualmente, existen dos formas de recopilar datos de comportamiento en SalesWings para la puntuación de clientes potenciales y la información de ventas:
* [Despliega el JavaScript de seguimiento de SalesWings][5] en los sitios web y aplicaciones en los que quieras seguir e identificar clientes potenciales
* Envía datos de actividad de clientes potenciales basados en el comportamiento (y datos de perfiles de clientes potenciales) mediante la integración de SalesWings con Segment.com

### Paso 3: Conexión de SalesWings con Braze

Ve a la [página**Configuración de SalesWings**][6] y amplía la sección **Integración Braze**.

![La sección Integración Braze de la página Configuración de SalesWings.][7]

Copia el valor de la columna **Identificador** de la clave recién creada y pégalo en el campo **Clave de API Braze** de la sección **Integración Braze** de SalesWings.

Añade tu punto final de la API Braze como se describe en [Artículo sobre puntos finales de la API y el SDK][8], e introdúcelo en el campo **Punto final de la API Braze**. Copia el valor de la columna **Punto final REST** e introdúcelo en el campo **Punto final API Braze** de la sección **Integración Braze** de SalesWings.

A continuación, haz clic en **Guardar cambios** en la configuración de SalesWings.

### Paso 4: Configuración de la puntuación de clientes potenciales de SalesWings para Braze, integración con CRM, etc.

Consulta con el equipo de servicios de SalesWings para obtener un servicio completo de incorporación a través del [sitio web][1].

## Mediante esta integración 

Para activar la puntuación de clientes potenciales y la creación de perspectivas de ventas, SalesWings debe identificar a un usuario en tu sitio web o aplicación. Esto puede ocurrir de las siguientes maneras:

- **Presentación de formularios:** Cuando un usuario envía un formulario Web, SalesWings identificará automáticamente todos tus tipos de formulario Web (como iniciar sesión, descargar, contactar con nosotros, etc.) y resolverá la identidad de un usuario cuando envíe un formulario. 
- **Clics en URL con un Braze ID o un ID externo:** Un usuario hace clic en una acción de marketing de Braze, normalmente clics de correo electrónico, clics de banner o similares, que conducen a una página que estás siguiendo con SalesWings.
- **Seguimiento del correo electrónico de ventas mediante plugins de Gmail y Outlook (opcional):** Si decides dotar a tu representante de ventas de plugins de seguimiento de correo electrónico, pueden desencadenar el seguimiento completo del sitio web de los usuarios mediante el envío de enlaces rastreables.
- **Segment.com Identificador del evento (opcional):** Si eres usuario de Segment.com, también puedes resolver la identidad de un usuario con la integración de Segment.com.

### Identificación de usuarios a partir de clics en URL

Puedes identificar a los usuarios automáticamente cuando hagan clic en una URL rastreable (por ejemplo, envíos masivos por correo electrónico, banners con URL). Para hacer que una URL sea rastreable, hay dos formas de modificar las URL de tu sitio web en tus correos electrónicos, banners o SMS añadiendo el parámetro y el ID al final de tus enlaces.

1. Añadiendo `?braze_id=` seguido de {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Ejemplo de enlace:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Añadiendo `?br_user_id=` seguido de {% raw %}`{{${user_id}}}`{% endraw %}
  - **Ejemplo de enlace:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

La variable `braze_id` se establece en un identificador del usuario generado por Braze y está siempre disponible. La variable `br_user_id` se establece con el identificador del usuario en su sistema y puede faltar en ciertos escenarios (por ejemplo, para usuarios anónimos creados por el SDK Braze). Si en un enlace se utilizan tanto `braze_id` como `br_user_id`, SalesWings sólo tendrá en cuenta el parámetro `braze_id`.

Para la configuración y la solución de problemas adicionales, ponte en contacto con el [equipo de servicios de SalesWings][1] para obtener ayuda sobre la incorporación.

[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[5]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[6]: https://helium.saleswings.pro/settings
[7]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[8]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
