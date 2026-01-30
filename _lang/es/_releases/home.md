---
nav_title: Inicio
article_title: Novedades en Braze
description: "Las notas de la versión de Braze se publican mensualmente para que puedas estar al día de las principales versiones del producto, las mejoras continuas del producto, las asociaciones de Braze, los cambios de última hora en el SDK y las características obsoletas."
page_order: 0
search_rank: 1
page_type: reference

---

# Novedades en Braze

{% alert tip %}
Para obtener más información sobre cualquiera de las actualizaciones enumeradas en esta página, ponte en contacto con el director de cuentas o [abre un ticket de soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). También puedes consultar nuestro [SDK Changelogs]({{site.baseurl}}/developer_guide/changelogs) para obtener más información sobre nuestras versiones mensuales del SDK, mejoras y cambios de última hora.
{% endalert %}

{% details January 8, 2026 %}
## Lanzamiento el 8 de enero de 2026

### Datos e informes

#### Eventos recomendados de comercio electrónico

{% multi_lang_include release_type.md release="Early access" %}

Para hacer coincidir los eventos recomendados por eCommerce con el evento de compra existente, añadimos el [ evento de conversión "Realiza pedido"]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report), que es similar a "Realiza compra".

#### Actualizaciones de los eventos Currents

{% multi_lang_include release_type.md release="General availability" %}

En la versión 4 se han introducido los siguientes cambios en Currents:

* El campo cambia al tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Añadido el nuevo campo `string` `push_token` : Token de notificaciones push del evento
* El campo cambia al tipo de evento `users.messages.pushnotification.Bounce`:
    * Añadido el nuevo campo `string` `push_token` : Token de notificaciones push del evento
* El campo cambia al tipo de evento `users.messages.pushnotification.Send`:
    * Añadido el nuevo campo `string` `push_token` : Token de notificaciones push del evento
* El campo cambia al tipo de evento `users.messages.rcs.Click`:
    * Añadido el nuevo campo `string` `canvas_variation_name` : Nombre de la variación de Canvas que recibió este usuario
    * El campo `user_phone_number` es ahora *opcional*.
* El campo cambia al tipo de evento `users.messages.rcs.InboundReceive`:
    * El campo `user_id` es ahora *opcional*.
* El campo cambia al tipo de evento `users.messages.rcs.Rejection`:
    * Añadido el nuevo campo `string` `canvas_step_message_variation_id` : API ID de la variación del mensaje del paso Canvas que recibió este usuario

Consulta [el registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) para ver los cambios en los eventos de cada versión.

#### Exportar registros de sincronización por todas las filas

{% multi_lang_include release_type.md release="Early access" %}

En el [panel **Registro de sincronización**]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs) de [la ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs), puedes elegir exportar los registros a nivel de fila de una sincronización ejecutada por:

* Filas con errores Descarga un archivo que contiene sólo las filas que tenían un estado de **Error**.
* Todas las filas Descarga un archivo que contiene todas las filas procesadas en la ejecución.

### Canales y puntos de intervención

#### Conector WhatsApp "Trae tu propio" (BYO)

El [conector Bring Your Own (BYO) WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/) ofrece una asociación entre Braze e Infobip, en la que das acceso a Braze a tu administrador de negocios WhatsApp de Infobip (WABA). Esto te permite gestionar y pagar los costes de mensajería directamente con Infobip, a la vez que utilizas Braze para la segmentación, personalización y orquestación de campañas. 

#### Banners en Canvas

{% multi_lang_include release_type.md release="Early access" %}

Puedes seleccionar **Banners** como canal de mensajería en un [paso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) en Canvas. Puedes utilizar el editor de arrastrar y soltar para crear mensajes personalizados en línea, proporcionando experiencias no intrusivas y contextualmente relevantes que se actualizan automáticamente al inicio de cada sesión de usuario. 

#### CCO dinámico

{% multi_lang_include release_type.md release="General availability" %}

Con [el CCO dinámico]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc), puedes utilizar Liquid en tu dirección CCO. Ten en cuenta que esta característica sólo está disponible en **Preferencias de correo electrónico** y no se puede configurar en la propia campaña. Sólo se permite una dirección CCO por destinatario de correo electrónico.

#### Límites de velocidad basados en el canal

Como alternativa a un límite de velocidad que se comparte en toda una campaña multicanal o Canvas, puedes seleccionar un límite de velocidad específico por canal. En este caso, el límite de velocidad se aplicará a cada uno de tus canales seleccionados. Por ejemplo, puedes configurar tu campaña o Canvas para que envíe un máximo de 5.000 webhooks y 2.500 mensajes SMS por minuto en toda la campaña o Canvas. Para más detalles, consulta [Limitación de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting).

### Asociación

#### LILT - Localización

[LILT]({{site.baseurl}}/partners/lilt/) es la solución completa de IA para la traducción y la creación de contenidos empresariales. LILT habilita a las organizaciones globales para escalar y optimizar sus contenidos, productos, comunicaciones y operaciones de soporte, con agentes de IA y flujos de trabajo totalmente automatizados.

### Actualizaciones de última hora del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Androide 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011):
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [SDK de Swift 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Elimina la fuente de noticias.
        - Esto elimina por completo todos los elementos de la interfaz de usuario, los modelos de datos y las acciones asociadas a la Fuente de noticias.
- [SDK Web 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## 9 de diciembre de 2025

### Datos e informes

#### Añadir Google Tag Manager a una página de destino

Para añadir Google Tag Manager a tus páginas de destino, añade un bloque de código personalizado a tu página de destino en el editor de arrastrar y soltar, y luego [inserta el código de Google Tag Manager]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) en el bloque.

### Orquestación

#### Caso de uso de SMS Liquid

El caso de uso [Responder con mensajes diferentes en función de la palabra clave del SMS entrante]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) incorpora el procesamiento dinámico de palabras clave del SMS para responder a mensajes entrantes específicos con una copia de mensaje diferente. Por ejemplo, puedes enviar respuestas diferentes cuando alguien envía un mensaje de texto de "INICIAR" frente a "UNIRSE".

#### Allowlisting para contenido conectado

Puedes permitir que se utilicen URL específicas para [el Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call). Para acceder a esta característica, ponte en contacto con tu administrador del éxito del cliente.

### Canales y puntos de intervención

#### Codificación de caracteres SMS

¡Nuestra [calculadora de segmentos]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator) SMS ahora tiene codificación de caracteres! Selecciona **Mostrar codificación de caracteres** para identificar qué caracteres están codificados como GSM-7 o UCS-2. 

