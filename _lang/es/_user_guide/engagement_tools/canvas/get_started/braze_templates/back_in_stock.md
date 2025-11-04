---
nav_title: De nuevo en stock
article_title: De nuevo en stock
page_order: 2
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de Braze Canvas para impulsar las compras notificando a tus usuarios cuando un artículo vuelve a estar disponible con mensajes personalizados."
tool: Canvas
---

# De nuevo en stock

> Utiliza la plantilla de nuevo en stock para crear mensajes dirigidos a usuarios que hayan visto previamente o expresado interés por un artículo que estaba agotado pero que ahora está disponible para su compra. Esto ayuda a los usuarios a obtener los productos que desean, interactuando con ellos en el momento crítico en que un producto vuelve a estar disponible.

Este artículo te guiará a través de un caso de uso de la plantilla **Volver a existencias**, que está diseñada para el paso de conversión del ciclo de vida del usuario. Cuando hayas terminado, habrás creado un Canvas que envía un push (Web o móvil), SMS o correo electrónico a los usuarios cuando un artículo vuelve a estar disponible, y hasta dos recordatorios.

## Requisitos previos

Para utilizar correctamente esta plantilla, necesitarás lo siguiente:

- Un [catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) con información sobre tu artículo
- [Las notificaciones de reposición de existencias]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work) deben estar configuradas para el artículo sobre el que quieres enviar mensajes a los usuarios

## Adaptar la plantilla a tus necesidades

Digamos que trabajamos para PantsLabyrinth, un comercio minorista de ropa directa al consumidor especializado en pantalones, vaqueros, culottes y muchos otros tipos de pantalones. Podemos utilizar la plantilla de nuevo en stock para notificar a los clientes en varios canales que un popular par de vaqueros, los Classic Straight Leg, vuelven a estar en stock.

Antes de crear el Canvas, [configuramos un catálogo]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) que contiene información sobre nuestro inventario de pantalones de pierna recta y [configuramos las notificaciones de agotado]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications) para los vaqueros de pierna recta clásicos. Hemos hecho que los usuarios se suscriban a las notificaciones después de realizar el evento personalizado de marcar como favoritos los vaqueros Classic Straight Leg en la aplicación.

Para acceder a la plantilla de reserva, al crear un nuevo Canvas, selecciona **Utilizar una plantilla de Canvas** > **Plantillas de Braze**. Luego, junto a **Volver a existencias**, selecciona **Aplicar plantilla**. Ahora, podemos repasar la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configura los detalles

Vamos a ajustar los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Editar** junto al nombre de la plantilla.

\![El título actual y la descripción del Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Actualiza el nombre del Canvas para especificar que el Canvas es para dirigirse a los usuarios cuando nuestro producto Pierna recta clásica vuelva a estar en stock.
3\. Actualiza la descripción para explicar que este Canvas contiene mensajería personalizada.
4\. Añade la etiqueta **Disponible**, que está anidada bajo la etiqueta **Promocional**, para que podamos filtrarla en la página de inicio de Canvas. 

\!["Configurar los detalles del Canvas" paso con un nombre de Canvas "De nuevo en stock - Pierna recta clásica" y una breve descripción del Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})

### Paso 2: Asignar eventos de conversión

Cambia el **evento de conversión primaria - A** a **Hacer una compra específica** y selecciona **Pierna recta clásica** para el nombre del producto.

\!["Asignar eventos de conversión" para el tipo de evento de conversión de compra del producto Pierna recta clásica con un plazo de conversión de 7 días.]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})

### Paso 3: Adapta el horario de entrada

Mantengamos el horario de entrada como **Basado en acciones** para que los usuarios entren en nuestro Canvas cuando realicen una acción, que la plantilla ya tiene configurada como **Realizar un evento de reposición**.

Haremos dos ajustes en este paso:

1. Selecciona el catálogo que incluye información sobre nuestros vaqueros clásicos de pierna recta, que hemos denominado "Pantalones de pierna recta". 

\!["Horario de entrada" paso para un Canvas basado en acciones.]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})

{: start="2"}
2\. Ajusta la **Hora de inicio (Obligatorio** ) a la fecha y hora de inicio que desees.

