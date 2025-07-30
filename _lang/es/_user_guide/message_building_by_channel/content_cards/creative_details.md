---
nav_title: Detalles creativos
article_title: Detalles creativos para las tarjetas de contenido
page_order: 1
description: "Este artículo cubre detalles creativos como las recomendaciones de tamaño de imagen y el comportamiento de descarte en los tres tipos de tarjetas de contenido estándar."
channel:
  - content cards
tool: Media

---

# Detalles creativos de las tarjetas de contenidos

> La personalización de las tarjetas de contenido y del feed en el que se encuentran no puede realizarse durante el proceso de creación de la campaña: debe trabajar con sus ingenieros y desarrolladores para crear y personalizar sus tarjetas. Para más detalles técnicos, visita nuestra [documentación para desarrolladores]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Tipos de tarjetas de contenido

{% tabs %}
{% tab Clásico %}

La tarjeta clásica es ideal para mensajes y notificaciones estándar o incluso para categorizar visualmente los mensajes con iconos. La imagen es opcional, pero debe tener una proporción de 1:1.

![Imagen de una tarjeta clásica con detalles recomendados y un ejemplo de tarjeta clásica]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| Capacidad de la tarjeta | Detalles |
| --- | ---|
| Texto de cabecera | 18px; Negrita <br> Lo ideal es una línea de texto. <br> Puede utilizar Liquid aquí para personalizar su mensaje. |
| Texto del mensaje | 13px; Peso normal <br> Lo ideal son de dos a cuatro líneas de texto. <br> Puede utilizar Liquid aquí para personalizar su mensaje. |
| Texto de enlace | Opcional. <br> 13 px <br> Enlace a página web o vínculo profundo dentro de tu aplicación. |
| Imagen | Opcional. <br> Debe tener una proporción de 1:1. <br> Recomendamos una calidad de imagen de 60 x 60 px. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Imagen subtitulada %}

La tarjeta de imagen con pie de foto es una forma estupenda de mostrar y llamar la atención sobre contenido importante, como una gran venta o una nueva función de la aplicación.

![Imagen de una tarjeta de Imagen Subtitulada con los detalles recomendados y un ejemplo de tarjeta de Imagen Subtitulada]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| Capacidad de la tarjeta | Detalles |
| --- | ---|
| Texto de cabecera | 18px; Negrita <br> Lo ideal es una línea de texto. <br> Puede utilizar Liquid aquí para personalizar su mensaje. |
| Texto del mensaje | 13px; Peso normal <br> Lo ideal son de dos a cuatro líneas de texto. <br> Puede utilizar Liquid aquí para personalizar su mensaje. |
| Texto de enlace | Opcional. <br> 13 px <br> Enlace a página web o vínculo profundo dentro de tu aplicación. |
| Imagen | Se sugiere una proporción de 4:3. <br> Anchura mínima de 600 px.  <br> Admite PNG, JPEG y GIF de alta resolución. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Sólo imagen %}

Si quieres más control creativo, la tarjeta de sólo imagen es para ti. Crea tu imagen utilizando cualquier herramienta que te guste y cárgala en este tipo de tarjeta.

![Imagen de una tarjeta de contenido de sólo imagen con detalles recomendados y un ejemplo de sólo imagen]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| Capacidad de la tarjeta | Detalles |
| --- | ---|
| Tarjeta vinculada | Opcional. <br> 13 px <br> El comportamiento al hacer clic enlaza a una página web o a un enlace profundo dentro de su aplicación. |
| Imagen | Admite cualquier relación de aspecto. <br> Anchura mínima de 600 px.  <br> Admite PNG, JPEG y GIF de alta resolución. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Detalles creativos globales {#general}

Las tarjetas de contenido vienen con una gran funcionalidad desde el principio. En este momento, el estilo de la tarjeta no se puede hacer de forma nativa en su cuenta Braze, pero puede estilizar su tarjeta de contenido por tipo y el feed de la tarjeta de contenido durante la integración. Consulta [Personalizar tarjetas de contenido]({{site.baseurl}}/developer_guide/content_cards/) para obtener más información.

### Comportamiento de descarte

Para que un usuario descarte una tarjeta, puede retirarla en el móvil o utilizar la función `close X`, como se muestra en la siguiente captura de pantalla. El `x` aparecerá al pasar el ratón solo para el SDK Web.

![Imagen que muestra los comportamientos de deslizar o cerrar el descarte de tarjeta]({% image_buster /assets/img/dismissal-cc.png %})

Si un usuario ha descartado todas sus tarjetas o usted no ha enviado ninguna actualización, el feed del usuario tendrá normalmente este aspecto:

![Imagen de una fuente de tarjeta de contenido vacía]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}

{% alert tip %}
Mantenga la relevancia de las tarjetas de contenido configurándolas para que se descarten cuando un usuario realice acciones relevantes. Por ejemplo, configure las tarjetas de contenido promocional para que se descarten en cuanto los usuarios realicen una compra, de modo que no sigan viendo una oferta por algo que ya han comprado.
{% endalert %}

### Uso de GIF en las tarjetas de contenido

| Tarjetas de contenido para Android | Tarjetas de contenido para iOS | Tarjetas de contenido para Web |
| --- | --- |---|
| El SDK de Android no proporciona soporte para GIF animados por defecto. Para más detalles sobre cómo activar la compatibilidad con GIF, consulta [GIF]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android). | El SDK Swift no proporciona soporte para GIF animados de forma predeterminada. Para obtener más información sobre la activación de la compatibilidad con GIF, consulta el [tutorial sobre compatibilidad con GIF](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | La compatibilidad con GIF está incluida por defecto en la integración del SDK Web. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

