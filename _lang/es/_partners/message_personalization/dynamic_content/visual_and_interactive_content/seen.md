---
nav_title: VISTO
article_title: VISTO
description: "Este artículo de referencia describe la asociación entre Braze y SEEN, una plataforma para diseñar videos personalizados para aumentar la interacción a lo largo del recorrido del cliente."
alias: /partners/seen/
page_type: partner
search_tag: Partner
---

# VISTO

> [SEEN](https://seen.io/) es una plataforma de personalización de videos que permite a las empresas crear y construir videos en torno a sus clientes para entregarles una experiencia más atractiva. Con SEEN, puedes diseñar un video en torno a tus datos, personalizarlo a escala en la nube y luego distribuirlo donde mejor funcione.

## Ejemplos

SEEN ofrece una personalización de video automatizada a lo largo de todo el recorrido del cliente. Los usos más comunes son la incorporación, la fidelización, el registro y la conversión, así como la recuperación y la lucha contra el abandono.

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo          | Descripción                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Una campaña SEEN   | Se requiere una campaña SEEN para beneficiarse de esta asociación.                                                                     |
| Origen de datos   | Tendrás que enviar datos a SEEN para personalizar tus videos. Asegúrate de que tienes todos los datos relevantes disponibles en Braze, y de que pasas los datos con **braze_id** como identificador. |
| URL Webhook de Transformación de datos Braze   | La Transformación de Datos Braze se utilizará para reformatear los datos entrantes de SEEN de modo que puedan ser aceptados por el punto final /users/track de Braze. |

## Límite de velocidad

La API SEEN acepta actualmente 1.000 llamadas por hora.

## Integración de SEEN con Braze

En el siguiente ejemplo, enviaremos los datos de los usuarios a SEEN para la generación del video, y recibiremos un enlace único a la página de destino y una miniatura única y personalizada de vuelta a Braze para su distribución. Este ejemplo utiliza un webhook POST para enviar datos a SEEN, y una transformación de datos para recibir los datos de vuelta a Braze. Si tienes varias campañas de video con SEEN, repite el proceso para conectar Braze con todas las campañas de video.

{% alert tip %}
Si tienes algún problema, ponte en contacto con tu administrador del éxito del cliente de SEEN para que te ayude.
{% endalert %}

### Paso 1: Crear una campaña webhook

Crea una nueva [campaña webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) en Braze. Dale un nombre a tu campaña y, a continuación, consulta la tabla siguiente para componer tu webhook:

{% raw %}
<table>
  <thead>
    <tr>
      <th><strong>Campo</strong></th>
      <th><strong>Detalles</strong></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>URL del webhook</strong></td>
      <td>Utiliza la siguiente URL de webhook. Recibirás tu <code>campaign_slug</code> de SEEN para llamar al punto final correcto.<br><br><code>https://api.seen.io/v1/campaigns/{campaign_slug}/receivers/</code></td>
    </tr>
    <tr>
      <td><strong>Método HTTP</strong></td>
      <td>Utiliza el <code>POST</code> método.</td>
    </tr>
    <tr>
      <td><strong>Cuerpo de la solicitud</strong></td>
      <td>Introduce el cuerpo de tu solicitud en texto sin formato similar al siguiente.<br><br><pre><code>[
    {
    "first_name":"{{${first_name}}}",
    "last_name":"{{${last_name}}}",
    "email":"{{${email_address}}}",
    "customer_id":"{{${braze_id}}}"
    }
]</code></pre><br>Para más información, consulta la <a href="https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/overview/tvy2F5tS3JRM7DfcHwz5fK#request-content">API SEEN</a>.</td>
    </tr>
    <tr>
      <td><strong>Encabezado de solicitud</strong></td>
      <td>Utiliza la siguiente información para rellenar tus encabezados de solicitud:<br>- <strong>Autorización:</strong> <code>Token {token}</code><br>- <strong>Tipo de contenido:</strong> <code>application/json</code><br><br>Recibirás tu token de autenticación de SEEN.</td>
    </tr>
  </tbody>
</table>
{% endraw %}
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ahora puedes probar el webhook con un usuario cambiando a la pestaña **Prueba**.

Si todo funciona según lo previsto, ve a Braze y establece la tasa de envío de la campaña en 10 **mensajes por minuto**. De este modo no superarás el límite de velocidad de la SEEN de 1.000 llamadas por hora.

### Paso 2: Crear transformación de datos

1. Crea nuevos campos de [atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) para `landing_page_url` y `email_thumbnail_url`. Estos son los dos atributos que utilizaremos en este ejemplo.
2. Abre [Transformación de Datos]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#prerequisites) en **Configuración de Datos**, y selecciona **Crear transformación**.
3. Dale un nombre a tu transformación, luego elige **Empezar de cero** y establece **Destino** en **POST: Seguimiento de usuarios**.
4. Selecciona **Compartir la URL de tu webhook con SEEN**.
5. Puedes utilizar el código siguiente como punto de partida para la transformación:

```javascript
let brazecall = {
  "attributes": [
    {
      "braze_id": payload.customer_id,
      "_update_existing_only": true,
      "landing_page_url": payload.landing_page_url,
      "email_thumbnail_url": payload.email_thumbnail_url
    }
  ]
};
return brazecall;
```
{% alert note %}
Si quieres incluir otros datos, asegúrate de incluirlos también. Recuerda hablar también con SEEN para que la carga útil de la devolución de llamada incluya todos los campos necesarios.
{% endalert %}

{: start="6"}
6\. Envía una carga útil de prueba al punto final proporcionado. Si quieres utilizar la carga útil de devolución de llamada definida en la [documentación de SEEN](https://docs.seen.io/api-documentation/ntRoJJ3rXoHzFXhA94JiHB/callbacks/k9DEbcgkq3Vr2pxbHyPQbp), puedes enviarla tú mismo con [Postman](https://www.postman.com/) u otro servicio similar:

```json
{
        "customer_id": "101",
        "campaign_slug": "onboarding",
        "landing_page_url": "your.subdomain.com/v/12345",
        "video_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/output.m3u8",
        "thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/thumbnail.jpg",
        "email_thumbnail_url": "https://motions.seen.io/298abdcf-1f0f-46e7-9c26-a35b4c1e83cc/d3c1dffdf063986ad521a63e3e68fd7d1100c90a/email_thumbnail.jpg"
       
}
```

{: start="7"}
7\. Selecciona **Validar** para asegurarte de que todo funciona según lo previsto.
8\. Selecciona **Guardar** y **Activar**.
