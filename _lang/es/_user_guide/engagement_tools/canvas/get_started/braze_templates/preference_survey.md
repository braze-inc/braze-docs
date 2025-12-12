---
nav_title: Cuestionario de incorporación con preferencias
article_title: Cuestionario de incorporación con preferencias
page_order: 5.5
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de Braze Canvas para impulsar la adopción temprana con un flujo de incorporación guiado para presentar tu marca a los nuevos usuarios y recoger sus preferencias para mantener su interacción a largo plazo."
tool: Canvas
---

# Cuestionario de incorporación con preferencias

> Utiliza la plantilla de cuestionario de incorporación con preferencias para crear un flujo de trabajo guiado de incorporación dirigido a nuevos usuarios. Preséntales tu marca, ayúdales a empezar y recoge sus preferencias para mantener su interacción a largo plazo.

Este artículo te guiará a través de un caso de uso de la plantilla de **cuestionario Incorporación con preferencias**, que está diseñada para la etapa de consideración del ciclo de vida del usuario. Cuando hayas terminado, habrás creado un Canvas que envía correos electrónicos y mensajes dentro de la aplicación a los usuarios cuando inician una sesión y cuando no han completado su incorporación.

## Requisitos previos

Para utilizar correctamente esta plantilla, necesitarás lo siguiente:

- Un correo electrónico de bienvenida que pide a los usuarios que comiencen la incorporación.
- Un correo electrónico de seguimiento que incluye consejos para empezar a utilizar la aplicación para los usuarios que la incorporaron.
- Un correo electrónico de seguimiento para pedir a los usuarios que completen su incorporación.
- Un [cuestionario]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey) que contiene varias preguntas para determinar las preferencias del usuario.

## Adaptar la plantilla a tus necesidades

Digamos que trabajamos para StyleRyde, una aplicación de transporte compartido a la carta que lleva a la gente a donde necesita ir. Antes de crear el Canvas, creamos [un cuestionario sencillo]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog) que incluye una serie de preguntas atractivas para determinar la experiencia y la impresión del primer viaje de un usuario con la aplicación.

Para acceder a la plantilla, al crear un nuevo Canvas, selecciona **Utilizar una plantilla de Canvas** > **Plantillas de Braze**. A continuación, junto a **Cuestionario de incorporación con preferencias**, selecciona **Aplicar plantilla**. Ahora, podemos repasar la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configura los detalles

Vamos a ajustar los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Editar** junto al nombre de la plantilla.

\![El título actual y la descripción del Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey1.png %}){: style="max-width:50%;"}

{:start="2"}
2\. Actualiza el nombre del Canvas para especificar que es para dirigirse a nuevos usuarios cuando utilizan la aplicación por primera vez.
3\. Actualiza la descripción para explicar que este Canvas contiene mensajería personalizada.
4\. Añade la etiqueta **Incorporación** para que podamos filtrarla en la página de inicio de Canvas.

\![El nuevo nombre, descripción y etiqueta del Canvas.]({% image_buster /assets/img/canvas_templates/preference_survey2.png %}){: style="max-width:90%;"}

### Paso 2: Asignar eventos de conversión

Actualiza el **evento de conversión primaria - A** para **realizar un evento personalizado**. A continuación, selecciona **Última aplicación utilizada** para el evento personalizado.

\![Última aplicación utilizada como nombre del evento personalizado seleccionado para el evento de conversión.]({% image_buster /assets/img/canvas_templates/preference_survey3.png %}){: style="max-width:90%;"}

### Paso 3: Adapta el horario de entrada

Mantengamos el horario de entrada como **Basado en acciones** para que los usuarios entren en nuestro Canvas cuando inicien una sesión en la aplicación. De este modo, podemos empezar a establecer relaciones con una interacción oportuna.

Haremos una actualización en esta sección ajustando la **Ventana de Entrada** a la fecha y hora que deseemos.

