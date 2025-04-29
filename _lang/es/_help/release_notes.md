---
nav_title: Notas de publicación
article_title: Notas de publicación
page_order: 4
layout: dev_guide
guide_top_header: "Notas de publicación"
guide_top_text: "Aquí es donde puedes encontrar todas las actualizaciones de la plataforma Braze, con las siguientes <a href='/docs/help/release_notes/#most-recent'>actualizaciones de plataforma más recientes</a>."
page_type: landing
search_rank: 1
description: "En esta página encontrarás las notas de la versión de Braze. Aquí es donde puedes encontrar todas las actualizaciones de la plataforma Braze y los SDK, así como una lista de características obsoletas."

guide_featured_title: "Notas de publicación"
guide_featured_list:
  - name: 2025
    link: /docs/help/release_notes/2025/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2024
    link: /docs/help/release_notes/2024/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2023
    link: /docs/help/release_notes/2023/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2022
    link: /docs/help/release_notes/2022/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2021
    link: /docs/help/release_notes/2021/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2020
    link: /docs/help/release_notes/2020/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2019
    link: /docs/help/release_notes/2019/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2018
    link: /docs/help/release_notes/2018/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2017
    link: /docs/help/release_notes/2017/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2016
    link: /docs/help/release_notes/2016/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Depreciaciones
    link: /docs/help/release_notes/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: Registros de cambios del SDK
    link: /docs/developer_guide/changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Notas de la versión más reciente de Braze {#most-recent}

> Braze publica información sobre las actualizaciones del producto con una cadencia mensual, en consonancia con las principales versiones del producto, aunque el producto se actualiza con mejoras varias semana a semana.
> <br>
> <br>

> Para obtener más información sobre cualquiera de las actualizaciones enumeradas en esta sección, ponte en contacto con tu director de cuentas o [abre un ticket de soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). También puedes consultar [nuestros registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs) para ver más información sobre nuestros lanzamientos, actualizaciones y mejoras mensuales del SDK.
 
## Liberación el 1 de abril de 2025

### Actualizaciones de la navegación Braze

La navegación actualizada en Braze está diseñada para ayudarte a acceder eficazmente a características y contenidos en todos los dispositivos. Nota que la opción de cambiar entre versiones de navegación ya no está disponible. Más información en nuestro artículo dedicado a [Navegar por Braze]({{site.baseurl}}/user_guide/administrative/access_braze/navigation).

### Guía del desarrollador detangle

Antes, muchas tareas a nivel de plataforma se dividían en varias páginas, como la integración del SDK de Swift, que se dividía en seis páginas. Además, las características compartidas estaban documentadas individualmente para cada plataforma, lo que significaba que la búsqueda de un tema como "Configuración de las notificaciones push" devolvía 10 páginas diferentes.

**Antes:**

![La documentación anterior de Swift ubicada en la sección Guías de integración de plataformas.]({% image_buster /assets/img/before_swift.png %})

Ahora, las tareas a nivel de plataforma se han fusionado en páginas individuales y las características compartidas del SDK existen ahora en la misma página (con la ayuda de nuestra nueva característica de pestañas SDK). Por ejemplo, ahora sólo hay una página para Integrar el SDK de Braze, en la que puedes cambiar de plataforma seleccionando una pestaña en la parte superior de la página. Cuando lo hagas, incluso el índice de la página se actualizará para reflejar la pestaña seleccionada en ese momento.

**Después:**

![La documentación actualizada de Swift se encuentra en la pestaña Swift del artículo Integración del SDK.]({% image_buster /assets/img/after_swift.png %})

![La documentación actualizada de Android se encuentra en la pestaña Android del artículo Integración del SDK.]({% image_buster /assets/img/after_android.png %})

### Contribuir a la documentación de Braze

Por si no lo sabías, ¡nuestros documentos son totalmente de código abierto! Puedes aprender cómo hacerlo en nuestra [Guía de Contribución]({{site.baseurl}}/contributing/home). Este mes, hemos documentado algunas funcionalidades del sitio, como [forzar la autoexpansión de las secciones]({{site.baseurl}}/contributing/content_management/sections#forcing-auto-expand) y [mostrar contenido generado por la API]({{site.baseurl}}/contributing/generating_a_preview#step-2-start-a-local-server).

### Flexibilidad de los datos

#### Actualización de las propiedades de entrada en Canvas

Las propiedades de entrada del Canvas ahora forman parte de [las variables de contexto del Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Cada variable contextual incluye un nombre, un tipo de datos y un valor que puede incluir Liquid. Para más información, consulta el [componente Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

#### Actualizaciones de los filtros de segmentación para filtrar números de teléfono

Se han actualizado los filtros de segmentación para reflejar los cambios en dos filtros de números de teléfono:

- [Número de teléfono sin formato]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#unformatted-phone-number) (antes **Número de teléfono**): Segmenta a tus usuarios por su número de teléfono sin formato.
- [Número de teléfono]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#phone-number) (antes **Número de teléfono remitente**): Segmenta a tus usuarios según el campo del número de teléfono formateado en E.164.

#### Borrar datos personalizados

A medida que construyas campañas y segmentos específicos, puede que te des cuenta de que ya no necesitas un evento personalizado o un atributo personalizado. Ahora puedes [borrar estos datos personalizados]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data) y eliminar sus referencias de tu aplicación.

#### Importar usuarios con direcciones de correo electrónico y números de teléfono

Ahora puedes utilizar una dirección de correo electrónico o un número de teléfono para [importar usuarios]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#importing-with-email-addresses-and-phone-numbers) y omitir un ID externo o un alias de usuario.

#### Solución de problemas de inicio de sesión iniciada por el proveedor de servicios

El inicio de sesión iniciado por el proveedor de servicios (SP) tiene ahora una [sección de solución de problemas]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#troubleshooting) para ayudarte a resolver los problemas con SAML y el inicio de sesión único.

#### Solución de problemas de importación de usuarios

La [sección de solución de problemas de importación de usuarios]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#troubleshooting) tiene entradas nuevas y actualizadas, que incluyen cómo solucionar el problema de las filas que faltan en tus archivos CSV importados.

#### Preguntas frecuentes sobre las extensiones de segmento

Consulta nuestras [preguntas frecuentes]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#frequently-asked-questions) sobre las extensiones de segmento, incluyendo cómo puedes crear una extensión de segmento que utilice varios eventos personalizados.

#### Retrasos personalizados y ampliados

{% multi_lang_include release_type.md release="Acceso anticipado" %}

Puedes configurar un [retraso personalizado]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step#personalized-delays) para tus usuarios y utilizarlo con un paso Contexto para seleccionar la variable de contexto por la que se retrasará.

Ahora también puedes prolongar los pasos de Retraso hasta dos años. Por ejemplo, si estás incorporando nuevos usuarios a tu aplicación, puedes añadir un retraso de dos meses antes de enviar un paso de Mensaje para animar a los usuarios que no han iniciado una sesión.

#### Atributos predeterminados del perfil de usuario para Snowflake

{% multi_lang_include release_type.md release="Beta" %}

Ahora hay tres [atributos predeterminados del perfil de usuario]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/user_attributes) en Snowflake. Cada vista está diseñada para un caso de uso específico con sus propias consideraciones de rendimiento. Por ejemplo, se te puede proporcionar un snapchat periódico de los atributos predeterminados de un perfil de usuario.

### Canales robustos

#### Fundamentos de la mensajería

[Fundamentos de la mensajería]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals) es una nueva sección en Herramientas de interacción que alberga los conceptos y términos compartidos para campañas y Lienzos, como archivar y localizar mensajes.

#### Dominios personalizados de WhatsApp

Ahora puedes asignar [dominios personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/) a uno o varios grupos de suscripción de WhatsApp.

#### Mensajes desencadenados dentro de la aplicación para Canvas

Ahora puedes seleccionar un [desencadenante para que tus mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) se desencadenen al iniciar la sesión, o por eventos personalizados y compras. Una vez transcurridos los retrasos y comprobadas las opciones de audiencia, los mensajes dentro de la aplicación se activan en vivo cuando un usuario llega al paso Mensaje. Si un usuario inicia una sesión y realiza el evento desencadenante del mensaje dentro de la aplicación, el usuario verá el mensaje dentro de la aplicación. 

#### Limitar el volumen de entrada para Canvas

Puedes limitar el número de personas que potencialmente entrarían en este Canvas según una cadencia seleccionada (diariamente, durante toda la vida del Canvas o cada vez que se programe el Canvas). Por ejemplo, puedes [configurar los controles de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience) para que el Canvas sólo envíe a 5.000 usuarios al día.

#### Nuevo caso de uso: Sistema de recordatorio de reservas por correo electrónico

Aprende a utilizar las características de Braze para [crear un servicio de mensajería por correo electrónico de recordatorio de reserva]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case). El servicio permitirá a los usuarios reservar citas y enviará mensajes a los usuarios recordándoles sus próximas citas. Aunque este caso de uso utiliza mensajes de correo electrónico, puedes enviar mensajes en cualquier canal, o en varios, basándote en una única actualización de un perfil de usuario.

