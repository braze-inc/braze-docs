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
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Notas de la versión más reciente de Braze {#most-recent}

> Braze publica información sobre las actualizaciones del producto con una cadencia mensual, en consonancia con las principales versiones del producto, aunque el producto se actualiza con mejoras varias semana a semana.
> <br>
> <br>
> Para obtener más información sobre cualquiera de las actualizaciones enumeradas en esta sección, ponte en contacto con tu director de cuentas o [abre un ticket de soporte]({{site.baseurl}}/help/support/). También puedes consultar [nuestros registros de cambios del SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) para ver más información sobre nuestros lanzamientos, actualizaciones y mejoras mensuales del SDK.

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

La integración de Braze y [Zeotap](https://zeotap.com/) te permite ampliar la escala y el alcance de tus campañas sincronizando los segmentos de clientes de Zeotap con los perfiles de usuario de Braze. Con [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), también puedes conectar los datos a Zeotap para que sean procesables en todo el stack de crecimiento.

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

Utiliza [el depurador integrado del SDK de Braze]({{site.baseurl}}/developer_guide/platform_wide/debugging/) para solucionar problemas de tus canales con SDK sin necesidad de habilitar el registro detallado en tu aplicación.

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

[Conecta tu propio dominio]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/connect_domain/) a tu espacio de trabajo Braze para personalizar las URL de tus páginas de destino con tu marca.

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

Mediante el [cifrado a nivel de campo identificador]({{site.baseurl}}/user_guide/data_and_analytics/field_level_encryption/), puedes cifrar fácilmente las direcciones de correo electrónico con el servicio de administración de claves (KMS) de AWS para minimizar la información de identificación personal (PII) compartida en Braze. La encriptación sustituye los datos sensibles por texto cifrado, que es información encriptada ilegible.

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

El [panel de uso de mensajes]({{site.baseurl}}/message_usage/) proporciona información de autoservicio sobre tu uso de crédito de SMS y WhatsApp para obtener una visión completa del uso histórico y actual comparado con las asignaciones del contrato. Esta información puede reducir tu confusión y ayudarte a hacer ajustes para evitar riesgos de excedente.

### SDK

#### Inicialización retardada para el SDK Swift de Braze

Configura [la inicialización retardada]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/) para inicializar tu SDK Braze Swift de forma asíncrona, garantizando al mismo tiempo que se conserva la gestión de las notificaciones push. Esto puede ser útil cuando necesites configurar otros servicios antes de inicializar el SDK, como obtener datos de configuración de un servidor o esperar el consentimiento del usuario.

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

## Liberación el 20 de agosto de 2024

### Nuevos casos de uso

#### Catálogos

Puede introducir cualquier tipo de datos en un catálogo. Normalmente, los datos son metadatos sobre ofertas, como productos, descuentos, promociones, eventos y similares. Lee nuestros [casos de uso]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) y descubre cómo puedes utilizar estos datos para dirigirte a los usuarios con mensajes muy relevantes.

#### Intelligence Suite

La Intelligence Suite proporciona potentes características para analizar el historial de usuarios y el rendimiento de campañas y Canvas, y luego hacer ajustes automáticos para aumentar la interacción, la audiencia y las conversiones. Para ver algunos ejemplos de cómo estas características pueden beneficiar a distintos sectores, consulta nuestros [casos de uso]({{site.baseurl}}/user_guide/brazeai/intelligence).

### Actualización del panel de inicio

Puedes [continuar donde lo dejaste]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off) en el panel de Braze, con fácil acceso a los archivos que has editado o creado recientemente. Esta sección aparece en la parte superior de la página de **Inicio** del panel de Braze.

### Flexibilidad de los datos

#### Plantillas de transformación de datos y nuevo destino

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Construye tu Transformación de Datos utilizando nuestra [biblioteca de plantillas]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-2-create-a-transformation) específica para ayudarte a empezar con determinadas plataformas externas, en lugar del código predeterminado. Ahora puedes seleccionar **POST: Envía mensajes inmediatamente a través de la API Sólo** como destino para transformar webhooks de una plataforma de origen para enviar mensajes inmediatos a tus usuarios.

