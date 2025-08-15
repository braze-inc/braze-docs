---
nav_title: Conmutador de características
article_title: Conmutador de características
page_order: 8
page_type: reference
description: "Este artículo de referencia explica cómo se pueden utilizar los indicadores de características en Canvas."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/engagement_tools/canvas/canvas_components/feature_flags/#creating-a-feature-flag'
---

# Banderas de características

> Las banderas de características le permiten experimentar y confirmar sus hipótesis en torno a nuevas características. Los profesionales del marketing pueden utilizar los indicadores de funciones para segmentar su audiencia en [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) y realizar un seguimiento del impacto del despliegue de funciones en las conversiones. Además, [las rutas de experimentación]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) le permiten optimizar estas conversiones probando diferentes mensajes o rutas entre sí y determinando cuál es la más eficaz. Utiliza la ruta ganadora a medida que despliegues progresivamente tu característica a una audiencia más amplia.

¿Busca más información sobre las banderas de características y cómo utilizarlas en Braze? Consulta nuestros artículos dedicados a [las banderas de características]({{site.baseurl}}/developer_guide/feature_flags/).

## Creación de un indicador de características

![Un paso de ejemplo de la Bandera de Características para la característica Botón de Chat en Vivo.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Para crear un componente Bandera de Características, primero añada un paso a su Lienzo. Arrastre y suelte el componente desde la barra lateral, o haga clic en el botón <i class="fas fa-plus-circle"></i> más en la parte inferior de un paso y seleccione **Bandera de características**. A continuación, seleccione el indicador de características en el menú desplegable, que contiene los indicadores de características que no están archivados.

## Cómo funciona este paso

Cuando se detiene un Canvas, o se archiva, o se elimina un paso, cualquier usuario que haya pasado por ese paso dejará de recibir la bandera de característica del paso y sus propiedades. El usuario seguirá estando sujeto al porcentaje de despliegue por defecto y a la segmentación de la audiencia para esa bandera de función y para cualquier otro Lienzo que pueda seguir activo.

Las propiedades de un paso de Canvas se pueden cambiar después del lanzamiento, e incluso después de que un usuario pase por el paso. Los usuarios recibirán siempre una versión dinámica y en tiempo real de la bandera de características, en lugar de la versión antigua guardada previamente.

## Sobrescribir propiedades

Al crear una bandera de característica se especifican las propiedades por defecto. Al configurar un paso del Lienzo de marcado de funciones, puede mantener los valores predeterminados o sobrescribir los valores para los usuarios que entren en este paso.

![Una bandera de característica "Centro de preferencias" con "cadena" como propiedad, "url" como clave de propiedad y un valor.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Vaya a **Mensajería** > **Indicadores de funciones** para editar, añadir o eliminar propiedades adicionales.

## Diferencias entre el lienzo y el despliegue

El lienzo y el despliegue de una bandera de características (arrastrando el control deslizante) pueden funcionar independientemente el uno del otro. Una advertencia importante es que la entrada a un paso de Canvas sobrescribirá cualquier configuración de rollout por defecto. Esto significa que si un usuario no cumple los requisitos para una bandera de función, un paso de Canvas puede habilitar la función para ese usuario.

Del mismo modo, si un usuario cumple los requisitos para el despliegue de una bandera de características con determinadas propiedades, si también entra en el paso del lienzo, recibirá cualquier valor sobrescrito de ese paso del lienzo.

