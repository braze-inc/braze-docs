---
nav_title: Adopción de características
article_title: Adopción de características
page_order: 3
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de Canvas de Braze para entregar mensajes personalizados a tiempo y destacar las ventajas y consejos de uso."
tool: Canvas
---

# Adopción de características

> Esta plantilla está diseñada para impulsar el uso de tus nuevas características, productos existentes, ofertas adicionales o cualquier otra área que te gustaría que experimentaran tus clientes. Aprovechando la comunicación personalizada y un conjunto estructurado de mensajes, puedes presentar fácilmente nuevas características a los usuarios y obtener valiosos comentarios de ellos. 

En este artículo, te guiaremos a través de un caso de uso de la plantilla **Adopción de características**, que está pensada para las etapas de retención y fidelización del ciclo de vida del usuario. Después de este artículo, habrás personalizado un recorrido del usuario que anima a los usuarios a utilizar nuevas características y recoge el sentimiento de los usuarios.

## Requisitos previos

Para utilizar correctamente esta plantilla, necesitarás un [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) que haga referencia a cuándo los usuarios han utilizado la característica.

## Adaptar la plantilla a tus necesidades

Supongamos que trabajas en Calorie Rocket, una aplicación de entrega de comida, que acaba de lanzar Cruise Control, una característica para programar entregas de comida recurrentes, y quieres animar a más usuarios a adoptar esta nueva característica. En nuestro ejemplo, utilizaremos el evento personalizado `scheduled_delivery` para hacer un seguimiento de cuándo los usuarios han probado la característica Control de crucero.

Para acceder a la plantilla de reserva, al crear un nuevo Canvas, selecciona **Utilizar una plantilla de Canvas** > **Plantillas de Braze**. Luego, junto a **Adopción de características**, selecciona **Aplicar plantilla**. Ahora, podemos repasar la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configura los detalles

Vamos a ajustar los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Editar** junto al nombre de la plantilla.

\![El título actual y la descripción del Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Actualiza el nombre del Canvas para especificar que el Canvas está destinado a los usuarios para recoger sus opiniones.
3\. Actualiza la descripción para especificar que el Canvas sirve para animar a los usuarios a enviar comentarios y hacer un seguimiento de la opinión de los usuarios sobre la nueva característica Control de crucero.
4\. Añade la etiqueta **Adopción de características** para que podamos filtrarla en la página de inicio de Canvas.

\![El nuevo nombre y descripción del Canvas. La nueva descripción dice Un Canvas de adopción de características para el seguimiento de la adopción y el sentimiento de los usuarios de Cruise Control, una característica para programar entregas recurrentes de comida".]({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### Paso 2: Asignar un evento de conversión

A continuación, vamos a añadir un evento de conversión a nuestro Canvas para señalar la adopción de la característica. Esto nos permitirá adaptar más adelante la ruta de experimentos en nuestro recorrido del usuario.

1. En **Asignar eventos de conversión**, selecciona **Añadir evento de conversión**.
2. En **Evento de conversión primaria - A**, selecciona **Realiza evento personalizado** como **tipo de evento de conversión**.
3. Selecciona nuestro evento personalizado `scheduled_delivery`.
4. Mantendremos el plazo de conversión en tres días.

La ventana del evento de conversión en el Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %}){: style="max-width:90%;"}

### Paso 3: Adapta el horario de entrada

Nuestro objetivo es animar a nuestros usuarios a adoptar el Control de Crucero, pero no queremos que nuestra mensajería sea demasiado frecuente. Por tanto, mantendremos este Canvas como una entrega programada y haremos los siguientes ajustes en la sección **Opciones basadas en el tiempo**.

1. Actualiza la **frecuencia de entrada** a **semanal**.
2. Mantén la recurrencia como está.
3. Selecciona **Lun** para dirigirte a los usuarios al principio de la semana.
4. Selecciona la hora de inicio de nuestro Canvas.
5. Actualiza los **parámetros de Finalización** para finalizar el Canvas el último día del año.

