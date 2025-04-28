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

![][0]{: style="float:right;max-width:13%;margin-left:15px;margin-top:15px;"}

Las rutas de audiencia son similares a los embudos de clasificación con criterios de clasificación. Los usuarios son evaluados para cada criterio en orden de prioridad y enviados por la vía del criterio de mayor rango que cumplan. Esto reduce la ambigüedad de dónde irán los usuarios y qué mensajes recibirán. Ten en cuenta que las clasificaciones no son [editables después del lanzamiento]({{site.baseurl}}/post-launch_edits/).

Con las Rutas de audiencia, puedes:

- Envíe a los usuarios por diferentes rutas de Canvas en función de los criterios de audiencia.
- Asigne prioridad a los distintos grupos de destinatarios, para que sus mensajes lleguen a los usuarios correctos. 
  - Anteriormente, si los usuarios cumplían los criterios de dos posibles pasos completos, se les asignaba aleatoriamente. 
- Dirigirse con precisión a los usuarios a gran escala.
  - Cree hasta ocho grupos de destinatarios (dos predeterminados y seis adicionales) por componente, pero es posible que desee conectar varios Pasos de rutas de destinatarios para clasificar mejor a sus usuarios. 

## Crear una ruta de audiencia

![][1]{: style="float:right;max-width:20%;margin-left:15px;"}

Para añadir un paso de Rutas de audiencia, haz lo siguiente: 

1. Añade un paso a tu Canvas. 
2. Arrastre y suelte el componente desde la barra lateral, o haga clic en <i class="fas fa-plus-circle"></i> **Añadir** en la parte inferior de un paso y seleccione **Rutas de audiencia**.

El componente por defecto Rutas de público contiene dos grupos de público por defecto, **Grupo 1** y **Todos los demás**. El grupo **Todos los demás** incluye a cualquier usuario que no pertenezca a un grupo de audiencia definido. Este grupo siempre irá último.

### Definir los grupos de audiencia

La siguiente captura de pantalla muestra el diseño de un paso Ampliado de Rutas de Audiencia. Aquí puede definir hasta ocho grupos de audiencia (uno preestablecido y siete personalizables). Para definir un grupo de destinatarios, seleccione el nombre del grupo en el editor de rutas de destinatarios. Puede cambiar el nombre de su grupo de público, elegir los filtros y segmentos que se aplican a su grupo y añadir o eliminar grupos.

Por ejemplo, si desea enviar a un grupo de usuarios recomendaciones útiles sobre comida, puede seleccionar filtros de atributos personalizados que ya haya creado, como "Le gusta la cocina asiática", "Le gusta la cocina latina" y "Le gusta la cocina europea". 

![][3]{: style="max-width:90%;margin-left:15px;"}

Una vez completado el paso Rutas de audiencia, cada grupo de audiencia tendrá una rama independiente. Puedes seguir utilizando las Rutas de audiencia para filtrar aún más tu audiencia, o continuar tu recorrido en Canvas con los pasos en Canvas estándar. 

![][4]{: style="max-width:90%;margin-left:15px;"}

### Probar los grupos de audiencia

![]({% image_buster /assets/img_archive/user_lookup.png %}){: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Después de añadir segmentos y filtros a su público, puede probar si sus grupos de público están configurados como se esperaba [buscando un usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) para confirmar que coincide con los criterios del público. 

## Utilizar rutas de audiencia

El verdadero poder de las Rutas de audiencia reside en la capacidad de asignar prioridades. Aunque no es necesario utilizar esta función de forma estratégica, es posible que algunos vendedores se vean obligados a promocionar determinados productos entre los usuarios, como ofertas especiales o lanzamientos de edición limitada. 

Al asignar una prioridad alta a estos grupos, puede dirigirse a los usuarios que entran en filtros y segmentos específicos y, al mismo tiempo, dirigirse a los usuarios que podrían no encajar en esos criterios específicos, todo en un único paso de Canvas.

![][2]{: style="float:right;max-width:40%;margin-left:15px;margin-bottom:15px;"}

Por ejemplo, supongamos que desea enviar a un grupo de usuarios anuncios de nuevos productos. Empezarías por clasificar los filtros que corresponden a esos productos en la parte alta de la ruta de audiencia. Si estuviera creando una campaña de marketing para la empresa "Big Brand" y acabara de lanzarse una nueva marca de zapatos, podría seleccionar filtros como "Le gustan los zapatos de Big Brand" o "Le gusta Big Brand", y enviar diferentes mensajes de correo electrónico en función del grupo filtrado en el que se encuentren. 

Cuando los usuarios entran en este componente de Rutas de Audiencia, primero se evaluará si pertenecen al grupo de audiencia mejor clasificado: Al grupo de audiencia A "le gustan los zapatos de grandes marcas". En caso afirmativo, pasarán al siguiente componente definido en su lienzo. Si no les "gustan los zapatos de la gran marca", serán evaluados para el siguiente grupo de audiencia, el grupo de audiencia B "le gusta la gran marca", y continuarán con el siguiente componente del Canvas si se cumplen los criterios. Por último, los usuarios que no entren en los grupos anteriores entrarán en el grupo **Todos los demás** y continuarán con el siguiente componente Canvas que defina para esa ruta.

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

[0]: {% image_buster /assets/img/audience_path/audience_path.png %}
[1]: {% image_buster /assets/img/audience_path/audience_path1.png %}
[2]: {% image_buster /assets/img/audience_path/audience_path2.png %}
[3]: {% image_buster /assets/img/audience_path/audience_path3.png %}
[4]: {% image_buster /assets/img/audience_path/audience_path4.png %}
