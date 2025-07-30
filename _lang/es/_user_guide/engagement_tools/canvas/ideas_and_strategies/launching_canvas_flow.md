---
nav_title: Lanzamiento con Canvas Flow
article_title: Lanzamiento con Canvas Flow
page_order: 3
description: "Este artículo de referencia explica cómo preparar y probar un lienzo creado con el flujo de lienzo antes de su lanzamiento."
page_type: reference
tool: Canvas
---

# Lanzamiento con Canvas Flow

> Este artículo de referencia explica cómo preparar y probar un lienzo creado con el flujo de lienzo antes de su lanzamiento. Esto incluye la identificación de puntos de control importantes de Canvas, como las condiciones de entrada en Canvas, los resúmenes de audiencia y los segmentos de usuarios.

Mientras te preparas para lanzar tu Canvas, Braze te recomienda que compruebes tu Canvas en cada etapa del constructor de Canvas para ver si hay configuraciones que puedan afectar al envío de mensajes, incluyendo:
* [Condiciones de la carrera](#race-conditions)
* [Plazos de entrega](#delivery-times)
* [Segmentos de usuarios](#segment-users)

## Condiciones de la carrera 

Ten en cuenta las [condiciones de carrera]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) que pueden darse antes de lanzar tu Canvas. 

Para entrar en un lienzo, los usuarios deben estar en la audiencia de entrada antes de que se produzca el horario de entrada, independientemente de si el lienzo está programado, basado en acciones o activado por la API. 

![Un Canvas basado en acciones que introduce a los usuarios cuando realizan cualquier compra durante la hora local de un usuario desde el 30 de abril de 2025 a las 12 pm hasta el 7 de mayo de 2025 a las 12 pm.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Tenga en cuenta que los usuarios que reúnan los requisitos para formar parte de su público de entrada después del lanzamiento del lienzo no entrarán en el lienzo.

{% alert tip %}
Consulte [Tipos de programación de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule) para obtener orientación y detalles sobre cuándo utilizar la entrega programada, basada en acciones o activada por API para su Canvas.
{% endalert %}

### Revisar los filtros de audiencia de entrada

En general, evite configurar un Canvas basado en acciones o activado por API con el mismo desencadenante que el filtro de audiencia. Por ejemplo, tras el lanzamiento de un Canvas, los usuarios que realicen una acción específica se incluirán en el público de entrada, por lo que no es necesario añadir el evento como filtro de público. 

Para más detalles sobre los filtros de segmentación disponibles para dirigirse a su público, consulte [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

### Solicitudes API múltiples por lotes

Realice sus solicitudes en la misma llamada a la API, en lugar de varias llamadas, para confirmar que el perfil de usuario se crea o actualiza en primer lugar. Consulte la sección [Utilización de varios puntos finales]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints) para ver más ejemplos.

### Añadir un retraso

Otra opción para evitar condiciones de carrera es utilizar el paso Retraso (idealmente fijado en 5 minutos) como primer paso de tu Canvas. 

Esto da tiempo a que los atributos, las direcciones de correo electrónico y los tokens push se procesen en los nuevos perfiles de usuario antes de que se dirijan a los siguientes pasos de Canvas. Sin este paso de Retraso, es posible que se envíe un correo electrónico a un usuario cuyo correo electrónico aún no se ha actualizado.

## Plazos de entrega

Establecer una hora de entrega de Canvas en tiempo real puede aumentar la interacción y las tasas de conversión. Toma nota de la hora de entrega que has establecido para tu Canvas. Para ayudar a aumentar la tasa de interacción y conversión, es mejor desencadenar los Canvases en tiempo real en lugar de de forma programada y recurrente.

Si seleccionaste una entrega programada para tu Canvas, Braze recomienda programar tu Canvas al menos 24 horas antes de que quieras que se lance para permitir cualquier ajuste en tu Canvas.

## Segmentos de usuarios

Antes de sobresaturar su recorrido de usuario de Canvas Flow con componentes, considere cómo podría mantener un recorrido de usuario simple. Utilice la vista simplificada del editor Canvas para hacerse una mejor idea de cómo se ramifica su recorrido de usuario. 

Existen cuatro componentes principales que puede utilizar para segmentar a sus usuarios de forma sencilla y eficaz:

* [Rutas de audiencia](#audience-paths)
* [División de decisiones](#decision-split)
* [Rutas de acción](#action-paths)
* [Recorridos de experimentos](#experiment-paths)

### Rutas de audiencia

Utilice los pasos de [rutas de público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) para segmentar a los usuarios dentro del lienzo en función de atributos personalizados, eventos personalizados y datos de participación en mensajes anteriores de los perfiles de usuario.

### División de decisiones

El paso para [la división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) te permite enviar a tus usuarios a diferentes rutas de viaje de usuario en función de sus respuestas a una pregunta polar.

### Rutas de acción

[Las rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) se centran en segmentar a los usuarios en función de comportamientos en tiempo real, como eventos personalizados, eventos de compra y cambios de atributos personalizados. 

### Recorridos de experimentos

De forma similar a las Rutas de acción, puede aprovechar los pasos de [las Rutas de experimentación]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) en su lienzo para probar varias rutas del lienzo entre sí, junto con un grupo de control. De este modo se realiza un seguimiento del rendimiento de la ruta, lo que le permite tomar decisiones fundamentadas a la hora de construir su recorrido Canvas. 

## Pruebas antes del lanzamiento

Después de revisar los detalles de su lienzo, consulte [Enviar lienzos de prueba]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) para conocer los diferentes métodos que puede utilizar para probar su lienzo con usuarios de prueba.

## Solución de problemas

{% details ¿Por qué mis usuarios no reciben mis mensajes Canvas? %}
**Comprobar la disponibilidad del usuario**
- Asegúrate de que cumplen tus criterios de segmentación.
- Confirma que su estado de suscripción push es "suscrito" o "habilitado" **y** que su estado **de habilitación push** es "verdadero". Si las ha añadido como reglas de entrada en el lienzo, es posible que los usuarios se hayan dado de baja entre el momento en que entraron en el lienzo y recibieron el paso Mensaje.
- Confirma que coinciden con tu configuración de envío de Canvas. (Si los usuarios están "suscritos" pero la configuración es "Adhesión voluntaria", los usuarios no estarán habilitados para el canal).
- Si la limitación de frecuencia global está habilitada para tu Canvas, comprueba si tus reglas están limitando cuántas veces puede recibir cada usuario un mensaje de un canal específico. 
- Si se habilitan las Horas tranquilas, la hora de envío de tu mensaje podría verse afectada, lo que significa que tu mensaje podría enviarse a la siguiente hora disponible (cuando finalicen las Horas tranquilas) o cancelarse por completo.

**Comprueba la disponibilidad del usuario para filtrar más en tu paso en Canvas**
- Confirma que han realizado el evento personalizado o la compra necesarios.
- Comprueba si existe una [condición de carrera]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/), que afecta a los mensajes que reciben los usuarios si desencadenan varias acciones al mismo tiempo.
- Asegúrate de que no hay filtros específicos en el paso que podrían haber bloqueado a los usuarios la recepción del mensaje.
- Busca conflictos entre diferentes pasos dentro del mismo Canvas. Por ejemplo, los usuarios que no recibieron el mensaje podrían ser detenidos por un filtro que requiere la realización de otro paso en una rama diferente.
- Confirma que los usuarios cumplen las normas de validación adicionales.
- Confirma que el paso en Canvas estaba conectado al paso anterior en el momento del envío.
{% enddetails %}

