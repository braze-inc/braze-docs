---
nav_title: Estilo del correo electrónico
article_title: Estilo de correo electrónico
page_order: 2
page_type: reference
description: "En este artículo se describen las mejores prácticas de estilo de correo electrónico que debes tener en cuenta al crear tus campañas de correo electrónico."
channel: email

---

# Estilo del correo electrónico

## Dirección de estilo

La **línea del asunto** es una de las primeras cosas que verán los destinatarios al recibir tu mensaje. Las tasas de apertura más elevadas se consiguen con entre 6 y 10 palabras. 

También hay distintos enfoques para crear una buena línea del asunto, que van desde formular una pregunta para despertar el interés del lector o ser más directo, hasta personalizarlo para que atraiga a tu clientela. No te quedes con una sola línea del asunto, aprovecha [las pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing/) para probar otras nuevas y medir su eficacia. Las líneas del asunto no deben tener más de 35 caracteres para que se muestren correctamente en el móvil.

El campo "De" debe mostrar claramente quién es el remitente. Procura no utilizar el nombre de una persona o una abreviatura poco común. En su lugar, utiliza un nombre reconocible, como el nombre de tu marca. Si utilizar el nombre de una persona se ajusta a los métodos de personalización del correo electrónico de tu marca, mantén la coherencia para desarrollar una relación con el destinatario. El nombre "De" no debe tener más de 25 caracteres para mostrarse adecuadamente en el móvil.

### Direcciones sin respuesta

Las direcciones de correo electrónico sin respuesta no suelen ser recomendables por múltiples razones, ya que desvinculan a tus lectores. Muchos destinatarios responden al correo electrónico para cancelar suscripción, por lo que, si no se les permite hacerlo, la siguiente medida suele ser marcar el correo como no deseado.

Recibir respuestas fuera de la oficina puede proporcionar información valiosa, aumentando las tasas de apertura y disminuyendo los informes de correos no deseados (al eliminar a los que no quieren recibir correos electrónicos). A nivel personal, no responder puede parecer impersonal a los destinatarios y puede hacer que dejen de recibir más correos electrónicos de tu empresa.

## Texto preencabezado

El texto preencabezado de un correo electrónico comunica el punto principal del mensaje de forma eficaz para captar el interés del lector y fomentar la apertura. Los especialistas en marketing por correo electrónico también suelen utilizar el texto preencabezado para proporcionar información adicional sobre el contenido de un correo electrónico. Un preencabezado es el texto de vista previa que aparece inmediatamente después del asunto de un correo electrónico. En el siguiente ejemplo, el preencabezado es `- Brand. New. Lounge Shorts`.

\![Texto preencabezado en un buzón de entrada de Gmail con el texto "Marca. Nuevo. Pantalones cortos de salón".]({% image_buster /assets/img_archive/preheader_example.png %})

La cantidad de texto preencabezado visible depende del cliente de correo electrónico del usuario y de la longitud de la línea del asunto del correo electrónico. Por lo general, sugerimos que los preencabezados de los correos electrónicos tengan entre 50 y 100 caracteres.

He aquí algunas buenas prácticas que debes tener en cuenta al escribir tus preencabezados:

1. Las llamadas a la acción entran en juego después de que los lectores hayan abierto tu correo electrónico.
  - Dirige a tus lectores en la dirección correcta, tanto si quieres que se suscriban, compren un producto o visiten tu sitio web.
  - Utiliza palabras fuertes para que el lector sepa exactamente lo que le estás pidiendo, pero asegúrate de que refleje la voz de la marca de tu empresa y de que cada llamada a la acción muestre algún tipo de valor para el consumidor.
  - El preencabezado no debe tener más de 85 caracteres y debe contener algún tipo de llamada a la acción descriptiva que apoye la línea del asunto.

2. El correo electrónico y los sitios de destino a los que dirijas a tus usuarios deben estar optimizados para móviles:
  - Sin cajas intersticiales
  - Grandes campos de forma
  - Fácil navegación
  - Texto grande
  - Generoso espacio en blanco
  - Cuerpo breve y conciso
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
  | Correo de Apple             | 33      |
  | Perspectivas '13            | 38      |
  | Outlook para Mac '15   | 53      |
  | Perspectivas '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }


  |  Cliente de correo electrónico Webmail  |  Límite  |
  |:----------------------:|:-------:|
  | Correo AOL               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Oficina 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tamaño del correo electrónico

Asegúrate de limitar el tamaño de tu correo electrónico. Los cuerpos de correo electrónico de más de 102 KB no sólo son extremadamente gravosos para los servidores Braze, sino que también son recortados por Gmail y otros clientes de correo electrónico. Intenta que el tamaño de tu correo electrónico no supere los 25 KB si es sólo texto o 60 KB con imágenes. Te recomendamos encarecidamente que utilices nuestro cargador de imágenes para alojarlas y que hagas referencia a ellas en `href`.

|   Sólo texto   | Texto con imágenes |     Anchura del correo electrónico    |
|:-------------:|:----------------:|:------------------:|
| 25 KB máximo |   60 KB máximo   | 600 píxeles como máximo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Longitud del texto

Consulta la tabla siguiente para conocer las longitudes de texto recomendadas.

| Especificaciones del texto | Propiedades recomendadas |
| --- | --- |
| Longitud de la línea del asunto | 35 caracteres como máximo (para una visualización óptima en el móvil) (de 6 a 10 palabras) |
| Nombre del remitente Longitud | 25 caracteres como máximo (para una visualización óptima en el móvil) |
| Longitud del preencabezado | 85 caracteres máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tamaño de la imagen

Consulta la tabla siguiente para ver los tamaños de imagen recomendados. Las imágenes más pequeñas y de alta calidad se cargarán más rápido, así que utiliza el activo más pequeño posible para conseguir el resultado deseado.

|     Talla    | Ancho de la imagen de cabecera |  Anchura de la imagen corporal  |   Tipos de archivos  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5 MB máximo | 600 píxeles como máximo | 480 píxeles como máximo | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Vinculación en profundidad

Un alto porcentaje de correos electrónicos se leen en dispositivos móviles. Utilizar [la vinculación en profundidad]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) es una gran práctica para interactuar con estos destinatarios de correo electrónico móvil. Con las notificaciones push y los mensajes dentro de la aplicación, un vínculo profundo lleva al usuario directamente a un destino especificado dentro de una aplicación. 

Sin embargo, los correos electrónicos no ofrecen la claridad de saber si los destinatarios tienen instalada la aplicación. Por tanto, evitar la vinculación en profundidad ayuda a prevenir mensajes de error para estos destinatarios de correo electrónico que no tienen la aplicación.

