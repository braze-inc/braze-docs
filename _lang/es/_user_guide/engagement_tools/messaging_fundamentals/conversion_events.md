---
nav_title: Eventos de conversión
article_title: Eventos de conversión
page_order: 3
page_type: reference
description: "Este artículo de referencia define los eventos de conversión, cómo utilizarlos para definir tus métricas de éxito en Braze y cómo utilizar estos eventos para ver el nivel de interacción de tus usuarios."
tool:
    - Campaigns
    - Canvas
---

# Eventos de conversión

> Un evento de conversión es un tipo de métrica de éxito que realiza un seguimiento para determinar si el destinatario de tu mensaje realiza una acción de gran valor en un periodo de tiempo determinado tras recibir tu interacción. Aprovecha estos eventos para asegurarte de que estás recopilando información relevante y útil que luego podrás utilizar para obtener información valiosa para tu campaña o Canvas.

## Cómo funciona

Para una campaña navideña personalizada dirigida a usuarios activos, un evento de conversión de **«Iniciar sesión»** en un plazo de dos o tres días puede ser adecuado, ya que permite recabar información sobre la interacción de los usuarios al recibir tu mensaje. También puedes seleccionar eventos adicionales como **«Realizar pedido**», **«Actualizar aplicación**» o cualquiera de tus eventos personalizados como eventos de conversión.

