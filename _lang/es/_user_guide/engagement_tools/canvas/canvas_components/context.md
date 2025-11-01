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
Los pasos del contexto están actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.<br><br>Ten en cuenta que la adhesión voluntaria al paso en Canvas de acceso anticipado modificará el modo en que se gestionan las marcas de tiempo en todos tus lienzos. Para saber más sobre esto, consulta [Normalización de la coherencia horaria](#time-zone-consistency-standardization).
{% endalert %}

## Cómo funciona

\![Un paso de Contexto como primer paso de un Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Los pasos contextuales te permiten crear y utilizar datos temporales durante el recorrido de un usuario por un Canvas concreto. Estos datos sólo existen dentro de ese recorrido en Canvas y no persisten en diferentes Canvas ni fuera de la sesión.

Dentro de este marco, cada paso de Contexto puede definir múltiples variables de contexto: datos temporales que te habilitan para personalizar los retrasos, segmentar a los usuarios dinámicamente y enriquecer la mensajería sin alterar permanentemente la información del perfil de un usuario.

Por ejemplo, si estás gestionando reservas de vuelos, podrías crear una variable de contexto para la hora de vuelo programada de cada usuario. Así podrías establecer retrasos relativos a la hora de vuelo de cada usuario y enviar recordatorios personalizados desde el mismo Canvas.

Puedes establecer variables de contexto de dos formas:

- **A la entrada de Canvas:** Cuando los usuarios entran en un Canvas, los datos del evento o del desencadenante de la API pueden rellenar automáticamente las variables de contexto.
- **En un paso de Contexto:** Puedes definir o actualizar manualmente variables de contexto dentro del Canvas añadiendo un paso en Canvas Contexto.

Cada variable de contexto incluye

- Un nombre (como `flight_time` o `subscription_renewal_date`)
- Un [tipo de datos](#context-variable-types) (como número, cadena, hora o matriz)
- Un valor que asignas utilizando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) o a través de la herramienta **Añadir personalización**.

Una vez definida, puedes utilizar una variable de contexto en todo el Canvas haciendo referencia a ella con este formato: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Por ejemplo, {% raw %}`{{context.${flight_time}}}`{% endraw %} podría devolver la hora de vuelo programada del usuario.

Cada vez que un usuario entre en el Canvas -incluso si ya ha entrado antes-, las variables de contexto se redefinirán en función de los últimos datos de entrada y de la configuración del Canvas. Este enfoque basado en estados permite que cada entrada de Canvas mantenga su propio contexto independiente, lo que permite a los usuarios tener varios estados activos dentro del mismo viaje, conservando el contexto específico de cada estado.

Por ejemplo, si un cliente tiene dos vuelos próximos, tendrá dos estados de viaje distintos ejecutándose simultáneamente, cada uno con sus propias variables de contexto específicas del vuelo, como la hora de salida y el destino. Esto te permite enviar recordatorios personalizados sobre su vuelo de las 2 de la tarde a Nueva York al tiempo que envías actualizaciones diferentes sobre su vuelo de las 8 de la mañana a Los Ángeles mañana, de modo que cada mensaje siga siendo relevante para la reserva específica.

## Consideraciones

- Puedes tener hasta 10 variables de contexto por paso Contexto.
- Cada nombre de variable contextual puede tener hasta 100 caracteres.
- Los nombres de las variables de contexto deben ser identificadores válidos (sólo letras, números y guiones bajos).
- Las definiciones de las variables de contexto pueden tener hasta 10.240 caracteres. 
- Las variables de contexto pasadas a un Canvas desencadenado por la API comparten los mismos espacios de nombres que las variables de contexto creadas en un paso en Canvas. Esto significa que si envías una variable `purchased_item` en el [objeto de contexto]({{site.baseurl}}/api/objects_filters/context_object) de punto final `/canvas/trigger/send`, se puede hacer referencia a ella como {% raw %}`{context.${purchased_item}}`{% endraw %}, y volver a declarar esa variable en un paso en Canvas anulará lo que se envió anteriormente.
- Puedes almacenar hasta 50 KB por paso de contexto, distribuidos hasta 10 variables por paso. Los tamaños de las variables que sumen más de 50 KB en un paso no se evaluarán ni almacenarán para el usuario. Estos tamaños se calculan en secuencia. Por ejemplo, si tienes 3 variables en un paso Contexto:
  - Variable 1: 30 KB
  - Variable 2: 19 KB
  - Variable 3: 2 KB
  - Esto significa que la Variable 3 no se evaluará ni almacenará porque la suma de todas las demás variables de contexto supera los 50 KB.

## Crear un paso Contexto

### Paso 1: Añade un paso

Añade un paso a tu Canvas, luego arrastra y suelta el componente desde la barra lateral, o selecciona el botón más <i class="fas fa-plus-circle"></i> y selecciona **Contexto**.

### Paso 2: Define las variables

{% alert note %}
Puedes definir hasta 10 variables de contexto para cada paso de Contexto.
{% endalert %}

Para definir una variable de contexto:

1. Dale un **nombre** a tu variable contextual.
2. Selecciona un [tipo de datos](#context-variable-types).
3. Escribe una expresión Liquid manualmente o utiliza **Añadir personalización** para crear un fragmento de código Liquid a partir de atributos preexistentes.
4. Selecciona **Vista previa** para comprobar el valor de tu variable contextual.
5. (Opcional) Para variables adicionales, selecciona **Añadir variable de contexto** y repite los pasos 1-4.
6. Cuando hayas terminado, selecciona **Hecho**.

Ahora puedes utilizar tu variable contextual en cualquier lugar donde utilices Liquid, como en los pasos de actualización de mensajes y usuarios, seleccionando **Añadir personalización**. Para un recorrido completo, consulta [Utilizar variables contextuales](#using-context-variables).

## Tipos de datos de las variables de contexto {#context-variable-types}

A las variables de contexto que se crean o actualizan en el paso se les pueden asignar los siguientes tipos de datos.

{% alert note %}
Las variables de contexto tienen los mismos formatos previstos para los tipos de datos que [los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Para objetos anidados y matrices de objetos, utiliza el [filtro`as_json_string` Liquid](#converting-connected-content-strings-to-json). Si vas a crear el mismo objeto en un paso de Contexto, tendrás que renderizar el objeto utilizando `as_json_string`, como por ejemplo {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Tipo de datos | Ejemplo de nombre de variable | Valor de ejemplo |
|---|---|---|
|Booleano| loyalty_program |{% raw %}<code>verdadero</code>{% endraw %}| 
|Número| credit_score |{% raw %}<code>740{% endraw %}|
|Cadena| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Matriz| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Hora (en UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objeto (aplanado) | user_profile|{% raw %}<code>{<br> "first_name": "{{user.first_name}}",<br> "last_name": "{{user.last_name}}",<br> "correo electrónico": "{{user.email}}",<br> "loyalty_points": {{user.loyalty_points}},<br> "preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por defecto, el tipo de datos de la hora está en UTC. Si utilizas un tipo de datos de cadena para almacenar un valor de hora, puedes definir la hora como una zona horaria diferente, como PST. 

Por ejemplo, si vas a enviar un mensaje a un usuario el día antes de su cumpleaños, guardarías la variable de contexto como un tipo de datos de hora, porque hay una lógica Liquid asociada al envío del día anterior. Sin embargo, si vas a enviar un mensaje festivo el día de Navidad (25 de diciembre), no necesitarías referenciar la hora como una variable dinámica, por lo que sería preferible utilizar un tipo de datos cadena.

## Utilizar variables de contexto {#using-context-variables}

Por ejemplo, supongamos que quieres notificar a los pasajeros su acceso a una sala VIP antes de su próximo vuelo. Este mensaje sólo debe enviarse a los pasajeros que hayan comprado un billete de primera clase. Una variable de contexto es una forma flexible de hacer un seguimiento de esta información.

Los usuarios entrarán en el Canvas cuando compren un billete de avión. Para determinar la elegibilidad para el acceso al salón, crearemos una variable de contexto llamada `lounge_access_granted` en un paso de Contexto, y luego haremos referencia a esa variable de contexto en los pasos posteriores del recorrido del usuario.

\![Variable de contexto configurada para realizar un seguimiento de si un pasajero reúne los requisitos para acceder a la sala VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

En este paso de Contexto, utilizaremos {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} para determinar si el tipo de vuelo que han comprado es `first_class`.

A continuación, crearemos un paso Mensaje para dirigirnos a los usuarios en los que {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} es `true`. Este mensaje será una notificación push que incluirá información personalizada sobre el salón. En función de esta variable de contexto, los pasajeros elegibles recibirán los mensajes pertinentes antes de su vuelo.

- Los pasajeros con billetes de primera clase recibirán: "¡Disfruta de un acceso exclusivo a la sala VIP!"
- Los pasajeros con billetes de negocios y económicos recibirán: "Mejora tu vuelo para acceder a una sala VIP exclusiva".

\![Un paso de Mensajes con diferentes mensajes para enviar, dependiendo del tipo de billete de avión comprado.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Puedes añadir [opciones de retraso personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) con la información del paso Contexto, lo que significa que puedes seleccionar la variable que retrasa a los usuarios.
{% endalert %}

### Para las rutas de acción y los criterios de salida

Puedes aprovechar la comparación de filtros de propiedades con variables de contexto o atributos personalizados en estas acciones desencadenantes: **Realiza un evento personalizado** y **efectúa una compra**. Estos desencadenantes de acciones también admiten filtrar propiedades tanto básicas como anidadas. 

- Al comparar con propiedades básicas, las comparaciones disponibles coincidirán con el tipo de propiedad definido por el evento personalizado. Por ejemplo, las propiedades de cadena tendrán coincidencias regex exactamente iguales. Las propiedades booleanas serán verdaderas o falsas. 
- Al comparar con propiedades anidadas, los tipos no están predefinidos, por lo que puedes seleccionar comparaciones entre varios tipos de datos para booleanos, números, cadenas, hora y día del año, de forma similar a las comparaciones para atributos personalizados anidados. Si seleccionas un tipo de datos que no coincide con el tipo de datos real de la propiedad anidada en el momento de la comparación, el usuario no coincidirá con la Ruta de acción ni con los criterios de salida.

#### Ejemplos de ruta de acción

{% alert important %}
Para las comparaciones de atributos personalizados, utilizaremos el valor del atributo personalizado en el momento en que se realice la acción. Esto significa que un usuario no coincidirá con el grupo Ruta de acción si no tiene este atributo personalizado rellenado en el momento de la comparación, o si el valor del atributo personalizado no coincide con las comparaciones de propiedades definidas. Esto ocurre aunque el usuario hubiera coincidido al entrar en el paso Ruta de acción.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

La siguiente ruta de acción está configurada para ordenar a los usuarios que realizaron el evento personalizado `Account_Created` con la propiedad básica `source` a la variable contextual `app_source_variable`.

\![Un ejemplo de ruta de acción que hace referencia a una variable de contexto al realizar un evento personalizado.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

La siguiente ruta de acción está configurada para hacer coincidir la propiedad básica `brand` del nombre concreto del producto `shoes` con una variable contextual `promoted_shoe_brand`.

\![Ejemplo de ruta de acción que hace referencia a una variable de contexto al realizar una compra.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Ejemplos de criterios de salida

{% tabs %}
{% tab Perform custom event %}

Los criterios de salida establecen que, en cualquier punto del recorrido de un usuario en el Canvas, saldrá de él si:

- Realizan el evento personalizado **Abandonar carrito**, y
- La propiedad básica **Artículo de la cesta** coincide con el valor de cadena de la variable de contexto `cart_item_threshold`.

\![Criterios de salida configurados para salir de un usuario si realiza un evento personalizado basado en la variable de contexto.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Los criterios de salida establecen que, en cualquier punto del recorrido de un usuario en el Canvas, saldrá de él si:

- Realizan una compra específica para el nombre del producto "libro", y
- La propiedad anidada de esa compra "loyalty_program" es igual al atributo personalizado "VIP" del usuario.

\![Criterios de salida configurados para salir de un usuario si realiza una compra.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Filtros de variables de contexto

Puedes crear filtros que utilicen variables de contexto previamente declaradas en [las rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) y en los pasos para [la división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

{% alert important %}
Los filtros de variables de contexto sólo están disponibles para las rutas de audiencia y los pasos para la división de decisiones.
{% endalert %}

Las variables de contexto se declaran y sólo son accesibles en el ámbito de un Canvas, lo que significa que no se puede hacer referencia a ellas en los segmentos. Los filtros de variables de contexto funcionan de forma similar en las rutas de audiencia y en los pasos para la división de decisiones: los pasos para la ruta de audiencia representan grupos múltiples, mientras que los pasos para la división de decisiones representan decisiones binarias.

\![Ejemplo de paso para la división de decisiones con la opción de crear un filtro con una variable de contexto.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Al igual que las variables de contexto de Canvas tienen tipos predefinidos, las comparaciones entre variables de contexto y valores estáticos deben tener [tipos de datos coincidentes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). El filtro de variables de contexto permite realizar comparaciones entre varios tipos de datos para booleanos, números, cadenas, hora y día del año, de forma similar a las comparaciones para [atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Utiliza el mismo tipo de datos para tu variable contextual y para la comparación. Por ejemplo, si tu variable de contexto es un tipo de dato temporal, utiliza comparaciones temporales (como "antes" o "después"). Utilizar tipos de datos no coincidentes (como comparaciones de cadenas con una variable de contexto temporal) puede provocar un comportamiento inesperado.
{% endalert %}

He aquí un ejemplo de filtro de variables de contexto que compara la variable de contexto `product_name` con la regex `/braze/`.

Una configuración de filtrar la variable de contexto "product_name" para que coincida con el regex "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparación con variables de contexto o atributos personalizados

Si seleccionas el alternador **Comparar con una variable de contexto o un atributo personalizado**, puedes construir filtros de variables de contexto que se comparen con variables de contexto previamente definidas o con atributos personalizados del usuario. Esto puede ser útil para realizar comparaciones dinámicas por usuario, como las desencadenadas por la API `context`, o para condensar una lógica de comparación compleja definida a través de variables de contexto.

{% tabs %}
{% tab Example 1 %}

Digamos que quieres enviar un recordatorio personalizado a los usuarios después de un periodo dinámico de inactividad, que incluye a cualquiera que no haya iniciado sesión en tu aplicación en los últimos tres días, debería recibir un mensaje.

Tienes una variable de contexto `re_engagement_date` que está definida como {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Ten en cuenta que `3 days` puede ser una cantidad variable que también se almacena como atributo personalizado del usuario. Así, si el `re_engagement_date` está después del `last_login_date` (almacenado como atributo personalizado en el perfil de usuario), se le enviará un mensaje.

\![Una configuración de filtrado con atributos personalizados como tipo de personalización para la variable de contexto "re_engagement_date" después del atributo personalizado "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

El siguiente filtro compara la variable de contexto `reminder_date` para que sea anterior a la variable de contexto `appointment_deadline`. Esto puede ayudar a agrupar usuarios en un paso de Rutas de audiencia para determinar si deben recibir recordatorios adicionales antes de la fecha límite de su cita.

\![Una configuración de filtro con variables de contexto como tipo de personalización para la variable de contexto "reminder_date" en la variable de contexto "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Vista previa de las rutas de usuario

Te recomendamos que pruebes y [veas previamente tus rutas de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) para asegurarte de que tus mensajes se envían a la audiencia adecuada y de que las variables de contexto se evalúan según los resultados esperados.

{% alert note %}
Si estás previsualizando tu Canvas en la sección **Vista previa & Prueba de envío** del editor, la fecha y hora de la vista previa del mensaje de prueba **no** estará normalizada a UTC porque este panel genera vistas previas como cadenas. Esto significa que si un Canvas está configurado para aceptar un objeto `time`, la vista previa del mensaje no previsualizará con precisión lo que ocurre cuando el Canvas está en vivo. Para probar tu Canvas con mayor precisión, te recomendamos que, en su lugar, previsualices las rutas de usuario.
{% endalert %}

Asegúrate de observar las situaciones habituales que crean variables de contexto no válidas. Al previsualizar tu ruta de usuario, puedes ver los resultados de los pasos de Retraso personalizados mediante variables de contexto, y cualquier comparación de pasos de audiencia, decisión o Ruta de acción que relacione a los usuarios con cualquier variable de contexto.

Si la variable de contexto es válida, puedes hacer referencia a ella en todo tu Canvas. Sin embargo, si la variable de contexto no se creó correctamente, los pasos futuros de tu Canvas tampoco tendrán un rendimiento correcto. Por ejemplo, si creas un paso Contexto para asignar a los usuarios una hora de cita, pero estableces el valor de la hora de cita en una fecha pasada, el correo electrónico recordatorio de tu paso Mensaje nunca se enviará.

## Convertir cadenas de contenido conectado a JSON

Al realizar una [llamada a Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) en un paso de Contexto, el JSON devuelto por la llamada se evaluará como un tipo de datos de cadena para mantener la coherencia y evitar errores. Si quieres convertir esta cadena en JSON, conviértela utilizando `as_json_string`. Por ejemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Normalización de la coherencia horaria

Con la adición del Contexto Canvas, todas las marcas de tiempo con un [tipo de fecha/hora]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) de las [propiedades del evento desencadenante]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) en los Canvas basados en acciones se normalizarán siempre a [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Antes, las marcas de tiempo de las propiedades del evento se normalizaban a UTC, con [algunas excepciones]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know). Ahora, esto proporcionará una experiencia más coherente para editar los pasos en Canvas y los mensajes.

Considera este ejemplo de cómo este cambio podría afectar a una marca de tiempo en Canvas. Supongamos que tenemos un Canvas basado en acciones que utiliza una propiedad de evento en el primer paso del Canvas con el siguiente paso Mensaje: 

{% raw %}
`Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!`
{% endraw %}

\![Viaje contextual con un paso de Mensaje como primer paso.]({% image_buster /assets/img/context_timezone_example.png %}){: style="max-width:50%"}

El paso también tendrá una carga útil de evento como: 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
}
```

Históricamente, el mensaje sería: `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

Con el acceso anticipado al Contexto Canvas, el mensaje será ahora: `Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!` Esto se debe a que la marca de tiempo está en UTC, que está 8 horas por delante de la hora del Pacífico (la zona horaria especificada en la carga útil original con `-08:00`).

{% alert important %}
Para tener en cuenta este cambio de marca de tiempo, en todas las circunstancias, recomendamos encarecidamente [utilizar filtros Liquid]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) para que las marcas de tiempo estén representadas en la zona horaria deseada.
{% endalert %}

### Utilizar Liquid para indicar una marca de tiempo en tu zona horaria preferida

Considera el siguiente fragmento de código Liquid:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

Esta lógica da como resultado la siguiente salida: `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

La zona horaria preferida también puede enviarse en la carga útil de propiedades del evento y utilizarse en la lógica Liquid: 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

Este es un ejemplo del fragmento de código Liquid:

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: canvas_entry_properties.${user_timezone} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

## Solución de problemas {#troubleshooting}

### Variables de contexto no válidas

Se considera que una variable de contexto no es válida cuando
- Falla una llamada a un Contenido conectado incrustado.
- La expresión Liquid en tiempo de ejecución devuelve un valor que no coincide con el tipo de datos o está vacío (nulo).

Por ejemplo, si el tipo de datos de la variable de contexto es **Número**, pero la expresión Liquid devuelve una cadena, no es válida.

En estas circunstancias: 
- El usuario avanzará al siguiente paso. 
- El análisis del paso en Canvas lo contará como _No actualizado_.

Al solucionar problemas, controla la métrica _No actualizado_ para comprobar que tu variable de contexto se actualiza correctamente. Si la variable de contexto no es válida, tus usuarios podrán continuar en tu Canvas pasado el paso de Contexto, pero no podrán acceder a los pasos posteriores.

Consulta los ejemplos de configuración de cada tipo de datos en [Tipos de datos variables contextuales](#context-variable-types).

## Preguntas más frecuentes

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
4. Todos los pasos posteriores que hagan referencia a `JobInfo` utilizarán ahora el valor actualizado `job_description`.

Las variables de contexto utilizan su valor más reciente en todo el Canvas, y cada actualización afecta a todos los pasos siguientes que hagan referencia a esa variable.

### ¿Influye la estandarización de la coherencia horaria del Contexto Canvas en los Canvas desencadenados por API?

No, este cambio sólo afecta a los Lienzos desencadenantes de acciones. Las marcas de tiempo enviadas a los Lienzos desencadenados por la API tendrán el tipo de cadena, no el tipo de hora, por lo que siempre se conserva la zona horaria original.

### ¿Cómo se relaciona esto con las excepciones anotadas en las propiedades de entrada y propiedades del evento del Canvas?

Participar en el acceso anticipado al Contexto Canvas elimina [esas excepciones]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know), independientemente de si estás utilizando un paso en Canvas.