#### Fusionar usuarios en bloque

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Si encuentras perfiles de usuario duplicados, puedes [fusionarlos en bloque]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) para racionalizar tus datos.

#### Exportar atributos personalizados

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Puedes [exportar la lista de atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#exporting-data) como un archivo CSV seleccionando **Exportar todo** en la página **Atributos personalizados**. Se generará el archivo CSV y se le enviará por correo electrónico un enlace de descarga.

#### Lista de IP permitidas Currents

Braze enviará los datos de Currents de las IP incluidas en la lista, que se añaden automática y dinámicamente a cualquier clave de API que haya sido objeto de [adhesión]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents) voluntaria.

### Canales robustos

#### Nueva experiencia de creación de segmentos

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Construye un segmento utilizando nuestra [experiencia actualizada]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment). Los segmentos se actualizan en tiempo real a medida que cambian los datos, y usted puede crear tantos segmentos como necesite para sus fines de segmentación y mensajería.

#### Métricas por segmentos

Utilice las plantillas de informes [del Generador de consultas]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) para desglosar las métricas de rendimiento de las campañas, Canvas, variantes y pasos por segmentos.

#### Adquisición de número de teléfono

Para utilizar el canal de mensajería de WhatsApp, necesitarás un número de teléfono que cumpla los requisitos de WhatsApp para su [API en la nube](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) o [su API local](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers). 

Debes adquirir tu número de teléfono tú mismo, ya que Braze no te lo proporcionará. Puede adquirir un teléfono físico con una tarjeta SIM a través de su proveedor de telefonía profesional o recurrir a uno de nuestros socios: Twilio o Infoblip. **Debes tener tu propia cuenta de Twilio o Infobip porque esto no se puede hacer a través de Braze.**

### Nuevas asociaciones Braze

#### Zendesk Chat - Chat instantáneo

La integración de Braze y [Zendesk Chat]({{site.baseurl}}/partners/zendesk_chat/) utiliza webhooks de cada plataforma para establecer una conversación bidireccional por SMS. Cuando un usuario solicita soporte, se crea un ticket en Zendesk. Las respuestas de los agentes se reenvían a Braze a través de una campaña de SMS desencadenada por la API, y las respuestas de los usuarios se devuelven a Zendesk.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Android SDK 32.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [SDK de Swift 10.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Se han realizado los siguientes cambios al suscribirse a eventos push con [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)):
        - El cierre de `update` se desencadenará ahora por los eventos "Push abierto" y "Push recibido" predeterminados. Antes, sólo se desencadenaba con los eventos "Push Abierto".
            - Para seguir suscribiéndote sólo a los eventos "Push Abierto", introduce `[.opened]` para el parámetro `payloadTypes`. Alternativamente, implementa tu cierre `update` para comprobar que el `type` del `Braze.Notifications.Payload` es `.opened`.
        - Al recibir una notificación push con `content-available: true`, la dirección [`Braze.Notifications.Payload.type`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type) será ahora `.received` en lugar de `.opened`.
    - Marca las siguientes API obsoletas como no disponibles:
        - `Braze.Configuration.Api.Flavor`
        - `Braze.Configuration.Api.flavor`
        - `Braze.Configuration.Api.SdkMetadata`
        - `Braze.Configuration.Api.addSdkMetadata(_:)`
        - `Braze.ContentCard.ClickAction.uri(_:useWebview:)`
        - `Braze.ContentCard.ClickAction.uri`
        - `Braze.InAppMessage.ClickAction.uri(_:useWebview:)`
        - `Braze.InAppMessage.ClickAction.uri`
        - `Braze.InAppMessage.ModalImage.imageUri`
        - `Braze.InAppMessage.Full.imageUri`
        - `Braze.InAppMessage.FullImage.imageUri`
        - `Braze.InAppMessage.Themes.default`
        - `Braze.deviceId(queue:completion:)`
        - `Braze._objc_deviceId(completion:)`
        - `Braze.deviceId()`
        - `Braze.User.setCustomAttributeArray(key:array:fileID:line:)`
        - `Braze.User.addToCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User.removeFromCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User._objc_addToCustomAttributeArray(key:value:)`
        - `Braze.User._objc_removeFromCustomAttributeArray(key:value:)`
        - `gifViewProvider`
        - `GifViewProvider.default`
    - Elimina las API obsoletas:
        - `Braze.Configuration.DeviceProperty.pushDisplayOptions`
        - `Braze.InAppMessageRaw.Context.Error.extraProcessClickAction`
    - Elimina la clase obsoleta `BrazeLocation` en favor de `BrazeLocationProvider`.
