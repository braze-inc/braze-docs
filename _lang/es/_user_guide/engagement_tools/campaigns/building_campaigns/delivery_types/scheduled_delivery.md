---
nav_title: Entrega programada
article_title: Entrega programada
page_order: 0
page_type: reference
description: "Este artículo de referencia describe las diferencias entre las opciones de programación basadas en el tiempo para la entrega de campañas."
tool: Campaigns

---

# Entrega programada

> Las campañas enviadas mediante entrega programada en función de la hora se entregan en los días especificados.

## Opción 1: Enviar en cuanto se lance la campaña

Si eliges enviar un mensaje en cuanto se lance, tu mensaje empezará a enviarse en cuanto termines de crear tu campaña.

\![La sección "Entrega" con la opción "Programada" seleccionada y la opción de programación en función del tiempo de envío en cuanto se lance la campaña.]({% image_buster /assets/img_archive/schedule_immediately.png %})

Este tipo de programación está diseñada para campañas puntuales que deseas enviar inmediatamente, como mensajes sobre un acontecimiento actual. Una aplicación deportiva, por ejemplo, puede programar notificaciones push sobre actualizaciones de resultados utilizando esta opción. Además, cuando envíes mensajes de prueba dirigidos sólo a ti o a tu equipo, esta opción te permite entregarlos inmediatamente. 

Si piensas editar la campaña y volver a enviarla después de ver la prueba, asegúrate de marcar la casilla que hace que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/reeligibility/) para recibir la campaña. Por defecto, Braze envía una campaña a un usuario sólo una vez, a menos que esa casilla esté marcada.

## Opción 2: Enviar a una hora determinada

Programar una campaña para un tiempo determinado te permite especificar los días y horas en que se enviará tu campaña. Puedes enviar un mensaje una vez, diaria, semanal o mensualmente a una hora determinada del día, así como especificar cuándo debe empezar y terminar tu campaña. Esta fecha final es inclusiva, lo que significa que el último envío será en la fecha final. 

Si seleccionas **Entrega programada** y no eliges enviar a la hora local del usuario, tu campaña se enviará según la zona horaria especificada en tu página **Configuración de la empresa**.

Las opciones de programación basadas en el tiempo para enviar una campaña a una hora determinada.]({% image_buster /assets/img_archive/schedule_designated.png %})

### Campañas en zonas horarias locales

Puedes entregar el mensaje en las zonas horarias locales de los usuarios para que los miembros de tu audiencia internacional no reciban una notificación a horas intempestivas. Las campañas en zonas horarias locales deben programarse con 24 horas de antelación para garantizar que los usuarios elegibles de todas las zonas horarias puedan recibirlas. Consulta [las Preguntas frecuentes sobre campañas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#how-do-i-schedule-a-local-time-zone-campaign/) para entender cómo funcionan las campañas según la zona horaria local y las normas de entrega asociadas.

Los segmentos a los que se dirigen las campañas de zonas horarias locales deben incluir, como mínimo, una ventana de 2 días para incorporar usuarios de todas las zonas horarias. Por ejemplo, si tu campaña está programada para enviarse por la tarde, pero sólo tiene una ventana de 1 día, algunos usuarios pueden haber quedado fuera del segmento al llegar a su zona horaria. Ejemplos de filtros que crean una ventana de 2 días son "último uso hace más de 1 día" y "último uso hace menos de 3 días", o "primera compra hace más de 7 días" y "primera compra hace menos de 9 días".

### Casos de uso

Los horarios designados son los más adecuados para los mensajes programados con antelación y las campañas recurrentes, como las de incorporación y retención, que se ejecutan regularmente con todos los usuarios cualificados.

## Opción 3: Intelligent Timing

[Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) te permite entregar una campaña a cada usuario a una hora diferente. Braze calcula el tiempo de cada individuo en función de cuándo suele interactuar con tu aplicación y sus notificaciones. Opcionalmente, puedes especificar que las campañas de Intelligent Timing sólo se envíen durante una determinada parte del día. Por ejemplo, si estás notificando a los usuarios una promoción que finaliza a medianoche, puede que quieras que tus mensajes se envíen como muy tarde a las 10 de la noche.

Las opciones de programación basadas en el tiempo para utilizar Intelligent Timing para enviar una campaña en el momento más popular para utilizar la aplicación entre todos los usuarios.]({% image_buster /assets/img_archive/schedule_intelligent.png %})

### Normas de entrega

Como la hora óptima de un usuario puede ser cualquier momento a lo largo de 24 horas, todas las campañas de Intelligent Timing deben programarse con 24 horas de antelación. Además, de forma similar a las campañas con horario designado, los mensajes con una ventana de 1 día pasarán por alto a los usuarios que queden fuera del segmento antes de que se alcance su hora óptima en su zona horaria. Los segmentos de las campañas de Intelligent Timing deben incorporar como mínimo una ventana de 3 días para tenerlo en cuenta.

Si el perfil de un usuario no tiene suficientes datos para calcular una hora óptima, puedes elegir un método de reserva para enviar durante la hora más popular de uso de la aplicación entre todos los usuarios o una hora de reserva personalizada. 

### Casos de uso

Las campañas de Intelligent Timing funcionan mejor para mensajes puntuales y recurrentes en los que hay cierta flexibilidad en cuanto a la hora de entrega, como cuando no son adecuadas para noticias de última hora o anuncios programados.

