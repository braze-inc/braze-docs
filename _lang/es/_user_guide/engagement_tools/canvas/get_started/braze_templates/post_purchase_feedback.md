---
nav_title: Comentarios posteriores a la compra
article_title: Comentarios posteriores a la compra
page_order: 6
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla Braze Canvas para orquestar experiencias personalizadas que te permitan responder a los comentarios y establecer relaciones con tus usuarios."
tool: Canvas
---

# Comentarios posteriores a la compra

> Utiliza la plantilla de comentarios posteriores a la compra para obtener información crítica sobre cómo interactúan tus clientes con tu marca y asegurarte de que siguen teniendo experiencias positivas. Al aprovechar la comunicación personalizada y un conjunto estructurado de mensajes, puedes seguir construyendo y fomentando las relaciones con tus clientes.

Este artículo te guiará a través de un caso de uso de la plantilla **Comentarios posteriores a la compra**, que está diseñada para la etapa de conversión del ciclo de vida del usuario. Cuando hayas terminado, habrás creado un Canvas que anima a los usuarios a dar su opinión sobre tu aplicación.

## Requisitos previos

Para utilizar correctamente esta plantilla, necesitarás lo siguiente:

- Un [atributo personalizado]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes) al que hacer referencia para los resultados del cuestionario de opinión.
- Una [Sincronización de Audiencias Braze]({{site.baseurl}}/partners/canvas_audience_sync/) configurada con los socios y audiencias que utilices.

## Adaptar la plantilla a tus necesidades

Supongamos que trabajamos para Decorumsoft, un desarrollador de videojuegos para móviles. Utilizaremos la plantilla de comentarios posteriores a la compra para recabar opiniones sobre el lanzamiento de nuestro último videojuego, Proxy War 3: Guerra de sed. Con esta información, elaboraremos nuestros planes de desarrollo para la expansión Liquid Mirage.

Antes de crear el Canvas, configuramos la integración de [Braze Audience Sync con Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/), de modo que podamos añadir datos de usuarios de Braze a Google Audiences para enviar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más.

Para acceder a la plantilla de comentarios posteriores a la compra, al crear un nuevo Canvas, selecciona **Utilizar una plantilla de Canvas** > **Plantillas de Braze**. A continuación, junto a **Comentarios posteriores a la compra**, selecciona **Aplicar plantilla**. Ahora, podemos repasar la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configurar los detalles de Canvas

Vamos a ajustar los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Editar** junto al nombre de la plantilla.

![El título actual y la descripción del Canvas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_edit_details.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Actualiza el nombre del Canvas para especificar que es para dirigirse a usuarios recientes.
3\. Actualiza la descripción para especificar que el Canvas sirve para animar a los usuarios a enviar sus opiniones.
4\. Añade la etiqueta **Feedback** para filtrarla en la página de inicio de Canvas.

![El nuevo nombre y descripción del Canvas. La nueva descripción dice 'Un Canvas de opinión posterior a la compra para medir el interés por la próxima expansión para PWD3, Liquid Mirage.']({% image_buster /assets/img/canvas_templates/post_purchase_feedback/enter_new_canvas_name.png %}){: style="max-width:50%;"}

### Paso 2: Asignar eventos de conversión

A continuación, vamos a asignar nuestros eventos de conversión. Actualiza el **evento de conversión primaria - A** para **Hacer una compra específica** y selecciona **Guerra de poderes**.

!["Asignar eventos de conversión" para el tipo de evento de conversión de la compra del producto del juego Proxy War.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/select_conversion_event.png %}){: style="max-width:90%;"}

Mantendremos el plazo de conversión de la plantilla en tres días porque queremos dirigirnos a nuestros usuarios más recientes.

### Paso 3: Establecer un horario de entrada

1. Mantén el tipo de horario de entrada como **Basado en acciones**.
2. Establece la **Hora de inicio** de la ventana de entrada en la fecha de lanzamiento del juego.

### Paso 4: Determina quién entra en el Canvas

Nuestra audiencia objetivo para los comentarios son los usuarios que han comprado recientemente Proxy War 3.

1. Selecciona nuestro segmento objetivo, "Comprado Proxy War 3", que consiste en usuarios que han comprado el juego.
2. Selecciona un filtro para incluir a los usuarios que hayan comprado "Proxy War 3" más de "0" veces.

![Un segmento denominado "Comprado Proxy War 3" que segmenta a los usuarios que han comprado el juego.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/entry_window_segment.png %}){: style="max-width:90%;"}

{: start="3"}
3\. Actualiza los controles de entrada para que no permitan a los usuarios volver a entrar en el Canvas después de la duración máxima del Canvas.

### Paso 5: Selecciona tu configuración de envío

Mantendremos la configuración predeterminada de suscripción, para que sólo enviemos a los usuarios que se hayan suscrito o hayan optado por recibir mensajes o notificaciones. 

Como queremos ser precavidos con nuestros envíos, seleccionaremos **Habilitar horas tranquilas** para evitar solicitar respuestas entre las 11 de la noche y las 10 de la mañana en la zona horaria de nuestros usuarios, y sólo enviaremos en la siguiente hora disponible.