\!["Ventana de entrada" sección con la hora de inicio 30 de enero de 2025 a las 12 pm.]({% image_buster /assets/img/canvas_templates/preference_survey4.png %}){: style="max-width:90%;"}

### Paso 4: Selecciona la audiencia objetivo

Mantendremos la audiencia objetivo tal cual para dirigirnos a nuestros usuarios que utilizaron por primera vez la aplicación StyleRyde hace menos de un día.

\![El filtro "Utilizó por primera vez estas aplicaciones hace menos de 1 día" seleccionado para dirigirse a la audiencia de entrada.]({% image_buster /assets/img/canvas_templates/preference_survey5.png %}){: style="max-width:90%;"}

### Paso 5: Selecciona tu configuración de envío

Mantendremos la configuración predeterminada de la suscripción, de modo que sólo enviemos a los usuarios que se hayan suscrito o hayan optado por recibir mensajes o notificaciones con las horas tranquilas activadas, y omitiremos las demás configuraciones (limitación de frecuencia y grupos de semilla).

\!["Configuración de envío" sección con la configuración de suscripción para usuarios suscritos o con adhesión voluntaria con las horas tranquilas activadas entre las 12 de la mañana y las 8 de la tarde.]({% image_buster /assets/img/canvas_templates/preference_survey6.png %}){: style="max-width:90%;"}

### Paso 6: Personaliza tu Canvas

Ahora, construiremos nuestro Canvas personalizando el contenido que se enviará a los usuarios. 

1. Para el primer paso Mensaje **de correo electrónico de bienvenida**, actualizaremos este paso para incluir nuestro correo electrónico de bienvenida de StyleRyde.
2. A continuación, mantendremos el paso Ruta de acción tal como está. Este paso divide a nuestros usuarios en dos grupos en una ventana de tres días:

- Usuarios que han iniciado una sesión o han hecho clic en el correo electrónico de incorporación
- Usuarios que no han iniciado sesión o no han hecho clic en el correo electrónico de incorporación

\![Un paso de Ruta de acción dividido en dos rutas, una para los usuarios que han iniciado una sesión y otra para todos los demás.]({% image_buster /assets/img/canvas_templates/preference_survey8.png %}){: style="max-width:50%;"}

A partir de aquí, orientaremos a nuestros usuarios y la mensajería en función de los grupos mencionados.

#### Dirígete a tus usuarios comprometidos

Para nuestros usuarios que han iniciado una sesión o han interactuado con nuestro correo electrónico de incorporación desde el primer paso Mensaje, actualizaremos el paso Mensaje de **consejos de incorporación** para incluir los consejos esenciales de viaje y seguridad para nuestros nuevos usuarios de StyleRyde.

Cuando un usuario haya completado su incorporación, saldrá del Canvas.

A continuación, actualiza el paso Mensaje de **la encuesta de preferencias de contenido** para incluir nuestro cuestionario de preferencias que pide a nuestros usuarios que seleccionen los temas sobre los que están interesados en recibir información en el futuro.

\![Una vista previa del cuestionario de preferencias que pide a los usuarios que seleccionen todos los intereses que correspondan.]({% image_buster /assets/img/canvas_templates/preference_survey7.png %}){: style="max-width:90%;"}

#### Dar un codazo a los usuarios que no han empezado la incorporación 

Para el resto de nuestros usuarios, actualizaremos el paso **Winback Nudge** Message con nuestro correo electrónico de seguimiento para pedir a los usuarios que completen su incorporación.

Como último paso para la reactivación de la interacción, cambiaremos el nombre del **paso 2** por el de **"codazo final de vuelta"** y actualizaremos el paso con nuestro mensaje dentro de la aplicación para pedir a nuestros nuevos usuarios que completen su incorporación.

### Paso 7: Prueba y lanza tu Canvas

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como esperamos, lo lanzaremos seleccionando **Lanzar Canvas**.

{% alert tip %}
Consulta nuestra [Lista de comprobación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber qué cosas debes tener en cuenta antes y después de lanzar un Canvas.
{% endalert %}