![Calculadora de segmentos SMS con un mensaje SMS de muestra introducido en el cuadro de texto y la codificación de caracteres activada.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### Mensajes de WhatsApp con optimización

Dado que la API de MM para WhatsApp no ofrece una capacidad de entrega del 100%, es importante entender cómo reorientar a los usuarios que no hayan recibido tu mensaje en otros canales. 

Para reorientar a los usuarios, recomendamos crear un segmento de usuarios que no recibieron un mensaje específico. Para ello, filtra por el código de error `131049`, que indica que no se ha enviado un mensaje de plantilla de marketing debido a la aplicación del límite de plantillas de marketing por usuario de WhatsApp. Puedes hacerlo [utilizando Braze Currents o Extensiones de segmento SQL]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels).

### Asociación

#### OtrosNiveles - Contenido dinámico

[OtherLevels]({{site.baseurl}}/partners/otherlevels/) es una plataforma de experiencias que utiliza IA generativa para transformar el modo en que las marcas deportivas, los editores y los operadores conectan con sus clientes, transformando el contenido tradicional en experiencias de video y rich media personalizadas y a escala.

### SDK

#### Actualizaciones de última hora del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK Web 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## Noviembre de 11, 2025:

### Flexibilidad de los datos

#### `Live Activities Push to Start Registered for App` filtro de segmentación

El filtro `Live Activities Push to Start Registered for App` segmenta a tus usuarios en función de si están registrados para iniciar una Actividad en vivo a través de notificaciones push de iOS para una aplicación específica.

#### Extensión de segmento RFM SQL

Puedes crear una [Extensión de segmento RFM (recencia, frecuencia, monetario)]({{site.baseurl}}/rfm_segments/) para dirigirte a tus mejores usuarios midiendo sus hábitos de compra.

El análisis RFM es una técnica de marketing que identifica a tus mejores usuarios puntuándolos en una escala de 0 a 3 para cada categoría (recurrencia, frecuencia, monetaria), donde 3 es la mejor puntuación y 0 la peor. La recurrencia, la frecuencia y los valores monetarios se basan en los datos de un intervalo de tiempo específico que tú elijas.

#### Atributos personalizados - Valores 

Cuando visualices un informe de uso, selecciona la [pestaña**Valores**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) para ver los valores más altos de los atributos personalizados seleccionados, basados en una muestra de aproximadamente 250.000 usuarios.

#### Registros de sincronización y observabilidad para la ingesta de datos en la nube

{% multi_lang_include release_type.md release="General availability" %}

El [panel de Registro de Sincronización]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) de la Ingesta de Datos en la Nube (CDI) te permite supervisar todos los datos procesados por CDI, verificar si los datos se sincronizaron correctamente y diagnosticar cualquier problema con datos "incorrectos" o ausentes.

#### Despliegues de banderas de características multirregla

Utiliza lanzamientos [de banderas de características con]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) reglas [múltiples]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) para definir una secuencia de reglas para evaluar a los usuarios, lo que permite una segmentación precisa y lanzamientos de características controlados. Este método es ideal para desplegar la misma característica a diversas audiencias.

#### Mapeado a campos de catálogo para bloques de producto arrastrar y soltar

En la configuración de tu catálogo, puedes seleccionar el alternador **Bloques de productos** para [mapear a campos]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) e información [específicos]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) de tu catálogo. Esto te permite seleccionar qué campos utilizar como título del producto, URL del producto y URL de la imagen.

#### Eventos de anulación por limitación de frecuencia en Currents

Al utilizar Currents, ahora puedes hacer referencia a `abort_type` en los eventos de interrupción del canal. Identifica que un mensaje se ha interrumpido debido a la limitación de frecuencia e incluye la regla de limitación de frecuencia que ha provocado la interrupción. Esto te ayudará a configurar tus reglas de limitación de frecuencia. Consulta [Eventos de interacción con mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) para obtener detalles específicos de los eventos de Currents.

### Canales robustos

#### Imágenes de fondo de fila 

{% multi_lang_include release_type.md release="General availability" %}

Puedes [añadir una imagen de fondo de fila]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image) a un mensaje dentro de la aplicación o a una página de destino en el panel de **propiedades de fila**. Alterna entre **Imagen de fondo** y, a continuación, proporciona una URL de imagen o selecciona una imagen de la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). Por último, configura el texto alternativo, el tamaño, la posición y si la imagen se repite para crear patrones en toda la fila.

![Una imagen de fondo en fila de una pizza que tiene un patrón de repetición horizontal.]({% image_buster /assets/img_archive/background_row.png %})

#### Copiar enlace a vista previa

Utiliza **el enlace Copiar vista previa** en tus [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional), [pies de página personalizados de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer) y [páginas de adhesión voluntaria y cancelación suscripción]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers) para generar un enlace compartible que muestre el aspecto que tendrá tu contenido para un usuario cualquiera.

#### Mensajes de WhatsApp con entrega optimizada

Utiliza los avanzados sistemas de IA de Meta para entregar tus mensajes de marketing a más usuarios que tengan más probabilidades de interactuar con ellos, aumentando significativamente la capacidad de entrega y la interacción con los mensajes.

[Los mensajes de WhatsApp con entrega optimizada]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/) se envían utilizando la nueva [API Lite de Mensajes de Marketing](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) de Meta, que proporciona un rendimiento superior en comparación con la API tradicional de la Nube. Este nuevo canal de envío te ayuda a llegar mejor a los usuarios que valoran y quieren recibir tus mensajes.

#### WhatsApp Flows

Al incorporar un mensaje de WhatsApp Flow a un Braze Canvas o a una campaña, puede que quieras capturar y utilizar información específica que los usuarios envíen a través del Flow. Braze necesita recibir información adicional sobre la estructura de la respuesta del usuario, concretamente la forma prevista de la respuesta JSON, para generar el esquema de atributos personalizados anidados (NCA) requerido.

Ahora puedes dar a Braze la información sobre la estructura de la respuesta [guardando la respuesta Flujo como un atributo personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) y completando un envío de prueba.

#### Vista previa de usuario editable

Puedes [editar campos individuales de un usuario aleatorio o existente]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user) para ayudar a probar el contenido dinámico dentro de tu mensaje. Selecciona **Editar** para convertir el usuario seleccionado en un usuario personalizado que puedas modificar.

![La pestaña "Vista previa como usuario" con un botón "Editar".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Automatización de IA y ML

#### BrazeAI Decisioning Studio™ Go

Ya puedes configurar tu integración con [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go) Go consultando estos artículos de configuración para:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Nuevas características para los Agentes Braze

{% multi_lang_include release_type.md release="Beta" %}

Ahora puedes personalizar tu [Agente Braze]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents):

- Aplicar [directrices de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) para que tu agente se adhiera a ellas en su respuesta. 
- Hacer referencia a un catálogo para personalizar aún más tu mensaje.
- Estructurar la salida de un agente proporcionando el [formato de salida]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format).
- Ajusta la [temperatura]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) para el nivel de desviación de la salida de tu agente.

