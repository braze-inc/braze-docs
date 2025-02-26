---
nav_title: "Función de icono de aplicación personalizado (iOS)"
article_title: Icono de aplicación personalizado
page_order: 7
page_type: reference
description: "En este artículo de referencia se cubre la actualización de iOS 10.3 sobre Ícono de aplicación personalizable."
platform: iOS
channel:
  - push

---

# Función de icono de aplicación personalizado (iOS 10.3) 

> Con iOS 10.3 Apple introdujo la posibilidad de cambiar el icono de la pantalla de inicio de una app sin tener que actualizar la aplicación desde la Apple App Store. El desarrollador puede ahora permitir al usuario cambiar el icono de la pantalla de inicio dentro de su aplicación. Apple exige que todas las imágenes de los iconos de la aplicación que el desarrollador quiera poner a disposición del usuario se incluyan en el binario que se envía a Apple para su revisión durante la publicación de la aplicación en el App Store de Apple.

Para notificar a sus usuarios de esta función es posible enviar un mensaje in-app o una notificación push a través de Braze al usuario explicando esta funcionalidad o preguntándole si desea cambiar su icono. El desarrollador sólo tendría que crear un enlace profundo en la aplicación donde se pueda mostrar el aviso nativo de iOS para realizar el cambio de icono. Esto es similar a la misma orientación que proporcionamos en torno a la configuración de una imprimación de notificaciones push para APNs hoy.

Además, esta mensajería puede aprovechar al máximo la segmentación para que la copia del mensaje sea muy contextual para un usuario. También puede aprovechar las pruebas A/B de mensajes para ver qué mensaje tiene más impacto en el resultado deseado.
