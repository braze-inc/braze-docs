---
nav_title: Contexto 
article_title: Contexto 
alias: /context/
page_order: 1.5
page_type: reference
toc_headers: "h2"
description: "Este artículo de referencia explica cómo crear y utilizar pasos en Canvas."
tool: Canvas

---

# Contexto

> Los pasos contextuales te permiten crear y actualizar una o varias variables para un usuario a medida que se desplaza por un Canvas. Por ejemplo, si tienes un Canvas que gestiona descuentos de temporada, puedes utilizar una variable de contexto para almacenar un código de descuento diferente cada vez que un usuario entre en el Canvas.

{% alert important %}
Los pasos del contexto están actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.<br><br>Ten en cuenta que la adhesión voluntaria al paso en Canvas de acceso anticipado actualiza cómo se gestionan las marcas de tiempo en todos tus Canvas. Para saber más sobre esto, consulta [Normalización de la coherencia horaria](#time-zone-consistency-standardization).
{% endalert %}

## Cómo funciona

![Un paso de Contexto como primer paso de un Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Los pasos contextuales te permiten crear y utilizar datos temporales durante el recorrido de un usuario por un Canvas concreto. Estos datos sólo existen dentro de ese recorrido en Canvas y no persisten en diferentes Canvas ni fuera de la sesión.

Para obtener una referencia completa sobre las variables de contexto, incluidos los tipos de datos, el uso y las mejores prácticas, consulta la [Referencia sobre variables de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

Dentro de un paso de Contexto, puedes definir o actualizar hasta 10 variables de contexto. Estas variables pueden utilizarse para personalizar los retrasos, segmentar dinámicamente a los usuarios y enriquecer la mensajería en todo el Canvas. Por ejemplo, podrías crear una variable de contexto para la hora de vuelo programada de un usuario, y luego utilizarla para establecer retrasos personalizados y enviar recordatorios.

Puedes establecer variables de contexto de dos formas:

- **A la entrada de Canvas:** Los datos del evento o del desencadenante de la API pueden rellenar automáticamente las variables de contexto.
- **En un paso de Contexto:** Define o actualiza manualmente las variables de contexto añadiendo un paso Contexto.

Cada variable contextual requiere un nombre, un tipo de datos y un valor (establecidos mediante Liquid o la herramienta Añadir personalización). Una vez definidas, puedes hacer referencia a variables de contexto en todo el Canvas utilizando Liquid, como {% raw %}`{{context.${flight_time}}}`{% endraw %}.

Cada entrada en Canvas redefine las variables de contexto en función de los últimos datos de entrada y de la configuración de Canvas, lo que permite a los usuarios tener varios viajes activos con su propio contexto. Por ejemplo, si un cliente tiene dos vuelos próximos, tendrá dos estados de viaje distintos ejecutándose simultáneamente, cada uno con sus propias variables de contexto específicas del vuelo, como la hora de salida y el destino. Esto te permite enviar recordatorios personalizados sobre su vuelo de las 2 de la tarde a Nueva York al tiempo que envías actualizaciones diferentes sobre su vuelo de las 8 de la mañana a Los Ángeles mañana, de modo que cada mensaje siga siendo relevante para la reserva específica.

### Procesamiento y procesamiento por lotes de usuarios

Los pasos contextuales procesan a los usuarios por lotes para optimizar el rendimiento. Cuando los usuarios entran en un paso de Contexto, Braze los procesa por predeterminado en lotes de 1.000 usuarios. Estos lotes se procesan en paralelo, pero dentro de cada lote, los usuarios se procesan secuencialmente.

Es decir:
- **Procesamiento paralelo por lotes**: Se procesan varios lotes de 1.000 usuarios simultáneamente, lo que permite gestionar grandes audiencias con eficacia.
- **Procesamiento secuencial en lotes**: Dentro de cada lote, los usuarios se procesan uno tras otro. Si tu paso de Contexto incluye llamadas de [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call), la solicitud de Contenido conectado de cada usuario debe completarse antes de que se procese la del siguiente usuario de ese lote.
- **Progresión independiente por lotes**: Cada lote avanza de forma independiente. Cuando un lote termina de procesarse, esos usuarios avanzan al siguiente paso inmediatamente, aunque otros lotes sigan procesándose. Esto significa que los usuarios de diferentes lotes pueden llegar a los pasos siguientes en momentos diferentes.

**Por ejemplo**: Si 3.500 usuarios entran en un paso de Contexto con Contenido conectado, eso tarda 650 ms por usuario:
- Braze crea aproximadamente 4 lotes de usuarios (612, 802, 1.000, 880 y 120 usuarios en este ejemplo).
- Cada lote procesa a los usuarios secuencialmente, por lo que un lote de 1.000 usuarios tarda aproximadamente 11 minutos (1.000 × 650ms).
- Los lotes se completan en momentos diferentes, por lo que los usuarios pasan al siguiente paso a medida que finaliza su lote.
- Los primeros usuarios pueden llegar al siguiente paso varios minutos antes que los últimos, dependiendo del tamaño del lote y de los tiempos de respuesta del Contenido conectado.

Sin Contenido Conectado, los pasos del Contexto se procesan mucho más rápido porque no hay que esperar llamadas externas a la API.

## Consideraciones

- Puedes definir hasta 10 variables de contexto por paso de Contexto.
- Cada variable requiere un nombre único (sólo letras, números y guiones bajos, hasta 100 caracteres).
- El tamaño total de todas las variables de un paso no puede superar los 50 KB.
- Las variables que se pasan mediante desencadenadores de la API comparten el mismo espacio de nombres que las creadas en pasos de Contexto; redefinir una variable en un paso de Contexto anula el valor de la API.

Para más detalles y uso avanzado, consulta [Referencia de variables contextuales]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

## Crear un paso Contexto

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Paso 1: Añade un paso

Añade un paso a tu Canvas, luego arrastra y suelta el componente desde la barra lateral, o selecciona el botón más <i class="fas fa-plus-circle"></i> y selecciona **Contexto**.

### Paso 2: Define las variables

{% alert note %}
Puedes definir hasta 10 variables de contexto para cada paso de Contexto.
{% endalert %}

Para definir una variable de contexto:

1. Dale un **nombre** a tu variable contextual.
2. Selecciona un [tipo de datos](#context-variable-types).
3. Escribe una expresión Liquid manualmente o utiliza **Añadir personalización** para crear un fragmento de código Liquid a partir de atributos preexistentes.
4. Selecciona **Vista previa** para comprobar el valor de tu variable contextual.
5. (Opcional) Para añadir variables adicionales, selecciona **Añadir variable de contexto** y repite los pasos 1-4.
6. Cuando hayas terminado, selecciona **Hecho**.

Ahora puedes utilizar tu variable contextual en cualquier lugar donde utilices Liquid, como en los pasos de actualización de mensajes y usuarios, seleccionando **Añadir personalización**. Para un recorrido completo, consulta la [referencia Variables contextuales]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

### Filtros de variables de contexto

Puedes crear filtros utilizando variables de contexto en los pasos de [rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) y [división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split). Para la configuración del filtro, la lógica de comparación y los ejemplos avanzados, consulta la [referencia Variables contextuales]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters).

## Vista previa de las rutas de usuario

Te recomendamos que pruebes y [veas previamente tus rutas de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) para asegurarte de que tus mensajes se envían a la audiencia adecuada y de que las variables de contexto se evalúan según los resultados esperados.

{% alert note %}
Si estás previsualizando tu Canvas en la sección **Vista previa & Prueba de envío** del editor, la marca de tiempo de la vista previa del mensaje de prueba **no** se estandariza a UTC porque este panel genera vistas previas como cadenas. Esto significa que si un Canvas está configurado para aceptar un objeto `time`, la vista previa del mensaje no previsualiza con precisión lo que ocurre cuando el Canvas está en vivo. Para probar tu Canvas con mayor precisión, te recomendamos que, en su lugar, previsualices las rutas de usuario.
{% endalert %}

Asegúrate de observar las situaciones habituales que crean variables de contexto no válidas. Al previsualizar tu ruta de usuario, puedes ver los resultados de los pasos de Retraso personalizados mediante variables de contexto, y cualquier comparación de pasos de audiencia, decisión o Ruta de acción que relacione a los usuarios con cualquier variable de contexto.

Si la variable de contexto es válida, puedes hacer referencia a ella en todo tu Canvas. Sin embargo, si la variable de contexto no se creó correctamente, los pasos futuros de tu Canvas tampoco tendrán un rendimiento correcto. Por ejemplo, si creas un paso Contexto para asignar a los usuarios una hora de cita y estableces el valor de la hora de cita en una fecha pasada, el correo electrónico recordatorio de tu paso Mensaje no se envía.

## Convertir cadenas de contenido conectado a JSON

Al realizar una [llamada a Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) en un paso de Contexto, el JSON devuelto por la llamada se evalúa como un tipo de datos de cadena para mantener la coherencia y evitar errores. Si quieres convertir esta cadena en JSON, conviértela utilizando `as_json_string`. Por ejemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Normalización de la coherencia horaria

Aunque la mayoría de las propiedades del evento que utilizan el tipo de marca de tiempo ya están en UTC en Canvas, hay algunas excepciones. Con la adición del Contexto Canvas, todas las propiedades del evento predeterminadas en los Lienzos basados en acciones están en UTC. Este cambio forma parte de un esfuerzo más amplio para garantizar una experiencia más predecible y coherente al editar pasos en Canvas y mensajes. Ten en cuenta que este cambio afecta a todos los Canvas basados en acciones, tanto si el Canvas específico utiliza un paso en Canvas como si no.

{% alert important %}
En cualquier caso, recomendamos encarecidamente utilizar [filtros Liquid time_zone ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) para que las marcas de tiempo se representen en la zona horaria deseada. Puedes consultar esta [pregunta](#faq-example) frecuente como ejemplo.
{% endalert %}

## Solución de problemas

### Variables de contexto no válidas

Se considera que una variable de contexto no es válida cuando

- Falla una llamada a un Contenido conectado incrustado.
- La expresión Liquid en tiempo de ejecución devuelve un valor que no coincide con el tipo de datos o está vacío (nulo).

Por ejemplo, si el tipo de datos de la variable de contexto es **Número**, pero la expresión Liquid devuelve una cadena, no es válida.

En estas circunstancias:
- El usuario avanza al siguiente paso.
- El análisis del paso en Canvas lo cuenta como _No actualizado_.

Al solucionar problemas, controla la métrica _No actualizado_ para comprobar que tu variable de contexto se actualiza correctamente. Si la variable de contexto no es válida, tus usuarios podrán continuar en tu Canvas pasado el paso de Contexto, pero no podrán acceder a los pasos posteriores.

Consulta en [Tipos de]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) datos los ejemplos de configuración de cada tipo de datos.

### Retrasos en el envío con Contenido conectado

Cuando el Contenido conectado falla en un paso de Contexto, los usuarios que han tenido éxito avanzan inmediatamente al siguiente paso, mientras que los usuarios que han fallado vuelven a intentarlo por separado. Esto significa que un lote no espera a que todos los usuarios tengan éxito antes de avanzar: los usuarios que tienen éxito avanzan en cuanto finaliza su llamada a Contenido conectado.

**Comportamiento de reintento**: Los pasos en Contexto (y todos los pasos en Canvas) utilizan mecanismos de reintento específicos de Canvas, no el comportamiento estándar de reintento de Contenido Conectado. Si falla una llamada de contenido conectado, Braze reintenta el paso aproximadamente 13 veces con retirada exponencial. Si todos los reintentos fallan, el usuario sale del Canvas.

**Nota**: La etiqueta `:retry` utilizada en el Contenido conectado estándar no se aplica a las llamadas al Contenido conectado realizadas dentro de pasos en Canvas. Los pasos en Canvas tienen su propia lógica de reintento optimizada para los flujos de trabajo en Canvas.

**Tiempo de tramitación**: El tiempo que se tarda en procesar a todos los usuarios a través de un paso de Contexto depende de:
- El número de usuarios que entran en el paso
- Si se utiliza contenido conectado (y su tiempo de respuesta)
- El tamaño del lote (predeterminado: 1.000 usuarios por lote)

Si tu punto final de Contenido conectado tiene límites de tasa, considera que los pasos de Contexto procesan a los usuarios secuencialmente dentro de cada lote, lo que ayuda a respetar los límites de tasa de forma natural. Sin embargo, varios lotes se procesan en paralelo, así que asegúrate de que tu punto final puede gestionar solicitudes concurrentes de varios lotes.

## Preguntas más frecuentes

### ¿Qué cambia cuando Canvas Context está disponible de forma general?

Cuando el Contexto Canvas esté disponible de forma general, se aplicarán los siguientes detalles:

- Todas las marcas de tiempo con un [tipo de fecha/hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) de [las propiedades del evento desencadenante]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) en los Lienzos basados en acciones están en [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). 
- Este cambio afecta a todos los Canvas basados en acciones, tanto si el Canvas específico utiliza un paso en Canvas de Contexto como si no.

#### ¿Cuál es la razón de este cambio?

Este cambio forma parte de un esfuerzo más amplio por crear una experiencia más predecible y coherente al editar pasos en Canvas y mensajes.

#### ¿Cuándo entra en vigor este cambio?

- Si participas en el acceso anticipado al Contexto Canvas, este cambio ya se ha aplicado. 
- Si no participas en el acceso anticipado al Contexto de Canvas, este cambio se aplicará cuando te unas al acceso anticipado o cuando el Contexto de Canvas esté disponible de forma general.

#### ¿Este cambio afecta a los Lienzos programados o desencadenados por la API?

No.

#### ¿Este cambio afectará a las propiedades de entrada de Canvas?

Sí, esto afecta a `canvas_entry_properties` si se utiliza `canvas_entry_property` en un Canvas basado en acciones y el tipo de propiedad es `time`. En cualquier caso, recomendamos utilizar los filtros de Liquid `time_zone` para que las marcas de tiempo se representen en la zona horaria deseada.

Aquí tienes un ejemplo de cómo hacerlo:

| Liquid en el paso Mensaje | Salida | ¿Es ésta la forma de representar correctamente las zonas horarias en Liquid? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | No |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | No
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Sí |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### ¿Cuál es un ejemplo práctico de cómo el nuevo comportamiento de la marca de tiempo puede afectar a mis mensajes? {#faq-example}

Digamos que tenemos un Canvas basado en acciones que tiene el siguiente contenido en un paso en Canvas Mensaje:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

El resultado es el siguiente mensaje: 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Como no se especifica ninguna zona horaria utilizando Liquid, la marca de tiempo aquí está en UTC. 

Para especificar claramente una zona horaria, podemos utilizar filtros Liquid `time_zone` como éste: 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

El resultado es el siguiente mensaje: 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Como la zona horaria de América/Los Ángeles se especifica con Liquid, la marca horaria aquí está en PST.

La zona horaria preferida también puede enviarse en la carga útil de propiedades del evento y utilizarse en la lógica Liquid:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### ¿En qué se diferencian las variables de contexto de las propiedades de entrada en Canvas?

Si participas en el acceso anticipado al paso en Canvas, las propiedades de entrada al Canvas se incluyen ahora como variables de contexto del Canvas. Esto significa que puedes enviar propiedades de entrada Canvas utilizando la API Braze y hacer referencia a ellas en otros pasos, de forma similar al uso de una variable de contexto con el fragmento de código Liquid.

### ¿Pueden las variables referenciarse entre sí en un paso Contexto singular?

Sí. Todas las variables de un paso Contexto se evalúan en una secuencia, lo que significa que podrías tener configuradas las siguientes variables de contexto:

| Variable de contexto | Valor | Descripción |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | El tipo de cocina favorito de un usuario. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | El código de descuento disponible para un usuario. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.promo_code}} "on delivery from your favorite" {{context.favorite_cuisine}} restaurants!"`{% endraw %} | Un mensaje personalizado que combina las variables anteriores. En un paso de mensajería, podrías utilizar el fragmento de código Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} para hacer referencia a la variable de contexto y entregar un mensaje personalizado a cada usuario. También podrías utilizar un paso en Canvas para guardar el valor del [código promocional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) y utilizarlo como plantilla en otros pasos a lo largo de un Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Esto también se aplica a varios pasos del Contexto. Por ejemplo, imagina esta secuencia:
1. Un paso inicial de Contexto crea una variable llamada `JobInfo` con el valor `job_title`.
2. Un paso de Mensaje hace referencia a {% raw %}`{{context.${JobInfo}}}`{% endraw %} y muestra `job_title` al usuario.
3. Más tarde, un paso de Contexto actualiza la variable de contexto, cambiando el valor de `JobInfo` a `job_description`.
4. Todos los pasos posteriores que hagan referencia a `JobInfo` utilizan ahora el valor actualizado `job_description`.

Las variables de contexto utilizan su valor más reciente en todo el Canvas, y cada actualización afecta a todos los pasos siguientes que hagan referencia a esa variable.
