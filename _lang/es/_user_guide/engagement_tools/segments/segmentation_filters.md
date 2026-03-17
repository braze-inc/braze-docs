---
page_order: 2
nav_title: Filtros de segmentación
article_title: Filtros de segmentación
layout: glossary_page
glossary_top_header: "Filtros de segmentación"
glossary_top_text: "El SDK de Braze te ofrece un potente arsenal de filtros para segmentar y dirigirte a tus usuarios en función de características y atributos específicos. Puedes buscar o limitar estos filtros por categoría de filtrado.<br><br>Para obtener más información sobre los diferentes tipos de datos de atributos personalizados que puedes utilizar para la segmentación de usuarios, consulta <a href=\"/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types\">Tipos de datos de atributos personalizados</a>."

page_type: glossary
tool: Segments
description: "Este glosario enumera los filtros disponibles para segmentar y orientar a sus usuarios."
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
# NOTE: glossary_tags names must match the "tags" under each glossary entry exactly (filter/checkbox logic).
glossary_tags:
  - name: Membresía de segmento o de CSV
  - name: Atributo personalizado
  - name: Eventos personalizados
  - name: Sesiones
  - name: Reorientación
  - name: Comportamiento de suscripción al canal
  - name: Comportamiento de compra
  - name: Comercio electrónico
  - name: Atributos demográficos
  - name: Aplicación
  - name: Desinstalar
  - name: Dispositivos
  - name: Ubicación
  - name: Membresía de cohorte
  - name: Atribución de instalación
  - name: Inteligencia y predicción
  - name: Actividad social
  - name: Otros filtros
  - name: Casos de uso de publicidad
  - name: Atributos de usuario

