---
nav_title: Mensajes push rápidos
article_title: Mensajes push rápidos
alias: "/quick_push/"
description: "Este artículo describe las cosas que debes saber al crear una campaña push o Canvas utilizando la experiencia de edición push rápida."
---

# Mensajes push rápidos

Al crear una campaña push o Canvas en Braze, puedes seleccionar varias plataformas y dispositivos para elaborar un mensaje para todas las plataformas en una única experiencia de edición llamada push rápido.

## Casos de uso

Esta experiencia de edición es ideal para los siguientes casos de uso:

- Campañas push para móviles y pasos de Mensaje en Canvas que deban enviarse a varios tipos de dispositivos (como iOS y Android).
- Notificaciones push urgentes que necesitan dirigirse a múltiples plataformas de forma rápida y precisa, cuando el contenido es el mismo en todas las plataformas (como noticias de última hora o actualizaciones de partidos en vivo).

## Crear una campaña push rápida o Canvas

Para crear una campaña dirigida a múltiples plataformas y dispositivos:

1. Crea una campaña o añade un [paso de Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) a un Canvas.  
2. Selecciona **Notificación push**.
3. Selecciona las plataformas que desees (Móvil, Web, Kindle) y los dispositivos móviles (iOS, Android). Si seleccionas varios dispositivos, las pruebas multivariante no estarán disponibles para tu campaña.

### Selección de plataformas para una campaña
![Opciones para seleccionar varias plataformas para una campaña push, como Móvil, Web y Kindle, y varios dispositivos, como iOS y Android.]({% image_buster /assets/img_archive/quick_push_1.png %})

### Selección de plataformas para un paso en Canvas
![Opciones para seleccionar varias plataformas para un paso de Mensaje push, como Móvil, Web y Kindle, y varios dispositivos, como iOS y Android.]({% image_buster /assets/img_archive/quick_push_4.png %})

{:start="4"}
4. Selecciona **Confirmar**. Después de seleccionar **Confirmar**, no podrás cambiar las plataformas o dispositivos seleccionados.
5. Continúa configurando tu campaña o Canvas.

Tu compositor tendrá un aspecto ligeramente distinto al habitual. Sigue leyendo para ver las diferencias.

### La diferencia

En la pestaña **Redactar**, puedes especificar un título, un mensaje y un comportamiento al hacer clic para todas las plataformas y dispositivos que elijas.

El panel de vista previa muestra una aproximación del aspecto que tendrá tu mensaje en cada plataforma. Aunque puede darte un buen indicador de dónde podrías alcanzar el límite de caracteres, recuerda probar siempre tus mensajes en un dispositivo real antes de enviar tu campaña.

![Vista de edición única con un campo de título, mensaje y comportamiento al hacer clic para tres tipos de push: iOS, Android y Web.]({% image_buster /assets/img_archive/quick_push_2.png %})

En la sección **Activos**, selecciona o carga las imágenes que deseas que aparezcan para cada plataforma. Ten en cuenta que los distintos dispositivos tienen especificaciones diferentes para las imágenes y el recuento de caracteres. Para obtener ayuda, consulta [Especificaciones de imágenes y texto para push]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#push).

![Sección de activos de la vista de edición única con campos para Imagen de icono push, Imagen de notificación iOS, Imagen de notificación Android e Imagen de notificación Web.]({% image_buster /assets/img_archive/quick_push_3.png %}){:style="max-width:50%"}

Después, termina de configurar tu campaña push con normalidad. Consulta [Crear una campaña push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/) para obtener más información.

## Lo que debes saber

### Tipo de notificación

El tipo de notificación predeterminado es "Push estándar" y no puede modificarse. Si deseas crear un push diferente, como Push Stories o Inline Image (Android), crea campañas separadas para cada tipo de dispositivo.

### Pruebas multivariante

Si seleccionas varios dispositivos para plataformas móviles, como iOS y Android, las pruebas multivariante no estarán disponibles para tu campaña. Si deseas realizar pruebas multivariante, crea campañas independientes para cada tipo de dispositivo.

### Configuración específica del dispositivo

Puedes editar la configuración específica de la plataforma en el editor. Esto incluye ajustes como [botones de acción para notificación push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), canales y grupos de notificación, TTL, prioridad de visualización, sonidos y mucho más. 

Ten en cuenta que los botones de acción para notificación push no son compatibles cuando te diriges tanto a iOS como a Android utilizando campañas de push rápido. Para más información sobre la configuración específica de cada dispositivo, consulta las siguientes colecciones de artículos:

- [Opciones de iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios)
- [Opciones de Android]({{site.baseurl}}/user_guide/message_building_by_channel/push/android)