#### Seguimiento de clics en enlaces específicos

Puedes [desactivar el seguimiento de clics]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) para enlaces específicos añadiendo código HTML a tu mensaje de correo electrónico en el editor HTML o a los componentes en el editor de arrastrar y soltar.

#### Gestión dinámica de la pasarela del servicio de notificaciones push de Apple

[La gestión dinámica de la pasarela APNs]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management) mejora la fiabilidad y eficacia de las notificaciones push de iOS al detectar automáticamente el entorno APNs correcto. Antes, seleccionabas manualmente los entornos APN (desarrollo o producción) para tus notificaciones push, lo que a veces provocaba configuraciones incorrectas de las pasarelas, fallos en la entrega y errores BadDeviceToken.

#### Soporte Flutter para tarjetas Banner

{% multi_lang_include release_type.md release="Acceso anticipado" %}

Las tarjetas Banner ahora son compatibles con Flutter. Además, se ha revisado toda la documentación de la tarjeta Banner para facilitar su uso. Consulta los siguientes artículos para empezar:

- [Acerca de las tarjetas Banner]({{site.baseurl}}/developer_guide/banner_cards)
- [Creación de campañas de tarjetas Banner]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns)
- [Insertar tarjetas Banner en tu aplicación]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards)

#### Seguimiento de clics en WhatsApp

{% multi_lang_include release_type.md release="Acceso anticipado" %}

[El seguimiento de clics]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/) te permite medir cuándo alguien pulsa un enlace en tu mensaje de WhatsApp, lo que te proporciona una visión clara del contenido que genera interacción. Braze acorta tus URL, añade seguimiento entre bastidores y registra los clics en el momento en que se producen.

#### Preguntas frecuentes sobre push

Echa un vistazo a nuestro nuevo artículo [Preguntas frecuentes sobre push]({{site.baseurl}}/user_guide/message_building_by_channel/push/faq), que aborda algunas de las preguntas más frecuentes que surgen al configurar campañas push.

#### Push solución de problemas

[La solución de problemas push]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting) proporciona una serie de pasos para ayudarte a superar los problemas de entrega con las notificaciones push. Por ejemplo, si tienes problemas de entrega con las notificaciones push, hemos recopilado los pasos que puedes seguir para solucionar el problema.

### Nuevas asociaciones Braze

#### Movable Ink Da Vinci - Contenido dinámico

