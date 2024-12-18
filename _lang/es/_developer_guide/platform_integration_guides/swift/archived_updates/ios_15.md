---
nav_title: Guía de actualización a iOS 15
article_title: Guía de actualización al SDK de iOS 15
page_order: 7
platform: iOS
description: "Este artículo de referencia cubre las nuevas actualizaciones del sistema operativo iOS 15, las actualizaciones necesarias del SDK y las nuevas características."
hidden: true
noindex: true
---

# Guía de actualización del SDK de iOS 15

> Esta guía describe los cambios introducidos en iOS 15 (WWDC21) y los pasos de actualización necesarios para tu integración de SDK de Braze iOS. Para obtener una lista completa de las nuevas actualizaciones de iOS 15, consulta [las notas de la versión iOS 15](https://developer.apple.com/documentation/ios-ipados-release-notes/ios-ipados-15-release-notes) de Apple.


## Cambios de transparencia en las navegaciones de la IU

Como parte de nuestras pruebas anuales de las betas de iOS, hemos identificado un cambio realizado por Apple que hace que determinadas barras de navegación de la interfaz de usuario aparezcan transparentes en lugar de opacas. Esto será visible en iOS 15 cuando utilices la interfaz de usuario predeterminada de Braze para las tarjetas de contenido, o cuando los enlaces profundos web se abran dentro de tu aplicación en lugar de en una aplicación de navegador independiente.

Para evitar este cambio visual en iOS 15, te recomendamos encarecidamente que actualices al [SDK para iOS de Braze v4.3.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.3.2) lo antes posible, antes de que los usuarios empiecen a actualizar su teléfono al nuevo sistema operativo iOS 15.

## Nueva configuración de notificaciones {#notification-settings}

iOS 15 introdujo nuevas características de notificación para ayudar a los usuarios a mantenerse concentrados y evitar interrupciones frecuentes a lo largo del día. Nos complace ofrecer compatibilidad con estas nuevas características. Estas características no requieren ninguna actualización adicional del SDK y sólo se aplicarán a los usuarios de dispositivos iOS 15.

### Modos de enfoque {#focus-mode}

Ahora, los usuarios de iOS 15 pueden crear "Modos de enfoque", es decir, perfiles personalizados que se utilizan para determinar qué notificaciones quieren que atraviesen su enfoque y se muestren de forma destacada.

![]({% image_buster /assets/img/ios/ios15-notification-settings.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

### Niveles de interrupción {#interruption-levels}

En iOS 15, las notificaciones push pueden enviarse con uno de los cuatro niveles de interrupción:

* **Pasivo** (nuevo) - Sin sonido, sin vibración, sin despertar la pantalla, sin romper la configuración de enfoque.
* **Activo** (predeterminado) - Permite sonido, vibración, activación de la pantalla, sin interrupción de la configuración de enfoque.
* **Sensible al tiempo** (nuevo) - Permite sonido, vibración, encender la pantalla, puede romper los controles del sistema si se permite.
* **Crítico** \- Permite sonido, vibración, encender la pantalla, puede atravesar los controles del sistema y anular el interruptor del timbre.

Consulta [Opciones de notificación de]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#interruption-level) iOS para saber más sobre cómo configurar esta opción en iOS Push.

### Resumen de la notificación {#notification-summary}

![]({% image_buster /assets/img/ios/ios15-notification-summary.png %}){: style="float:right;max-width:25%;margin-left:15px;border:0"}

En iOS 15, los usuarios pueden (opcionalmente) elegir determinadas horas a lo largo del día para recibir un resumen de las notificaciones. Las notificaciones que no requieran atención inmediata (como las enviadas como "Pasivas" o mientras el usuario está en Modo Enfoque) se agruparán para evitar interrupciones constantes a lo largo del día.

Para cada notificación que envíes, pronto podrás especificar una "puntuación de relevancia" para controlar qué notificación debe aparecer en la parte superior del resumen.

Consulta [Opciones de notificación de iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/#relevance-score) para saber más sobre cómo establecer la "puntuación de relevancia" de una notificación.

## Botones de ubicación {#location-buttons}

iOS 15 introduce una nueva y cómoda forma para que los usuarios concedan temporalmente acceso a la ubicación dentro de una aplicación. 

El nuevo botón de ubicación se basa en el permiso existente "Permitir una vez", sin preguntar repetidamente a los usuarios que hacen clic varias veces en la misma sesión.

Para más información, mira el video de Apple [Conoce el botón de ubicación](https://developer.apple.com/videos/play/wwdc2021/10102/) de la Conferencia Mundial de Desarrolladores (WWDC) de este año.

{% alert tip %}
Esta característica te da una oportunidad extra de pedir permiso a los usuarios. A los usuarios que hayan rechazado previamente los permisos de ubicación antes de iOS 15 se les mostrará un aviso al hacer clic en el botón de ubicación como una oportunidad para restablecer el permiso desde el estado rechazado por última vez.
{% endalert %}

### Utilizar botones de ubicación con Braze

No es necesaria ninguna integración adicional cuando se utilizan botones de ubicación con Braze. Tu aplicación debe seguir pasando la ubicación del usuario (una vez que haya concedido permiso) como de costumbre.

Según Apple, para los usuarios que ya hayan compartido el acceso a la ubicación en segundo plano, la opción "Mientras se utiliza la aplicación" seguirá concediendo ese nivel de permiso después de que actualicen a iOS 15.

## Correo de Apple {#mail}

Este año, Apple ha anunciado muchas actualizaciones sobre el seguimiento del correo electrónico y la privacidad. Para más información, consulta la [entrada de nuestro blog](https://www.braze.com/resources/articles/9-ways-email-marketers-can-respond-to-apples-mail-privacy-protection-feature).

## Ubicación de la dirección IP de Safari

En iOS 15, los usuarios podrán configurar Safari para anonimizar o generalizar la ubicación determinada a partir de sus direcciones IP. Tenlo en cuenta cuando utilices la segmentación basada en la ubicación.

