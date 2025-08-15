---
nav_title: Actualizar a iOS 18
article_title: Actualizar a iOS 18
page_order: 7.1
platform: 
  - iOS
description: "Este artículo contiene información sobre la versión iOS 18 para ayudarte a actualizar tu SDK fácilmente."
---

# Actualizar a iOS 18

> ¿Tienes curiosidad por saber cómo se está preparando Braze para el próximo lanzamiento de iOS? Este artículo resume nuestra información sobre la versión de iOS 18 para ayudarte a crear una experiencia fluida para ti y tus usuarios.

La [WWDC](https://developer.apple.com/wwdc24/) de Apple tuvo lugar del 9 al 11 de junio de 2024. Obtén más información sobre sus anuncios en nuestra [entrada de blog](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18), o sigue leyendo para saber cómo puedes aprovechar iOS 18 con Braze.

## Cambios en iOS 18

### Actividades en vivo en el Apple Watch

Las [Actividades en vivo](https://www.braze.com/docs/developer_guide/push_notifications/live_notifications/?sdktab=swift) serán compatibles con watchOS 11. No se requiere ninguna configuración adicional. Sin embargo, Apple ofrece la opción de personalizar la interfaz del reloj.

### Apple Vision Pro

El Vision Pro ya está disponible en China, Japón, Singapur, Australia, Canadá, Francia, Alemania y Reino Unido. Consulta nuestro blog para ver cómo [Braze es compatible con visionOS](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support).

### Notificaciones del iPhone en macOS

La nueva característica de [duplicación del iPhone](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/) de Apple permite a los usuarios recibir notificaciones del iPhone en sus dispositivos macOS. Ten en cuenta que algunos tipos de medios, como las imágenes de historias push y los GIF, no son compatibles, ya que no se pueden representar como una notificación de macOS.

### Inteligencia de Apple

[La Inteligencia de Apple](https://developer.apple.com/documentation/Updates/Apple-Intelligence) ya está disponible para dispositivos con iOS 18.1 y versiones posteriores.

Como usuario de Braze, la nueva característica más importante que debes conocer son [los resúmenes de notificación](https://support.apple.com/en-us/108781), que utilizan el procesamiento en el dispositivo para agrupar y generar automáticamente resúmenes de texto para notificaciones push relacionadas enviadas desde una única aplicación. Los usuarios finales pueden tocar para ampliar un resumen y ver cada notificación push tal y como se envió originalmente.

Debido a cómo se generan estos resúmenes, no tendrás control sobre su comportamiento específico ni sobre el texto generado. Sin embargo, esto no afectará a ninguna característica de análisis o informes, como el seguimiento push-click.

![Una captura de pantalla de muestra del resumen de la vista previa de una notificación push.]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})
