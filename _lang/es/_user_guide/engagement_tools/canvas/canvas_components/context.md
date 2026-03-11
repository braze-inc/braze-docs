---
nav_title: Contexto 
article_title: Contexto 
alias: /context/
page_order: 6
page_type: reference
toc_headers: "h2"
description: "Este artículo de referencia explica cómo crear y utilizar pasos de contexto en tu Canvas."
tool: Canvas

---

# Contexto

> Los pasos de contexto te permiten crear y actualizar una o más variables para un usuario a medida que avanza por un Canvas. Por ejemplo, si tienes un Canvas que administra descuentos de temporada, puedes utilizar una variable de contexto para almacenar un código de descuento diferente cada vez que un usuario entra en el Canvas.

## Cómo funciona

![Un paso de contexto como primer paso de un Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Los pasos de contexto te permiten crear y utilizar datos temporales durante el recorrido de un usuario por un lienzo específico. Estos datos solo existen dentro de ese recorrido de Canvas y no se conservan en otros Canvases ni fuera de la sesión.

Las variables de contexto solo existen para ese recorrido específico de Canvas. No cambian el perfil de usuario de forma permanente y no aparecen en otros lienzos. Esto los hace ideales para información temporal que solo es relevante para una campaña o un flujo de trabajo específicos.

{% alert tip %}
Para obtener información completa sobre las variables de contexto, incluidos los tipos de datos, el uso y las prácticas recomendadas, consulta la [referencia de variables de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).
{% endalert %}

En un paso de contexto, puedes definir o actualizar hasta 10 variables de contexto. Estas variables se pueden utilizar para personalizar los retrasos, realizar la segmentación de los usuarios de forma dinámica y enriquecer la mensajería en todo el Canvas. Por ejemplo, puedes crear una variable de contexto para la hora de vuelo programada de un usuario y, a continuación, utilizarla para establecer retrasos personalizados y enviar recordatorios.

Puedes establecer variables de contexto de dos maneras:

- **A la entrada de Canvas:** Los datos del evento o del activador de la API pueden rellenar automáticamente las variables de contexto.
- **En un paso de contexto:** Define o actualiza las variables de contexto manualmente añadiendo un paso de contexto.

Cada variable de contexto requiere un nombre, un tipo de datos y un valor (establecido mediante Liquid o la herramienta Añadir personalización). Una vez definidas, puedes hacer referencia a las variables de contexto en todo Canvas utilizando Liquid, como por ejemplo {% raw %}`{{context.${flight_time}}}`{% endraw %}.

Cada entrada de Canvas redefine las variables de contexto en función de los últimos datos introducidos y la configuración de Canvas, lo que permite a los usuarios tener múltiples recorridos activos con su propio contexto. Por ejemplo, si un cliente tiene dos vuelos próximos, tendrás dos estados de viaje independientes que se ejecutarán simultáneamente, cada uno con sus propias variables de contexto específicas del vuelo, como la hora de salida y el destino. Esto te permite enviar recordatorios personalizados sobre tu vuelo de las 2 de la tarde a Nueva York, al tiempo que envías diferentes actualizaciones sobre tu vuelo de las 8 de la mañana a Los Ángeles mañana, de modo que cada mensaje sea relevante para la reserva específica.

### Procesamiento y agrupación de usuarios

El contexto procesa a los usuarios por lotes para optimizar el rendimiento. Cuando los usuarios entran en un paso de contexto, Braze los procesa de forma predeterminada en lotes de 1000 usuarios. Estos lotes se procesan en paralelo, pero dentro de cada lote, los usuarios se procesan secuencialmente.

Esto significa:

**Por ejemplo**: Si 3500 usuarios entran en un paso de contexto con contenido conectado que tarda 650 ms por usuario:
- Braze crea cuatro lotes de usuarios (1000, 1000, 1000 y 500 usuarios en este ejemplo).
- Cada lote procesa a los usuarios de forma secuencial, por lo que un lote de 1000 usuarios tarda aproximadamente 10,8 minutos (650 segundos; 1000 × 650 ms).
- Los lotes se completan en diferentes momentos, por lo que los usuarios pasan al siguiente paso a medida que se completa su lote.
- Los primeros usuarios pueden llegar al siguiente paso varios minutos antes que los últimos, dependiendo del tamaño del lote y de los tiempos de respuesta del contenido conectado.

Sin contenido conectado, los pasos de contexto se procesan mucho más rápido porque no hay que esperar llamadas API externas.

## Consideraciones

- Puedes definir hasta 10 variables de contexto por cada paso de contexto.
- Cada variable requiere un nombre único (solo letras, números y guiones bajos, hasta 100 caracteres).
- El tamaño total de todas las variables de un paso no puede superar los 50 KB.
- Las variables pasadas mediante desencadenadores de API comparten el mismo espacio de nombres que las creadas en los pasos de contexto; al redefinir una variable en un paso de contexto, se anula el valor de la API.

Para obtener más detalles y conocer el uso avanzado, consulta [la referencia de variables de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

## Crear un paso Contexto

{% multi_lang_include alerts/tip_alerts.md alert='Reference properties from triggering event' %}

### Paso 1: Añadir un paso

Añade un paso a tu Canvas, luego arrastra y solta el componente desde la barra lateral, o selecciona el botón<i class="fas fa-plus-circle"></i> más y selecciona **Contexto**.

### Paso 2: Define las variables.

{% alert note %}
Puedes definir hasta 10 variables de contexto para cada paso de contexto.
{% endalert %}

Para definir una variable de contexto:

1. Asigna un **nombre** a tu variable de contexto.
2. Selecciona un [tipo de datos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types).
3. Escribe una expresión Liquid manualmente o utiliza **Añadir personalización** para crear un fragmento de código Liquid a partir de atributos preexistentes.
4. Selecciona **Vista previa** para comprobar el valor de tu variable de contexto.
5. (Opcional) Para añadir variables adicionales, selecciona **Añadir variable de contexto** y repite los pasos 1 a 4.
6. Cuando hayas terminado, selecciona **Hecho**.

Ahora puedes utilizar tu variable de contexto en cualquier lugar donde utilices Liquid, como en los pasos Mensaje y Actualización de usuario, seleccionando **Añadir personalización**. Para obtener una guía completa, consulta [Referencia de variables de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/).

{% alert important %}
Cuando hagas referencia a variables de contexto, utiliza siempre el formato {% raw %}`{{context.${variable_name}}}`{% endraw %}.
{% endalert %}

### Filtrar variables de contexto

Puedes crear filtros utilizando variables de contexto en los pasos [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) (rutas de audiencia) y [paso para la división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split). Para la configuración del filtro, la lógica de comparación y ejemplos avanzados, consulta [la referencia de variables de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters).

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

## Vista previa de las rutas de los usuarios

Recomendamos probar y [realizar una vista previa de las rutas de los usuarios]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) para asegurarte de que tus mensajes se envían a la audiencia adecuada y que las variables de contexto se evalúan según los resultados esperados.

{% alert note %}
Si estás previsualizando tu Canvas en la sección **Vista previa  &Envío de prueba** del editor, la marca de tiempo en la vista previa del mensaje de prueba **no se** estandariza a UTC porque este panel genera vistas previas como cadenas. Esto significa que si un Canvas está configurado para aceptar un`time`objeto, la vista previa del mensaje no muestra con precisión lo que ocurre cuando el Canvas está en vivo. Para probar tu Canvas con mayor precisión, te recomendamos que realices una vista previa de las rutas de los usuarios.
{% endalert %}

Asegúrate de observar cualquier situación habitual que genere variables de contexto no válidas. Al realizar la vista previa de la ruta del usuario, puedes ver los resultados de los pasos de retraso de personalización utilizando variables de contexto, así como cualquier comparación de audiencias o pasos de decisión que relacionen a los usuarios con cualquier variable de contexto.

Si la variable de contexto es válida, puedes hacer referencia a ella en todo tu Canvas. Sin embargo, si la variable de contexto no se ha creado correctamente, los pasos posteriores de tu Canvas tampoco tendrán un rendimiento adecuado. Por ejemplo, si creas un paso de contexto para asignar a los usuarios una hora de cita y estableces el valor de la hora de la cita en una fecha pasada, el correo electrónico de recordatorio del paso de mensaje no se enviará.

## Conversión de cadenas de contenido conectado a JSON

Al realizar una [llamada de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) en un paso de contexto, el JSON devuelto por la llamada se evalúa como un tipo de datos de cadena para garantizar la coherencia y evitar errores. Si deseas convertir esta cadena a JSON, hazlo utilizando `as_json_string`. Por ejemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Solución de problemas

### Variables de contexto no válidas

Una variable de contexto se considera inválida cuando:

- Falla una llamada a un contenido conectado integrado.
- La expresión Liquid en tiempo de ejecución devuelve un valor que no coincide con el tipo de datos o está vacío (nulo).

Por ejemplo, si el tipo de datos de la variable de contexto es **Número,** pero la expresión Liquid devuelve una cadena, no es válida.

En estas circunstancias:
- El usuario avanza al siguiente paso.
- El análisis de pasos en Canvas cuenta esto como _«No actualizado_».

Al realizar la solución de problemas, supervisa la métrica _«No actualizado»_ para comprobar que tu variable de contexto se actualiza correctamente. Si la variable de contexto no es válida, tus usuarios podrán continuar en Canvas más allá del paso de contexto, pero es posible que no cumplan los requisitos para los pasos posteriores.

Consulta [Tipos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) de [datos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#data-types) para ver ejemplos de configuración para cada tipo de datos.

### Retrasos en el envío con contenido conectado

Todos los usuarios de un lote se procesan antes de que ningún usuario avance. Una vez completado el procesamiento por lotes, los usuarios que han superado la prueba pasan al siguiente paso, mientras que los que han fallado se vuelven a intentar por separado; los usuarios que han superado la prueba no esperan a que los reintentos tengan éxito antes de avanzar.

**Comportamiento de reintento**: Los pasos de contexto (y todos los pasos en Canvas) utilizan mecanismos de reintento específicos de Canvas, no el comportamiento de reintento estándar del contenido conectado. Si falla una llamada de contenido conectado, Braze vuelve a intentar el paso aproximadamente 13 veces con retirada exponencial. Si todos los reintentos fallan, el usuario sale del Canvas.

{% alert note %}
La`:retry`etiqueta utilizada en el contenido conectado estándar no se aplica a las llamadas de contenido conectado realizadas dentro de los pasos en Canvas. Los pasos en Canvas tienen su propia lógica de reintento optimizada para los flujos de trabajo de Canvas.
{% endalert %}

**Tiempo de procesamiento**: El tiempo que se tarda en procesar a todos los usuarios a través de un paso de contexto depende de:
- El número de usuarios que entran en el paso
- Si se utiliza contenido conectado (y su tiempo de respuesta)
- El tamaño del lote (predeterminado, 1000 usuarios por lote)

Si tu punto final de contenido conectado tiene límites de velocidad, ten en cuenta que los pasos de contexto procesan a los usuarios de forma secuencial dentro de cada lote, lo que ayuda a respetar los límites de velocidad de forma natural. Sin embargo, varios lotes se procesan en paralelo, por lo que debes asegurarte de que tu punto final pueda gestionar solicitudes simultáneas de varios lotes.

## Estandarización de la coherencia de las zonas horarias

Aunque la mayoría de las propiedades del evento que utilizan el tipo de marca de tiempo ya están en UTC en Canvas, hay algunas excepciones. Con la incorporación de Canvas Context, todas las propiedades predeterminadas del evento de marca de tiempo en los lienzos basados en acciones están en UTC. Este cambio forma parte de un esfuerzo más amplio por garantizar una experiencia más predecible y coherente al editar los pasos y mensajes en Canvas. Ten en cuenta que este cambio afecta a todos los Canvas basados en acciones, independientemente de si el Canvas específico utiliza un paso de contexto o no.

{% alert important %}
En cualquier caso, recomendamos encarecidamente utilizar [filtros time_zoneLiquid]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know)  para que las marcas de tiempo se representen en la zona horaria deseada. Puedes consultar esta [pregunta frecuente](#faq-example) para ver un ejemplo.
{% endalert %}

## Preguntas más frecuentes

### ¿Qué ha cambiado desde que Canvas Context pasó a estar disponible de forma generalizada?

Ahora que Canvas Context está disponible de forma generalizada, se aplican los siguientes detalles:

- Todas las marcas de tiempo con un [tipo de fecha y hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) de [las propiedades del evento]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) en los lienzos basados en acciones están en [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time).
- Este cambio afecta a todos los Canvas basados en acciones, independientemente de si el Canvas específico utiliza un paso de contexto o no.

#### ¿Cuál es el motivo de este cambio?

Este cambio forma parte de un esfuerzo más amplio por crear una experiencia más predecible y coherente al editar los pasos en Canvas y los mensajes.

#### ¿Este cambio afecta a los lienzos que se desencadenan mediante API o a los programados?

No.

#### ¿Este cambio afecta a las propiedades de entrada de Canvas?

Sí, esto afecta`canvas_entry_properties`si se`canvas_entry_property`utiliza en un Canvas basado en acciones y el tipo de propiedad es `time`. En cualquier caso, recomendamos utilizar filtros `time_zone`Liquid  para que las marcas de tiempo se representen en la zona horaria deseada.

Aquí tienes un ejemplo de cómo hacerlo:

| Líquido en el paso Mensaje | Salida | ¿Es esta la forma correcta de representar las zonas horarias en Liquid? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | No |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | No
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | Sí |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### ¿Cuál es un ejemplo práctico de cómo el nuevo comportamiento de la marca de tiempo podría afectar a tus mensajes? {#faq-example}

Supongamos que tenemos un Canvas basado en acciones que tiene el siguiente contenido en un paso de mensaje:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Esto da como resultado el siguiente mensaje: 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Dado que no se especifica ninguna zona horaria con Liquid, la marca de tiempo aquí está en UTC. 

Para especificar claramente una zona horaria, podemos utilizar filtros `time_zone`Liquid como este: 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Esto da como resultado el siguiente mensaje: 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

Dado que la zona horaria América/Los Ángeles se especifica mediante Liquid, la marca de tiempo aquí está en PST.

La zona horaria preferida también se puede enviar en la carga útil de las propiedades del evento y utilizarse en la lógica Liquid:

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### ¿En qué se diferencian las variables de contexto de las propiedades de entrada de Canvas?

Las propiedades de entrada de Canvas se incluyen como variables de contexto de Canvas. Esto significa que puedes enviar propiedades de entrada de Canvas utilizando la API de Braze y hacer referencia a ellas en otros pasos, de forma similar al uso de una variable de contexto con el fragmento de código Liquid.

### ¿Pueden las variables referenciarse entre sí en un paso de contexto Singular?

Sí. Todas las variables de un paso de contexto se evalúan en secuencia, lo que significa que podrías tener configuradas las siguientes variables de contexto:

| Variable de contexto | Valor | Descripción |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | El tipo de cocina favorito de un usuario. |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | El código de descuento disponible para un usuario. |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.${promo_code}}} "on delivery from your favorite" {{context.${favorite_cuisine}}} restaurants!"`{% endraw %} | Un mensaje personalizado que combina las variables anteriores. En un paso Mensaje, puedes utilizar el fragmento de {% raw %}`{{context.${personalized_message}}}`{% endraw %}código Liquid para hacer referencia a la variable de contexto y entregar un mensaje personalizado a cada usuario. También puedes utilizar un paso de contexto para guardar el valor [del código promocional]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) y utilizarlo como plantilla en otros pasos a lo largo de un Canvas. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Esto también se aplica a varios pasos de contexto. Por ejemplo, imagina esta secuencia:

1. Un paso Context inicial crea una variable llamada`JobInfo`  con el valor `job_title`.
2. Un paso de mensaje hace referencia{% raw %}`{{context.${JobInfo}}}`{% endraw %}y muestra`job_title`al usuario.
3. Más tarde, un paso de contexto actualiza la variable de contexto, cambiando el valor de`JobInfo`  a `job_description`.
4. Todos los pasos posteriores que hacen referencia`JobInfo`  ahora utilizan el valor actualizado`job_description` .

Las variables de contexto utilizan su valor más reciente en todo el Canvas, y cada actualización afecta a todos los pasos siguientes que hacen referencia a esa variable.