### Modelos ChatGPT con Operador <sup>BrazeAITM</sup> 

{% multi_lang_include release_type.md release="Beta" %}

Puedes seleccionar entre estos modelos de GPT para utilizarlos en diferentes tipos de solicitudes con [Operador]({{site.baseurl}}/user_guide/brazeai/operator):

- GPT-5 Nano
- GPT-5 mini (predeterminado)
- GPT-5

### Nuevas asociaciones Braze

#### StackAdapt - Publicidad

[StackAdapt]({{site.baseurl}}/partners/stackadapt/) es una plataforma de marketing basada en IA que entrega publicidad orientada al rendimiento. Te permite sincronizar los datos de perfil de usuario desde Braze al Data Hub de StackAdapt. Al conectar las dos plataformas, puedes crear una visión unificada de tus clientes y activar los datos propios para mejorar el rendimiento de los anuncios.

#### Cloudinary - Contenido dinámico

[Cloudinary]({{site.baseurl}}/partners/cloudinary/) es una plataforma de imagen y video que te permite gestionar, editar, optimizar y entregar imágenes y video a gran escala a cualquier campaña a través de canales y recorridos del cliente. Una vez integrada y habilitada, la gestión de medios de Cloudinary potenciará y proporcionará una entrega de activos dinámica, contextual y personalizada para tus campañas y Lienzos Braze.

#### Kameleoon - Pruebas A/B

[Kameleoon]({{site.baseurl}}/partners/kameleoon/) es una solución de optimización con capacidades de experimentación, personalización basada en IA y gestión de características en una única plataforma unificada.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de React Native 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Corrige el tipo Typescript para la devolución de llamada de `subscribeToInAppMessage` y `addListener` para `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Estas escuchas ahora devuelven correctamente una devolución de llamada con el nuevo tipo `InAppMessageEvent`. Antes, los métodos estaban anotados para devolver un tipo `BrazeInAppMessage`, pero en realidad devolvían un `String`.
         - Si utilizas cualquiera de las dos API de suscripción, asegúrate de que el comportamiento de tus mensajes dentro de la aplicación no cambia tras actualizar a esta versión. Consulta nuestro código de muestra en `BrazeProject.tsx`.
    - Las API `logInAppMessageClicked`, `logInAppMessageImpression`, y `logInAppMessageButtonClicked` ahora sólo aceptan un objeto `BrazeInAppMessage` para que coincida con su interfaz pública existente.
        - Anteriormente, aceptaba tanto un objeto `BrazeInAppMessage` como un `String`.
    - `BrazeInAppMessage.toString()` ahora devuelve una cadena legible por humanos en lugar de la representación de cadena JSON.
        - Para obtener la representación en cadena JSON de un mensaje dentro de la aplicación, utiliza `BrazeInAppMessage.inAppMessageJsonString`.
    - En iOS, `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` se ha trasladado a `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`.
        - Este nuevo método es ahora un método de clase en lugar de un método de instancia.
    - Añade anotaciones de anulabilidad a los métodos de `BrazeReactUtils`.
    - Elimina de la API los siguientes métodos y propiedades obsoletos:
        - `getInstallTrackingId(callback:)` a favor de `getDeviceId`.
        - `registerAndroidPushToken(token:)` a favor de `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` a favor de `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` a favor de `payload_type`.
        - `PushNotificationEvent.deeplink` a favor de `url`.
        - `PushNotificationEvent.content_text` a favor de `body`.
        - `PushNotificationEvent.raw_android_push_data` a favor de `android`.
        - `PushNotificationEvent.kvp_data` a favor de `braze_properties`.
    - Actualiza los enlaces de la versión nativa de Android SDK [de Braze Android SDK 39.0.0 a 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [.NET MAUI (Xamarin) SDK Versión 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Actualizado el enlace iOS de [Braze Swift SDK 12.1.0 a 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Esto incluye la compatibilidad con Xcode 26.
- [SDK de Flutter 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Actualiza el puente nativo de Android [de Braze Android SDK 39.0.0 a 40.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [SDK Swift de Braze 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Web 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## Liberación el 14 de octubre de 2025

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) sustituye las pruebas A/B por la toma de decisiones con IA que lo personaliza todo y maximiza cualquier métrica: impulsa los dólares, no los clics. Con BrazeAI Decisioning Studio™, puedes optimizar cualquier KPI empresarial. Consulta nuestra sección dedicada [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) para ver ejemplos de casos de uso y características clave.

### Flexibilidad de los datos

#### Eventos de New Currents

Estos nuevos acontecimientos se han añadido al [glosario de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events):

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`
- `users.messages.inappmessage.Abort`

Estos nuevos campos se añadieron a los siguientes eventos de Currents:

