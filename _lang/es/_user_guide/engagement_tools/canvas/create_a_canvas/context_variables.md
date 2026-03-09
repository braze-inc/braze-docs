---
nav_title: Variables de contexto
article_title: Variables de contexto
page_type: reference
description: "Este artículo de referencia explica las variables de contexto en Braze Canvases, incluyendo sus tipos, uso y mejores prácticas."
---

# Variables de contexto

> Las variables de contexto son datos temporales que puedes crear y utilizar durante el recorrido de un usuario por un Canvas específico. Habilitan la personalización de los retrasos, la segmentación dinámica de los usuarios y la enriquecimiento de la mensajería sin alterar permanentemente la información del perfil de usuario. Las variables de contexto solo existen dentro de la sesión de Canvas y no persisten en diferentes Canvases ni fuera de la sesión.

## Cómo funcionan las variables de contexto

Las variables de contexto se pueden configurar de dos maneras:

- **A la entrada de Canvas:** Cuando los usuarios entran en un Canvas, los datos del evento o del activador de la API pueden rellenar automáticamente las variables de contexto.
- **En un paso de contexto:** Puedes definir o actualizar las variables de contexto manualmente dentro del Canvas añadiendo un [paso de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

Cada variable de contexto incluye:

- Un nombre (como`flight_time`  o `subscription_renewal_date`)
- Un tipo de datos (como número, cadena, hora o matriz).
- Un valor que asignas utilizando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) o mediante la herramienta **Añadir personalización**.

Una vez definida, puedes utilizar una variable de contexto en todo el Canvas haciendo referencia a ella en este formato: {% raw %}`{{context.${example_variable_name}}}`{% endraw %}.

Por ejemplo,{% raw %}`{{context.${flight_time}}}`{% endraw %}podría devolver la hora del vuelo programado del usuario.

Cada vez que un usuario accede al Canvas, incluso si ya ha accedido anteriormente, las variables de contexto se redefinirán en función de las últimas entradas realizadas y de la configuración del Canvas. Este enfoque con estado permite que cada entrada de Canvas mantenga su propio contexto independiente, lo que permite a los usuarios tener varios estados activos dentro del mismo recorrido, al tiempo que se conserva el contexto específico de cada estado.

Por ejemplo, si un cliente tiene dos vuelos próximos, tendrás dos estados de viaje independientes que se ejecutarán simultáneamente, cada uno con sus propias variables de contexto específicas del vuelo, como la hora de salida y el destino. Esto te permite enviar recordatorios personalizados sobre tu vuelo de las 2 de la tarde a Nueva York, al tiempo que envías diferentes actualizaciones sobre tu vuelo de las 8 de la mañana a Los Ángeles mañana, de modo que cada mensaje sea relevante para la reserva específica.

## Consideraciones

Puedes definir hasta 10 variables de contexto por cada [paso de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/). Cada nombre de variable puede tener hasta 100 caracteres y solo puede contener letras, números o guiones bajos.

Las definiciones de variables de contexto pueden tener hasta 10 240 caracteres. Si pasas variables de contexto a un Canvas desencadenado por API, estas compartirán el mismo espacio de nombres que las variables creadas en un paso de contexto. Por ejemplo, si envías una variable`purchased_item`  en el objeto de contexto[`/canvas/trigger/send` del punto final]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/), puedes hacer referencia a ella como {% raw %}`{{context.${purchased_item}}}`{% endraw %}. Si redefines esa variable en un paso de contexto, el nuevo valor sustituirá al valor de la API para el recorrido de ese usuario.

Puedes almacenar hasta 50 KB por paso de contexto, distribuidos en hasta 10 variables. Si el tamaño total de todas las variables de un paso supera los 50 KB, las variables que superen el límite no se evaluarán ni se almacenarán. Por ejemplo, si tienes tres variables en un paso de contexto:

- Variable 1: 30 KB
- Variable 2: 19 KB
- Variable 3: 2 KB

La variable 3 no se evaluará ni almacenará porque la suma de las variables anteriores supera los 50 KB.

## Tipos de datos

A las variables de contexto que se crean o actualizan en el paso se les pueden asignar los siguientes tipos de datos.

