---
nav_title: Carrito abandonado
article_title: Carrito abandonado
page_order: 1
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de Braze Canvas para interactuar con los usuarios en tiempo real y animarles a completar sus compras."
tool: Canvas
---

# Carrito abandonado

> Interactúa con los usuarios en tiempo real para animarles a completar sus compras. Utiliza esta plantilla para crear un recorrido del usuario centrado en el envío de mensajes oportunos y personalizados que recuerden a los usuarios sus carritos abandonados, destacando las ventajas del producto y ofreciendo incentivos, como códigos de descuento.

En este artículo, te guiaremos a través de un caso de uso de la plantilla **Intención Abandonada**, que está pensada para la etapa de consideración del ciclo de vida del usuario. Después de este artículo, habrás personalizado un recorrido de usuario que anima a comprar a los usuarios que no lo han hecho después de añadir artículos a sus carritos.

## Requisitos previos

Para utilizar correctamente esta plantilla, necesitarás lo siguiente:

- Un Canvas de recorrido del usuario posterior a la compra separado, ya que realizar una compra en este Canvas hará que los usuarios salgan del Canvas.
- Una [Sincronización de Audiencias Braze]({{site.baseurl}}/partners/canvas_audience_sync/) configurada con los socios y audiencias que utilices.

## Adaptar la plantilla a tus necesidades

Supongamos que trabajamos en Kitchenerie, una marca de comercio minorista especializada en utensilios de cocina, y nuestro objetivo es volver a captar a los usuarios que han añadido el último producto "Plato de papel enorme" a sus carritos, pero no han realizado sus compras.

Antes de crear el Canvas, configuramos la integración de [Braze Audience Sync con Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) para que podamos añadir datos de usuarios de Braze a Facebook Audiences para enviar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más.

Para acceder a la plantilla de intención abandonada, al crear un nuevo Canvas, selecciona **Utilizar una plantilla de Canvas** > **Plantillas de Braze**. A continuación, junto a **Intención abandonada**, selecciona **Aplicar plantilla**. Ahora, podemos repasar la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configura los detalles

Vamos a ajustar los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Editar** junto al nombre de la plantilla.

\![El título actual y la descripción del Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_old_name_description.png %}){: style="max-width:60%;"}

{:start="2"}
2\. Actualiza el nombre del Canvas para especificar que el Canvas es para dirigirse a usuarios con carritos abandonados.
3\. Actualiza la descripción para especificar que el Canvas sirve para animar a los usuarios a completar las compras del último lanzamiento de menaje de temporada.
4\. Añade la etiqueta **Abandonar carrito** para que podamos filtrarla en la página de inicio de Canvas.

\![El nuevo nombre, descripción y etiqueta del Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent_new_name_description.png %}){: style="max-width:60%;"}

### Paso 2: Asigna tus eventos de conversión

A continuación, vamos a asignar nuestro evento de conversión. Como nos centramos en nuestro producto "Plato de papel enorme", haremos lo siguiente para **el evento de conversión primaria A**:

1. Para el **tipo de evento de conversión**, selecciona **Realiza compra**.
2. Selecciona **Hacer una compra específica**. Esto nos permite seleccionar un nombre de producto concreto.
3. Selecciona **Plato de Papel Enorme**.

\![Evento de conversión primaria - A con el tipo de conversión "Realiza compra" con el nombre de producto "Enorme plato de papel". Hay un plazo de conversión de 3 días.]({% image_buster /assets/img/canvas_templates/abandoned_intent1.png %})

### Paso 3: Establecer un horario de entrada

Aunque el programa de entrada de esta plantilla está configurado como **Activado por API**, nuestro caso de uso se beneficiará más de tener una entrada basada en acciones para este Canvas, ya que queremos centrarnos en los usuarios que han abandonado su carrito (que es una acción).

1. Selecciona **Basado en acciones** como tipo de horario de entrada.
2. Selecciona **Carrito Abandonado** como desencadenante.
3. Para la ventana de entrada, selecciona la fecha de la hora de inicio.
4. Selecciona la opción que permite a los usuarios introducir su zona horaria local. Esto puede mantener la relevancia de nuestros mensajes y conseguir una mayor interacción si los mensajes se envían en momentos óptimos.

