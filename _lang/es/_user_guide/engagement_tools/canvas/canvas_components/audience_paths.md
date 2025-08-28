---
nav_title: Rutas de audiencia 
article_title: Rutas de audiencia 
alias: /audience_paths/
page_order: 1
page_type: reference
description: "Este artículo de referencia describe cómo utilizar las Rutas de Audiencia en su Canvas para filtrar y segmentar intuitivamente a los usuarios a gran escala con agrupaciones de usuarios estratégicas basadas en prioridades."
tool: Canvas

---

# Rutas de audiencia 

> Las rutas de audiencia de Canvas le permiten filtrar y segmentar intuitivamente a los usuarios a gran escala con agrupaciones de usuarios estratégicas basadas en prioridades. 

Este componente Canvas sustituye la necesidad de crear excesivos pasos completos basados en el público, permitiéndole combinar lo que podrían haber sido ocho componentes completos en uno solo. Esto le ayuda a simplificar la orientación de los usuarios al tiempo que despeja sus lienzos de desorden y complejidad innecesarios. 

## Cómo funciona

![Una ruta de audiencia con dos grupos: usuarios comprometidos y todos los demás.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Las rutas de audiencia son similares a los embudos de clasificación con criterios de clasificación. Los usuarios son evaluados para cada criterio en orden de prioridad y enviados por la vía del criterio de mayor rango que cumplan. Esto reduce la ambigüedad de dónde irán los usuarios y qué mensajes recibirán. Ten en cuenta que las clasificaciones no son [editables después del lanzamiento]({{site.baseurl}}/post-launch_edits/).

Con las Rutas de audiencia, puedes:

- Envíe a los usuarios por diferentes rutas de Canvas en función de los criterios de audiencia.
- Asigne prioridad a los distintos grupos de destinatarios, para que sus mensajes lleguen a los usuarios correctos. 
  - Anteriormente, si los usuarios cumplían los criterios de dos posibles pasos completos, se les asignaba aleatoriamente. 
- Dirigirse con precisión a los usuarios a gran escala.
  - Cree hasta ocho grupos de destinatarios (dos predeterminados y seis adicionales) por componente, pero es posible que desee conectar varios Pasos de rutas de destinatarios para clasificar mejor a sus usuarios. 

### Dejar tiempo para las evaluaciones de los usuarios

![Canvas muestra un retraso de 24 horas tras un paso en Mensaje, seguido de una ruta de audiencia.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Los usuarios son evaluados en cuanto alcanzan el paso de la Ruta de audiencia. Una vez evaluados, pasarán inmediatamente al siguiente paso. Esto hace que sea importante dejar transcurrir una ventana de tiempo adecuada si la Ruta de audiencia viene determinada por una acción del usuario.

Por ejemplo, si a los usuarios se les envía el Mensaje A y el siguiente paso es una Ruta de audiencia que evalúa si han interactuado con ese mensaje, todos los usuarios avanzarán al paso de los que no han interactuado con ese mensaje. Esto se debe a que los usuarios pasaron inmediatamente al paso de la ruta de audiencia sin tiempo para interactuar con el mensaje. En otras palabras, se evalúa la interacción de los usuarios con el mensaje casi inmediatamente después del envío del mensaje.

Para dar tiempo a los usuarios a interactuar con un mensaje enviado, es necesario que haya un retraso entre el paso Mensaje y la Ruta de audiencia. Por ejemplo, un retraso de 24 horas daría a los usuarios 24 horas después del envío del mensaje para interactuar con el Mensaje A antes de ser evaluado.

Ten en cuenta que los usuarios avanzan al siguiente paso en función de la primera acción que hayan realizado tras entrar en el paso Ruta de audiencia dentro de la ventana de evaluación. Esto significa que si un usuario realiza un segundo evento personalizado, no cambiaría de grupo de audiencia.

## Crear una ruta de audiencia

Para añadir un paso de Rutas de audiencia, haz lo siguiente: 

1. Añade un paso a tu Canvas. 
2. Arrastra y suelta el componente desde la barra lateral, o selecciona <i class="fas fa-plus-circle"></i> **Añadir** en la parte inferior de un paso y selecciona **Rutas de audiencia**.

El componente por defecto Rutas de público contiene dos grupos de público por defecto, **Grupo 1** y **Todos los demás**. El grupo **Todos los demás** incluye a cualquier usuario que no pertenezca a un grupo de audiencia definido. Este grupo siempre irá último.

### Definir los grupos de audiencia

La siguiente captura de pantalla muestra el diseño de un paso Ampliado de Rutas de Audiencia. Aquí puede definir hasta ocho grupos de audiencia (uno preestablecido y siete personalizables). Para definir un grupo de destinatarios, seleccione el nombre del grupo en el editor de rutas de destinatarios. Puede cambiar el nombre de su grupo de público, elegir los filtros y segmentos que se aplican a su grupo y añadir o eliminar grupos.

Por ejemplo, si quisieras dirigir la mensajería de incorporación a un grupo de usuarios, podrías seleccionar filtros de reorientación, como "Ha hecho clic en el correo electrónico" y "Ha hecho clic en el mensaje dentro de la aplicación".

![Una ruta de audiencia ampliada con grupos para "Amantes de la cocina asiática", "Amantes de la cocina latina", "Amantes de la cocina europea" y "Todos los demás".]({% image_buster /assets/img/audience_path/audience_path3.png %})

Una vez completado el paso Rutas de audiencia, cada grupo de audiencia tendrá una rama independiente. Puedes seguir utilizando las Rutas de audiencia para filtrar aún más tu audiencia, o continuar tu recorrido en Canvas con los pasos en Canvas estándar. 

![Dos rutas de audiencia con diferentes grupos basados en la interacción.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

### Probar los grupos de audiencia

Después de añadir segmentos y filtros a su público, puede probar si sus grupos de público están configurados como se esperaba [buscando un usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar que coincide con los criterios del público.

![La sección "Búsqueda de usuarios".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Utilizar rutas de audiencia

El verdadero poder de las Rutas de audiencia reside en la capacidad de asignar prioridades. Aunque no es necesario utilizar esta función de forma estratégica, es posible que algunos vendedores se vean obligados a promocionar determinados productos entre los usuarios, como ofertas especiales o lanzamientos de edición limitada. 

Al asignar una prioridad alta a estos grupos, puede dirigirse a los usuarios que entran en filtros y segmentos específicos y, al mismo tiempo, dirigirse a los usuarios que podrían no encajar en esos criterios específicos, todo en un único paso de Canvas.

![Una ruta de audiencia con grupos para "Le gustan los zapatos de gran marca", "Le gustan los zapatos de gran marca" y "Todos los demás".]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Por ejemplo, supongamos que desea enviar a un grupo de usuarios anuncios de nuevos productos. Empezarías por clasificar los filtros que corresponden a esos productos en la parte alta de la ruta de audiencia. Si estuvieras creando una campaña de marketing para la empresa "Gran Marca" y acabara de lanzarse una nueva marca minorista, podrías seleccionar filtros como "Le gustan los zapatos de Gran Marca" o "Le gustan los bolsos de Gran Marca", y enviar diferentes mensajes de mensajería electrónica en función del grupo filtrado en el que se encuentren. 

Cuando los usuarios entren en este componente de Rutas de audiencia, primero se evaluará si pertenecen al grupo de audiencia mejor clasificado: Grupo de audiencia 1 "Le gustan los zapatos de grandes marcas". Si es así, continuarán con el siguiente componente definido en tu Canvas. Si no les "gustan los zapatos de gran marca", se evaluarán para el siguiente grupo de audiencia, el Grupo de Audiencia 2 "Le gustan los bolsos de gran marca", y continuarán con el siguiente paso si se cumplen los criterios. Por último, los usuarios que no entren en los grupos anteriores entrarían en el grupo "Todos los demás" y también continuarían con el siguiente paso en Canvas que definas para esa ruta.

También puedes ver el rendimiento de este paso utilizando [los análisis de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#performance-visualization).

### Segmentación de rutas de audiencia con números de cubo aleatorios

Si su Canvas utiliza un [límite de tasa]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/) (como limitar el número total de usuarios que recibirán el Canvas), Braze recomienda que no utilice números de cubo aleatorios para segmentar sus Rutas de audiencia. 

Un [número de cubo aleatorio]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) es un atributo de usuario que puede utilizarse para crear segmentos de usuarios aleatorios distribuidos uniformemente. Braze utiliza el número de cubo aleatorio para agrupar a los usuarios durante la fase de segmentación de la entrada en Canvas, y cada grupo se procesa por separado. Dependiendo de qué grupos terminen de procesarse primero, algunos usuarios pueden verse limitados en la entrada debido al límite de velocidad, lo que podría causar una distribución desigual de los usuarios cuando lleguen al paso Rutas de audiencia.

En este caso, pruebe a utilizar [Vías de experimentación]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).

### Usar el filtro de canal inteligente con rutas de audiencia

Utilizando una combinación de pasos de rutas de audiencia y filtros de canales inteligentes, puedes adaptar tu experiencia de mensajería a las preferencias y comportamientos de cada usuario. De este modo, tus usuarios recibirán los mensajes más relevantes a través de los canales adecuados.

Por ejemplo, en un paso de Rutas de audiencia, puedes crear tres audiencias: Correo electrónico, push móvil y todos los demás. Para la audiencia de correo electrónico, añade el filtro `Intelligent Channel is Email`. Para la audiencia de Mobile Push, añade el filtro `Intelligent Channel is Mobile Push`. A continuación, puedes añadir un paso Mensaje para cada una de las rutas de audiencia para entregar mensajes personalizados y relevantes.

{% alert tip %}
Echa un vistazo a nuestras [plantillas Braze Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates) para ver ejemplos de cómo puedes personalizar estas plantillas prediseñadas en tu beneficio.
{% endalert %}
