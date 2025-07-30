---
nav_title: Entender las instalaciones de usuario
article_title: Entender las instalaciones de usuario 
page_order: 7
page_type: reference
description: "Este artículo de referencia describe las instalaciones de usuarios (seguimiento de atribución de instalaciones) y las distintas formas de aplicar esta información en su campaña."
tool:
  - Campaigns
  - Segments
---

# Entender las instalaciones de los usuarios

> El seguimiento de la atribución de la instalación es una excelente forma de mejorar la relación inicial con el usuario. Saber cómo, dónde y, lo que es aún más importante, por qué un usuario instala tu aplicación te permite comprender mejor quién es tu usuario y cómo debes presentarle tu aplicación. 

Aunque Braze no proporciona seguimiento de atribución de instalaciones, podemos integrarnos con [servicios]({{site.baseurl}}/partners/message_orchestration/) como Branch y AppsFlyer para proporcionarle datos de instalación sin problemas.

## Segmente a sus usuarios

Una vez que el usuario instala la aplicación, puede empezar a segmentarlo en función de los siguientes [filtros de atribución de instalación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#install-attribution). Por ejemplo, una aplicación de viajes podría añadir usuarios procedentes de un anuncio relacionado con ofertas de vacaciones en la playa a un segmento de "amantes de la playa". Del mismo modo, una aplicación de música podría segmentar a los usuarios en función del género musical mostrado en el anuncio que dio lugar a la instalación.

## Buenas prácticas

### Incorporación personalizada

Ahora que tienes más información sobre tu usuario, puedes personalizar su proceso de incorporación. Esto podría ser tan sencillo como cambiar las imágenes de tus mensajes para que se ajusten a sus preferencias, o tan complejo como crear un onboarding de usuario único para cada anuncio que pudiera conducir a una instalación. Para escalar una secuencia completa de mensajes que tenga en cuenta el comportamiento del usuario, consulta nuestra documentación sobre [Canvas]({{site.baseurl}}/developer_guide/rest_api/messaging/#canvas).

### Datos de referencia del anuncio

Los usuarios pueden ser atraídos a su aplicación por una oferta promocional o un sorteo. El uso de datos de atribución de instalación le permite enviar campañas que contengan códigos de descuento u ofertas sólo a los usuarios que se instalaron gracias a estas promociones. De forma similar, si tu anuncio contiene información sobre un producto concreto (como una película específica en una aplicación de video o una venta en una aplicación de comercio electrónico), puedes enviar campañas que dirijan a los usuarios a la página correcta de tu aplicación.

## Evaluar los esfuerzos publicitarios

Instalar datos de atribución puede ser valioso para evaluar la eficacia de diferentes campañas de marketing. Echar un vistazo para ver qué anuncios y campañas están consiguiendo más instalaciones y cuáles se están quedando atrás puede servirte para centrar tus recursos en los anuncios más atractivos.