{% alert tip %}
Para obtener más información sobre las conversiones, consulta nuestro [curso de Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.
{% endalert %}

### Reglas de seguimiento de conversiones

Los eventos de conversión atribuyen las acciones de los usuarios a un punto de interacción. Ten en cuenta lo siguiente sobre cómo Braze gestiona las conversiones múltiples:

- **Campañas de un solo canal**: Las conversiones se producen por usuario, no por dispositivo. Dentro de un mismo canal, un usuario solo realiza una conversión por cada evento de conversión, incluso si se envía un mensaje a varios dispositivos. Por ejemplo, si una campaña solo tiene un evento de conversión configurado como «Realiza cualquier compra» y un usuario realiza dos compras independientes dentro del plazo de conversión, Braze solo cuenta una conversión.
- **Campañas multicanal**: En las campañas multicanal, cada canal tiene su propia oportunidad de conversión. Un usuario puede convertir una vez por canal después de recibir un mensaje en ese canal. Esto significa que si un usuario recibe mensajes en varios canales (por ejemplo, tanto por correo electrónico como por notificaciones push) y realiza la acción de conversión, Braze cuenta una conversión por cada canal, lo que puede dar lugar a tasas de conversión superiores al 100 %.
- Si un usuario realiza un evento de conversión dentro de los plazos de conversión de dos campañas o lienzos distintos que ha recibido, la conversión se registra en ambos.
- Un usuario se considera convertido si ha realizado el evento de conversión específico en la ventana, incluso si no ha abierto ni hecho clic en el mensaje.
- En el caso de los Canvas, el seguimiento de conversiones funciona en función de la fecha límite de conversión final, que comienza cuando el usuario entra en el Canvas, y no en función del momento en que se envía cada mensaje individual. Braze cuenta las conversiones incluso durante los periodos de retraso entre mensajes en Canvas.

### Evento de conversión primaria

El evento de conversión primaria es el primer evento que añades durante la creación de la campaña o del Canvas. Este acontecimiento es el que más influye en tu compromiso y tus informes. Braze utiliza tu evento de conversión primaria para:

- Calcula la variación del mensaje ganador en campañas [multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) o lienzos.
- Determina la ventana en la que se calculan los ingresos para la campaña o el Canvas.
- Ajusta la distribución de mensajes para campañas y lienzos mediante [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

El recuento de eventos de conversión primaria es el número de eventos de conversión que se han producido. En las campañas multicanal, Braze cuenta las conversiones por canal (tal y como se describe en [las reglas de seguimiento de conversiones](#conversion-tracking-rules)), lo que significa que el recuento de conversiones puede superar el número de usuarios únicos y dar lugar a tasas de conversión superiores al 100 %. Braze calcula la tasa de conversión primaria dividiendo este recuento por el número de destinatarios únicos. Braze considera que un usuario es destinatario cuando se envía o se muestra el mensaje, dependiendo del canal. Por ejemplo, en los mensajes push o por correo electrónico, el usuario se convierte en destinatario después de que Braze envía el mensaje. En el caso de los mensajes dentro de la aplicación o las tarjetas de contenido, el usuario debe ver el mensaje para que se te considere destinatario.

{% alert note %}
Si se cancelan mensajes utilizando la etiqueta de`abort` Liquid, Braze solo cancela los mensajes de los usuarios que pasan por variantes. Los mensajes a los usuarios del grupo de control no se cancelan, lo que puede dar lugar a porcentajes de conversión sesgados entre las variantes y los grupos de control. Como solución, utilice [la segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) para dirigirse a sus usuarios en la campaña y en la entrada de Canvas.
{% endalert %}

## Crear una campaña con seguimiento de conversiones

### Paso 1: Configura tu campaña

[Cree una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) para el canal de mensajería que desee. Después de configurar los mensajes y el calendario de tu campaña, puedes añadir hasta cuatro eventos de conversión para su seguimiento.

Utiliza tantos eventos de conversión como sea necesario. Añadir un segundo o tercer evento de conversión enriquece significativamente tus informes. Por ejemplo, para una campaña dirigida a usuarios inactivos, añadir un evento de conversión secundario junto con el evento de conversión primaria **«Iniciar sesión»** te ayuda a comprender la eficacia de tu campaña a la hora de atraer de nuevo a los usuarios a tu aplicación. 

### Paso 2: Añadir los eventos de conversión

En primer lugar, selecciona el tipo general de evento que deseas utilizar:

| Tipo de evento de conversión   | Descripción                |
|-------------------------|----------------------------|
| **Inicia la sesión**      | Se considera que un usuario se ha convertido cuando abre cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones del área de trabajo).|
| **Hace la compra**      | Se considera que un usuario se ha convertido cuando registra un [evento de compra]({{site.baseurl}}/api/objects_filters/purchase_object/). Esto realiza el seguimiento de cualquier compra de forma predeterminada, o puedes especificar un producto en particular.|
| **Pedidos realizados**        | Se considera que un usuario se ha convertido cuando desencadena el [evento recomendado «Pedido realizado» de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events?tab=ecommerce.order_placed#ecommerce-recommended-events). Esto realiza el seguimiento de cualquier pedido de forma predeterminada, o puedes filtrar por un producto específico.<br><br>El evento «Places Order» se encuentra actualmente en acceso anticipado. Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en este acceso anticipado. |
| **Lleva a cabo el evento personalizado**| Se considera que un usuario se ha convertido cuando realiza uno de sus eventos personalizados existentes (no hay ningún evento predeterminado, debe especificar el evento).|
| **Actualiza la aplicación**         | Se considera que un usuario se ha convertido cuando actualiza la versión de la aplicación en cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones del área de trabajo). Braze realiza una comparación numérica exhaustiva para determinar si el cambio ha supuesto una mejora. Las versiones no numéricas se cuentan como conversiones si cambia la versión.|
| **Abre el correo electrónico**         | Se considera que un usuario se ha convertido cuando abre el correo electrónico (sólo para campañas por correo electrónico).|
| **Hace clic en el correo electrónico**        | Se considera que un usuario se ha convertido cuando hace clic en un enlace dentro del correo electrónico (sólo para campañas por correo electrónico).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% alert important %}
**Las propiedades anidadas no son compatibles con los eventos de conversión**. No puedes utilizar propiedades anidadas en eventos de conversión. Por ejemplo, si`product_code`  o`product_name`  son propiedades anidadas dentro de una`products`matriz  (como `products[].product_code`), no puedes utilizarlas para comprobar si se ha realizado la compra de un producto específico en un evento de conversión.
{% endalert %}

Establece tu plazo de conversión. Este es el tiempo máximo que puede transcurrir antes de que Braze considere una conversión. Puedes establecer un periodo de hasta 30 días durante el cual Braze contabiliza la conversión si el usuario realiza la acción especificada.

![El tipo de evento de conversión "Realiza compra" como ejemplo para registrar conversiones de usuarios que realizan cualquier compra. Tiene un plazo de conversión de 12 horas.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Una vez seleccionados los eventos de conversión, continúa con el proceso de creación de la campaña y comienza a enviarla.

### Paso 3: Ver tus resultados

Ve a la página **Detalles** para ver los detalles de cada evento de conversión asociado a la campaña que has creado. Independientemente de los eventos de conversión seleccionados, también puedes ver los ingresos totales atribuidos a esta campaña específica, así como a variantes específicas, durante el periodo del evento de conversión primaria.

{% alert note %}
Si no seleccionas ningún evento de conversión durante la creación de la campaña, el tiempo predeterminado será de tres días.
{% endalert %}

Además, para los mensajes multivariantes, puede ver el número de conversiones y los porcentajes de conversión de su grupo de control y de cada variante.

![Cuatro eventos de conversión que realizan un seguimiento de las conversiones en función de cuándo se realizó una compra en un plazo de tres horas, se realizó una compra en un plazo de dos horas, se inició una sesión en un plazo de 30 minutos y se inició una sesión en un plazo de 25 minutos.]({% image_buster /assets/img_archive/conversion_event_details.png %})