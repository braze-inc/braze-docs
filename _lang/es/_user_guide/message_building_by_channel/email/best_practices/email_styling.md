---
nav_title: Estilo del correo electrónico
article_title: Estilo de correo electrónico
page_order: 2
page_type: reference
description: "En este artículo se describen las mejores prácticas de estilo de correo electrónico a las que puedes recurrir al crear tus campañas de correo electrónico."
channel: email

---

# Estilo del correo electrónico

## Estilo de dirección

La **línea del asunto** es una de las primeras cosas que verán los destinatarios al recibir tu mensaje. Si la limitas a entre 6 y 10 palabras, obtendrás las tasas de apertura más altas. 

También hay distintos enfoques para crear una buena línea del asunto, desde formular una pregunta para despertar el interés del lector o ser más directo, hasta personalizarla para captar la atención de tu clientela. No te quedes con una sola línea del asunto, aprovecha las [pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing/) para probar otras nuevas y medir su eficacia. Las líneas del asunto no deben tener más de 35 caracteres para que se muestren correctamente en dispositivos móviles.

El campo "De" debe mostrar claramente quién es el remitente. Procura no utilizar el nombre de una persona o una abreviatura poco común. En su lugar, utiliza un nombre reconocible como el de tu marca. Si utilizar el nombre de una persona se ajusta a los métodos de personalización del correo electrónico de tu marca, mantén la coherencia para desarrollar una relación con el destinatario. El nombre "De" no debe tener más de 25 caracteres para que se muestre correctamente en el móvil.

### Direcciones sin respuesta

Por lo general, no se recomienda utilizar direcciones de correo electrónico sin respuesta por múltiples razones, ya que alejan a tus lectores. Muchos destinatarios responden al correo electrónico para cancelar su suscripción, por lo que, si no se les permite hacerlo, la siguiente medida suele ser marcar el correo como no deseado.

Recibir respuestas de fuera de la oficina puede proporcionar información valiosa, aumentar las tasas de apertura y disminuir los informes de correos no deseados (al eliminar a quienes no quieren recibir correos electrónicos). A nivel personal, una dirección sin respuesta puede parecer impersonal a los destinatarios y hacer que dejen de recibir correos electrónicos de tu empresa.

## Texto del preencabezado

El texto del preencabezado de un correo electrónico comunica el punto principal del mensaje de forma eficaz para captar el interés del lector y fomentar la apertura. Los especialistas en marketing por correo electrónico también suelen utilizar el texto del preencabezado para proporcionar información adicional sobre el contenido de un mensaje. Un preencabezado es el texto de vista previa que aparece inmediatamente después del asunto de un correo electrónico. En el siguiente ejemplo, el preencabezado es `- Brand. New. Lounge Shorts`.

![Texto de preencabezado en un buzón de entrada de Gmail con el texto "Brand. New. Lounge Shorts".]({% image_buster /assets/img_archive/preheader_example.png %})

La cantidad de texto visible en el preencabezado depende del cliente de correo electrónico del usuario y de la longitud del asunto del mensaje. Por lo general, sugerimos que los preencabezados de los correos electrónicos tengan entre 50 y 100 caracteres.

{% alert note %}
El preencabezado puede hacer referencia a Liquid en el cuerpo del correo electrónico, y el cuerpo del correo electrónico puede hacer referencia a Liquid en el preencabezado. Esto se debe a que el texto del preencabezado forma parte del cuerpo del correo electrónico cuando envías mensajes a los destinatarios.
{% endalert %}

Estas son algunas de las mejores prácticas que debes tener en cuenta a la hora de redactar tus preencabezados:

