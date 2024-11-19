---
nav_title: Acontecimientos excepcionales 
article_title: Acontecimientos excepcionales
page_order: 4
page_type: reference
description: "Este artículo de referencia describe los eventos de excepción y cómo afectan a los componentes de Canvas."
tool: Canvas

---

# Eventos de excepción del lienzo

{% alert important %}
A partir del 28 de febrero de 2023, ya no podrás crear o duplicar Lienzos utilizando el editor original. Este artículo está disponible como referencia a la hora de configurar eventos de excepción para el flujo de trabajo original de Canvas. <br><br> Braze recomienda a los clientes que utilicen la experiencia Canvas original que se pasen a Canvas Flow. Es una experiencia de edición mejorada para construir y gestionar mejor los Lienzos. Más información sobre la [clonación de tus lienzos en el flujo de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

> Al programar un componente para un lienzo utilizando el editor de lienzos original, tiene la opción de configurar un evento de excepción. Puedes añadir un evento de excepción a un componente siempre que la audiencia no avance inmediatamente. Los usuarios que realicen el evento de excepción no serán [avanzados a través del paso][2] y saldrán de su audiencia Canvas.

Los eventos de excepción sólo se activarán mientras un usuario esté esperando recibir el componente Canvas asociado. Si un usuario realiza la misma acción en un paso anterior de Canvas, el evento de excepción no se activará.

{% alert important %}
Para el Canvas Flow, los eventos de excepción sólo se configuran utilizando [Rutas de Acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/). Por ejemplo, puede definir una ruta de acción y utilizar la ruta Todos los demás como excepción.
{% endalert %}

Los eventos de excepción para un paso basado en una acción funcionarán durante el retardo o la ventana del paso. Los pasos programados no tienen ventana, y como resultado, el evento de excepción sólo funcionará si ocurre durante el retraso.

Por ejemplo, si tiene un evento de excepción para "Carrito Abandonado" en el tercer paso de su Canvas, pero un usuario abandona su carrito mientras está en el segundo paso, el evento de excepción no se activará. En este ejemplo, el evento de excepción sólo se activará si el usuario abandona su carrito mientras se encuentra en el tercer paso de su Canvas. 

![][1]


[1]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/
