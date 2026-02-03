---
nav_title: Variables de contexto
article_title: Variables de contexto
page_type: reference
description: "Este artículo de referencia explica las variables de contexto en los Lienzos Braze, incluyendo sus tipos, uso y mejores prácticas."
---

# Variables de contexto

> Las variables de contexto son datos temporales que puedes crear y utilizar en el recorrido de un usuario por un Canvas concreto. Te habilitan para personalizar los retrasos, segmentar a los usuarios dinámicamente y enriquecer la mensajería sin alterar permanentemente la información del perfil de un usuario. Las variables de contexto sólo existen dentro de la sesión de Canvas y no persisten en diferentes Canvas ni fuera de la sesión.

## Cómo funcionan las variables de contexto

Las variables de contexto pueden configurarse de dos formas:

- **A la entrada de Canvas:** Cuando los usuarios entran en un Canvas, los datos del evento o del desencadenante de la API pueden rellenar automáticamente las variables de contexto.
- **En un paso de Contexto:** Puedes definir o actualizar manualmente variables de contexto dentro del Canvas añadiendo un [paso en Canvas Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

Cada variable de contexto incluye

- Un nombre (como `flight_time` o `subscription_renewal_date`)
- Un tipo de datos (como número, cadena, hora o matriz)
- Un valor que asignas utilizando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) o a través de la herramienta **Añadir personalización**.

Una vez definida, puedes utilizar una variable de contexto en todo el Canvas haciendo referencia a ella con este formato: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Por ejemplo, {% raw %}`{{context.${flight_time}}}`{% endraw %} podría devolver la hora de vuelo programada del usuario.

Cada vez que un usuario entre en el Canvas -incluso si ya ha entrado antes-, las variables de contexto se redefinirán en función de los últimos datos de entrada y de la configuración del Canvas. Este enfoque basado en estados permite que cada entrada de Canvas mantenga su propio contexto independiente, lo que permite a los usuarios tener varios estados activos dentro del mismo viaje, conservando el contexto específico de cada estado.

Por ejemplo, si un cliente tiene dos vuelos próximos, tendrá dos estados de viaje distintos ejecutándose simultáneamente, cada uno con sus propias variables de contexto específicas del vuelo, como la hora de salida y el destino. Esto te permite enviar recordatorios personalizados sobre su vuelo de las 2 de la tarde a Nueva York al tiempo que envías actualizaciones diferentes sobre su vuelo de las 8 de la mañana a Los Ángeles mañana, de modo que cada mensaje siga siendo relevante para la reserva específica.

## Consideraciones

Puedes definir hasta 10 variables de contexto por [paso de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/). Cada nombre de variable puede tener hasta 100 caracteres y debe utilizar sólo letras, números o guiones bajos.

