---
nav_title: Hacer coincidir los criterios de salida con los eventos de entrada
article_title: Hacer coincidir los criterios de salida con los eventos de entrada
page_order: 5
page_type: tutorial
description: "Aprende a configurar criterios de salida y rutas de acción que comparen propiedades del evento con las propiedades de entrada de Canvas, para que los usuarios solo salgan o se ramifiquen cuando completen la acción específica con la que entraron."
tool: Canvas
---

# Hacer coincidir los criterios de salida con los eventos de entrada

> Este artículo explica cómo configurar criterios de salida y rutas de acción que se correlacionen directamente con el evento de entrada de Canvas, de modo que los usuarios solo salgan o se ramifiquen cuando realicen una acción específica relacionada con el motivo por el que entraron al Canvas.

Al comparar las propiedades del evento con las [propiedades de entrada de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_and_event_properties/canvas_persistent_entry_properties/), puedes crear flujos altamente segmentados. Por ejemplo, en un Canvas de compra abandonada, puedes configurar que un usuario solo salga cuando compre el artículo exacto que abandonó, mientras sigue recibiendo mensajes de recordatorio si compra un artículo diferente.

Este enfoque utiliza [variables de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/) para comparar propiedades entre eventos. El patrón se aplica a muchos escenarios más allá del comercio electrónico, incluyendo renovaciones de pólizas, recordatorios de reservas y gestión de suscripciones.

## Criterios de salida: salir del Canvas cuando ocurre una acción coincidente

Usa los [criterios de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/) cuando quieras que un usuario abandone el Canvas por completo después de realizar una acción que coincida con su evento de entrada.

### Ejemplo: compra de entrada abandonada

En este escenario, un usuario entra al Canvas cuando realiza el evento personalizado `Selected Ticket`, que contiene una propiedad llamada `event_id`. Los criterios de salida se configuran de modo que cuando un usuario desencadena el evento personalizado `Purchased Ticket`—que también incluye una propiedad llamada `event_id`—la propiedad del evento de salida se compara con la propiedad del evento de entrada. Si ambas coinciden, el usuario sale del Canvas.

Esto significa:

- Si el usuario compra la misma entrada que seleccionó originalmente, sale del Canvas y deja de recibir recordatorios.
- Si el usuario compra una entrada diferente, permanece en el Canvas y sigue recibiendo mensajes de seguimiento sobre la entrada original.

Para configurar esto:

1. Configura una entrada de Canvas basada en acciones con el evento personalizado desencadenante (como `Selected Ticket`) y su propiedad relevante (como `event_id`).
2. En el paso **Audiencia objetivo**, configura el evento de excepción de los criterios de salida con el evento personalizado de finalización (como `Purchased Ticket`).
3. Selecciona **Añadir filtros de propiedades** y luego añade un filtro donde la comparación de la propiedad básica `event_id` esté configurada como `equals`.
4. Activa el alternar **Personalizar valor**, establece el **Tipo de personalización** en `Context Variables` y configura el **Atributo** como `event_id`.

Esto compara el `event_id` del evento `Purchased Ticket` con el `event_id` almacenado del evento de entrada original del Canvas. Para más detalles sobre la configuración de estos filtros, consulta [Ejemplos de criterios de salida]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#exit-criteria-examples).

## Rutas de acción: ramificación basada en una acción coincidente

Usa las [rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) cuando quieras que un usuario permanezca en el Canvas pero siga un camino diferente dependiendo de si su acción posterior coincide con el evento de entrada.

### Ejemplo: compra abandonada con rutas ramificadas

En este escenario, un usuario que seleccionó un artículo pero no completó la compra primero recibe un mensaje de compra abandonada. Luego, el usuario se mantiene en un paso de ruta de acción durante una semana antes de ser clasificado en tres caminos según lo que hizo durante ese período:

- **Completó la compra original:** el ID de la propiedad del evento personalizado es igual al ID de la propiedad de entrada. Estos usuarios podrían recibir un mensaje de agradecimiento o una recomendación de venta cruzada.
- **Realizó una compra diferente:** el ID de la propiedad del evento personalizado no es igual al ID de la propiedad de entrada. Estos usuarios podrían recibir un recordatorio sobre el artículo original.
- **No realizó ninguna compra:** pasa al grupo **El resto**. Estos usuarios podrían recibir un incentivo más fuerte o un recordatorio final.

Para configurar esto:

1. Añade un paso de [rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) y establece la ventana de evaluación (como una semana).
2. Para el primer grupo de acción (compra original), añade un desencadenante para el evento personalizado de finalización (como `Purchased_Ticket`). Selecciona **Añadir filtros de propiedades** y luego añade un filtro donde la comparación de la propiedad básica `event_id` esté configurada como `equals`. Activa **Personalizar valor**, establece el **Tipo de personalización** en `Context Variables` y configura el **Atributo** como `event_id`.
3. Para el segundo grupo de acción (compra diferente), añade el mismo evento desencadenante pero configura la comparación como `does not equal` con la misma configuración de variable de contexto.
4. Usa el grupo **El resto** para los usuarios que no realizaron el evento de finalización en absoluto.

Para más detalles sobre la configuración de estos filtros, consulta [Ejemplos de rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#action-path-examples).

## Otras aplicaciones

Aunque este artículo usa un ejemplo de compra abandonada, puedes aplicar el mismo patrón a cualquier escenario donde una acción de finalización necesite correlacionarse con la acción de entrada, incluyendo:

- **Renovaciones de pólizas:** hacer que salgan los usuarios que renuevan la póliza específica que desencadenó el Canvas.
- **Recordatorios de reservas:** ramificar a los usuarios según si confirmaron o modificaron su reserva original.
- **Gestión de suscripciones:** dirigir a los usuarios de forma diferente dependiendo de si actualizaron el plan específico sobre el que se les consultó.
- **Registros de eventos:** hacer que salgan los usuarios que completan el registro para el evento específico en el que mostraron interés.

## Cosas a tener en cuenta

- Las configuraciones de este artículo son ejemplos ilustrativos. Prueba todos los componentes en tu entorno de desarrollo antes de lanzarlos.
- Verifica que los nombres de las propiedades y los tipos de datos en tus eventos de entrada coincidan con los utilizados en tus criterios de salida o rutas de acción.
- Consulta [variables de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/) para obtener detalles sobre cómo funcionan las comparaciones de propiedades entre eventos.