- `is_sms_fallback`: 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id` 
  - `users.messages.whatsapp.InboundReceive`
- `message_id` 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Listas de supresión

{% multi_lang_include release_type.md release="General availability" %}

[Las listas de supresión]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) son grupos de usuarios que no reciben automáticamente ninguna campaña o Lienzo. Las listas de supresión se definen mediante filtros de segmento, y los usuarios entran y salen de las listas de supresión a medida que cumplen los criterios de filtrado.

#### Personalización sin copia

{% multi_lang_include release_type.md release="Early access" %}

Sincroniza los desencadenantes de Canvas utilizando la ingesta de datos en la nube para [una personalización de copia cero]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). Esta característica accede a información específica del usuario desde tu solución de almacenamiento de datos y la pasa a un Canvas de destino. Los pasos en Canvas pueden incluir opcionalmente campos de personalización que no persisten en los perfiles de usuario Braze.

#### Variables contextuales de Canvas para las rutas de audiencia y los pasos para la división de decisiones

{% multi_lang_include release_type.md release="Early access" %}

Puedes [crear filtros de]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters) variables de contexto que utilicen variables de contexto previamente declaradas en [las rutas de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) y en los pasos para [la división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

### Desbloquear la creatividad

#### Tarjetas de reparto para correos electrónicos

Utiliza [tarjetas de ofertas]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab) para proporcionar información clave sobre las ofertas directamente en la parte superior de los cuerpos de los correos electrónicos. Esto permite a los destinatarios comprender rápidamente los detalles de la oferta y pasar a la acción.

#### Plantillas para pancartas

Cuando [compongas tu Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create), ahora puedes empezar con una plantilla en blanco, utilizar una plantilla Braze o seleccionar una plantilla de Banner guardada.

### Canales robustos

#### Listas de supresión

{% multi_lang_include release_type.md release="General availability" %}
 
Las listas de supresión especifican grupos de usuarios que nunca recibirán mensajes. Los administradores pueden crear listas de supresión con filtros de segmento para acotar un grupo de usuarios del mismo modo que lo harías para la segmentación.

#### Seguimiento de clics en LINE

{% multi_lang_include release_type.md release="General availability" %}

Cuando [el seguimiento de clics de LINE]({{site.baseurl}}/line/click_tracking/) está activado, Braze acorta automáticamente tus URL, añade mecanismos de seguimiento y registra los clics en tiempo real. Mientras que LINE ofrece datos agregados de clics, Braze proporciona información granular del usuario que es oportuna y procesable. Estos datos te permiten crear estrategias de segmentación y reorientación más específicas, como segmentar a los usuarios en función de su comportamiento al hacer clic y desencadenar mensajes en respuesta a clics concretos.

#### Filtrado de clics de bots SMS y RCS

{% multi_lang_include release_type.md release="General availability" %}

[Filtrar los clics de bots de SMS y RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/) mejora el análisis y los flujos de trabajo de las campañas al excluir los clics sospechosos de bots. Un "clic de bot" se refiere a los clics automatizados en enlaces acortados en mensajes SMS y RCS, como los de rastreadores web, previsualizaciones de enlaces de Android e iOS o software de seguridad CPaaS. Esta característica facilita la elaboración de informes precisos, la segmentación y la orquestación para captar usuarios reales.

#### Transferir números de teléfono de WhatsApp

Transfiere un número de teléfono de una cuenta de WhatsApp Business (WABA) y su grupo de suscripción asociado [de un espacio de trabajo a otro]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) dentro de Braze.

#### Mensajes de respuesta y vista previa de WhatsApp Flows

En un Canvas, puedes crear un paso en mensaje de WhatsApp que utilice un [mensaje de respuesta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) y un mensaje de flujo. También puedes seleccionar **Vista previa del** Flujo para previsualizar el Flujo directamente en Braze y confirmar que se comporta como se espera.

#### Mensajes de productos de WhatsApp

[Los mensajes de producto]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/) te permiten enviar mensajes de WhatsApp interactivos que muestran productos directamente desde tu catálogo Meta.

#### Integración de Braze y WhatsApp con un sistema externo

[Aprovecha el poder de los chatbots de IA y las entregas de agentes en vivo]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) en el canal WhatsApp para agilizar tus operaciones de atención al cliente. Automatizando las consultas rutinarias y pasando fácilmente a agentes humanos cuando sea necesario, puedes mejorar significativamente los tiempos de respuesta y mejorar la experiencia general del cliente.

### Automatización de IA y ML

#### Agentes de Braze

{% multi_lang_include release_type.md release="Beta" %}

[Los Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents/) son ayudantes potenciados por IA que puedes crear dentro de Braze. Los agentes pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas entregar experiencias del cliente más personalizadas.

### Nuevas asociaciones Braze

#### Jasper - Plantillas

La integración de [Jasper]({{site.baseurl}}/partners/jasper/) con Braze te permite agilizar la creación de contenidos y la ejecución de campañas. Con Jasper, tus equipos de marketing pueden generar textos de alta calidad y adaptados a la marca en cuestión de minutos. A continuación, Braze facilita la entrega de estos mensajes a la audiencia adecuada en el momento óptimo. Esta integración fomenta flujos de trabajo sin fisuras, reduce el esfuerzo manual e impulsa resultados de interacción más sólidos.

#### Swym - Fidelización y reorientación

[Swym]({{site.baseurl}}/partners/swym/) ayuda a las marcas de comercio electrónico a captar la intención de compra con listas de deseos, guardar para más tarde, registro de regalos y alertas de existencias. Utilizando datos ricos y basados en permisos, puedes crear campañas hiperdirigidas y entregar experiencias de compra personalizadas que impulsen la interacción, aumenten las conversiones e incrementen la fidelización.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; puedes encontrar el resto de actualizaciones consultando los correspondientes registros de cambios del SDK.

- [Cordova SDK 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Actualizado el puente nativo de Android [de Braze Android SDK 37.0.0 a 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - La GradlePluginKotlinVersion mínima requerida es ahora 2.1.0.
    - Actualizado el puente nativo de iOS [de Braze Swift SDK 12.0.0 a 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Esto incluye la compatibilidad con Xcode 26.
    - Elimina la compatibilidad con la fuente de noticias. Se han eliminado las siguientes API:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [SDK de React Native 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Actualiza los enlaces de la versión nativa de Android [SDK de Braze Android SDK 37.0.0 a 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Elimina la compatibilidad con la fuente de noticias. Se han eliminado las siguientes API:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [SDK Web 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [SDK de Flutter 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [SDK de Unity 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Actualizado el puente nativo de iOS [de Braze Swift SDK 12.0.0 a 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Esto incluye la compatibilidad con Xcode 26.

{% enddetails %}
{% details September 16, 2025 %}

## Liberación el 16 de septiembre de 2025

### Flexibilidad de los datos

#### Plataforma de datos Braze

La plataforma de datos Braze es un conjunto completo y componible de capacidades de datos e integraciones de socios que te permite crear experiencias personalizadas e impactantes a lo largo del ciclo de vida del cliente. Obtén más información sobre los tres trabajos relacionados con los datos que hay que realizar: 

- [Unificación de datos]({{site.baseurl}}/user_guide/data/unification)
- Activación de datos
- [Distribución de datos]({{site.baseurl}}/user_guide/data/distribution)

#### Propiedades personalizadas del Banner

{% multi_lang_include release_type.md release="Early access" %}

Puedes utilizar propiedades personalizadas de tu campaña de Banner para recuperar datos clave-valor a través del SDK y modificar el comportamiento o la apariencia de tu aplicación. Para saber más, consulta [Propiedades personalizadas del Banner]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Autenticación por token

{% multi_lang_include release_type.md release="General availability" %}

Al utilizar Braze Connected Content, es posible que determinadas API requieran un token en lugar de un nombre de usuario y una contraseña. Braze puede almacenar credenciales que contengan [valores de encabezado de autenticación de token]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication).

#### Códigos de promoción

Puedes guardar códigos promocionales en el perfil de un usuario mediante un paso de Actualización de usuario. Para más información, consulta [Guardar códigos promocionales en perfiles de usuario]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile).

### Desbloquear la creatividad

#### Piloto Braze

[Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot) es una aplicación disponible públicamente para Android e iOS que te permite lanzar mensajes desde tu panel Braze a tu teléfono. Echa un vistazo a [Cómo empezar con Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started) para ver cómo descargar la aplicación, iniciar la conexión con tu panel Braze y completar la configuración.

### Nuevas asociaciones Braze

#### Blings - Contenidos visuales e interactivos

[Blings]({{site.baseurl}}/partners/blings/) es una plataforma de vídeo personalizado de nueva generación que te habilita para entregar experiencias de vídeo en tiempo real, interactivas y basadas en datos a través de canales a escala.

#### Integración estándar de Shopify con herramienta de terceros

Para las tiendas online de Shopify, recomendamos utilizar el método de integración estándar de Braze para admitir los SDK de Braze en tu sitio.

Sin embargo, entendemos que tal vez prefieras utilizar una herramienta de terceros, como Google Tag Manager, por lo que hemos elaborado una guía sobre cómo hacerlo. Para empezar, consulta [Shopify: Etiquetado de terceros]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de Flutter de Braze 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Actualiza el puente nativo de Android desde Braze Android SDK `36.0.0` a `39.0.0`.
    - Actualiza el puente nativo de iOS de Braze Swift SDK `12.0.0` a `13.2.0`. Esto incluye la compatibilidad con Xcode 26.

- [SDK Swift de Braze 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Actualiza los enlaces del SDK Swift de Braze para que requieran versiones de la denominación `13.0.0+` SemVer. Esto permite la compatibilidad con cualquier versión del SDK de Braze desde `13.0.0` hasta, pero sin incluir, `14.0.0`.

{% enddetails %}
{% details August 19, 2025 %}

## Liberación el 19 de agosto de 2025

### Normalización de la coherencia horaria con el contexto Canvas

{% multi_lang_include release_type.md release="Early access" %}

Si participas en el [acceso anticipado al paso Contexto de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), todas las marcas de tiempo con un tipo de fecha/hora de las propiedades del evento desencadenante en los Lienzos basados en acciones se normalizarán siempre a [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Para saber más sobre esto, consulta [Normalización de la coherencia horaria]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization).

### Flexibilidad de los datos

#### Dominios personalizados en autogestión

{% multi_lang_include release_type.md release="General access" %}

[Los dominios personalizados de autoservicio]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) te permiten configurar y gestionar tus propios dominios personalizados para SMS, RCS y WhatsApp, directamente desde tu panel Braze. Puedes añadir, supervisar y gestionar fácilmente hasta 10 dominios personalizados en un solo lugar.

#### Estadísticas del embudo del segmento

Selecciona [Ver estadísticas del embudo]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics) para mostrar las estadísticas de ese grupo de filtros y ver cómo afecta cada filtro añadido a tus estadísticas de segmento. Verás un recuento estimado y el porcentaje de usuarios a los que se dirigen todos los filtros hasta ese momento. Una vez mostradas las estadísticas de un grupo de filtros, se actualizarán automáticamente cada vez que cambies los filtros. 

#### Nuevos campos de respuesta para `/campaigns/details` endpoint para notificaciones push

La respuesta `messages` para notificaciones push incluye ahora dos nuevos campos:

- `image_url`: Una URL de imagen para una imagen de notificación de Android, una imagen de notificación de iOS o una imagen de icono push web.
- `large_image_url`: Una URL de imagen de notificación web para las acciones push web de Android Chrome y Windows.

#### Definición de los campos PII

Seleccionar y [definir determinados campos como campos PII]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) sólo afecta a lo que los Usuarios pueden ver en el panel Braze y no afecta a cómo se gestionan los datos del Usuario final en dichos campos PII.

Consulta a tu equipo jurídico para alinear la configuración de tu panel con las normativas y políticas de privacidad aplicables a tu empresa, incluidas las relacionadas con la [retención de datos]({{site.baseurl}}/api/data_retention/).

#### Compartir un enlace de descarga del Generador de informes

Puedes [compartir un enlace del panel]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) al informe seleccionando **Compartir** y, a continuación, **Compartir un enlace** o **Enviar o programar un correo electrónico**.

### Desbloquear la creatividad

#### Etiquetas de encabezado personalizadas para arrastrar y soltar correos electrónicos

Utiliza las etiquetas `<head>` para añadir CSS y metadatos en tu mensaje de correo electrónico. Por ejemplo, puedes utilizar estas etiquetas para añadir una hoja de estilos o un favicon. Liquid es compatible con las etiquetas `<head>`.

### Canales robustos

#### Mejores prácticas de salida difusa

Hemos añadido una [sección de buenas prácticas]({{site.baseurl}}) para ayudarte a configurar cuidadosamente tu mensaje de exclusión difusa y crear una experiencia clara, conforme y positiva para tus suscriptores.

#### WhatsApp Flows

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) es una mejora del canal de mensajería de WhatsApp existente, que te permite crear experiencias de mensajería interactivas y dinámicas. 

#### Preguntas sobre productos entrantes de WhatsApp

Los usuarios pueden responder a tu mensaje de producto o catálogo con [preguntas sobre el producto]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions). Éstos llegan como mensajes entrantes, que pueden clasificarse con una Ruta de acción.

Además, Braze extrae el ID de producto y el ID de catálogo de estas preguntas, por lo que si deseas automatizar las respuestas o enviar preguntas a otro equipo (como el de atención al cliente), puedes incluir esos datos.

### Automatización de IA y ML

#### Nuevos artículos sobre casos de uso de BrazeAI

Hemos añadido nuevos artículos sobre casos de uso para ayudarte a sacar el máximo partido de BrazeAI™. Estas guías destacan formas prácticas de aplicar la IA a tus estrategias de interacción, entre ellas:

- Predictive Churn Identifica a los clientes en riesgo de abandono y actúa con prontitud.
- Eventos predecibles Anticipa las acciones clave de los usuarios y da forma a las experiencias en tiempo real.
- [Recomendaciones]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): Entrega contenidos y productos más relevantes en función del comportamiento del cliente.

#### Servidor MCP

{% multi_lang_include release_type.md release="Beta" %}

El [servidor Braze MCP]({{site.baseurl}}/user_guide/brazeai/mcp_server/), una conexión segura y de sólo lectura, permite a herramientas de IA como Claude y Cursor acceder a datos Braze no PII para responder preguntas, analizar tendencias y proporcionar información sin alterar los datos.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de Swift 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Amplía la funcionalidad de `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` para que se desencadene en caso de errores de autenticación "Opcional".
        - El método delegado `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` se desencadenará ahora para los errores de autenticación "Obligatorio" y "Opcional".
        - Si sólo quieres gestionar errores de autenticación SDK "requeridos", añade una comprobación que asegure que `BrazeSDKAuthError.optional` es falso dentro de tu implementación de este método delegado.
    - Corrige el uso de `Braze.Configuration.sdkAuthentication` para que surta efecto cuando esté habilitado.
        - Antes, el SDK no consumía el valor de esta configuración y el token siempre se adjuntaba a las solicitudes si estaba presente.
        - Ahora, el SDK sólo adjuntará el token de autenticación SDK a las solicitudes de red salientes cuando esta configuración esté habilitada.
    - Los definidores de todas las propiedades de `Braze.FeatureFlag` y de todas las propiedades de `Braze.Banner` se han convertido en `private`. Las propiedades de estas clases son ahora de sólo lectura.
    - Elimina la propiedad `Braze.Banner.id`, que quedó obsoleta en la versión `11.4.0`.
        - En su lugar, utiliza `Braze.Banner.trackingId` para leer el ID de seguimiento de campaña de un banner.
- [SDK de React Native 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Actualiza los enlaces de la versión nativa de Android SDK de [Braze Android SDK 36.0.0 a 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualiza los enlaces de la versión nativa del SDK [Swift de Braze Swift SDK 12.0.0 a 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - El evento `sdkAuthenticationError` se desencadenará ahora para los errores de autenticación "Obligatorio" y "Opcional".
- [SDK de Xamarin 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Se ha añadido compatibilidad con .NET 9.0 para los enlaces de iOS y Android.
        - Esto elimina la compatibilidad con .NET 8.0.
        - Esto requiere una [versión mínima de iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0).
    - Actualizado el enlace Android de [Braze Android 32.0.0 a 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el enlace iOS de [Braze Swift SDK 10.0.0 a 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Esta versión contiene API para la característica Banners, pero actualmente no es totalmente compatible con este SDK. Si deseas utilizar Banners en tu aplicación .NET MAUI, ponte en contacto con tu administrador de atención al cliente antes de integrarlos en tu aplicación.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Se ha actualizado la implementación interna de iOS del método `enableSdk` para utilizar `setEnabled`: en lugar de `_requestEnableSDKOnNextAppRun`, que estaba obsoleto en el SDK de Swift.
    - Llamar a este método ya no requiere relanzar la aplicación para que surta efecto. El SDK quedará habilitado en cuanto se ejecute este método.
    - Actualizado el puente nativo de Android desde [Braze Android SDK `36.0.0` a `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

