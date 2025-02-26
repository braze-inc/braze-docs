---
nav_title: "OfferFit"
article_title: OfferFit
alias: /partners/offerfit/
description: "OfferFit sustituye las pruebas A/B manuales por pruebas de IA. Los profesionales del marketing de ciclo de vida utilizan las pruebas de IA de OfferFit para tomar la mejor decisión 1:1 para cada cliente, probar todas las variables simultáneamente y detectar y adaptarse a los cambios del mercado."
page_type: partner
search_tag: OfferFit

---


# OfferFit

> [OfferFit](https://www.offerfit.ai/) sustituye las pruebas A/B manuales por pruebas de IA. Los profesionales del marketing de ciclo de vida utilizan las pruebas de IA de OfferFit para tomar la mejor decisión 1:1 para cada cliente, probar todas las variables simultáneamente y detectar y adaptarse a los cambios del mercado.

La integración de OfferFit y Braze le permite descubrir automáticamente el mensaje, el canal y el momento adecuados para cada cliente basándose en sus datos de cliente. Puede optimizar sus campañas para clientes existentes identificados, con objetivos empresariales como ventas cruzadas, ventas adicionales, recompra, retención, renovación, recomendación y recuperación.

## Requisitos previos

| Requisito | Descripción |
|-------------|-------------|
| Licencia de OfferFit | Se requiere una licencia activa de OfferFit para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST Braze con los siguientes permisos: {::nomarkdown}<ul><li><code>users.export.ids</code></li><li><code>users.export.segment</code></li><li><code>messages.send</code></li><li><code>campaigns.trigger.send</code></li> <li><code>campaigns.list</code></li><li><code>campaigns.data_series</code></li><li><code>campaigns.details</code></li><li><code>canvas.trigger.send</code></li><li><code>canvas.list</code></li><li><code>canvas.data_series</code></li><li><code>canvas.details</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>templates.create</code></li><li><code>templates.update</code></li><li><code>templates.info</code></li><li><code>templates.list</code></li></ul>{:/} Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final de la API REST Braze | [La URL de tu punto final de la API REST][1]. Tu punto final depende de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), puede crear una clave de API en **Consola de desarrollador** > **Configuración de API**.
{% endalert %}

### Puntos finales de la API REST Braze

Su licencia de OfferFit y su caso de uso determinarán los puntos finales de Braze REST API que utilice. A continuación encontrarás varios puntos finales de la API que puedes utilizar.

| Punto final de la API REST Braze | Uso de OfferFit |
|--------------|----------------|
| [POST /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                          | Recuperar la lista de clientes a los que va dirigida una campaña o Canvas. Como OfferFit no acepta ningún dato PII, el atributo `fields_to_export` se utiliza para recuperar únicamente los atributos de datos acordados con el usuario de la plataforma. |
| [POST /users/export/segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)                         | Recuperar todos los usuarios que forman parte de un segmento específico. Como OfferFit no acepta datos PII, el atributo `fields_to_export` se utiliza para recuperar únicamente los campos no PII acordados con el usuario de la plataforma. |
| [POST /users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                            | OfferFit puede utilizar este punto final para actualizar los perfiles de usuario con atributos de datos personalizados que pueden utilizarse para personalizar la mensajería.                                                                                                                                            |
| [POST /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)                         | Activar una campaña API en Braze. |
| [POST /campaigns/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)     | Activa un envío para una campaña configurada para entrega activada por API. |
| [GET /campaigns/list]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)                                     | Recupera la lista de todas las campañas configuradas en Braze y sus metadatos asociados. |
| [GET /campaigns/data_series]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                     | Recupere los datos analíticos de una campaña Braze específica. |
| [GET /campaigns/details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)                           | Recuperar los detalles de una campaña Braze específica. |
| [POST /canvas/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)         | Activa un envío para un lienzo configurado para entrega activada por API. |
| [GET /canvas/list]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)                                            | Recupera la lista de todos los Lienzos configurados en Braze y sus metadatos asociados. |
| [GET /canvas/data_series]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)                             | Recuperar los datos analíticos de un Canvas específico. |
| [GET /canvas/details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)                                   | Recuperar los detalles de un Canvas específico. |
| [GET /segments/list]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)                                        | Recupera la lista de todos los segmentos configurados en Braze y sus metadatos asociados. |
| [GET /segments/data_series]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)                        | Recupera el tamaño del segmento Braze. |
| [GET /segments/details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)                              | Recupera los detalles de un segmento Braze específico. |
| [POST /templates/email/create]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)      | Cree una nueva plantilla de correo electrónico Braze HTML. |
| [POST /templates/email/update]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)      | Actualice una plantilla de correo electrónico Braze HTML existente. |
| [GET /templates/email/info]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Recupera los detalles de una plantilla de correo electrónico Braze HTML específica. |
| [GET /templates/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)           | Recuperar la lista de todas las plantillas de correo electrónico Braze HTML configuradas en Braze y sus `subject line` y `HTML content`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

