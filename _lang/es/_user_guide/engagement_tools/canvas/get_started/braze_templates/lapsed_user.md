---
nav_title: Usuario caducado
article_title: Usuario caducado
page_order: 4
page_type: reference
description: "Este artículo describe cómo utilizar una plantilla de Braze Canvas para hacer que los usuarios vuelvan a tu aplicación con incentivos basados en sus interacciones anteriores."
tool: Canvas
---

# Usuario caducado

> Utiliza la plantilla de usuario caducado para recordar a los usuarios el valor que tu marca les aporta, y anímales a volver con ofertas e incentivos interesantes basados en sus interacciones anteriores.

Este artículo te guiará a través de un caso de uso de la plantilla **Usuario caducado**, que está diseñada para la etapa de retención y fidelización del ciclo de vida del usuario. Cuando hayas terminado, habrás creado un Canvas que anima a los usuarios a volver a tu aplicación con promociones que varían en función de su comportamiento, como por ejemplo si iniciaron una sesión en tu aplicación después de recibir un mensaje promocional.

## Requisitos previos

Para utilizar correctamente la plantilla de usuario caducado, tienes que configurar [Braze Audience Sync]({{site.baseurl}}/partners/canvas_audience_sync/) con los socios y audiencias que utilices.

## Adaptar la plantilla a tus necesidades

Supongamos que trabajamos para MovieCanon, un servicio de streaming que tiene contenidos exclusivos de películas y series. Podemos utilizar la plantilla de usuario caducado para promocionar ventajas y contenido premium para usuarios que no han visitado nuestra aplicación en 30 días.

Antes de crear el Canvas, configuramos la integración de [Braze Audience Sync con Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/), de modo que podamos añadir datos de usuarios de Braze a Google Audiences para enviar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más.

Para acceder a la plantilla de usuario lapsing, al crear un nuevo Canvas, selecciona **Utilizar una plantilla de Canvas** > **Plantillas de Braze**. A continuación, junto a **Usuario Lapsing**, selecciona **Aplicar plantilla**. Ahora, podemos repasar la plantilla para adaptarla a nuestras necesidades.

### Paso 1: Configura los detalles 

Vamos a ajustar los detalles del Canvas para reflejar nuestro objetivo.

1. Selecciona **Editar** junto al nombre de la plantilla.

![El título actual y la descripción del Canvas.]({% image_buster /assets/img/canvas_templates/lapsed_user_old_name_description.png %}){: style="max-width:45%;"}

{:start="2"}
2\. Actualiza el nombre del Canvas para especificar que este Canvas enviará mensajes a los usuarios con promociones y realizará una sincronización de audiencias para aquellos que inicien una sesión.
3\. Actualiza la descripción para explicar que este Canvas contiene ventajas y promociones.
4\. Añade la etiqueta **Lapsing/Retención** para poder filtrar este Canvas en la página de inicio de Canvas.

!["Configurar detalles en Canvas" paso con el nombre en Canvas de "Usuario caducado - Visitar aplicación" y una breve descripción en Canvas]({% image_buster /assets/img/canvas_templates/lapsing_user_1.png %})

### Paso 2: Asigna tus eventos de conversión

Actualiza el **evento de conversión primaria** **\- A** para que se dirija a los usuarios de nuestra aplicación (MovieCanon), y deja el **evento de conversión primaria - B** como predeterminado para realizar cualquier compra.

![Sección "Asignar eventos de conversión" con un evento de conversión primaria de un usuario que inicia una sesión en una aplicación específica.]({% image_buster /assets/img/canvas_templates/lapsing_user_2.png %})

### Paso 3: Adapta el horario de entrada

Mantengamos el horario de entrada como **Programado** y las opciones predeterminadas basadas en el tiempo, para que el Canvas compruebe diariamente si hay usuarios caducados.

Haremos dos ajustes en este paso: 

1. Selecciona una fecha y hora de inicio.
2. Selecciona los parámetros de finalización de **En una fecha concreta** y una fecha a dos meses vista. Supongamos que tenemos otro Canvas de usuario caducado que queremos iniciar después de éste.