{% alert note %}
Las variables de contexto tienen los mismos formatos esperados para los tipos de datos que [los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format). <br><br>Cuando usas el tipo de matriz, Braze intenta analizar el valor como JSON, lo que permite crear matrices de objetos correctamente. Si los objetos dentro de tus matrices no son JSON válidos, el resultado será una simple matriz de cadenas. <br><br>Para objetos anidados y matrices de objetos, utiliza el [filtro`as_json_string` Liquid](#converting-connected-content-strings-to-json). Si estás creando el mismo objeto en un paso de contexto, tendrás que renderizar el objeto utilizando `as_json_string`, como por ejemplo {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
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

Predeterminadamente, el tipo de datos de hora está en UTC. Si utilizas un tipo de datos de cadena para almacenar un valor de hora, puedes definir la hora como una zona horaria diferente, como PST. 

Por ejemplo, si envías un mensaje a un usuario el día antes de su cumpleaños, guardarías la variable de contexto como un tipo de datos de tiempo, ya que hay una lógica Liquid asociada al envío el día anterior. Sin embargo, si envías un mensaje festivo el día de Navidad (25 de diciembre), no necesitarás hacer referencia a la hora como una variable dinámica, por lo que sería preferible utilizar un tipo de datos de cadena.

## Uso de variables de contexto

Puedes utilizar variables de contexto en cualquier lugar donde utilices Liquid en Canvas, como en los pasos [Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) y [Actualización de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update), seleccionando **Añadir personalización**.

Por ejemplo, supongamos que deseas notificar a los pasajeros sobre su acceso a la sala VIP antes de su próximo vuelo. Este mensaje solo debe enviarse a los pasajeros que hayan comprado un billete de primera clase. Una variable de contexto es una forma flexible de realizar el seguimiento de esta información.

Los usuarios entrarán en Canvas cuando compren un billete de avión. Para determinar la elegibilidad para acceder a la sala VIP, crearemos una variable de contexto llamada`lounge_access_granted`  en un paso de contexto y, a continuación, haremos referencia a esa variable de contexto en los pasos posteriores del recorrido del usuario.

![Variable de contexto configurada para realizar el seguimiento de si un pasajero cumple los requisitos para acceder a la sala VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

En este paso del contexto, utilizaremos{% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %}  para determinar si el tipo de vuelo que han comprado es `first_class`.

A continuación, crearemos un paso Mensaje para dirigirnos a los usuarios donde{% raw %}`{{context.${lounge_access_granted}}}`{% endraw %}  es `true`. Este mensaje será una notificación push que incluirá información personalizada sobre la sala VIP. En función de esta variable contextual, los pasajeros elegibles recibirán los mensajes pertinentes antes de vuestro vuelo.

- Los pasajeros con billetes de primera clase recibirán: ¡Disfruta de acceso exclusivo a la sala VIP!
- Los pasajeros con billetes de clase Business y Economy recibirán: Mejora tu vuelo y disfruta de acceso exclusivo a la sala VIP.

![Un paso de mensaje con diferentes mensajes que enviar, dependiendo del tipo de billete de avión comprado.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Puedes añadir [opciones de retraso personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) con la información del paso Contexto, lo que significa que puedes seleccionar la variable que retrasa a los usuarios.
{% endalert %}

### Para las rutas de acción y los criterios de salida

Puedes aprovechar la comparación de filtros de propiedades con variables de contexto o atributos personalizados en estas acciones desencadenantes: **Realiza un evento personalizado** y **haz una compra**. Estos desencadenantes de acciones también admiten filtros de propiedades tanto para propiedades básicas como anidadas. 

- Al comparar con propiedades básicas, las comparaciones disponibles coincidirán con el tipo de propiedad definido por el evento personalizado. Por ejemplo, las propiedades de cadena tendrán coincidencias exactamente iguales en regex. Las propiedades booleanas serán verdaderas o falsas. 
- Al comparar con propiedades anidadas, los tipos no están predefinidos, por lo que puedes seleccionar comparaciones entre varios tipos de datos para booleanos, números, cadenas, hora y día del año, de forma similar a las comparaciones para atributos personalizados anidados. Si seleccionas un tipo de datos que no coincide con el tipo de datos real de la propiedad anidada en el momento de la comparación, el usuario no coincidirá con la ruta de acción ni con los criterios de salida.

#### Ejemplos de rutas de acción

{% alert important %}
Para las comparaciones de atributos personalizados, utilizaremos el valor del atributo personalizado en el momento en que se realice la acción. Esto significa que un usuario no coincidirá con el grupo Ruta de acción si no tiene este atributo personalizado rellenado en el momento de la comparación, o si el valor del atributo personalizado no coincide con las comparaciones de propiedades definidas. Esto ocurre incluso si el usuario hubiera coincidido al entrar en el paso de la ruta de acción.
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

La siguiente ruta de acción se configura para clasificar a los usuarios que realizaron el evento personalizado`Account_Created` con la propiedad básica`source` en la variable de contexto`app_source_variable` .

![Un ejemplo de ruta de acción que hace referencia a una variable de contexto al realizar un evento personalizado.]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

La siguiente ruta de acción está configurada para hacer coincidir la propiedad básica del nombre`brand` específico del`shoes` producto con una variable de contexto`promoted_shoe_brand` .

![Un ejemplo de ruta de acción que hace referencia a una variable de contexto al realizar una compra.]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### Ejemplos de criterios de salida

{% tabs %}
{% tab Perform custom event %}

Los criterios de salida establecen que, en cualquier momento del recorrido del usuario por Canvas, este saldrá de Canvas si:

- Realizan el evento personalizado **Abandonar carrito de compras** y
- La propiedad básica **Item in Cart** coincide con el valor de cadena de la variable de contexto`cart_item_threshold` .

![Criterios de salida configurados para dar de baja a un usuario si realiza un evento personalizado basado en la variable de contexto.]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

Los criterios de salida establecen que, en cualquier momento del recorrido del usuario por Canvas, este saldrá de Canvas si:

- Realizan una compra específica para el nombre del producto «libro» y
- La propiedad anidada de "loyalty_program"esa compra es igual al atributo personalizado «VIP» del usuario.

![Criterios de salida establecidos para dar de baja a un usuario si realiza una compra.]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### Filtrar variables de contexto

Puedes crear filtros que utilicen variables de contexto previamente declaradas en los pasos [de la ruta de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) y [para la división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

{% alert note %}
Los filtros de variables de contexto solo están disponibles para los pasos «Rutas de audiencia» y «Paso para la división de decisiones».
{% endalert %}

Las variables de contexto se declaran y solo son accesibles en el ámbito de un Canvas, lo que significa que no se puede hacer referencia a ellas en segmentos. Los filtros de variables de contexto funcionan de manera similar en los pasos de rutas de audiencia y para la división de decisiones: los pasos de rutas de audiencia representan múltiples grupos, mientras que los pasos para la división de decisiones representan decisiones binarias.

![Ejemplo de paso para la división de decisiones con la opción de crear un filtro con una variable de contexto.]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

Al igual que las variables de contexto de Canvas tienen tipos predefinidos, las comparaciones entre variables de contexto y valores estáticos deben tener [tipos de datos coincidentes]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types). El filtro de variable de contexto permite realizar comparaciones entre múltiples tipos de datos para valores booleanos, números, cadenas, hora y día del año, de forma similar a las comparaciones para [atributos personalizados anidados]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/).

{% alert note %}
Utiliza el mismo tipo de datos para la variable de contexto y la comparación. Por ejemplo, si tu variable de contexto es un tipo de datos de tiempo, utiliza comparaciones de tiempo (como «antes» o «después»). El uso de tipos de datos incompatibles (como comparaciones de cadenas con una variable de contexto temporal) puede provocar un comportamiento inesperado.
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

Aquí tienes un ejemplo de cómo filtrar la variable de contexto para comparar la variable de contexto`product_name` con la regex`/braze/`.

![Una configuración para filtrar la variable de contexto"product_name" de manera que coincida con la regex «/Braze/».]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### Comparación con variables de contexto o atributos personalizados

Al alternar la opción **Comparar con una variable de contexto o un atributo personalizado**, puedes crear filtros de variables de contexto que se comparen con variables de contexto definidas previamente o con atributos personalizados del usuario. Esto puede resultar útil para realizar comparaciones dinámicas por usuario, como las que se desencadenan a través de la API`context`, o para condensar una lógica de comparación compleja definida a través de variables de contexto.

{% tabs %}
{% tab Example 1 %}

Supongamos que deseas enviar un recordatorio personalizado a los usuarios tras un periodo dinámico de inactividad, lo que incluye a cualquier persona que no haya iniciado sesión en tu aplicación en los últimos tres días, que debería recibir un mensaje.

Tienes una variable de contexto`re_engagement_date`  que se define como {% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}. Ten en cuenta que`3 days`  puede ser una cantidad variable que también se almacena como un atributo personalizado del usuario. Por lo tanto, si el`re_engagement_date`  está después del`last_login_date`  (almacenado como un atributo personalizado en el perfil de usuario), se les enviará un mensaje.

![Una configuración de filtro con atributos personalizados como tipo de personalización para la variable de contexto"re_engagement_date" después del atributo "last_login_date".]({%image_buster/assets/img/context_variable_filter2.pngpersonalizado    %})

{% endtab %}
{% tab Example 2 %}

El siguiente filtro filtra la variable de contexto`reminder_date`  con la variable de contexto`appointment_deadline` . Esto puede ayudar a los usuarios del grupo en un paso de la ruta de audiencia a determinar si deben recibir recordatorios adicionales antes de la fecha límite de su cita.

![Una configuración de filtro con variables de contexto como tipo de personalización para la variable de contexto"reminder_date"  en la variable de contexto"appointment_deadline".]({%image_buster/assets/img/context_variable_filter3.png    %})

{% endtab %}
{% endtabs %}

## Estandarización de la coherencia de las zonas horarias

Aunque la mayoría de las propiedades del evento que utilizan el tipo de marca de tiempo ya están en UTC en Canvas, hay algunas excepciones. Con la incorporación de Canvas Context, todas las propiedades predeterminadas del evento con marca de tiempo en los lienzos basados en acciones estarán siempre en UTC. Este cambio forma parte de un esfuerzo más amplio por garantizar una experiencia más predecible y coherente al editar los pasos y mensajes en Canvas. Ten en cuenta que este cambio afectará a todos los Canvases basados en acciones, independientemente de si el Canvas específico utiliza un paso de contexto o no.

{% alert important %}
En cualquier caso, recomendamos encarecidamente utilizar [filtros time_zoneLiquid]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know)  para que las marcas de tiempo se representen en la zona horaria deseada. Puedes consultar esta [pregunta frecuente en el artículo sobre el paso Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example) para ver un ejemplo.
{% endalert %}

## Artículos relacionados

- [Paso de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Personalización y contenido dinámico con Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)
