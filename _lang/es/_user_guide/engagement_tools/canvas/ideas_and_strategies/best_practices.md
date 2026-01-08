---
nav_title: Buenas prácticas
article_title: Buenas prácticas en Canvas
page_order: 1
description: "Este artículo proporciona algunas prácticas recomendadas para crear y personalizar recorridos de usuario con Canvas y Canvas Flow."
tool: Canvas

---

# Las mejores prácticas de Canvas

> Este artículo proporciona algunas prácticas recomendadas para crear y personalizar recorridos de usuario con Canvas y Canvas Flow.

## Identifica tu objetivo

¡Sumérgete en el qué, el quién y el por qué!
- ¿Qué intentas ayudar a conseguir a los usuarios?
- ¿Quiénes son los usuarios a los que quieres llegar?
- ¿Por qué construyes este Canvas?

## Mezcla y combina

Desbloquea nuevas combinaciones de recorridos de usuario con los [componentes de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/).
- Divide a tus usuarios con la [División de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) y crea flujos de trabajo diferentes.
- Espacia tus recorridos de usuario con un paso de [Retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/).
- Añade [mensajes independientes]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) donde quieras en tu flujo de Canvas. 

## Crea mensajes más ricos

Atrae a tus usuarios con mensajes más ricos.

- Crea [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) para lienzos de incorporación para sacar el máximo partido a tu primera impresión.
- Introduce [tarjetas de contenido]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) en un viaje Canvas para ofertas promocionales y notificaciones push.

## Prueba tus recorridos de usuario

Determina el impacto de tu mensaje Canvas incorporando grupos de control. De este modo, podrás hacerte una idea de cómo se ha recibido tu Canvas.

- Nombra cada paso de tu Canvas para identificar el recorrido de tu usuario.
- Aprovecha el componente [Rutas de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) en tu recorrido de usuario para asignar aleatoriamente a los usuarios a las distintas rutas que crees. 
- Diversifica tus recorridos de usuario con pasos de Retraso y Mensaje para ayudar a descubrir qué camino es más eficaz.
- Consulta [los análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para ver el rendimiento de cada componente en tu recorrido del usuario.
- [Edita tu Canvas]({{site.baseurl}}/post-launch_edits/) después del lanzamiento inicial.

## Programar tus Lienzos

{% alert note %}
Canvas te impedirá utilizar el envío programado con una hora que ya haya pasado. Sin embargo, es posible lanzar un Canvas durante el mismo minuto exacto en que está programada la campaña (o en los segundos anteriores). Esto puede hacer que el Canvas no llegue a la hora de entrada programada y que los usuarios no entren en el Canvas. Recomendamos enviar los Lienzos inmediatamente en caso de que se edite alguna campaña a los pocos minutos de la hora de envío programada.
{% endalert %}

Para los pasos en Canvas, ten en cuenta los siguientes detalles al programar tu Canvas:

- Los cambios de horario sólo se aplicarán a los usuarios que aún no estén esperando recibir el paso.
- Los cambios de audiencia se aplican por predeterminado a todos los usuarios, a menos que programes los cambios para que se apliquen a los usuarios que no están esperando recibir el paso.
- Si editas un Canvas que está programado para entregarse en cuanto se despliegue y seleccionas **Actualizar**, básicamente se enviará.
