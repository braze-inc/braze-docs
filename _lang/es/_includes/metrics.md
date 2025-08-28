{% if include.metric == "AMP Clicks" %}
<i>Clics AMP</i> es el número total de clics en tu correo electrónico AMP HTML, acumulado de las versiones HTML, texto sin formato y AMP HTML del correo electrónico.
{% endif %}

{% if include.metric == "AMP Opens" %}
<i>Aperturas AMP</i> es el recuento total de aperturas en tus versiones AMP HTML del correo electrónico y AMP HTML del correo electrónico.
{% endif %}

{% if include.metric == "Audience" %}
La <i>audiencia</i> es el porcentaje de usuarios que han recibido un mensaje concreto. Este número se recibe de Braze.
{% endif %}

{% if include.metric == "Bounces" %}
<i>Rebotes</i> es el número total de mensajes que se entregaron sin éxito a los destinatarios previstos.
{% endif %}

{% if include.metric == "Estimated Real Opens" %}
<i>Las Aperturas Reales Estimadas</i> son una estimación de cuántas aperturas únicas habría si no existieran las aperturas por máquina, y son el resultado de un modelo estadístico propio de Braze.
{% endif %}

{% if include.metric == "Help" %}
<i>Ayuda</i> es cuando un usuario ha respondido a tu mensaje con la <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">palabra clave AYUDA</a> y se le ha enviado una respuesta automática de AYUDA.
{% endif %}

{% if include.metric == "Hard Bounce" %}
Un <i>rebote duro</i> es cuando un correo electrónico no se entrega al destinatario debido a un error de entrega permanente. Un rebote duro puede producirse porque el nombre de dominio no existe o porque el destinatario es desconocido.
{% endif %}

{% if include.metric == "Soft Bounce" %}
Un <i>rebote blando</i> es cuando un correo electrónico no se entrega al destinatario debido a un error temporal de entrega, aunque la dirección de correo electrónico del destinatario sea válida. Un rebote blando puede producirse porque el buzón de entrada del destinatario está lleno, el servidor no funcionaba o el mensaje era demasiado grande para el buzón de entrada del destinatario.
{% endif %}

{% if include.metric == "Deferral" %}
Un <i>Aplazamiento</i> es cuando un correo electrónico no se ha entregado inmediatamente, pero Braze reintenta el correo electrónico hasta 72 horas después de este fallo de entrega temporal para maximizar las posibilidades de éxito en la entrega antes de que se detengan los intentos para esa campaña específica.
{% endif %}

{% if include.metric == "Body Click" %}
Las notificaciones push de historias registran un <i>clic en el cuerpo</i> cuando se hace clic en la notificación. No se grabará cuando se expanda un mensaje, o para los clics en los botones de acción.
{% endif %}

{% if include.metric == "Body Clicks" %}
<i>Los clics en el cuerpo</i> se producen cuando un usuario hace clic en un mensaje que no tiene botones (Botón 1, Botón 2) y que se creó con el editor tradicional, y cuando un mensaje creado con el editor HTML o el editor de arrastrar y soltar utiliza <code>brazeBridge.logClick()</code> sin argumentos.
{% endif %}

{% if include.metric == "Button 1 Clicks" %}
<i>Clics en el botón 1</i> es el número total de clics en el botón 1 del mensaje.
{% endif %}

{% if include.metric == "Button 2 Clicks" %}
<i>Clics en el botón 2</i> es el número total de clics en el botón 2 del mensaje.
{% endif %}

{% if include.metric == "Choices Submitted" %}
<i>Opciones enviadas</i> es el número total de opciones seleccionadas cuando el usuario hace clic en el botón enviar de la página de preguntas de un <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>cuestionario simple</a>.
{% endif %}

{% if include.metric == "Click-to-Open Rate" %}
<i>La tasa de clics abiertos</i> es el porcentaje de correos electrónicos entregados que han sido abiertos por un único usuario o máquina al menos una vez, y sólo está disponible en el <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>generador de informes</a>.
{% endif %}

