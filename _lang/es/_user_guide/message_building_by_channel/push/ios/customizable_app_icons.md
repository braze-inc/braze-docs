---
nav_title: "Característica de icono de aplicación personalizado (iOS)"
article_title: Característica de icono de aplicación personalizado
page_order: 7
page_type: reference
description: "Este artículo de referencia cubre la actualización de iOS 10.3 sobre Icono de aplicación personalizable."
platform: iOS
channel:
  - push

---

# Característica de icono de aplicación personalizado (iOS 10.3) 

> Con iOS 10.3, Apple introdujo la posibilidad de cambiar el icono de la pantalla de inicio de una aplicación sin tener que actualizar la aplicación desde el Apple App Store. Ahora el desarrollador puede permitir al usuario cambiar el icono de la pantalla de inicio dentro de su aplicación. Apple exige que todas las imágenes de los iconos de la aplicación que el desarrollador quiera poner a disposición del usuario se incluyan en el binario que se envía a Apple para su revisión durante la publicación de la aplicación en el Apple App Store.

Para notificar a tus usuarios esta característica, es posible enviar un mensaje dentro de la aplicación o una notificación push a través de Braze al usuario explicando esta funcionalidad o preguntándole si desea cambiar su icono. El desarrollador sólo tendría que crear un vínculo profundo dentro de la aplicación donde se pueda mostrar la indicación nativa de iOS para realizar el cambio de icono. Esto es similar a la misma orientación que proporcionamos hoy sobre la configuración de una imprimación de notificación push para APN.

Además, esta mensajería puede aprovechar al máximo la segmentación para que la copia del mensaje sea altamente contextual para un usuario. También puedes aprovechar las pruebas A/B de mensajes para ver qué mensajería tiene más impacto en el resultado deseado.