- [Versión 6.0.0 del SDK de Xamarin](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Se ha añadido compatibilidad con .NET 8.0 para los enlaces de iOS y Android, ya que .NET 7.0 ha llegado al final de su vida útil.
        - Esto elimina la compatibilidad con .NET 7.0.
    - Actualizado el enlace Android de [Braze Android 30.4.0 a 32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el enlace iOS de [Braze Swift SDK 9.0.0 a 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Al suscribirte a eventos de notificación push, la suscripción se desencadenará en iOS tanto para los eventos "Push recibido" como "Push abierto", en lugar de sólo para los eventos "Push abierto".
- [SDK de React Native 12.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/12.0.0/CHANGELOG.md)
    - Actualiza los enlaces de la versión nativa de iOS de [Braze Swift SDK 9.0.0 a 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Al suscribirte a eventos de notificación push, la suscripción se desencadenará en iOS tanto para `push_received` como para `push_opened`, en lugar de sólo para los eventos de `push_opened`.

## Liberación el 23 de julio de 2024

### Actualizaciones de Braze Docs

#### Diátaxis y Braze Docs

Estamos estandarizando nuestra documentación mediante un marco llamado [Diátaxis](https://diataxis.fr/). Para ayudar a nuestros escritores y colaboradores a crear contenidos que se ajusten a este nuevo marco, hemos creado [plantillas para cada tipo de contenido]({{site.baseurl}}/contributing/content_types).

#### Nueva plantilla pull-request para la documentación de Braze

Nos hemos tomado el tiempo de mejorar nuestra plantilla de solicitud de colaboración (PR) para que sea más fácil y menos confuso [contribuir a Braze Docs]({{site.baseurl}}/contributing/home/). Si aún crees que se puede mejorar, abre un PR o [envía una incidencia](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=). ¡Lo que sea más fácil!
 
### Flexibilidad de los datos

#### Exporta eventos personalizados y atributos

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Ahora puedes exportar eventos personalizados y atributos personalizados mediante el botón [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) y [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) puntos finales.

#### Nuevos permisos de Currents para usuarios

Hay dos nuevas configuraciones de permisos para los usuarios: **Ver integraciones de Currents** y **Editar integraciones de Currents**. Más información sobre los [permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions). 

#### Actualización de la política de retención de datos de Snowflake
 
A partir del 27 de agosto de 2024, se eliminará la información de identificación personal (PII) de todos los datos de los eventos de Intercambio Seguro de Datos de Snowflake que tengan más de dos años. Si utilizas Snowflake, puedes optar por conservar los datos completos de los eventos en tu entorno almacenando una copia en tu cuenta de Snowflake antes de que se aplique la política de retención. Más información sobre [la retención de datos en Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/).
 
### Desbloquear la creatividad

#### Mensajes multipágina dentro de la aplicación

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Añadir páginas a tu mensaje dentro de la aplicación te permite guiar a los usuarios a través de un flujo secuencial, como un flujo de incorporación o un viaje de bienvenida. Para obtener más información, consulta [Crear un mensaje dentro de la aplicación con arrastrar y soltar]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page).

#### Acortamiento de enlaces con Liquid

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Utiliza [Liquid para personalizar]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening) las URL, acortar automáticamente las URL contenidas en los mensajes SMS y recopilar análisis de la tasa de click-through. Para probarlo, consulta [Acortamiento de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/).

#### Ejemplos de API para catálogos

Hemos añadido ejemplos para el punto final `/catalogs` utilizando campos de matriz. Para ver los ejemplos, consulta lo siguiente:

- [Editar varios elementos del catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [Crear varios elementos del catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [Actualizar elementos del catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [Editar elemento del catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [Crear elemento del catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [Actualizar elemento del catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [Crear catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### Canales robustos

### Varias cuentas de WhatsApp Business

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Ahora puedes añadir varias cuentas de WhatsApp Business y grupos de suscripción (y números de teléfono) a cada espacio de trabajo. Para más detalles, consulta [Múltiples cuentas de WhatsApp Business]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups). 

#### Permisos geográficos para SMS

Los Permisos geográficos SMS mejoran la seguridad y protegen contra el tráfico SMS fraudulento al imponer controles sobre los países a los que puedes enviar mensajes SMS. Para saber cómo especificar una lista de países permitidos para asegurarte de que los mensajes SMS sólo se envían a las regiones aprobadas, consulta [Configurar tu lista de países permitidos para SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist).

#### LÍNEA y Braze

{% multi_lang_include release_type.md release="Beta" %}

[LINE](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf) es la aplicación de mensajería más popular de Japón, con más de 95 millones de usuarios activos al mes. Puedes integrar tus cuentas de LINE con Braze para aprovechar tus datos de clientes zero-party y first-party para enviar mensajes convincentes de LINE a los clientes adecuados en función de sus preferencias, comportamientos e interacciones entre canales. Para empezar, consulta [LÍNEA]({{site.baseurl}}/line).

#### Shopify: Bajadas de precio y reposición de existencias

{% multi_lang_include release_type.md release="Acceso anticipado" %}

Ahora, con Shopify, puedes crear notificaciones personalizadas para las [bajadas de precios]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) y los [artículos agotados]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications).
 
### Automatización de IA y ML
 
#### Fusión basada en reglas para usuarios duplicados

Anteriormente, podías encontrar y fusionar usuarios duplicados en Braze individualmente o en bloque. Ahora puedes crear reglas para controlar cómo se resuelven los duplicados, de modo que se mantenga al usuario más relevante. Para saber más, consulta [Fusión basada en reglas]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

#### Asistente de IA de Liquid

{% multi_lang_include release_type.md release="Beta" %}

El Asistente AI Liquid es un asistente de chat impulsado por <sup>BrazeAITM</sup> que te ayuda a generar el Liquid que necesitas para personalizar el contenido de los mensajes. Puedes generar Liquid a partir de plantillas, recibir sugerencias personalizadas de Liquid y optimizar el Liquid existente con la ayuda de <sup>BrazeAITM</sup>. El Asistente AI Liquid también proporciona anotaciones que explican el Liquid utilizado, para que puedas aumentar tu comprensión de Liquid y aprender a escribir el tuyo propio.

Para empezar, consulta [Asistente AI Liquid]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_liquid).
 
### SDK
 
#### Registros del SDK de Android

Hemos revisado [los documentos de registro del SDK para Android de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#logging), para que sean más fáciles de leer y utilizar en tu aplicación. También hemos añadido descripciones para cada nivel de registro.

#### Notificaciones push en primer plano del SDK de iOS

El método `subscribeToUpdates` del SDK de Braze para iOS ahora puede detectar si se recibe una notificación push en primer plano. Para saber más, consulta [Integración de notificaciones push de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration).
 
#### Actualización de la documentación de Xamarin
 
Desde [la versión 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0), el SDK de Xamarin para Braze utiliza la vinculación con el SDK Swift, por lo que hemos actualizado los fragmentos de código y el material de referencia. También hemos reestructurado la sección para que sea más fácil de leer y entender. Para comprobarlo, consulta [la documentación de Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup).

#### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.
 
- [SDK Swift 9.3.1](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.1)
- [SDK Web 5.3.2](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#532)
    - Se ha corregido una regresión introducida en la versión 5.2.0 que podía provocar que los mensajes dentro de la aplicación en formato HTML se mostraran incorrectamente cuando se cargaba un script externo de forma sincrónica.
- [SDK Web 5.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#540)

## Liberación el 25 de junio de 2024

### Documentos japoneses

¡Ahora la documentación de Braze está disponible en japonés!

![El sitio de documentación de Braze muestra la interfaz japonesa]({% image_buster /assets/img/braze-docs-japan.png %}){: style="max-width:70%;"}
 
### Flexibilidad de los datos

#### Adjuntos para campañas desencadenadas por API

{% multi_lang_include release_type.md release="Disponibilidad general" %}

El punto final [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) ahora admite archivos adjuntos (igual que el punto final `/messages/send` admite archivos adjuntos para correos electrónicos). 

#### Apoyo adicional al almacén de datos

{% multi_lang_include release_type.md release="Acceso anticipado" %}

La [ingesta de datos en la nube (CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources) de Braze ahora es compatible con BigQuery, Databricks, Redshift y Snowflake.

#### Migración del número de teléfono de WhatsApp

Migra tu número de teléfono de WhatsApp entre cuentas de WhatsApp Business utilizando el Registro integrado de Meta. Leer más sobre [Migración del número de teléfono de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration).
 
### Desbloquear la creatividad

#### Participación por dispositivo

{% multi_lang_include release_type.md release="Disponibilidad general" %}

El nuevo informe de **interacción por dispositivo** proporciona un desglose de los dispositivos que utilizan tus usuarios para interactuar con tu correo electrónico. Estos datos hacen un seguimiento de la interacción del correo electrónico en móviles, ordenadores de sobremesa, tabletas y otros tipos de dispositivos. Más información sobre [el informe y el panel de rendimiento del correo electrónico]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard).

#### Propiedades de WhatsApp y SMS Liquid en el flujo Canvas

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Hemos añadido compatibilidad con [las propiedades WhatsApp y SMS Liquid en el flujo Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Ahora, cuando un paso en Canvas contiene un desencadenante "Enviado un mensaje SMS entrante" o "Enviado un mensaje WhatsApp entrante", los pasos en Canvas posteriores pueden incluir una propiedad SMS o WhatsApp Liquid. Esto refleja cómo funcionan las propiedades del evento en el Flujo Canvas. De este modo, puedes aprovechar tus mensajes para guardar y consultar datos propios sobre perfiles de usuario y mensajería conversacional.
 
#### Caminos personalizados en lienzos recurrentes

{% multi_lang_include release_type.md release="Acceso anticipado" %}

Las rutas personalizadas en Canvas te permiten personalizar cualquier punto de un recorrido en Canvas para usuarios individuales en función de la probabilidad de conversión. Ahora, los Caminos personalizados están disponibles para los Lienzos recurrentes. Más información sobre [las variantes personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths).

#### Solución de problemas por segmentos

¿Trabajar con segmentos? Aquí tienes algunos [pasos para la solución de problemas y consideraciones]({{site.baseurl}}/user_guide/engagement_tools/segments/troubleshooting) para tener en cuenta.

#### Subrayado líquido

Hemos mejorado el [código de colores que utiliza Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) para adaptarlo mejor a las directrices de accesibilidad.

![]({% image_buster /assets/img/liquid_color_code.png %})
 
### Canales robustos

#### Permisos geográficos para SMS

{% multi_lang_include release_type.md release="Acceso anticipado" %}

Los permisos geográficos para SMS mejoran la seguridad y protegen contra el tráfico fraudulento de SMS al imponer controles sobre los países a los que puedes enviar mensajes SMS. Ahora los administradores pueden especificar una lista de países permitidos para asegurarse de que los mensajes SMS sólo se envían a las regiones aprobadas. Para más información, consulta [Permisos geográficos SMS]({{site.baseurl}}/sms_geographic_permissions). 

![El desplegable "Lista de países permitidos" con los países más comunes mostrados en la parte superior.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

#### Buenas prácticas para SMS/MMS

Obtén más información sobre [las buenas prácticas para SMS/MMS con Braze]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/best_practices), incluidas nuestras recomendaciones para la supervisión de la adhesión voluntaria y el bombeo de tráfico. 

#### Seguimiento de las cancelaciones de suscripción push

Consulta nuestro nuevo [artículo de ayuda]({{site.baseurl}}/help/help_articles/push/push_unsubscribes) para obtener algunos consejos sobre el seguimiento de las cancelaciones de suscripción push.

#### Supresión de `checkout.liquid` de Shopify

Ten en cuenta que el soporte para Shopify `checkout.liquid` comenzará a quedar obsoleto en agosto de 2024 y finalizará en agosto de 2025. Más información sobre cómo Braze [gestionará esta transición]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout). 

### Actualizaciones del SDK
 
Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.
 
- [SDK Swift 9.3.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.0)
    - Deja obsoletas las actuales API de banderas de características, que se eliminarán en una versión futura:
        - `Braze.FeatureFlag.jsonStringProperty(key:)` quedó obsoleto.
        - `Braze.FeatureFlag.jsonObjectProperty(key:)` ha quedado obsoleto en favor de `Braze.FeatureFlag.jsonProperty(key:)`.
- [SDK de Roku 2.2.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)
- [Plugin Expo de Braze 2.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)

#### Documentación de tvOS

Hace unos meses, los artículos para [las tarjetas de contenido de tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/tvos) y la [mensajería dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/tvos) quedaron obsoletos por error. Estos documentos se han vuelto a publicar en la sección Swift de Braze Docs.

{% alert note %}
[Los colaboradores]({{site.baseurl}}/contributing/home) de la documentación de Braze deben tener en cuenta que el sitio funciona ahora con Ruby 3.3.0. Actualiza tu versión de Ruby si es necesario.
{% endalert %}

## Liberación el 28 de mayo de 2024

### Actualizaciones visuales del sitio de documentación

Te habrás dado cuenta de que nuestro sitio web de documentación tiene un nuevo y elegante aspecto. Lo renovamos para reflejar la nueva y vibrante identidad de la marca Braze. Para ver entre bastidores nuestra nueva marca, lee más en [Unveiling Our New Brand: Una conversación con el director creativo ejecutivo de Braze Greg Erdelyi](https://www.braze.com/resources/articles/unveiling-our-new-brand-a-conversation-with-braze-executive-creative-director-greg-erdelyi).

### Soporte para portugués y español

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Braze ya está disponible en portugués y español. Para cambiar el idioma en el que aparece el panel de Braze, consulta [Configuración del idioma]({{site.baseurl}}/user_guide/administrative/access_braze/language/).

### Canales robustos

#### Configuración multilingüe

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Ajustando [la configuración multilingüe]({{site.baseurl}}/multi_language_support/), puedes dirigirte a usuarios de distintos idiomas y ubicaciones con mensajes diferentes, todo dentro de un mismo mensaje de correo electrónico. Para editar y administrar el soporte multilingüe, debes tener el permiso de usuario "Administrar configuración multilingüe". Para añadir la localización a un mensaje, necesitarás permisos para editar campañas.

#### Encabezado de cancelar suscripción a la lista con un clic a nivel de mensaje

{% multi_lang_include release_type.md release="Disponibilidad general" %}

La opción de cancelar suscripción con un clic para el encabezado de cancelar suscripción a la lista ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) ofrece a los destinatarios una forma sencilla de darse de baja de los correos electrónicos. Puedes ajustar esta configuración de cabecera para que se aplique a nivel de mensaje en tus correos electrónicos. Para más información sobre esta configuración, consulta [Cabecera de cancelar suscripción por correo electrónico en los espacios de trabajo]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#email-unsubscribe-header-in-workspaces).

#### Acerca de la desinfección del correo electrónico

Visita nuestro nuevo artículo [sobre desinfección]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization) para obtener más información sobre el proceso que se produce cuando Braze detecta un tipo específico de JavaScript en tu mensaje de correo electrónico. Su objetivo principal es impedir que los malos actores accedan a los datos de sesión de otros usuarios del panel de Braze.

#### Recuento de inclusión para bloques de contenido

Después de añadir un Bloque de contenido en una campaña o Canvas activos, puedes [obtener una vista previa de este Bloque de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) desde la Biblioteca de Bloques de contenido pasando el ratón por encima del Bloque de contenido y seleccionando el icono <i class="fa fa-eye preview-icon"></i> **Vista previa**.

#### Estados en Canvas

En el panel de Braze, tus Lienzos están agrupados por su estado. Consulta los diferentes [estados de Canvas y las descripciones]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) de lo que significan.

### Automatización de IA y ML

#### Directrices de marca para el asistente de redacción AI

{% multi_lang_include release_type.md release="Disponibilidad general" %}

Ahora puedes crear y aplicar [directrices de marca]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/) para personalizar el estilo de los textos generados por el asistente de redacción de IA para que se ajusten a la voz de tu marca. Configura múltiples pautas para diferentes escenarios, para asegurarte de que tu tono siempre se ajusta al contexto.
 
### Nuevas asociaciones Braze

#### Adikteev - Análisis

La integración de Braze y [Adikteev]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/) te permite impulsar la retención de usuarios aprovechando la tecnología de predicción del abandono de usuarios de Adikteev dentro de las campañas de CRM de Braze para dirigirte prioritariamente a los segmentos de usuarios de alto riesgo.
 
#### Celebrus - Análisis
 
La integración de Braze y [Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus) se integra fácilmente con el SDK de Braze en los canales Web y de aplicaciones móviles, facilitando la población de Braze con los datos de actividad del canal. Esto incluye información exhaustiva sobre el tráfico de visitantes en los activos digitales durante periodos específicos.
 
#### Estudio IAM - Plantillas de mensajes
 
Con la integración de Braze e [IAM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/) Studio, puedes insertar fácilmente plantillas de mensajes dentro de la aplicación personalizables en tus mensajes dentro de la aplicación Braze, ofreciendo sustitución de imágenes, modificación de texto, configuración de enlaces profundos, atributos personalizados y configuración de eventos. Con IAM Studio, puedes reducir el tiempo de producción de mensajes y dedicar más tiempo a la planificación de contenidos.
 
#### Regal - Chat instantáneo

Al integrar Braze y [Regal]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/), puedes crear una experiencia más coherente y personalizada en todos tus puntos de intervención con el cliente.

#### Treasure Data - Importación de cohortes
 
Con la integración de Braze y [Treasure Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/), puedes importar cohortes de usuarios de Treasure Data a Braze para poder enviar campañas específicas basadas en datos que quizá sólo existan en tu almacén.
 
#### Zapier - Automatización del flujo de trabajo
 
La asociación entre Braze y [Zapier]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/zapier/) aprovecha la API de Braze y los webhooks de Braze para conectar con aplicaciones de terceros y automatizar diversas acciones.

### Actualizaciones del SDK
 
Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Android SDK 31.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Plugin Swift de segmentos Braze 3.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#300)
    - Actualiza las vinculaciones del SDK Swift de Braze para que requieran versiones de la denominación 9.2.0+ SemVer.
        - Esto permite la compatibilidad con cualquier versión del SDK de Braze desde la 9.2.0 hasta la 10.0.0, pero sin incluirla.
        - Consulta las entradas del registro de cambios de las [versiones 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#700), [8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800) y [9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#900) para obtener más información sobre posibles cambios de última hora.
    - La compatibilidad con las notificaciones push requiere ahora una llamada al método estático `BrazeDestination.prepareForDelayedInitialization()` lo antes posible en el ciclo de vida de la aplicación, en el método `AppDelegate.application(_:didFinishLaunchingWithOptions:)` de tu aplicación.
- [Cordova SDK 9.0.0-9.2.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Actualizado el puente nativo de iOS [del SDK Swift de Braze 7.7.0 a 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Plugin Expo 2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [SDK de Flutter 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [SDK React Native 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [SDK Swift 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- Unity 6.0.0
    - Actualizado el puente nativo de iOS [del SDK Swift de Braze 7.7.0 a 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el puente nativo de Android [del SDK para Android de Braze 29.0.1 a 30.3.0](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK Web 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Versión 5.0.0 del SDK de Xamarin
    - Actualizada la vinculación de iOS [del SDK Swift de Braze 8.4.0 a 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
