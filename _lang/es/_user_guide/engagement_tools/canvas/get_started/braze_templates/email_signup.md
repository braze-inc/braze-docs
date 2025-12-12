---
nav_title: Registro por correo electrónico con doble adhesión voluntaria
article_title: Registro por correo electrónico con doble adhesión voluntaria
page_order: 2
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de Braze Canvas para ampliar tu alcance con registros por correo electrónico verificados."
tool: Canvas
---

# Registro por correo electrónico con doble adhesión voluntaria

> Utiliza la plantilla de registro por correo electrónico con doble adhesión voluntaria para ampliar tu alcance con adhesiones por correo electrónico verificadas. Dirígete a nuevos usuarios para captar su correo electrónico, confirmar su suscripción y recibir un código promocional, todo en un solo viaje sin interrupciones.

Este artículo te guiará a través de un caso de uso para la plantilla de **registro por correo electrónico con doble adhesión voluntaria**, que está diseñada para la fase de consideración del ciclo de vida del usuario. Cuando hayas terminado, habrás creado un Canvas que envía correos electrónicos y mensajes dentro de la aplicación a los usuarios cuando inician una sesión o cuando no han completado su incorporación.

## Requisitos previos

Para utilizar correctamente esta plantilla, necesitarás lo siguiente:

- Un [mensaje dentro de la aplicación con varias páginas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page), una para captar los correos electrónicos de tus usuarios y otra para comunicar un mensaje de éxito.
- Un correo electrónico de confirmación para que los usuarios verifiquen su dirección de correo electrónico.
- Un correo electrónico de bienvenida con un código promocional exclusivo para los usuarios que hagan doble adhesión voluntaria.

## Adaptar la plantilla a tus necesidades

Digamos que trabajamos para Steppington, una aplicación de salud conocida por sus características como el seguimiento de calorías, las clases digitales de ejercicio y los maratones flash-mob. Antes de crear el Canvas, [configuramos mensajes dentro de la aplicación y en el explorador de varias páginas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page) que incluían una serie de preguntas atractivas para determinar la experiencia y la impresión del primer viaje de un usuario con la aplicación.

Para acceder a la plantilla, al crear un nuevo Canvas, selecciona **Utilizar una plantilla de Canvas** > **Plantillas de Braze**. A continuación, junto a **Registro por correo electrónico con doble adhesión voluntaria**, selecciona **Aplicar plantilla**. Ahora, podemos repasar la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configura los detalles

Vamos a ajustar los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Editar** junto al nombre de la plantilla.