{% enddetails %}
{% details July 22, 2025 %}

## Liberación el 22 de julio de 2025

### Exportación de eventos de seguridad con Amazon S3

Puedes [exportar]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/) automáticamente [los Eventos de Seguridad a Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/), un proveedor de almacenamiento en la nube, con una tarea diaria que se ejecuta a medianoche UTC. Una vez configurado, no necesitas exportar manualmente los Eventos de seguridad desde el panel.

### Flexibilidad de los datos

#### Importación CSV

{% multi_lang_include release_type.md release="General availability" %}

Puedes utilizar la importación de usuarios en CSV para registrar y actualizar atributos de usuario y eventos personalizados en Braze como `first_name`, `last_destination_searched` y `trip_booked`. Para empezar, consulta [Importación de CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### Alertas de uso de la API

{% multi_lang_include release_type.md release="General availability" %}

Las alertas de uso de la API proporcionan una visibilidad crítica del uso de tu API, permitiéndote detectar proactivamente el tráfico inesperado. Al configurar estas alertas para hacer un seguimiento de los volúmenes de solicitudes de API clave, puedes recibir notificaciones en tiempo real y abordar los problemas antes de que afecten a tus campañas de marketing.

#### Límites de velocidad de la API del espacio de trabajo

Con los límites de velocidad de la API del espacio de trabajo, puedes establecer un número máximo de solicitudes de API que un espacio de trabajo puede hacer a un punto final de ingesta específico, como `/users/track` o los datos del SDK. También puedes aplicar límites de velocidad a un grupo de espacios de trabajo, lo que significa que el límite se comparte entre todos los espacios de trabajo de ese grupo.

#### Eventos de New Currents

Estos nuevos acontecimientos se han añadido al glosario de Currents:

- [Banner Abortar eventos]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Banner Eventos de clic]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Eventos de impresión de banners]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [Banner Eventos vistos]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Eventos de fallo del webhook]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### Intervalo de tiempo predeterminado para los análisis de campaña

