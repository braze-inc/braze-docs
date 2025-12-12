---
nav_title: Seguimiento de usuarios
article_title: Seguimiento de usuarios a través de un formulario
description: "Aprende a identificar a los usuarios que envían un formulario a través de tu página de destino añadiendo una etiqueta de Liquid a tus mensajes."
page_order: 2
---

# Seguimiento de usuarios a través de un formulario

> Aprende a hacer un seguimiento de los usuarios que envían un formulario a través de tu página de destino añadiendo una etiqueta de Liquid de página de destino a tus mensajes. Esta etiqueta de Liquid es compatible con todos los canales de mensajería de Braze, incluidos correo electrónico, SMS, mensajes dentro de la aplicación, etc. Para saber más sobre los [datos de]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/about_tracking_data) seguimiento, consulta [Acerca de los datos de seguimiento de la página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/about_tracking_data).

## Cómo funciona

Puedes añadir una etiqueta de Liquid {% raw %}`{% landing_page_url %}`{% endraw %} a cualquiera de tus mensajes de uno o varios canales en Braze. Cuando un usuario visite esa página de destino y envíe el formulario, Braze vinculará automáticamente esos datos a su perfil existente, en lugar de crear un perfil nuevo para ese usuario. En el siguiente ejemplo, se utiliza una etiqueta de Liquid de la página de destino para enlazar a los clientes con un cuestionario:

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
También puedes utilizar las páginas de aterrizaje para generar clientes potenciales incrustando la URL de la página en tus canales externos. Después de crear una página de destino, ve a **Detalles de la página de destino** para obtener la URL única de tu página de destino.
{% endalert %}

## Utilizar etiquetas de Liquid en la página de destino

### Requisitos previos

Antes de empezar, tendrás que crear una [página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) y una [campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

### Paso 1: Verifica la URL de la página {#page-url}

Braze utilizará la URL de tu página de destino para generar su etiqueta de Liquid única. Si quieres cambiar la URL de la página actual, ve a **Mensajería** > **Páginas de destino** y, a continuación, abre tu página de destino. En **URL de página**, puedes introducir una nueva URL de página.

{% alert warning %}
Si cambias la URL de la página después de enviar tu mensaje, cualquier usuario que intente visitar tu página de destino utilizando la URL antigua será enviado a una página `404`.
{% endalert %}

URL de página de ejemplo para una página de destino en Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Paso 2: Generar la etiqueta de Liquid

Ve a **Mensajería** > **Campañas** y, a continuación, elige una campaña. En tu editor de mensajes, selecciona **Personalización**.

\![El botón "Añadir personalización" del editor de arrastrar y soltar.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

Braze generará automáticamente una etiqueta de Liquid utilizando [la URL de](#page-url) tu [página de destino](#page-url). Consulta la tabla siguiente para generar tu etiqueta:

**|Tipo de personal**ización| Elige **Página de Aterrizaje**.
|Página de**aterrizaje|Elige** la página de aterrizaje [que creaste](#prerequisites) previamente.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para añadir la etiqueta de Liquid a tu mensaje, puedes seleccionar **Insertar** o copiar el fragmento al portapapeles y añadirlo manualmente.

\![Una etiqueta de Liquid autogenerada para la página de destino seleccionada.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

Tu fragmento de código será similar al siguiente:

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### Paso 3: Finaliza y envía tu mensaje

Incrusta el fragmento de código Liquid en tu mensaje y, a continuación, finaliza el resto del mensaje. Por ejemplo:

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

Cuando estés listo, puedes enviar el mensaje para iniciar el seguimiento de los usuarios a través de tu página de destino.