Después de [integrar OfferFit](#integration), puede automatizar el proceso de experimentación haciendo lo siguiente:

1. Selecciona una **métrica de éxito** a maximizar, como ingresos, conversiones, ARPU o cualquier otra
KPI que puede medir a partir de los datos de sus clientes. Esta es la métrica que OfferFit intentará maximizar con su IA.
2. Seleccione las **dimensiones** a probar (por ejemplo, oferta, línea de asunto, creatividad, canal, hora, día, frecuencia, etc.).
3. Seleccione las **opciones** disponibles para cada dimensión. Por ejemplo, podrías seleccionar correo electrónico, SMS y push para la dimensión canal, y luego seleccionar diariamente, dos veces por semana y semanalmente para la dimensión frecuencia.

![of_use_case_example][2]


Una vez automatizado el proceso de experimentación, OfferFit comenzará a hacer recomendaciones diarias para cada cliente con el objetivo de maximizar la métrica de éxito elegida. 

La IA de OfferFit aprenderá de cada interacción con el cliente y aplicará esos conocimientos a las recomendaciones del día siguiente.


| Casos de uso | Objetivo | Enfoque previo | Enfoque OfferFit |
|----------|------|----------------|-------------------|
| **Venta cruzada o venta mejorada** | Maximizar los ingresos medios por usuario (ARPU) de las suscripciones a Internet. | Realice campañas anuales ofreciendo a cada cliente el plan de nivel superior. | Descubra empíricamente el mejor mensaje, momento de envío, descuento y plan que ofrecer a cada cliente, aprendiendo qué clientes son susceptibles de recibir ofertas de salto y qué clientes necesitan descuentos u otros incentivos para subir de categoría. |
| **Renovación y retención** | Garantizar la renovación de los contratos, maximizando tanto su duración como su valor actual neto (VAN). | Realice pruebas A/B manualmente y ofrezca descuentos importantes para conseguir renovaciones. | Utilice la experimentación automatizada para encontrar la mejor oferta de renovación para cada cliente, e identifique a los clientes menos sensibles a los precios y que necesitan descuentos menos importantes para renovar. |
| **Compra repetida** | Maximizar las tasas de compra y recompra. | Todos los clientes reciben el mismo recorrido después de crear una cuenta en el sitio web (por ejemplo, la misma secuencia de correos electrónicos con la misma cadencia). | Automatice la experimentación para encontrar el mejor elemento del menú que ofrecer a cada cliente, así como la línea de asunto, la hora de envío y la frecuencia de comunicación más eficaces. |
| **Winback** | Aumenta la reactivación animando a los antiguos suscriptores a volver a suscribirse. | Pruebas A/B y segmentación sofisticadas. | Aprovecha la experimentación automatizada para probar miles de variables a la vez, descubriendo la mejor creatividad, mensaje, canal y cadencia para cada individuo. |
| **Referidos** | Maximizar las nuevas cuentas abiertas a través de referencias de tarjetas de crédito de empresas de clientes existentes. | Secuencia de correo electrónico fija para todos los clientes, con pruebas A/B exhaustivas para determinar las mejores horas de envío, cadencia, etc. para la población de clientes. | Automatice la experimentación para determinar el correo electrónico, la creatividad, el tiempo de envío y la tarjeta de crédito ideales para ofrecer a clientes específicos. |
| **Nutrición y conversión de clientes potenciales** | Aumente los ingresos y pague la cantidad correcta por cada cliente. | A medida que cambian las políticas de privacidad en Facebook y otras plataformas, los enfoques anteriores de los anuncios de pago personalizados pierden eficacia. | Aprovecha los sólidos datos propios para experimentar automáticamente con los segmentos de clientes, la metodología de pujas, los niveles de puja y la creatividad. |
| **Fidelización y compromiso** | Maximizar las compras de los nuevos inscritos en el programa de fidelización de clientes. | Los clientes recibían una secuencia fija de correos electrónicos en respuesta a sus acciones. Por ejemplo, todos los nuevos inscritos en el programa de fidelización reciben el mismo viaje. | Experimenta automáticamente con diferentes ofertas de correo electrónico, creatividades, tiempo de envío y frecuencia para maximizar la compra y recompra de cada cliente. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Integración

### Paso 1: Definir el público objetivo en Braze

Defina su público objetivo creando al menos un segmento en Braze. Este segmento se utilizará para enviar su campaña o Canvas a los usuarios adecuados.

### Paso 2: Configurar una campaña Braze activada por API o Canvas y crear activos de campaña (por ejemplo, plantillas HTML, imágenes) {#step-2}

1. Crear una campaña o Canvas en Braze. OfferFit utilizará esta campaña o Canvas para enviar eventos de activación personalizados 1:1 a los usuarios adecuados de su audiencia definida. 
2. No incluyas un [grupo de control]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) Braze en tu campaña o Canvas. Esto permite que el grupo de control OfferFit sea el único activo.
3. Dependiendo de sus dimensiones, puede configurar etiquetas Liquid en su contenido creativo para rellenar dinámicamente su campaña o Canvas con recomendaciones de OfferFit. OfferFit pasará contenido específico del cliente a las etiquetas Liquid de sus plantillas a través de la API Braze.

### Paso 3: Actualice la configuración de su caso de uso de OfferFit para orquestar eventos de activación de Braze

Puede aprovechar la integración de activación nativa de OfferFit con Braze para orquestar y programar recomendaciones personalizadas 1:1 para su público objetivo.

## Personalización

Además de orquestar eventos de activación en Braze, OfferFit proporciona capacidades de integración de datos que le permiten recuperar el perfil del cliente (no PII) y datos de compromiso de Braze a través de los puntos finales de API disponibles.

## Mediante esta integración

Una vez configurado OfferFit, la plataforma de experimentación automatizada enviará automáticamente a Braze eventos de activación personalizados 1:1 para cada usuario de su público objetivo. Estos eventos de activación se activarán a través de las campañas Braze o los Canvases que configuró en [el paso 2](#step-2).

Además de los datos analíticos disponibles en Braze, OfferFit proporciona una completa capa de informes que permite a los profesionales del marketing explorar las perspectivas de los clientes descubiertas por OfferFit a través de sus capacidades de inteligencia artificial de aprendizaje automático.




[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}