Por predeterminado, el intervalo de tiempo para [**Análisis de campaña**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) mostrará los últimos 90 días desde la hora actual. Esto significa que si la campaña se lanzó hace más de 90 días, el análisis se mostrará como "0" para el intervalo de tiempo dado. Para ver todos los análisis de las campañas más antiguas, ajusta el intervalo de tiempo del informe.

#### Comportamiento actualizado para el paso de rutas de experimentos en Canvas

Si tu Canvas tiene un [experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) activo o en curso y actualizas el Canvas activo (aunque no sea al paso Ruta de experimentos), el experimento en curso finalizará. Para reiniciar el experimento, puedes desconectar la Ruta de experimentos existente y lanzar una nueva, o duplicar el Canvas y lanzar un nuevo Canvas. 

Para más información, consulta [Editar Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits/).

#### Límite de velocidad más rápido disponible para el punto final `/users/export/ids` 

También puedes aumentar el [límite de velocidad del endpoint /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) a 40 peticiones por segundo cumpliendo los siguientes requisitos:

- Tu espacio de trabajo tiene habilitado el límite de velocidad predeterminado (250 peticiones por minuto). Ponte en contacto con tu administrador de cuentas Braze para que te ayude a eliminar cualquier límite de velocidad preexistente que puedas tener.
- Tu solicitud incluye el parámetro fields_to_export para enumerar todos los campos que quieres recibir.

#### Nueva traducción para los puntos finales de las plantillas de correo electrónico

{% multi_lang_include release_type.md release="Early access" %}

Utiliza estos puntos finales para ver y actualizar las traducciones y localizaciones de las plantillas de correo electrónico:

- [GET: Ver las traducciones originales]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [GET: Ver una traducción y localización específicas para el punto final de la plantilla de correo electrónico]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_locale_template)
- [GET: Ver todas las traducciones y localizaciones de una plantilla de correo electrónico]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_template)
- [PUT: Actualizar las traducciones de una plantilla de correo electrónico]({{site.baseurl}}/api/endpoints/translations/email_templates/put_update_template)

### Desbloquear la creatividad

#### Páginas de destino

Puedes hacer que tu página de destino [sea receptiva al tamaño del dispositivo del usuario]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) apilando verticalmente las columnas en las pantallas más pequeñas. Para habilitarlo, añade una columna a la fila que quieras hacer receptiva y, a continuación, alterna la opción **Apilar verticalmente en pantallas pequeñas** en la sección **Personalizar columnas**.

### Canales robustos

#### Bot para filtrar correos electrónicos

{% multi_lang_include release_type.md release="General availability" %}

Configura el filtrado de bots en tus [Preferencias de correo electrónico]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) para excluir todos los clics sospechosos de máquina o bot. Un "clic de bot" en correo electrónico se refiere a un clic en hipervínculos dentro de un correo electrónico generado por un programa automatizado. Al filtrar estos clics de bot, puedes desencadenar y entregar mensajes intencionadamente a destinatarios que estén interactuando.

#### Arrastrar y soltar bloques de producto

{% multi_lang_include release_type.md release="Early access" %}

El [editor de arrastrar y soltar]({{site.baseurl}}/dnd_product_blocks/) te permite añadir y configurar rápidamente bloques de producto a tus mensajes para mostrar los productos fácilmente, sin necesidad de crear código Liquid personalizado. Actualmente, la característica de arrastrar y soltar bloques de productos sólo está disponible para el correo electrónico.