\!["Ventana de entrada" sección con hora de inicio el 2 de enero de 2025 a las 12 de la mañana.]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})

### Paso 4: Selecciona la audiencia objetivo

Definiremos nuestra audiencia objetivo como los usuarios que pensamos que tienen más probabilidades de comprar los vaqueros Classic Straight Leg.

1. Selecciona nuestro segmento objetivo, "Favoritos - Vaqueros clásicos de pata recta", que consiste en usuarios que han dado "Favoritos" a nuestros vaqueros clásicos de pata recta en nuestra aplicación o sitio web.
2. Selecciona un filtro para incluir a los usuarios que hayan comprado "Vaqueros" más de "0" veces.

\!["Audiencia objetivo" paso con el segmento de "Favoritos - Vaqueros clásicos de pierna recta".]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})

{: start="3"}
3\. Adjust the entry controls to allow users to re-enter the Canvas after the Canvas's maximum duration, to prevent the likelihood of users triggering the same step concurrently.

\!["Controles de entrada" sección con una casilla de verificación para permitir a los usuarios volver a entrar en este Canvas con una duración máxima del Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})

{: start="4"}
4\. Ajusta los criterios de salida para eliminar a los usuarios que realizaron el evento personalizado de desfavorecer los vaqueros Classic Straight Leg.

\!["Criterios de salida" con una excepción para los usuarios que realicen el evento personalizado de "Desfavorito".]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})

### Paso 5: Selecciona tu configuración de envío

Mantendremos la configuración predeterminada de la suscripción, de modo que sólo enviemos a los usuarios que se hayan suscrito o hayan optado por recibir mensajes o notificaciones, y omitiremos las demás configuraciones (limitación de frecuencia, horas tranquilas y grupos de semilla).

\!["Enviar configuración" paso dirigido a usuarios suscritos o con adhesión voluntaria.]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})

### Paso 6: Personaliza tu Canvas

Ahora, construiremos nuestro Canvas personalizando los canales y el contenido que enviaremos a los usuarios. Como estamos utilizando los cuatro canales de la plantilla (push móvil y Web, SMS y correo electrónico) y usando el filtro [Canal inteligente]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/), no necesitamos añadir ni eliminar ninguno.

{% alert tip %}
Puedes utilizar [las propiedades de entrada del]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/) Canvas para personalizar los mensajes de tu Canvas en función del producto al que te refieras.
{% endalert %}

Comenzaremos nuestra personalización pasando por cada paso de Mensaje para actualizar el contenido.

1. Sustituye `!!YOURCATALOGHERE!!` por el nombre de nuestro catálogo (“Straight_Leg_Pants”).
2. Sustituye `[0]` por el número de índice de los vaqueros Classic Straight Leg, que es "9" porque los vaqueros son el décimo artículo de la matriz `items` de nuestro catálogo. (Las matrices tienen índice cero en Liquid, por lo que el primer elemento es `0` y no `1`.)
3. Repite los pasos 1 y 2 para todos los pasos de Mensajes restantes, incluyendo:
    - El mensaje "In-Product Msg & Correo electrónico" que se envía tras el retraso de un día
    - Los mensajes de "Alerta Push+Email" que se envían a los usuarios que no han realizado una compra
4. Actualiza el paso Rutas de acción seleccionando el grupo de acciones **Comprar**. A continuación, selecciona **Hacer una compra específica** y elige Vaqueros clásicos de pierna recta como producto.

\![Paso en Canvas de push móvil con un mensaje que notifica a los usuarios que un producto vuelve a estar disponible.]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})

### Paso 7: Prueba y lanza tu Canvas

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como esperamos, lo lanzaremos seleccionando **Lanzar Canvas**. Ahora, nuestros usuarios que hayan dado un favorito a nuestros vaqueros Classic Straight Leg y se hayan suscrito a nuestros canales de mensajería, ¡recibirán notificaciones cuando vuelvan a estar disponibles!

{% alert tip %}
Consulta nuestra [Lista de comprobación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber qué cosas debes tener en cuenta antes y después de lanzar un Canvas.
{% endalert %}

