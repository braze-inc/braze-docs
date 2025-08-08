---
nav_title: Estilo de correo electrónico
article_title: Estilo de correo electrónico
page_order: 2
page_type: reference
description: "En este artículo se describen las mejores prácticas de estilo de correo electrónico a las que debe remitirse al crear sus campañas de correo electrónico."
channel: email

---

# Estilo del correo electrónico

## Estilo de dirección

La **línea de asunto** es una de las primeras cosas que verán los destinatarios al recibir su mensaje. Si se limita a entre 6 y 10 palabras, obtendrá las tasas de apertura más altas. 

También hay distintos enfoques para crear una buena línea de asunto, desde formular una pregunta para despertar el interés del lector o ser más directo, hasta personalizarlo para captar la atención de su clientela. No te quedes con una sola línea del asunto, aprovecha [las pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#what-are-multivariate-and-ab-testing/) para probar otras nuevas y medir su eficacia. Las líneas de asunto no deben tener más de 35 caracteres para que se muestren correctamente en los móviles.

El campo "De" debe mostrar claramente quién es el remitente. Procure no utilizar el nombre de una persona o una abreviatura poco común. En su lugar, utilice un nombre reconocible como el de su marca. Si utilizar el nombre de una persona se ajusta a los métodos de personalización del correo electrónico de su marca, mantenga la coherencia para desarrollar una relación con el destinatario. El nombre "De" no debe tener más de 25 caracteres para que se muestre correctamente en el móvil.

### Direcciones sin respuesta

En general, las direcciones de correo electrónico sin respuesta no son recomendables por múltiples razones, ya que desvinculan a sus lectores. Muchos destinatarios responden al correo electrónico para cancelar la suscripción, por lo que, si no se les permite hacerlo, la siguiente medida suele ser marcar el correo como no deseado.

Recibir respuestas fuera de la oficina puede proporcionar información valiosa, aumentar las tasas de apertura y disminuir los informes de spam (al eliminar a quienes no quieren recibir correos electrónicos). A nivel personal, una ausencia de respuesta puede parecer impersonal a los destinatarios y hacer que dejen de recibir correos electrónicos de su empresa.

## Texto del encabezamiento

El texto del preencabezado de un correo electrónico comunica el punto principal del mensaje de forma eficaz para captar el interés del lector y fomentar la apertura. Los responsables de marketing por correo electrónico también suelen utilizar el texto del preencabezado para proporcionar información adicional sobre el contenido de un mensaje. Un preencabezado es el texto de previsualización que aparece inmediatamente después del asunto de un correo electrónico. En el siguiente ejemplo, el preencabezado es `- Brand. New. Lounge Shorts`.

![Texto preencabezado en un buzón de entrada de Gmail con el texto "Marca. Novedad. Pantalones cortos de salón".]({% image_buster /assets/img_archive/preheader_example.png %})

La cantidad de texto visible en el preencabezado depende del cliente de correo electrónico del usuario y de la longitud del asunto del mensaje. Por lo general, sugerimos que los encabezados de los correos electrónicos tengan entre 50 y 100 caracteres.

Estas son algunas de las mejores prácticas que debe tener en cuenta a la hora de redactar sus preencabezados:

1. Las llamadas a la acción entran en juego después de que los lectores hayan abierto el correo electrónico.
  - Dirija a sus lectores en la dirección correcta, ya sea para que se suscriban, compren un producto o visiten su sitio web.
  - Utilice palabras contundentes para que el lector sepa exactamente lo que le está pidiendo, pero asegúrese de que refleja la voz de la marca de su empresa y de que cada llamada a la acción exhibe algún tipo de valor para el consumidor.
  - El preencabezado no debe superar los 85 caracteres y debe contener algún tipo de llamada a la acción descriptiva que apoye la línea de asunto.

2. El correo electrónico y los sitios de aterrizaje a los que dirija a sus usuarios deben estar optimizados para móviles:
  - Sin cajas intersticiales
  - Grandes campos de formulario
  - Navegación sencilla
  - Texto grande
  - Amplio espacio en blanco
  - Texto breve y conciso
  - Llamadas a la acción claras

### Límites de caracteres del preencabezamiento

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


  |  Cliente de correo electrónico Webmail  |  Límite  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tamaño del correo electrónico

Asegúrese de limitar el tamaño de su correo electrónico. Los cuerpos de correo electrónico de más de 102 KB no sólo son extremadamente gravosos para los servidores Braze, sino que también son recortados por Gmail y otros clientes de correo electrónico. Intente que el tamaño de su correo electrónico no supere los 25 KB sólo de texto o 60 KB con imágenes. Te recomendamos encarecidamente que utilices nuestro cargador de imágenes para alojarlas y que hagas referencia a ellas en `href`.

|   Solo texto   | Texto con imágenes |     Anchura del correo electrónico    |
|:-------------:|:----------------:|:------------------:|
| 25 KB máximo |   60 KB máximo   | 600 píxeles como máximo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Longitud del texto

Consulte la siguiente tabla para conocer las longitudes de texto recomendadas.

| Especificaciones del texto | Propiedades recomendadas |
| --- | --- |
| Longitud de la línea de asunto | 35 caracteres como máximo (para una visualización óptima en móviles) (de 6 a 10 palabras) |
| Longitud del nombre del remitente | 25 caracteres como máximo (para una visualización óptima en móviles) |
| Longitud del preencabezado | 85 caracteres como máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tamaño de la imagen

Consulte la tabla siguiente para conocer los tamaños de imagen recomendados. Las imágenes más pequeñas y de alta calidad se cargarán más rápido, así que utilice el activo más pequeño posible para conseguir el resultado deseado.

|     Tamaño    | Ancho de la imagen de cabecera |  Anchura de la imagen corporal  |   Tipos de archivo  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5 MB máximo | 600 píxeles como máximo | 480 píxeles como máximo | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Vínculos profundos

Un alto porcentaje de correos electrónicos se leen en dispositivos móviles. Utilizar [la vinculación en profundidad]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/) es una gran práctica para interactuar con estos destinatarios de correo electrónico móvil. Con las notificaciones push y los mensajes in-app, un enlace profundo lleva al usuario directamente a un destino específico dentro de una aplicación. 

Sin embargo, los correos electrónicos no ofrecen la claridad de saber si los destinatarios tienen instalada la aplicación. Por lo tanto, evitar los enlaces profundos ayuda a prevenir los mensajes de error para estos destinatarios de correo electrónico que no tienen la aplicación.