#### Texto extendido para páginas de destino y mensajes dentro de la aplicación

Extender texto te permite aplicar un estilo específico a bloques de texto sin código personalizado para tus [páginas de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) y [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks). Para ello, resalta el texto al que quieras aplicar estilo y, a continuación, selecciona **Ajustar con espacio para el estilo**. 

#### Anuncio Clic a WhatsApp

[Los anuncios que hacen clic en WhatsApp]({{site.baseurl}}/whatsapp_use_cases/) son una forma eficaz de atraer tanto a clientes nuevos como a los ya existentes a partir de Meta anuncios en Facebook, Instagram u otras plataformas. Utiliza estos anuncios para promocionar tus productos y servicios a la vez que haces que los usuarios conozcan tu presencia en WhatsApp. 

### Nuevas asociaciones Braze

#### API de visitas de Shopify - Comercio electrónico

Braze recopila información de los visitantes, como direcciones de correo electrónico y números de teléfono, a través de mensajes en el explorador. Esta información se envía a Shopify. Estos datos ayudan a los comerciantes a reconocer a los visitantes de su tienda y a crear una experiencia de compra más personalizada.

#### Okendo - Comercio electrónico

La integración de Braze y [Okendo]({{site.baseurl}}/partners/okendo/) funciona en múltiples productos de la plataforma de Okendo, incluyendo Opiniones, Fidelización, Referidos, Encuestas y Cuestionarios. Okendo envía eventos personalizados y atributos del usuario a Braze, que pueden utilizarse para personalizar y desencadenar mensajes.

#### Lemnisk - Plataforma de datos de los clientes