La integración de Braze y Movable Ink [con Da Vin]({{site.baseurl}}/partners/movable_ink_da_vinci) ci permite a las marcas entregar mensajes altamente personalizados aprovechando el motor de toma de decisiones sobre contenidos basado en IA de Da Vinci. Da Vinci selecciona el contenido más relevante para cada usuario y despliega fácilmente mensajes a través de Braze.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de Flutter 13.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Actualiza el puente nativo de Android de [Braze Android SDK 33.0.0 a 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - La versión mínima requerida del SDK de Android es la 25. Consulta más detalles [aquí](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [SDK de Swift v11.8.0-11.9.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Web v5.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## Lanzamiento el 4 de marzo de 2025

### Aplazamientos

Braze ha actualizado nuestra definición de lo que es un rebote blando y está enviando un nuevo evento llamado [aplazamientos]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance) a partir del 25 de febrero de 2025 a las 10 am EST.

Para los clientes de SendGrid, hemos realizado un cambio para separar los eventos de aplazamiento de nuestros eventos de rebote blando. Contamos los eventos diferidos como un evento de rebote blando. Esto afecta a cualquier cliente de Sendgrid que utilice Currents, Query Builder, SQL Extension, Snowflake Data Sharing o nuestro producto de correo electrónico transaccional.

#### Comportamiento previo

Antes del 25 de febrero de 2025, un evento de aplazamiento para una dirección de correo electrónico en una campaña o Canvas registra cada vez un evento de rebote blando. En consecuencia, los aplazamientos se incluyen como parte de los datos de rebote blando. Esto puede dar lugar a que un usuario o una campaña informen de más eventos de rebote blando de lo esperado. 

#### Nuevo comportamiento

A partir del 25 de febrero de 2025, un evento diferido ya no registrará cada vez un evento de rebote blando. En su lugar, registraremos un evento de rebote blando una vez por envío para la dirección de correo electrónico, independientemente de cuántas veces se reintente o aplace el correo electrónico.

#### Qué significa

A partir del 25 de febrero de 2025 notarás un descenso considerable en el volumen de eventos de rebote blando, lo que dará lugar a los siguientes cambios potenciales:

- Disminución de los rebotes blandos de los informes creados con el Generador de informes
- Segmento de menor tamaño utilizando extensiones SQL si te diriges a usuarios que han rebotado X veces durante un periodo Y
- Disminución del número de eventos de rebote blando entregados mediante Currents y cualquiera de nuestras características mediante Snowflake
- Descenso del número de rebotes blandos para el producto correo electrónico transaccional

Para los clientes de Sparkpost, no hay ningún impacto en tus datos de eventos de rebote blando, en su lugar empezarás a recibir un nuevo evento de correo electrónico, el aplazamiento, en Currents y Snowflake.

### Guía del desarrollador detangle

El contenido idéntico que se comparte en varios SDK está empezando a fusionarse mediante la nueva característica de pestañas SDK del sitio de documentación. Este mes se combinaron la [integración de SDK]({{site.baseurl}}/developer_guide/sdk_integration/), la [inicialización de SDK]({{site.baseurl}}/developer_guide/sdk_initialization/) y [las tarjetas de contenido]({{site.baseurl}}/developer_guide/content_cards/). Permanece atento a más actualizaciones en los próximos meses.

### Flexibilidad de los datos
 
#### Braze ID para perfiles de usuario

Un perfil de usuario incluye ahora un [ID de Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#user-profiles). Puedes utilizarlo cuando busques perfiles de usuario.

#### Aplazamientos

Braze ha actualizado nuestra definición de lo que es un rebote blando y está enviando un nuevo evento llamado [aplazamientos]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance), que es cuando un correo electrónico no se ha entregado inmediatamente, pero Braze reintentará el correo electrónico hasta 72 horas después de este fallo de entrega temporal para maximizar las posibilidades de éxito en la entrega antes de que se detengan los intentos para esa campaña específica.

#### Relaciones entre entidades Snowflake
 
Hemos mapeado los [esquemas de tablas sin procesar](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt) para las relaciones entre entidades de Snowflake y Braze en una nueva [página de documentación fácil de usar](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships). Incluye un desglose de las tablas `USER_MESSAGES` pertenecientes a cada canal, así como descripciones de las claves primarias, foráneas y nativas de cada tabla.

#### Gestión de identidades para ID externos

Utilizar una dirección de correo electrónico o una dirección de correo electrónico con hash como ID externo de Braze puede simplificar la gestión de identidades en todos tus orígenes de datos; sin embargo, es importante tener en cuenta los [riesgos potenciales]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) para la privacidad de los usuarios y la seguridad de los datos.
 
### Desbloquear la creatividad

#### Tutoriales Liquid

Añadidos tres [tutoriales Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/#tutorials) sobre cómo utilizar los operadores en los siguientes escenarios.

<table border="1">
  <tr>
    <td>Elegir un mensaje con un atributo personalizado entero.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/integer.png %}" alt="El paso de composición en Braze muestra un mensaje con un atributo personalizado entero." /></td>
  </tr>
  <tr>
    <td>Elegir un mensaje con un atributo personalizado de cadena.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/string.png %}" alt="El paso de composición en Braze muestra un mensaje con un atributo personalizado de cadena." /></td>
  </tr>
  <tr>
    <td>Cancelar un mensaje en función de la ubicación.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/location.png %}" alt="El paso de composición en Braze muestra un mensaje abortado en función de la ubicación." /></td>
  </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Pasos contextuales para Canvas
 
{% multi_lang_include release_type.md release="Acceso anticipado" %}
 
Utiliza [los pasos de Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) para crear o actualizar un conjunto de variables que representen el contexto de un usuario (o información sobre el comportamiento de ese usuario) a medida que se desplaza por un Canvas.

#### Retraso personalizado

{% multi_lang_include release_type.md release="Acceso anticipado" %}

Puedes configurar un [retardo personalizado]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) para tus usuarios seleccionando el alternador **Personalizar retardo** en tu paso Retardo. Puedes utilizarlo con un paso Contexto para seleccionar una variable contextual por la que retrasar.

Al configurar un paso de Retraso en tu recorrido de usuario de Canvas, ahora puedes crear un retraso de hasta 2 años.

#### Revertir la sincronización automática

Al [redactar un mensaje de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email), puedes volver a la sincronización automática en la pestaña Texto sin formato seleccionando el icono Regenerar a partir de HTML, que sólo aparece si el texto sin formato no se está sincronizando.

![El botón para revertir la sincronización automática en Braze.]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
### Canales robustos

#### Actualizaciones en vivo de Android

Aunque las Actualizaciones en vivo no estarán disponibles oficialmente hasta que
[Android 16](https://android-developers.googleblog.com/2025/01/first-beta-android16.html), nuestra página [Actualizaciones en vivo para Android]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=android&tab=local) te muestra cómo emular su comportamiento, para que puedas mostrar notificaciones interactivas en la pantalla de bloqueo similares a las [Actividades en vivo para el SDK de Swift Braze]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift). A diferencia de las Actualizaciones en vivo oficiales, esta funcionalidad puede implementarse para versiones anteriores de Android.

#### Copiar campañas con banderas de características entre espacios de trabajo

Ahora puedes [copiar campañas con banderas de características entre espacios de trabajo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/#copying-campaigns-with-feature-flags). Para ello, asegúrate de que el espacio de trabajo de destino tiene un experimento de bandera de características configurado con un ID que coincide con la bandera de características a la que se hace referencia en la campaña original.

#### Nuevos tipos de mensajes de WhatsApp compatibles

Los mensajes de WhatsApp ahora admiten [mensajes salientes de video, audio y documentación]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages). Ponte en contacto con tu director de cuentas de Braze si estás interesado en participar en el acceso anticipado.

#### Mensajes de derecha a izquierda

[Crear mensajes de]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) derecha a [izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) cubre las mejores prácticas para elaborar mensajes en idiomas que se leen de derecha a izquierda, de modo que tus mensajes se muestren con la mayor precisión posible.
 