{% if include.metric == "Close Message" %}
<i>Cerrar mensaje</i> es el número total de clics en el botón de cierre del mensaje. Esto sólo existe para los mensajes dentro de la aplicación creados en el editor de arrastrar y soltar, no en el editor tradicional.
{% endif %}

{% if include.metric == "Confirmed Deliveries" %}
Las <i>entregas confirmadas</i> se producen cuando el operador ha confirmado que el mensaje se ha entregado en el número de teléfono de destino.
{% endif %}

{% if include.metric == "Confidence" %}
La <i>confianza</i> es el porcentaje de confianza en que una determinada variante de un mensaje supera al grupo de control.
{% endif %}

{% if include.metric == "Confirmation Page Button" %}
<i>Botón de página</i> de confirmación es el total de clics en el botón de llamada a la acción de la página de confirmación de un <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>cuestionario simple</a>.
{% endif %}

{% if include.metric == "Confirmation Page Dismissals" %}
<i>Los descartes de la página de confirmación</i> es el total de clics en el botón de cierre (x) de la página de confirmación de un <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>cuestionario simple</a>.
{% endif %}

{% if include.metric == "Conversion Rate" %}
<i>La tasa de conversión</i> es el porcentaje de veces que se ha producido un evento definido en comparación con todos los destinatarios de un mensaje. Este evento definido se determina cuando construyes la campaña.
{% endif %}

{% if include.metric == "Conversion Window" %}
<i>La ventana de conversión</i> es el número de días después de recibir el mensaje durante los cuales se hace un seguimiento de las acciones del usuario y se atribuyen a un evento de conversión. Las conversiones que ocurren después de esta ventana no se atribuyen al evento de conversión.
{% endif %}

{% if include.metric == "Conversions (B, C, D)" %}
<i>Las conversiones (B, C, D)</i> son eventos de conversión adicionales añadidos después del evento de conversión primaria. Es el número de veces que se produjo un evento definido después de interactuar o ver un mensaje recibido de una campaña Braze.
{% endif %}

{% if include.metric == "Total Conversions" %}
<i>Conversiones totales</i> es el número total de veces que un usuario completa un evento de conversión específico después de ver una campaña de mensajería dentro de la aplicación.
{% endif %}

{% if include.metric == "Deliveries" %}
<i>Entregas</i> es el número total de solicitudes de mensajes aceptadas por el servidor receptor. Esto no significa que el mensaje se haya entregado a un dispositivo, sino que el servidor ha aceptado el mensaje.
{% endif %}

{% if include.metric == "Deliveries %" %}
<i>El % de entregas</i> es el porcentaje del número total de mensajes (Envíos) enviados y recibidos con éxito por las partes que pueden enviar correos electrónicos.
{% endif %}

{% if include.metric == "Delivery Failures" %}
<i>Los fallos de entrega</i> se producen cuando el SMS no se ha podido enviar porque se han desbordado las colas (envío de SMS a una tasa superior a la que pueden soportar tus códigos largo o abreviado).
{% endif %}

{% if include.metric == "Delivery Failures RCS" %}
<i>Los fallos de entrega</i> se producen cuando no se ha podido enviar el RCS por desbordamiento de las colas (envío de RCS a una tasa superior a la que puede soportar tu remitente verificado por RCS).
{% endif %}

{% if include.metric == "Failed Delivery Rate" %}
La <i>tasa de entregas fallidas</i> es el porcentaje de envíos que fallaron porque no se pudo enviar el mensaje. Esto puede ocurrir por varias razones, como el desbordamiento de la cola, la suspensión de la cuenta y errores de medios en el caso de los MMS.
{% endif %}

{% if include.metric == "Direct Opens" %}
<i>Direct Opens</i> es el número total de usuarios que abrieron tu aplicación o sitio web pulsando directamente la notificación.
{% endif %}

