---
nav_title: Zapier
article_title: Zapier
alias: /partners/zapier/
description: "Este artículo de referencia describe la asociación entre Braze y Zapier, una herramienta web de automatización que permite compartir datos entre aplicaciones web y utilizar esa información para automatizar acciones."
page_type: partner
search_tag: Partner

---
# Integración con Zapier

> [Zapier](https://zapier.com/) es una herramienta web de automatización que permite compartir datos entre aplicaciones web y luego utilizar esa información para automatizar acciones. 

La asociación entre Braze y Zapier aprovecha la API de Braze y [los webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#creating-a-webhook) de Braze para conectarse con aplicaciones de terceros, como Google Workplace, Slack, Salesforce, WordPress, etc. para automatizar diversas acciones.

## Requisitos previos

| Requisitos | Descripción |
|---|---|
| Cuenta Zapier | Se requiere una cuenta Zapier para aprovechar esta asociación. |
| Punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/api/basics/#api-definitions). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

En el siguiente ejemplo de Zapier, enviaremos información de WordPress a Braze mediante un webhook POST. Esta información puede utilizarse para crear un Canvas de Braze.

### Paso 1: Crear un disparador Zapier

Utilizando la terminología de Zapier, un "zap" es un flujo de trabajo automatizado que conecta tus aplicaciones y servicios. La primera parte de cualquier zap es designar un desencadenante. Una vez habilitado tu zap, Zapier realizará automáticamente las acciones respectivas siempre que se detecte tu desencadenante.

Usando nuestro ejemplo de WordPress, en la plataforma Zapier, configuraremos nuestro zap para que se active cuando se añada un nuevo post de WordPress y seleccionaremos **Published** y **Posts** como **Post Status** y **Post Type**. 

![En la plataforma Zapier, dentro de un zap, selecciona que el desencadenante sea "nuevo comentario", "cualquier webhook" o "nueva publicación". Para este ejemplo, se selecciona "nueva entrada". ] [5]

![En la plataforma Zapier, dentro de un zap, configura el desencadenante seleccionando el estado y el tipo de entrada deseados. En este ejemplo, se selecciona "Publicado" y "Mensajes".] [6]

### Paso 2: Añadir un webhook de acción

A continuación, define la acción zap. Cuando tu zap está habilitado y se detecta tu desencadenante, la acción se producirá automáticamente.

Siguiendo con nuestro ejemplo, queremos enviar una solicitud POST como JSON a un punto final de Braze. Para ello, seleccione la opción **Webhooks** en **Apps**.

![]({% image_buster /assets/img_archive/zapier3.png %})

### Paso 3: Configurar Braze POST

Cuando configures tu webhook, utiliza la siguiente configuración y proporciona tu punto final REST Braze en la URL del webhook. Cuando haya terminado, seleccione **Publicar**.

- **Método**: POST
- **URL del webhook**: `https://rest.iad-01.braze.com/canvas/trigger/send`
- **Paso de datos**: Falso
- **Con capas**: No
- **Encabezado de solicitud**:
  - **Content-Type**: application/json
  - **Autorización**: Portador YOUR-API-KEY
- **Datos**: 

```json
{
  "canvas_id": "your_canvas_identifier",
  "recipients": [
    {
      "external_user_id": "external_user_identifier",
      "canvas_entry_properties":{
        "string_property": "Your example string",
        "example_integer_property": 1
      }
    }
  ]
}
```

![]({% image_buster /assets/img/zapier.png %}){: style="max-width:70%;"}

### Paso 4: Crear una campaña Braze

Una vez que haya configurado correctamente su zap, puede personalizar sus campañas Braze o Canvases con datos de WordPress utilizando el formato Liquid para mostrar la información en sus mensajes.

[5]: {% image_buster /assets/img_archive/zapier1.png %}
[6]: {% image_buster /assets/img_archive/zapier2.png %}
