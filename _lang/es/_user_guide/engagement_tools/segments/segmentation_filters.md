---
page_order: 2
nav_title: Filtros de segmentación
article_title: Filtros de segmentación
layout: glossary_page
glossary_top_header: "Segmentation Filters"
glossary_top_text: The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. You can search or narrow these filters by filter category.<br><br>To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.

page_type: glossary
tool: Segments
description: "Este glosario enumera los filtros disponibles para segmentar y orientar a sus usuarios."
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Membresía de segmento o de CSV
  - name: Atributos personalizados
  - name: Eventos personalizados
  - name: Sesiones
  - name: Reorientación
  - name: Comportamiento de suscripción al canal
  - name: Comportamiento de compra
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

glossaries:
  - name: Membresía de Segment
    description: "Le permite filtrar en función de la pertenencia a un segmento en cualquier lugar en el que se utilicen filtros (como segmentos, campañas y otros) y dirigirse a varios segmentos diferentes dentro de una misma campaña. <br><br>Ten en cuenta que los segmentos que ya utilizan este filtro no pueden incluirse más ni anidarse en otros segmentos, porque esto puede crear un ciclo en el que el segmento A incluya al segmento B, que a su vez intentará incluir de nuevo al segmento A. Si eso ocurriera, el segmento seguiría haciendo referencia a sí mismo, haciendo imposible calcular quién pertenece realmente a él. Además, anidar segmentos de este modo añade complejidad y puede ralentizar las cosas. En su lugar, recrea el segmento que intentas incluir utilizando los mismos filtros."
    tags:
      - Segment or CSV membership
  - name: Extensiones de segmento de Braze
    description: "Después de crear una extensión de segmento en el panel de control de Braze, puede elegir incluir/excluir esas extensiones en su segmento."
    tags:
      - Segment or CSV membership
  - name: Actualizado/Importado desde un CSV
    description: Segmenta a sus usuarios en función de si formaron parte o no de una carga CSV.
    tags:
      - Segment or CSV membership
  - name: Atributos personalizados
    description: "Determina si un usuario coincide o no con un valor de atributo registrado personalizado. (período de 24 horas) <br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Custom attributes
  - name: Creado el
    description: "Segmenta a los usuarios en función de cuándo se creó su perfil de usuario. Si un usuario se añadió por CSV o API, este filtro refleja la fecha en que se añadió. Si el usuario no está añadido por CSV o API y tiene su primera sesión seguida por el SDK, entonces este filtro refleja la fecha de esa primera sesión."
    tags:
      - Other Filters
  - name: Atributos personalizados anidados
    description: "Atributos que son las propiedades de los atributos personalizados.<br><br>Al filtrar un atributo personalizado de hora anidado, puede elegir filtrar en función del \"Día del año\" o de la \"Hora\". \"Día del año\" comprobará sólo el mes y el día para la comparación. \"Hora\" comparará la marca de tiempo completa, incluido el año."
    tags:
      - Custom attributes
  - name: Día del evento recurrente
    description: "Este filtro mira el mes y el día del atributo personalizado con el tipo de dato \"fecha\", pero no mira el año. Este filtro es útil para eventos anuales.<br><br>Zona horaria:<br>Este filtro se ajusta a las zonas horarias en las que se encuentre el usuario."
    tags:
      - Custom attributes
  - name: Evento personalizado
    description: "Determina si un usuario ha realizado o no un evento especialmente registrado.<br><br> Ejemplo:<br>Actividad completada con la propiedad nombre_actividad.<br><br>Zona horaria:<br>UTC - Día natural = 1 día natural considerará 24-48 horas del historial del usuario"
    tags:
      - Custom events
  - name: Primer evento personalizado hecho
    description: "Determina la hora más temprana a la que un usuario ha realizado un evento especialmente registrado. (período de 24 horas) <br><br>Ejemplo:<br> Primer carro abandonado Hace menos de 1 día<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Custom events
  - name: Último evento personalizado hecho 
    description: "Determina la última vez que un usuario ha realizado un evento especialmente registrado. Este filtro admite decimales, como 0,25 horas. (período de 24 horas) <br><br>Ejemplo:<br> Último carro abandonado Hace menos de 1 día<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Custom events
  - name: Evento personalizado X en Y días
    description: "Determina si un usuario ha realizado o no un evento especialmente registrado entre 0 y 50 veces en el último número especificado de días naturales entre 1 y 30. (Día natural = 1 día natural se examinarán entre 24 y 48 horas del historial del usuario)<br> <a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a> <br><br>Ejemplo:<br>Carrito abandonado exactamente 0 veces en el último 1 día calendario<br><br>Zona horaria:<br>UTC - Para tener en cuenta todas las zonas horarias, 1 día natural considerará de 24 a 48 horas de historial de usuario, dependiendo de la hora a la que se evalúe el segmento; para 2 días naturales, considerará de 48 a 72 horas de historial de usuario, y así sucesivamente."
    tags:
      - Custom events
  - name: Propiedad de evento personalizado X en Y días
    description: "Determina si un usuario ha realizado o no un evento especialmente registrado en relación con una propiedad específica entre 0 y 50 veces en el último número especificado de días naturales entre 1 y 30. (Día natural = 1 día natural se examinarán entre 24 y 48 horas del historial del usuario)<br><a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a> <br><br>Ejemplo:<br> Añadido a Favoritos con la propiedad \"nombre_evento\" exactamente 0 veces en el último 1 día natural<br><br>Zona horaria:<br>UTC - Para tener en cuenta todas las zonas horarias, 1 día natural considerará de 24 a 48 horas de historial de usuario, dependiendo de la hora a la que se evalúe el segmento; para 2 días naturales, considerará de 48 a 72 horas de historial de usuario, y así sucesivamente."
    tags:
      - Custom events
  - name: Dirección de correo electrónico 
    description: "Le permite designar los destinatarios de su campaña por direcciones de correo electrónico individuales para realizar pruebas. Esto también se puede utilizar para enviar correos electrónicos transaccionales a todos tus usuarios (incluidos los que se han dado de baja) utilizando el especificador \"La dirección de correo electrónico no está en blanco\" dentro del filtro, para que puedas maximizar la entrega de correos electrónicos independientemente del estado de adhesión voluntaria. <br><br>Este filtro sólo comprueba si los perfiles de usuario tienen una dirección de correo electrónico, mientras que el filtro <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">Correo electrónico</a> disponible comprueba criterios adicionales."
    tags:
      - Other Filters
  - name: ID de usuario externo
    description: Le permite designar los destinatarios de sus campañas por ID de usuario individuales para realizar pruebas.
    tags:
      - Other Filters
  - name: "# Contenedor aleatorio"
    description: Segmenta a tus usuarios por un número asignado aleatoriamente (de 0 a 9999 inclusive). Puede permitir la creación de segmentos uniformemente distribuidos de usuarios verdaderamente aleatorios para pruebas A/B y multivariantes.
    tags:
      - Other Filters
  - name: Recuento de sesiones
    description: Segmenta a tus usuarios por el número de sesiones que han tenido en cualquiera de tus aplicaciones dentro de tu espacio de trabajo.
    tags:
      - Sessions
  - name: Recuento de sesiones para aplicación
    description: Segmenta a tus usuarios por el número de sesiones que han tenido en una app concreta y determinada.
    tags:
      - Sessions
  - name: X sesiones en los últimos Y días
    description: "Segmenta a tus usuarios por el número de sesiones (entre 0 y 50) que han tenido en tu app en el último número especificado de días naturales entre 1 y 30. <br> <a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a>"
    tags:
      - Sessions
  - name: Primera aplicación usada
    description: "Segmenta a los usuarios en función de la primera vez que abrieron la aplicación. <em>Ten en cuenta que esto capturará la primera sesión que tengan utilizando una versión de tu aplicación con el SDK de Braze integrado.</em> (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Sessions
  - name: Primera aplicación concreta usada
    description: "Segmenta a tus usuarios según la hora más temprana registrada en la que abrieron cualquiera de tus aplicaciones dentro de tu espacio de trabajo. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Sessions
  - name: Última aplicación usada
    description: "Segmenta a tus usuarios según la última vez que han abierto tu aplicación. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Sessions
  - name: Última aplicación concreta usada
    description: "Segmenta a tus usuarios en función de la última vez que han abierto una aplicación determinada. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Sessions
  - name: Duración promedio de la sesión
    description: Segmenta a tus usuarios según la duración media de sus sesiones en tu aplicación.
    tags:
      - Sessions
  - name: Mensaje recibido de una campaña
    description: "Segmenta a tus usuarios en función de si han recibido o no una campaña concreta.<br><br> Para tarjetas de contenido, banners y mensajes dentro de la aplicación, esto es cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando el mensaje es enviado al usuario.<br><br> En el caso de WhatsApp, se trata del momento en que se envía la última solicitud de la API de mensajes a WhatsApp, no del momento en que se entrega el mensaje al dispositivo del usuario. <br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega). Cuando varios usuarios comparten la misma dirección de correo electrónico:<br>- En el envío inicial, solo se actualiza el perfil del usuario objetivo específico. <br>- Cuando se entrega el correo electrónico, o si el usuario abre el correo o un enlace del mismo, todos los usuarios que compartan esa dirección de correo electrónico parecerán haber recibido el mensaje.<br><br>En el caso de los SMS, es el momento en que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario."
    tags:
      - Retargeting
  - name: Variante de campaña recibida
    description: "Segmenta a tus usuarios según la variante de una campaña multivariante que han recibido.<br><br> Para tarjetas de contenido, banners y mensajes dentro de la aplicación, esto es cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando el mensaje es enviado al usuario.<br><br> En el caso de WhatsApp, se trata del momento en que se envía la última solicitud de la API de mensajes a WhatsApp, no del momento en que se entrega el mensaje al dispositivo del usuario. <br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega). Cuando varios usuarios comparten la misma dirección de correo electrónico:<br>- En el envío inicial, solo se actualiza el perfil del usuario objetivo específico. <br>- Cuando se entrega el correo electrónico, o si el usuario abre el correo o un enlace del mismo, todos los usuarios que compartan esa dirección de correo electrónico parecerán haber recibido el mensaje.<br><br>En el caso de los SMS, es el momento en que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario."
    tags:
      - Retargeting
  - name: Mensaje recibido de un paso en Canvas
    description: "Segmenta a sus usuarios en función de si han recibido o no un componente específico de Canvas.<br><br> En el caso de las tarjetas de contenido y los mensajes dentro de la aplicación, esto ocurre cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando el mensaje es enviado al usuario.<br><br> En el caso de WhatsApp, se trata del momento en que se envía la última solicitud de la API de mensajes a WhatsApp, no del momento en que se entrega el mensaje al dispositivo del usuario. <br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega). Cuando varios usuarios comparten la misma dirección de correo electrónico:<br>- En el envío inicial, solo se actualiza el perfil del usuario objetivo específico. <br>- Cuando se entrega el correo electrónico, o si el usuario abre el correo o un enlace del mismo, todos los usuarios que compartan esa dirección de correo electrónico parecerán haber recibido el mensaje.<br><br>En el caso de los SMS, es el momento en que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario."
    tags:
      - Retargeting
  - name: Último mensaje recibido de un paso de Canvas concreto
    description: Segmenta a sus usuarios según el momento en que recibieron un componente Canvas específico. Este filtro no tiene en cuenta si los usuarios han recibido otros componentes Canvas.
    tags:
      - Retargeting
  - name: Último mensaje recibido de una campaña concreta
    description: Segmenta a tus usuarios en función de si han recibido o no una campaña concreta. Este filtro no tiene en cuenta si los usuarios han recibido otras campañas.
    tags:
      - Retargeting
  - name: Mensaje recibido de una campaña o Canvas con etiqueta
    description: "Segmenta a tus usuarios en función de si han recibido o no una determinada campaña o Canvas con una etiqueta específica.<br><br> Para tarjetas de contenido, banners (sólo campañas) y mensajes dentro de la aplicación, esto es cuando un usuario registra una impresión, no cuando se envía la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando el mensaje es enviado al usuario.<br><br> En el caso de WhatsApp, se trata del momento en que se envía la última solicitud de la API de mensajes a WhatsApp, no del momento en que se entrega el mensaje al dispositivo del usuario. <br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega). Cuando varios usuarios comparten la misma dirección de correo electrónico:<br>- En el envío inicial, solo se actualiza el perfil del usuario objetivo específico. <br>- Cuando se entrega el correo electrónico, o si el usuario abre el correo o un enlace del mismo, todos los usuarios que compartan esa dirección de correo electrónico parecerán haber recibido el mensaje.<br><br>En el caso de los SMS, es el momento en que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario."
    tags:
      - Retargeting
  - name: Último mensaje recibido de una campaña o de Canvas con una etiqueta concreta
    description: Segmenta a tus usuarios en función de cuándo recibieron una campaña o un Canvas concreto con una etiqueta específica. Este filtro no tiene en cuenta si los usuarios han recibido otras campañas o Lienzos. (período de 24 horas)
    tags:
      - Retargeting
  - name: Jamás recibió un mensaje de campaña o de paso en Canvas
    description: Segmenta a tus usuarios en función de si han recibido o no algún componente de la campaña o del Canvas.
    tags:
      - Retargeting
  - name: Último correo electrónico recibido
    description: "Segmenta a tus usuarios según la última vez que han recibido uno de tus mensajes de correo electrónico. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Retargeting
  - name: Última notificación emergente recibida
    description: "Segmenta a tus usuarios según la última vez que recibieron una de tus notificaciones push. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Retargeting
  - name: Última impresión de un mensaje dentro de la aplicación
    description: Segmenta a tus usuarios según la última vez que vieron un mensaje in-app.
    tags:
      - Retargeting
  - name: Último SMS recibido
    description: "Segmenta a tus usuarios por la hora a la que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Retargeting
  - name: Último webhook recibido
    description: "Segmenta tus usuarios por la última vez que Braze envió un webhook para ese usuario. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Retargeting
  - name: Último WhatsApp recibido
    description: "Segmenta a tus usuarios según la última vez que recibieron un mensaje de WhatsApp. Es cuando se envía la última solicitud de la API de mensajes a WhatsApp, no cuando se entrega el mensaje al dispositivo del usuario. (período de 24 horas)<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Retargeting
  - name: Campaña que se abrió o a la que se hizo clic
    description: "Filtrar por interacción con una campaña específica. Para el envío por correo electrónico, el evento de apertura incluye tanto las aperturas por máquina como las aperturas sin máquina.<br><br> Para el correo electrónico, esto también incluye la opción de filtrar por \"abrió cualquier correo electrónico (máquina abre)\" y \"abrió cualquier correo electrónico (otras aperturas)\". Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando se abre el correo electrónico o se hace clic en él, también se actualizan los perfiles de todos los demás usuarios con esa misma dirección de correo electrónico. <br>- Si el usuario original cambia su dirección de correo electrónico después del envío del mensaje y antes de la apertura o el clic, la apertura o el clic se aplican a todos los usuarios restantes con esa dirección de correo electrónico en lugar de al usuario original.<br><br>Para los SMS, una interacción se define como:<br>- El último usuario que envió un SMS de respuesta que coincide con una categoría de palabras clave determinada. Se atribuye a la campaña más reciente recibida por todos los usuarios con este número de teléfono. La campaña debe haberse recibido en las últimas cuatro horas.<br>- El usuario seleccionó por última vez cualquier enlace acortado en un mensaje SMS que tenga activado el seguimiento de clics del usuario, de una campaña determinada."
    tags:
      - Retargeting
  - name: Campaña o Canvas que se abrió o en la que se hizo clic con etiqueta
    description: "Filtrar por interacción con una campaña específica que tiene una etiqueta específica. Para el envío por correo electrónico, el evento de apertura incluye tanto las aperturas por máquina como las aperturas sin máquina.<br><br> Para el correo electrónico, esto incluye la opción de filtrar por \"abrió cualquier correo electrónico (aperturas de máquina)\" y \"abrió cualquier correo electrónico (otras aperturas)\". Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando se abre el correo electrónico o se hace clic en él, también se actualizan los perfiles de todos los demás usuarios con esa misma dirección de correo electrónico. <br>- Si el usuario original cambia su dirección de correo electrónico después del envío del mensaje y antes de la apertura o el clic, la apertura o el clic se aplican a todos los usuarios restantes con esa dirección de correo electrónico en lugar de al usuario original.<br><br>Para los SMS, una interacción se define como:<br>- El último usuario que envió un SMS de respuesta que coincide con una categoría de palabras clave determinada. Se atribuye a la campaña más reciente recibida por todos los usuarios con este número de teléfono. La campaña debe haberse recibido en las últimas cuatro horas.<br>- Cuando el usuario seleccionó por última vez cualquier enlace acortado en un mensaje SMS que tenga activado el seguimiento de clics del usuario, desde una campaña o paso de Canvas con etiqueta determinada."
    tags:
      - Retargeting
  - name: Paso que se abrió o en el que se hizo clic
    description: "Filtrar por interacción con un componente Canvas específico. Para el envío por correo electrónico, el evento de apertura incluye tanto las aperturas por máquina como las aperturas sin máquina.<br><br>Para el correo electrónico, esto incluye la opción de filtrar por \"abrió cualquier correo electrónico (aperturas de máquina)\" y \"abrió cualquier correo electrónico (otras aperturas)\".<br><br>Para los SMS, una interacción se define como:<br>- El último usuario que envió un SMS de respuesta que coincide con una categoría de palabras clave determinada. Se atribuye a la campaña más reciente recibida por todos los usuarios con este número de teléfono. La campaña debe haberse recibido en las últimas cuatro horas. <br>- El usuario seleccionó por última vez cualquier enlace acortado en un mensaje SMS que tenga activado el seguimiento de clics del usuario, desde un determinado paso de Canvas."
    tags:
      - Retargeting
  - name: Alias al que se hizo clic en la campaña
    description: "Filtre a sus usuarios por si han hecho clic en un alias específico en una campaña concreta. Esto sólo se aplica a los mensajes de correo electrónico. <br><br> Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando se abre el correo electrónico o se hace clic en él, también se actualizan los perfiles de todos los demás usuarios con esa misma dirección de correo electrónico. <br>- Si el usuario original cambia su dirección de correo electrónico después del envío del mensaje y antes de la apertura o el clic, la apertura o el clic se aplican a todos los usuarios restantes con esa dirección de correo electrónico en lugar de al usuario original."
    tags:
      - Retargeting
  - name: Alias en que se hizo clic en paso en Canvas
    description: "Filtre a sus usuarios por si han hecho clic en un alias específico en un Canvas concreto. Esto sólo se aplica a los mensajes de correo electrónico. <br><br> Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando se abre el correo electrónico o se hace clic en él, también se actualizan los perfiles de todos los demás usuarios con esa misma dirección de correo electrónico. <br>- Si el usuario original cambia su dirección de correo electrónico después del envío del mensaje y antes de la apertura o el clic, la apertura o el clic se aplican a todos los usuarios restantes con esa dirección de correo electrónico en lugar de al usuario original."
    tags:
      - Retargeting
  - name: Alias con clic en cualquier paso de campaña o lienzo
    description: "Filtra a tus usuarios por si han hecho clic en un alias específico en cualquier campaña o Canvas. Esto sólo se aplica a los mensajes de correo electrónico. <br><br> Si varios usuarios comparten la misma dirección de correo electrónico:<br>- Cuando se abre el correo electrónico o se hace clic en él, también se actualizan los perfiles de todos los demás usuarios con esa misma dirección de correo electrónico. <br>- Si el usuario original cambia su dirección de correo electrónico después del envío del mensaje y antes de la apertura o el clic, la apertura o el clic se aplican a todos los usuarios restantes con esa dirección de correo electrónico en lugar de al usuario original."
    tags:
      - Retargeting
  - name: Rebote duro
    description: "Segmente a sus usuarios en función de si su dirección de correo electrónico ha rebotado o no (por ejemplo, si la dirección de correo electrónico no es válida)."
    tags:
      - Retargeting
  - name: Rebote blando
    description: "Segmenta a tus usuarios en función de si han rebotado blando X veces en Y días. Los filtros de segmento sólo pueden mirar 30 días atrás, pero puedes mirar más atrás con las extensiones de segmento.<br><br>Este filtro funciona de forma diferente a un evento de rebote blando en Currents. El filtro de segmento Rebote blando contabiliza un rebote blando si no hubo una entrega correcta durante el periodo de reintento de 72 horas. En Currents, cada reintento fallido se envía como un evento de rebote blando." 
    tags:
      - Retargeting
  - name: Te marcó como correo no deseado
    description: Segmenta a tus usuarios en función de si han marcado o no tus mensajes como spam.
    tags:
      - Retargeting
  - name: Número de teléfono no válido 
    description: Segmenta a tus usuarios según si su número de teléfono es inválido o no.
    tags:
      - Retargeting
  - name: Última categoría enviada de palabras clave entrantes de SMS específicas
    description: Segmenta a tus usuarios según la última vez que enviaron un SMS a un grupo de suscripción específico dentro de una categoría de palabras clave concreta. 
    tags:
      - Retargeting
  - name: Convertido desde campaña
    description: Segmenta a tus usuarios en función de si han convertido o no en una campaña concreta. Este filtro no incluye a los usuarios que están en el grupo de control.
    tags:
      - Retargeting
  - name: Convertido desde Canvas
    description: Segmenta a tus usuarios en función de si han convertido o no en un Canvas concreto. Este filtro no incluye a los usuarios que están en el grupo de control.
    tags:
      - Retargeting
  - name: Grupo de control en campaña
    description: Segmenta a sus usuarios en función de si estaban o no en el grupo de control de una campaña multivariante específica.
    tags:
      - Retargeting
  - name: Grupo de control en Canvas
    description: "Segmenta a tus usuarios en función de si estaban o no en el grupo de control de un Canvas concreto. Este filtro sólo evalúa a los usuarios que han entrado en el Canvas.<br><br>Por ejemplo, si filtra los usuarios que no están en el grupo de control de un lienzo, recibirá todos los usuarios que entraron en el lienzo pero que no están en el grupo de control."
    tags:
      - Retargeting
  - name: Últimos inscritos en cualquier grupo de control
    description: "Segmenta a tus usuarios por la última vez que cayeron en el grupo de control en una campaña. <br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Retargeting
  - name: Variación de Canvas ingresada
    description: "Segmenta a tus usuarios en función de si han entrado o no en una ruta de variación de un Canvas específico. Este filtro evalúa a todos los usuarios.<br><br>Por ejemplo, si filtra por usuarios que no han entrado en un grupo de control de variación de Canvas, recibirá todos los usuarios que no estén en el grupo de control independientemente de si han entrado en el Canvas."
    tags:
      - Retargeting
  - name: Último mensaje recibido
    description: "Segmenta a tus usuarios determinando el último mensaje recibido. (período de 24 horas)<br><br> En el caso de las tarjetas de contenido, las pancartas y los mensajes dentro de la aplicación, se trata del último momento en que el usuario registró una impresión, no del último momento en que se envió la tarjeta o el mensaje dentro de la aplicación.<br><br>Para push y webhooks, esto es cuando cualquier mensaje fue enviado al usuario.<br><br> En el caso de WhatsApp, se trata de cuándo se envió la última solicitud de la API de mensajes a WhatsApp, no cuándo se entregó el mensaje al dispositivo del usuario. <br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega). Cuando varios usuarios comparten la misma dirección de correo electrónico:<br>- En el envío inicial, solo se actualiza el perfil del usuario objetivo específico. <br>- Cuando se entrega el correo electrónico, o si el usuario abre el correo o un enlace del mismo, todos los usuarios que compartan esa dirección de correo electrónico parecerán haber recibido el mensaje.<br><br>En el caso de los SMS, es el momento en que se entregó el último mensaje al proveedor de SMS. Esto no garantiza que el mensaje haya llegado al dispositivo del usuario.<br><br>Ejemplo:<br>Último mensaje recibido hace menos de 1 día = hace menos de 24 horas<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Retargeting
  - name: Última interacción con un mensaje
    description: "Segmenta a tus usuarios según la última vez que han hecho clic o han abierto uno de tus canales de mensajería (Banners, tarjeta de contenido, correo electrónico, in-app, SMS, push, WhatsApp). Para el envío por correo electrónico, el evento de apertura incluye tanto las aperturas por máquina como las aperturas sin máquina. (período de 24 horas)<br><br>En el caso de los correos electrónicos, es cuando se envía una solicitud de correo electrónico al proveedor de servicios de correo electrónico (independientemente de si realmente se entrega). Esto también incluye la opción de filtrar por \"abrió cualquier correo electrónico (máquina abre)\" y \"abrió cualquier correo electrónico (otras aperturas)\". Cuando varios usuarios comparten la misma dirección de correo electrónico:<br>- En el envío inicial, solo se actualiza el perfil del usuario objetivo específico. <br>- Cuando se entrega el correo electrónico, o si el usuario abre el correo o un enlace del mismo, todos los usuarios que compartan esa dirección de correo electrónico parecerán haber recibido el mensaje.<br><br>En el caso de los SMS, se trata del momento en que el usuario seleccionó por última vez cualquier enlace acortado en un mensaje que tenga activado el seguimiento de clics del usuario.<br><br>Zona horaria:<br>Zona horaria de la empresa"
    tags:
      - Retargeting
  - name: Tarjeta clicada 
    description: "Segmenta a sus usuarios en función de si han hecho clic o no en una tarjeta de contenido específica. Este filtro está disponible como subfiltro de \"Campaña clicada/abierta\", \"Campaña clicada/abierta o Canvas con etiqueta\" y \"Paso clicado/abierto\"."
    tags:
      - Retargeting
  - name: Conmutador de características
    description: "Segmento de usuarios que tienen activada una determinada <a href=\"/docs/developer_guide/feature_flags/\">función</a>."
    tags:
      - Retargeting
  - name: Grupo de suscripción
    description: "Segmenta a tus usuarios por su grupo de suscripción para correo electrónico, SMS/MMS o WhatsApp. Los Grupos archivados no aparecerán y no podrán utilizarse."
    tags:
      - Channel subscription behavior
  - name: Correo electrónico disponible
    description: "Segmenta a tus usuarios según si tienen una dirección de correo electrónico válida, y si están suscritos o han optado por la adhesión voluntaria al correo electrónico. Este filtro comprueba tres criterios: si el usuario se ha dado de baja de los correos electrónicos, si Braze ha recibido un rebote duro y si el correo se marcó como correo no deseado. Si se cumple alguno de estos criterios, o si no existe un correo electrónico para un usuario, éste no será incluido.<br><br>Ten en cuenta que si envías un mensaje transaccional, los usuarios cuyo \"Correo electrónico disponible\" sea <code>false</code> no se incluirán en el cálculo de audiencia, pero podrían recibir un mensaje. Sin embargo, el cálculo de la audiencia sólo incluirá a los usuarios suscritos o con adhesión voluntaria. <br><br>Para los correos electrónicos en los que el estado de adhesión voluntaria es importante, te sugerimos que utilices el filtro \"Correo electrónico disponible\" en lugar del filtro <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">Dirección de correo electrónico</a>; los criterios adicionales pueden ayudarte a dirigirte a los usuarios que realmente quieren ver tus mensajes."
    tags:
      - Channel subscription behavior
  - name: Fecha de adhesión voluntaria por correo electrónico
    description: Segmenta a tus usuarios por la fecha en la que optaron por el correo electrónico.
    tags:
      - Channel subscription behavior
  - name: Estado de la suscripción del correo electrónico
    description: Segmenta a tus usuarios según su estado de suscripción al correo electrónico.
    tags:
      - Channel subscription behavior
  - name: Fecha de cancelación de suscripción del correo electrónico 
    description: Segmenta a tus usuarios por la fecha en la que se dieron de baja de futuros correos electrónicos.
    tags:
      - Channel subscription behavior
  - name: Notificaciones push habilitadas
    description: "Segmenta a los usuarios que tienen autorización push provisional o están habilitados para push en primer plano. En concreto, este recuento incluye:<br>1. Usuarios de iOS autorizados provisionalmente para push. <br>2. Usuarios que activaron explícitamente las notificaciones push para cualquiera de las aplicaciones de su espacio de trabajo. Para estos usuarios, este recuento incluye sólo las pulsaciones en primer plano.<br><br>Push Activado no incluye a los usuarios que se han dado de baja. <br><br>Después de segmentar con este filtro, podrás ver un desglose de quién está en ese segmento para Android, iOS y web en el panel inferior, llamado <em>Usuarios alcanzables</em>."
    tags:
      - Channel subscription behavior
  - name: Notificaciones push habilitadas para la aplicación
    description: "Segmenta según si los usuarios tienen activada la función push para tu aplicación en su dispositivo. Estos usuarios son accesibles mediante push, pero puede que no hayan optado por ello. Este recuento incluye a los usuarios que han autorizado provisionalmente tokens push en primer y segundo plano."
    tags:
      - Channel subscription behavior
  - name: Notificaciones push de fondo habilitadas
    description: Segmenta según si los usuarios tienen un token de notificaciones push y no se han dado de baja.
    tags:
      - Channel subscription behavior
  - name: Fecha de adhesión voluntaria a notificaciones push
    description: Segmenta a tus usuarios por la fecha en la que optaron por push.
    tags:
      - Channel subscription behavior
  - name: Estado de la suscripción a notificaciones push
    description: "Segmenta a tus usuarios por su <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">estado de suscripción</a> para push."
    tags:
      - Channel subscription behavior
  - name: Fecha de cancelación de suscripción a notificaciones push
    description: Segmenta a tus usuarios por la fecha en la que se dieron de baja de futuras notificaciones push.
    tags:
      - Channel subscription behavior
  - name: Producto comprado
    description: Segmenta a tus usuarios por productos comprados en tu app.
    tags:
      - Purchase behavior
  - name: Cantidad total de compras
    description: Segmenta a tus usuarios según el número de compras que han realizado en tu aplicación.
    tags:
      - Purchase behavior
  - name: X producto comprado en Y días
    description: Filtre a los usuarios por las veces que se compró un producto específico.
    tags:
      - Purchase behavior
  - name: X compras en los últimos Y días
    description: "Segmenta a tus usuarios por el número de veces (entre 0 y 50) que han realizado una compra en el último número especificado de días naturales entre 1 y 30. <br> <a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a>"
    tags:
      - Purchase behavior
  - name: Propiedad de compra X en Y días
    description: "Segmenta a sus usuarios por el número de veces que se ha realizado una compra en relación con una determinada propiedad de compra en el último número especificado de días naturales entre 1 y 30. <br> <a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a>"
    tags:
      - Purchase behavior
  - name: Primera compra hecha
    description: Segmenta a tus usuarios según la primera vez que un usuario realizó una compra en tu aplicación.
    tags:
      - Purchase behavior
  - name: Primera compra de la aplicación
    description: Segmenta a tus usuarios según la primera vez que un usuario realizó una compra en tu aplicación.
    tags:
      - Purchase behavior
  - name: Última compra hecha
    description: Filtre a los usuarios por la última vez que realizaron una compra.
    tags: 
      - Purchase behavior
  - name: Último producto comprado
    description: Filtre a los usuarios por la última vez que compraron un producto específico.
    tags:
      - Purchase behavior
  - name: Dinero gastado
    description: Segmenta a tus usuarios por la cantidad de dinero que han gastado en tu aplicación.
    tags:
      - Purchase behavior
  - name: X dinero gastado en Y días
    description: "Segmenta a tus usuarios por la cantidad de dinero que han gastado en tu aplicación en el último número especificado de días naturales entre 1 y 30. Este importe sólo incluirá la suma de las últimas 50 compras. <br> <a href=\"/docs/x-in-y-behavior/\"> Aprende más sobre el comportamiento X-en-Y aquí.</a>"
    tags:
      - Purchase behavior
  - name: País
    description: Segmenta a tus usuarios por la ubicación del último país indicado.
    tags:
      - Demographic attributes
  - name: Localidad
    description: Segmenta a tus usuarios por la ubicación de su última ciudad indicada.
    tags:
      - Demographic attributes
  - name: Idioma
    description: Segmenta a tus usuarios por su idioma preferido.
    tags:
      - Demographic attributes
  - name: Edad
    description: "Segmenta a tus usuarios por su edad, tal y como indican desde tu aplicación."
    tags:
      - Demographic attributes
  - name: Cumpleaños
    description: "Segmenta a tus usuarios por su fecha de cumpleaños, tal y como indicaron desde tu aplicación. <br> Los usuarios que cumplan años el 29 de febrero se incluirán en los segmentos que incluyan el 1 de marzo.<br><br>Para apuntar a los cumpleaños de diciembre o enero, inserte la lógica de filtro sólo dentro del intervalo de 12 meses del año al que apunta. En otras palabras, no introduzca lógica que se remonte al mes de diciembre del año anterior o al mes de enero del año siguiente. Por ejemplo, para los cumpleaños de diciembre, puede filtrar por \"el 31 de diciembre\", \"antes del 31 de diciembre\" o \"después del 30 de noviembre\"."
    tags:
      - Demographic attributes
  - name: Género
    description: "Segmenta a tus usuarios por género, tal y como indicaron desde tu aplicación."
    tags:
      - Demographic attributes
  - name: Número de teléfono sin formato
    description: "Segmenta a tus usuarios por su número de teléfono sin formato. No incluye paréntesis, guiones ni otros símbolos."
    tags:
      - Demographic attributes
  - name: Nombre
    description: "Segmenta a tus usuarios por su nombre de pila, tal y como lo indicaron desde tu aplicación."
    tags:
      - Demographic attributes
  - name: Apellido
    description: "Segmenta a tus usuarios por su apellido, tal y como lo indicaron desde tu aplicación."
    tags:
      - Demographic attributes
  - name: Tiene la aplicación
    description: "Segmenta en función de si el usuario ha instalado alguna vez su aplicación o no. Esto incluirá a los usuarios que actualmente tienen su aplicación instalada y a los que la han desinstalado en el pasado. Esto requiere generalmente que los usuarios abran la aplicación (inicien una sesión) para ser incluidos en este filtro. Sin embargo, hay algunas excepciones, como si un usuario se importó a Braze y se asoció manualmente a su aplicación."
    tags:
      - App
  - name: Nombre de la versión más reciente de la aplicación
    description: Segmenta por el nombre reciente de la aplicación del usuario.
    tags:
      - App 
  - name: Número de la versión más reciente de la aplicación
    description: Segmenta por el número de versión reciente de la aplicación del usuario.
    tags:
      - App 
  - name: Desinstalada
    description: Segmenta a tus usuarios en función de si han desinstalado tu aplicación y no la han vuelto a instalar.
    tags:
      - Uninstall 
  - name: Operador del dispositivo
    description: Segmenta a tus usuarios según el operador de su dispositivo.
    tags:
      - Devices
  - name: Recuento de dispositivos
    description: Segmenta a tus usuarios según el número de dispositivos en los que han utilizado tu aplicación.
    tags:
      - Devices
  - name: Modelo del dispositivo
    description: Segmenta a tus usuarios por la versión del modelo de su teléfono móvil.
    tags:
      - Devices
  - name: Sistema operativo del dispositivo
    description: Segmenta a los usuarios que tienen uno o más dispositivos con el sistema operativo especificado.
    tags:
      - Devices
  - name: Configuración regional del dispositivo más reciente
    description: "Segmenta a sus usuarios según la <a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">información de localización</a> del dispositivo utilizado más recientemente."
    tags:
      - Devices      
  - name: Modelo de reloj más reciente
    description: Segmenta a tus usuarios según su modelo de smartwatch más reciente.
    tags:
      - Devices    
  - name: Autorizados provisionalmente en iOS
    description: Permite encontrar usuarios autorizados provisionalmente en iOS 12 para una app determinada.
    tags:
      - Devices   
  - name: Navegador web
    description: Segmenta a tus usuarios según el navegador que utilizan para acceder a tu web.
    tags:
      - Devices
  - name: Identificador para anunciantes (IDFA) del dispositivo
    description: Te permite designar los destinatarios de tu campaña por IDFA para realizar pruebas.
    tags:
      - Advertising use cases
  - name: IDFV del dispositivo
    description: Le permite designar los destinatarios de su campaña por IDFV para realizar pruebas.
    tags:
      - Advertising use cases 
  - name: ID de anuncios de Google del dispositivo
    description: Segmenta a tus usuarios por el ID del anuncio de Google.
    tags:
      - Advertising use cases
  - name: ID de anuncios de Roku del dispositivo
    description: Segmenta a tus usuarios por el ID del anuncio de Roku.
    tags:
      - Advertising use cases
  - name: ID de anuncios de Windows del dispositivo
    description: Segmenta a sus usuarios por el ID de anuncio de Windows.
    tags:
      - Advertising use cases  
  - name: Seguimiento de anuncios habilitado
    description: "Le permite filtrar en función de si sus usuarios han optado por el seguimiento de anuncios. El seguimiento de anuncios está relacionado con el IDFA o \"identificador para anunciantes\" asignado a todos los dispositivos iOS por Apple, que puede configurarse mediante SDK. Este identificador permite a los anunciantes rastrear a los usuarios y ofrecerles anuncios específicos."
    tags:
      - Advertising use cases
  - name: Ubicación más reciente
    description: Segmenta a tus usuarios según la última ubicación registrada en la que han utilizado tu aplicación.
    tags:
      - Location
  - name: Ubicación disponible
    description: "Segmenta a tus usuarios en función de si han comunicado o no su ubicación. Para utilizar este filtro, tu aplicación debe tener <a href=\"/docs/search/?query=location%20tracking\">integrado el seguimiento de la ubicación.</a>"
    tags:
      - Location
  - name: Cohortes de amplitud
    description: Los clientes que utilizan Amplitude pueden completar sus segmentos eligiendo e importando sus cohortes en Amplitude.
    tags:
      - Cohort membership
  - name: Cohortes de Census
    description: Los clientes que utilizan Census pueden complementar sus segmentos eligiendo e importando sus cohortes en Census.
    tags:
      - Cohort membership
  - name: Cohortes de Heap
    description: Los clientes que utilizan Heap pueden completar sus segmentos eligiendo e importando sus cohortes en Heap.
    tags:
      - Cohort membership
  - name: Cohortes de Hightouch
    description: Los clientes que utilizan Hightouch pueden completar sus segmentos eligiendo e importando sus cohortes en Hightouch.
    tags:
      - Cohort membership
  - name: Cohortes de Kubit
    description: Los clientes que utilizan Kubit pueden completar sus segmentos eligiendo e importando sus cohortes en Kubit.
    tags:
      - Cohort membership
  - name: Cohortes de Mixpanel
    description: Los clientes que utilizan Mixpanel pueden complementar sus segmentos eligiendo e importando sus cohortes en Mixpanel.
    tags:
      - Cohort membership
  - name: Cohortes de Segment
    description: Los clientes que utilizan Segment pueden complementar sus segmentos eligiendo e importando sus cohortes en Segment.
    tags:
      - Cohort membership
  - name: Cohortes de Tinyclues
    description: Los clientes que utilizan Tinyclues pueden completar sus segmentos eligiendo e importando sus cohortes en Tinyclues.
    tags:
      - Cohort membership
  - name: Anuncio de atribución de instalación
    description: Segmenta a sus usuarios por el anuncio al que se atribuyó su instalación.
    tags:
      - User Attributes
  - name: Grupo de anuncios de atribución de instalación
    description: Segmenta a sus usuarios por el grupo de anuncios al que se atribuyó su instalación.
    tags:
      - Install Attribution
  - name: Campaña de atribución de instalación
    description: Segmenta a sus usuarios según la campaña publicitaria a la que se atribuyó su instalación.
    tags:
      - Install Attribution
  - name: Origen de atribución de instalación
    description: Segmenta a sus usuarios según la fuente a la que se atribuyó su instalación.
    tags:
      - Install Attribution
  - name: Categoría de riesgo de pérdida
    description:  Segmenta a sus usuarios por categoría de riesgo de pérdida de clientes según una predicción específica.
    tags:
      - Intelligence and predictive
  - name: Puntuación de riesgo de pérdida
    description: Segmenta a sus usuarios por puntuación de riesgo de abandono de acuerdo con una predicción específica.
    tags:
      - Intelligence and predictive
  - name: Categoría de probabilidad del evento
    description: Segmenta a sus usuarios por probabilidad de realizar un evento según una predicción específica.
    tags:
      - Intelligence and predictive
  - name: Puntuación de probabilidad del evento
    description: Segmenta a sus usuarios por probabilidad de realizar un evento según una predicción específica.
    tags:
      - Intelligence and predictive
  - name: Canal inteligente
    description: Segmente a sus usuarios por su canal más activo en los últimos tres meses.
    tags:
      - Intelligence and predictive
  - name: Probabilidad de mensaje abierto
    description: "Filtra a tus usuarios en función de su probabilidad de abrir un mensaje en un canal específico en una escala del 0 al 100%. Los usuarios sin datos suficientes para medir la probabilidad de un canal pueden seleccionarse mediante \"está en blanco\"."
    tags:
      - Intelligence and predictive
  - name: Cantidad de amigos de Facebook que usan la aplicación
    description: Segmenta a tus usuarios en función de cuántos amigos de Facebook tienen que utilizan la misma aplicación.
    tags:
      - Social activity
  - name: Facebook conectado
    description: Segmenta a tus usuarios en función de si han conectado tu aplicación a Facebook.
    tags:
      - Social activity
  - name: Twitter conectado
    description: Segmenta a tus usuarios en función de si han conectado tu aplicación a X (antes Twitter).
    tags:
      - Social activity
  - name: Cantidad de seguidores en Twitter
    description: Segmenta a tus usuarios según el número de seguidores X (antes Twitter) que tengan.
    tags:
      - Social activity
  - name: Número de teléfono
    description: "Segmenta a tus usuarios por el campo del número de teléfono con formato E.164.<br><br> Cuando se envía un número de teléfono a Braze, éste intenta coaccionarlo para que adopte el <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">formato e.164</a> que se utiliza para enviar a través de los canales SMS y WhatsApp. El proceso de coacción puede fallar si el número no está formateado correctamente, lo que hace que el perfil de usuario tenga un número de teléfono sin formatear, pero no un número de teléfono de envío. Este filtro de segmento devuelve a los usuarios por su número de teléfono con formato e.164 (cuando está disponible).<br><br>Casos de uso:<br> - Utiliza este filtro para conocer con mayor precisión el tamaño de la audiencia objetivo al enviar mensajes SMS o WhatsApp.  <br>- Utiliza expresiones regulares (regex) con este filtro para segmentar por números de teléfono con un código de país concreto. <br>- Utiliza este filtro para segmentar a los usuarios por números de teléfono que no hayan superado el proceso de coerción e.164."
    tags:
      - Other filters
---
