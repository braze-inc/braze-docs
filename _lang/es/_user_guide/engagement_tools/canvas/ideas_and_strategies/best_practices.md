---
nav_title: Buenas prácticas
article_title: Mejores prácticas de Canvas
page_order: 1
description: "Este artículo proporciona algunas de las mejores prácticas para crear y personalizar los recorridos del usuario con Canvas y Canvas Flow."
tool: Canvas

---

# Mejores prácticas de Canvas

> Este artículo proporciona algunas de las mejores prácticas para crear y personalizar los recorridos del usuario con Canvas y Canvas Flow.

## Identifica tu objetivo

¡Sumérgete en el qué, el quién y el por qué!
- ¿Qué intentas ayudar a conseguir a los usuarios?
- ¿Quiénes son los usuarios a los que quieres llegar?
- ¿Por qué construyes este lienzo?

## Mezcla y combina

Desbloquee nuevas combinaciones de recorridos de usuario con [componentes Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/).
- Divide a tus usuarios con la [División de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) y crea flujos de trabajo diferentes.
- Espacia tus recorridos de usuario con un paso de [Retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/).
- Añade [mensajes independientes]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) donde quieras en tu flujo Canvas. 

## Crea mensajes más enriquecidos

Atrae a tus usuarios con mensajes más enriquecidos.

- Cree [mensajes en la aplicación]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/) para los lienzos de incorporación para sacar el máximo partido a su primera impresión.
- Introduce [tarjetas de contenido]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/content-cards_in_canvas/) en un recorrido de Canvas para ofertas promocionales y notificaciones push.

## Prueba tus recorridos de usuario

Determine el impacto de su mensaje Canvas incorporando grupos de control. De este modo, podrá hacerse una idea de la acogida que ha tenido su lienzo.

- Nombra cada paso de tu Canvas para identificar tu recorrido de usuario.
- Aproveche el componente [Rutas de experimentación]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) en su recorrido de usuario para asignar aleatoriamente a los usuarios a las diferentes rutas que cree. 
- Diversifica tus recorridos de usuario con pasos de Retraso y Mensaje para ayudar a descubrir qué camino es más eficaz.
- Compruebe [los análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/) para ver el rendimiento de cada componente en el recorrido del usuario.
- [Edita tu Canvas]({{site.baseurl}}/post-launch_edits/) después del lanzamiento inicial.

## Programar tus Lienzos

{% alert note %}
Canvas te impedirá utilizar el envío programado con una hora que ya haya pasado. Sin embargo, es posible lanzar un Canvas durante el mismo minuto exacto en que está programada la campaña (o en los segundos anteriores). Esto puede hacer que el Canvas no llegue a la hora de entrada programada y que los usuarios no entren en el Canvas. Recomendamos enviar los lienzos inmediatamente en caso de que se edite alguna campaña a los pocos minutos de la hora de envío programada.
{% endalert %}

Para los pasos en Canvas, ten en cuenta los siguientes detalles al programar tu Canvas:

- Los cambios de horario sólo se aplicarán a los usuarios que aún no estén esperando recibir el paso.
- Los cambios de audiencia se aplican por predeterminado a todos los usuarios, a menos que programes los cambios para que se apliquen a los usuarios que no están esperando recibir el paso.
- Si editas un Canvas que está programado para entregarse en cuanto se despliegue y seleccionas **Actualizar**, básicamente se enviará.
