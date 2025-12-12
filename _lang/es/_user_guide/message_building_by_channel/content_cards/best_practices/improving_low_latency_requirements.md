---
nav_title: Mejorar la baja latencia
article_title: Mejorar la baja latencia de las tarjetas de contenido como banners
page_order: 10
description: "Este artículo trata de las estrategias para garantizar que se cumplen los requisitos de baja latencia con las tarjetas de contenido."
channel:
  - content cards
---

# Mejorar la latencia de las tarjetas de contenido como banners

> Si estás experimentando latencia con tu implementación de Tarjetas de Contenido para casos de uso críticos, como los banners de la página de inicio, revisa esta página para conocer estrategias y consejos que te ayudarán a resolver y acelerar tu renderización.

{% alert tip %}
¿Quieres mostrar banners destacados y personalizados en tu aplicación o sitio web? Prueba [los banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/), creados para soportar casos de uso de banners de baja latencia.
{% endalert %}

## Utiliza la entrada programada en lugar de la entrada basada en acciones

Las tarjetas basadas en acciones, tanto en campañas como en Lienzos, requieren un proceso de fondo. Braze debe recibir primero la notificación de la acción desencadenante (como la realización de una compra o el inicio de una sesión) antes de crear una tarjeta para un usuario. Como consecuencia, habrá un retraso antes de que estas tarjetas estén disponibles.

Las tarjetas basadas en acciones introducirán una complejidad añadida a tu aplicación, en la que puede que te encuentres continuamente sondeando y refrescando para esperar a que la tarjeta esté disponible. En lugar de eso, configura tu tarjeta para que sea `Scheduled Entry`, que actuará como una ventana de disponibilidad para que la tarjeta esté siempre disponible para la audiencia objetivo.

Si programas tus tarjetas con antelación, estarán listas, esperando a que el usuario abra tu aplicación y solicite las tarjetas.

## Utiliza la lógica de envío "A primera impresión".

Junto con los envíos programados, la opción `At First Impression` evitará la latencia debido a la velocidad con la que se crea y almacena una tarjeta en Braze. La página `At Campaign Launch` crea por adelantado todas las tarjetas para todos los usuarios segmentados, lo que puede llevar tiempo. La opción `At First Impression` generará una tarjeta para un usuario la primera vez que la solicite, como cuando un usuario abre tu aplicación por primera vez.

Esto significa que, junto con la entrada programada, las tarjetas estarán disponibles inmediatamente, en cuanto las necesites, ya sea al inicio de la sesión o para una ventana de elegibilidad basada en el tiempo.

## Recuerda que la entrada en Canvas es un requisito previo para recibir tarjetas

Cuando utilices Canvas, recuerda que un usuario debe entrar primero en el Canvas según tus criterios de entrada configurados, y *luego* debe pasar por el paso de mensajes de tu tarjeta de contenido. Sólo entonces la tarjeta estará disponible para tu aplicación o sitio web. Recuerda que existe una latencia incorporada para que se cree la tarjeta una vez que el usuario pasa por el paso y puede retrasarse cuando la tarjeta esté disponible.

## No refresques excesivamente las tarjetas

El SDK actualiza automáticamente las tarjetas de contenido cada vez que se inicia una nueva sesión. También puedes solicitar manualmente una actualización de la tarjeta de contenido en cualquier momento durante una sesión activa.

Llamar al método `requestContentCardsRefresh` y refrescar con demasiada frecuencia puede provocar un límite de velocidad. Si tu aplicación está temporalmente limitada en cuanto a velocidad, es posible que no puedas actualizar las tarjetas cuando lo necesites o en un momento crítico de la interacción del usuario con tu aplicación.

Para evitar que esto ocurra, llama a este método de actualización sólo en momentos importantes del ciclo de vida del usuario, como después de que un usuario realice una compra o después de que un usuario actualice su nivel de suscripción.

## Evita incluir Contenidos conectados

El contenido conectado enriquece las tarjetas de contenido con datos propios o de terceros de la API. Sin embargo, cuando se incluye en un mensaje de tarjeta de contenido, bloqueará la disponibilidad de la tarjeta hasta que pueda completarse la solicitud de la red de contenido conectado. En algunos casos, esto hará que los SDK vuelvan a intentarlo unos segundos más tarde en un esfuerzo por no retrasar la lógica de renderización de tu aplicación, que puede esperar a que el SDK complete su tarea de actualización.

Si debes utilizar Contenido conectado, programa estas tarjetas con antelación y utiliza la opción `At Campaign Launch` para que las tarjetas se creen previamente antes de la próxima sesión de un usuario. Ten en cuenta que estas tarjetas no estarán disponibles inmediatamente, ya que Braze escribe todas las tarjetas para todos los usuarios elegibles.
