---
nav_title: Tarjetas de contacto
article_title: Tarjetas de contacto
page_order: 3
description: "Este artículo de referencia explica cómo crear una tarjeta de contacto para incluirla en tus mensajes MMS y SMS."
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS
  
---

# Tarjetas de contacto 

> Las tarjetas de contacto (a veces conocidas como vCard o Archivos Virtuales de Contacto (VCF)) son un formato de archivo estandarizado para enviar información empresarial y de contacto que puede importarse fácilmente a libretas de direcciones o de contactos. 

Las tarjetas de contacto pueden crearse [mediante programación](https://www.twilio.com/blog/send-vcard-twilio-sms) y cargarse en la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) de Braze o crearse a través de nuestro generador de tarjetas de contacto integrado. A estas tarjetas se les pueden asignar propiedades comunes como el nombre de su empresa, el número de teléfono, la dirección, el correo electrónico y una pequeña foto. Para empezar a crear tarjetas de contacto, primero asegúrate de que estás configurado para utilizar MMS en Braze.

## Generador de tarjetas de contacto

### Paso 1: Asignar nombre

Se pueden crear tarjetas de contacto a partir del compositor de SMS y MMS. Seleccione la pestaña **Generador de tarjetas de contacto** para empezar.

A continuación, se le pedirá que introduzca el nombre o apodo de su empresa. Este es el nombre que sus usuarios verán cuando guarden la tarjeta. Se impone un límite de 20 caracteres para garantizar que el usuario pueda ver el nombre completo de tu empresa o alias en sus contactos y aplicación de mensajería. 

![La pestaña del generador de tarjetas de contacto.]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### Paso 2: Asignar número de teléfono

Selecciona el grupo de suscripción y el número de teléfono deseado en las opciones desplegables disponibles. Este número aparecerá en tu tarjeta de contacto y estará disponible en su teléfono para enviarte un mensaje de texto una vez guardado.

Ten en cuenta que los códigos alfanuméricos no son compatibles con la mensajería bidireccional y no son compatibles con las tarjetas de contacto.

### Paso 3: Campos opcionales

![Campos opcionales para el generador de tarjetas de contacto.]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### Subir tarjeta de contacto foto de contacto

Puedes subir una foto de contacto en miniatura opcional para tu tarjeta de contacto. Recomendamos una imagen JPEG o PNG de 240 x 240 px. Cualquier imagen de alta resolución que se cargue se redimensionará a 240 x 240 px para garantizar la entregabilidad del mensaje, ya que los mensajes MMS de más de 5 MB pueden fallar.

#### Añade más información

Otros campos te permiten insertar tu nombre, subtítulo, dirección y otra información de contacto que tu usuario quiera tener disponible. 

### Paso 4: Guardar la tarjeta de contacto

Una vez que hayas introducido todos los campos necesarios, haz clic en **Generar tarjeta de contacto** y se adjuntará automáticamente a tu campaña o Canvas. Desde aquí, puedes añadir un mensaje, probar tu tarjeta de contacto y lanzar tu campaña o Canvas.

La tarjeta de contacto también se guardará en la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) para reutilizarla fácilmente en futuras campañas y Lienzos.

## Añadir una tarjeta de contacto existente

Para añadir una tarjeta de contacto existente, crea una campaña o Canvas y selecciona el grupo de suscripción que desees. A continuación, aparecerá una opción **Añadir medios** en la ventana del compositor de mensajes. Aquí puedes cargar un archivo de tarjeta de contacto existente o localizar uno a través de la biblioteca multimedia.
