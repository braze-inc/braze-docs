---
nav_title: Jampp
article_title: Jampp
alias: /partners/jampp/
description: "Este artículo de referencia describe la asociación entre Braze y Jampp, una plataforma de marketing del rendimiento utilizada para captar y reorientar clientes móviles."
page_type: partner
search_tag: Partner

---

# Jampp

> [Jampp](https://www.jampp.com/) es una plataforma de marketing del rendimiento utilizada para captar y reorientar clientes móviles. Jampp combina datos de comportamiento con tecnología predictiva y programática para generar ingresos para los anunciantes mostrando anuncios personales y relevantes que inspiran a los consumidores a comprar por primera vez o más a menudo.

_Esta integración está mantenida por Jampp._

## Sobre la integración

La integración de Braze y Jampp permite a los usuarios de Braze sincronizar eventos en Jampp a través de eventos webhook de Braze. Como resultado, los clientes pueden añadir conjuntos de datos más ricos a sus iniciativas de retargeting dentro de sus ecosistemas de publicidad móvil.

Algunos ejemplos de casos en los que se puede reorientar a los clientes con un anuncio:
- Cuando cambia el estado del correo electrónico o de la suscripción push de un cliente.
- Cómo interactuó un cliente con una campaña de mensajería Braze.
- Si el cliente ha desencadenado una geovalla específica.

## Requisitos previos

Esta integración es compatible con aplicaciones iOS y Android.

| Requisito | Descripción |
|---|---|
| Cuenta Jampp | Se necesita una [cuenta Jampp](https://www.jampp.com/) para beneficiarse de esta asociación. |
| ID de la aplicación Android | Tu identificador único de aplicación Braze para Android (como "com.example"). |
| ID de la aplicación iOS | Tu identificador único de aplicación Braze para iOS (como "012345678"). |
| Habilitar la recogida de IDFA en el SDK de Braze | La recogida de IDFA es opcional dentro del SDK de Braze y está desactivada por defecto. | 
| Recopilación del identificador de publicidad de Google mediante un atributo personalizado | La recogida del ID de publicidad de Google es opcional para los clientes y puede recogerse como un [atributo personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración

### Paso 1: Crear una plantilla de webhook en Braze

Para crear una plantilla de webhook Jampp y utilizarla en futuras campañas o Canvases, vaya a **Plantillas** > **Plantillas de webhook** en la plataforma Braze.

Si desea hacer una campaña Jampp webhook única o utilizar una plantilla existente, seleccione **Webhook** en Braze al crear una nueva campaña.

En tu nueva plantilla Webhook, rellena los siguientes campos:
- **Cuerpo de la solicitud**: Texto sin procesar
- **URL del webhook**:
{% raw %}
```liquid
{% assign event_name = 'your_jampp_event_name' %}
{% assign android_app_id = 'your_android_app_id' %}
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'{{event_name}}','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

http://tracking.jampp.com/event?kind={{event_name}}&rnd={{rnd}}&app={% if {{most_recently_used_device.${idfa}}} == blank %}{{android_app_id}}{% else %}{{iOS_app_id}}{% endif %}&apple_ifa={{most_recently_used_device.${idfa}}}&google_advertising_id={{custom_attribute.${aaid}}}&user_agent={user-agent}&prtnr=braze

{% if {{most_recently_used_device.${idfa}}} == blank and {{custom_attribute.${aaid}}} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

En la URL del webhook, debe:
- Establece el nombre del evento. Este nombre aparecerá en su panel de Jampp.
- Pasa el identificador único de tu aplicación para Android (como "com.example") e iOS (como "012345678").
- Inserte [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#using-liquid) para el atributo personalizado adecuado que esté rastreando como ID de publicidad de Google. Tenga en cuenta que el ID de publicidad de Google aparece como `aaid` en este ejemplo, pero tendrá que sustituirlo por el nombre de atributo personalizado que establezcan sus desarrolladores.

![La URL del webhook y la vista previa del mensaje mostrados en el constructor de webhook Braze.]({% image_buster /assets/img/jampp_webhook.png %})

{% alert important %}
Braze no recoge automáticamente el IDFA/AAID del dispositivo, por lo que debe almacenar estos valores usted mismo. Tenga en cuenta que puede necesitar el consentimiento del usuario para recopilar estos datos.
{% endalert %}

#### Encabezados de solicitud y método

El webhook de Jampp requiere un método HTTP y una cabecera de solicitud.

- **Método HTTP**: OBTENER
- **Encabezados de solicitud**:
  - **Content-Type**: application/json

![Los encabezados de solicitud, el método HTTP y la vista previa del mensaje que se muestran en el constructor de webhook Braze.]({% image_buster /assets/img/jampp_method.png %})

#### Cuerpo de la solicitud

No es necesario definir un cuerpo de petición para este webhook.

### Paso 2: Vista previa de su solicitud

Previsualice el mensaje para asegurarse de que la solicitud se muestra correctamente para los distintos usuarios. Recomendamos previsualizar y enviar solicitudes de prueba tanto para usuarios de Android como de iOS. Si la solicitud tiene éxito, la API responderá con `HTTP 204`.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas webhook actualizadas pueden encontrarse en la lista **Plantillas webhook guardadas** al crear una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}