{% if include.metric == "Emailable" %}
Por <i>correo electrónico</i> se entiende el número total de usuarios que tienen registrada una dirección de correo electrónico y han optado explícitamente por ella o se han suscrito.
{% endif %}

{% if include.metric == "Errors" %}
<i>Errores</i> es el número de errores devueltos por los eventos webhook (se incrementa durante el proceso de envío).
{% endif %}

{% if include.metric == "Failures" %}
Los <i>fallos</i> se producen cuando el mensaje de WhatsApp no se ha podido enviar porque el proveedor de servicios de Internet ha devuelto un rebote duro. Un rebote duro significa un fallo permanente en la capacidad de entrega.
{% endif %}

{% if include.metric == "Influenced Opens" %}
<i>Influenced Opens</i> es el número total (y el porcentaje) de usuarios que abrieron la aplicación tras el envío de la notificación push, sin abrir directamente el push.
{% endif %}

{% if include.metric == "Lifetime Revenue" %}
Los <i>ingresos de toda la vida</i> son el total de <code>PurchaseEvents</code> valor del precio (en USD) recibido desde el inicio.
{% endif %}

{% if include.metric == "Lifetime Value Per User" %}
<i>El valor de duración por usuario</i> son los <i>ingresos de por vida</i> divididos por el total de tus <i>usuarios</i> (ubicados en tu página de inicio).
{% endif %}

{% if include.metric == "Average Daily Revenue" %}
Los <i>ingresos medios diarios</i> son la media de la suma de los ingresos de la campaña y de Canvas de un día determinado.
{% endif %}

{% if include.metric == "Daily Purchases" %}
<i>Compras diarias</i> es la media del total de compras únicas <code>PurchaseEvents</code> a lo largo del periodo de tiempo.
{% endif %}

{% if include.metric == "Daily Revenue Per User" %}
Los <i>ingresos diarios por usuario</i> son los ingresos medios diarios por usuario activo diario.
{% endif %}

{% if include.metric == "Machine Opens" %}
<i>Aperturas de máquina</i> incluye la proporción de "aperturas" que se ven afectadas por la Protección de la privacidad en los correos electrónicos (MPP) de Apple para iOS 15. Por ejemplo, si un usuario abre un correo electrónico utilizando la aplicación Mail en un dispositivo Apple, esto se registrará como una <i>Máquina Abierta</i>.
{% endif %}

{% if include.metric == "Other Opens" %}
<i>Otras aperturas</i> incluye correos electrónicos que no han sido identificados como <i>aperturas de máquina</i>. Por ejemplo, cuando un usuario abre un correo electrónico en otra plataforma (como la aplicación de Gmail en un teléfono, Gmail en un navegador de escritorio), esto se registrará como <i>Otras aperturas</i>.
{% endif %}

{% if include.metric == "Opens" %}
<i>Las aperturas</i> son instancias que incluyen tanto <i>Direct Opens</i> como <i>Influenced Opens</i> en las que el SDK de Braze ha determinado, mediante un algoritmo propio, que una notificación push ha provocado que un usuario abra la aplicación.
{% endif %}

{% if include.metric == "Opt-Out" %}
La <i>exclusión voluntaria</i> se produce cuando un usuario responde a tu mensaje con una <a href="https://braze.com/docs/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#default-opt-in-opt-out-keywords">palabra clave de exclusión voluntaria</a> y se da de baja de tu programa de SMS o RCS.
{% endif %}

{% if include.metric == "Pending Retry" %}
El <i>reintento pendiente</i> hace referencia al número de solicitudes que fueron rechazadas temporalmente por el servidor receptor, pero que el proveedor de servicios de correo electrónico (ESP) intentó volver a entregar. El ESP reintentará la entrega hasta que se alcance un tiempo de espera (normalmente después de 72 horas).
{% endif %}

