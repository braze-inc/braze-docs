---
nav_title: Eventos de conversión
article_title: Eventos de conversión
page_order: 4
page_type: reference
description: "Este artículo de referencia define los eventos de conversión, cómo utilizarlos para definir tus métricas de éxito en Braze, y cómo utilizar estos eventos para ver el grado de interacción de tus usuarios."
tool:
    - Campaigns
    - Canvas
---

# Eventos de conversión

> Un evento de conversión es un tipo de métrica de éxito que realiza un seguimiento de si un destinatario de tu mensajería realiza una acción de alto valor en un tiempo determinado tras recibir tu interacción. Utiliza estos eventos para asegurarte de que estás recopilando información relevante y útil que luego puedas utilizar para obtener información para tu campaña o Canvas.

## Cómo funciona

Digamos que estás creando una campaña personalizada de vacaciones para usuarios activos, un evento de conversión de **Iniciar una sesión** en un plazo de dos o tres días puede ser adecuado, ya que te permitirá reunir una sensación de interacción del usuario al recibir tu mensaje. Eventos adicionales como **Realizar compra**, **Actualizar aplicación** o cualquiera de tus eventos personalizados pueden seleccionarse como eventos de conversión.

{% alert tip %}
Para saber más sobre conversiones, consulta nuestro [curso de Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.
{% endalert %}

### Reglas de seguimiento de la conversión

Los eventos de conversión te permiten atribuir la acción del usuario a un punto de interacción. Dicho esto, hay que tener en cuenta algunas cosas sobre cómo Braze gestiona las conversiones múltiples. Echa un vistazo a los siguientes escenarios para entender cómo Braze realiza el seguimiento de estas conversiones:

- Las conversiones se producen por usuario, no por dispositivo. Esto significa que un usuario sólo puede convertir una vez, aunque un mensaje se envíe a varios dispositivos. Como otro ejemplo, supón que una campaña sólo tiene un evento de conversión que es "Realiza cualquier compra". Si un usuario que recibe esta campaña realiza dos compras distintas dentro del plazo de conversión, sólo se contabilizará una conversión.
- Si un usuario realiza un evento de conversión dentro de los plazos de conversión de dos campañas o Canvases distintos que haya recibido, la conversión se registrará en ambos.
- Un usuario contará como convertido si realizó el evento de conversión específico en la ventana aunque no abriera ni hiciera clic en el mensaje.
- En el caso de los Canvas, el seguimiento de la conversión se basa en el plazo final de conversión que comienza cuando un usuario entra en el Canvas, no en el tiempo de los mensajes individuales. Esto significa que las conversiones pueden contarse incluso durante los periodos de retraso entre mensajes en Canvas.

### Evento de conversión primaria

El evento de conversión primaria es el primer evento que se añade durante la creación de la campaña o del Canvas. Este acontecimiento es el que más influye en tu compromiso y tus informes. Tu evento de conversión primaria se utiliza para:

- Calcula la variación del mensaje ganador en campañas [multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) o Lienzos.
- Determina la ventana en la que se calculan los ingresos de la campaña o Canvas.
- Ajusta la distribución de mensajes para campañas y Lienzos mediante [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% alert note %}
Si los mensajes se cancelan utilizando la etiqueta de Liquid `abort`, sólo se cancelan potencialmente los usuarios que pasan por variantes. Esto significa que los mensajes a los usuarios que pasen por el grupo de control no se abortarán, lo que puede dar lugar a porcentajes de conversión sesgados entre las variantes y los grupos de control. Como solución, utiliza [la segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) para dirigirte a tus usuarios a la entrada de la campaña y de Canvas.
{% endalert %}

## Crear una campaña con seguimiento de la conversión

### Paso 1: Configura tu campaña

[Crea una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) para el canal de mensajería que desees. Tras configurar los mensajes y el calendario de tu campaña, tendrás la opción de añadir hasta cuatro eventos de conversión para su seguimiento.

Te recomendamos que utilices tantos eventos de conversión como consideres necesario, ya que la adición de un segundo (o tercer) evento de conversión puede enriquecer significativamente tus informes. Por ejemplo, supongamos que tienes una campaña dirigida a usuarios rezagados. En este caso, añadir un evento de conversión secundario y el evento de conversión **Sesión de inicio** primario puede ayudarte a comprender mejor la eficacia de tu campaña a la hora de hacer que tus usuarios vuelvan a tu aplicación. 

### Paso 2: Añade los eventos de conversión

Primero, selecciona el tipo general de evento que te gustaría utilizar:

| Tipo de evento de conversión         | Descripción                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Comienza la sesión**      | Se considera que un usuario se ha convertido cuando abre cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones del espacio de trabajo).                                                                                                                                                                                                         |
| **Realiza la compra**      | Se considera que un usuario se ha convertido cuando compra el producto que especifiques (por defecto, cualquier producto).                                                                                                                                                                                                                                 |
| **Realiza un evento personalizado** | Se considera que un usuario se ha convertido cuando realiza uno de tus eventos personalizados existentes (no está predeterminado, debes especificar el evento).                                                                                                                                                                                                        |
| **Actualizar aplicación**         | Se considera que un usuario se ha convertido cuando actualiza la versión de la aplicación en cualquiera de las aplicaciones que especifiques (por defecto, en todas las aplicaciones del espacio de trabajo). Braze realiza una comparación numérica de los mejores esfuerzos para determinar si el cambio fue una mejora. Las versiones no numéricas se cuentan como conversiones si cambia la versión.              |
| **Abre el correo electrónico**         | Se considera que un usuario se ha convertido cuando abre el correo electrónico (sólo para campañas por correo electrónico).                                                                                                                                                                                                                                                 |
| **Clics correo electrónico**        | Se considera que un usuario se ha convertido cuando hace clic en un enlace dentro del correo electrónico (sólo para campañas por correo electrónico).                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Establece tu plazo de conversión. Es el tiempo máximo que puede transcurrir para considerar una conversión. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará la conversión si el usuario realiza la acción especificada.

\![El tipo de evento de conversión "Realiza una compra" como ejemplo para registrar las conversiones de los usuarios que realizan cualquier compra. Tiene un plazo de conversión de 12 horas.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Cuando hayas seleccionado los eventos de conversión, continúa con el proceso de creación de la campaña y comienza a enviarla.

### Paso 3: Ver tus resultados

Ve a la página **Detalles** para ver los detalles de cada evento de conversión asociado a la campaña que acabas de crear. Independientemente de los eventos de conversión seleccionados, también puedes ver los ingresos totales que pueden atribuirse a esta campaña concreta, así como a variantes específicas, durante la ventana del evento de conversión primaria.

{% alert note %}
Si no hay eventos de conversión seleccionados durante la creación de la campaña, el tiempo predeterminado es de tres días.
{% endalert %}

Además, para los mensajes multivariantes, puedes ver el número de conversiones y los porcentajes de conversión de tu grupo de control y de cada variante.

Cuatro eventos de conversión que realizan un seguimiento de las conversiones en función de cuándo se realizó una compra en un plazo de tres horas, cuándo se realizó una compra en un plazo de dos horas, cuándo se inició una sesión en un plazo de 30 minutos y cuándo se inició una sesión en un plazo de 25 minutos.]({% image_buster /assets/img_archive/conversion_event_details.png %})


