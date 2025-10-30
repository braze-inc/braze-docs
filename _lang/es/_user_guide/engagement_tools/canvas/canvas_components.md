---
nav_title: Componentes de Canvas
article_title: Componentes de Canvas
page_order: 2
alias: "/user_guide/engagement_tools/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Componentes de Canvas"
guide_top_text: "Mejora tu viaje en Canvas con los componentes de Canvas. Los componentes del Canvas pueden utilizarse para simplificar el proceso de determinación de la eficacia de tu Canvas, sustituyendo excesivos pasos completos por uno solo. Los componentes en Canvas se refieren al recorrido personalizado del usuario en tus ramas de Canvas."

page_type: landing
description: "En esta página encontrarás artículos sobre componentes de Canvas que te ayudarán a crear Canvas más avanzados. Algunos de estos componentes son el paso para el mensaje, el paso para el retraso, el paso para la división de decisiones, etc."
tool: Canvas

guide_featured_title: "Artículos de sección"
guide_featured_list:
  - name: Paso de la mensajería
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Paso de retardo
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: Paso para la división de decisiones
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Paso a paso de las rutas de audiencia
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    image: /assets/img/braze_icons/users-01.svg 
  - name: Paso de las rutas de acción  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    image: /assets/img/braze_icons/zap.svg
  - name: Paso de ruta de experimentos
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    image: /assets/img/braze_icons/columns-01.svg
  - name: Paso de actualización de usuario
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Banderas de características en Canvas
    link: /docs/developer_guide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Sincronización de audiencias en Canvas
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## Acerca de los componentes de Canvas

Con los componentes de Canvas, puedes desbloquear nuevos recorridos de usuario para mejorar tu proceso y aumentar la eficacia del alcance de tu audiencia.

### Personalización de los recorridos del usuario

\![Ejemplo de un recorrido de usuario en Canvas con un paso para la división de decisiones seguido de pasos de retraso y pasos de mensajería.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Utiliza [las Rutas de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) para dividir tu recorrido de usuario en función de acciones y eventos de interacción, como la realización de una compra. Si quieres filtrar y segmentar tus audiencias, [las Rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) te ayudan a simplificar la segmentación de tus usuarios enviándolos por diferentes rutas de Canvas en función de los criterios de audiencia.

Los componentes de [división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) utilizan una lógica simple de "sí o no" para crear dos rutas mutuamente excluyentes para tus recorridos de usuario que se basan en una acción o en un atributo del usuario. Esto puede ayudarte a identificar y dirigirte a tus grupos de usuarios.

Los componentes de [retraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step) te permiten retrasar un solo paso en tu Canvas. Este paso en Canvas es ideal para comunicar mensajes a tus usuarios en un momento determinado. Además, los componentes de Retraso también pueden aumentar el alcance de tu audiencia al dar más tiempo a tu audiencia para cumplir los criterios del componente.

### Prueba

Al crear tus recorridos de usuario, quizá quieras probar también cuál es el recorrido Canvas más eficaz. Con [las Rutas de experimentos]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step), puedes probar varias rutas de Canvas en cualquier paso. También puedes utilizar las conexiones entre pasos como vista previa de alto nivel. Las conexiones naranjas indican que el paso anterior hará avanzar inmediatamente a los usuarios al siguiente paso.

### Integración

¿Quieres sincronizarte con los datos de usuario propios de tu marca? Aprovecha las opciones de sincronización de audiencias disponibles para [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) y [Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).