### Automatización de IA y ML
 
#### Recomendaciones

[Utilizar recomendaciones de elementos en mensajería]({{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations) cubre el objeto `product_recommendation` Liquid e incluye un tutorial para ayudarte a poner en práctica esos conocimientos.

### Nuevas asociaciones Braze
 
#### Email Love - Extensiones de canal
 
La asociación entre Braze y [Email Love]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates) aprovecha la característica Exportar a Braze de Email Love y la API de Braze para cargar tus plantillas de correo electrónico a Braze fácilmente.

#### VWO - Pruebas A/B
 
La integración de Braze y [VWO]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/vwo) te permite aprovechar los datos de los experimentos de VWO para crear segmentos específicos y entregar campañas personalizadas.
 
### Actualizaciones del SDK
 
Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.
 
- [React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Aumenta los requisitos mínimos de React Native a la [versión 0.71.0](https://reactnative.dev/blog/2023/01/12/version-071). Para más información, consulta la [Política de soporte de versiones](https://github.com/reactwg/react-native-releases#releases-support-policy) en el Grupo de Trabajo React.
    - Aumenta la versión mínima requerida de iOS a 12.0.
    - Actualiza los enlaces de la versión nativa de iOS de [Braze Swift SDK 7.5.0 a 8.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualiza los enlaces de la versión nativa de Android de [Braze Android SDK 29.0.1 a 30.1.1](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

## Lanzamiento el 4 de febrero de 2025

### Mejoras en Braze Docs

#### Guía contribuyente
Nuestras recientes actualizaciones de la [Guía de Contribución]({{site.baseurl}}/contributing/your_first_contribution) facilitan a los usuarios no técnicos la contribución a Braze Docs.

#### Renovación de datos y análisis
Para que te resulte más fácil encontrar lo que buscas, hemos separado los artículos que antes estaban anidados en "Datos y análisis" en [Datos]({{site.baseurl}}/user_guide/data) y [análisis]({{site.baseurl}}/user_guide/analytics). 

#### Guía del desarrollador
Hemos hecho una gran limpieza de toda la documentación de [la Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/home), que incluye la fusión de "instrucciones" divididas en varias páginas en una sola.

También hay una nueva [página de referencia SDK]({{site.baseurl}}/developer_guide/references) que enumera toda la documentación de referencia y los repositorios de cada SDK de Braze.

##### SDK Braze de Unreal Engine
Hemos migrado y reescrito todo el contenido del README del repositorio GitHub del SDK Braze de Unreal Engine en su [sección dedicada en Braze Docs]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unreal%20engine).

### Flexibilidad de los datos

#### Panel de uso de la API

{% multi_lang_include release_type.md release="Disponibilidad general" %}

El [panel de uso de la API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard) te permite controlar el tráfico entrante de la API REST en Braze para comprender las tendencias de uso de nuestras API REST y solucionar posibles problemas.

#### Añadir etiquetas a atributos personalizados

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Puedes [añadir etiquetas a un atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#adding-tags) después de crearlo si tienes el permiso "Gestionar eventos, atributos, compras". Las etiquetas pueden utilizarse para filtrar la lista de atributos.

#### Selecciones de catálogo y puntos finales de campos de catálogo asíncronos 

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Los siguientes puntos finales ya están disponibles de forma general:
* [POST: Crear campos de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)
* [DELETE: Borrar campo de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)
* [DELETE: Borrar selección de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)
* [POST: Crear selección de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections)

#### Utilizar una dirección de correo electrónico para desencadenar campañas o Lienzos

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Ahora puedes especificar un destinatario por dirección de correo electrónico para desencadenar tus [campañas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users) y [Lienzos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience).

#### Utilizar un número de teléfono para identificar a un usuario a través de la API

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Ahora puedes utilizar un número de teléfono, además de un alias y una dirección de correo electrónico, para identificar a un usuario a través del [punto final de la API`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

#### Obtener una traza SAML
Hemos añadido [pasos sobre cómo obtener un rastreo SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace), que te ayuda a resolver problemas sobre SAML SSO con el Soporte de forma más eficiente.
 
#### Centros de datos específicos para cada región
Como Braze está creciendo para dar servicio a nuevas áreas, hemos añadido un [artículo sobre los centros de datos Braze]({{site.baseurl}}/user_guide/data/data_centers) para aclarar nuestro enfoque operativo.
 
### Desbloquear la creatividad
 
#### Notificaciones de bajada de precios y de reposición de existencias

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Ahora puedes avisar a los clientes cuando un artículo vuelva a estar disponible configurando [notificaciones de reposición de existencias]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications) a través de un Canvas y un catálogo.

También puedes crear [notificaciones de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications) bajada de precios para avisar a los clientes cuando el precio de un artículo ha bajado configurando notificaciones de bajada de precios en un catálogo y en Canvas.

#### Vista previa para la selección 

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Después de crear una [selección]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview), puedes [ver lo que devolvería una selección]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview) para un usuario aleatorio o para un usuario concreto.

#### Elementos del catálogo de plantillas, incluido Liquid 

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Puedes [hacer plantillas de artículos del catálogo que incluyan Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid).

#### Plantillas de Canvas
Hemos añadido nuevas plantillas Canvas para la [incorporación de usuarios con un cuestionario de preferencias]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey) y para [crear un registro por correo electrónico con doble adhesión voluntaria]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup).

#### Gestión de clientes potenciales con Salesforce Sales Cloud para B2B
Una forma en que los especialistas en marketing B2B pueden utilizar Braze es mediante una integración con Salesforce Sales Cloud. Lee más sobre cómo poner en práctica este [caso de uso]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud).
 
### Canales robustos

#### Listas de supresión

{% multi_lang_include release_type.md release="Beta" %}
 
[Las listas de supresión]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) especifican grupos de usuarios que nunca recibirán mensajes. Los administradores pueden crear listas de supresión con filtros de segmento para acotar un grupo de usuarios del mismo modo que lo harías para la segmentación.

### Nuevas asociaciones Braze

#### Constructor - Contenido dinámico
[Constructor]({{site.baseurl}}/partners/message_personalization/dynamic_content/constructor) es una plataforma de búsqueda y descubrimiento de productos que utiliza IA y aprendizaje automático para entregar experiencias personalizadas de búsqueda, recomendación y navegación para sitios web de comercio minorista y comercio electrónico.
 
#### Trustpilot - Contenido dinámico
[Trustpilot]({{site.baseurl}}/partners/message_personalization/dynamic_content/trustpilot) es una plataforma de opiniones en línea que habilita a tus clientes a compartir opiniones y te permite administrar y responder a las opiniones.

### Actualizaciones del SDK
 
Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.
 
- [SDK para Android de Braze 34.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3400)
    - Actualizada la versión mínima del SDK de 21 (Lollipop) a 25 (Nougat).

## Lanzamiento el 7 de enero de 2025

### Desbloquear la creatividad

#### Plantillas de mensajes dentro de la aplicación

Hemos añadido [plantillas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/) para arrastrar y soltar mensajes dentro de la aplicación.

#### B2B Salesforce Sales Cloud gestión de clientes potenciales

La [gestión de clientes potenciales con Salesforce]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud/) Sales Cloud muestra cómo utilizar webhooks Braze para crear y actualizar clientes potenciales en Salesforce Sales Cloud mediante una integración enviada por la comunidad.

### Canales robustos

#### Plantillas de Canvas

Hemos añadido plantillas Braze Canvas para [el registro por correo electrónico con doble adhesión voluntaria]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup/) y [la incorporación con un cuestionario de preferencias]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey/).

#### Cambios en la política de adhesión voluntaria de WhatsApp

Meta ha actualizado recientemente su [política de adhesión voluntaria](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Para más información, consulta [las actualizaciones de productos WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/).

#### Herramienta de anchura para bloques de contenido en el editor de arrastrar y soltar de correo electrónico

Puedes [ajustar la anchura]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) de tu bloque de contenido en el editor de arrastrar y soltar de correo electrónico. La anchura predeterminada es 100%.

### Flexibilidad de los datos

#### Filtro de segmentos con rebote blando

Segmenta a tus usuarios en función de si han rebotado blando X veces en Y días. Para más información, consulta el [glosario Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced).

#### Resumen de usuarios anónimos

[Usuarios anónimos]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) ofrece un resumen de los usuarios anónimos y los alias de usuario, destacando su importancia y cómo pueden aprovecharse en tus mensajes.

#### Pertenencia al grupo de control global

Puedes [ver la pertenencia al grupo de control global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#view-whether-a-user-is-in-a-global-control-group) yendo a la pestaña **"Interacción"** del perfil de un usuario individual y desplazándote hasta la sección **"Varios"**.

### Nuevas asociaciones Braze

#### Justuno - Captación de clientes potenciales

[Justuno]({{site.baseurl}}/partners/data_and_infrastructure_agility/leads_capture/justuno/) te permite crear experiencias de visita totalmente optimizadas para todas tus audiencias con segmentos dinámicos, ofreciendo la segmentación más avanzada disponible, todo ello sin afectar a la velocidad del sitio ni aumentar el trabajo de desarrollo.

#### Odicci - Plataforma de datos de los clientes

Integra Braze con [Odicci]({{site.baseurl}}/partners/message_personalization/dynamic_content/odicci/), una plataforma que permite a las empresas captar, fidelizar y retener a sus clientes mediante experiencias omnicanales basadas en la fidelización.

#### Optimizely - Pruebas A/B

La integración de Braze y [Optimizely]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/optimizely/) es una integración bidireccional que te permite:

- Sincroniza tus segmentos y eventos de clientes Braze con la Plataforma de Datos Optimizely (ODP) cada noche para enriquecer los perfiles, informes y segmentación de clientes Optimizely.
- Envía eventos de Braze Currents desde Braze a la herramienta de informes de Optimizely.
- Sincroniza datos de clientes y eventos ODP con Braze para enriquecer tus datos de clientes Braze y desencadenar mensajería Braze basada en eventos de clientes en ODP.

## Liberación el 10 de diciembre de 2024

### Ubicación del usuario del SDK por dirección IP

A partir del 26 de noviembre de 2024, Braze detectará la ubicación de los usuarios desde el país geolocalizado utilizando la dirección IP desde el inicio de la primera sesión del SDK. Braze utilizará la dirección IP para establecer el valor del país en los perfiles de usuario que se creen a través del SDK, y esa configuración del país basada en la IP estará disponible durante y después de la primera sesión. Consulta [Seguimiento de ubicación]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/) para más detalles.

### Configuración de Acceso Elevado

[El Acceso Elevado]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#elevated-access) añade una capa extra de seguridad para las acciones sensibles en tu panel Braze. Cuando están activos, los usuarios tienen que volver a verificar su cuenta antes de exportar un segmento o ver una clave de API. Para utilizar el Acceso Elevado, ve a **Configuración** > **Configuración de administrador** > **Configuración de seguridad** y altérnalo.

### Permiso para ver información de identificación personal (PII)

Para los administradores, puedes [permitir que los usuarios vean la PII]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) definida por tu empresa en el panel en vistas previas de mensajes que utilizan variables Liquid para acceder a las propiedades de los usuarios. 

Para los espacios de trabajo, puedes permitir que los usuarios vean la PII definida por tu empresa en el panel, o ver los perfiles de usuario pero redactando los campos que tu empresa haya identificado como PII.

### Flexibilidad de los datos

#### Esquemas de lago de datos

Se han añadido los siguientes esquemas a los esquemas de tablas sin procesar:
- `USERS_CANVASSTEP_PROGRESSION_SHARED`: Eventos de progresión de un usuario en un Canvas
- `CHANGELOGS_GLOBALCONTROLGROUP_SHARED`: Identificar qué números de contenedor aleatorios hay en el grupo de control global actual y en el anterior
- `USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED`: Eventos de impresión para cuando un usuario ve una bandera de característica

#### Segmentación basada en cuentas

Puedes hacer [la segmentación basada en cuentas de empresa a empresa (B2B]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/account_based_segmentation/) ) de dos formas, dependiendo de cómo configures tu modelo de datos B2B:

- Cuando utilices catálogos para tus objetos de negocio
- Cuando utilices fuentes conectadas para tus objetos de negocio

#### Filtros de segmentación

Consulta [Filtros de segmentación]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) para ver la lista completa de filtros de segmentación y sus descripciones.

##### Perfil de usuario creado en

Segmenta a tus usuarios en función de cuándo se creó su perfil de usuario. Si un usuario se añadió por CSV o API, este filtro refleja la fecha en que se añadió. Si el usuario no está añadido por CSV o API y tiene su primera sesión seguida por el SDK, entonces este filtro refleja la fecha de esa primera sesión.

##### Envío del número de teléfono

Segmenta a tus usuarios por el campo de número de teléfono e.164. Puedes utilizar expresiones regulares con este filtro para segmentar por números de teléfono con un código de país concreto.

### Nuevas asociaciones Braze

#### Narvar - Comercio electrónico

La integración de Braze y [Narvar](https://corp.narvar.com/) habilita a las marcas a aprovechar los eventos de notificación de Narvar para desencadenar mensajes directamente desde Braze, manteniendo a los clientes informados con actualizaciones puntuales.

#### Zeotap para Currents - Plataforma de datos de los clientes

La integración de Braze y [Zeotap](https://zeotap.com/) te permite ampliar la escala y el alcance de tus campañas sincronizando los segmentos de clientes de Zeotap con los perfiles de usuario de Braze. Con [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), también puedes conectar los datos a Zeotap para que sean procesables en todo el stack de crecimiento.

#### Notificar - Contenido dinámico

La integración de Braze y [Notify](https://notifyai.io/) permite a los especialistas en marketing impulsar eficazmente la interacción en varias plataformas. En lugar de depender de los métodos de marketing tradicionales, una campaña desencadenada por la API de Braze puede aprovechar las capacidades de Notify para entregar mensajes personalizados a través de múltiples canales, como correo electrónico, SMS, notificaciones push, etc.

#### Contentful - Contenido dinámico

La integración de Braze y [Contentful](https://www.contentful.com/) te permite utilizar dinámicamente el contenido conectado para extraer contenido de Contentful en tus campañas Braze.

#### Outgrow - Captación de clientes potenciales 

La integración de Braze y [Outgrow](https://outgrow.co/) te permite transferir automáticamente los datos de usuario de Outgrow a Braze, habilitando campañas altamente personalizadas y dirigidas.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK Web 5.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [SDK de Flutter 12.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/12.0.0)
    - Actualiza el puente nativo de iOS [de Braze Swift SDK 10.3.1 a 11.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.1...11.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Actualiza el puente nativo de Android [de Braze Android SDK 32.1.0 a 33.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v33.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [SDK de Swift 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/11.0.1/CHANGELOG.md)

## Liberación el 12 de noviembre de 2024
 
### Flexibilidad de los datos
 
#### Límite de velocidad para `/users/track`

El límite de velocidad para el [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) se ha actualizado a 3.000 cada 3 segundos.
 
### Desbloquear la creatividad

#### Casos de uso de Canvas

Hemos reunido algunos casos de uso que muestran las distintas formas en que puedes aprovechar un Canvas de Braze. Si buscas inspiración, elige un caso de uso a continuación para empezar.

- [Carrito abandonado]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [De nuevo en stock]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [Adopción de características]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [Usuario caducado]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [Incorporación]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [Comentarios posteriores a la compra]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### Canales robustos

#### LINE

{% multi_lang_include release_type.md release="Disponibilidad general" %}

¡La integración con LINE de Braze ya está disponible! LINE es la aplicación de mensajería más popular de Japón, con más de 95 millones de usuarios activos al mes. Además de mensajería, LINE ofrece a sus usuarios una plataforma "todo en uno" para redes sociales, juegos, compras y pagos.

Para empezar, consulta nuestra [documentación sobre LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/).
 
#### Sincronización de audiencias de LinkedIn

{% multi_lang_include release_type.md release="Beta" %}

Ahora puedes utilizar LinkedIn con [Braze Audience Sync]({{site.baseurl}}/partners/canvas_steps/), una herramienta que te ayuda a ampliar el alcance de tus campañas a muchas de las principales tecnologías sociales y publicitarias. Para unirte a la beta, ponte en contacto con tu administrador de éxito de Braze.
 
### Mejorar la guía del desarrollador
 
Estamos realizando importantes mejoras en la [Guía del desarrollador de Braze]({{site.baseurl}}/developer_guide/home/). Como primer paso, simplificamos la navegación y redujimos el número de secciones anidadas. 

|Antes de|Después de|
|------|-----|
|!["La antigua navegación de la Guía del Desarrollador de Braze"]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["La nueva navegación de la Guía del Desarrollador de Braze"]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### Nuevas asociaciones Braze
 
#### MyPostcard

[MyPostcard](https://www.mypostcard.com/), una aplicación de postales líder en el mundo, te permite realizar campañas de correo directo con facilidad, proporcionándote una forma sencilla y rentable de conectar con tus clientes. Para empezar, consulta [Integrar MyPostcard con Braze]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/).
 
### Actualizaciones del SDK
 
Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.
 
- [Plugin Expo 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - Esta versión requiere la versión 13.1.0 del SDK Braze React Native.
    - Sustituye la llamada al método BrazeAppDelegate de iOS de BrazeReactUtils.populateInitialUrl por BrazeReactUtils.populateInitialPayload.
        - Esta actualización resuelve un problema por el que los eventos abiertos push no se desencadenaban al hacer clic en una notificación mientras la aplicación estaba en estado finalizado.
        - Para aprovechar al máximo esta actualización, sustituye todas las llamadas a Braze.getInitialURL por Braze.getInitialPushPayload en tu código JavaScript. Ahora se puede acceder a la URL inicial a través de la propiedad url de la carga útil push inicial.
- [Plugin Swift de segmentos Braze 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Actualiza los enlaces del SDK Swift de Braze para que requieran versiones de la denominación SemVer 11.1.1+.
    - Esto permite la compatibilidad con cualquier versión del SDK de Braze desde la 11.1.1 hasta la 12.0.0, pero sin incluirla.
    - Consulta la entrada del registro de cambios de la 11.1.1 para obtener más información sobre posibles cambios de última hora.

## Liberación el 15 de octubre de 2024

### Flexibilidad de los datos

#### Campañas y Canvas

Al crear campañas y Lienzos, puedes calcular el número exacto de usuarios alcanzables de tu audiencia objetivo en lugar de la estimación predeterminada, seleccionando [Calcular estadísticas exactas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size).

#### API Objetos Android

El [parámetro`android_priority` ]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details) aceptará los valores "normal" o "alto" para especificar la prioridad del remitente del FCM. Por predeterminado, los mensajes de notificación se envían con prioridad alta, y los mensajes de datos con prioridad normal.

Para más información sobre cómo afectan los distintos valores a la entrega, consulta [Prioridad de mensajes en Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority/).

#### SDK

Utiliza [el depurador integrado del SDK de Braze]({{site.baseurl}}/developer_guide/debugging/) para solucionar problemas de tus canales con SDK sin necesidad de habilitar el registro detallado en tu aplicación.

#### Actividades en vivo

Hemos actualizado las [preguntas más frecuentes]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/) sobre las Actividades en vivo de Swift con algunas preguntas y respuestas nuevas.

#### Eventos personalizados

[Los objetos de propiedades del]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) evento que contienen valores de matrices u objetos ahora pueden tener una carga útil de propiedades del evento de hasta 100 KB.

#### Números de contenedor aleatorio

Utiliza [la reentrada aleatoria de audiencia con números de contenedor aleatorios]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers) para las pruebas A/B o para dirigirte a grupos de usuarios específicos en tus campañas.

#### Extensiones de segmento

Puedes [actualizar las extensiones de segmento de forma periódica]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh) seleccionando la frecuencia con la que se actualizarán las extensiones (diaria, semanal o mensualmente) y la hora concreta en la que se producirá la actualización.

### Canales robustos

#### SMS

Hemos añadido [Añadir parámetros UTM]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening) para demostrar cómo puedes utilizar parámetros UTM en un mensaje SMS, de modo que puedas hacer un seguimiento del rendimiento de las campañas en herramientas de análisis de terceros, como Google Analytics.

#### Páginas de destino

[Conecta tu propio dominio]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/customizing_urls/) a tu espacio de trabajo Braze para personalizar las URL de tus páginas de destino con tu marca.

#### LÍNEA y Braze

{% multi_lang_include release_type.md release="Beta" %}

Hemos añadido nueva documentación:

- [Tipos de mensajes de LINE]({{site.baseurl}}/line/create/message_types/) cubre los tipos de mensajes de LINE que puedes componer, incluyendo aspectos y limitaciones, y forma parte de la colección beta de LINE.
- [La vinculación de cuentas de usuario]({{site.baseurl}}/line/line_setup/#user-account-linking) permite a los usuarios vincular su cuenta de LINE a la cuenta de usuario de tu aplicación. A continuación, puedes utilizar Liquid en Braze, como {% raw %}`{{line_id}}`{% endraw %}, para crear una URL personalizada para el usuario que devuelva el ID de LINE del usuario a tu sitio web o aplicación, que podrá asociarse a un usuario conocido.

#### WhatsApp y Braze

[Las cuentas de WhatsApp Business (WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) ahora pueden compartirse con varios proveedores de soluciones empresariales.

### Nuevas asociaciones Braze

#### Himno del Futuro - Contenido dinámico

La asociación entre Braze y [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) aprovecha la IA del Amplificador para entregar personalización de contenidos, experiencias en tiempo real y audiencias dinámicas. El Amplificador de IA funciona en deportes, casinos y loterías, permitiéndote mejorar los perfiles de jugador de Braze con atributos de jugador específicos del sector, como juego favorito, puntuación de interacción, próxima apuesta prevista y mucho más.

### Configuración

#### Cifrado a nivel de campo del identificador

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Mediante el [cifrado a nivel de campo identificador]({{site.baseurl}}/user_guide/analytics/field_level_encryption/), puedes cifrar fácilmente las direcciones de correo electrónico con el servicio de administración de claves (KMS) de AWS para minimizar la información de identificación personal (PII) compartida en Braze. La encriptación sustituye los datos sensibles por texto cifrado, que es información encriptada ilegible.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de Swift 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [SDK de Swift 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - Añade compatibilidad con [la comprobación de concurrencia estricta de Swift 6](https://developer.apple.com/documentation/swift/adoptingswift6)
        - Las clases y tipos de datos públicos relevantes de Braze se ajustan ahora al protocolo `Sendable` y pueden utilizarse con seguridad en contextos de concurrencia.
        - Las API de sólo hilo principal ahora están marcadas con el atributo `@MainActor`.
        - Recomendamos utilizar Xcode 16.0 o posterior para aprovechar estas características y minimizar al mismo tiempo el número de advertencias generadas por el compilador. Las versiones anteriores de Xcode pueden seguir utilizándose, pero algunas características pueden generar advertencias.
    - Al integrar manualmente la compatibilidad con las notificaciones push, puede que tengas que actualizar la conformidad de `UNUserNotificationCenterDelegate` para utilizar el atributo `@preconcurrency` y evitar advertencias.
        - La aplicación del atributo `@preconcurrency` a la conformidad del protocolo sólo está disponible en Xcode 16.0 o posterior. Consulta [aquí](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual) nuestro código de integración de muestra.
- [SDK de React Native 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - Actualiza los enlaces de la versión nativa de Android de [Braze Android SDK 31.1.0 a 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualiza los enlaces de la versión nativa de iOS de [Braze Swift SDK 10.3.0 a 11.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK de Flutter 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [SDK de Swift 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Android SDK 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Actualizado Kotlin de 1.8 a Kotlin 2.0.
- [SDK Web 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## Liberación el 17 de septiembre de 2024

### Flexibilidad de los datos

#### Ingesta de datos en la nube Braze para S3

Puedes utilizar [Cloud Data Ingestion (CDI) para S3]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) para integrar directamente uno o varios contenedores de S3 de tu cuenta de AWS con Braze. Cuando se publican nuevos archivos en S3, se envía un mensaje a SQS, y la ingesta de datos en la nube de Braze recoge esos nuevos archivos.

#### Usuarios activos al mes CY 24-25

Para los clientes que hayan comprado Usuarios activos al mes - CY 24-25, Braze gestiona diferentes límites de velocidad en su punto final `/users/track`. Para más detalles, consulta [POST: Seguimiento de usuarios]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### Desbloquear la creatividad

#### Elementos del catálogo de plantillas, incluido Liquid

{% multi_lang_include release_type.md release="Acceso anticipado" %}

Utiliza la bandera `:rerender` en una etiqueta de Liquid para [mostrar el contenido Liquid de un elemento del catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid). Por ejemplo, si generas el siguiente contenido Liquid:

{% raw %}
```liquid
Hi ${first_name}
{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

Aparecerá lo siguiente:

{% raw %}
```
Hi Peter,
Welcome to our store, Peter!
```
{% endraw %}

### Canales robustos

#### Mensajes de respuesta de WhatsApp

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Puedes utilizar [mensajes de respuesta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) para responder a los mensajes entrantes de WhatsApp de tus usuarios. Estos mensajes se crean in-app en Braze durante tu experiencia de composición y pueden editarse en cualquier momento. Puede utilizar Liquid para adaptar el idioma de los mensajes de respuesta a los usuarios adecuados.

#### Plantillas de Canvas

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Crea [plantillas de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/) para perfeccionar tu mensajería creando un marco coherente que pueda personalizarse fácilmente para adaptarse a tus objetivos específicos en todos tus Canvases.

#### Páginas de destino

{% multi_lang_include release_type.md release="Beta" %}

[Las páginas de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages) Braze son páginas web independientes que pueden impulsar tu estrategia de captación e interacción de usuarios.

#### Cambios desde la última visita

Puedes ver el número de actualizaciones de tus [Lienzos]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), campañas y [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed) realizadas por otros miembros de tu equipo consultando la métrica *Cambios desde la última vez que los viste* en las respectivas páginas de resumen (como la página de resumen de una [campaña por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)). 

#### Solución de problemas de webhook y solicitudes de contenido conectado 

[Este artículo]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors) explica cómo solucionar los códigos de error de webhook y Contenido conectado, incluyendo cuáles son los errores y los pasos para resolverlos.

### Nuevas asociaciones Braze

#### Inbox Monster - Análisis

[Inbox Monster]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) es una plataforma de señales de buzón de entrada que ayuda a las marcas empresariales a aterrizar cada envío. Es una línea integrada de soluciones de capacidad de entrega, renderización creativa y monitorización de SMS, que capacita a los equipos modernos de administración de las relaciones con el cliente (CRM) y acaba con los sustos de los envíos.

#### SesiónM - Fidelización

[SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) es una plataforma de interacción con los clientes y fidelización que proporciona características de gestión de campañas y soluciones de gestión de la fidelización para ayudar a los especialistas en marketing a impulsar el alcance específico para aumentar la interacción y la ganancia.

### Automatización de IA y ML

#### Recomendaciones de artículos de moda

Además del modelo "AI Personalizado", la característica de [recomendaciones de artículos AI]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) también incluye un modelo de recomendación de "Tendencias", que presenta los artículos que tuvieron el impulso más positivo en lo que respecta a las interacciones recientes de los usuarios.

### Configuración

#### Roles

{% multi_lang_include release_type.md release="Disponibilidad general" %}

[Los roles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) permiten una mayor estructuración al agrupar tus permisos personalizados individuales con controles de acceso al espacio de trabajo. Esto es especialmente útil si tiene muchas marcas o espacios de trabajo regionales en un mismo cuadro de mandos. Con las funciones, puede añadir usuarios del cuadro de mandos a los espacios de trabajo adecuados y concederles directamente los permisos asociados. 

#### Informe de sucesos de seguridad

Hemos añadido una lista completa de los [eventos de seguridad]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report) que pueden aparecer en tu evento de informe de seguridad descargado.

#### Informe de uso de mensajes

{% multi_lang_include release_type.md release="Acceso anticipado" %}

El [panel de uso de mensajes]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/message_usage/) proporciona información de autoservicio sobre tu uso de crédito de SMS y WhatsApp para obtener una visión completa del uso histórico y actual comparado con las asignaciones del contrato. Esta información puede reducir tu confusión y ayudarte a hacer ajustes para evitar riesgos de excedente.

