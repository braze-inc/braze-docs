---
nav_title: Eventos de conversión
article_title: Eventos de conversión
page_order: 3
page_type: reference
description: "Este artículo de referencia define los eventos de conversión, cómo utilizarlos para definir tus métricas de éxito en Braze, y cómo utilizar estos eventos para ver el grado de interacción de tus usuarios."
tool:
    - Campaigns
    - Canvas
---

# Eventos de conversión

> Un evento de conversión es un tipo de métrica de éxito que realiza un seguimiento de si un destinatario de tu mensajería realiza una acción de alto valor en un tiempo determinado tras recibir tu interacción. Utiliza estos eventos para asegurarte de que estás recopilando información relevante y útil que luego puedas utilizar para obtener información para tu campaña o Canvas.

## Cómo funciona

Para una campaña personalizada de vacaciones dirigida a usuarios activos, un evento de conversión de **Iniciar una sesión** en un plazo de dos o tres días puede ser adecuado, porque te permite reunir una sensación de interacción del usuario al recibir tu mensaje. También puedes seleccionar eventos adicionales como **Pedido de lugares**, **Actualizar aplicación** o cualquiera de tus eventos personalizados como eventos de conversión.

{% alert tip %}
Para saber más sobre conversiones, consulta nuestro [curso de Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.
{% endalert %}

### Reglas de seguimiento de conversiones

Los eventos de conversión atribuyen las acciones de los usuarios a un punto de interacción. Nota lo siguiente sobre cómo Braze gestiona las conversiones múltiples:

- **Campañas monocanal**: Las conversiones se producen por usuario, no por dispositivo. Dentro de un mismo canal, un usuario sólo convierte una vez por evento de conversión, aunque se envíe un mensaje a varios dispositivos. Por ejemplo, si una campaña sólo tiene un evento de conversión configurado como "Realiza cualquier compra" y un usuario realiza dos compras distintas dentro del plazo de conversión, Braze sólo cuenta una conversión.
- **Campañas multicanal**: En las campañas multicanal, cada canal tiene su propia oportunidad de conversión. Un usuario puede convertir una vez por canal tras recibir un mensaje en ese canal. Esto significa que si un usuario recibe mensajes en varios canales (por ejemplo, tanto correo electrónico como push) y realiza la acción de conversión, Braze cuenta una conversión por cada canal, lo que puede dar lugar a tasas de conversión superiores al 100%.
- Si un usuario realiza un evento de conversión dentro de los plazos de conversión de dos campañas o Canvases distintos que haya recibido, la conversión se registra en ambos.
- Un usuario cuenta como convertido si realizó el evento de conversión específico en la ventana, aunque no abriera ni hiciera clic en el mensaje.
- En el caso de los Canvas, el seguimiento de la conversión se basa en el plazo final de conversión que comienza cuando un usuario entra en el Canvas, no en el tiempo de los mensajes individuales. Braze cuenta las conversiones incluso durante los periodos de retraso entre mensajes en Canvas.

### Evento de conversión primaria

El evento de conversión primaria es el primer evento que añades durante la creación de una campaña o Canvas. Este acontecimiento es el que más influye en tu compromiso y tus informes. Braze utiliza tu evento de conversión primaria para:

- Calcula la variación del mensaje ganador en campañas [multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) o Lienzos.
- Determina la ventana en la que se calculan los ingresos para la campaña o el Canvas.
- Ajusta la distribución de mensajes para campañas y Lienzos mediante [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

El recuento de eventos de conversión primaria es el número de eventos de conversión que se han producido. Para las campañas multicanal, Braze cuenta las conversiones por canal (como se describe en [Reglas de seguimiento de conversiones](#conversion-tracking-rules)), lo que significa que el recuento de conversiones puede superar el número de usuarios únicos y dar lugar a tasas de conversión superiores al 100%. Braze calcula la tasa de evento de conversión primaria dividiendo este recuento por el número de destinatarios únicos. Braze considera destinatario a un usuario cuando el mensaje se envía o se muestra, dependiendo del canal. Por ejemplo, en push o correo electrónico, un usuario se convierte en destinatario después de que Braze envíe el mensaje. Para los mensajes dentro de la aplicación o las tarjetas de contenido, el usuario debe ver el mensaje para ser considerado destinatario.

{% alert note %}
Si abortas mensajes utilizando la etiqueta de Liquid `abort`, Braze aborta mensajes sólo para los usuarios que pasan por variantes. Los mensajes a los usuarios del grupo de control no se cancelan, lo que puede dar lugar a porcentajes de conversión sesgados entre variantes y grupos de control. Como solución, utilice [la segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) para dirigirse a sus usuarios en la campaña y en la entrada de Canvas.
{% endalert %}

## Crear una campaña con seguimiento de la conversión

### Paso 1: Configura tu campaña

[Cree una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) para el canal de mensajería que desee. Tras configurar los mensajes y el calendario de tu campaña, puedes añadir hasta cuatro eventos de conversión para su seguimiento.

Utiliza tantos eventos de conversión como sea necesario. Añadir un segundo o tercer evento de conversión enriquece significativamente tus informes. Por ejemplo, en el caso de una campaña dirigida a usuarios rezagados, añadir un evento de conversión secundario junto con el evento de conversión primario **Sesión de inicio** te ayuda a comprender la eficacia de tu campaña a la hora de hacer que los usuarios vuelvan a tu aplicación. 

### Paso 2: Añade los eventos de conversión

Primero, selecciona el tipo general de evento que te gustaría utilizar:

| Tipo de evento de conversión   | Descripción                |
|-------------------------|----------------------------|
| **Inicia la sesión**      | Se considera que un usuario se ha convertido cuando abre cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones del área de trabajo).|
| **Hace la compra**      | Se considera que un usuario se ha convertido cuando registra un [evento de Compra]({{site.baseurl}}/api/objects_filters/purchase_object/). Esto hace un seguimiento predeterminado de cualquier compra, o puedes especificar un producto concreto.|
| **Pedidos realizados**        | Se considera que un usuario se ha convertido cuando desencadena el [evento recomendado de Comercio Electrónico Pedido Realizado]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events?tab=ecommerce.order_placed#ecommerce-recommended-events). Esto hace un seguimiento de cualquier pedido de forma predeterminada, o puedes filtrar por un producto específico.|
| **Lleva a cabo el evento personalizado**| Se considera que un usuario se ha convertido cuando realiza uno de sus eventos personalizados existentes (no hay ningún evento predeterminado, debe especificar el evento).|
| **Actualiza la aplicación**         | Se considera que un usuario se ha convertido cuando actualiza la versión de la aplicación en cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones del área de trabajo). Braze realiza una comparación numérica de los mejores esfuerzos para determinar si el cambio fue una mejora. Las versiones no numéricas se cuentan como conversiones si cambia la versión.|
| **Abre el correo electrónico**         | Se considera que un usuario se ha convertido cuando abre el correo electrónico (sólo para campañas por correo electrónico).|
| **Hace clic en el correo electrónico**        | Se considera que un usuario se ha convertido cuando hace clic en un enlace dentro del correo electrónico (sólo para campañas por correo electrónico).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
**No se admiten propiedades anidadas en los eventos de conversión**. No puedes utilizar propiedades anidadas en eventos de conversión. Por ejemplo, si `product_code` o `product_name` son propiedades anidadas dentro de una matriz `products` (como `products[].product_code`), no puedes utilizarlas para comprobar si se ha realizado la compra de un producto concreto en un evento de conversión.
{% endalert %}

Establece tu plazo de conversión. Es el tiempo máximo que puede pasar antes de que Braze considere una conversión. Puedes establecer una ventana de hasta 30 días durante la cual Braze cuenta la conversión si el usuario realiza la acción especificada.

![El tipo de evento de conversión "Realiza compra" como ejemplo para registrar conversiones de usuarios que realizan cualquier compra. Tiene un plazo de conversión de 12 horas.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Cuando hayas seleccionado los eventos de conversión, continúa con el proceso de creación de la campaña y comienza a enviarla.

### Paso 3: Ver tus resultados

Ve a la página **Detalles** para ver los detalles de cada evento de conversión asociado a la campaña que has creado. Independientemente de los eventos de conversión seleccionados, también puedes ver los ingresos totales atribuidos a esta campaña concreta, así como variantes específicas, durante la ventana del evento de conversión primaria.

{% alert note %}
Si no seleccionas ningún evento de conversión durante la creación de la campaña, el tiempo predeterminado es de tres días.
{% endalert %}

Además, para los mensajes multivariantes, puede ver el número de conversiones y los porcentajes de conversión de su grupo de control y de cada variante.

![Cuatro eventos de conversión que realizan un seguimiento de las conversiones en función de cuándo se realizó una compra en un plazo de tres horas, cuándo se realizó una compra en un plazo de dos horas, cuándo se inició una sesión en un plazo de 30 minutos y cuándo se inició una sesión en un plazo de 25 minutos.]({% image_buster /assets/img_archive/conversion_event_details.png %})