Las definiciones de las variables de contexto pueden tener hasta 10.240 caracteres. Si pasas variables de contexto a un Canvas desencadenado por la API, éstas comparten el mismo espacio de nombres que las variables creadas en un paso en Canvas. Por ejemplo, si envías una variable `purchased_item` en el objeto de contexto [de punto final`/canvas/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/), puedes hacer referencia a ella como {% raw %}`{{context.${purchased_item}}}`{% endraw %}. Si redefines esa variable en un paso de Contexto, el nuevo valor anulará el valor de la API para el recorrido de ese usuario.

Puedes almacenar hasta 50 KB por paso de Contexto, distribuidos en hasta 10 variables. Si el tamaño total de todas las variables de un paso supera los 50 KB, las variables que superen el límite no se evaluarán ni almacenarán. Por ejemplo, si tienes tres variables en un paso Contexto:

- Variable 1: 30 KB
- Variable 2: 19 KB
- Variable 3: 2 KB

La variable 3 no se evaluará ni almacenará porque la suma de las variables anteriores supera los 50 KB.

## Tipos de datos

A las variables de contexto que se crean o actualizan en el paso se les pueden asignar los siguientes tipos de datos.

{% alert note %}
Las variables de contexto tienen los mismos formatos previstos para los tipos de datos que [los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Cuando se utiliza el tipo matriz, Braze intenta analizar el valor como JSON, lo que permite crear con éxito matrices de objetos. Si los objetos de tus matrices no son JSON válidos, el resultado será una simple matriz de cadenas. <br><br>Para objetos anidados y matrices de objetos, utiliza el [filtro`as_json_string` Liquid](#converting-connected-content-strings-to-json). Si vas a crear el mismo objeto en un paso de Contexto, tendrás que renderizar el objeto utilizando `as_json_string`, como por ejemplo {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| Tipo de datos | Ejemplo de nombre de variable | Valor de ejemplo |
|---|---|---|
|Booleano| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|Número| credit_score |{% raw %}<code>740</code>{% endraw %}|
|Cadena| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|Matriz| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Matriz (de objetos)| pet_details |{% raw %}<code>[_mem_lt_br>_mem_amp_emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }_mem_lt_br>_mem_amp_emsp;,_mem_lt_br>_mem_amp_emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }_mem_lt_br>]</code>{% endraw %}|
|Hora (en UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objeto (aplanado) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Por defecto, el tipo de datos de la hora está en UTC. Si utilizas un tipo de datos de cadena para almacenar un valor de hora, puedes definir la hora como una zona horaria diferente, como PST. 

Por ejemplo, si vas a enviar un mensaje a un usuario el día antes de su cumpleaños, guardarías la variable de contexto como un tipo de datos de hora, porque hay una lógica Liquid asociada al envío del día anterior. Sin embargo, si vas a enviar un mensaje festivo el día de Navidad (25 de diciembre), no necesitarías referenciar la hora como una variable dinámica, por lo que sería preferible utilizar un tipo de datos cadena.

## Utilizar variables de contexto

Puedes utilizar variables contextuales en cualquier lugar en el que utilices Liquid en un Canvas, como en los pasos de [actualización de]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update) [mensajes]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) y usuarios, seleccionando **Añadir personalización**.

Por ejemplo, supongamos que quieres notificar a los pasajeros su acceso a la sala VIP antes de su próximo vuelo. Este mensaje sólo debe enviarse a los pasajeros que hayan comprado un billete de primera clase. Una variable de contexto es una forma flexible de hacer un seguimiento de esta información.

Los usuarios entrarán en el Canvas cuando compren un billete de avión. Para determinar la elegibilidad para el acceso al salón, crearemos una variable de contexto llamada `lounge_access_granted` en un paso de Contexto, y luego haremos referencia a esa variable de contexto en los pasos posteriores del recorrido del usuario.

![Variable de contexto configurada para hacer un seguimiento de si un pasajero reúne los requisitos para acceder a la sala VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

En este paso de Contexto, utilizaremos {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} para determinar si el tipo de vuelo que han comprado es `first_class`.

A continuación, crearemos un paso Mensaje para dirigirnos a los usuarios en los que {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} es `true`. Este mensaje será una notificación push que incluirá información personalizada sobre el salón. En función de esta variable de contexto, los pasajeros elegibles recibirán los mensajes pertinentes antes de su vuelo.

- Los pasajeros con billetes de primera clase recibirán: "¡Disfruta de un acceso exclusivo a la sala VIP!"
- Los pasajeros con billetes de negocios y económicos recibirán: "Mejora tu vuelo para acceder a una sala VIP exclusiva".

![Un paso de Mensajes con diferentes mensajes para enviar, según el tipo de billete de avión comprado.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Puedes añadir [opciones de retraso personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) con la información del paso Contexto, lo que significa que puedes seleccionar la variable que retrasa a los usuarios.
{% endalert %}

### Para las rutas de acción y los criterios de salida

Puedes aprovechar la comparación de filtros de propiedades con variables de contexto o atributos personalizados en estas acciones desencadenantes: **Realiza el evento personalizado** y **efectúa la compra**. Estos desencadenantes de acciones también admiten filtrar propiedades tanto básicas como anidadas. 

- Al comparar con propiedades básicas, las comparaciones disponibles coincidirán con el tipo de propiedad definido por el evento personalizado. Por ejemplo, las propiedades de cadena tendrán coincidencias regex exactamente iguales. Las propiedades booleanas serán verdaderas o falsas. 
- Al comparar con propiedades anidadas, los tipos no están predefinidos, por lo que puedes seleccionar comparaciones entre varios tipos de datos para booleanos, números, cadenas, hora y día del año, de forma similar a las comparaciones para atributos personalizados anidados. Si seleccionas un tipo de datos que no coincide con el tipo de datos real de la propiedad anidada en el momento de la comparación, el usuario no coincidirá con la Ruta de acción ni con los criterios de salida.

#### Ejemplos de ruta de acción

{% alert important %}
Para las comparaciones de atributos personalizados, utilizaremos el valor del atributo personalizado en el momento en que se realice la acción. Esto significa que un usuario no coincidirá con el grupo Ruta de acción si no tiene este atributo personalizado rellenado en el momento de la comparación, o si el valor del atributo personalizado no coincide con las comparaciones de propiedades definidas. Esto ocurre aunque el usuario hubiera coincidido al entrar en el paso Ruta de acción.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

La siguiente ruta de acción está configurada para ordenar a los usuarios que realizaron el evento personalizado `Account_Created` con la propiedad básica `source` a la variable contextual `app_source_variable`.

![Un ejemplo de ruta de acción que hace referencia a una variable de contexto al realizar un evento personalizado.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

La siguiente ruta de acción está configurada para hacer coincidir la propiedad básica `brand` del nombre concreto del producto `shoes` con una variable contextual `promoted_shoe_brand`.

![Un ejemplo de ruta de acción que hace referencia a una variable de contexto al realizar una compra.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Ejemplos de criterios de salida

{% tabs %}
{% tab Perform custom event %}

Los criterios de salida establecen que, en cualquier punto del recorrido de un usuario en el Canvas, saldrá de él si:

- Realizan el evento personalizado **Abandonar carrito**, y
- La propiedad básica **Artículo de la cesta** coincide con el valor de cadena de la variable de contexto `cart_item_threshold`.

![Criterios de salida configurados para salir de un usuario si realiza un evento personalizado basado en la variable de contexto.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Los criterios de salida establecen que, en cualquier punto del recorrido de un usuario en el Canvas, saldrá de él si:

- Realizan una compra específica para el nombre del producto "libro", y
- La propiedad anidada de esa compra "loyalty_program" es igual al atributo personalizado "VIP" del usuario.

![Criterios de salida configurados para salir de un usuario si realiza una compra.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Filtros de variables de contexto

Puedes crear filtros que utilicen variables de contexto previamente declaradas en [las rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) y en los pasos para [la división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

{% alert note %}
Los filtros de variables de contexto sólo están disponibles para las rutas de audiencia y los pasos para la división de decisiones.
{% endalert %}

Las variables de contexto se declaran y sólo son accesibles en el ámbito de un Canvas, lo que significa que no se puede hacer referencia a ellas en los segmentos. Los filtros de variables de contexto funcionan de forma similar en las rutas de audiencia y en los pasos para la división de decisiones: los pasos para la ruta de audiencia representan grupos múltiples, mientras que los pasos para la división de decisiones representan decisiones binarias.

![Ejemplo de paso para la división de decisiones con la opción de crear un filtro con una variable de contexto.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Al igual que las variables de contexto de Canvas tienen tipos predefinidos, las comparaciones entre variables de contexto y valores estáticos deben tener [tipos de datos coincidentes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). El filtro de variables de contexto permite realizar comparaciones entre varios tipos de datos para booleanos, números, cadenas, hora y día del año, de forma similar a las comparaciones para [atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Utiliza el mismo tipo de datos para tu variable contextual y para la comparación. Por ejemplo, si tu variable de contexto es un tipo de dato temporal, utiliza comparaciones temporales (como "antes" o "después"). Utilizar tipos de datos no coincidentes (como comparaciones de cadenas con una variable de contexto temporal) puede provocar un comportamiento inesperado.
{% endalert %}

He aquí un ejemplo de filtro de variables de contexto que compara la variable de contexto `product_name` con la regex `/braze/`.

![Un filtro configurado para que la variable de contexto "product_name" coincida con el regex "/braze/".]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparación con variables de contexto o atributos personalizados

Si seleccionas el alternador **Comparar con una variable de contexto o un atributo personalizado**, puedes construir filtros de variables de contexto que se comparen con variables de contexto previamente definidas o con atributos personalizados del usuario. Esto puede ser útil para realizar comparaciones dinámicas por usuario, como las desencadenadas por la API `context`, o para condensar una lógica de comparación compleja definida a través de variables de contexto.

{% tabs %}
{% tab Example 1 %}

Digamos que quieres enviar un recordatorio personalizado a los usuarios después de un periodo dinámico de inactividad, que incluye a cualquiera que no haya iniciado sesión en tu aplicación en los últimos tres días, debería recibir un mensaje.

Tienes una variable de contexto `re_engagement_date` que está definida como {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Ten en cuenta que `3 days` puede ser una cantidad variable que también se almacena como atributo personalizado del usuario. Así, si el `re_engagement_date` está después del `last_login_date` (almacenado como atributo personalizado en el perfil de usuario), se le enviará un mensaje.

![Una configuración de filtrado con atributos personalizados como tipo de personalización para la variable de contexto "re_engagement_date" después del atributo personalizado "last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

El siguiente filtro compara la variable de contexto `reminder_date` para que sea anterior a la variable de contexto `appointment_deadline`. Esto puede ayudar a agrupar usuarios en un paso de Rutas de audiencia para determinar si deben recibir recordatorios adicionales antes de la fecha límite de su cita.

![Una configuración de filtro con variables de contexto como tipo de personalización para la variable de contexto "reminder_date" en la variable de contexto "appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## Normalización de la coherencia horaria

Aunque la mayoría de las propiedades del evento que utilizan el tipo de marca de tiempo ya están en UTC en Canvas, hay algunas excepciones. Con la adición del Contexto Canvas, todas las propiedades del evento predeterminadas en los Lienzos basados en acciones estarán siempre en UTC. Este cambio forma parte de un esfuerzo más amplio para garantizar una experiencia más predecible y coherente al editar pasos en Canvas y mensajes. Ten en cuenta que este cambio afectará a todos los Canvas basados en acciones, tanto si el Canvas específico utiliza un paso en Canvas como si no.

{% alert important %}
En cualquier caso, recomendamos encarecidamente utilizar [filtros Liquid time_zone ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) para que las marcas de tiempo se representen en la zona horaria deseada. Puedes hacer referencia a esta [pregunta frecuente en el artículo Paso del contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example) para ver un ejemplo.
{% endalert %}

## Artículos relacionados

- [Paso contextual]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personalización y contenido dinámico con Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)
