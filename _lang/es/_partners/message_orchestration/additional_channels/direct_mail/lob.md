---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "Este artículo de referencia describe la asociación entre Braze y Lob.com, que te permite enviar correo directo como cartas, postales y cheques por correo."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com][38] es un servicio online que te permite enviar correo directo a tus usuarios.

La integración de Braze y Lob aprovecha los webhooks de Braze y la API de Lob para enviar correo como cartas, postales y cheques por correo.  

## Requisitos previos

|Requisito| Descripción|
| ---| ---|
|Cuenta Lob | Se necesita una cuenta Lob para beneficiarse de esta asociación. |
| Clave de API Lob | Tu clave de API de Lob se encuentra en la sección de configuración, debajo de tu nombre, en el panel de Lob. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Selecciona el punto final Lob

La URL HTTP a solicitar en el webhook es diferente para cada acción que puedas realizar en Lob. En el siguiente ejemplo, utilizamos el punto final de la API de postales `https://api.lob.com/v1/postcards`. Visita la [lista completa de puntos finales][39] para seleccionar el punto final apropiado para tu caso de uso. 

| Punto de conexión de API | Puntos finales disponibles |
| ------------ | ------------------- |
| https://api.lob.com/ | /v1/addresses<br>/v1/addresses/{id}<br>/v1/verify<br>/v1/postcards<br>/v1/postcards/{id}<br>/v1/letter<br>/v1/letter/{id}<br>/v1/checks<br>/v1/checks/{id}<br>/v1/bank_accounts<br>/v1/bank_accounts/{id}<br>/v1/bank_accounts/{id}/verify<br>/v1/areas<br>/v1/areas/{id}<br>/v1/routes/{zip_code}<br>/v1/routes<br>/v1/countries<br>/v1/states|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Paso 2: Crea tu plantilla de webhook Braze

Para crear una plantilla de webhook Lob para utilizarla en futuras campañas o Canvas, ve a **Plantillas** > **Plantillas de webhook** en la plataforma Braze. 

{% alert note %}
Si utiliza la [navegación anterior]({{site.baseurl}}/navigation), vaya a **Compromiso** > **Plantillas y medios** > **Plantillas de Webhook**.
{% endalert %}

Si quieres hacer una campaña única de webhook Lob o utilizar una plantilla existente, selecciona **Webhook** en Braze al crear una nueva campaña.

En tu nueva plantilla Webhook, rellena los siguientes campos:
- **URL del webhook**: `<LOB_API_ENDPOINT>`
- **Cuerpo de la solicitud**: Texto sin procesar

#### Encabezados de solicitud y método

Lob requiere un encabezado HTTP para la autorización y un método HTTP. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Configuración**, debes sustituir el `<LOB_API_KEY>` por tu clave API Lob. Esta clave debe incluir un ":" justo después de la clave y estar codificada en base 64. 

- **Método HTTP**: POST
- **Encabezados de solicitud**:
  - **Autorización**: Básica `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Código del cuerpo de la solicitud y URL del webhook mostrados en la pestaña de composición del creador de webhooks Braze.][35]

#### Cuerpo de la solicitud

A continuación se muestra un ejemplo de cuerpo de solicitud para el punto final de postales Lob. Aunque este cuerpo de solicitud se proporciona en la plantilla base Lob de Braze, si deseas utilizar otros puntos finales, deberás ajustar tus campos Liquid en consecuencia.

```json
{% raw %}"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}",
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"{% endraw %}
```

### Paso 3: Vista previa de su solicitud

En este punto, tu campaña debería estar lista para probarla y enviarla. Comprueba el panel de Lob y los registros de mensajes de error de la consola para desarrolladores Braze si te encuentras con errores. Por ejemplo, el siguiente error fue causado por una cabecera de autenticación formateada incorrectamente. 

![Un registro de mensajes de error que muestra la hora, el nombre de la aplicación, el canal y el mensaje de error. El mensaje de error incluye el mensaje de alerta y el código de estado.][36]

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas webhook actualizadas pueden encontrarse en la lista **Plantillas webhook guardadas** al crear una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

[33]: {% image_buster /assets/img_archive/lob_api_key.png %}
[34]: {% image_buster /assets/img_archive/lob_success_response.png %}
[35]: {% image_buster /assets/img_archive/lob_full_request.png %}
[36]: {% image_buster /assets/img_archive/error_log.png %}
[37]: {% image_buster /assets/img_archive/lob_api_endpoint.png %}
[38]: https://lob.com
[39]: https://lob.com/docs#intro
[40]: https://lob.com/docs#auth
