---
nav_title: Remerge
article_title: Remerge
alias: /partners/remerge/
description: "Este artículo de referencia describe la asociación entre Braze y Remerge, una aplicación diseñada específicamente para la reorientación a gran escala, que te proporciona herramientas para segmentar eficazmente las audiencias de las aplicaciones y reorientar a los usuarios."
page_type: partner
search_tag: Partner

---

# Remerge

> [Remerge](https://www.remerge.io/) se ha creado específicamente para la reorientación de aplicaciones a gran escala, y te proporciona herramientas para segmentar eficazmente las audiencias de las aplicaciones y reorientar a los usuarios.

_Esta integración está mantenida por Remerge._

## Sobre la integración

La integración de Braze y Remerge te ayuda a desarrollar sólidas campañas de marketing de canales cruzados mediante el envío de datos de usuario a Remerge a través de eventos webhook para ayudar a reorientar a los usuarios a través de su plataforma de demanda móvil.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Remerge | Se necesita una cuenta Remerge para beneficiarse de esta asociación. |
| Clave de webhook de Remerge | Esta clave será proporcionada por Remerge. |
| ID de la aplicación Android | Tu identificador único de aplicación Braze para Android (como "com.example"). |
| ID de la aplicación iOS | Tu identificador único de aplicación Braze para iOS (como "012345678"). |
| Habilitar la recogida de IDFA en el SDK de Braze | La recogida de IDFA es opcional dentro del SDK de Braze y está desactivada por defecto. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Cree su plantilla de webhook Braze

Para crear una plantilla de webhook Remerge para futuras campañas o Canvases, navegue hasta **Templates** > **Webhook Templates** en la plataforma Braze. 

Si desea crear una campaña webhook Remerge única o utilizar una plantilla existente, seleccione **Webhook** en Braze al crear una nueva campaña.

En tu nueva plantilla Webhook, rellena los siguientes campos:
- **Cuerpo de la solicitud**: Texto sin procesar
- **URL del webhook**:
{% raw %}
```liquid
{% assign event_name = 'your_remerge_event_name' %} 
{% assign android_app_id = 'your_android_app_id' %} 
{% assign iOS_app_id = 'your_iOS_app_id' %}

{% capture json %}{'name':'event_name','active':true,'joined':{{'now' | date: '%s' }}}{% endcapture %}

https://remerge.events/event?partner=braze&app_id=\{% if most_recently_used_device.${idfa} == blank %}android_app_id{% else %}iOS_app_id{% endif %}&key=1cs3p12k&ts='now' | date: '%s' }}&{% if {{most_recently_used_device.${idfa} == blank%}aaid=custom_attribute.${aaid}{% else %}idfa=most_recently_used_device.${idfa{%endif%}&event=event_name&non_app_event=true&data=json | url_param_escape

{% if most_recently_used_device.${idfa} == blank and custom_attribute.${aaid} == blank %}
{% abort_message('No IDFA or AAID available') %}
{% endif %}
```
{% endraw %}

En la URL del webhook, debe:
- Utiliza la API `https://remerge.events/event` para enviar tus eventos webhook.
- Establece el nombre del evento. Este nombre aparecerá en tu panel de [remerge.io](https://www.remerge.io/).
- Pasa a Remerge el identificador único de tu aplicación para Android (como "com.example") e iOS (como "012345678").
- Define una clave; Remerge te la proporcionará.

![La URL del webhook y la vista previa del mensaje mostrados en el constructor de webhook Braze.]({% image_buster /assets/img_archive/webhook_remerge_preview.png %})

{% alert important %}
Braze no recoge automáticamente el IDFA/AAID del dispositivo, por lo que debe almacenar estos valores usted mismo. Tenga en cuenta que puede necesitar el consentimiento del usuario para recopilar estos datos.
{% endalert %}

#### Encabezados de solicitud y método

El webhook Remerge requiere un método HTTP y una cabecera de petición.

- **Método HTTP**: OBTENER
- **Encabezados de solicitud**:
  - **Content-Type**: application/json

![Los encabezados de solicitud, el método HTTP y la vista previa del mensaje que se muestran en el constructor de webhook Braze.]({% image_buster /assets/img_archive/httpmethod_remerge.png %})

#### Cuerpo de la solicitud

No es necesario definir un cuerpo de petición para este webhook.

## Paso 2: Vista previa de su solicitud

Previsualice el mensaje para asegurarse de que la solicitud se muestra correctamente para los distintos usuarios. Recomendamos previsualizar y enviar solicitudes de prueba tanto para usuarios de Android como de iOS. Si la solicitud tiene éxito, la API responderá con `HTTP 204`.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas webhook actualizadas pueden encontrarse en la lista **Plantillas webhook guardadas** al crear una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}


