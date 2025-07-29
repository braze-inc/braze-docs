---
nav_title: Contexto 
article_title: Contexto 
alias: /context/
page_order: 1.5
page_type: reference
description: "Este artículo de referencia explica cómo crear y utilizar pasos en Canvas."
tool: Canvas

---

# Contexto

> Los pasos contextuales te permiten crear y actualizar una o varias variables para un usuario a medida que se desplaza por un Canvas. Por ejemplo, si tienes un Canvas que gestiona descuentos de temporada, puedes utilizar una variable de contexto para almacenar un código de descuento diferente cada vez que un usuario entre en el Canvas.

{% alert important %}
Los pasos del contexto están actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado.
{% endalert %}

## Cómo funciona

![Un paso de Contexto como primer paso de un Canvas.]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

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

Por ejemplo,
{% raw %}`{{context.${flight_time}}}{% endraw %}` podría devolver la hora de vuelo programada del usuario.

Cada vez que un usuario entre en el Canvas -incluso si ya ha entrado antes-, las variables de contexto se redefinirán en función de los últimos datos de entrada y de la configuración del Canvas. Esto permite que los viajes sigan siendo personalizados y precisos, incluso para usuarios con múltiples entradas.

## Crear un paso Contexto

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
5. (Opcional) Para variables adicionales, selecciona **Añadir variable de contexto** y repite los pasos 1-4.
6. Cuando hayas terminado, selecciona **Hecho**.

Ahora puedes utilizar tu variable contextual en cualquier lugar donde utilices Liquid, como en los pasos de actualización de mensajes y usuarios, seleccionando **Añadir personalización**. Para un recorrido completo, consulta [Utilizar variables contextuales](#using-context-variables).

### Paso 3: Rutas de usuario de prueba (opcional)

Si la variable de contexto es válida, puedes hacer referencia a ella en todo tu Canvas. Sin embargo, si la variable de contexto no se creó correctamente, los pasos futuros de tu Canvas tampoco tendrán un rendimiento correcto. Te recomendamos que pruebes y [veas previamente tus rutas de usuario]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths) para asegurarte de que tus mensajes se envían a la audiencia adecuada. Ten cuidado con las situaciones habituales que crean [variables de contexto no válidas](#troubleshooting).

Por ejemplo, si creas un paso de Contexto para asignar a los usuarios una hora de cita, pero estableces el valor de la hora de cita en una fecha pasada, el correo electrónico recordatorio que elabores en tu paso de Mensaje nunca se enviará. 

## Tipos de datos de las variables de contexto {#context-variable-types}

A las variables de contexto que se crean o actualizan en el paso se les pueden asignar los siguientes tipos de datos.

{% alert note %}
Las variables de contexto tienen los mismos formatos esperados para los tipos de datos que [los eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format), pero las variables de contexto no admiten objetos anidados.
{% endalert %}

| Tipo de datos | Ejemplo de nombre de variable | Valor de ejemplo |
|---|---|---|
|Booleano| programa_de_fidelidad |{% raw %}<code>true</code>{% endraw %}| 
|Número| puntuación_crédito |{% raw %}<code>740{% endraw %}|
|Cadena| nombre_producto |{% raw %}<code>green_tea</code>{% endraw %} |
|Matriz| productos_favoritos|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|Tiempo| fecha_última_compra|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|Objeto (aplanado) | perfil_usuario|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Utilizar variables de contexto {#using-context-variables}

Por ejemplo, supongamos que quieres notificar a los pasajeros su acceso a una sala VIP antes de su próximo vuelo. Este mensaje sólo debe enviarse a los pasajeros que hayan comprado un billete de primera clase. Una variable de contexto es una forma flexible de hacer un seguimiento de esta información.

Los usuarios entrarán en el Canvas cuando compren un billete de avión. Para determinar la elegibilidad para el acceso al salón, crearemos una variable de contexto llamada `lounge_access_granted` en un paso de Contexto, y luego haremos referencia a esa variable de contexto en los pasos posteriores del recorrido del usuario.

![Variable de contexto configurada para realizar un seguimiento de si un pasajero cumple los requisitos para acceder a la sala VIP.]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

En este paso de Contexto, utilizaremos {% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} para determinar si el tipo de vuelo que han comprado es `first_class`.

A continuación, crearemos un paso Mensaje para dirigirnos a los usuarios en los que {% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} es `true`. Este mensaje será una notificación push que incluirá información personalizada sobre el salón. En función de esta variable de contexto, los pasajeros elegibles recibirán los mensajes pertinentes antes de su vuelo.

- Los pasajeros con billetes de primera clase recibirán: "¡Disfruta de un acceso exclusivo a la sala VIP!"
- Los pasajeros con billetes de negocios y económicos recibirán: "Mejora tu vuelo para acceder a una sala VIP exclusiva".

![Un paso de mensajería con diferentes mensajes para enviar, dependiendo del tipo de billete de avión comprado.]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
Puedes añadir [opciones de retraso personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) con la información del paso Contexto, lo que significa que puedes seleccionar la variable que retrasa a los usuarios.
{% endalert %}

## Convertir cadenas de contenido conectado a JSON

Al realizar una [llamada a Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call) en un paso de Contexto, el JSON devuelto por la llamada se evaluará como un tipo de datos de cadena para mantener la coherencia y evitar errores. Si quieres convertir esta cadena en JSON, conviértela utilizando `as_json_string`. Por ejemplo:

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## Solución de problemas {#troubleshooting}

### Variables de contexto no válidas

Se considera que una variable de contexto no es válida cuando
- Falla una llamada a un Contenido conectado incrustado.
- La expresión Liquid en tiempo de ejecución devuelve un valor que no coincide con el tipo de datos o está vacío (nulo).

Por ejemplo, si el tipo de datos de la variable de contexto es **Número**, pero la expresión Liquid devuelve una cadena, no es válida.

En estas circunstancias: 
- El usuario avanzará al siguiente paso. 
- El análisis del paso en Canvas lo contará como _No actualizado_.

Al solucionar problemas, controla la métrica _No actualizado_ para comprobar que tu variable de contexto se actualiza correctamente. Si la variable de contexto no es válida, tus usuarios podrán continuar en tu Canvas más allá del paso Contexto, pero no podrán acceder a los pasos posteriores.

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
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{promo_code}} "on delivery from your favorite" {{favorite_cuisine}} restaurants!"`{% endraw %} | Un mensaje personalizado que combina las variables anteriores. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

En un paso de mensajería, podrías utilizar el fragmento de código Liquid {% raw %}`{{context.${personalized_message}}}`{% endraw %} para hacer referencia a la variable de contexto y entregar un mensaje personalizado a cada usuario.

Esto también se aplica a varios pasos del Contexto. Por ejemplo, imagina esta secuencia:
1. Un paso inicial de Contexto crea una variable llamada `JobInfo` con el valor `job_title`.
2. Un paso de Mensaje hace referencia a {% raw %}`{{context.${JobInfo}}}`{% endraw %} y muestra `job_title` al usuario.
3. Más tarde, un paso de Contexto actualiza la variable de contexto, cambiando el valor de `JobInfo` a `job_description`.
4. Todos los pasos posteriores que hagan referencia a `JobInfo` utilizarán ahora el valor actualizado `job_description`.

Las variables de contexto utilizan su valor más reciente en todo el Canvas, y cada actualización afecta a todos los pasos siguientes que hagan referencia a esa variable.