1. Las llamadas a la acción entran en juego después de que los lectores hayan abierto el correo electrónico.
  - Dirige a tus lectores en la dirección correcta, ya sea para que se suscriban, compren un producto o visiten tu sitio web.
  - Utiliza palabras contundentes para que el lector sepa exactamente lo que le estás pidiendo, pero asegúrate de que refleja la voz de marca de tu empresa y de que cada llamada a la acción aporta algún tipo de valor al consumidor.
  - El preencabezado no debe superar los 85 caracteres y debe contener algún tipo de llamada a la acción descriptiva que apoye la línea del asunto.

2. El correo electrónico y los sitios de destino a los que redirijas a tus usuarios deben estar optimizados para dispositivos móviles:
  - Sin cajas intersticiales
  - Campos de formulario grandes
  - Navegación sencilla
  - Texto grande
  - Amplio espacio en blanco
  - Texto breve y conciso
  - Llamadas a la acción claras

### Límites de caracteres del preencabezado

  |   Cliente de correo electrónico móvil  |  Límite  |
  |:----------------------:|:-------:|
  | Outlook para iOS            | 74      |
  | Android nativo         | 43      |
  | Android Gmail          | 24      |
  | iOS nativo             | 82      |
  | iOS Gmail              | 30      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

  |  Cliente de correo electrónico de escritorio  |  Límite  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook para Mac '15   | 53      |
  | Outlook '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }


  |  Cliente de correo electrónico webmail  |  Límite  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tamaño del correo electrónico

Asegúrate de limitar el tamaño de tu correo electrónico. Los cuerpos de correo electrónico de más de 102&nbsp;KB no solo suponen una carga excesiva para los servidores de Braze, sino que también son recortados por Gmail y otros clientes de correo electrónico. Intenta que el tamaño de tu correo electrónico no supere los 25&nbsp;KB solo de texto o 60&nbsp;KB con imágenes. Te recomendamos encarecidamente que utilices nuestro cargador de imágenes para alojarlas y que hagas referencia a ellas mediante `href`.

|   Solo texto   | Texto con imágenes |     Anchura del correo electrónico    |
|:-------------:|:----------------:|:------------------:|
| 25&nbsp;KB máximo |   60&nbsp;KB máximo   | 600 píxeles como máximo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Para guardar tu campaña o plantilla de correo electrónico, asegúrate de que el cuerpo del mensaje no supere los 400&nbsp;KB.
{% endalert %}

## Longitud del texto

Consulta la siguiente tabla para conocer las longitudes de texto recomendadas.

| Especificaciones del texto | Propiedades recomendadas |
| --- | --- |
| Longitud de la línea del asunto | 35 caracteres como máximo (para una visualización óptima en móviles) (de 6 a 10 palabras) |
| Longitud del nombre del remitente | 25 caracteres como máximo (para una visualización óptima en móviles) |
| Longitud del preencabezado | 85 caracteres como máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tamaño de la imagen

Consulta la tabla siguiente para conocer los tamaños de imagen recomendados. Las imágenes más pequeñas y de alta calidad se cargarán más rápido, así que utiliza el activo más pequeño posible para conseguir el resultado deseado.

|     Tamaño    | Ancho de la imagen de encabezado |  Ancho de la imagen del cuerpo  |   Tipos de archivo  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5&nbsp;MB máximo | 600 píxeles como máximo | 480 píxeles como máximo | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Vínculos profundos

Con las notificaciones push y los mensajes dentro de la aplicación, un [vínculo profundo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) lleva a los usuarios directamente a un destino específico dentro de una aplicación. Sin embargo, los vínculos profundos requieren que la aplicación esté instalada, y los correos electrónicos no ofrecen una forma de saber si los destinatarios tienen la aplicación. Esto significa que los vínculos profundos en los correos electrónicos pueden generar errores para los destinatarios que no tienen la aplicación instalada.

En su lugar, utiliza [enlaces universales y App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links), que funcionan como URLs estándar. Puedes configurarlos para que abran la aplicación o dirijan a los usuarios a una página específica. También pueden redirigir a la tienda de aplicaciones o recurrir a una página web cuando la aplicación no está instalada.