Mantendremos la opción de permitir a los usuarios introducir el Canvas en su zona horaria local.

### Paso 4: Selecciona la audiencia objetivo

Ahora, vamos a configurar nuestra audiencia objetivo actualizando los siguientes datos en la plantilla:

1. Selecciona el segmento **Todos los usuarios**.
2. Elimina los filtros adicionales de la plantilla. 
3. Crea este filtro utilizando nuestro evento personalizado: `Has scheduled_delivery for exactly 0 times`. Esto nos permite excluir a los usuarios que ya han utilizado la característica de entrar en nuestro Canvas.

\![El segmento para todos los usuarios que no han utilizado el Control de Crucero.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %}){: style="max-width:90%;"}

{: start="4"}
4\. Teniendo en cuenta que Calorie Rocket permitió anteriormente a algunos usuarios probar la nueva característica Control de Crucero, actualizaremos los criterios de salida para excluir a estos usuarios de entrar en el Canvas.

### Paso 5: Selecciona tu configuración de envío

Mantendremos la configuración predeterminada de la suscripción, de modo que sólo enviemos a los usuarios que se hayan suscrito o hayan optado por recibir mensajes o notificaciones, y omitiremos las demás configuraciones (limitación de frecuencia, horas tranquilas y grupos de semilla).

### Paso 6: Personaliza tu Canvas

#### Construye la ruta de acción

A continuación, vamos a construir el primer paso de la ruta de acción, que tiene por objeto indicar si nuestros usuarios están interesados en la nueva característica. Haremos los siguientes ajustes en la plantilla:

1. Como la característica Control de crucero sólo está disponible después de que se haya añadido un pedido al carrito, daremos al primer grupo de acción el nombre de **Añadido al carrito** y seleccionaremos `added_to_cart` para el evento personalizado.

\![El nombre del grupo de acciones establecido en "Añadido a la cesta" y la opción "Realizar evento personalizado" establecida en "added_to_cart".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2\. Mantén el segundo grupo de acción **Recorrido realizado** tal cual, ya que queremos evaluar si los usuarios han hecho un recorrido por la aplicación y, si lo han hecho, entonces avanzarán a la segunda ruta.
3\. En la ruta de acción siguiente denominada **Evaluar uso**, sustituye **Característica usada >3x** por **Configuración del control de crucero vista**.
4\. Selecciona el menú desplegable **Realizar evento personalizado** y, a continuación, selecciona `scheduled_delivery` para el evento personalizado.

\![El nombre del grupo de acción establecido en "Característica utilizada >3x" y "Realizar evento personalizado" establecido en 'scheduled_delivery'.]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### Configurar cuestionario de opinión

A continuación, iremos al paso Mensaje llamado **Encuesta de opinión** para incluir nuestro cuestionario de opinión para que nuestros usuarios lo rellenen después de utilizar el Control de Crucero por primera vez. Nuestras opciones de respuesta a los cuestionarios para nuestros usuarios son:

- **¡Me ha encantado!**
- **No para mí.**

1. Para las dos opciones del cuestionario, selecciona **Comentarios sobre la experiencia** como nuestro atributo personalizado para capturar y hacer un seguimiento de los comentarios sobre el Control de Crucero. Este atributo personalizado tendrá dos valores para representar las respuestas del cuestionario (`good` y `bad`).
2. Actualiza los valores de los atributos para que coincidan con las opciones del cuestionario. Esto nos permitirá hacer un seguimiento de la respuesta de un usuario.

### Paso 7: Prueba y lanza tu Canvas

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como esperábamos, selecciona **Lanzar Canvas** para iniciar el Canvas. Ahora podemos dirigirnos a los usuarios con un viaje de usuario personalizado para animarles a adoptar nuestra nueva característica Control de crucero.

{% alert tip %}
Consulta nuestra [Lista de comprobación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber qué cosas debes tener en cuenta antes y después de lanzar un Canvas.
{% endalert %}
