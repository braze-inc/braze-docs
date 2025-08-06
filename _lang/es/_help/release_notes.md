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

> Braze publica información sobre las actualizaciones del producto con una cadencia mensual, en consonancia con las principales versiones del producto, aunque el producto se actualiza con mejoras varias semana a semana.<br><br>Para obtener más información sobre cualquiera de las actualizaciones enumeradas en esta sección, ponte en contacto con tu director de cuentas o [abre un ticket de soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). También puedes consultar [nuestros registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs) para ver más información sobre nuestros lanzamientos, actualizaciones y mejoras mensuales del SDK.

## Lanzamiento el 24 de junio de 2025

### OfferFit de Braze

[OfferFit](https://www.offerfit.ai/) sustituye las pruebas A/B por la toma de decisiones con IA que lo personaliza todo y maximiza cualquier métrica: impulsa los dólares, no los clics: con OfferFit, puedes optimizar cualquier KPI empresarial. Consulta nuestra sección dedicada [OfferFit by Braze]({{site.baseurl}}/user_guide/offerfit) para ver ejemplos de casos de uso y características clave.

### Nuevos tutoriales del SDK

Cada tutorial del SDK de Braze ofrece instrucciones paso a paso junto con un código de muestra completo. Elige un tutorial a continuación para empezar:

- [Mostrar pancartas]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Personalización del estilo de los mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [Visualización condicional de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [Aplazar mensajes desencadenados dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### Flexibilidad de los datos

#### Aprovisionamiento justo a tiempo SAML

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Utiliza [el aprovisionamiento justo a tiempo SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit) para permitir que los nuevos usuarios del panel creen una cuenta Braze en su primer inicio de sesión. Esto elimina la necesidad de que los administradores creen manualmente una cuenta para un nuevo usuario del cuadro de mandos, elijan sus permisos, lo asignen a un espacio de trabajo y esperen a que active su cuenta.

#### Filtros por selección

Ahora puedes añadir hasta 10 filtros por [selección]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections).

#### Almacenamiento de catálogos

El tamaño de almacenamiento para la versión gratuita de [los catálogos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#catalog-storage) es de hasta 100 MB. Puedes tener un número ilimitado de objetos, siempre que no superen los 100 MB.

#### Número de filas sincronizadas con la ingesta de datos en la nube

Por defecto, para la Ingesta de datos en la nube, cada ejecución puede sincronizar hasta 500 millones de filas. Se detendrá cualquier sincronización con más de 500 millones de filas nuevas.

Consulta las [limitaciones del producto Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/#product-limitations) para más detalles.

### Canales robustos

#### Pruebas de accesibilidad en Inbox Vision

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Utiliza [las pruebas de accesibilidad]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) de Inbox Vision para resaltar los problemas de accesibilidad que puedan existir en tu correo electrónico. 

Las pruebas de accesibilidad analizan el contenido de tu correo electrónico en función de algunos requisitos de [las Pautas de Accesibilidad al Contenido en la Web](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA. Esto puede proporcionar información sobre qué elementos no cumplen las normas de accesibilidad.

#### Seguimiento de clics para WhatsApp

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Puedes activar [el seguimiento de clics]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking) tanto en los mensajes de respuesta como en los de plantilla para ver los datos de clics en tus informes de rendimiento de WhatsApp y poder segmentar a los usuarios en función de quién hizo clic en qué.

#### Vídeos para WhatsApp

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Puedes [incrustar videos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features) en el cuerpo del texto de los mensajes salientes de WhatsApp. Estos archivos deben estar alojados a través de URL o en la [biblioteca multimedia de Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library).

### Nuevas asociaciones Braze

#### Stripe - Comercio electrónico

La interacción entre Braze y [Stripe]({{site.baseurl}}/partners/stripe) te permite desencadenar mensajería en Braze basada en eventos de Stripe, como inicio de prueba, suscripción activada, cancelación de suscripción, etc.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de React Native 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [SDK de Flutter 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - Actualizado el puente nativo de Android [de Braze Android SDK 35.0.0 a 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el puente nativo de iOS [de Braze Swift SDK 11.6.1 a 12.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Segmento Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Actualizado el SDK para Android de Braze [de 35.0.0 a 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

## Comunicado de 27 de mayo de 2025

### Flexibilidad de los datos

#### Copiar lienzos en distintos espacios de trabajo

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Ahora puedes copiar Lienzos entre espacios de trabajo. Esto te permite poner en marcha la composición de tu mensaje empezando con una copia de un Canvas en un espacio de trabajo diferente. Para más información sobre lo que se copia, consulta [Copiar campañas y lienzos entre espacios de trabajo]({{site.baseurl}}/copying_to_workspaces/).

#### Reglas de mensajería para el flujo de trabajo de aprobación 

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Utiliza [reglas de mensajería]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules) en tu flujo de trabajo de aprobación para limitar el número de usuarios alcanzables antes de que se requiera una aprobación adicional; de este modo, puedes revisar tus campañas y Canvases antes de dirigirte a una audiencia mayor.

#### Diagramas de relación de entidades para Snowflake y Braze

A principios de este año, creamos tablas de relaciones de entidades para los datos compartidos entre Snowflake y Braze. Este mes, hemos añadido [nuevos diagramas interactivos]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/) en los que puedes desplazarte, agarrar y hacer zoom en los detalles de cada tabla, dándote una mejor idea de cómo interactúan tus datos con Braze.

### Desbloquear la creatividad

#### Eventos recomendados

{% multi_lang_include release_type.md release="Acceso anticipado" %}

[Los eventos recomendados]({{site.baseurl}}/user_guide/data/custom_data/recommended_events) se corresponden con los casos de uso más comunes del comercio electrónico. Al utilizar eventos recomendados, puedes desbloquear plantillas Canvas prediseñadas, paneles de informes mapeados según el ciclo de vida del cliente y mucho más.

### Canales robustos

#### Canal de pancartas

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Con [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners), puedes crear mensajes personalizados para tus usuarios, a la vez que amplías el alcance de tus otros canales, como el correo electrónico o las notificaciones push. Puedes incrustar banners directamente en tu aplicación o sitio web, lo que te permite interactuar con los usuarios a través de una experiencia natural.

#### Canal de Servicios de Comunicación Enriquecidos (RCS)

{% multi_lang_include release_type.md release="Disponibilidad general" %}

[Los Servicios de Comunicación Enriquecidos (RCS)]({{site.baseurl}}/about_rcs/) mejoran los SMS tradicionales, habilitando a las marcas para entregar mensajes no sólo informativos, sino también mucho más interactivos. Ahora compatible tanto con Android como con iOS, RCS aporta características como medios de alta calidad, botones interactivos y perfiles de remitente de marca directamente en las aplicaciones de mensajería preinstaladas de los usuarios, eliminando la necesidad de descargar una aplicación aparte.

#### Página de configuración push

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Utiliza [la página de**Configuración push**]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings) para configurar los ajustes clave de tus notificaciones push, incluido el Tiempo de vida push (TTL) y la prioridad predeterminada del FCM para las campañas de Android. Estas configuraciones ayudan a optimizar la entrega y la eficacia de tus notificaciones push, garantizando una mejor experiencia a tus usuarios.

#### Códigos promocionales para campañas de mensajes dentro de la aplicación

{% multi_lang_include release_type.md release="Acceso anticipado" %}

Puedes utilizar [códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) en campañas de mensajería dentro de la aplicación insertando un [fragmento de lista de códigos promocionales]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) en el cuerpo del mensaje de tu campaña de mensajería dentro de la aplicación.

#### Gestión de errores de webhook y límite de velocidad

[Acerca de los webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#webhook-error-handling-and-rate-limiting) tiene una nueva sección que describe cómo gestiona Braze los errores de los webhooks y el límite de tasa.

#### Mensajes dentro de la aplicación locales

Tras [añadir localizaciones]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/using_locales) a tu espacio de trabajo, puedes dirigirte a usuarios en distintos idiomas con un solo mensaje dentro de la aplicación.

#### Amazon SES como proveedor de envío por correo electrónico (ESP)

Ahora puedes utilizar Amazon SES como ESP, de forma similar a como utilizarías SendGrid y SparkPost. Consulta [SSL en Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it) y [Enlaces universales y enlaces de aplicaciones]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) para conocer los matices de la configuración de SSL y el seguimiento de clics enlace a enlace.

### Nuevas asociaciones Braze

#### Ojo de Águila - Fidelización

La integración bidireccional de Braze y [Eagle]({{site.baseurl}}/partners/eagle_eye/) Eye te permite activar datos de fidelización y promocionales directamente en Braze, lo que permite a los especialistas en marketing personalizar la interacción con los clientes utilizando datos en tiempo real, como saldos de puntos, promociones y actividades de recompensa.

#### Eppo - Pruebas A/B

La integración de Braze y [Eppo]({{site.baseurl}}/partners/eppo/) te permite configurar pruebas A/B en Braze y analizar los resultados en Eppo para descubrir información y vincular el rendimiento de los mensajes a métricas empresariales a largo plazo, como los ingresos o la retención.

#### Mencióname - Referidos

Juntos, [Mention Me](https://www.mention-me.com/) y Braze pueden ser tu puerta de entrada para atraer a clientes premium y fomentar una fidelización inquebrantable a la marca. Al integrar fácilmente datos propios de referidos en Braze, puedes entregar experiencias omnicanal altamente personalizadas dirigidas a los fans de tu marca. Para empezar, consulta [Socios tecnológicos: Mencióname]({{site.baseurl}}/partners/mention_me).

#### Shopify - Comercio electrónico

[Conecta varios dominios de tiendas Shopify]({{site.baseurl}}/shopify_connecting_multiple_stores/) a un único espacio de trabajo para tener una visión holística de tus clientes en todos los mercados. Construye y lanza programas y viajes de automatización en un único espacio de trabajo sin duplicar esfuerzos en las tiendas regionales.

### Otro

#### Actualización para Construir mensajes accesibles en Braze

Hemos actualizado nuestro artículo [Crear mensajes accesibles en Braze]({{site.baseurl}}/help/accessibility/) con orientaciones más claras y prescriptivas sobre la creación de mensajes accesibles. Este artículo incluye ahora prácticas recomendadas ampliadas para la estructura del contenido, el texto alternativo, los botones y el contraste de colores, junto con una nueva sección sobre la gestión de ARIA para mensajes HTML personalizados. 

Esta actualización forma parte de nuestro esfuerzo más amplio por dar soporte a experiencias de mensajería más accesibles en Braze. Sabemos que la accesibilidad es un área en evolución, y seguiremos compartiendo lo que aprendamos.

{% multi_lang_include accessibility/feedback.md %}

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Android SDK 36.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Esta versión revierte el aumento de la versión mínima del SDK de Android de Braze de la API 21 a la API 25 introducido en la versión 34.0.0. Esto permite volver a compilar el SDK en aplicaciones compatibles con la API 21. Ten en cuenta que, aunque estamos reintroduciendo la capacidad de compilar, no estamos reintroduciendo la compatibilidad formal con < API 25, y no podemos garantizar que el SDK funcione según lo previsto en dispositivos que ejecuten esas versiones.
    - Si tu aplicación es compatible con esas versiones, deberías hacerlo:
        - Valida que tu integración del SDK funciona según lo previsto en dispositivos físicos (no sólo emuladores) para esas versiones de la API.
        - Si no puedes validar el comportamiento esperado, debes llamar a [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) o no inicializar el SDK en esas versiones. De lo contrario, podrías causar efectos secundarios no deseados o degradar el rendimiento de los dispositivos de tus usuarios finales.
    - Se ha solucionado un problema por el que los mensajes dentro de la aplicación provocaban una lectura en el hilo principal.
    `BrazeInAppMessageManager.displayInAppMessage` es ahora una función de suspensión de Kotlin.
        - Si no llamas directamente a esta función, no necesitas hacer ningún cambio.
    - Lista de materiales de AndroidX Compose actualizada a 2025.04.01 para gestionar las actualizaciones de las API de Jetpack Compose.
- [SDK de React Native 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Actualiza el puente nativo de Android de Braze Android SDK 35.0.0 a 36.0.0.
    - Actualiza los enlaces de la versión nativa de iOS de Braze Swift SDK 11.9.0 a 12.0.0.
    - Actualiza la representación unitaria de PushNotificationEvent.timestamp a milisegundos en iOS.
        - Antes, este valor se representaba en segundos en iOS. Ahora coincidirá con la implementación existente de Android.
- [SDK Web 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - Esta versión revierte el aumento de la versión mínima del SDK de Android de Braze de la API 21 a la API 25 introducido en la versión 34.0.0. Esto permite volver a compilar el SDK en aplicaciones compatibles con la API 21. Sin embargo, no vamos a reintroducir la compatibilidad formal con < API 25. Lee más [aquí](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600).
    - Actualiza el puente nativo de Android de Braze Android SDK 35.0.0 a 36.0.0.
    - Actualiza el puente nativo de iOS de Braze Swift SDK 11.9.0 a 12.0.0.

## Lanzamiento el 29 de abril de 2025

### Solución de problemas de acceso Braze

[La solución de problemas de acceso a Braze]({{site.baseurl}}/user_guide/administrative/access_braze/troubleshooting/) te ayuda a resolver los problemas que puedas tener al intentar acceder a Braze, como quedar bloqueado en tu cuenta o trabajar con un panel de Braze que no rinde como esperabas.

### Flexibilidad de los datos

#### Preguntas frecuentes sobre Currents

Puedes encontrar respuestas a algunas preguntas frecuentes sobre Currents en la nueva página [Preguntas frecuentes]({{site.baseurl}}/user_guide/data/braze_currents/faq/).

#### Usuarios anónimos

Consulta las siguientes secciones en [Usuarios anónimos]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) para obtener nuevos detalles sobre cómo funcionan los usuarios anónimos y por qué te puede interesar asignarles alias de usuario:
- [Cómo funciona]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#how-it-works) 
- [Asignar alias de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#assigning-user-aliases)

#### Borradores de campaña

[Guardar borradores]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#campaign-drafts) puede ayudarte a realizar cambios a gran escala en las campañas activas. Al crear un borrador, puedes pilotar los cambios previstos antes de tu próximo lanzamiento.

#### Identificar y fusionar usuarios

Al [identificar]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) o [fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/), ahora puedes utilizar el parámetro `least_recently_updated` en la matriz `prioritization` para dar prioridad al usuario actualizado menos recientemente.

#### Fusión programada de usuarios

[La fusión programada]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#scheduled-merging) te permite automatizar diariamente la fusión de perfiles de usuario mediante reglas preconfiguradas. Braze notificará a los administradores de tu espacio de trabajo 24 horas antes de que se produzca la fusión programada, proporcionando un recordatorio y tiempo para revisar la configuración.

#### Objeto destinatario

Ahora puedes incluir `braze_id` en el [objeto destinatario]({{site.baseurl}}/api/objects_filters/recipient_object/), lo que te permite solicitar o escribir información en nuestros endpoints.

#### Nuevos centros de datos

Braze ha puesto en marcha dos nuevos [centros de datos]({{site.baseurl}}/user_guide/data/data_centers/): US-10 e ID-01. Puedes registrarte en centros de datos específicos de una región al configurar tu cuenta Braze. 

### Desbloquear la creatividad

#### Plantillas de páginas de destino

Utiliza [plantillas de páginas de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#using-landing-page-templates) para crear plantillas para tus próximas campañas. Se puede acceder a estas plantillas y gestionarlas tanto en el editor de páginas de destino como en la sección **Plantillas** del panel de control.

#### Campo del formulario de la página de destino

Al personalizar tu página de destino, puedes elegir si un campo de formulario es [obligatorio u opcional]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page). Los campos obligatorios deben rellenarse antes de enviar el formulario. El usuario puede dejar en blanco o deseleccionar los campos opcionales.

#### Plantillas prediseñadas de Canvas

Braze Canvas ofrece varias [plantillas preconstruidas]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) adaptadas específicamente a los especialistas en marketing de comercio electrónico, lo que facilita la aplicación de estrategias esenciales. Esta página ofrece algunas plantillas clave que puedes utilizar para mejorar tus recorridos del cliente.

### Canales robustos

#### Vídeos de WhatsApp

{% multi_lang_include release_type.md release="Acceso anticipado" %}

[Los archivos de video de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages) ahora se pueden alojar a través de una URL o en la biblioteca multimedia Braze.

#### Mensajes de la lista de WhatsApp

[Los mensajes de lista]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages#list-messages/) aparecen como un cuerpo de mensaje con una lista de opciones en las que se puede hacer clic. Cada lista puede tener varias secciones, y cada lista puede tener hasta 10 filas.

#### Copiar enlace a vista previa

Utiliza **el enlace Copiar vista previa** en tus [mensajes de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#step-3-add-your-sending-information) HTML y arrastrar y soltar, [plantillas de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/#step-5-preview-and-test-your-message) y [bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) para generar un enlace compartible que muestre el aspecto que tendrá tu contenido para un usuario aleatorio.

#### Esquema de registro push

Hemos renovado nuestra documentación sobre notificaciones push en la Guía del usuario y hemos añadido un nuevo diagrama para ayudar a visualizar [cómo es el registro push a gran escala]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#what-does-this-look-like-on-a-broader-scale).

### Nuevas asociaciones Braze

#### Categorías de socios actualizadas

Hemos actualizado la [sección Socios tecnológicos]({{site.baseurl}}/partners/home/) con nuevas categorías y subcategorías para mejorar tu experiencia de navegación.

#### Shopify (nueva versión) - Comercio electrónico

A partir de abril se lanzará una nueva versión de la integración de Shopify por fases, en función del tipo de tienda Shopify y del ID externo utilizado para configurar la integración inicial.

**La versión anterior de la integración quedará obsoleta el 28 de agosto de 2025. Debes actualizar a la nueva versión de la integración antes del 28 de agosto de 2025.**

Nuevos clientes de Braze: A partir de abril de 2025, Braze desplegará gradualmente el nuevo conector de Shopify para las nuevas incorporaciones y la actualización de los clientes existentes. Para saber más sobre la nueva integración estándar, consulta [Integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration/).

#### Just Words - Contenido dinámico

[Just Words]({{site.baseurl}}/partners/just_words/) hiperpersonaliza la mensajería a escala en los canales de marketing del ciclo de vida, permitiéndote probar dinámicamente cientos de variaciones y actualizar automáticamente el contenido de bajo rendimiento.

#### Tapcart - Comercio electrónico

[Tapcart]({{site.baseurl}}/partners/ecommerce/tapcart/) es una plataforma líder de comercio móvil para marcas impulsadas por Shopify, que habilita a los comerciantes para crear aplicaciones móviles personalizadas que entregan experiencias de compra personalizadas y atractivas que sus clientes adoran.

### SDK

#### Gestión de la versión del SDK de Braze

Ahora puedes informarte sobre la [gestión de versiones]({{site.baseurl}}/developer_guide/sdk_integration/version_management/) del SDK de Braze, para que tu aplicación se mantenga actualizada con las últimas características y mejoras de calidad.

#### Auditoría de documentos SDK

Actualmente estamos auditando todo el [contenido de]({{site.baseurl}}/developer_guide/) nuestro [SDK para desarrolladores]({{site.baseurl}}/developer_guide/) con el fin de garantizar que todos nuestros ejemplos de código sean útiles y precisos. Hasta ahora, hemos realizado diversas actualizaciones de nuestros documentos sobre Android y Swift, y hay más en camino.

### Contribuir a la documentación de Braze

#### Soporte offline para colaboradores de Braze

Si eres colaborador de Braze Docs, ahora puedes generar tu sitio docs local completamente sin conexión. Para empezar, consulta [Contribuir a Braze Docs]({{site.baseurl}}/contributing/home/).

#### Solución de problemas de tu horquilla Braze Docs

Para los colaboradores de Braze Docs que tengan problemas para acceder a nuestro repositorio desde su bifurcación, hemos creado [unos pasos de solución de problemas]({{site.baseurl}}/contributing/troubleshooting/#missing-base-repository) que te ayudarán a volver al buen camino.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de Unity para Braze 8.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
    - Actualizado el puente nativo de iOS de [Braze Swift SDK 10.3.0 a 11.9.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.9.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el puente nativo de Android de [Braze Android SDK 32.1.0 a 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - La versión mínima requerida del SDK de Android es la 25. Consulta más detalles [aquí](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Braze Segmento Kotlin 3.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md)
    - Actualizado el SDK para Android de Braze [de 32.1.0 a 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - La versión mínima requerida del SDK de Android es la 25. Consulta más detalles [aquí](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [SDK Swift de Braze 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200)
    - Los XCFrameworks estáticos distribuidos ahora incluyen sus recursos directamente en lugar de depender de paquetes de recursos externos.
        - Al integrar manualmente los XCFrameworks estáticos, debes seleccionar la opción *Incrustar y firmar* para cada XCFramework en la sección *Marcos, bibliotecas y contenido incrustado* de la *configuración general* de tu objetivo.
        - No se requieren cambios para las integraciones con Swift Package Manager o CocoaPods.
- [Segmento Braze Swift 6.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Actualiza los enlaces del SDK Swift de Braze para que requieran versiones de la denominación `12.0.0`+ SemVer.
        - Esto permite la compatibilidad con cualquier versión del SDK de Braze desde `12.0.0` hasta, pero sin incluir, `13.0.0`.
        - Consulta la entrada del registro de cambios de [`12.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200) para obtener más información sobre posibles cambios de última hora.

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

Ahora hay tres [atributos predeterminados del perfil de usuario]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes/) en Snowflake. Cada vista está diseñada para un caso de uso específico con sus propias consideraciones de rendimiento. Por ejemplo, se te puede proporcionar un snapchat periódico de los atributos predeterminados de un perfil de usuario.

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

#### Soporte Flutter para Banners

{% multi_lang_include release_type.md release="Acceso anticipado" %}

Ahora los banners son compatibles con Flutter. Además, se ha revisado toda la documentación de Banner para facilitar su uso. Consulta los siguientes artículos para empezar:

- [Acerca de las pancartas]({{site.baseurl}}/developer_guide/banners/)
- [Crear campañas de banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
- [Insertar banners en tu aplicación]({{site.baseurl}}/developer_guide/banners/creating_placements/)

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

![El botón de revertir para la sincronización automática en Braze.]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
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
 
La asociación entre Braze y [Email Love]({{site.baseurl}}/partners/message_orchestration/) aprovecha la característica Exportar a Braze de Email Love y la API de Braze para cargar tus plantillas de correo electrónico a Braze fácilmente.

#### VWO - Pruebas A/B
 
La integración de Braze y [VWO]({{site.baseurl}}/partners/data_and_analytics/ab_testing/vwo/) te permite aprovechar los datos de los experimentos de VWO para crear segmentos específicos y entregar campañas personalizadas.
 
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

Ahora puedes especificar un destinatario por dirección de correo electrónico para desencadenar tus [campañas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) y [Lienzos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience).

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
[Constructor]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/constructor/) es una plataforma de búsqueda y descubrimiento de productos que utiliza IA y aprendizaje automático para entregar experiencias personalizadas de búsqueda, recomendación y navegación para sitios web de comercio minorista y comercio electrónico.
 
#### Trustpilot - Contenido dinámico
[Trustpilot]({{site.baseurl}}/partners/trustpilot/) es una plataforma de opiniones en línea que habilita a tus clientes a compartir opiniones y te permite administrar y responder a las opiniones.

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

[Justuno]({{site.baseurl}}/partners/data_and_analytics/leads_capture/justuno/) te permite crear experiencias de visita totalmente optimizadas para todas tus audiencias con segmentos dinámicos, ofreciendo la segmentación más avanzada disponible, todo ello sin afectar a la velocidad del sitio ni aumentar el trabajo de desarrollo.

#### Odicci - Plataforma de datos de los clientes

Integra Braze con [Odicci]({{site.baseurl}}/partners/odicci/), una plataforma que permite a las empresas captar, fidelizar y retener a sus clientes mediante experiencias omnicanales basadas en la fidelización.

#### Optimizely - Pruebas A/B

La integración de Braze y [Optimizely]({{site.baseurl}}/partners/data_and_analytics/ab_testing/optimizely/) es una integración bidireccional que te permite:

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
