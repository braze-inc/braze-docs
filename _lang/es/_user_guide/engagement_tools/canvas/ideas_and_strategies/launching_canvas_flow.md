---
nav_title: Lanzamiento con el flujo Canvas
article_title: Lanzamiento con Canvas Flow
page_order: 3
description: "Este artículo de referencia explica cómo preparar y probar un Canvas creado con el Flujo de Canvas antes de lanzarlo."
page_type: reference
tool: Canvas
---

# Lanzamiento con Canvas Flow

> Este artículo de referencia explica cómo preparar y probar un Canvas creado con el Flujo de Canvas antes de lanzarlo. Esto incluye identificar los puntos de control importantes de Canvas, como las condiciones de entrada en Canvas, los resúmenes de audiencia y los segmentos de usuarios.

Mientras te preparas para lanzar tu Canvas, Braze te recomienda que compruebes tu Canvas en cada etapa del constructor de Canvas para ver si hay configuraciones que puedan afectar al envío de mensajes, incluyendo:
* [Condiciones de carrera](#race-conditions)
* [Plazos de entrega](#delivery-times)
* [Segmentos de usuarios](#segment-users)

## Condiciones de carrera 

Ten en cuenta las [condiciones de carrera]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) que pueden darse antes de lanzar tu Canvas. 

Para entrar en un Canvas, los usuarios deben estar en la audiencia de entrada antes de que se produzca la programación de entrada, independientemente de si el Canvas está programado, basado en acciones o desencadenado por la API. 

\![Un Canvas basado en acciones que introduce a los usuarios cuando realizan cualquier compra durante la hora local de un usuario desde el 30 de abril de 2025 a las 12 pm hasta el 7 de mayo de 2025 a las 12 pm.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Ten en cuenta que los usuarios que cumplan los requisitos para formar parte de tu audiencia de entrada después del lanzamiento del Canvas no entrarán en el Canvas.

{% alert tip %}
Consulta [Tipos de programación de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule) para obtener orientación y detalles sobre cuándo utilizar la entrega programada, basada en acciones o desencadenada por API para tu Canvas.
{% endalert %}

### Revisar filtros de audiencia de entrada

En general, evita configurar un Canvas basado en acciones o activado por la API con el mismo desencadenante que el filtro de audiencia. Por ejemplo, tras el lanzamiento de un Canvas, los usuarios que realicen una acción concreta se incluirán en la audiencia de entrada, por lo que no es necesario añadir el evento como filtro de audiencia. 

Para más detalles sobre los filtros de segmentación disponibles para dirigirte a tu audiencia, consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

### Peticiones API múltiples por lotes

Haz tus peticiones en la misma llamada a la API, en lugar de varias llamadas, para confirmar que el perfil de usuario se crea o actualiza primero. Consulta [Utilizar varios puntos finales]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints) para ver más ejemplos.

### Añade un retraso

Otra opción para evitar condiciones de carrera es utilizar el paso Retraso (idealmente fijado en 5 minutos) como primer paso de tu Canvas. 

Esto da tiempo a que los atributos, las direcciones de correo electrónico y los tokens de notificaciones push se procesen en los nuevos perfiles de usuario antes de que se dirijan a ellos en los siguientes pasos en Canvas. Sin este paso de Retraso, es posible que se envíe un correo electrónico a un usuario cuyo correo electrónico aún no se ha actualizado.

## Plazos de entrega

Establecer una hora de entrega de Canvas en tiempo real puede aumentar las tasas de interacción y conversión. Toma nota de la hora de entrega que has configurado para tu Canvas. Para ayudar a aumentar la tasa de interacción y conversión, es mejor desencadenar los Canvases en tiempo real en lugar de de forma programada y recurrente.

Si seleccionaste una entrega programada para tu Canvas, Braze recomienda programar tu Canvas al menos 24 horas antes de que quieras que se lance para permitir cualquier ajuste en tu Canvas.

## Segmentos de usuarios

Antes de sobresaturar de componentes tu recorrido de usuario del Flujo del Canvas, piensa en cómo podrías mantener un recorrido de usuario sencillo. Utiliza la vista simplificada del editor Canvas para hacerte una mejor idea de cómo se ramifica tu recorrido de usuario. 

Hay cuatro componentes principales que puedes utilizar para segmentar a tus usuarios de forma sencilla y eficaz:

* [Rutas de audiencia](#audience-paths)
* [División de decisiones](#decision-split)
* [Rutas de acción](#action-paths)
* [Rutas de experimentos](#experiment-paths)

### Rutas de audiencia

Utiliza los pasos en Canvas [de las rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) para segmentar a los usuarios en función de atributos personalizados, eventos personalizados y datos de interacción con los mensajes anteriores de los perfiles de usuario.

### División de decisiones

El paso para [la división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) te permite enviar a tus usuarios a diferentes rutas de viaje de usuario en función de sus respuestas a una pregunta polar.

### Rutas de acción

[Las rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) se centran en segmentar a los usuarios basándose en comportamientos en tiempo real, como eventos personalizados, eventos de compra y cambios de atributos personalizados. 

### Rutas de experimentos

De forma similar a las rutas de acción, puedes aprovechar los pasos [de rutas de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) en tu Canvas para probar varias rutas de Canvas entre sí, junto con un grupo de control. Esto realiza un seguimiento del rendimiento de la ruta, permitiéndote tomar decisiones informadas cuando construyas tu recorrido en Canvas. 

## Pruebas antes del lanzamiento

Después de revisar los detalles de tu Canvas, consulta [Enviar lienzos de prueba]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) para conocer los distintos métodos que puedes aprovechar para probar tu Canvas con usuarios de prueba.

## Lista de control de lanzamiento

### Comprobar la disponibilidad del usuario

- Asegúrate de que tus usuarios cumplen tus criterios de segmentación.
- Confirma que su estado de suscripción es "suscrito" o "adhesión voluntaria" y que existe su token de notificaciones push. Si las añadiste como reglas de entrada a Canvas, es posible que los usuarios se dieran de baja entre la entrada a tu Canvas y la recepción del paso en Mensajería.
- Confirma que coinciden con tu configuración de envío de Canvas. (Si los usuarios están "suscritos" pero la configuración es "Adhesión voluntaria", los usuarios no estarán habilitados para el canal).
- Si la limitación de frecuencia global está habilitada para tu Canvas, comprueba si tus reglas están limitando cuántas veces puede recibir cada usuario un mensaje de un canal específico.
- Si se habilitan las Horas tranquilas, la hora de envío de tu mensaje podría verse afectada, lo que significa que tu mensaje podría enviarse a la siguiente hora disponible (cuando finalicen las Horas tranquilas) o cancelarse por completo.
- Comprueba la disponibilidad del usuario para filtrar más en tu paso en Canvas.

### Confirma que han realizado el evento personalizado o la compra necesarios

- Comprueba si existe una condición de carrera, que afecta a los mensajes que reciben los usuarios si desencadenan varias acciones al mismo tiempo.
- Asegúrate de que no hay filtros específicos en el paso que podrían haber bloqueado a los usuarios la recepción del mensaje.
- Busca conflictos entre diferentes pasos dentro del mismo Canvas. Por ejemplo, los usuarios que no recibieron el mensaje podrían ser detenidos por un filtro que requiere la realización de otro paso en una rama diferente.
- Confirma que los usuarios cumplen las normas de validación adicionales.
- Confirma que el paso en Canvas estaba conectado al paso anterior en el momento del envío.

### Confirma que tu Canvas se guarda correctamente y que todos los pasos son válidos

Si tu Canvas no se carga y no avanza, puede deberse a que una versión anterior del Canvas no se guardó correctamente y contiene pasos no válidos. Puedes duplicar el Canvas desde el panel. Si el problema persiste, abre un [ticket de soporte]({{site.baseurl}}/braze_support/).

## Solución de problemas

{% details Why are my users not receiving my Canvas messages? %}
**Comprobar la disponibilidad del usuario**
- Asegúrate de que cumplen tus criterios de segmentación.
- Confirma que su estado de suscripción push es "suscrito" o "habilitado" **y** que su estado **de habilitación push** es "verdadero". Si las añadiste como reglas de entrada a Canvas, es posible que los usuarios se dieran de baja entre la entrada a tu Canvas y la recepción del paso en Mensajería.
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

