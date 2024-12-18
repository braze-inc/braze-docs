---
nav_title: Campañas push rápidas
article_title: Campañas push rápidas
alias: "/quick_push/"
description: "Este artículo describe las cosas que hay que saber al crear una campaña push utilizando la experiencia de edición rápida de push."
---

# Campañas rápidas

Al crear una campaña push en Braze, puede seleccionar varias plataformas y dispositivos para elaborar un mensaje para todas las plataformas en una única experiencia de edición denominada push rápido.

{% alert important %}
Esta funcionalidad sólo está disponible para las campañas.
{% endalert %}

## Ejemplos

Esta experiencia de edición es la mejor para los siguientes casos de uso:

- Campañas push para móviles que deben enviarse a varios tipos de dispositivos (como iOS y Android).
- Notificaciones push sensibles al tiempo que necesitan dirigirse a múltiples plataformas de forma rápida y precisa, cuando el contenido es el mismo en todas las plataformas (como noticias de última hora o actualizaciones de partidos en directo).

## Creación de una campaña push rápida

Para crear una campaña dirigida a múltiples plataformas y dispositivos:

1. Vaya a **Campañas** y haga clic en **Crear campaña**.
2. Selecciona **Notificación push**.
3. Seleccione las plataformas que desee (Móvil, Web, Kindle) y los dispositivos móviles (iOS, Android). Si seleccionas varios dispositivos, la prueba multivariante no estará disponible para tu campaña.

![Opciones para seleccionar varias plataformas para una campaña push, como Móvil, Web y Kindle, y varios dispositivos, como iOS y Android.][1]

{:start="4"}
4\. Haga clic en **Siguiente**. Después de hacer clic en **Siguiente**, no podrá cambiar las plataformas o dispositivos seleccionados.
5\. Continúa configurando tu campaña push.

Tu compositor tendrá un aspecto ligeramente distinto al habitual. Siga leyendo para ver las diferencias.

### La diferencia

En la pestaña **Redactar**, puede especificar un título, un mensaje y un comportamiento al hacer clic para todas las plataformas y dispositivos que elija.

El panel de vista previa muestra una aproximación del aspecto que tendrá tu mensaje en cada plataforma. Aunque puede darte un buen indicador de dónde podrías alcanzar el límite de caracteres, recuerda probar siempre tus mensajes en un dispositivo real antes de enviar tu campaña.

![Vista de edición única con un campo de título, mensaje y comportamiento al hacer clic para tres tipos de push: iOS, Android y Web.][2]

En la sección **Activos**, seleccione o cargue las imágenes que desea que aparezcan para cada plataforma. Tenga en cuenta que los distintos dispositivos tienen especificaciones diferentes para las imágenes y el recuento de caracteres. Consulte los [formatos de mensajes push e imágenes][3] para obtener ayuda.

![Sección de activos de la vista de edición única con campos para Imagen de icono push, Imagen de notificación iOS, Imagen de notificación Android e Imagen de notificación Web.][4]{:style="max-width:50%"}

Después, termina de configurar tu campaña push normalmente. Consulte [Crear una campaña push][5] para obtener más información.

## Lo que hay que saber

### Tipo de notificación

El tipo de notificación predeterminado es "Push estándar" y no puede modificarse. Si desea crear un push diferente, como Push Stories o Inline Image (Android), cree campañas separadas para cada tipo de dispositivo.

### Pruebas multivariantes

Si selecciona varios dispositivos para plataformas móviles, como iOS y Android, las pruebas multivariantes no estarán disponibles para su campaña. Si desea realizar pruebas multivariantes, cree campañas independientes para cada tipo de dispositivo.

### Ajustes específicos del dispositivo

Los ajustes específicos de iOS y Android no son compatibles cuando se seleccionan varias plataformas o dispositivos. Esto incluye ajustes como [pulsadores de acción]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_action_buttons/), canales y grupos de notificación, TTL, prioridad de visualización, sonidos y mucho más.

Para más información sobre los ajustes específicos de cada dispositivo, consulte las siguientes colecciones de artículos:

- [Opciones de iOS][6]
- [Opciones de Android][7]


[1]: {% image_buster /assets/img_archive/quick_push_1.png %}
[2]: {% image_buster /assets/img_archive/quick_push_2.png %}
[4]: {% image_buster /assets/img_archive/quick_push_3.png %}

[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/ios
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android