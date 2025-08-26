---
nav_title: optilyz
article_title: optilyz
description: "Este artículo de referencia describe la asociación entre Braze y Optilyz, que te habilita para realizar campañas de correo directo más centradas en el cliente, sostenibles y rentables."
alias: /partners/optilyz/
page_type: partner
search_tag: Partner

---

# optilyz

> [optilyz](https://optilyz.com) es una plataforma de automatización de correo directo que le permite realizar campañas de correo directo más centradas en el cliente, sostenibles y rentables. 

_Esta integración está mantenida por optilyz._

## Sobre la integración

Utilice la integración de optilyz y Braze webhook para enviar a sus clientes correo directo, como cartas, postales y autoenvíos.

## Requisitos previos

| Requisito | Descripción |
|---|---|
|cuenta optilyz | Se necesita una cuenta de Optilyz para beneficiarse de esta asociación. |
| Clave API de optilyz<br><br>`<OPTILYZ_API_KEY>`| Tu administrador del éxito del cliente de Optilyz te proporcionará tu clave de API de Optilyz.<br><br>Esta clave de API te habilitará para conectar tus cuentas de Braze y Optilyz. |
| ID de automatización de Optilyz<br><br>`<OPTILYZ_AUTOMATION_ID>` | El ID de automatización se encuentra en un recuadro en la cabecera de la página.<br><br>Cuando haya iniciado sesión en optilyz, podrá navegar hasta la automatización a la que desea enviar los datos.<br>Primero hay que activar la automatización. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Casos prácticos

Gestionar la publicidad directa como un canal digital significa alejarse de los envíos masivos y aprovechar el canal como parte de los viajes (digitales) de los clientes. Las ventajas de un enfoque moderno del correo directo son:
- Aumento de las tasas de conversión mediante una mayor relevancia, casos de uso adicionales, pruebas A/B más sencillas y efectos de canales cruzados.
- Reducción del esfuerzo mediante la automatización y una solución de extremo a extremo
- Reducción de costes mediante contratos marco y transparencia de costes

## Integración

Para integrarse con optilyz, utilice la [API de optilyz](https://www.optilyz.com/doc/api/) para enviar los datos del destinatario al webhook Braze.

### Paso 1: Cree su plantilla de webhook Braze

Para crear una plantilla de webhook optilyz para utilizarla en futuras campañas o Canvases, navegue hasta **Plantillas** > **Plantillas de webhook** en la plataforma Braze. 

Si desea crear una campaña optilyz webhook única o utilizar una plantilla existente, seleccione **Webhook** en Braze al crear una nueva campaña.

En tu nueva plantilla Webhook, rellena los siguientes campos:
- **URL del webhook**: La URL del webhook es única para cada cliente y te la proporcionará tu administrador del éxito del cliente de Optilyz.
- **Cuerpo de la solicitud**: Texto sin procesar

#### Encabezados de solicitud y método

Optilyz también requiere un encabezado HTTP para la autorización y un método HTTP. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Configuración**, debe reemplazar el `<OPTILYZ_API_KEY>` con su clave API de optilyz. Esta clave debe incluir un ":" justo después de la clave y estar codificada en base 64. 

- **Método HTTP**: POST
- **Encabezados de solicitud**:
  - **Autorización**: {% raw %} `{{ '<OPTILYZ_API_KEY>:' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![Los encabezados de solicitud y el método HTTP que se muestran en el constructor de webhook Braze.]({% image_buster /assets/img/optilyz/optilyz_settings.png %}){: style="max-width:50%"}

#### Cuerpo de la solicitud

En el siguiente cuerpo de solicitud, puede utilizar cualquier etiqueta de personalización de Liquid y crear una plantilla de solicitud personalizada de acuerdo con [la documentación de la API](https://www.optilyz.com/doc/api/) de optilyz.

El campo `variation` es opcional y puede definir qué diseño dentro de la automatización debe utilizarse. Si se omite una variación, optilyz asignará aleatoriamente una de las variaciones definidas.

{% raw %}
```json
{
    "address": {
        "title": "{{custom_attribute.${salutation}}}",
        "firstName": "{{${first_name}}}",
        "lastName": "{{${last_name}}}",
        "street": "{{custom_attribute.${street}}}",
        "houseNumber": "{{custom_attribute.${houseNumber}}}",
        "address2": "{{custom_attribute.${address2}}}",
        "zipCode": "{{custom_attribute.${zipCode}}}",
        "city": "{{custom_attribute.${city}}}",
        "country": "{{custom_attribute.${country}}}"
    },
    "variation": {{custom_attribute.${designVariation}}}
}
```
{% endraw %}

![Una imagen del código del cuerpo de la solicitud y la URL del webhook que se muestra en la pestaña de composición del constructor de webhook Braze.]({% image_buster /assets/img/optilyz/optilyz_compose.png %})

### Paso 2: Vista previa de su solicitud

A continuación, previsualice su solicitud en el panel **Vista previa** o vaya a la pestaña **Prueba**, donde puede seleccionar un usuario al azar, un usuario existente o personalizar el suyo propio para probar su webhook. Recuerda guardar tu plantilla antes de salir de la página.

![Diferentes campos de prueba disponibles en la pestaña de prueba del constructor de webhook Braze.]({% image_buster /assets/img/optilyz/optilyz_testing.png %})

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas webhook actualizadas pueden encontrarse en la lista **Plantillas webhook guardadas** al crear una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}


