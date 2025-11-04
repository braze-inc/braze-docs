---
nav_title: Banderas de características
article_title: Banderas de características
page_order: 8
page_type: reference
description: "Este artículo de referencia explica cómo pueden utilizarse los indicadores de características en Canvas."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/engagement_tools/canvas/canvas_components/feature_flags/#creating-a-feature-flag'
---

# Banderas de características

> Las banderas de características te permiten experimentar y confirmar tus hipótesis sobre nuevas características. Los especialistas en marketing pueden utilizar banderas de características para segmentar su audiencia en [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) y hacer un seguimiento del impacto del despliegue de características en las conversiones. Además, [las Rutas de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) te permiten optimizar estas conversiones probando diferentes mensajes o rutas entre sí y determinando cuál es la más eficaz. Utiliza la ruta ganadora a medida que despliegues progresivamente tu característica a una audiencia más amplia.

¿Buscas más información sobre las banderas de características y cómo pueden utilizarse en Braze? Consulta nuestros artículos dedicados a [las banderas de características]({{site.baseurl}}/developer_guide/feature_flags/).

## Crear una bandera de característica

\![Un ejemplo del paso Bandera de características para la característica Botón de chat en vivo.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Para crear un componente Bandera de características, añade primero un paso a tu Canvas. Arrastra y suelta el componente desde la barra lateral, o haz clic en el botón más <i class="fas fa-plus-circle"></i> situado en la parte inferior de un paso y selecciona **Bandera de características**. A continuación, selecciona la bandera de característica en el desplegable, que contiene las banderas de característica que no están archivadas.

## Cómo funciona este paso

Cuando se detiene un Canvas, o se archiva, o se elimina un paso, cualquier usuario que haya pasado por ese paso dejará de recibir la bandera de característica del paso y sus propiedades. El usuario seguirá estando sujeto al porcentaje de despliegue predeterminado y a la segmentación de la audiencia para esa bandera de característica y para cualquier otra Lona que pueda seguir activa.

Las propiedades de un paso en Canvas pueden cambiarse después del lanzamiento, e incluso después de que un usuario haya pasado por el paso. Los usuarios siempre recibirán una versión dinámica y en tiempo real de la bandera de características, en lugar de la versión antigua guardada previamente.

## Sobrescribir propiedades

Al crear una bandera de característica, especifica las propiedades predeterminadas. Al configurar un paso en Canvas de bandera de característica, puedes mantener los valores predeterminados o sobrescribir los valores para los usuarios que entren en este paso.

\![Un indicador de característica "Centro de preferencias" con "Cadena" como propiedad, "url" como clave de propiedad y un valor.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Ve a **Mensajería** > **Banderas de características** para editar, añadir o eliminar propiedades adicionales.

## Diferencias entre Canvas y Rollout

El Canvas y el despliegue de una bandera de características (arrastrando el deslizador) pueden funcionar independientemente el uno del otro. Una advertencia importante es que la entrada a un paso en Canvas sobrescribirá cualquier configuración predeterminada del despliegue. Esto significa que si un usuario no cumple los requisitos para una bandera de característica, un paso en Canvas puede habilitar la característica para ese usuario.

Del mismo modo, si un usuario cumple los requisitos para el despliegue de una bandera de características con determinadas propiedades, si también entra en el paso en Canvas, recibirá cualquier valor sobrescrito de ese paso en Canvas.

