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

Digamos que estás creando una campaña personalizada de vacaciones para usuarios activos, un evento de conversión de **Iniciar una sesión** en un plazo de dos o tres días puede ser adecuado, ya que te permitirá reunir una sensación de interacción del usuario al recibir tu mensaje. Eventos adicionales como **Realizar Compra**, **Actualizar Aplicación**, o cualquiera de sus eventos personalizados pueden ser seleccionados como eventos de conversión.

{% alert tip %}
Para saber más sobre conversiones, consulta nuestro [curso de Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.
{% endalert %}

### Reglas de seguimiento de conversiones

Los eventos de conversión te permiten atribuir la acción del usuario a un punto de participación. Dicho esto, hay que tener en cuenta algunas cosas sobre cómo Braze gestiona las conversiones múltiples. Eche un vistazo a los siguientes escenarios para comprender cómo Braze realiza el seguimiento de estas conversiones:

- Las conversiones se producen por usuario, no por dispositivo. Esto significa que un usuario sólo puede convertir una vez, aunque un mensaje se envíe a varios dispositivos. Como otro ejemplo, supongamos que una campaña sólo tiene un evento de conversión que es "Realiza cualquier compra". Si un usuario que recibe esta campaña realiza dos compras distintas dentro del plazo de conversión, sólo se contabilizará una conversión.
- Si un usuario realiza un evento de conversión dentro de los plazos de conversión de dos campañas o lienzos distintos que haya recibido, la conversión se registrará en ambos.
- Un usuario contará como convertido si realizó el evento de conversión específico en la ventana aunque no haya abierto o hecho clic en el mensaje.

### Evento de conversión primaria

El evento de conversión principal es el primer evento añadido durante la creación de la campaña o del Canvas. Este acontecimiento es el que más influye en tu compromiso y tus informes. Su evento de conversión primaria se utiliza para:

- Calcula la variación del mensaje ganador en campañas [multivariantes]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing) o Lienzos.
- Determina la ventana en la que se calculan los ingresos para la campaña o el Canvas.
- Ajusta la distribución de mensajes para campañas y Lienzos mediante [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% alert note %}
Si los mensajes se cancelan utilizando la etiqueta de Liquid `abort`, solo se cancelan potencialmente los usuarios que pasan por variantes. Esto significa que los mensajes a los usuarios que pasen por el grupo de control no se abortarán, lo que puede dar lugar a porcentajes de conversión sesgados entre las variantes y los grupos de control. Como solución, utilice [la segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) para dirigirse a sus usuarios en la campaña y en la entrada de Canvas.
{% endalert %}

## Crear una campaña con seguimiento de conversiones

### Paso 1: Configura tu campaña

[Cree una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) para el canal de mensajería que desee. Después de configurar los mensajes y el calendario de su campaña, tendrá la opción de añadir hasta cuatro eventos de conversión para su seguimiento.

Te recomendamos que utilices tantos eventos de conversión como consideres necesario, ya que la adición de un segundo (o tercer) evento de conversión puede enriquecer significativamente tus informes. Por ejemplo, supongamos que tienes una campaña dirigida a usuarios inactivos. En este caso, añadir un evento de conversión secundario y el evento de conversión primario **Inicio de sesión** puede ayudarle a comprender mejor la eficacia de su campaña a la hora de hacer que los usuarios vuelvan a su aplicación. 

### Paso 2: Añade los eventos de conversión

Primero, selecciona el tipo general de evento que te gustaría utilizar:

| Tipo de evento de conversión         | Descripción                                                                                                                                                                                                                                                                                                                                 |
|-------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Inicia la sesión**      | Se considera que un usuario se ha convertido cuando abre cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones del área de trabajo).                                                                                                                                                                                                         |
| **Hace la compra**      | Se considera que un usuario se ha convertido cuando compra el producto que especifique (por defecto, cualquier producto).                                                                                                                                                                                                                                 |
| **Lleva a cabo el evento personalizado** | Se considera que un usuario se ha convertido cuando realiza uno de sus eventos personalizados existentes (no hay ningún evento predeterminado, debe especificar el evento).                                                                                                                                                                                                        |
| **Actualiza la aplicación**         | Se considera que un usuario se ha convertido cuando actualiza la versión de la aplicación en cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones del área de trabajo). Braze realiza una comparación numérica de los mejores esfuerzos para determinar si el cambio fue una mejora. Las versiones no numéricas se cuentan como conversiones si cambia la versión.              |
| **Abre el correo electrónico**         | Se considera que un usuario se ha convertido cuando abre el correo electrónico (sólo para campañas por correo electrónico).                                                                                                                                                                                                                                                 |
| **Hace clic en el correo electrónico**        | Se considera que un usuario se ha convertido cuando hace clic en un enlace dentro del correo electrónico (sólo para campañas por correo electrónico).                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Establece tu plazo de conversión. Es el plazo máximo que puede transcurrir para considerar una conversión. Tiene la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará la conversión si el usuario realiza la acción especificada.

![El tipo de evento de conversión "Realiza compra" como ejemplo para registrar conversiones de usuarios que realizan cualquier compra. Tiene un plazo de conversión de 12 horas.]({% image_buster /assets/img_archive/conversion_event_selection.png %})

Cuando hayas seleccionado los eventos de conversión, continúa con el proceso de creación de la campaña y comienza a enviarla.

### Paso 3: Ver tus resultados

Vaya a la página **Detalles** para ver los detalles de cada evento de conversión asociado a la campaña que acaba de crear. Independientemente de los eventos de conversión seleccionados, también puede ver los ingresos totales que pueden atribuirse a esta campaña específica, así como a variantes específicas, durante la ventana del evento de conversión principal.

{% alert note %}
Si no hay eventos de conversión seleccionados durante la creación de la campaña, el tiempo por defecto es de tres días.
{% endalert %}

Además, para los mensajes multivariantes, puede ver el número de conversiones y los porcentajes de conversión de su grupo de control y de cada variante.

![Cuatro eventos de conversión que realizan un seguimiento de las conversiones en función de cuándo se realizó una compra en un plazo de tres horas, se realizó una compra en un plazo de dos horas, se inició una sesión en un plazo de 30 minutos y se inició una sesión en un plazo de 25 minutos.]({% image_buster /assets/img_archive/conversion_event_details.png %})


