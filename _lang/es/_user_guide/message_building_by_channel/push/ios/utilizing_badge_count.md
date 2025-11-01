---
nav_title: Utilizar el recuento de señales
article_title: Utilizar el recuento de señales
page_order: 8

page_type: reference
description: "Este artículo trata sobre el uso del recuento de señales de iOS para reactivar la interacción de los usuarios que no han notado un push o que han desactivado las notificaciones push en primer plano."
platform: iOS
channel: 
- push
- in-app messages

---

# Utilizar el recuento de señales

> La cuenta de señales de iOS muestra el número de notificaciones no leídas dentro de tu aplicación, tomando la forma de un círculo rojo en la esquina superior derecha del icono de la aplicación. En los últimos años, las señales se han convertido en un medio eficaz de reactivación de la interacción de los usuarios de aplicaciones.

El recuento de señales puede utilizarse para reactivar la interacción de tus usuarios que no hayan notado un push, o que hayan desactivado las notificaciones push en primer plano. Del mismo modo, puede utilizarse para notificar a tus usuarios los mensajes que no han visto, como las actualizaciones dentro de la aplicación.

## Recuento de señales con Braze

Puedes especificar el recuento de señales deseado cuando redactes una notificación push a través del panel de Braze. Puede establecerse como un atributo del usuario con mensajería personalizada, lo que permite una lógica infinitamente personalizable. Si deseas enviar un push silencioso que actualice el recuento de señales sin molestar al usuario, añade la bandera "Contenido disponible" a tu push y deja vacío el contenido de su mensaje.

{% alert note %}
¿Te preguntas cómo configurar el recuento de señales para Android? Android gestiona automáticamente las señales de las aplicaciones para push, por lo que no hay configuraciones personalizadas para las señales en Braze.
{% endalert %}

### Eliminar el recuento de señales

Establece el recuento de señales en 0 o "" para eliminar el recuento de señales del icono de la aplicación. Braze también borrará automáticamente la señal cuando se reciba una notificación push mientras la aplicación está en primer plano.

## Buenas prácticas

Para optimizar el poder de reactivación de la interacción de las señales, es crucial que configures los ajustes de tus señales de forma que simplifiquen al máximo la experiencia del usuario.

### Mantén bajo el número de señales
Los estudios demuestran que, cuando el número de señales supera los dos dígitos, los usuarios suelen perder interés en las actualizaciones y a menudo dejan de utilizar la aplicación.

> Puede haber excepciones a esta regla dependiendo de la naturaleza de tu aplicación (por ejemplo, correo electrónico y aplicaciones de mensajería en grupo).

### Limitar las cosas que puede representar un recuento de señales
Cuando pongas una señal, querrás que las notificaciones sean lo más claras y directas posible. Limitando el número de cosas que puede representar una notificación de señal, puedes proporcionar a tus usuarios una sensación de familiaridad con las características y actualizaciones de tu aplicación.