{% if include.metric == "Primary Conversions (A) or Primary Conversion Event" %}
<i>Conversiones primarias (A)</i> o <i>evento de conversión primaria</i> es el número de veces que se ha producido un evento definido tras interactuar o ver un mensaje recibido de una campaña Braze. Este evento definido lo determinas tú al crear la campaña.
{% endif %}

{% if include.metric == "Reads" %}
<i>Lee</i> es cuando el usuario lee el mensaje. Los recibos de lectura del usuario deben estar "Activados" para que Braze realice un seguimiento de las lecturas.
{% endif %}

{% if include.metric == "Read Rate" %}
<i>La tasa de lectura</i> es el porcentaje de envíos que dieron lugar a una lectura. Sólo se da a los usuarios que tienen activados los recibos de lectura.
{% endif %}

{% if include.metric == "Received" %}
<i>La recepción</i> se define de forma diferente según el canal, y puede ser cuando los usuarios ven el mensaje, los usuarios realizan una acción desencadenante definida o el mensaje se envía al proveedor de mensajes.
{% endif %}

{% if include.metric == "Rejections" %}
<i>Los rechazos</i> se producen cuando el SMS o RCS ha sido rechazado por el operador. Esto puede ocurrir por varias razones, como el filtrado de contenidos del operador, la disponibilidad del dispositivo de destino, que el número de teléfono ya no esté en servicio, y similares.
{% endif %}

{% if include.metric == "Revenue" %}
Los <i>ingresos</i> son los ingresos totales en dólares de los destinatarios de la campaña dentro de la <a href='/docs/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events'>ventana de conversión primaria</a> establecida.
{% endif %}

{% if include.metric == "Messages Sent" %}
<i>Mensajes enviados</i> es el número total de mensajes enviados en una campaña. Tras lanzar una campaña programada, esta métrica incluirá todos los mensajes enviados, independientemente de si se han enviado ya debido a la limitación de tasa. Esto no significa que el mensaje se haya recibido o entregado a un dispositivo, sólo que el mensaje se ha enviado.
{% endif %}

{% if include.metric == "Sent" %}
Se <i>envía</i> cada vez que se ha lanzado o desencadenado una campaña o un paso en Canvas, y se ha enviado un SMS o RCS desde Braze. Es posible que el SMS o RCS no haya llegado al dispositivo de un usuario debido a errores.
{% endif %}

{% if include.metric == "Sends" %}
<i>Envíos</i> es el número total de mensajes enviados en una campaña. Tras lanzar una campaña programada, esta métrica incluirá todos los mensajes enviados, independientemente de si se han enviado ya debido a la limitación de tasa. Esto no significa que el mensaje se haya recibido o entregado a un dispositivo, sólo que el mensaje se ha enviado.
{% endif %}

{% if include.metric == "Sends to Carrier" %}
<i>Enviar al operador</i> está obsoleto, pero seguirá siendo compatible para los usuarios que ya lo tengan. Es la suma de las <i>Entregas Confirmadas</i>, los <i>Rechazos</i> y los <i>Envíos</i> cuya entrega o rechazo no fue confirmado por el operador. Esto incluye las instancias en las que los operadores no proporcionan la confirmación de entrega o rechazo, ya que algunos operadores no proporcionan esta confirmación o no pueden hacerlo en el momento del envío.
{% endif %}

{% if include.metric == "Sends to Carrier Rate" %}
<i>La tasa de envíos al operador</i> es el porcentaje del total de mensajes enviados que se clasificaron como <i>envíos al operador</i>. Esto incluye las instancias en las que los operadores no proporcionan confirmación de entrega o rechazo, ya que algunos operadores no proporcionan esta confirmación o no pueden hacerlo en el momento del envío. Esta métrica está obsoleta, pero seguirá siendo compatible para los usuarios que ya la tengan.
{% endif %}

