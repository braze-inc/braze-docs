---
nav_title: Utilización del recuento de insignias
article_title: Utilización del recuento de insignias
page_order: 8

page_type: reference
description: "En este artículo se explica cómo utilizar el recuento de insignias de iOS para volver a captar a los usuarios que no han recibido una notificación push o que han desactivado las notificaciones push en primer plano."
platform: iOS
channel: 
- push
- in-app messages

---

# Utilizar el recuento de insignias

> El recuento de insignias de iOS muestra el número de notificaciones no leídas dentro de tu aplicación, tomando la forma de un círculo rojo en la esquina superior derecha del icono de la aplicación. En los últimos años, las insignias se han convertido en un medio eficaz de reactivación de la interacción de los usuarios de aplicaciones.

El recuento de insignias puede utilizarse para volver a captar a los usuarios que no hayan recibido una notificación push o que hayan desactivado las notificaciones push en primer plano. Del mismo modo, puede utilizarse para notificar a los usuarios los mensajes que no han visto, como las actualizaciones de la aplicación.

## Recuento de insignias con Braze

Puedes especificar el recuento de señales deseado cuando redactes una notificación push a través del panel de Braze. Esto puede establecerse en un atributo del usuario con mensajes personalizados, lo que permite una lógica infinitamente personalizable. Si desea enviar un push silencioso que actualice el recuento de insignias sin molestar al usuario, añada el indicador "Contenido disponible" a su push y deje vacío el contenido de su mensaje.

{% alert note %}
¿Te preguntas cómo configurar el recuento de insignias para Android? Android gestiona automáticamente el badging de aplicaciones para push, por lo que no hay ajustes de personalización para el badging en Braze.
{% endalert %}

### Eliminar el recuento de insignias

Establezca el recuento de insignias en 0 o "" para eliminar el recuento de insignias del icono de la aplicación. Braze también borrará automáticamente la insignia cuando se reciba una notificación push mientras la aplicación está en primer plano.

## Buenas prácticas

Para optimizar el poder de reactivación de la interacción de las insignias, es crucial que configures los ajustes de estas de forma que simplifiquen al máximo la experiencia del usuario.

### Mantén bajo el número de insignias
Los estudios demuestran que, cuando el número de insignias supera los dos dígitos, los usuarios suelen perder interés en las actualizaciones y a menudo dejan de utilizar la aplicación.

> Puede haber excepciones a esta regla dependiendo de la naturaleza de tu aplicación (por ejemplo, aplicaciones de correo electrónico y mensajería en grupo).

### Limitar lo que puede representar un recuento de insignias
A la hora de colocar una placa, conviene que las notificaciones sean lo más claras y directas posible. Al limitar el número de cosas que puede representar una notificación de insignia, puede proporcionar a sus usuarios una sensación de familiaridad con las funciones y actualizaciones de su aplicación.

