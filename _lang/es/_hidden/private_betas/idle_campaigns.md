---
nav_title: "Campañas y lonas ociosas"
permalink: "/idle_campaigns_canvases/"
hidden: true
---

# Campañas y lonas ociosas

> Este artículo de referencia explica el estado de inactividad de las campañas y los Lienzos y responde a las preguntas más frecuentes.

{% alert note %}
En 2024, las Lonas se marcarán como **inactivas** y se detendrán, de forma similar a las campañas. Cuando los lienzos estén inactivos o parados, seguirán la lógica de este documento.
{% endalert %}

A las campañas y a los lienzos se les asigna un estado inactivo cuando no han enviado mensajes ni han introducido usuarios en algún tiempo. Estas campañas y Lienzos se detendrán automáticamente en sus fechas de finalización asociadas. Puedes filtrar por campañas y Lienzos inactivos para ayudarte a ordenar y gestionar tu lista de campañas y Lienzos.

## Campañas ociosas

De forma continuada, se detendrán las campañas inactivas que cumplan los siguientes criterios:
 
- Un envío único programado ha superado su fecha de envío por siete días
- Una campaña programada o basada en acciones con fecha de finalización supera su fecha de finalización en siete días
- Una campaña sin fecha de finalización que no ha enviado mensajes en un año

Para las campañas sin fecha de finalización, si se envía un mensaje o se actualiza la campaña, se reiniciará la cuenta atrás de un año para detener la campaña. Cuando se detengan las campañas, Braze lo notificará a los clientes en su panel y por correo electrónico.

Las campañas se detendrán en la fecha de detención predeterminada o un día después de la última fecha límite de conversión, lo que sea posterior. Los envíos que sean consecuencia de una Variante Ganadora o Personalizada se tratan como envíos programados, y se detendrán siete días después de que se envíe la Variante Ganadora o Personalizada. Todas las campañas se detendrán a las 4 de la madrugada UTC todos los días para todos los usuarios de Braze.

Las tarjetas de contenido no se detendrán hasta su fecha límite de caducidad, y también se atendrán a los criterios antes mencionados, así como a la regla de la fecha límite de conversión.

Consulta esta tabla para saber cómo mantener activa una campaña inactiva:

| Motivo del estado de inactividad                                                                              | Pasos para activar la campaña                     |
|-----------------------------------------------------------------------------------------------------|---------------------------------------------------|
| Campañas que son envíos únicos programados, y han pasado siete días desde la fecha de envío                 | Programar un envío futuro                            |
| Las campañas programadas o basadas en acciones, tienen fecha de finalización, y es siete días después de la fecha de finalización | Ampliar la fecha de finalización                               |
| Campañas sin fecha de finalización que no han enviado mensajes en un año                                | Envía un mensaje o realiza cualquier modificación en la campaña |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Lienzos ociosos

De forma continua, se detendrán los Lienzos ociosos que cumplan los siguientes criterios:

- Un envío único programado ha superado su fecha de envío y duración máxima en más de 7 días
- Un Canvas programado o basado en acciones con fecha de finalización ha superado su fecha de finalización y duración máxima en más de 7 días
- Un Canvas sin fecha de finalización no ha entrado en usuarios ni ha sido editado en más de 12 meses y su duración máxima

Para los Canvas sin fecha final, si se introduce un usuario o se actualiza el Canvas, se reiniciará la cuenta atrás de un año para detener el Canvas. Cuando se detengan los Lienzos, Braze lo notificará a los clientes en su panel y por correo electrónico.

La [duración máxima]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) de un Canvas es el mayor tiempo posible que un usuario puede tardar en completar un Canvas determinado. Esta duración incluye los vencimientos de las tarjetas de contenido y los mensajes dentro de la aplicación.

Consulta esta tabla para saber cómo mantener activo un Canvas inactivo:

| Motivo del estado de inactividad                                                                                                  | Pasos para activar Canvas                     |
|-------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| Lienzos que son envíos únicos programados, y su duración es de siete días como máximo a partir de la fecha de envío                 | Programar un envío futuro                          |
| Los lienzos programados o basados en acciones, tienen fecha de finalización, y son de siete días y duración máxima pasada la fecha de finalización | Ampliar la fecha de finalización                             |
| Lienzos sin fecha de fin que no han enviado mensajes en un año                                                      | Envía un mensaje o realiza cualquier edición en el Canvas |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Preguntas más frecuentes

#### ¿A qué campañas o lonas se aplica esto?

Esto se aplicará a las campañas y Lienzos que ya cumplan los criterios enumerados anteriormente, y a las campañas y Lienzos que los cumplan en el futuro.

#### ¿Cómo sé si una campaña o Canvas está inactivo?

Las campañas y Canvas inactivos se mostrarán en las páginas de lista de campañas y Canvas bajo la categoría **Inactivo**. La fecha en la que se detendrá la campaña o Canvas aparece como una columna en la lista.

#### ¿Qué ocurre si se actualiza una campaña inactiva o un Canvas?

Si se actualiza una campaña que no ha enviado ningún mensaje o un Canvas que no ha introducido usuarios, la cuenta atrás se reiniciará.

#### ¿Qué ocurre con las campañas que no han enviado ningún mensaje en un año (o las Lonas que no han introducido usuarios en un año), pero tienen una fecha de finalización en el futuro?

Detendremos estas campañas y lonas siete días después de la fecha de finalización.

#### ¿Quién recibirá notificaciones por correo electrónico sobre campañas paradas y Lienzos?

Por defecto, todos los usuarios con permisos de administrador están predeterminados para recibir notificaciones por correo electrónico sobre las campañas que se detienen automáticamente y los Lienzos. El creador de la campaña o Canvas siempre recibirá una notificación cuando se detenga. Los usuarios pueden administrar las preferencias de notificación por correo electrónico yendo a **Configuración de la empresa** > **Preferencias de notificación** y, a continuación, añadiendo o eliminando destinatarios de la notificación **Campaña detenida automáticamente** y de la notificación **Canvas detenido automáticamente**.

#### ¿Cómo funciona la detención de las tarjetas de contenido?

Las tarjetas de contenido de las campañas no se detendrán hasta su fecha límite de caducidad y el periodo de amortiguación correspondiente. Se detendrán en la fecha más tardía del periodo de amortiguación (correspondiente a si la campaña es un envío único, tiene fecha de finalización o no tiene fecha de finalización) y la fecha límite de caducidad. 

Por ejemplo, si una tarjeta de contenido caduca el 1 de abril, es un envío único y tiene un plazo de conversión de 10 días, dejará de enviarse el 12 de abril (10 días después del plazo de conversión, más un día). Si una tarjeta de contenido caduca el 1 de abril, está desencadenada por la API y no ha enviado mensajes desde el 15 de marzo, caducará el 15 de marzo del año que viene.

Los lienzos sólo se detienen cuando se detienen las tarjetas de contenido, es decir, cuando ha pasado su duración máxima.

#### Tengo un experimento con la bandera de características en mi Canvas. Una vez configurada la bandera de mi característica, ¿permanecerá activo el Canvas?

Los lienzos con pasos de bandera de características no se detienen automáticamente y no quedan inactivos.

#### ¿Por qué veo campañas inactivas en mi lista de campañas cuando he aplicado un filtro para mostrar sólo las campañas activas?

Las campañas inactivas se consideran activas hasta que se detienen.

#### ¿Aparecería una campaña como inactiva cuando sigue enviando notificaciones push?

No. Una campaña aparecerá como inactiva cuando ya no envíe mensajes activamente. 