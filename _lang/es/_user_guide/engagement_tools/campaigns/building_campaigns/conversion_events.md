---
nav_title: Eventos de conversión
article_title: Eventos de conversión
page_order: 5
page_type: tutorial
description: "Este artículo define los eventos de conversión, cómo utilizarlos y definir sus métricas de éxito en Braze, y cómo utilizar estas herramientas para ver el grado de compromiso de sus usuarios."
tool: Campaigns

---
# Eventos de conversión

> Los eventos de conversión se pueden utilizar para asegurarse de que está recopilando información relevante y útil que más tarde podrá utilizar para obtener información para su campaña. 

Para realizar un seguimiento de las métricas de participación y los detalles necesarios sobre cómo la mensajería impulsa sus KPI, Braze le permite establecer eventos de conversión para cada una de sus campañas y Canvases.

Un evento de conversión es un tipo de métrica de éxito que registra si un destinatario de su mensaje realiza una acción de alto valor en un periodo de tiempo determinado tras recibir su mensaje. Con esto, puede empezar a atribuir estas acciones de valor a los diferentes puntos de compromiso que llegan al usuario. 

Por ejemplo, si está creando una campaña navideña personalizada para usuarios activos, un evento de conversión de **Iniciar una sesión** en un plazo de dos o tres días puede ser adecuado, ya que le permitirá recopilar una sensación de compromiso del usuario al recibir su mensaje. Eventos adicionales como **Realizar Compra**, **Actualizar Aplicación**, o cualquiera de sus eventos personalizados pueden ser seleccionados como eventos de conversión.

Para más información sobre conversiones, consulte nuestro [curso Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuración de campañas.

## Evento de conversión primaria

El evento de conversión principal es el primer evento añadido durante la creación de la campaña o del Canvas. Este acontecimiento es el que más influye en tu compromiso y tus informes. Su evento de conversión primaria se utiliza para:

- Calcule la variación del mensaje ganador en [campañas multivariantes][4] o Canvases.
- Determina la ventana en la que se calculan los ingresos para la campaña o el Canvas.
- Ajuste la distribución de mensajes para campañas y lonas mediante [Selección inteligente][5].

{% alert note %}
Si los mensajes se cancelan utilizando la etiqueta de Liquid `abort`, solo se cancelan potencialmente los usuarios que pasan por variantes. Esto significa que los mensajes a los usuarios que pasen por el grupo de control no se abortarán, lo que puede dar lugar a porcentajes de conversión sesgados entre las variantes y los grupos de control. Como solución, utilice [la segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment) para dirigirse a sus usuarios en la campaña y en la entrada de Canvas.
{% endalert %}

## Paso 1: Crear una campaña con seguimiento de conversiones

[Cree una campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) para el canal de mensajería que desee. Después de configurar los mensajes y el calendario de su campaña, tendrá la opción de añadir hasta cuatro eventos de conversión para su seguimiento.

Le recomendamos encarecidamente que utilice tantos eventos de conversión como considere necesario, ya que la adición de un segundo (o tercer) evento de conversión puede enriquecer significativamente sus informes. Por ejemplo, supongamos que tienes una campaña dirigida a usuarios inactivos. En este caso, añadir un evento de conversión secundario y el evento de conversión primario **Inicio de sesión** puede ayudarle a comprender mejor la eficacia de su campaña a la hora de hacer que los usuarios vuelvan a su aplicación. 

## Paso 2: Añadir eventos de conversión

Para cada evento de conversión que quieras seguir, selecciona el evento y la fecha límite de conversión.

1. Seleccione el tipo general de evento que desea utilizar:
  - **Comienza la sesión**: Se considera que un usuario se ha convertido cuando abre cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones del área de trabajo).
  - **Hace la compra**: Se considera que un usuario se ha convertido cuando compra el producto que especifique (por defecto, cualquier producto).
  - **Realiza un evento personalizado**: Se considera que un usuario se ha convertido cuando realiza uno de sus eventos personalizados existentes (no hay ningún evento predeterminado, debe especificar el evento).
  - **Actualiza la aplicación**: Se considera que un usuario se ha convertido cuando actualiza la versión de la aplicación en cualquiera de las aplicaciones que especifiques (por defecto, todas las aplicaciones del área de trabajo). Braze realizará una comparación numérica de los mejores esfuerzos para determinar si el cambio de versión fue una actualización. Por ejemplo, un usuario se convertiría si actualiza de la versión 1.2.3 a la 1.3.0 de la aplicación, pero Braze no registraría una conversión si un usuario baja de la versión 1.2.3 a la 1.2.2. Sin embargo, si el nombre de la versión de la aplicación contiene cadenas, como "1.2.3-beta2", Braze no podrá determinar si un cambio de versión ha sido una actualización. En esta situación, Braze contará como conversión cuando cambie la versión más reciente de la aplicación del usuario.
  - **Abre el correo electrónico**: Se considera que un usuario se ha convertido cuando abre el correo electrónico (sólo para campañas por correo electrónico).
  - **Haz clic en el correo electrónico**: Se considera que un usuario se ha convertido cuando hace clic en un enlace dentro del correo electrónico (sólo para campañas por correo electrónico).<br><br>
2. Establece tu plazo de conversión. Es el plazo máximo que puede transcurrir para considerar una conversión. Tiene la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará la conversión si el usuario realiza la acción especificada.  

![El tipo de evento de conversión "Realiza compra" como ejemplo para registrar conversiones de usuarios que realizan cualquier compra. Tiene un plazo de conversión de 12 horas.][2]

Una vez que haya seleccionado los eventos de conversión, continúe con el proceso de creación de la campaña y comience a enviarla.

## Paso 3: Ver resultados

Vaya a la página **Detalles** para ver los detalles de cada evento de conversión asociado a la campaña que acaba de crear. Independientemente de los eventos de conversión seleccionados, también puede ver los ingresos totales que pueden atribuirse a esta campaña específica, así como a variantes específicas, durante la ventana del evento de conversión principal.

{% alert note %}
Si no hay eventos de conversión seleccionados durante la creación de la campaña, el tiempo por defecto es de tres días.
{% endalert %}

Además, para los mensajes multivariantes, puede ver el número de conversiones y los porcentajes de conversión de su grupo de control y de cada variante.

![][3]

## Reglas de seguimiento de conversiones

Los eventos de conversión te permiten atribuir la acción del usuario a un punto de participación. Dicho esto, hay que tener en cuenta algunas cosas sobre cómo Braze gestiona las conversiones múltiples. Eche un vistazo a los siguientes escenarios para comprender cómo Braze realiza el seguimiento de estas conversiones:

- Las conversiones se producen por usuario, no por dispositivo. Esto significa que un usuario sólo puede convertir una vez, aunque un mensaje se envíe a varios dispositivos. Como otro ejemplo, supongamos que una campaña sólo tiene un evento de conversión que es "Realiza cualquier compra". Si un usuario que recibe esta campaña realiza dos compras distintas dentro del plazo de conversión, sólo se contabilizará una conversión.
- Si un usuario realiza un evento de conversión dentro de los plazos de conversión de dos campañas o lienzos distintos que haya recibido, la conversión se registrará en ambos.
- Un usuario contará como convertido si realizó el evento de conversión específico en la ventana aunque no haya abierto o hecho clic en el mensaje.

[2]: {% image_buster /assets/img_archive/conversion_event_selection.png %}
[3]: {% image_buster /assets/img_archive/conversion_event_details.png %}
[4]: {{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/#multivariate-and-ab-testing
[5]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