### SDK

#### Inicialización retardada para el SDK Swift de Braze

Configura [la inicialización retardada]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift) para inicializar tu SDK Braze Swift de forma asíncrona, garantizando al mismo tiempo que se conserva la gestión de las notificaciones push. Esto puede ser útil cuando necesites configurar otros servicios antes de inicializar el SDK, como obtener datos de configuración de un servidor o esperar el consentimiento del usuario.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Android SDK 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [Segmento Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [SDK de Swift 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [SDK de React Native 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova SDK 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - Esta versión ahora requiere Cordova Android 13.0.0.
    - Consulta el [anuncio de lanzamiento de Cordova](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html) para obtener una lista completa de los requisitos de dependencia del proyecto.- Actualizado el puente nativo de Android [de Braze Android SDK 30.3.0 a 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el puente nativo de iOS [de Braze Swift SDK 9.2.0 a 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK de Swift 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - Actualizado el puente nativo de Android [de Braze Android SDK 30.3.0 a 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el puente nativo de iOS [de Braze Swift SDK 9.0.0 a 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Plugin Swift de segmentos Braze 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - Actualiza los enlaces del SDK Swift de Braze para que requieran versiones de la denominación `10.2.0+` SemVer.
        - Esto permite la compatibilidad con cualquier versión del SDK de Braze desde `10.2.0` hasta, pero sin incluir, `11.0.0`.
        - Consulta la entrada del registro de cambios de [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000) para obtener más información sobre posibles cambios de última hora.
- [SDK de Flutter 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - Actualiza el puente nativo de Android [de Braze Android SDK 30.4.0 a 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Cambia el comportamiento de `wipeData()` en Android para que conserve las suscripciones externas (como `subscribeToContentCards()`) después de ser llamado.
    - Actualiza el puente nativo de iOS [de Braze Swift SDK 9.0.0 a 10.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK de Swift 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [SDK de React Native 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)
