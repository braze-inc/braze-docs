---
nav_title: Componentes del lienzo
article_title: Componentes del lienzo
page_order: 2
alias: "/user_guide/engagement_tools/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Componentes del lienzo"
guide_top_text: "Mejora tu viaje en Canvas con los componentes de Canvas. Los componentes del lienzo pueden utilizarse para simplificar el proceso de determinación de la eficacia de su lienzo sustituyendo excesivos pasos completos por uno solo. Los componentes en Canvas se refieren al recorrido personalizado del usuario en sus ramas de Canvas."

page_type: landing
description: "En esta página encontrarás artículos sobre componentes de Canvas que te ayudarán a crear Canvas más avanzados. Algunos de estos componentes son el paso para el mensaje, el paso para el retraso, el paso para la división de decisiones, etc."
tool: Canvas

guide_featured_title: "Artículos de sección"
guide_featured_list:
  - name: Paso de mensaje
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Paso de demora
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: Paso para la división de decisiones
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Paso de las rutas de audiencia
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    image: /assets/img/braze_icons/users-01.svg 
  - name: Paso de rutas de acción  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    image: /assets/img/braze_icons/zap.svg
  - name: Paso de recorridos de experimentos
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    image: /assets/img/braze_icons/columns-01.svg
  - name: Paso de actualización de usuario
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Banderas de características en Canvas
    link: /docs/developer_guide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Sincronización de audiencias en Canvas
    link: /docs/partners/canvas_steps/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## Acerca de los componentes de Canvas

Con los componentes de Canvas, puede desbloquear nuevos recorridos de usuario para mejorar su proceso y aumentar la eficacia de su difusión entre el público.

### Personalizar los recorridos del usuario

![Ejemplo de un recorrido de usuario en Canvas con un paso para la división de decisiones seguido de pasos de retraso y pasos de mensajería.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Utilice [las rutas de acción][1] para dividir el recorrido del usuario en función de las acciones y los eventos de compromiso, como la realización de una compra. Si desea filtrar y segmentar sus audiencias, [las rutas de audiencia][2] le ayudan a simplificar la segmentación de sus usuarios enviándolos por diferentes rutas de Canvas en función de los criterios de audiencia.

Los componentes [de división de decisión][3] utilizan una lógica simple de "sí o no" para crear dos rutas mutuamente excluyentes para sus recorridos de usuario que se basan en una acción o un atributo del usuario. Esto puede ayudar a identificar y orientar a sus grupos de usuarios.

Los componentes de [retardo][4] le permiten retrasar un solo paso en su lienzo. Este paso de retardo independiente en su Canvas se utiliza mejor para comunicar mensajes a sus usuarios en un momento específico. Además, los componentes de Retraso también pueden aumentar el alcance de su audiencia al permitir más tiempo para que su audiencia cumpla los criterios del componente.

### Pruebas

Al crear sus recorridos de usuario, es posible que también desee probar la ruta Canvas más eficaz. Con [Experiment Paths][5], puede probar varias rutas de Canvas en cualquier paso. También puedes utilizar las conexiones entre pasos como una vista previa de alto nivel. Las conexiones naranjas indican que el paso anterior hará avanzar inmediatamente a los usuarios al siguiente paso.

### Integración

¿Quieres sincronizarte con los datos de los usuarios de tu marca? Aprovecha las opciones de sincronización de audiencia disponibles para [Facebook][6] y [Google][7].

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split
[4]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step
[6]: {{site.baseurl}}/partners/canvas_steps/facebook_audience_sync
[7]: {{site.baseurl}}/partners/canvas_steps/google_audience_sync