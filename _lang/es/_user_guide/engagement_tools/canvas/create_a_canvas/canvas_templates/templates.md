---
nav_title: Plantillas de Canvas
article_title: Plantillas de Canvas
alias: "/canvas_templates/templates/"
page_order: 0
description: "Este artículo de referencia explica cómo crear plantillas Canvas disponibles."
page_type: reference
---

# Plantillas de Canvas

> Braze dispone de una selección de plantillas de Canvas que puedes consultar y utilizar como mejores prácticas para casos de uso comunes. Aunque estas plantillas no se pueden editar, puedes verlas en **Plantillas** > **Plantillas Braze** o utilizarlas en tus Lienzos.

![Plantillas Braze en la sección de plantillas Canvas con trece plantillas disponibles.]({% image_buster /assets/img/braze_canvas_templates.png %})

Selecciona una de las siguientes plantillas disponibles para utilizarla como referencia o como Canvas.

## Plantillas estándar de Canvas

{% tabs %}
{% tab Abandoned Intent %}

### Intención abandonada

Interactúa con los usuarios en tiempo real para animarles a completar sus compras.

Ten en cuenta lo siguiente cuando utilices esta plantilla:

- Añade una audiencia específica. Actualmente, las rutas de audiencia se desencadenan basándose en "Realizada cualquier compra", pero puedes adaptar esto a productos específicos a los que quieras dirigirte.
- Esta plantilla asume que tienes un recorrido post-compra separado, por lo que realizar una compra hará que los usuarios salgan del Canvas.
- Rellena los datos en el paso Sincronizar audiencia.

{% endtab %}
{% tab Back In Stock %}

### Reaprovisionamiento de existencias

Impulsa las compras notificando a tus usuarios cuando un artículo vuelve a estar disponible con mensajes personalizados. Ten en cuenta lo siguiente cuando utilices esta plantilla:

- En **Programa de entradas**, selecciona un catálogo para utilizarlo. Esto te permite acceder a datos, como productos, descuentos y promociones, para dirigirte más a tus usuarios.
- En **Audiencia objetivo**, añade un segmento para dirigirte a los usuarios que indicaron interés por un determinado artículo.
- En los pasos de Mensaje en todo el Canvas, actualiza el Liquid para hacer referencia a tu catálogo.

{% endtab %}
{% tab Feature Adoption %}

### Adopción de características

Entrega oportunamente mensajes personalizados para destacar las ventajas y consejos de uso. Ten en cuenta lo siguiente cuando utilices esta plantilla:

- Excluye a los usuarios que ya hayan adoptado la característica. Por ejemplo, en **Audiencia objetivo**, añade un filtro para un evento personalizado como "Característica activada" que ya se haya producido.
- Para utilizar el paso de ruta de experimentos, define un evento de conversión. Este acontecimiento debe ser el que señale la adopción de la característica.
- Configura el paso Ruta de acción en la plantilla con eventos personalizados para "Característica activada" y "Recorrido realizado".
- Configura los atributos personalizados en el paso Mensaje llamado "Encuesta de opinión" para captar el sentimiento de la opinión.

{% endtab %}
{% tab Lapsed User %}

### Usuario caducado

Haz que los usuarios vuelvan a tu aplicación con incentivos basados en sus interacciones anteriores. Ten en cuenta lo siguiente cuando utilices esta plantilla:

- En **Conceptos básicos**, selecciona una aplicación específica para realizar el seguimiento de las conversiones.
- En el editor Canvas, añade aplicaciones específicas para los pasos de las Rutas de acción.
- Configura el paso Sincronización de audiencias con los socios y audiencias para tu caso de uso.

{% endtab %}
{% tab Onboarding %}

### Incorporación

Crea trayectos de incorporación que promuevan una fuerte adopción inicial y fomenten relaciones duraderas con tus usuarios. Ten en cuenta lo siguiente cuando utilices esta plantilla:

- En el paso Rutas de audiencia denominado "División de la audiencia", considera la posibilidad de personalizar las acciones clave para los usuarios comprometidos. En la plantilla, el filtro de segmento es "Ha hecho clic en el correo electrónico para el paso Correo electrónico de bienvenida".

{% endtab %}
{% tab Post-Purchase Feedback %}

### Comentarios posteriores a la compra

Orquesta experiencias personalizadas que te permitan responder a los comentarios y establecer relaciones con tus usuarios. Ten en cuenta lo siguiente cuando utilices esta plantilla:

- En el primer paso del editor Canvas:
    - Especifica los atributos personalizados en el mensaje dentro de la aplicación para indicar el sentimiento de la respuesta en función de la opción de cuestionario seleccionada. 
    - Especifica atributos en los enlaces de cada llamada a la acción para captar qué opción se selecciona. Se hace referencia a estos atributos en la ruta de audiencia posterior.
- Personaliza la ruta de audiencia con los atributos del primer paso de esta plantilla.
- Configura el paso de Sincronización de audiencias denominado "Reorientación de anuncios".

{% endtab %}
{% endtabs %}

{% alert tip %}
Para obtener una guía paso a paso para crear un Canvas de ejemplo utilizando estas plantillas Braze, consulta [Utilizar plantillas Braze]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates).
{% endalert %}

## Plantillas Canvas para comercio electrónico

Las plantillas eCommerce Canvas están diseñadas específicamente para especialistas en marketing de comercio electrónico, lo que facilita la aplicación de estrategias esenciales.

{% multi_lang_include canvas/ecommerce_templates.md %}