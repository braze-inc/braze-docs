---
nav_title: Configuración de promociones de Gmail
article_title: Configuración de promociones de Gmail
page_order: 8
description: "Este artículo de referencia explica cómo utilizar Braze para ayudarte a crear la tarjeta de promociones para móviles de Gmail a partir de tu campaña de correo electrónico."
channel:
  - email

---

# Configuración de la promoción de Gmail

> La [pestaña Promociones de Gmail para móviles](https://developers.google.com/gmail/promotab/) permite a los profesionales del marketing enviar más información mediante anotaciones en una "tarjeta", en lugar de limitarse a la línea de asunto o a la información del preencabezado. Braze tiene una herramienta integrada que le ayuda a crear la tarjeta de su campaña de correo electrónico.

## Requisito previo

En primer lugar, envía tus dominios y subdominios al equipo de difusión de la pestaña Promociones de Google a la dirección <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> para añadirlos a la lista de permitidos de Gmail. Esto te permite utilizar cualquier función que muestre imágenes enriquecidas, como el carrusel de productos de la pestaña Promociones de Gmail.

## Construir la tarjeta con Braze

Sigue estos pasos para crear una tarjeta promocional de Gmail para una campaña de correo electrónico. Ten en cuenta que al salir de la sección **Contenido** del editor se restablecerán los campos y la información de la pestaña **Promoción de Gmail**. Complete la configuración de su tarjeta promocional y copie el HTML generado para no perder su código HTML.

1. [Crea tu campaña de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) y selecciona el **editor** HTML como experiencia de edición.
2. Ve a la sección **Contenido** del editor HTML y selecciona la pestaña **Promoción de Gmail**.
3. Rellene los campos de **Información básica** y, a continuación, haga clic en **Generar código HTML**. Esto ayudará a generar la secuencia de comandos para su tarjeta Gmail Promo Tab en la sección **Copiar y pegar código HTML en `<Head>`**. <br> ![Un ejemplo de cómo construir una tarjeta.]({% image_buster /assets/img/create-gmail-promo.png %})
4. Elige si deseas incluir solo una oferta de descuento, tarjetas de promoción o ambas para tu tarjeta de promoción de Gmail. <br> ![Opciones para incluir una oferta de descuento y tarjetas de promoción.]({% image_buster /assets/img_archive/gmail_promo_discount.png %}){: style="max-width:70%;"}
5. Copie y pegue el script en el elemento `<head>` del HTML de su correo electrónico.

{% alert warning %}
La secuencia de comandos Promociones sólo aparece si tu correo electrónico aparece en la pestaña Promociones de Gmail. Actualmente, Gmail utiliza algoritmos para determinar dónde irá a parar tu correo electrónico. Sin embargo, si un usuario marca alguna vez tu correo electrónico como promoción, el algoritmo de Gmail hará caso omiso y tu correo electrónico aparecerá automáticamente en la pestaña Promociones en adelante.
{% endalert %}

### Incluir una oferta de descuento

Configurar una oferta de descuento le permite especificar las fechas válidas para un descuento. Tras determinar tu oferta de descuento, selecciona una fecha y hora de inicio. Tiene la opción de finalizar la oferta de descuento en un momento determinado o de no finalizarla nunca.

![Opciones para especificar el valor de la oferta, el código y la fecha y hora de inicio de una oferta de descuento.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

### Personalizar el carrusel de productos

Las tarjetas de promoción en tu carrusel de productos son útiles para proporcionar imágenes a tu oferta. También puede personalizar las variables de su carrusel de productos e incluir hasta diez vistas previas de imágenes, donde cada imagen es única.

![Un ejemplo de carrusel de productos de una empresa llamada Motto con el encabezamiento de correo electrónico "Nuestros calcetines más vendidos están de rebajas", con tres imágenes de calcetines y sus precios rebajados.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

| Variable personalizable | Descripción |
|---|---|
| URL de imagen | La URL de tu imagen. Cada imagen de su carrusel de productos debe tener una URL única y utilizar la misma relación de aspecto (4:5, 1:1, 1,91:1). |
| URL de destino | El enlace para su promoción. |
| Titular | (opcional) Descripción de la promoción en una o dos frases. Aparece bajo la imagen de previsualización. |
| Divisa | (opcional) La moneda del precio. |
| Precio | El precio de la promoción. |
| Valor del descuento | El importe descontado del precio original. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Le recomendamos que cargue las imágenes de sus productos en la mediateca y, a continuación, copie y pegue las URL en los campos correspondientes. Sólo se aceptan formatos de imagen estáticos (PNG y JPEG). Algunos formatos de imagen (GIF) se cargarán pero no se mostrarán como se espera.
{% endalert %}

### Buenas prácticas

En general, sigue estas [prácticas recomendadas por Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
Aunque puede utilizar Liquid dentro de este script, le recomendamos encarecidamente que pruebe su mensajería tanto como sea posible para evitar un error.
{% endalert %}

#### Incorporación de imágenes

Gmail ha obtenido mejores resultados con imágenes potentes relacionadas con el mensaje de correo electrónico. Gmail no recomienda utilizar un diseño de solo texto, ya que este espacio se diseñó para aportar a la vista previa un lenguaje visual, que es vital para el marketing por correo electrónico. No utilice imágenes con texto recortado ni repita imágenes en varias campañas.

#### Describir ofertas

Gmail no sugiere el uso de frases u oraciones, como "Puedes comprar 1 y llevarte 1 gratis o Descuentos en todos los pantalones cortos y camisas", ya que puede recortar, dejar de llamar la atención y competir con la línea del asunto. Este espacio sólo debe utilizarse para atraer a sus clientes con sus mensajes, por lo que debe evitar cualquier lenguaje similar a "Abra este correo electrónico ahora" o "Haga clic aquí para ver las ofertas". Lo mejor es evitar repetir el asunto.

## Preguntas más frecuentes

### ¿Por qué mi mensaje promocional no muestra la tarjeta de promoción o el carrusel de productos en la bandeja de entrada del usuario final?

Hay muchos factores que determinan si el carrusel de productos se mostrará en la pestaña Promoción de Gmail.

Todas las imágenes de la anotación tienen que pasar un filtro de calidad. Para que el carrusel de productos se complete, es fundamental que todas las imágenes de la anotación tengan la relación de aspecto recomendada, y que sean imágenes de alta calidad o de alta resolución de primeros planos del producto. Las imágenes deben contener poco o ningún texto (preferible). El filtro de calidad también filtra los contenidos inapropiados, por lo que las imágenes deben ser aptas para familias, usuarios y niños.

Además, Gmail tiene un límite de densidad para el número de carruseles de productos que aparecen en la pestaña Promoción de Gmail de un usuario. Por ejemplo, si un usuario se suscribe a muchas marcas que utilizan carruseles de productos en sus correos electrónicos de promoción, Gmail acaba poniendo un límite al número de carruseles de productos que se muestran.

Debido a las normas de privacidad y seguridad de Google, los correos electrónicos con anotaciones deben enviarse ampliamente para que la anotación funcione. Es recomendable lanzar una campaña y enviarla al menos a 100 destinatarios para que el sistema de Google la detecte como un "envío masivo". Las URL de las imágenes no pueden variar de un destinatario a otro.

### ¿Cómo se rastrean los clics en una tarjeta promocional o en un carrusel de productos?

Braze o cualquier otro ESP no son capaces de insertar el seguimiento de enlaces en los enlaces de la sección de cabecera. Esto significa que no se pueden rastrear los clics en una tarjeta de promoción o en un carrusel de productos.

### ¿Hay alguna forma de ver cuántos usuarios han recibido un carrusel de productos?

Gmail determina cuándo y a quién mostrar la tarjeta, por lo que no se garantiza que todos los destinatarios vean el carrusel de productos.