{% if include.metric == "Spam" %}
<i>Spam</i> es el número total de correos electrónicos entregados que fueron marcados como "spam" por el destinatario. Aunque Braze no cambia el estado de suscripción de estos usuarios, estos usuarios serán excluidos automáticamente en futuros correos electrónicos, a menos que estés enviando un correo electrónico transaccional, que esté configurado para "enviar a todos los usuarios, incluida la cancelación suscripción".
{% endif %}

{% if include.metric == "Survey Page Dismissals" %}
<i>Los descartes de la página del cuestionario</i> es el total de clics en el botón cerrar (x) de la página de preguntas de un <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>cuestionario simple</a>.
{% endif %}

{% if include.metric == "Survey Submissions" %}
<i>Los envíos de encuestas</i> son el total de clics en el botón de envío de un <a href='https://braze.com/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/'>cuestionario simple</a>.
{% endif %}

{% if include.metric == "Total Clicks" %}
<i>Clics totales</i> es el número de destinatarios únicos que hicieron clic en un enlace del mensaje entregado.
{% endif %}

{% if include.metric == "Total Dismissals" %}
<i>El total de descartes</i> es el número de veces que se han descartado tarjetas de contenido de una campaña.
{% endif %}

{% if include.metric == "Total Impressions" %}
<i>El total de impresiones</i> es el número de veces que el mensaje se ha cargado y aparece en la pantalla de un usuario, independientemente de la interacción previa (por ejemplo, si a un usuario se le muestra un mensaje dos veces, se le contará dos veces).
{% endif %}

{% if include.metric == "Total Opens" %}
<i>Aperturas totales</i> es el número total de mensajes que se abrieron.
{% endif %}

{% if include.metric == "Total Revenue" %}
<i>Los ingresos totales</i> son los ingresos totales en dólares de los destinatarios de la campaña dentro de la ventana de conversión primaria establecida.
{% endif %}

{% if include.metric == "Unique Clicks" %}
<i>Clics únicos</i> es el número distinto de destinatarios que han hecho clic en un enlace dentro de un mensaje al menos una vez y se mide por <a href='https://braze.com/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>.
{% endif %}

{% if include.metric == "Unique Dismissals" %}
<i>Descartes únicos</i> es el número de destinatarios únicos que descartaron una tarjeta de contenido de una campaña. Un usuario que descarta varias veces una tarjeta de contenido de una campaña representa un único descarte.
{% endif %}

<!-- Unique Impressions & Unique Recipients have a dedicated section in campaign_analytics.md -->

{% if include.metric == "Unique Impressions" %}
Las <i>impresiones únicas</i> son el número total de usuarios que recibieron y vieron un mensaje de una campaña determinada.
{% endif %}

{% if include.metric == "Unique Recipients" %}
<i>Destinatarios únicos</i> es el número de destinatarios únicos diarios, o usuarios que recibieron un mensaje nuevo en un día. Para que este recuento se incremente para un usuario más de una vez, el usuario debe recibir un nuevo mensaje en un día diferente.
{% endif %}

{% if include.metric == "Unique Opens" %}
<i>Unique Opens</i> es el número total de mensajes entregados que han sido abiertos por un único usuario al menos una vez y que son objeto de seguimiento durante un periodo de siete días.
{% endif %}

{% if include.metric == "Unsubscribers or Unsub" %}
<i>Desuscritos</i> o <i>Cancelar suscripción</i> es el número de mensajes que dan lugar a una cancelación de suscripción. Las cancelaciones de suscripción se producen cuando un usuario hace clic en el enlace Braze cancelar suscripción.
{% endif %}

{% if include.metric == "Unsubscribes" %}
<i>Desuscritos</i> es el número de destinatarios cuyo estado de suscripción cambió a cancelado como resultado de hacer clic en la URL de cancelación de suscripción proporcionada por Braze.
{% endif %}

{% if include.metric == "Variation" %}
<i>Variación</i> es el número de variaciones de una campaña, diferentes según las defina el creador.
{% endif %}
