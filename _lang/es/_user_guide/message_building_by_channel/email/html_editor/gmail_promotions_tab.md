---
nav_title: Configuración de las promociones de Gmail
article_title: Configuración de promociones de Gmail
page_order: 8
description: "Este artículo de referencia explica cómo utilizar Braze para ayudarte a crear la tarjeta de promociones para móviles de Gmail a partir de tu campaña de correo electrónico."
channel:
  - email
toc_headers: h2
---

# Configuración de la promoción de Gmail

> La [pestaña Promociones de Gmail para móviles](https://developers.google.com/gmail/promotab/) permite a los especialistas en marketing enviar más información mediante anotaciones en una "tarjeta", en lugar de limitarse a la línea del asunto o a la información del preencabezado. Braze tiene una herramienta integrada que te ayuda a crear la tarjeta a partir de tu campaña de correo electrónico.

## Requisito previo

En primer lugar, envía tus dominios y subdominios al equipo de difusión de la pestaña Promociones de Google a la dirección <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> para añadirlos a la lista de permitidos de Gmail. Esto te permite utilizar cualquier característica que muestre imágenes enriquecidas, como el carrusel de productos de la pestaña Promociones de Gmail.

## Construir la tarjeta con Braze

Sigue estos pasos para crear una tarjeta promocional de Gmail para una campaña de correo electrónico. Ten en cuenta que al salir de la sección **Contenido** del editor se restablecerán los campos y la información de la pestaña **Promoción de Gmail**. Completa la configuración de tu tarjeta promocional y copia el HTML generado para no perder tu código HTML.

### Paso 1: Crear una campaña de correo electrónico

En primer lugar, [crea tu campaña de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) y selecciona el **editor de código HTML** como experiencia de edición.

### Paso 2: Añadir detalles a la tarjeta de promoción de Gmail

A continuación, ve a la sección **Contenido** del editor HTML y selecciona la pestaña **Promoción de Gmail**. Rellena los campos de **Información básica** y, a continuación, selecciona **Generar código HTML**. Esto ayudará a generar el script para tu tarjeta de la pestaña Promociones de Gmail en la sección **Copiar y pegar código HTML en `<Head>`**.

![Un ejemplo de cómo construir una tarjeta.]({% image_buster /assets/img/create-gmail-promo.png %})

### Paso 3: Personaliza tu tarjeta de promoción de Gmail

Elige si quieres incluir una oferta de descuento, una tarjeta de oferta, una tarjeta de promoción o todas las opciones para tu tarjeta de promoción de Gmail.

{% tabs %}
{% tab Discount offer %}

Configurar una oferta de descuento te permite especificar las fechas válidas para un descuento. 

1. Selecciona el alternador **Oferta de descuento**.
2. En **Oferta**, introduce un breve resumen del descuento. Un ejemplo es "20% de descuento".
3. En **Código**, añade el código promocional que el usuario debe aplicar al pagar.
4. A continuación, selecciona la fecha y hora de inicio de la oferta de descuento.
5. Determina si la oferta de descuento debe terminar a una hora determinada o no terminar nunca.

![Opciones para especificar el valor de la oferta, el código y la fecha y hora de inicio de una oferta de descuento.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Deal Cards %}

Utiliza tarjetas de ofertas para proporcionar información clave sobre las ofertas directamente en la parte superior del cuerpo de los correos electrónicos. Esto permite a los destinatarios comprender rápidamente los detalles de la oferta y pasar a la acción. Por ejemplo, puedes utilizar tarjetas de ofertas para promocionar ofertas por tiempo limitado y reducir la necesidad de que los usuarios busquen detalles dentro de los correos electrónicos.

1. Selecciona el alternador **Tarjeta de oferta**.
2. En **Oferta**, introduce un breve resumen del descuento. Un ejemplo es "20% de descuento en todos los zapatos".
3. (opcional) En **Código**, añade el código promocional que el usuario debe aplicar al pagar.
4. Introduce al menos una de las siguientes URL. 
-  **URL de la página de la oferta:** La URL de la página de destino de la oferta específica. Esto crea un botón "Comprar ahora" (o similar). Te recomendamos que proporciones esta URL para tu tarjeta de oferta. 
- **URL de la página de inicio del comerciante:** La URL de tu página de inicio principal. Utiliza este campo solo si no está disponible la URL de una página de oferta específica.
5. (opcional) Añade una fecha de inicio para la oferta.
6. Determina si la oferta debe terminar a una hora determinada o no terminar nunca.

![Opciones para especificar el valor de la oferta, el código y la fecha y hora de inicio de una tarjeta de oferta.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Promotion cards %}

Las tarjetas de promoción en tu carrusel de productos son útiles para proporcionar imágenes a tu oferta. También puedes personalizar las variables de tu carrusel de productos e incluir hasta diez vistas previas de imágenes, donde cada imagen es única.

1. Selecciona el alternador **Tarjetas de promoción**.
2. Selecciona **Añadir tarjeta de promoción**. Cada imagen de tu carrusel de productos debe tener una URL única y utilizar la misma relación de aspecto (4:5, 1:1, 1.91:1).
3. Incluye una URL de la imagen.
4. En **URL de destino**, añade el enlace de tu promoción.

{% alert tip %}
Te recomendamos que subas las imágenes de tus productos a la biblioteca multimedia y, a continuación, copies y pegues las URL en los campos correspondientes. Solo se aceptan formatos de imagen estáticos (PNG y JPEG). Algunos formatos de imagen (GIF) se cargarán pero no se mostrarán como se espera.
{% endalert %}

{: start="5"}
5. Personaliza tu tarjeta promocional añadiendo un titular, una moneda, un precio y el valor del descuento.

| Propiedad personalizable | Descripción |
|---|---|
| Titular | (opcional) Descripción de la promoción en una o dos frases. Aparece bajo la imagen de vista previa. |
| Divisa | (opcional) La moneda del precio. |
| Precio | El precio de la promoción. |
| Valor del descuento | El importe descontado del precio original. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Un ejemplo de carrusel de productos de una empresa llamada Motto con el encabezado de correo electrónico "Nuestros calcetines más vendidos están de oferta", con tres imágenes de calcetines y sus precios rebajados.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Paso 4: Generar y pegar código HTML

Después de crear tu tarjeta promocional de Gmail, selecciona **Generar código HTML**. Copia y pega el script en el elemento `<head>` del HTML de tu correo electrónico. 

{% alert tip %}
Para el editor de arrastrar y soltar, copia y pega el código HTML generado en la sección de [etiquetas de encabezado personalizadas]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#custom-head-tags), en **Configuración de envío**.
{% endalert %}

{% alert warning %}
El script de Promociones solo aparece si tu correo electrónico llega a la pestaña Promociones de Gmail. Actualmente, Gmail utiliza algoritmos para determinar dónde irá a parar tu correo electrónico. Sin embargo, si un usuario marca alguna vez tu correo electrónico como promoción, el algoritmo de Gmail se ignorará y tu correo electrónico aparecerá automáticamente en la pestaña Promociones en adelante.
{% endalert %}

## Medir las tarjetas de Gmail

Gmail no devuelve análisis sobre estas tarjetas, y los proveedores de servicios de correo electrónico (ESP) como Braze no pueden insertar su propio seguimiento de enlaces en los enlaces de la sección de encabezado (incluidas las tarjetas de promoción y los carruseles de productos). Sin embargo, puedes añadir parámetros UTM o códigos únicos a las URL durante la configuración. Estos parámetros te permiten hacer un seguimiento de la interacción utilizando tus propios análisis del sitio web o el seguimiento de conversión, porque el seguimiento forma parte de la propia URL, no lo inserta el ESP. El seguimiento de clics a nivel de ESP no está disponible para estos enlaces.

### Incorpora imágenes

Gmail ha obtenido mejores resultados con imágenes potentes relacionadas con el mensaje de correo electrónico. Gmail no recomienda utilizar un diseño de solo texto, ya que este espacio se diseñó para aportar a la vista previa un lenguaje visual, que es vital para el marketing por correo electrónico. No utilices imágenes con texto recortado ni repitas imágenes en varias campañas.

### Describe las ofertas

Gmail no sugiere el uso de frases u oraciones, como "Puedes comprar 1 y llevarte 1 gratis o Descuentos en todos los pantalones cortos y camisas", ya que puede recortarse, dejar de llamar la atención y competir con la línea del asunto. Este espacio solo debe utilizarse para atraer a tus clientes con tu mensajería, por lo que debes evitar cualquier lenguaje similar a "Abre este correo electrónico ahora" o "Haz clic aquí para ver las ofertas". Lo mejor es evitar repetir la línea del asunto.

## Buenas prácticas

En general, sigue estas [prácticas recomendadas por Gmail](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
Aunque puedes utilizar Liquid dentro de este script, te recomendamos encarecidamente que pruebes tu mensajería tanto como sea posible para evitar errores.
{% endalert %}

### Previsualiza tu anotación

Utiliza la [herramienta de vista previa](https://developers.google.com/workspace/gmail/promotab/preview) para previsualizar tu anotación. Ten en cuenta que enviarte un correo electrónico de prueba no funcionará para las anotaciones, ya que tu anotación solo se renderiza si el correo electrónico se envía a un número significativo de destinatarios. Asegúrate de enviar el correo electrónico final (con sus URL de imágenes) a al menos 100 destinatarios de Gmail.

No utilices Google Workspace para enviar correos electrónicos con anotaciones. Utiliza únicamente dominios de correo electrónico incluidos en la lista de permitidos para enviar anotaciones a un grupo grande de destinatarios.

### Cumple con las directrices de imágenes

Comprueba que tus imágenes cumplan con estas directrices:
- Utiliza imágenes de alta calidad y alta resolución.
- Todas las imágenes anotadas deben usar la misma relación de aspecto. Las relaciones de aspecto compatibles incluyen: 4:5, 1:1, 1.91:1.
- Utiliza tamaños de imagen correctos. El mínimo es 256x256; el máximo es 4096x4096 píxeles.

Gmail recomienda evitar:
- Usar demasiado texto en tus imágenes
- Usar imágenes que sean solo iconos
- Usar imágenes con máscaras redondeadas
- Usar URL de imágenes personalizadas

### Regístrate con DMARC

Para que tus anotaciones se rendericen correctamente, confirma que los dominios enviados estén registrados con DMARC y que todas las políticas estén habilitadas.


## Preguntas más frecuentes

### ¿Por qué mi mensaje promocional no muestra la tarjeta de promoción o el carrusel de productos en el buzón de entrada del usuario final?

Hay muchos factores que determinan si el carrusel de productos se mostrará en la pestaña Promociones de Gmail.

Todas las imágenes de la anotación tienen que pasar un filtro de calidad. Para que se llene el carrusel de productos, todas las imágenes de la anotación deben tener la relación de aspecto de imagen recomendada y ser imágenes de producto en primer plano de alta calidad y alta resolución. Las imágenes deben contener poco o ningún texto. El filtro de calidad también filtra los contenidos inapropiados, por lo que las imágenes deben ser aptas para familias, usuarios y niños.

Además, Gmail tiene un límite de densidad en el número de carruseles de productos que aparecen en la pestaña Promociones de Gmail de un usuario. Por ejemplo, si un usuario se suscribe a muchas marcas que utilizan carruseles de productos en su correo electrónico de promoción, Gmail acaba poniendo un límite al número de carruseles de productos que se muestran.

Debido a las normas de privacidad y seguridad de Google, los correos electrónicos con anotaciones deben enviarse ampliamente para que la anotación funcione. Se recomienda lanzar una campaña y enviarla al menos a 100 destinatarios para que el sistema de Google la detecte como "envío masivo". Las URL de las imágenes no pueden variar de un destinatario a otro.

### ¿Cómo se rastrean los clics en una tarjeta promocional o en un carrusel de productos?

Ni Braze ni cualquier otro ESP pueden insertar el seguimiento de enlaces en los enlaces de la sección de encabezado. Esto significa que no se pueden rastrear los clics en una tarjeta de promoción o en un carrusel de productos.

### ¿Hay alguna forma de ver cuántos usuarios han recibido un carrusel de productos?

Gmail determina cuándo y a quién mostrar la tarjeta, por lo que no se garantiza que todos los destinatarios vean el carrusel de productos.

### ¿Por qué no veo anotaciones en la pestaña Promociones de Gmail?

Las anotaciones no son compatibles con Google Workspace. Para previsualizar las anotaciones, puedes crear una dirección de correo electrónico personal con Gmail.

Ten en cuenta que las anotaciones no se renderizan en la pestaña **Principal** ni en ninguna otra pestaña de la aplicación móvil de Gmail. Las anotaciones no se mostrarán después de que un usuario abra un correo electrónico o si estás utilizando el tipo de anotación `DiscountOffer` y la hora y la fecha ya han expirado.