![Paso "Configuración de envío" dirigido a usuarios suscritos o que han optado por la adhesión voluntaria. Se activan las horas tranquilas.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/send_settings_with_quiet_hours.png %}){: style="max-width:90%;"}

Para nuestro ejemplo, omitiremos las demás configuraciones (limitación de frecuencia y grupos semilla).

### Paso 6: Personaliza tu Canvas

A continuación, construiremos nuestro Canvas personalizando los canales de mensajería y el contenido que se enviará a los usuarios. Como sólo buscamos opiniones utilizando el correo electrónico, los mensajes dentro de la aplicación y los canales de webhook, revisaremos la plantilla y eliminaremos las variantes de SMS de los pasos de Mensaje.

Comenzaremos nuestra personalización pasando por cada componente de mensajería para actualizar el contenido. Nuestro atributo personalizado para hacer referencia es `Experience Feedback`.

1. En el constructor Canvas, selecciona el primer paso de Mensaje en el recorrido del usuario.
2. Selecciona la variante **Correo electrónico**.
3. Rellena la **Información de envío** con un asunto que fomente las opiniones de los usuarios. 
4. Selecciona **Editar mensaje** para sustituir el mensaje de correo electrónico de la plantilla por nuestro mensaje de encuesta de opinión. Esto incluye sustituir los enlaces de cada llamada a la acción para capturar qué opción se selecciona, a la que se hará referencia en el paso Ruta de acción de nuestro recorrido del usuario.

{% alert tip %}
Puedes utilizar [las propiedades de entrada del]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) Canvas para personalizar los mensajes de tu Canvas en función del producto al que te refieras.
{% endalert %}

#### Configurar cuestionario de opinión

A continuación, tendremos que rellenar los datos de la variante **Mensaje dentro de la aplicación**. Aquí es donde tenemos que especificar nuestro atributo personalizado `Experience Feedback` que indica el sentimiento de la opinión de nuestro usuario. (También haremos referencia a esto en el paso posterior Ruta de acción).

1. En el mismo primer paso de Mensajes, selecciona la variante **Mensajes dentro de la aplicación**. Mantendremos los controles de mensajes como están. 
2. Para el encabezamiento y el cuerpo, utilizaremos un lenguaje que anime a los usuarios a ser sinceros sobre su experiencia con Proxy War 3.
3. Como queremos que sus respuestas al cuestionario se registren con sus perfiles, mantendremos el cuestionario como **Selección de una sola opción** y **Registro de atributos al enviarlo**.
4. Para cada una de las tres opciones del cuestionario, selecciona **Opinión sobre la experiencia** como atributo personalizado. 
5. Mantendremos los valores de los atributos en el perfil de usuario tal como están, ya que estos valores se alinean con nuestro atributo personalizado.

![Un cuestionario que pregunta al usuario si le ha gustado su reciente compra de Proxy War 3 con tres opciones: "Me encantó", "Estuvo bien" y "No es para mí".]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/survey_example_iam.png %}){: style="max-width:90%;"}

#### Construye la ruta de acción

Utilizando nuestro atributo personalizado `Experience Feedback` y los valores de atributo de la sección anterior, actualizaremos la ruta de acción de la plantilla para que coincida con nuestro atributo y valores.

![El grupo de "Buenas opiniones" para el paso de la Ruta de acción que incluye a los usuarios que respondieron "Me encantó" a nuestro cuestionario.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/action_path_good_example.png %}){: style="max-width:90%;"}

### Configurar reorientación de anuncios

Nos aseguraremos de que nuestra sincronización con Google Audience esté configurada en nuestro paso de **Reorientación de anuncios**. Esto incluirá la selección de nuestra cuenta publicitaria, una audiencia existente y la opción de añadir usuarios a la audiencia.

### Configurar casos de soporte webhook

A continuación, vamos a configurar el webhook para desencadenar posibles casos de asistencia. Esto puede ser especialmente revelador en combinación con el análisis de las opiniones de nuestros usuarios.

Para el paso de mensajes denominado **Creación de casos de asistencia**, actualizaremos la plantilla para componer un webhook para los usuarios que no estén satisfechos con su compra y quieran un reembolso.

![Un webhook que crea casos de soporte para clientes que tienen un sentimiento negativo y quieren un reembolso por su compra de Proxy War 3.]({% image_buster /assets/img/canvas_templates/post_purchase_feedback/webhook_example.png %}){: style="max-width:90%;"}

### Paso 6: Prueba y lanza el Canvas

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como esperábamos, selecciona **Lanzar Canvas** para iniciar el Canvas. ¡Ahora podemos dirigirnos a los usuarios con un recorrido de usuario personalizado para animarles a responder a nuestro cuestionario de opinión basándonos en su reciente compra de Proxy War 3!

{% alert tip %}
Consulta nuestra [Lista de comprobación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber qué cosas debes tener en cuenta antes y después de lanzar un Canvas.
{% endalert %}
