---
nav_title: Inkit
article_title: Inkit
alias: /partners/inkit/
description: "Este artículo de referencia describe la asociación entre Braze e Inkit, que le permite ahorrar tiempo y esfuerzo automatizando sus campañas de publicidad directa y hacer que los clientes que no están conectados vuelvan a estarlo."
page_type: partner
search_tag: Partner

---

# Inkit

> [Inkit](https://www.inkit.com) y Braze permiten a las organizaciones generar y distribuir documentos de forma segura, tanto digitalmente como por correo directo.

_Esta integración está mantenida por Inkit._

## Sobre la integración

La integración de Braze e Inkit permite generar documentos y enviarlos por correo directamente a los usuarios de Braze con los webhooks de Braze.

## Requisitos previos

|Requisito| Descripción|
| ---| ---|
|Cuenta Inkit | Se necesita una [cuenta Inkit](https://www.inkit.com/) para beneficiarse de esta asociación. |
| Clave de API de Inkit<br><br>`<INKIT_API_TOKEN>` | Esta clave se encuentra en [el panel de Inkit](https://app.inkit.io/#/account/integrations), en la pestaña **Desarrollo**, y le permitirá conectar sus cuentas Braze e Inkit.|
| ID de la plantilla Inkit<br><br>`<INKIT_TEMPLATE_ID>` | Después de crear una plantilla, puede copiar el ID de plantilla de la pestaña **Plantillas** para utilizarlo en su plantilla en Braze.<br><br>Por ejemplo, puede crear una plantilla llamada `invoice_template` en el entorno Inkit con el ID de plantilla: `tmpl_3bDScFl9cwr3OAVR1RSdEC`.
| Cabecera HTTP | El encabezado HTTP forma parte de la solicitud API que se envía desde Braze a Inkit. En él, incluirá su clave API de Inkit para autenticar y autorizar las llamadas a la API de Inkit. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Integración

### Paso 1: Crear una plantilla Inkit

En la plataforma Inkit, cree una plantilla para utilizarla en su campaña Braze en HTML, Word, PowerPoint, Excel o PDF. Consulte [la documentación de Inkit](https://docs.inkit.com/docs/create-a-template) para obtener más información.

### Paso 2: Cree su plantilla de webhook Braze

Para crear una plantilla de webhook Inkit y utilizarla en futuras campañas o Canvases, vaya a **Plantillas** > **Plantillas de webhook** en la plataforma Braze. 

Si desea crear una campaña webhook Inkit única o utilizar una plantilla existente, seleccione **Webhook** en Braze al crear una nueva campaña.

![Una selección de plantillas de webhook prediseñadas disponibles en la pestaña Plantillas de webhook de la sección Plantillas y medios.]({% image_buster /assets/img/inkit-webhook-template.png %})

Una vez que haya seleccionado la plantilla de webhook Inkit, debería ver lo siguiente:
- **URL del webhook**: En blanco
- **Cuerpo de la solicitud**: Texto sin procesar

En el campo URL Webhook, tendrás que [crear](https://docs.inkit.com/docs/set-up-a-webhook-to-an-event) e introducir una URL webhook de Inkit.

![Código del cuerpo de la solicitud y URL del webhook mostrados en la pestaña de composición del constructor de webhook Braze.]({% image_buster /assets/img/inkit-integration.png %})

#### Encabezados de solicitud y método

Inkit requiere un `HTTP Header` para la autorización, incluida tu clave de API de Inkit codificada en base 64. Lo siguiente ya estará incluido dentro de la plantilla como un par clave-valor, pero en la pestaña **Configuración**, debe reemplazar el `<INKIT_API_TOKEN>` con su clave de API de Inkit.

{% raw %}
- **Método HTTP**: POST
- **Encabezado de solicitud**:
  - **Autorización**: Básica `{{ '<INKIT_API_TOKEN>' | base64_encode }}`
  - **Content-Type**: application/json
{% endraw %}

#### Cuerpo de la solicitud

Asegúrese de que su Liquid coincide con los atributos personalizados adecuados asociados a los siguientes campos obligatorios y opcionales. También puede añadir campos de datos personalizados a cualquier solicitud.

```json
{% raw %}{
  "api_token": "<INKIT_API_TOKEN>",
  "template_id": "<INKIT_TEMPLATE_ID>",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}",
  "email": "{{${email_address}}}",
  "company": "{{custom_attribute.${company_name}}}",
  "phone" : "{{${phone_number}}}",
  "address_line_1": "{{custom_attribute.${address}}}",
  "address_line_2": "{{custom_attribute.${address2}}}",
  "address_city": "{{${city}}}",
  "address_state": "{{custom_attribute.${state}}}",
  "address_zip": "{{custom_attribute.${zip}}}",
  "address_country": "{{${country}}}",
  "source" : "Braze"
}{% endraw %}
```

### Paso 3: Vista previa de su solicitud

El texto sin formato se resaltará automáticamente si se trata de una etiqueta Braze aplicable. `street` `unit` , `state` y `zip` deben configurarse como [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attributes) para enviar este Webhook.

Previsualiza tu solicitud en el panel de **Previsualización** o navega a la pestaña de **Prueba**, donde puedes seleccionar un usuario al azar, un usuario existente, o personalizar el tuyo propio para probar tu webhook.

{% alert important %}
Recuerda guardar tu plantilla antes de salir de la página. <br>Las plantillas webhook actualizadas pueden encontrarse en la lista **Plantillas webhook guardadas** al crear una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}