!["Paso en Canvas programado para la entrada de usuarios a una hora determinada.]({% image_buster /assets/img/canvas_templates/lapsing_user_3.png %})

### Paso 4: Selecciona nuestra audiencia objetivo

Mantendremos la configuración predeterminada para la audiencia de entrada, que se establece en usuarios que no han utilizado nuestra aplicación en más de 30 días. También mantendremos los controles de entrada predeterminados para que los usuarios puedan volver a entrar en el Canvas después de cuatro semanas. Esto significa que cada vez que un usuario no visite nuestra aplicación durante más de 30 días seguidos, entrará en el Canvas.

!["Audiencia objetivo" paso dirigido a los usuarios que utilizaron la aplicación por última vez en 30 días.]({% image_buster /assets/img/canvas_templates/lapsing_user_4.png %})

### Paso 5: Selecciona tu configuración de envío

Mantendremos la mayoría de las configuraciones de suscripción predeterminadas:

- Sólo se envía a los usuarios que se han suscrito o han optado por recibir mensajes o notificaciones.
- Aplica nuestras [reglas de limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) para no abrumar a nuestra audiencia con la cantidad de mensajes que recibe. En este caso, configuramos nuestra limitación de frecuencia para limitar a dos por semana el número de campañas o pasos en Canvas etiquetados con "Lapsing/Retención" que puede recibir un usuario.
- No envíes mensajes durante horas tranquilas en la hora local del usuario (de 12 a 8 de la mañana).

La única configuración que cambiaremos es qué hacer cuando se desencadena un mensaje durante las horas tranquilas. En lugar de cancelar el mensaje, selecciona **Enviar a la próxima hora disponible** para que nuestros usuarios no se pierdan ninguna promoción.

![Sección "Horas tranquilas" con hora de inicio a las 12 h y hora de finalización a las 8 h.]({% image_buster /assets/img/canvas_templates/lapsing_user_5.png %})

### Paso 6: Personaliza tu Canvas

Ahora, construiremos nuestro Canvas personalizando los pasos de la plantilla:

1. Personaliza el primer correo electrónico que se enviará a todos los usuarios que no hayan visitado nuestra aplicación en más de 30 días. Para nuestro caso de uso, personalizaremos un correo electrónico que informe a los usuarios de que desbloquearán nuevas ventajas cuando visiten hoy nuestra aplicación. 

![Paso en Canvas Mensaje para un correo electrónico que indica a los usuarios que desbloqueen nuevas ventajas cuando lo visiten hoy.]({% image_buster /assets/img/canvas_templates/lapsing_user_6.png %})

{: start="2"}
2\. Personaliza el componente de la ruta de acción llamado "¿Iniciar sesión?" seleccionando nuestra aplicación para la ruta **Sesión iniciada**. 

![Ruta de acción para las sesiones que se inician en una aplicación específica.]({% image_buster /assets/img/canvas_templates/lapsing_user_7.png %})

{: start="3"}
3\. Mantén el predeterminado para el paso para la división de decisiones llamado "¿Sesiones?", que define el grupo ">1 Sesión" como usuarios que han utilizado nuestra aplicación más de una vez en el último día del calendario.
4\. Personaliza el paso Mensaje para los usuarios que pertenezcan al grupo ">1 Sesión". En nuestro caso de uso, daremos las gracias a los usuarios por visitar nuestra aplicación y destacaremos las ventajas que han desbloqueado.
5\. Asegúrate de que nuestra sincronización con Google Audience está configurada en el paso Actualizar audiencia de anuncios, para que actualicemos y sincronicemos los datos de usuario de los usuarios que tuvieron varias sesiones después de recibir nuestro primer correo electrónico.
6\. Mantén predeterminado el componente [Ruta de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) llamado "Prueba A/B". Esto enviará aleatoriamente una de las dos promociones (que personalizaremos en el siguiente paso) a los usuarios que hayan tenido menos de dos sesiones.
7\. Personaliza las dos promociones que se enviarán a los usuarios como parte de la Ruta de experimentos. En nuestro caso de uso, haremos que una sea una promoción del 20% para una suscripción de tres meses y la otra una promoción del 10% para una suscripción de un mes.

![Pasos en Canvas con rutas de ramificación basadas en cuántas sesiones ha tenido un usuario.]({% image_buster /assets/img/canvas_templates/lapsing_user_8.png %}){: style="max-width:70%;"}

### Paso 7: Prueba y lanza el Canvas

Después de probar y revisar nuestro Canvas para asegurarnos de que funciona como esperamos, lo lanzaremos seleccionando **Lanzar Canvas**. Ahora nuestros usuarios que no hayan visitado nuestra aplicación en más de 30 días y se hayan suscrito a nuestros canales de mensajería, ¡recibirán correos electrónicos animándoles a volver!

{% alert tip %}
Consulta nuestra [Lista de comprobación previa y posterior al lanzamiento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch) para saber qué cosas debes tener en cuenta antes y después de lanzar un Canvas.
{% endalert %}