\![Un Canvas basado en acciones que se dirige a los usuarios que han abandonado su carrito, con la ventana de entrada 15 de octubre de 2024 15:20 h en la zona horaria local de los usuarios.]({% image_buster /assets/img/canvas_templates/abandoned_intent2.png %})

### Paso 4: Determina quién entra en el Canvas

A continuación, definamos nuestra audiencia objetivo como usuarios que han comprado exclusivamente en línea con nosotros en los últimos 90 días. Esto nos ayuda a limitar nuestra audiencia a los usuarios que sabemos que tienen interacción con nuestros productos. 

\!["Segmento de compradores en línea - 90 días" como segmento de usuarios al que dirigirse para este Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent3.png %})

Dejaremos los controles de entrada como están, para que los usuarios no puedan volver a entrar en este Canvas y no haya límite en el número de personas que potencialmente pueden entrar en este Canvas.

Para los criterios de salida, los usuarios saldrán del Canvas si han comprado el "Plato de Papel Enorme". De este modo, no recibirán más mensajes sobre un artículo que ya han comprado.

\![Criterios de salida que determinan que los usuarios que realicen una compra específica para el enorme plato de papel saldrán del Canvas.]({% image_buster /assets/img/canvas_templates/abandoned_intent4.png %})

### Paso 5: Selecciona tu configuración de envío

Mantendremos la configuración predeterminada de la suscripción, para que sólo enviemos a los usuarios que se hayan suscrito o hayan optado por recibir mensajes o notificaciones, y dejaremos las demás configuraciones como están.

### Paso 6: Personaliza tu Canvas

Ahora, construiremos nuestro Canvas personalizando los pasos de la plantilla:

1. Selecciona el paso Rutas de acción y, a continuación, el nombre del grupo de acción **Compras realizadas**.
2. Para **Hacer una compra**, selecciona **Hacer una compra específica** y elige **Plato de papel enorme** para el producto. De forma similar a los criterios de salida, los usuarios que compren este producto saldrán del Canvas.

\!["Hecho compra" grupo de acciones que saldrá del Canvas si el usuario compra el enorme plato de papel.]({% image_buster /assets/img/canvas_templates/abandoned_intent5.png %})

{: start="3"}
3\. En el paso Mensaje, selecciona **Editar mensaje** para personalizar el correo electrónico que se enviará a nuestros usuarios, notificándoles los artículos de su carrito abandonado.
4\. Mantén el paso Retraso como está.
5\. En los pasos de Mensaje posteriores al paso de Ruta de audiencia, personalizaremos el correo electrónico y el mensaje SMS que recibirán nuestros usuarios. Aquí es donde queremos animar a nuestros usuarios a comprar productos con mensajes personalizados.

Vista previa del mensaje SMS que recibirán los usuarios: "¡Hola, te has dejado el enorme plato de papel en el carrito! Completa tu compra ahora e intensifica tu juego de alojamiento. Utiliza el código MYPLATE al pasar por caja para obtener un 20% de descuento en tu pedido!"]({% image_buster /assets/img/canvas_templates/abandoned_intent6.png %})

{: start="6"}
6\. En el siguiente paso Rutas de acción, selecciona el grupo de acciones **Hecho compra**. A continuación, selecciona **Hacer una compra específica** y elige **Enorme plato de papel** como producto. Este paso reflejará el primer paso de las Rutas de acción saliendo de los usuarios que hayan comprado nuestro producto para que no reciban más mensajería.
7\. Asegúrate de que nuestro paso Sincronización de audiencia está configurado para sincronizarse con Facebook. Esto ayudará aún más a reorientar los anuncios.

{% alert tip %}
Puedes utilizar [las propiedades de entrada del]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) Canvas para personalizar los mensajes de tu Canvas en función del producto al que te refieras.
{% endalert %}

### Paso 7: Prueba y lanza el Canvas

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como esperábamos, selecciona **Lanzar Canvas** para iniciar el Canvas. Ahora podemos dirigirnos a los usuarios con un recorrido personalizado para animarles a comprar el producto que han añadido a sus carritos.

{% alert tip %}
Consulta nuestra [Lista de comprobación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber qué cosas debes tener en cuenta antes y después de lanzar un Canvas.
{% endalert %}