La integración de Braze y [Lemnisk]({{site.baseurl}}/partners/lemnisk/) permite a las marcas y empresas liberar todo el potencial de Braze actuando como una capa de inteligencia dirigida por CDP que unifica los datos de usuario en todas las plataformas en tiempo real, y enviando la información y los comportamientos del usuario recopilados a Braze en tiempo real.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK Web 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Se han suprimido la propiedad `Banner.html`, y los métodos `logBannerClick` y `logBannerImpressions`. En su lugar, utiliza [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) que gestiona automáticamente el seguimiento de impresiones y clics.
    - Se ha eliminado la compatibilidad con la característica de fuente de noticias heredada. Esto incluye la eliminación de la clase Fuente y sus métodos asociados.
    - Los campos creados y categorías que utilizaban las tarjetas de canal de noticias heredadas se han eliminado de las [`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) subclases.
    - También se ha eliminado el campo linkText de la subclase [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) subclase Tarjeta y de su constructor.
    - Se han aclarado las definiciones y se han actualizado los tipos para tomar nota de que algunos métodos del SDK devuelven explícitamente un valor indefinido cuando el SDK no está inicializado, alineando los tipos con el comportamiento real en tiempo de ejecución. Esto podría introducir nuevos errores de TypeScript en los proyectos que se basaban en las tipificaciones anteriores (incompletas).
    - Las imágenes de los mensajes dentro de la aplicación con `cropType` de `CENTER_CROP` (como `FullScreenMessage` por predeterminado) se muestran ahora mediante una etiqueta `<img>` en lugar de `<span>` para mejorar la accesibilidad. Esto puede romper las personalizaciones CSS existentes para la clase `.ab-center-cropped-img` o sus hijos.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Se ha actualizado la implementación interna en iOS del método `enableSdk` para utilizar setEnabled: en lugar de `_requestEnableSDKOnNextAppRun`, que estaba obsoleto en el SDK de Swift.
        - Llamar a este método ya no requiere relanzar la aplicación para que surta efecto. El SDK quedará habilitado en cuanto se ejecute este método.
    - Actualizado el puente nativo de Android [de Braze Android SDK 36.0.0 a 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Android SDK 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [SDK de Swift 12.0.1-12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
{% details June 24, 2025 %}

## Liberación el 24 de junio de 2025

### BrazeAI Decisioning Studio™

BrazeAI Decisioning [Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) sustituye las pruebas A/B por la toma de decisiones con IA que lo personaliza todo y maximiza cualquier métrica: impulsa los dólares, no los clics: con BrazeAI Decisioning Studio™, puedes optimizar cualquier KPI empresarial. Consulta nuestra sección dedicada [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) para ver ejemplos de casos de uso y características clave.

### Nuevos tutoriales del SDK

Cada tutorial del SDK de Braze ofrece instrucciones paso a paso junto con un código de muestra completo. Elige un tutorial a continuación para empezar:

- [Mostrar pancartas]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Personalización del estilo de los mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [Visualización condicional de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [Aplazar mensajes desencadenados dentro de la aplicación]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### Flexibilidad de los datos

#### Aprovisionamiento justo a tiempo SAML

{% multi_lang_include release_type.md release="General availability" %}

Utiliza [el aprovisionamiento justo a tiempo SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit) para permitir que los nuevos usuarios del panel creen una cuenta Braze en su primer inicio de sesión. Esto elimina la necesidad de que los administradores creen manualmente una cuenta para un nuevo usuario del cuadro de mandos, elijan sus permisos, lo asignen a un espacio de trabajo y esperen a que active su cuenta.

#### Filtros por selección

Ahora puedes añadir hasta 10 filtros por [selección]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections).

#### Almacenamiento de catálogos

El tamaño de almacenamiento para la versión gratuita de los catálogos es de hasta 100 MB. Puedes tener un número ilimitado de artículos siempre que no superen los 100 MB.

#### Número de filas sincronizadas con la ingesta de datos en la nube

Por defecto, para la Ingesta de datos en la nube, cada ejecución puede sincronizar hasta 500 millones de filas. Se detendrá cualquier sincronización con más de 500 millones de filas nuevas.

Consulta las [limitaciones del producto Ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/#product-limitations) para obtener más detalles.

### Canales robustos

#### Pruebas de accesibilidad en Inbox Vision

{% multi_lang_include release_type.md release="General availability" %}

Utiliza [las pruebas de accesibilidad]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) de Inbox Vision para resaltar los problemas de accesibilidad que puedan existir en tu correo electrónico. 

Las pruebas de accesibilidad analizan el contenido de tu correo electrónico en función de algunos requisitos de [las Pautas de Accesibilidad al Contenido en la Web](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA. Esto puede proporcionar información sobre qué elementos no cumplen las normas de accesibilidad.

#### Seguimiento de clics para WhatsApp

{% multi_lang_include release_type.md release="General availability" %}

Puedes activar [el seguimiento de clics]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking) tanto en los mensajes de respuesta como en los de plantilla para ver los datos de clics en tus informes de rendimiento de WhatsApp y poder segmentar a los usuarios en función de quién hizo clic en qué.

#### Vídeos para WhatsApp

{% multi_lang_include release_type.md release="General availability" %}

Puedes [incrustar videos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features) en el cuerpo del texto de los mensajes salientes de WhatsApp. Estos archivos deben estar alojados a través de URL o en la [biblioteca multimedia de Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library).

### Nuevas asociaciones Braze

#### Stripe - Comercio electrónico

La integración de Braze y [Stripe]({{site.baseurl}}/partners/stripe) te permite desencadenar mensajería en Braze basada en eventos de Stripe, como inicio de prueba, suscripción activada, cancelación de suscripción, etc.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de React Native 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [SDK de Flutter 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - Actualizado el puente nativo de Android [de Braze Android SDK 35.0.0 a 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualizado el puente nativo de iOS [de Braze Swift SDK 11.6.1 a 12.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Segmento Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Actualizado el SDK para Android de Braze [de 35.0.0 a 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

{% enddetails %}
{% details May 27, 2025 %}

## Liberación el 27 de mayo de 2025

### Flexibilidad de los datos

#### Copiar lienzos en distintos espacios de trabajo

{% multi_lang_include release_type.md release="General availability" %}

Ahora puedes copiar Lienzos entre espacios de trabajo. Esto te permite poner en marcha la composición de tu mensaje empezando con una copia de un Canvas en un espacio de trabajo diferente. Para más información sobre lo que se copia, consulta [Copiar campañas y lienzos entre espacios de trabajo]({{site.baseurl}}/copying_to_workspaces/).

#### Reglas de mensajería para el flujo de trabajo de aprobación 

{% multi_lang_include release_type.md release="General availability" %}

Utiliza [reglas de mensajería]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules) en tu flujo de trabajo de aprobación para limitar el número de usuarios alcanzables antes de que se requiera una aprobación adicional; de este modo, puedes revisar tus campañas y Canvases antes de dirigirte a una audiencia mayor.

#### Diagramas de relación de entidades para Snowflake y Braze

A principios de este año, creamos tablas de relaciones de entidades para los datos compartidos entre Snowflake y Braze. Este mes, hemos añadido [nuevos diagramas interactivos]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/) en los que puedes desplazarte, agarrar y hacer zoom en los detalles de cada tabla, dándote una mejor idea de cómo interactúan tus datos con Braze.

### Desbloquear la creatividad

#### Eventos recomendados

{% multi_lang_include release_type.md release="Early access" %}

[Los eventos recomendados]({{site.baseurl}}/user_guide/data/custom_data/recommended_events) se corresponden con los casos de uso más comunes del comercio electrónico. Al utilizar eventos recomendados, puedes desbloquear plantillas Canvas preconstruidas, paneles de informes mapeados según el ciclo de vida del cliente y mucho más.

### Canales robustos

#### Canal de pancartas

{% multi_lang_include release_type.md release="General availability" %}

Con [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners), puedes crear mensajes personalizados para tus usuarios, a la vez que amplías el alcance de tus otros canales, como el correo electrónico o las notificaciones push. Puedes incrustar banners directamente en tu aplicación o sitio web, lo que te permite interactuar con los usuarios a través de una experiencia natural.

#### Canal de Servicios de Comunicación Enriquecidos (RCS)

{% multi_lang_include release_type.md release="General availability" %}

[Los Servicios de Comunicación Enriquecidos (RCS)]({{site.baseurl}}/about_rcs/) mejoran los SMS tradicionales, habilitando a las marcas para entregar mensajes no sólo informativos, sino también mucho más interactivos. Ahora compatible tanto con Android como con iOS, RCS aporta características como medios de alta calidad, botones interactivos y perfiles de remitente de marca directamente en las aplicaciones de mensajería preinstaladas de los usuarios, eliminando la necesidad de descargar una aplicación aparte.

#### Página de configuración push

{% multi_lang_include release_type.md release="General availability" %}

Utiliza [la página de**Configuración push**]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings) para configurar los ajustes clave de tus notificaciones push, incluido el Tiempo de vida push (TTL) y la prioridad predeterminada del FCM para las campañas de Android. Estas configuraciones ayudan a optimizar la entrega y la eficacia de tus notificaciones push, garantizando una mejor experiencia a tus usuarios.

#### Códigos promocionales para campañas de mensajes dentro de la aplicación

{% multi_lang_include release_type.md release="Early access" %}

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
    - Esta versión revierte el aumento de la versión mínima del SDK de Android de Braze de la API 21 a la API 25 introducido en la versión 34.0.0. Esto permite volver a compilar el SDK en aplicaciones compatibles con la API 21. Ten en cuenta que, aunque estamos reintroduciendo la capacidad de compilar, no estamos reintroduciendo la compatibilidad formal con la API 25 de <, y no podemos garantizar que el SDK funcione según lo previsto en dispositivos que ejecuten esas versiones.
    - Si tu aplicación es compatible con esas versiones, deberías hacerlo:
        - Valida que tu integración del SDK funciona según lo previsto en dispositivos físicos (no sólo emuladores) para esas versiones de la API.
        - Si no puedes validar el comportamiento esperado, debes llamar a [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) o no inicializar el SDK en esas versiones. De lo contrario, podrías causar efectos secundarios no deseados o degradar el rendimiento de los dispositivos de tus usuarios finales.
    - Se ha solucionado un problema por el que los mensajes dentro de la aplicación provocaban una lectura en el hilo principal.
    `BrazeInAppMessageManager.displayInAppMessage` es ahora una función de suspensión de Kotlin.
        - Si no llamas directamente a esta función, no necesitas hacer ningún cambio.
    - La lista de materiales de AndroidX Compose se ha actualizado a 2025.04.01 para gestionar las actualizaciones de las API de Jetpack Compose.
- [SDK de React Native 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Actualiza el puente nativo de Android de Braze Android SDK 35.0.0 a 36.0.0
    - Actualiza los enlaces de la versión nativa de iOS de Braze Swift SDK 11.9.0 a 12.0.0.
    - Actualiza la representación unitaria de PushNotificationEvent.timestamp a milisegundos en iOS.
        - Antes, este valor se representaba en segundos en iOS. Ahora coincidirá con la implementación existente de Android.
- [SDK Web 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [SDK de Flutter 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - Esta versión revierte el aumento de la versión mínima del SDK de Android de Braze de la API 21 a la API 25 introducido en la versión 34.0.0. Esto permite volver a compilar el SDK en aplicaciones compatibles con la API 21. Sin embargo, no vamos a reintroducir la compatibilidad formal con la API 25 de <. Lee más [aquí](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600).
    - Actualiza el puente nativo de Android de Braze Android SDK 35.0.0 a 36.0.0
    - Actualiza el puente nativo de iOS de Braze Swift SDK 11.9.0 a 12.0.0

{% enddetails %}