glossaries:
  - name: Membresía de Segment
    description: "Le permite filtrar en función de la pertenencia a un segmento en cualquier lugar en el que se utilicen filtros (como segmentos, campañas y otros) y dirigirse a varios segmentos diferentes dentro de una misma campaña. <br><br>Ten en cuenta que los segmentos que ya utilizan este filtro no pueden incluirse más ni anidarse en otros segmentos, porque esto puede crear un ciclo en el que el segmento A incluya al segmento B, que a su vez intentará incluir de nuevo al segmento A. Si eso ocurriera, el segmento seguiría haciendo referencia a sí mismo, haciendo imposible calcular quién pertenece realmente a él. Además, anidar segmentos de este modo añade complejidad y puede ralentizar las cosas. En su lugar, recrea el segmento que intentas incluir utilizando los mismos filtros."
    tags:
      - Membresía de segmento o de CSV
  - name: Extensiones de segmento de Braze
    description: "Después de crear una extensión de segmento en el panel de control de Braze, puede elegir incluir/excluir esas extensiones en su segmento."
    tags:
      - Membresía de segmento o de CSV
  - name: Actualizado/Importado desde un CSV
    description: Segmenta a sus usuarios en función de si formaron parte o no de una carga CSV.
    tags:
      - Membresía de segmento o de CSV
  - name: Atributos personalizados
    description: "Determina si un usuario coincide o no con un valor de atributo registrado personalizado. <br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Atributo personalizado
  - name: Creado el
    description: "Segmenta a los usuarios en función de cuándo se creó su perfil de usuario. Si un usuario se añadió por CSV o API, este filtro refleja la fecha en que se añadió. Si el usuario no está añadido por CSV o API y tiene su primera sesión seguida por el SDK, entonces este filtro refleja la fecha de esa primera sesión."
    tags:
      - Otros filtros
  - name: Atributos personalizados anidados
    description: "Atributos que son las propiedades de los atributos personalizados.<br><br>Al filtrar un atributo personalizado de hora anidado, puede elegir filtrar en función del \"Día del año\" o de la \"Hora\". «Día del año» solo comprueba el mes y el día para la comparación. «Time» compara la marca de tiempo completa, incluido el año."
    tags:
      - Atributo personalizado
  - name: Día del evento recurrente
    description: "Este filtro mira el mes y el día del atributo personalizado con el tipo de dato \"fecha\", pero no mira el año. Este filtro es útil para eventos anuales.<br><br>Zona horaria:<br>Este filtro se ajusta a la zona horaria en la que se encuentre el usuario, siempre y cuando el mensaje se envíe utilizando la opción de programación por hora local; de lo contrario, este filtro utiliza la zona horaria de tu empresa."
    tags:
      - Atributo personalizado
  - name: Evento personalizado
    description: "Determina si un usuario ha realizado o no un evento especialmente registrado.<br><br> Ejemplo:<br>Actividad completada con la propiedad activity_name.<br><br>Zona horaria:<br>UTC - Día del calendario = 1 día del calendario analiza entre 24 y 48 horas del historial del usuario."
    tags:
      - Eventos personalizados
  - name: Primer evento personalizado hecho
    description: "Determina la hora más temprana a la que un usuario ha realizado un evento especialmente registrado. (período de 24 horas) <br><br>Ejemplo:<br> Primer carro abandonado Hace menos de 1 día<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Eventos personalizados
  - name: Último evento personalizado hecho 
    description: "Determina la última vez que un usuario ha realizado un evento especialmente registrado. Este filtro admite decimales, como 0,25 horas. (período de 24 horas) <br><br>Ejemplo:<br> Último carro abandonado Hace menos de 1 día<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Eventos personalizados
  - name: Evento personalizado X en Y días
    description: "Determina si un usuario ha realizado o no un evento especialmente registrado entre 0 y 50 veces en el último número especificado de días naturales entre 1 y 30. (Día del calendario = 1 día del calendario analiza entre 24 y 48 horas del historial del usuario)<br> <a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a> <br><br>Ejemplo:<br>Carrito abandonado exactamente 0 veces en el último 1 día calendario<br><br>Zona horaria:<br>UTC: para tener en cuenta todas las zonas horarias, un día natural analiza entre 24 y 48 horas del historial del usuario, dependiendo de la hora en que se evalúe el segmento; para dos días naturales, analiza entre 48 y 72 horas del historial del usuario, y así sucesivamente."
    tags:
      - Eventos personalizados
  - name: Propiedad de evento personalizado X en Y días
    description: "Determina si un usuario ha realizado o no un evento especialmente registrado en relación con una propiedad específica entre 0 y 50 veces en el último número especificado de días naturales entre 1 y 30. (Día del calendario = 1 día del calendario analiza entre 24 y 48 horas del historial del usuario)<br><a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a> <br><br>Ejemplo:<br> Añadido a Favoritos con la propiedad \"nombre_evento\" exactamente 0 veces en el último 1 día natural<br><br>Zona horaria:<br>UTC: para tener en cuenta todas las zonas horarias, un día natural analiza entre 24 y 48 horas del historial del usuario, dependiendo de la hora en que se evalúe el segmento; para dos días naturales, analiza entre 48 y 72 horas del historial del usuario, y así sucesivamente."
    tags:
      - Eventos personalizados
  - name: Dirección de correo electrónico 
    description: "Le permite designar los destinatarios de su campaña por direcciones de correo electrónico individuales para realizar pruebas. Esto también se puede utilizar para enviar correos electrónicos transaccionales a todos tus usuarios (incluidos los que han cancelado la suscripción) utilizando el especificador «La dirección de correo electrónico no está en blanco» dentro del filtro, de modo que puedas maximizar la entrega de correos electrónicos independientemente del estado de adhesión voluntaria. <br><br>Este filtro solo comprueba si los perfiles de usuario tienen una dirección de correo electrónico, mientras que el filtro <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">Correo electrónico disponible</a> comprueba criterios adicionales."
    tags:
      - Otros filtros
  - name: ID de usuario externo
    description: Le permite designar los destinatarios de sus campañas por ID de usuario individuales para realizar pruebas.
    tags:
      - Otros filtros
  - name: "# Contenedor aleatorio"
    description: Segmenta a tus usuarios por un número asignado aleatoriamente (de 0 a 9999 inclusive). Puede permitir la creación de segmentos uniformemente distribuidos de usuarios verdaderamente aleatorios para pruebas A/B y multivariantes.
    tags:
      - Otros filtros
  - name: Recuento de sesiones
    description: Segmenta a tus usuarios por el número de sesiones que han tenido en cualquiera de tus aplicaciones dentro de tu espacio de trabajo.
    tags:
      - Sesiones
  - name: Recuento de sesiones para aplicación
    description: Segmenta a tus usuarios por el número de sesiones que han tenido en una app concreta y determinada.
    tags:
      - Sesiones
  - name: X sesiones en los últimos Y días
    description: "Segmenta a tus usuarios por el número de sesiones (entre 0 y 50) que han tenido en tu app en el último número especificado de días naturales entre 1 y 30. <br> <a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a>"
    tags:
      - Sesiones
  - name: Primera aplicación usada
    description: "Segmenta a los usuarios en función de la primera vez que abrieron la aplicación. <em>Esto captura la primera sesión que tienen utilizando una versión de tu aplicación con la integración de SDK de Braze.</em> (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Sesiones
  - name: Primera aplicación concreta usada
    description: "Segmenta a tus usuarios según la hora más temprana registrada en la que abrieron cualquiera de tus aplicaciones dentro de tu espacio de trabajo. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Sesiones
  - name: Última aplicación usada
    description: "Segmenta a tus usuarios según la última vez que han abierto tu aplicación. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Sesiones
  - name: Última aplicación concreta usada
    description: "Segmenta a tus usuarios en función de la última vez que han abierto una aplicación determinada. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Sesiones
  - name: Duración promedio de la sesión
    description: Segmenta a tus usuarios según la duración media de sus sesiones en tu aplicación.
    tags:
      - Sesiones
  - name: Mensaje recibido de una campaña
    description: "Segmenta a tus usuarios en función de si han recibido o no una campaña concreta. Este filtro solo captura a los usuarios a los que se les envió explícitamente el mensaje, y no a otros usuarios con el mismo correo electrónico o número de teléfono que recibieron mensajes duplicados. Para capturar usuarios duplicados, utiliza <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Mensaje recibido de campaña o Canvas con etiqueta</a>.<br><br> En el caso de las tarjetas de contenido, los banners y los mensajes dentro de la aplicación, esto ocurre cuando el usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando el mensaje es enviado al usuario.<br><br> En el caso de WhatsApp, se trata del momento en que se envía la última solicitud de la API de mensajes a WhatsApp, no del momento en que se entrega el mensaje al dispositivo del usuario. <br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega).<br><br>En el caso de los SMS, es el momento en que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario."
    tags:
      - Reorientación
  - name: Variante de campaña recibida
    description: "Segmenta a tus usuarios según la variante de una campaña multivariante que han recibido. Este filtro solo captura a los usuarios a los que se les envió explícitamente el mensaje, y no a otros usuarios con el mismo correo electrónico o número de teléfono que recibieron mensajes duplicados. Para capturar usuarios duplicados, utiliza <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Mensaje recibido de campaña o Canvas con etiqueta</a>.<br><br> En el caso de las tarjetas de contenido, los banners y los mensajes dentro de la aplicación, esto ocurre cuando el usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando el mensaje es enviado al usuario.<br><br> En el caso de WhatsApp, se trata del momento en que se envía la última solicitud de la API de mensajes a WhatsApp, no del momento en que se entrega el mensaje al dispositivo del usuario. <br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega).<br><br>En el caso de los SMS, es el momento en que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario."
    tags:
      - Reorientación
  - name: Mensaje recibido de un paso en Canvas
    description: "Segmenta a sus usuarios en función de si han recibido o no un componente específico de Canvas. Este filtro solo captura a los usuarios a los que se les envió explícitamente el mensaje, y no a otros usuarios con el mismo correo electrónico o número de teléfono que recibieron mensajes duplicados. Para capturar usuarios duplicados, utiliza <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Mensaje recibido de campaña o Canvas con etiqueta</a>.<br><br> En el caso de las tarjetas de contenido y los mensajes dentro de la aplicación, esto ocurre cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando el mensaje es enviado al usuario.<br><br> En el caso de WhatsApp, se trata del momento en que se envía la última solicitud de la API de mensajes a WhatsApp, no del momento en que se entrega el mensaje al dispositivo del usuario. <br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega).<br><br>En el caso de los SMS, es el momento en que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario."
    tags:
      - Reorientación
  - name: Último mensaje recibido de un paso de Canvas concreto
    description: "Segmenta a sus usuarios según el momento en que recibieron un componente Canvas específico. Este filtro solo captura a los usuarios a los que se les envió explícitamente el mensaje, y no a otros usuarios con el mismo correo electrónico o número de teléfono que recibieron mensajes duplicados; para capturar usuarios duplicados, utiliza <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Mensaje recibido de campaña o Canvas con etiqueta</a>. Este filtro no tiene en cuenta si los usuarios han recibido otros componentes Canvas."
    tags:
      - Reorientación
  - name: Último mensaje recibido de una campaña concreta
    description: "Segmenta a tus usuarios en función de si han recibido o no una campaña concreta. Este filtro solo captura a los usuarios a los que se les envió explícitamente el mensaje, y no a otros usuarios con el mismo correo electrónico o número de teléfono que recibieron mensajes duplicados; para capturar usuarios duplicados, utiliza <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Mensaje recibido de campaña o Canvas con etiqueta</a>. Este filtro no tiene en cuenta si los usuarios han recibido otras campañas."
    tags:
      - Reorientación
  - name: Mensaje recibido de una campaña o Canvas con etiqueta
    description: "Segmenta a tus usuarios en función de si han recibido o no una determinada campaña o Canvas con una etiqueta específica. A diferencia de «Mensaje recibido de la campaña» y «Mensaje recibido del paso en Canvas», este filtro captura a todos los usuarios con el mismo correo electrónico o número de teléfono que recibieron mensajes duplicados.<br><br> En el caso de las tarjetas de contenido, los banners (solo campañas) y los mensajes dentro de la aplicación, esto ocurre cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando el mensaje es enviado al usuario.<br><br> En el caso de WhatsApp, se trata del momento en que se envía la última solicitud de la API de mensajes a WhatsApp, no del momento en que se entrega el mensaje al dispositivo del usuario. <br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega). Cuando varios usuarios comparten la misma dirección de correo electrónico:<br>- En el envío inicial, solo se actualiza el perfil del usuario objetivo específico. <br>- Cuando se entrega el correo electrónico, o si el usuario abre el correo electrónico o un enlace del correo electrónico, todos los usuarios que comparten esa dirección de correo electrónico parecen haber recibido el mensaje.<br><br>En el caso de los SMS, es el momento en que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario."
    tags:
      - Reorientación
  - name: Último mensaje recibido de una campaña o de Canvas con una etiqueta concreta
    description: Segmenta a tus usuarios en función de cuándo recibieron una campaña o un Canvas concreto con una etiqueta específica. Este filtro no tiene en cuenta si los usuarios han recibido otras campañas o Lienzos. (período de 24 horas)
    tags:
      - Reorientación
  - name: Jamás recibió un mensaje de campaña o de paso en Canvas
    description: Segmenta a tus usuarios en función de si han recibido o no algún componente de la campaña o del Canvas.
    tags:
      - Reorientación
  - name: Último correo electrónico recibido
    description: "Segmenta a tus usuarios según la última vez que han recibido uno de tus mensajes de correo electrónico. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Reorientación
  - name: Última notificación emergente recibida
    description: "Segmenta a tus usuarios según la última vez que recibieron una de tus notificaciones push. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Reorientación
  - name: Última impresión de un mensaje dentro de la aplicación
    description: Segmenta a tus usuarios según la última vez que vieron un mensaje in-app.
    tags:
      - Reorientación
  - name: Último SMS recibido
    description: "Segmenta a tus usuarios por la hora a la que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Reorientación
  - name: Último webhook recibido
    description: "Segmenta tus usuarios por la última vez que Braze envió un webhook para ese usuario. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Reorientación
  - name: Último WhatsApp recibido
    description: "Segmenta a tus usuarios según la última vez que recibieron un mensaje de WhatsApp. Es cuando se envía la última solicitud de la API de mensajes a WhatsApp, no cuando se entrega el mensaje al dispositivo del usuario. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Reorientación
  - name: Actividades en vivo Push to Start Registrado para la aplicación
    description: Segmenta a tus usuarios según si tienen registro para iniciar una actividad en vivo a través de notificaciones push de iOS para una aplicación específica.
    tags:
      - Dispositivos
  - name: Campaña que se abrió o a la que se hizo clic
    description: "Filtrar por interacción con una campaña específica. En el caso de la mensajería por correo electrónico, el evento de apertura incluye tanto las aperturas de máquinas como las no automáticas.<br><br> En el caso del correo electrónico, esto también incluye la opción de filtrar por «cualquier correo electrónico abierto (abierto por la máquina)» y «cualquier correo electrónico abierto (abierto por otros)». Los clics en los enlaces para cancelar la suscripción y en los centros de preferencias no cuentan para este filtro. Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando se abre el correo electrónico o se hace clic en él, también se actualizan los perfiles de todos los demás usuarios con esa misma dirección de correo electrónico. <br>- Si el usuario original cambia su dirección de correo electrónico después del envío del mensaje y antes de la apertura o el clic, la apertura o el clic se aplican a todos los usuarios restantes con esa dirección de correo electrónico en lugar de al usuario original.<br><br>Para los SMS, una interacción se define como:<br>- El último usuario que envió un SMS de respuesta que coincide con una categoría de palabras clave determinada. Se atribuye a la campaña más reciente recibida por todos los usuarios con este número de teléfono. La campaña debe haberse recibido en las últimas cuatro horas.<br>- El usuario seleccionó por última vez cualquier enlace acortado en un mensaje SMS que tenga activado el seguimiento de clics del usuario, de una campaña determinada."
    tags:
      - Reorientación
  - name: Campaña o Canvas que se abrió o en la que se hizo clic con etiqueta
    description: "Filtrar por interacción con una campaña específica que tiene una etiqueta específica. En el caso de la mensajería por correo electrónico, el evento de apertura incluye tanto las aperturas de máquinas como las no automáticas.<br><br> En el caso del correo electrónico, esto incluye la opción de filtrar por «cualquier correo electrónico abierto (abierto por la máquina)» y «cualquier correo electrónico abierto (abierto por otros)». Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando se abre el correo electrónico o se hace clic en él, también se actualizan los perfiles de todos los demás usuarios con esa misma dirección de correo electrónico. <br>- Si el usuario original cambia su dirección de correo electrónico después del envío del mensaje y antes de la apertura o el clic, la apertura o el clic se aplican a todos los usuarios restantes con esa dirección de correo electrónico en lugar de al usuario original.<br><br>Para los SMS, una interacción se define como:<br>- El último usuario que envió un SMS de respuesta que coincide con una categoría de palabras clave determinada. Se atribuye a la campaña más reciente recibida por todos los usuarios con este número de teléfono. La campaña debe haberse recibido en las últimas cuatro horas.<br>- Cuando el usuario seleccionó por última vez cualquier enlace acortado en un mensaje SMS que tenga activado el seguimiento de clics del usuario, desde una campaña o paso de Canvas con etiqueta determinada."
    tags:
      - Reorientación
  - name: Paso que se abrió o en el que se hizo clic
    description: "Filtrar por interacción con un componente Canvas específico. En el caso de la mensajería por correo electrónico, el evento de apertura incluye tanto las aperturas de máquinas como las no automáticas.<br><br>En el caso del correo electrónico, esto incluye la opción de filtrar por «cualquier correo electrónico abierto (abierto por la máquina)» y «cualquier correo electrónico abierto (abierto por otros)».<br><br>Para los SMS, una interacción se define como:<br>- El último usuario que envió un SMS de respuesta que coincide con una categoría de palabras clave determinada. Se atribuye a la campaña más reciente recibida por todos los usuarios con este número de teléfono. La campaña debe haberse recibido en las últimas cuatro horas. <br>- El usuario seleccionó por última vez cualquier enlace acortado en un mensaje SMS que tenga activado el seguimiento de clics del usuario, desde un determinado paso de Canvas."
    tags:
      - Reorientación
  - name: Alias al que se hizo clic en la campaña
    description: "Filtre a sus usuarios por si han hecho clic en un alias específico en una campaña concreta. Esto sólo se aplica a los mensajes de correo electrónico. <br><br> Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando se abre el correo electrónico o se hace clic en él, también se actualizan los perfiles de todos los demás usuarios con esa misma dirección de correo electrónico. <br>- Si el usuario original cambia su dirección de correo electrónico después del envío del mensaje y antes de la apertura o el clic, la apertura o el clic se aplican a todos los usuarios restantes con esa dirección de correo electrónico en lugar de al usuario original."
    tags:
      - Reorientación
  - name: Alias en que se hizo clic en paso en Canvas
    description: "Filtre a sus usuarios por si han hecho clic en un alias específico en un Canvas concreto. Esto sólo se aplica a los mensajes de correo electrónico. <br><br> Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando se abre el correo electrónico o se hace clic en él, también se actualizan los perfiles de todos los demás usuarios con esa misma dirección de correo electrónico. <br>- Si el usuario original cambia su dirección de correo electrónico después del envío del mensaje y antes de la apertura o el clic, la apertura o el clic se aplican a todos los usuarios restantes con esa dirección de correo electrónico en lugar de al usuario original."
    tags:
      - Reorientación
  - name: Alias con clic en cualquier paso de campaña o lienzo
    description: "Filtra a tus usuarios por si han hecho clic en un alias específico en cualquier campaña o Canvas. Esto sólo se aplica a los mensajes de correo electrónico. <br><br> Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando se abre el correo electrónico o se hace clic en él, también se actualizan los perfiles de todos los demás usuarios con esa misma dirección de correo electrónico. <br>- Si el usuario original cambia su dirección de correo electrónico después del envío del mensaje y antes de la apertura o el clic, la apertura o el clic se aplican a todos los usuarios restantes con esa dirección de correo electrónico en lugar de al usuario original."
    tags:
      - Reorientación
  - name: Rebote duro
    description: "Segmente a sus usuarios en función de si su dirección de correo electrónico ha rebotado o no (por ejemplo, si la dirección de correo electrónico no es válida)."
    tags:
      - Reorientación
  - name: Rebote blando
    description: "Segmenta a tus usuarios en función de si han rebotado blando X veces en Y días. Los filtros de segmento sólo pueden mirar 30 días atrás, pero puedes mirar más atrás con las extensiones de segmento.<br><br>Este filtro funciona de forma diferente a un evento de rebote blando en Currents. El filtro de segmento Rebote blando contabiliza un rebote blando si no hubo una entrega correcta durante el periodo de reintento de 72 horas. En Currents, cada reintento fallido se envía como un evento de rebote blando." 
    tags:
      - Reorientación
  - name: Te marcó como correo no deseado
    description: Segmenta a tus usuarios en función de si han marcado o no tus mensajes como spam.
    tags:
      - Reorientación
  - name: Número de teléfono no válido 
    description: Segmenta a tus usuarios según si su número de teléfono es inválido o no.
    tags:
      - Reorientación
  - name: Última categoría enviada de palabras clave entrantes de SMS específicas
    description: Segmenta a tus usuarios según la última vez que enviaron un SMS a un grupo de suscripción específico dentro de una categoría de palabras clave concreta. 
    tags:
      - Reorientación
  - name: Convertido desde campaña
    description: Segmenta a tus usuarios en función de si han convertido o no en una campaña concreta. Este filtro no incluye a los usuarios que están en el grupo de control.
    tags:
      - Reorientación
  - name: Convertido desde Canvas
    description: Segmenta a tus usuarios en función de si han convertido o no en un Canvas concreto. Este filtro no incluye a los usuarios que están en el grupo de control.
    tags:
      - Reorientación
  - name: Grupo de control en campaña
    description: Segmenta a sus usuarios en función de si estaban o no en el grupo de control de una campaña multivariante específica.
    tags:
      - Reorientación
  - name: Grupo de control en Canvas
    description: "Segmenta a tus usuarios en función de si estaban o no en el grupo de control de un Canvas concreto. Este filtro solo filtra a los usuarios que han entrado en Canvas, por lo que los usuarios que nunca han entrado quedan totalmente excluidos de los resultados.<br><br>Por ejemplo, si filtras los usuarios que no están en el grupo de control de un Canvas, solo obtendrás los usuarios que entraron en el Canvas y fueron asignados a una variante que no es de control; los usuarios que nunca entraron en el Canvas no se incluyen. Para incluir a todos los usuarios independientemente de su entrada en Canvas, utiliza el <code>Entered Canvas Variation</code> filtrar en su lugar."
    tags:
      - Reorientación
  - name: Últimos inscritos en cualquier grupo de control
    description: "Segmenta a tus usuarios por la última vez que cayeron en el grupo de control en una campaña. <br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Reorientación
  - name: Variación de Canvas ingresada
    description: "Segmenta a tus usuarios en función de si han entrado o no en una ruta de variación de un Canvas específico. Este filtro evalúa a todos los usuarios.<br><br>Por ejemplo, si filtras por usuarios que no han ingresado a un grupo de control de variación de Canvas, recibirás todos los usuarios que no están en el grupo de control, independientemente de si ingresaron a Canvas."
    tags:
      - Reorientación
  - name: Último mensaje recibido
    description: "Segmenta a tus usuarios determinando el último mensaje recibido. (período de 24 horas)<br><br> En el caso de las tarjetas de contenido, los banners y los mensajes dentro de la aplicación, se trata de la última vez que el usuario registró una impresión, no de la última vez que se envió la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando cualquier mensaje fue enviado al usuario.<br><br> En el caso de WhatsApp, se trata de cuándo se envió la última solicitud de la API de mensajes a WhatsApp, no cuándo se entregó el mensaje al dispositivo del usuario. <br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega). Cuando varios usuarios comparten la misma dirección de correo electrónico:<br>- En el envío inicial, solo se actualiza el perfil del usuario objetivo específico. <br>- Cuando se entrega el correo electrónico, o si el usuario abre el correo electrónico o un enlace del correo electrónico, todos los usuarios que comparten esa dirección de correo electrónico parecen haber recibido el mensaje.<br><br>En el caso de los SMS, es el momento en que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario.<br><br>Ejemplo:<br>Último mensaje recibido hace menos de 1 día = hace menos de 24 horas<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Reorientación
  - name: Última interacción con un mensaje
    description: "Segmenta a tus usuarios según la última vez que han hecho clic o abierto uno de tus canales de mensajería (banners, tarjetas de contenido, correo electrónico, dentro de la aplicación, SMS, push, WhatsApp). En el caso de la mensajería por correo electrónico, el evento de apertura incluye tanto las aperturas de máquinas como las no automáticas. (período de 24 horas)<br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega). Esto también incluye la opción de filtrar por «cualquier correo electrónico abierto (abierto por la máquina)» y «cualquier correo electrónico abierto (otros abiertos)». Cuando varios usuarios comparten la misma dirección de correo electrónico:<br>- En el envío inicial, solo se actualiza el perfil del usuario objetivo específico. <br>- Cuando se entrega el correo electrónico, o si el usuario abre el correo electrónico o un enlace del correo electrónico, todos los usuarios que comparten esa dirección de correo electrónico parecen haber recibido el mensaje.<br><br>En el caso de los SMS, se trata del momento en que el usuario seleccionó por última vez cualquier enlace acortado en un mensaje que tenga activado el seguimiento de clics del usuario.<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Reorientación
  - name: Tarjeta clicada 
    description: "Segmenta a sus usuarios en función de si han hecho clic o no en una tarjeta de contenido específica. Este filtro está disponible como subfiltro de \"Campaña clicada/abierta\", \"Campaña clicada/abierta o Canvas con etiqueta\" y \"Paso clicado/abierto\"."
    tags:
      - Reorientación
  - name: Conmutador de características
    description: "Segmento de usuarios que tienen activada una determinada <a href=\"/docs/developer_guide/feature_flags/\">función</a>."
    tags:
      - Reorientación
  - name: Grupo de suscripción
    description: "Segmenta a tus usuarios por su grupo de suscripción para correo electrónico, SMS/MMS o WhatsApp. Los grupos archivados no aparecen y no se pueden utilizar."
    tags:
      - Comportamiento de suscripción al canal
  - name: Correo electrónico disponible
    description: "Segmenta a tus usuarios según si tienen una dirección de correo electrónico válida y si son suscriptores o han realizado la adhesión voluntaria a recibir correos electrónicos. Este filtro comprueba tres criterios: si el usuario ha cancelado la suscripción a los correos electrónicos, si Braze ha recibido un rebote duro y si el correo electrónico se ha marcado como correo no deseado. Si se cumple alguno de estos criterios, o si no existe un correo electrónico para un usuario, este no se incluye.<br><br>Usuarios cuyo correo electrónico está disponible es <code>false</code> quedan excluidos de la audiencia de la campaña y no reciben el correo electrónico, incluso si la configuración de envío está configurada para enviar a todos los usuarios (incluidos los usuarios que han cancelado la suscripción).<br><br>Para los correos electrónicos en los que es importante el estado de adhesión voluntaria, utiliza «Correo electrónico disponible» en lugar de <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">«Dirección de correo electrónico</a>». Los criterios adicionales te ayudan a dirigirte a los usuarios elegibles para recibir correos electrónicos."
    tags:
      - Comportamiento de suscripción al canal
  - name: Fecha de adhesión voluntaria por correo electrónico
    description: Segmenta a tus usuarios por la fecha en la que optaron por el correo electrónico.
    tags:
      - Comportamiento de suscripción al canal
  - name: Estado de la suscripción del correo electrónico
    description: Segmenta a tus usuarios según su estado de suscripción al correo electrónico.
    tags:
      - Comportamiento de suscripción al canal
  - name: Fecha de cancelación de suscripción del correo electrónico 
    description: Segmenta a tus usuarios por la fecha en la que se dieron de baja de futuros correos electrónicos.
    tags:
      - Comportamiento de suscripción al canal
  - name: Notificaciones push en primer plano habilitadas
    description: "Segmenta a los usuarios que tienen autorización push provisional o están habilitados para push en primer plano. En concreto, este recuento incluye:<br>1. Usuarios de iOS autorizados provisionalmente para push. <br>2. Usuarios que tienen habilitada la función push en primer plano y cuyo estado de suscripción push no está cancelado, para cualquiera de tus aplicaciones. Para estos usuarios, este recuento incluye sólo las pulsaciones en primer plano.<br><br>La función «Push en primer plano habilitado» no incluye a los usuarios que han cancelado la suscripción. <br><br>Después de segmentar con este filtro, puedes ver un desglose de quiénes están en ese segmento para Android, iOS y Web en el panel inferior, llamado <em>Usuarios accesibles</em>."
    tags:
      - Comportamiento de suscripción al canal
  - name: Push en primer plano habilitado para la aplicación
    description: Segmenta según si los usuarios tienen activada la función push para tu aplicación en su dispositivo. Usuarios que tienen habilitada la función de push en primer plano para una aplicación. Esto no tiene en cuenta el estado de la suscripción push. Este recuento incluye a los usuarios que han autorizado provisionalmente tokens push en primer y segundo plano.
    tags:
      - Comportamiento de suscripción al canal
  - name: Push en segundo o primer plano habilitado
    description: Segmenta según si los usuarios tienen un token de notificaciones push y no han cancelado la suscripción. Usuarios que tienen habilitada la función push en segundo plano o en primer plano para cualquiera de tus aplicaciones.
    tags:
      - Comportamiento de suscripción al canal
  - name: Fecha de adhesión voluntaria a notificaciones push
    description: Segmenta a tus usuarios por la fecha en la que optaron por push.
    tags:
      - Comportamiento de suscripción al canal
  - name: Estado de la suscripción a notificaciones push
    description: "Segmenta a tus usuarios por su <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">estado de suscripción</a> para push."
    tags:
      - Comportamiento de suscripción al canal
  - name: Fecha de cancelación de suscripción a notificaciones push
    description: Segmenta a tus usuarios por la fecha en la que se dieron de baja de futuras notificaciones push.
    tags:
      - Comportamiento de suscripción al canal
  - name: Producto comprado
    description: Segmenta a tus usuarios por productos comprados en tu app.
    tags:
      - Comportamiento de compra
  - name: Cantidad total de compras
    description: Segmenta a tus usuarios según el número de compras que han realizado en tu aplicación.
    tags:
      - Comportamiento de compra
  - name: X producto comprado en Y días
    description: Filtre a los usuarios por las veces que se compró un producto específico.
    tags:
      - Comportamiento de compra
  - name: X compras en los últimos Y días
    description: "Segmenta a tus usuarios por el número de veces (entre 0 y 50) que han realizado una compra en el último número especificado de días naturales entre 1 y 30. <br> <a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a>"
    tags:
      - Comportamiento de compra
  - name: Propiedad de compra X en Y días
    description: "Segmenta a sus usuarios por el número de veces que se ha realizado una compra en relación con una determinada propiedad de compra en el último número especificado de días naturales entre 1 y 30. <br> <a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a>"
    tags:
      - Comportamiento de compra
  - name: Primera compra hecha
    description: Segmenta a tus usuarios según la primera vez que un usuario realizó una compra en tu aplicación.
    tags:
      - Comportamiento de compra
  - name: Primera compra de la aplicación
    description: Segmenta a tus usuarios según la primera vez que un usuario realizó una compra en tu aplicación.
    tags:
      - Comportamiento de compra
  - name: Última compra hecha
    description: Filtre a los usuarios por la última vez que realizaron una compra.
    tags: 
      - Comportamiento de compra
  - name: Último producto comprado
    description: Filtre a los usuarios por la última vez que compraron un producto específico.
    tags:
      - Comportamiento de compra
  - name: Dinero gastado
    description: Segmenta a tus usuarios por la cantidad de dinero que han gastado en tu aplicación.
    tags:
      - Comportamiento de compra
  - name: X dinero gastado en Y días
    description: "Segmenta a tus usuarios por la cantidad de dinero que han gastado en tu aplicación en el último número especificado de días naturales entre 1 y 30. Esta cantidad incluye solo la suma de las últimas 50 compras. <br> <a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a>"
    tags:
      - Comportamiento de compra
  - name: Último pedido realizado (últimos 730 días)
    description: "Segmenta a tus usuarios según la fecha de su último pedido, basándose en el <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado por el comercio electrónico</a> para los pedidos realizados (los espacios de trabajo que no realizan un seguimiento de los eventos de comercio electrónico no disponen de datos para este filtro). Los usuarios son evaluados para este filtro una vez al día, y el período máximo de revisión es de los últimos dos años.<br><br>Este filtro está en fase beta. Si estás interesado en utilizar este filtro, ponte en contacto con tu director de cuentas de Braze."
    tags:
      - Comercio electrónico
  - name: Recuento total de pedidos (últimos 730 días)
    description: "Segmenta a tus usuarios según el recuento total de pedidos realizados por cada usuario en los últimos dos años, basándose en el <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado por el comercio electrónico</a> para los pedidos realizados (los espacios de trabajo que no realizan un seguimiento de los eventos de comercio electrónico no disponen de datos para este filtro). Este recuento excluye los pedidos cancelados, que deben realizarse mediante el seguimiento del <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado por el comercio electrónico</a> para pedidos cancelados. Los usuarios son evaluados para este filtro una vez al día.<br><br>Este filtro está en fase beta. Si estás interesado en utilizar este filtro, ponte en contacto con tu director de cuentas de Braze."
    tags:
      - Comercio electrónico
  - name: Recuento total de pedidos
    description: "Segmenta a tus usuarios según el recuento total de pedidos realizados por un usuario a lo largo de su vida útil, basándose en el <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado por el comercio electrónico</a> para los pedidos realizados (los espacios de trabajo que no realizan un seguimiento de los eventos de comercio electrónico no disponen de datos para este filtro). Este recuento excluye los pedidos cancelados, que deben realizarse mediante el seguimiento del <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado por el comercio electrónico</a> para pedidos cancelados. Los usuarios son evaluados para este filtro en tiempo real.<br><br>Este filtro está en fase beta. Si estás interesado en utilizar este filtro, ponte en contacto con tu director de cuentas de Braze."
    tags:
      - Comercio electrónico
  - name: Recuento total de pedidos cancelados (últimos 730 días)
    description: "Segmenta a tus usuarios según el recuento total de pedidos que un usuario ha cancelado en los últimos dos años, basándose en el <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado por el comercio electrónico</a> para los pedidos realizados (los espacios de trabajo que no realizan un seguimiento de los eventos de comercio electrónico no disponen de datos para este filtro). Los usuarios son evaluados para este filtro una vez al día.<br><br>Este filtro está en fase beta. Si estás interesado en utilizar este filtro, ponte en contacto con tu director de cuentas de Braze."
    tags:
      - Comercio electrónico
  - name: Valor de duración del ciclo de vida del cliente (últimos 730 días)
    description: "Segmenta a tus usuarios según los ingresos totales que se espera que generen a lo largo de su historial de compras con tu marca. El cálculo tiene en cuenta los últimos 730 días y toma el valor medio de los pedidos (AOV), lo multiplica por el número total de pedidos realizados y, a continuación, tiene en cuenta la duración activa de las compras del usuario (el intervalo de tiempo entre tu primer pedido y el más reciente). Este filtro utiliza datos rastreados en <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento</a>s <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">recomendados de comercio electrónico</a> (los espacios de trabajo que no realizan el seguimiento de eventos de comercio electrónico no tienen datos para este filtro). Los usuarios son evaluados para este filtro una vez al día.<br><br>Este filtro está en fase beta. Si estás interesado en utilizar este filtro, ponte en contacto con tu director de cuentas de Braze."
    tags:
      - Comercio electrónico
  - name: Valor total de la devolución (últimos 730 días)
    description: "Segmenta a tus usuarios según el valor de los reembolsos concedidos a un usuario en los últimos dos años, basándose en el <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado por el comercio electrónico</a> para los pedidos reembolsados (los espacios de trabajo que no realizan el seguimiento de los eventos de comercio electrónico no disponen de datos para este filtro). Los usuarios son evaluados para este filtro una vez al día.<br><br>Este filtro está en fase beta. Si estás interesado en utilizar este filtro, ponte en contacto con tu director de cuentas de Braze."
    tags:
      - Comercio electrónico
  - name: Valor total del reembolso
    description: "Segmenta a tus usuarios según el valor total de los reembolsos concedidos a un usuario a lo largo de su vida útil, basándose en el <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado por el comercio electrónico</a> para los pedidos reembolsados (los espacios de trabajo que no realizan el seguimiento de los eventos de comercio electrónico no disponen de datos para este filtro). Los usuarios son evaluados para este filtro en tiempo real.<br><br>Este filtro está en fase beta. Si estás interesado en utilizar este filtro, ponte en contacto con tu director de cuentas de Braze."
    tags:
      - Comercio electrónico
  - name: Ingresos totales (últimos 730 días)
    description: "Segmenta a tus usuarios según los ingresos totales generados por los pedidos de un usuario en los últimos dos años, calculados restando los ingresos asociados al <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de</a> <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comercio electrónico</a> para pedidos reembolsados de los ingresos asociados al evento de comercio electrónico para pedidos realizados (los espacios de trabajo que no realizan el seguimiento de los eventos de comercio electrónico no disponen de datos para este filtro). Los usuarios son evaluados para este filtro una vez al día.<br><br>Este filtro está en fase beta. Si estás interesado en utilizar este filtro, ponte en contacto con tu director de cuentas de Braze."
    tags:
      - Comercio electrónico
  - name: Ingresos totales
    description: "Segmenta a tus usuarios según los ingresos totales generados por los pedidos de un usuario a lo largo de su vida útil, calculados restando los ingresos asociados al <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado de</a> <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">comercio electrónico</a> para pedidos reembolsados de los ingresos asociados al evento de comercio electrónico para pedidos realizados (los espacios de trabajo que no realizan el seguimiento de los eventos de comercio electrónico no disponen de datos para este filtro). Los usuarios son evaluados para este filtro en tiempo real.<br><br>Este filtro está en fase beta. Si estás interesado en utilizar este filtro, ponte en contacto con tu director de cuentas de Braze."
    tags:
      - Comercio electrónico
  - name: Valor medio de los pedidos (últimos 730 días)
    description: "Segmenta a tus usuarios según el valor medio (media) de los pedidos de un usuario en los últimos dos años, basándose en el <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">evento recomendado por el comercio electrónico</a> para los pedidos realizados (los espacios de trabajo que no realizan un seguimiento de los eventos de comercio electrónico no disponen de datos para este filtro). Los usuarios son evaluados para este filtro una vez al día.<br><br>Este filtro está en fase beta. Si estás interesado en utilizar este filtro, ponte en contacto con tu director de cuentas de Braze."
    tags:
      - Comercio electrónico
  - name: País
    description: Segmenta a tus usuarios por la ubicación del último país indicado.
    tags:
      - Atributos demográficos
  - name: Localidad
    description: Segmenta a tus usuarios por la ubicación de su última ciudad indicada.
    tags:
      - Atributos demográficos
  - name: Idioma
    description: Segmenta a tus usuarios por su idioma preferido.
    tags:
      - Atributos demográficos
  - name: Edad
    description: "Segmenta a tus usuarios por su edad, tal y como indican desde tu aplicación."
    tags:
      - Atributos demográficos
  - name: Cumpleaños
    description: "Segmenta a tus usuarios por su fecha de cumpleaños, tal y como indicaron desde tu aplicación. <br> Los usuarios cuyo cumpleaños sea el 29 de febrero se incluyen en segmentos que incluyen el 1 de marzo.<br><br>Para apuntar a los cumpleaños de diciembre o enero, inserte la lógica de filtro sólo dentro del intervalo de 12 meses del año al que apunta. En otras palabras, no introduzca lógica que se remonte al mes de diciembre del año anterior o al mes de enero del año siguiente. Por ejemplo, para los cumpleaños de diciembre, puede filtrar por \"el 31 de diciembre\", \"antes del 31 de diciembre\" o \"después del 30 de noviembre\"."
    tags:
      - Atributos demográficos
  - name: Género
    description: "Segmenta a tus usuarios por género, tal y como indicaron desde tu aplicación."
    tags:
      - Atributos demográficos
  - name: Número de teléfono sin formato
    description: "Segmenta a tus usuarios por su número de teléfono sin formato. No incluye paréntesis, guiones ni otros símbolos."
    tags:
      - Atributos demográficos
  - name: Nombre
    description: "Segmenta a tus usuarios por su nombre de pila, tal y como lo indicaron desde tu aplicación."
    tags:
      - Atributos demográficos
  - name: Apellido
    description: "Segmenta a tus usuarios por su apellido, tal y como lo indicaron desde tu aplicación."
    tags:
      - Atributos demográficos
  - name: Tiene la aplicación
    description: "Segmenta en función de si el usuario ha instalado alguna vez su aplicación o no. Esto incluye a los usuarios que actualmente tienen tu aplicación instalada y a los que la han desinstalado en el pasado. Esto requiere generalmente que los usuarios abran la aplicación (inicien una sesión) para ser incluidos en este filtro. Sin embargo, hay algunas excepciones, como si un usuario se importó a Braze y se asoció manualmente a su aplicación."
    tags:
      - Aplicación
  - name: Nombre de la versión más reciente de la aplicación
    description: "Segmenta por el nombre reciente de la aplicación del usuario.<br><br>Cuando se utiliza «menor que» o «menor o igual que», si la versión principal de la aplicación no existe, este filtro devuelve «true» porque el usuario es más antiguo que la versión de la aplicación. Esto significa que si la última versión principal de la aplicación del usuario no existe, automáticamente coinciden con el filtro."
    tags:
      - Aplicación
  - name: Número de la versión más reciente de la aplicación
    description: "Segmenta por el número de versión reciente de la aplicación del usuario.<br><br>Cuando se utiliza «menor que» o «menor o igual que», si la versión principal de la aplicación no existe, este filtro filtra y devuelve «true» porque el usuario es más antiguo que la versión de la aplicación. Esto significa que si la última versión principal de la aplicación del usuario no existe, automáticamente coinciden con el filtro.<br><br>Es posible que las versiones actuales de la aplicación tarden un poco en aparecer. La versión de la aplicación en el perfil de usuario se actualiza cuando el SDK captura la información, lo que depende del momento en que los usuarios abran sus aplicaciones. Si el usuario no abre la aplicación, la versión actual no se actualizará. Estos filtros tampoco se aplicarán de forma retroactiva. Es recomendable utilizar «mayor que» o «igual a» para las versiones actuales y futuras, pero filtrar versiones anteriores puede provocar comportamientos inesperados."
    tags:
      - Aplicación
  - name: Desinstalada
    description: Segmenta a tus usuarios en función de si han desinstalado tu aplicación y no la han vuelto a instalar.
    tags:
      - Desinstalar
  - name: Operador del dispositivo
    description: Segmenta a tus usuarios según el operador de su dispositivo.
    tags:
      - Dispositivos
  - name: Recuento de dispositivos
    description: Segmenta a tus usuarios según el número de dispositivos en los que han utilizado tu aplicación.
    tags:
      - Dispositivos
  - name: Modelo del dispositivo
    description: Segmenta a tus usuarios por la versión del modelo de su teléfono móvil.
    tags:
      - Dispositivos
  - name: Sistema operativo del dispositivo
    description: "Segmenta a los usuarios que tienen uno o más dispositivos con el sistema operativo especificado. Para realizar la segmentación de los usuarios por un rango de sistemas operativos, utiliza el filtro <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#device-os-version-number\">Número de versión del sistema operativo del dispositivo</a>."
    tags:
      - Dispositivos
  - name: Número de versión del SO del dispositivo
    description: "Segmenta a los usuarios que tienen uno o más dispositivos con una versión del sistema operativo que se encuentra dentro de un rango específico. Por ejemplo, puedes dirigirte a usuarios que tengan una versión del sistema operativo iOS superior o igual a 26.0."
    tags:
      - Dispositivos
  - name: Configuración regional del dispositivo más reciente
    description: "Segmenta a sus usuarios según la <a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">información de localización</a> del dispositivo utilizado más recientemente."
    tags:
      - Dispositivos
  - name: Modelo de reloj más reciente
    description: Segmenta a tus usuarios según su modelo de smartwatch más reciente.
    tags:
      - Dispositivos
  - name: Autorizados provisionalmente en iOS
    description: Permite encontrar usuarios autorizados provisionalmente en iOS 12 para una app determinada.
    tags:
      - Dispositivos
  - name: Navegador web
    description: Segmenta a tus usuarios según el navegador que utilizan para acceder a tu web.
    tags:
      - Dispositivos
  - name: Identificador para anunciantes (IDFA) del dispositivo
    description: Te permite designar los destinatarios de tu campaña por IDFA para realizar pruebas.
    tags:
      - Casos de uso de publicidad
  - name: IDFV del dispositivo
    description: Le permite designar los destinatarios de su campaña por IDFV para realizar pruebas.
    tags:
      - Casos de uso de publicidad
  - name: ID de anuncios de Google del dispositivo
    description: Segmenta a tus usuarios por el ID del anuncio de Google.
    tags:
      - Casos de uso de publicidad
  - name: ID de anuncios de Roku del dispositivo
    description: Segmenta a tus usuarios por el ID del anuncio de Roku.
    tags:
      - Casos de uso de publicidad
  - name: ID de anuncios de Windows del dispositivo
    description: Segmenta a sus usuarios por el ID de anuncio de Windows.
    tags:
      - Casos de uso de publicidad
  - name: Seguimiento de anuncios habilitado
    description: "Le permite filtrar en función de si sus usuarios han optado por el seguimiento de anuncios. El seguimiento de anuncios está relacionado con el IDFA o \"identificador para anunciantes\" asignado a todos los dispositivos iOS por Apple, que puede configurarse mediante SDK. Este identificador permite a los anunciantes rastrear a los usuarios y ofrecerles anuncios específicos."
    tags:
      - Casos de uso de publicidad
  - name: Ubicación más reciente
    description: Segmenta a tus usuarios según la última ubicación registrada en la que han utilizado tu aplicación.
    tags:
      - Ubicación
  - name: Ubicación disponible
    description: "Segmenta a tus usuarios en función de si han comunicado o no su ubicación. Para utilizar este filtro, tu aplicación debe tener <a href=\"/docs/search/?query=location%20tracking\">integrado el seguimiento de la ubicación.</a>"
    tags:
      - Ubicación
  - name: Cohortes de amplitud
    description: Los clientes que utilizan Amplitude pueden completar sus segmentos eligiendo e importando sus cohortes en Amplitude.
    tags:
      - Membresía de cohorte
  - name: Cohortes de Census
    description: Los clientes que utilizan Census pueden complementar sus segmentos eligiendo e importando sus cohortes en Census.
    tags:
      - Membresía de cohorte
  - name: Cohortes de Heap
    description: Los clientes que utilizan Heap pueden completar sus segmentos eligiendo e importando sus cohortes en Heap.
    tags:
      - Membresía de cohorte
  - name: Cohortes de Hightouch
    description: Los clientes que utilizan Hightouch pueden completar sus segmentos eligiendo e importando sus cohortes en Hightouch.
    tags:
      - Membresía de cohorte
  - name: Cohortes de Kubit
    description: Los clientes que utilizan Kubit pueden completar sus segmentos eligiendo e importando sus cohortes en Kubit.
    tags:
      - Membresía de cohorte
  - name: Cohortes de Mixpanel
    description: Los clientes que utilizan Mixpanel pueden complementar sus segmentos eligiendo e importando sus cohortes en Mixpanel.
    tags:
      - Membresía de cohorte
  - name: Cohortes de Segment
    description: Los clientes que utilizan Segment pueden complementar sus segmentos eligiendo e importando sus cohortes en Segment.
    tags:
      - Membresía de cohorte
  - name: Cohortes de Tinyclues
    description: Los clientes que utilizan Tinyclues pueden completar sus segmentos eligiendo e importando sus cohortes en Tinyclues.
    tags:
      - Membresía de cohorte
  - name: Anuncio de atribución de instalación
    description: Segmenta a sus usuarios por el anuncio al que se atribuyó su instalación.
    tags:
      - Atributos de usuario
  - name: Grupo de anuncios de atribución de instalación
    description: Segmenta a sus usuarios por el grupo de anuncios al que se atribuyó su instalación.
    tags:
      - Atribución de instalación
  - name: Campaña de atribución de instalación
    description: Segmenta a sus usuarios según la campaña publicitaria a la que se atribuyó su instalación.
    tags:
      - Atribución de instalación
  - name: Origen de atribución de instalación
    description: Segmenta a sus usuarios según la fuente a la que se atribuyó su instalación.
    tags:
      - Atribución de instalación
  - name: Categoría de riesgo de pérdida
    description:  Segmenta a sus usuarios por categoría de riesgo de pérdida de clientes según una predicción específica.
    tags:
      - Inteligencia y predicción
  - name: Puntuación de riesgo de pérdida
    description: Segmenta a sus usuarios por puntuación de riesgo de abandono de acuerdo con una predicción específica.
    tags:
      - Inteligencia y predicción
  - name: Categoría de probabilidad del evento
    description: Segmenta a sus usuarios por probabilidad de realizar un evento según una predicción específica.
    tags:
      - Inteligencia y predicción
  - name: Puntuación de probabilidad del evento
    description: Segmenta a sus usuarios por probabilidad de realizar un evento según una predicción específica.
    tags:
      - Inteligencia y predicción
  - name: Canal inteligente
    description: Segmente a sus usuarios por su canal más activo en los últimos tres meses.
    tags:
      - Inteligencia y predicción
  - name: Probabilidad de mensaje abierto
    description: "Filtra a tus usuarios en función de la <a href=\"/docs/user_guide/brazeai/intelligence/intelligent_channel/#individual-channels\">probabilidad de que abran un mensaje en un canal específico,</a> en una escala del 0 al 100 %. Los usuarios sin datos suficientes para medir la probabilidad de un canal pueden seleccionarse mediante \"está en blanco\".<br><br>En el caso del correo electrónico, las aperturas de máquinas se excluyen del cálculo de probabilidad."
    tags:
      - Inteligencia y predicción
  - name: Cantidad de amigos de Facebook que usan la aplicación
    description: Segmenta a tus usuarios en función de cuántos amigos de Facebook tienen que utilizan la misma aplicación.
    tags:
      - Actividad social
  - name: Facebook conectado
    description: Segmenta a tus usuarios en función de si han conectado tu aplicación a Facebook.
    tags:
      - Actividad social
  - name: Twitter conectado
    description: Segmenta a tus usuarios en función de si han conectado tu aplicación a X (antes Twitter).
    tags:
      - Actividad social
  - name: Cantidad de seguidores en Twitter
    description: Segmenta a tus usuarios según el número de seguidores X (antes Twitter) que tengan.
    tags:
      - Actividad social
  - name: Número de teléfono
    description: "Segmenta a tus usuarios por el campo del número de teléfono con formato E.164.<br><br> Cuando se envía un número de teléfono a Braze, éste intenta coaccionarlo para que adopte el <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">formato e.164</a> que se utiliza para enviar a través de los canales SMS y WhatsApp. El proceso de coacción puede fallar si el número no está formateado correctamente, lo que da como resultado que el perfil de usuario tenga un número de teléfono sin formatear, pero no un número de teléfono de envío. Este filtro de segmento devuelve usuarios por su número de teléfono con formato e.164 (cuando está disponible).<br><br>Casos de uso:<br> - Utiliza este filtro para conocer el tamaño más preciso de tu audiencia objetivo al enviar mensajes SMS o WhatsApp.  <br>- Utiliza expresiones regulares (regex) con este filtro para segmentar por números de teléfono con un código de país concreto. <br>- Utiliza este filtro para segmentar a los usuarios por números de teléfono que no hayan superado el proceso de coerción e.164."
    tags:
      - Otros filtros
---
