---
nav_title: "Tipos de notificaciones push"
article_title: Tipos de notificaciones push
page_order: 1
page_type: glossary
description: "Este glosario enumera los distintos tipos de notificaciones push que puede enviar con Braze."
channel: push

layout: glossary_page
glossary_top_header: "Tipos de notificaciones push"
glossary_top_text: "Hay muchos tipos de notificaciones push que puedes utilizar para interactuar con tus clientes. Pueden reducirse por canal y utilizarse para satisfacer las necesidades de muchos usuarios distintos. Puedes configurar la mayoría de estos ajustes en tus campañas Push, pero hay notas en las siguientes descripciones que te indicarán si se necesita alguna configuración de backend y cuáles podrían ser."

glossary_tag_name: Channels
glossary_filter_text: "Select any of the following channels to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: Web
  - name: Android
  - name: iOS

glossaries:
  - name: "Empuje regular"
    description: "El mensaje Push que todo lo abarca. Aparecen en el dispositivo del usuario con un sonido de notificación y un mensaje que se desliza o aparece en una barra o pila de notificaciones."
    tags:
      - Web
      - Android
      - iOS
  - name: "Notificación push web"
    description: "Estos mensajes push aparecen en Web Apps o Navegadores. Siguen necesitando permiso para llegar al cliente. Ten en cuenta que la notificación push web no funciona si el usuario utiliza un navegador oculto."
    tags:
      - Web
  - name: "Campañas Push Primer"
    description: "Campañas de mensajes dentro de la aplicación utilizadas para obtener señales explícitas de inclusión o exclusión de los usuarios. A través de la imprimación, puede evitar el envío de notificaciones a usuarios que probablemente desactiven la función push a través de los ajustes del dispositivo. Para iOS, las campañas push son relevantes, ya que las notificaciones push en primer plano (como las notificaciones que despiertan el dispositivo) no se activan hasta que el usuario opta explícitamente por la notificación push nativa de iOS."
    tags:
      - Web
      - Android
      - iOS
  - name: "Historias push"
    description: "Las Push Stories son mensajes inmersivos que llevan al usuario a través de un viaje visual en forma de carrusel. Sólo están disponibles para dispositivos móviles."
    tags:
      - iOS
      - Android
  - name: "Pulsar con botones de acción"
    description: "Los botones de acción son mensajes que permiten ofrecer opciones a los usuarios y varias llamadas a la acción."
    tags:
      - Web
      - Android
      - iOS
  - name: "Notificaciones Push enriquecidas"
    description: "Las notificaciones push enriquecidas son notificaciones con imágenes envolventes y contenidos creativos que pueden ir más allá de un simple icono y un texto de llamada a la acción."
    tags:
      - iOS
      - Android
  - name: "Notificaciones push provisionales para iOS"
    description: "Introducida por Apple en iOS 12, la autorización provisional se produce automáticamente al instalar las aplicaciones de iOS, lo que permite a las marcas enviar notificaciones silenciosas sin mostrar un aviso push a los usuarios. Cuando se envíe el push silencioso y se vea en la bandeja de notificaciones del dispositivo, los usuarios tendrán la opción de permitir o interrumpir las notificaciones push."
    tags:
      - iOS
  - name: "Notificaciones push HTML"
    description: "Las notificaciones push HTML son mensajes push codificados en HTML y no utilizan las plantillas push preestablecidas que proporciona Braze. Tener la opción de crear notificaciones push HTML permite a su empresa tener plena libertad creativa y una imagen de marca coherente cuando se trata de cómo quiere que se vean estos mensajes push."
    tags:
      - Android
  - name: "ID de notificación e ID de canal"
    description: "Los ID de notificación y los ID de canal permiten sustituir o actualizar las notificaciones push ya recibidas, pero no abiertas, por el usuario."
    tags:
      - iOS
      - Android
  - name: "Notificaciones push en segundo plano o silenciosas"
    description: "Notificaciones push que no se muestran en el dispositivo. Normalmente se utiliza para enviar paquetes de información a la aplicación para procesos en segundo plano y seguimiento de desinstalación. Se necesita un token de notificaciones push habilitado en segundo plano para que se envíe un push en segundo plano o silencioso."
    tags:
      - Web
      - Android
      - iOS
  - name: "Notificaciones push portátiles"
    description: "Estas notificaciones push permiten a las marcas enviar mensajes directamente a dispositivos wearables como el Apple Watch."
    tags:
      - iOS

---