\![El título actual y la descripción del Canvas.]({% image_buster /assets/img/canvas_templates/email_signup1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Actualiza el nombre del Canvas para especificar que es para dirigirse a nuevos usuarios cuando utilizan la aplicación por primera vez.
3\. Actualiza la descripción para explicar que este Canvas contiene mensajería personalizada para que los usuarios realicen una doble adhesión voluntaria.
4\. Añade la etiqueta **Correo electrónico** para que podamos filtrarlo en la página de inicio de Canvas.

\![El nuevo nombre, descripción y etiqueta del Canvas.]({% image_buster /assets/img/canvas_templates/email_signup2.png %}){: style="max-width:90%;"}

### Paso 2: Asignar eventos de conversión

A continuación, vamos a asignar nuestros eventos de conversión. Los eventos de conversión son un tipo de métrica que puede utilizarse para medir el éxito del Canvas. Para el **tipo de evento de conversión**, selecciona **Realiza evento personalizado**. A continuación, selecciona **email_opt_in** para el **nombre del evento personalizado**.

\!["Asignar eventos de conversión" sección para el tipo de evento de conversión de adhesión voluntaria por correo electrónico.]({% image_buster /assets/img/canvas_templates/email_signup3.png %}){: style="max-width:90%;"}

Mantendremos el plazo de conversión de la plantilla en tres días porque queremos dirigirnos a nuestros usuarios más recientes.

### Paso 3: Adapta el horario de entrada

Mantengamos el horario de entrada como **Basado en acciones** para que los usuarios entren en nuestro Canvas cuando inicien una sesión en la aplicación. De este modo, podemos empezar a establecer relaciones con una interacción oportuna.

También mantendremos las **Opciones basadas en la acción** tal como están, para que los usuarios sólo entren en el Canvas cuando inicien una sesión.

\![Un programa de entrada basado en acciones para introducir en el Canvas a los usuarios que inician cualquier sesión.]({% image_buster /assets/img/canvas_templates/email_signup4.png %}){: style="max-width:90%;"}

Para la **Ventana de entrada**, actualizaremos la **Hora de inicio (Obligatorio** ) a la fecha y hora que deseemos.

Una ventana de entrada con hora de inicio el 16 de enero de 2025 a las 12:30 h. Los usuarios introducirán este mensaje en su zona horaria local.]({% image_buster /assets/img/canvas_templates/email_signup5.png %}){: style="max-width:90%;"}

### Paso 4: Selecciona la audiencia objetivo

Definiremos nuestra audiencia objetivo como usuarios de Steppington que no tienen una dirección de correo electrónico en su perfil de usuario. Lo haremos manteniendo el [filtro de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) predeterminado de la plantilla `Email Available is false`.

\![Audiencia de entrada con el filtro "Correo electrónico disponible es falso".]({% image_buster /assets/img/canvas_templates/email_signup6.png %}){: style="max-width:90%;"}

### Paso 5: Selecciona tu configuración de envío

Mantendremos la configuración predeterminada de la suscripción, de modo que sólo enviemos a los usuarios que se hayan suscrito o hayan optado por recibir mensajes o notificaciones, y omitiremos las demás configuraciones (limitación de frecuencia, horas tranquilas y grupos de semilla).

\![Opciones de envío predeterminadas para enviar sólo a usuarios suscritos o con adhesión voluntaria.]({% image_buster /assets/img/canvas_templates/email_signup7.png %}){: style="max-width:90%;"}

### Paso 6: Personaliza tu Canvas

Ahora, construiremos nuestro Canvas personalizando los canales y el contenido que enviaremos a los usuarios. Como nos estamos centrando en verificar nuestros registros por correo electrónico, no necesitamos añadir ni eliminar ninguno de los pasos en Canvas y canales de la plantilla.

1. Selecciona el primer paso de Mensajes llamado **Registrarse por correo electrónico**. Aquí es donde actualizaremos la plantilla para utilizar nuestro mensaje multipágina dentro de la aplicación (y en el explorador).

- La página 1 capturará los correos electrónicos.
- La página 2 mostrará un mensaje de confirmación.

Dos páginas de un mensaje dentro de la aplicación para capturar correos electrónicos de usuarios y mostrar un mensaje de éxito.]({% image_buster /assets/img/canvas_templates/email_signup8.png %}){: style="max-width:90%;"}

{:start="2"}
2\. A partir de aquí, mantendremos el paso Ruta de acción **suscrita** tal como está. Este paso divide a nuestros usuarios en dos grupos en una ventana de un día:

- Usuarios suscritos a Steppington con su correo electrónico
- Usuarios que no se han suscrito a Steppington con su correo electrónico

{:start="3"}
3\. A continuación, sustituye el cuerpo del correo electrónico por nuestro correo electrónico de confirmación de marca para el paso **Verificar** mensaje de **correo** electrónico. Esto enviará un correo electrónico a nuestros usuarios suscritos y les pedirá que confirmen su dirección de correo electrónico y que se suscriban a nuestra mensajería.
4\. Mantén el paso **Confirmar** ruta de acción de suscripción como está. Este paso divide aún más a nuestros usuarios entre los que han confirmado su correo electrónico y los que no lo han hecho, con un plazo de una semana.
5\. Por último, actualiza el paso Mensaje de **bienvenida + descuento** con nuestro correo electrónico de confirmación que incluye un código promocional exclusivo.  

### Paso 7: Prueba y lanza tu Canvas

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como esperamos, lo lanzaremos seleccionando **Lanzar Canvas**.

{% alert tip %}
Consulta nuestra [Lista de comprobación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber qué cosas debes tener en cuenta antes y después de lanzar un Canvas.
{% endalert %}