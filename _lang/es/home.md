---
nav_title: Inicio
article_title: Novedades de Braze
description: "Las notas de la versión de Braze se publican mensualmente para que puedas mantenerte al día sobre los principales lanzamientos de productos, las mejoras continuas de los productos, las asociaciones de Braze, los cambios importantes en el SDK y las características obsoletas."
page_order: 0
search_rank: 1
page_type: reference

---

# Novedades de Braze

{% alert tip %}
Para obtener más información sobre cualquiera de las actualizaciones que figuran en esta página, ponte en contacto con tu director de cuentas o [abre un ticket de soporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Consulta nuestros [registros de cambios del SDK]({{site.baseurl}}/developer_guide/changelogs) para obtener más información sobre las versiones mensuales del SDK, las mejoras y los cambios importantes.
{% endalert %}

{% details March 5, 2026 %}

## Lanzamiento el 5 de marzo de 2026.

### Informes de& datos

#### Nuevo centro de datos

{% multi_lang_include release_type.md release="General availability" %}

Braze ha lanzado un nuevo [centro de datos]({{site.baseurl}}/user_guide/data/data_centers/): JP-01. Puedes registrarte en centros de datos específicos de cada región al configurar tu cuenta de Braze.

#### Variables de contexto

{% multi_lang_include release_type.md release="General availability" %}

[Las variables de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) son datos temporales que puedes crear y utilizar durante el recorrido de un usuario por un Canvas específico. Cada vez que un usuario accede al Canvas, incluso si ya ha accedido anteriormente, las variables de contexto se redefinirán en función de las últimas entradas realizadas y de la configuración del Canvas. Este enfoque permite que cada entrada de Canvas mantenga su propio contexto independiente, lo que permite a los usuarios tener múltiples estados activos dentro del mismo recorrido, al tiempo que se conserva el contexto específico de cada estado.

#### Fuentes de ingesta de datos en la nube

{% multi_lang_include release_type.md release="Early access" %}

[La ingesta de datos]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze) tiene una nueva interfaz de usuario que separa los orígenes de datos de las sincronizaciones, lo que te permite reutilizar un solo origen de datos en cualquier número de sincronizaciones. Esto reduce la configuración duplicada y simplifica la configuración cuando tienes varias sincronizaciones. Si ya tienes sincronizaciones, estas se realizarán automáticamente en la nueva estructura de fuentes y sincronizaciones sin tiempo de inactividad. Para empezar, ve a **Ingesta de datos en la nube** > **Orígenes** para ver, editar o crear orígenes y, a continuación, selecciona un origen en el menú desplegable al crear una sincronización.

#### Campos adicionales para eventos de Currents y Data Share

{% multi_lang_include release_type.md release="General availability" %}

[Los eventos de Currents y Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) ahora incluyen los siguientes campos nuevos para ampliar los datos disponibles para los sistemas de análisis y posteriores:

- `agentconsole.AgentExecuted`: Añadido`error`  (cadena): descripción de cualquier error que se haya producido.
- `agentconsole.ToolInvocation`: Añadido`request_id`  (cadena): un ID único para la solicitud LLM global y la ejecución completa.
- `users.messages.rcs.InboundReceive`: Añadido`canvas_variation_name`  (cadena): el nombre de la variante de Canvas que ha recibido el usuario.

#### Campos de campaña y Canvas para Snowflake Data Share

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3) ahora incluye campos adicionales que reflejan la información de campaña y Canvas en 66 tablas existentes, entre las que se incluyen:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### Validación previa a la importación de CSV e informe de errores

{% multi_lang_include release_type.md release="General availability" %}

[Las importaciones de usuarios en CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import) ahora admiten la validación previa a la importación y la generación de informes detallados de errores. Antes de importar, selecciona **Validar archivo antes de importar** en la página **Importar usuarios**: Braze analizará tu archivo y generará un informe en el que se identificarán las filas que fallarán por completo (errores) y las filas que se importarán correctamente, pero con algunos valores omitidos (advertencias). Puedes descargar el informe, corregir tu CSV y volver a subirlo, o continuar tal y como está. Una vez completada la importación, también se puede descargar un informe con las filas que han fallado, incluyendo el motivo exacto de cada problema.

#### Panel de diagnóstico de mensajería

{% multi_lang_include release_type.md release="Early access" %}

El [panel de diagnóstico de]({{site.baseurl}}/user_guide/analytics/dashboard/diagnostics_dashboard) [mensajería]({{site.baseurl}}/user_guide/analytics/dashboard/diagnostics_dashboard) proporciona un desglose de alto nivel de los resultados del envío de mensajes, lo que te permite detectar tendencias y diagnosticar posibles problemas en tu configuración de mensajería. Este panel te puede ayudar a comprender por qué los mensajes de tus campañas o Canvases pueden no haberse enviado como se esperaba.

### BrazeAI<sup>TM</sup>

#### Agentes de Braze en la consola de agentes

{% multi_lang_include release_type.md release="General availability" %}

[Los agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/) son asistentes basados en inteligencia artificial que puedes crear dentro de Braze. Los agentes pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas entregar experiencias del cliente más personalizadas. Cuando creas un agente, defines su propósito y estableces las pautas sobre cómo debe comportarse. Una vez que esté en vivo, el agente se puede [implementar]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents) en Braze para generar copias de personalización, tomar decisiones en tiempo real o actualizar campos del catálogo.

### Orquestación

#### Permisos de usuario granulares

{% multi_lang_include release_type.md release="Early access" %}

Braze presenta [los permisos granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/), una forma más flexible de administrar el acceso de los usuarios. Consulta [Migración a permisos granulares]({{site.baseurl}}/granular_permissions_migration/) para obtener más información sobre el proceso de migración, incluida la forma en que los permisos heredados están mapeados con los permisos granulares.

#### Límite de velocidad basado en canales

{% multi_lang_include release_type.md release="General availability" %}

Al establecer un límite de velocidad de entrega para una campaña multicanal o Canvas, puedes elegir entre establecer un límite compartido o un [límite basado en el canal]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#multichannel-campaigns-and-canvases). Cuando una campaña multicanal o Canvas utiliza la limitación de velocidad basada en canales, el límite de velocidad se aplica a cada uno de los canales seleccionados. Por ejemplo, puedes configurar tu campaña o Canvas para enviar un máximo de 5000 webhooks y 2500 mensajes SMS por minuto en toda la campaña o Canvas.

#### Paso en Canvas del contexto del lienzo

{% multi_lang_include release_type.md release="General availability" %}

[Los pasos en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) te permiten crear y actualizar una o más variables para un usuario a medida que avanza por un Canvas. Por ejemplo, si tienes un Canvas que administra descuentos de temporada, puedes utilizar una variable de contexto para almacenar un código de descuento diferente cada vez que un usuario entra en el Canvas.

### Canales&  Puntos de intervención

#### Traducir configuraciones regionales en bloques de contenido

{% multi_lang_include release_type.md release="Early access" %}

Después de añadir configuraciones regionales a tu espacio de trabajo, puedes [dirigirte a usuarios en diferentes idiomas,]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) todo ello dentro de un bloque de contenido.

### Asociación

#### Algolia: recomendaciones de búsqueda

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia) es una plataforma de búsqueda y descubrimiento que ayuda a los desarrolladores a crear experiencias de búsqueda rápidas, relevantes y escalables. Con un potente enfoque basado en API, Algolia combina algoritmos de clasificación avanzados con información basada en inteligencia artificial para ofrecer una búsqueda fácil en el sitio, navegación y descubrimiento de contenido personalizado.

#### Anthropic: proveedor de modelos de IA

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic) es una empresa dedicada a la seguridad y la investigación en inteligencia artificial que desarrolla Claude, un asistente de IA de última generación diseñado para ser útil, honesto y seguro en una amplia gama de tareas lingüísticas.

#### Canva - Personalización de mensajes - Estudio creativo

[Canva]({{site.baseurl}}/partners/canva) sincroniza tus imágenes en Canva directamente con la biblioteca multimedia de Braze, lo que agiliza tu flujo de trabajo creativo y mantiene tus activos visuales actualizados en todos tus canales de mensajería.

#### DOTS.ECO \- Recompensas

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) te permite proporcionar recompensas a los usuarios basadas en el impacto medioambiental real a través de certificados digitales rastreables. Cada certificado puede incluir metadatos como una URL compartible del certificado y una URL de la imagen, para que los usuarios puedan ver (y volver a visitar) vuestra prueba de impacto.

#### Figma - Personalización de mensajes - Estudio creativo

[Figma]({{site.baseurl}}/partners/figma) es una plataforma de diseño colaborativo que te permite crear, diseñar y desarrollar prototipos de productos. Utiliza esta integración para enviar imágenes y activos visuales desde Figma directamente a la biblioteca multimedia de Braze.

#### Flybuy - Personalización de mensajes - Ubicación

[Flybuy,]({{site.baseurl}}/partners/message_personalization/location/flybuy) de Radius Networks, es la plataforma de ubicación omnicanal líder que aprovecha la tecnología impulsada por IA para optimizar la velocidad del servicio en la recogida, la entrega, el servicio de autoservicio y el servicio en mesa. A través de su línea de productos de marketing integrado, Flybuy también habilita a las marcas para entregar mensajes hiperpersonalizados y basados en el momento, lo que ayuda a impulsar la interacción, aumentar el tamaño de los cheques y respaldar iniciativas de fidelización más amplias.

#### Google Gemini: proveedor de modelos de IA

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini) es la familia de modelos de inteligencia artificial de Google que combina razonamiento avanzado en texto, código e imágenes para ayudar a las marcas a entregar experiencias más inteligentes y personalizadas.

#### Limbik - Personalización de mensajes - Motores de personalización

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik) es tu capa de resonancia de IA: realiza predicciones sobre cómo interpretan y responden las audiencias reales a los mensajes, conceptos y resultados de IA antes de que lleguen al mercado. Gracias a una investigación primaria continua en más de 60 países y más de 25 idiomas, Limbik entrega audiencias sintéticas validadas por personas, es decir, poblaciones digitales que simulan la respuesta real de la audiencia a la velocidad de una máquina y con una precisión de nivel de investigación (95 % de confianza, margen de error del 1,5 % al 3 %). Limbik te permite asegurarte de inmediato de que tu mensajería resuene con lo que tu audiencia objetivo cree y siente.

#### Linkrunner - Orquestación de mensajes - Atribución

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner) es una plataforma móvil de atribución y análisis que te ayuda a realizar el seguimiento y el análisis de tus campañas de adquisición de usuarios.

#### Mailizio - Orquestación de mensajes - Plantillas

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio) es una plataforma de creación y administración de correos electrónicos que facilita el diseño de contenido reutilizable y seguro para la marca mediante un editor visual intuitivo. Con la integración de Mailizio en Braze, puedes exportar tus bloques de contenido y plantillas de correo electrónico, y luego generar automáticamente mensajes dentro de la aplicación a partir de esos mismos activos, lo que habilita una implementación rápida y totalmente controlada de las campañas.

#### Fidelización abierta - Datos y análisis - Fidelización

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty) es una plataforma de programas de fidelización basada en la nube que te permite crear y administrar programas de fidelización y recompensas para clientes. La integración de Braze y Open Loyalty sincroniza los datos de fidelización, como el saldo de puntos, los cambios de nivel y las advertencias de caducidad, directamente en Braze en tiempo real. Esto te permite desencadenar mensajes personalizados (correo electrónico, notificaciones push, SMS) cuando cambia el estado de fidelización de un usuario.

#### OpenAI: proveedor de modelos de IA

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai) crea modelos avanzados de IA, como GPT, que habilitan la comprensión y generación de lenguaje natural, lo que permite a las marcas crear y ampliar interacciones significativas con los clientes.

#### Shopgate - Canales

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate) es una plataforma de comercio móvil y omnicanal que ayuda a los comerciantes a crear aplicaciones de compras y a mejorar la eficiencia de las tiendas físicas mediante herramientas de cumplimiento y clienteling, es decir, atención al cliente personalizada en la tienda basada en los datos de los clientes.

#### Splio - Datos y análisis - Importación de cohortes

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio) es una herramienta para crear audiencias que te permite aumentar el número de campañas y los ingresos sin perjudicar la experiencia del cliente, y proporciona análisis para realizar el seguimiento del rendimiento de las campañas de CRM tanto online como offline.

### SDK

#### Actualizaciones importantes del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de Android 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [SDK de Flutter 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [SDK de Swift 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK de Xamarin 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Actualización del enlace Android de [Braze Android SDK 37.0.0 a 41.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Se ha actualizado el enlace iOS de [Braze SWIFT SDK 13.3.0 a 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Se han añadido nuevas dependencias transitivas de NuGet requeridas por el SDK de Braze para Android:
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib Se ha actualizado de la versión 2.0.21.3 a la 2.3.0.1. Si tu proyecto vincula explícitamente este paquete a una versión anterior, deberás actualizarlo para evitar errores de restauración.
    - Se ha eliminado la característica del canal de noticias.
        - Esta característica se eliminó del SDK nativo de Android en la versión [38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0).
        - Esta característica se eliminó del SDK nativo de SWIFT en la versión [14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0).
    - El casoBRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData de enumeración ha cambiado de nombre a BRZInAppMessageDismissalReason.WipeData.
- [Complemento Expo 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - Esta versión requiere la versión 19.0.0 del SDK Braze React Native.
    - (Android) Se ha corregido una fuga de memoria en la capa de persistencia de datos.
    - (Android) Se ha añadido compatibilidad con Braze.getInitialPushPayload() para gestionar vínculos profundos de notificaciones push cuando la aplicación se inicia desde un estado terminado. Esto resuelve un problema por el cual los vínculos profundos de las notificaciones push no se gestionaban en Android cuando la aplicación se iniciaba en frío.
- [SDK React Native 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - Actualiza los enlaces de la versión nativa del SDK de SWIFT de Braze SWIFT SDK 13.3.0 a 14.0.1.
    - Actualiza los enlaces de la versión nativa del SDK de Android de Braze Android SDK 40.0.2 a 41.0.0.

{% enddetails %}

{% details February 5, 2026 %}

## Lanzamiento el 5 de febrero de 2026

### BrazeAI<sup>TM</sup>

#### Optimizador de contenidos

{% multi_lang_include release_type.md release="Beta" %}

[Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer) es un paso en Canvas para la prueba continua de contenidos con alta variabilidad que entrega una automatización de la optimización de la interacción. Mediante una interfaz de arrastrar y soltar similar a la del paso de mensaje, define los componentes que deseas probar, genera variantes utilizando IA (o introdúcelas manualmente) y utiliza etiquetas de Liquid para realizar el mapeado de estos componentes al contenido de tu mensaje.

Basado en un optimizador multiarma no contextual, Content Optimizer envía un único mensaje por usuario y determina qué combinación de variantes de componentes entregar en función de recomendaciones predictivas. A medida que el paso recopila datos a lo largo del tiempo, las variantes de alto rendimiento aumentan naturalmente en la asignación de envíos, mientras que las variantes de bajo rendimiento disminuyen. Content Optimizer funciona mejor con lienzos de envío repetido que tienen un volumen diario constante de usuarios (al menos unos pocos miles de usuarios al día) para habilitar la optimización continua.

### Informes de& datos

#### Eventos recomendados para el comercio electrónico

{% multi_lang_include release_type.md release="Early access" %}

Para hacer coincidir los eventos recomendados para el comercio electrónico con el evento de compra existente, hemos añadido el [evento de conversión «Realizar pedido»]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report), que es similar a «Realizar compra».

### Canales&  Puntos de intervención

#### Traducir la localización regional en los banners

{% multi_lang_include release_type.md release="Early access" %}

Después de añadir configuraciones regionales a tu espacio de trabajo, [dirígete a usuarios de diferentes idiomas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales#translating-locales) con un solo banner.

#### Configura el ancho de los bloques de contenido que se pueden arrastrar y soltar.

[Ajusta el ancho de tu bloque de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) seleccionando el botón en el menú de navegación. El ancho predeterminado es 100 % cuando no se especifica en la configuración de estilo global de tu correo electrónico; de lo contrario, se respetará la configuración global.

![Una flecha de doble cara con una opción para editar la anchura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Utiliza el calentamiento automático de IP

{% multi_lang_include release_type.md release="Early access" %}

Utiliza [el calentamiento de IP automático]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/#automated-ip-warming) para aumentar gradualmente tu volumen diario de envíos, lo que permitirá a los proveedores de buzones de entrada conocer y confiar en tus patrones de envío. Braze envía primero a tus suscriptores más interactivos, lo que permite que el volumen diario crezca a un ritmo que se ajusta a las mejores prácticas.

### Asociación

#### LinkedIn – Sincronización de audiencias de Canvas

Con [Braze Audience Sync para LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/), añade datos de usuarios de tu integración de Braze a las listas de clientes de LinkedIn para entregar anuncios basados en desencadenantes de comportamiento, segmentación y mucho más. Cualquier criterio que se utilice normalmente para desencadenar un mensaje (como push, correo electrónico, SMS y webhook) en un BRAZE CANVAS basado en datos de usuario ahora puede desencadenar un anuncio para ese usuario en tus listas de clientes de LinkedIn.

#### Oracle Crowdtwist - Análisis de& datos

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist) es una solución líder en la nube para la fidelización de clientes que permite a las marcas ofrecer experiencias del cliente personalizadas. Su solución ofrece más de 100 vías de interacción listas para usar, lo que proporciona un rápido retorno de la inversión a los especialistas en marketing para que puedan desarrollar una visión más completa del cliente.

#### Fullstory - Contenido dinámico

La plataforma de datos de comportamiento [de Fullstory]({{site.baseurl}}/partners/fullstory/) ayuda a los líderes tecnológicos a tomar decisiones mejores y más informadas. Al incorporar datos de comportamiento digital en su stack tecnológico de análisis, la tecnología patentada de Fullstory libera el poder de los datos de comportamiento de calidad a gran escala, transformando cada visita digital en información accionable. 

#### Fidelización abierta - Análisis de& datos

[Open Loyalty]({{site.baseurl}}/partners/openloyalty) es una plataforma de programas de fidelización basada en la nube que te permite crear y administrar programas de fidelización y recompensas para clientes. La integración de Braze y Open Loyalty sincroniza los datos de fidelización, como el saldo de puntos, los cambios de nivel y las advertencias de caducidad, directamente en Braze en tiempo real. Esto te permite desencadenar mensajes personalizados (correo electrónico, notificaciones push, SMS) cuando cambia el estado de fidelización de un usuario.

#### DOTS.ECO \- Extensiones

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco) te permite proporcionar recompensas a los usuarios basadas en el impacto medioambiental real a través de certificados digitales rastreables. Cada certificado puede incluir metadatos como una URL compartible del certificado y una URL de la imagen, para que los usuarios puedan ver (y volver a visitar) vuestra prueba de impacto.

#### Mailizio - Orquestación de mensajes

[Mailizio]({{site.baseurl}}/partners/mailizio/) es una plataforma de creación y administración de correos electrónicos que facilita el diseño de contenido reutilizable y seguro para la marca mediante un editor visual intuitivo. Gracias a la integración de Mailizio con Braze, exporta tus bloques de contenido y plantillas de correo electrónico, y luego genera automáticamente mensajes dentro de la aplicación a partir de esos mismos activos, lo que te permite implementar campañas de forma rápida y totalmente controlada.

### API

#### API POST de la biblioteca multimedia

{% multi_lang_include release_type.md release="General availability" %}

Ahora se pueden añadir activos de la biblioteca multimedia a través de la API, lo que habilita a los clientes, socios y agencias automatizar en mayor medida vuestros flujos de trabajo de creación de mensajes. Utiliza la [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) para cargar un archivo de activos directamente o copia un archivo desde una URL existente. Esta característica desbloquea capacidades de integración y automatización.

### Currents y Datashare

#### Eventos de la consola del agente para destinos de almacenamiento y Datashare

{% multi_lang_include release_type.md release="General availability" %}

Ahora hay dos nuevos [eventos](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) disponibles para destinos de almacenamiento (AWS S3, GCS y Azure Blob Storage) y Snowflake Datashare:`agentconsole.AgentExecuted`  y `agentconsole.ToolInvocation`. Estos eventos te habilitan para analizar el uso y los detalles de la consola del agente en tus sistemas descendentes, lo que te ayuda a comprender y sacar el máximo partido al uso de tus agentes. Los agentes te permiten crear e implementar agentes inteligentes que pueden realizar tareas específicas en Braze, como generar contenido en lienzos o catálogos y dirigir a los usuarios por diferentes rutas basándose en decisiones inteligentes. Para obtener más información, consulta el [registro de cambios de Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Nuevos eventos «Reintentar» para canales individuales

{% multi_lang_include release_type.md release="General availability" %}

Ahora hay nuevos [eventos de reintento](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) disponibles para los canales de correo electrónico, LINE, notificaciones push, SMS, webhooks y WhatsApp. Estos eventos proporcionan visibilidad sobre cuándo la limitación de frecuencia provoca que un mensaje programado se retrase en lugar de cancelarse. Cuando se reduce la prioridad de un mensaje o se limita su frecuencia, ahora se puede reintentar dentro de una ventana de reintento configurada, lo que te proporciona más información sobre los patrones de entrega de mensajes y el impacto de la limitación de frecuencia. Para obtener más información, consulta el [registro de cambios de Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Añadir un nuevo'time_ms'campo al evento TokenStateChange

{% multi_lang_include release_type.md release="General availability" %}

Se ha añadido un nuevo`time_ms`campo al evento[`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), que proporciona una granularidad de milisegundos para el seguimiento de los cambios de estado de los tokens de notificaciones push. Esta mayor precisión te ayuda a comprender el estado más reciente de un token de notificaciones push cuando se producen varios cambios en el mismo segundo, lo que te da confianza en los sistemas posteriores de que tienes la suscripción correcta. Para obtener más información, consulta el [registro de cambios de Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Enviar usuario anónimo a destinos de Tealium

{% multi_lang_include release_type.md release="General availability" %}

Los eventos que no tienen un ID externo definido ahora se pueden transmitir a destinos [de Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents). Cuando seleccionas la casilla «Incluir eventos de usuarios anónimos» en tu integración de Currents, los eventos sin un ID externo se enviarán al destino en lugar de ser suprimidos. Esta capacidad es fundamental para los análisis posteriores y los casos de uso que involucran a usuarios no identificados y anónimos.

##### Enviar usuario anónimo a destinos HTTP personalizados

{% multi_lang_include release_type.md release="Beta" %}

Los eventos que no tienen un ID externo definido ahora se pueden transmitir a destinos CustomHTTP. Cuando seleccionas la casilla «Incluir eventos de usuarios anónimos» en tu integración de Currents, los eventos sin un ID externo se enviarán al destino en lugar de ser suprimidos. Esta capacidad es fundamental para los análisis posteriores y los casos de uso que involucran a usuarios no identificados y anónimos.

#### Evento de apertura de correo electrónico —"machine_open"  campo

El [evento «Apertura de correo electrónico»]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) ahora genera el valor"machine_open" del campo para informar sobre la métrica [_«Apertura de máquina_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens)». 

### SDK

Se han publicado las siguientes actualizaciones del SDK. SWIFT SDK v14.0.1 soluciona un problema con el manejo de enlaces universales. Android SDK v40.2.0 corrige una posible fuga de memoria y resuelve un problema con la apertura de varias sesiones cuando hay actividades transparentes. Expo SDK v3.2.0 añade la`forwardUniversalLinks`opción (predeterminada: false) para configurar el manejo de enlaces universales por parte del SDK nativo de SWIFT.

#### Actualizaciones importantes del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de Android 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - Se cambió el nombre de `BrazeConfig.Builder.setIsLocationCollectionEnabled()` a `setIsAutomaticLocationCollectionEnabled()`.
    - Se cambió el nombre de `BrazeConfig.isLocationCollectionEnabled` a `isAutomaticLocationCollectionEnabled`.
    - Se cambió el nombre de `BrazeConfigurationProvider.isLocationCollectionEnabled` a `isAutomaticLocationCollectionEnabled`.
- [SDK de Android 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Complemento Expo 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [SDK de Swift 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details January 8, 2026 %}
## Lanzamiento el 8 de enero de 2026.

### Informes de& datos

#### Actualizaciones de los eventos de Currents

{% multi_lang_include release_type.md release="General availability" %}

Se han realizado los siguientes cambios en Currents en la versión 4:

* Cambios de campo al tipo de evento`users.behaviors.pushnotification.TokenStateChange`:
    * Se ha añadido un nuevo`string`campo`push_token`: Envía el token de notificaciones push del evento.
* Cambios de campo al tipo de evento`users.messages.pushnotification.Bounce`:
    * Se ha añadido un nuevo`string`campo`push_token`: Envía el token de notificaciones push del evento.
* Cambios de campo al tipo de evento`users.messages.pushnotification.Send`:
    * Se ha añadido un nuevo`string`campo`push_token`: Envía el token de notificaciones push del evento.
* Cambios de campo al tipo de evento`users.messages.rcs.Click`:
    * Se ha añadido un nuevo`string`campo`canvas_variation_name`: Nombre de la variación de Canvas que recibió este usuario
    * El campo  ahora`user_phone_number` es *opcional*.
* Cambios de campo al tipo de evento`users.messages.rcs.InboundReceive`:
    * El campo  ahora`user_id` es *opcional*.
* Cambios de campo al tipo de evento`users.messages.rcs.Rejection`:
    * Se ha añadido un nuevo`string`campo`canvas_step_message_variation_id`: API ID de la variación del mensaje del paso Canvas que recibió este usuario

Consulta el [registro de cambios de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) para conocer los cambios en los eventos de cada versión.

#### Exportar registros de sincronización por todas las filas

{% multi_lang_include release_type.md release="Early access" %}

En el [panel de control **de sincronización** de ingesta de datos en la nube]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs), elige exportar los registros a nivel de fila para una sincronización ejecutada por:

* **Filas con errores:** Descarga un archivo que contiene solo las filas que tenían un estado **de error**.
* **Todas las filas:** Descarga un archivo que contiene todas las filas procesadas en la ejecución.

### Canales&  Puntos de intervención

#### Conector WhatsApp «trae el tuyo propio» (BYO)

El [conector Bring Your Own (BYO) WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/) ofrece una asociación entre Braze e Infobip, en la que tú le das a Braze acceso a tu Infobip WhatsApp Business Manager (WABA). Esto te permite administrar y pagar los costes de mensajería directamente con Infobip mientras utilizas Braze para la segmentación, la personalización y la orquestación de campañas. 

#### Banners en Canvas

{% multi_lang_include release_type.md release="Early access" %}

Selecciona **Banners** como canal de mensajería en un [paso Mensaje]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) para Canvas. Utiliza el editor de arrastrar y soltar para crear mensajes personalizados en línea, proporcionando experiencias no intrusivas y contextuales que se actualizan automáticamente al inicio de cada sesión de usuario. 

#### CCO dinámico

{% multi_lang_include release_type.md release="General availability" %}

Con [el BCC dinámico]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc), utiliza Liquid en tu dirección BCC. Ten en cuenta que esta característica solo está disponible en **Preferencias de correo electrónico** y no se puede configurar en la propia campaña. Solo se permite una dirección BCC por destinatario de correo electrónico.

#### Límites de velocidad basados en canales

Como alternativa a un límite de velocidad que se comparte en toda una campaña multicanal o Canvas, selecciona un límite de velocidad específico por canal. En este caso, el límite de velocidad se aplicará a cada uno de los canales seleccionados. Por ejemplo, configura tu campaña o Canvas para enviar un máximo de 5000 webhooks y 2500 mensajes SMS por minuto en toda la campaña o Canvas. Para obtener más información, consulta [Limite de velocidad y limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting).

### Asociación

#### LILT - Localización

[LILT]({{site.baseurl}}/partners/lilt/) es la solución completa de IA para la traducción y la creación de contenidos empresariales. LILT habilita a las organizaciones globales para ampliar y optimizar su contenido, productos, comunicaciones y operaciones de soporte, con agentes de IA y flujos de trabajo totalmente automatizados.

### Actualizaciones importantes del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [SDK de Android 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [SDK de SWIFT 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Elimina el canal de noticias.
        - Esto elimina por completo todos los elementos de la interfaz de usuario, los modelos de datos y las acciones asociadas con el canal de noticias.
- [SDK web 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## 9 de diciembre de 2025

### Informes de& datos

#### Añadir Google Tag Manager a una página de destino

Para añadir Google Tag Manager a tus páginas de destino, añade un bloque de código personalizado a tu página de destino en el editor de arrastrar y soltar, y luego [inserta el código de Tag Manager]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) en el bloque.

### Orquestación

#### Caso de uso de SMS Liquid

El caso de uso [«Responder con diferentes mensajes en función de la palabra clave del SMS entrante»]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) incorpora el procesamiento dinámico de palabras clave de SMS para responder a mensajes entrantes específicos con diferentes textos de mensaje. Por ejemplo, puedes enviar respuestas diferentes cuando alguien envía un mensaje de texto con «START» en lugar de «JOIN».

#### Lista de permitidos para contenido conectado

Puedes incluir en la lista blanca URL específicas para que se utilicen en [el contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call). Para acceder a esta característica, ponte en contacto con tu administrador del éxito del cliente.

### Canales&  Puntos de intervención

#### Codificación de caracteres SMS

¡Tu [calculadora de segmentos SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator) ahora tiene codificación de caracteres! Selecciona **Codificación de caracteres de visualización** para identificar qué caracteres están codificados como GSM-7 o UCS-2. 

![Calculadora de segmentos SMS con un mensaje SMS de ejemplo introducido en el cuadro de texto y la codificación de caracteres activada.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### Mensajes de WhatsApp con optimización

Dado que la API MM para WhatsApp no ofrece una capacidad de entrega del 100 %, es importante comprender cómo reorientar a los usuarios que pueden no haber recibido tu mensaje en otros canales. 

Para reorientar a los usuarios, recomendamos crear un segmento de usuarios que no hayan recibido un mensaje específico. Para ello, filtra por el código de error`131049` , que indica que no se ha enviado un mensaje de plantilla de marketing debido a la aplicación del límite de plantillas de marketing por usuario de WhatsApp. Para ello, puedes [utilizar Braze Currents o las extensiones de segmento de SQL]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels).

### Asociación

#### OtherLevels - Contenido dinámico

[OtherLevels]({{site.baseurl}}/partners/otherlevels/) es una plataforma de experiencias que utiliza IA generativa para transformar la forma en que las marcas deportivas, los editores y los operadores conectan con sus clientes, transformando el contenido tradicional en videos personalizados y experiencias multimedia enriquecidas a gran escala.

### SDK

#### Actualizaciones importantes del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK web 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## 11 de noviembre de 2025

### Flexibilidad de los datos

#### `Live Activities Push to Start Registered for App` filtro de segmentación

El`Live Activities Push to Start Registered for App`filtro segmenta a tus usuarios según si están registrados para iniciar una actividad en vivo a través de notificaciones push de iOS para una aplicación específica.

#### Extensiones de segmento RFM SQL

Puedes crear una [extensión de segmento RFM (reciencia, frecuencia, monetario)]({{site.baseurl}}/rfm_segments/) para dirigirte a tus mejores usuarios midiendo sus hábitos de compra.

El análisis RFM es una técnica de marketing que identifica a tus mejores usuarios mediante una puntuación del 0 al 3 para cada categoría (reciencia, frecuencia y valor monetario), donde 3 es la mejor puntuación y 0 la peor. La actualidad, la frecuencia y los valores monetarios se basan en datos de un intervalo de tiempo específico elegido por ti.

#### Atributos personalizados: valores 

Al ver un informe de uso, selecciona la [pestaña **Valores**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) para ver los valores principales de los atributos personalizados seleccionados basados en una muestra de aproximadamente 250 000 usuarios.

#### Sincronización de registros y observabilidad para la ingesta de datos en la nube

{% multi_lang_include release_type.md release="General availability" %}

El [panel]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) de control de la ingesta de datos (CDI) [Sync Log]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) te permite supervisar todos los datos procesados por CDI, verificar si los datos se han sincronizado correctamente y diagnosticar cualquier problema con datos «incorrectos» o faltantes.

#### Implementación de características con múltiples reglas

Utiliza [implementaciones de indicadores de características con múltiples reglas]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) para definir una secuencia de reglas para evaluar a los usuarios, lo que permite una segmentación precisa y lanzamientos de características controlados. Este método es ideal para implementar la misma característica en audiencias diversas.

#### Mapeado a campos del catálogo para bloques de productos de arrastrar y soltar

En la configuración de tu catálogo, puedes alternar la opción **Bloques de productos** para [realizar el mapeo de campos]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) e información [específicos]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) de tu catálogo. Esto te permite seleccionar qué campos utilizar como título del producto, URL del producto y URL de la imagen.

#### Eventos de interrupción de la limitación de frecuencia en Currents

Al utilizar Currents, ahora puedes hacer referencia`abort_type`a los eventos de aborto del canal. Esto identifica que un mensaje ha sido abortado debido a la limitación de frecuencia e incluye qué regla de limitación de frecuencia causó el aborto. Esto te ayuda a determinar cómo configurar tus reglas de limitación de frecuencia. Consulta [Eventos]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) de [interacción con]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) [mensajes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) para obtener detalles específicos sobre los eventos de Currents.

### Canales robustos

#### Imágenes de fondo de fila 

{% multi_lang_include release_type.md release="General availability" %}

Puedes [añadir una imagen de fondo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image) a un mensaje dentro de la aplicación o a una página de destino en el panel **Propiedades de fila**. Alternar la opción **Imagen de fondo** y, a continuación, introducir la URL de una imagen o seleccionar una imagen de la [biblioteca multimedia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). Por último, configura el texto alternativo, el tamaño, la posición y si la imagen se repite para crear patrones en toda la fila.

![Imagen de fondo de una fila de pizzas con un patrón repetido horizontalmente.]({% image_buster /assets/img_archive/background_row.png %})

#### Copiar enlace a vista previa

Utiliza **el enlace «Copiar vista previa»** en tus [banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional), [pies de página personalizados de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer) y [páginas de adhesión voluntaria y cancelación de suscripción al correo electrónico]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers) para generar un enlace compartible que muestre cómo se verá tu contenido para un usuario aleatorio.

#### Mensajes de WhatsApp con entrega optimizada

Utiliza los avanzados sistemas de inteligencia artificial de Meta para hacer llegar tus mensajes de marketing a más usuarios que sean más propensos a interactuar con ellos, lo que aumentará significativamente la capacidad de entrega y la interacción con los mensajes.

[Los mensajes de WhatsApp con entrega optimizada]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/) se envían utilizando [la](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) nueva [API Marketing Messages Lite](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) de Meta, que ofrece un rendimiento superior en comparación con la API Cloud tradicional. Esta nueva canalización de envío te ayuda a llegar mejor a los usuarios que valoran y desean recibir tus mensajes.

#### WhatsApp Flows

Al incorporar un mensaje de WhatsApp Flow en un BRAZE CANVAS o una campaña, es posible que quieras capturar y utilizar información específica que los usuarios envían a través del Flow. Braze necesita recibir información adicional sobre la estructura de la respuesta del usuario, concretamente la forma prevista de la respuesta JSON, para generar el esquema de atributos personalizados anidados (NCA) necesario.

Ahora puedes proporcionar a Braze la información sobre la estructura de respuesta [guardando la respuesta del flujo como un atributo personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) y completando un envío de prueba.

#### Vista previa del usuario editable

Puedes [editar campos individuales de un usuario aleatorio o existente]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user) para ayudar a probar el contenido dinámico dentro de tu mensaje. Selecciona **Editar** para convertir el usuario seleccionado en un usuario personalizado que puedas modificar.

![La pestaña «Vista previa como usuario» con un botón «Editar».]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Automatización de IA y ML

#### BrazeAI Decisioning Studio™ Go

Ahora puedes configurar tu integración con [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go) consultando estos artículos de configuración para:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Nuevas características para Braze Agents

{% multi_lang_include release_type.md release="Beta" %}

Ahora puedes personalizar tu [Braze Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) de la siguiente manera:

- Aplicar [las directrices de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) que tu agente debe seguir en sus respuestas. 
- Consultar un catálogo para realizar aún más la personalización de tu mensaje.
- Estructurar la salida de un agente proporcionando el [formato de salida]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format).
- Adjustar la [temperatura]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) según el nivel de desviación del rendimiento de tu agente.

### Modelos ChatGPT con BrazeAI Operator<sup>TM</sup>

{% multi_lang_include release_type.md release="Beta" %}

Puedes seleccionar entre estos modelos GPT para utilizarlos con diferentes tipos de solicitudes con [Operator]({{site.baseurl}}/user_guide/brazeai/operator):

- GPT-5 nano
- GPT-5 mini (predeterminado)
- GPT-5

### Nuevas asociaciones Braze

#### StackAdapt - Publicidad

[StackAdapt]({{site.baseurl}}/partners/stackadapt/) es una plataforma de marketing basada en inteligencia artificial que entrega publicidad dirigida y orientada al rendimiento. Te permite sincronizar los datos del perfil de usuario de Braze con el centro de datos StackAdapt. Al conectar las dos plataformas, puedes crear una visión unificada de tus clientes y activar los datos propios para mejorar el rendimiento de los anuncios.

#### Cloudinary: contenido dinámico

[Cloudinary]({{site.baseurl}}/partners/cloudinary/) es una plataforma de imágenes y videos que te permite administrar, editar, optimizar y entregar imágenes y videos a gran escala para cualquier campaña en todos los canales y recorridos del cliente. Cuando se integra y habilita, la gestión de medios de Cloudinary potenciará y proporcionará una entrega de activos dinámica, contextual y personalizada para tus campañas y lienzos de Braze.

#### Kameleoon - Pruebas A/B

[Kameleoon]({{site.baseurl}}/partners/kameleoon/) es una solución de optimización con capacidades de experimentación, personalización basada en inteligencia artificial y gestión de características en una única plataforma unificada.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Corrige el tipo de Typescript para la devolución de llamada de`subscribeToInAppMessage`  y`addListener`  para `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Ahora estos oyentes devuelven correctamente una devolución de llamada con el nuevo`InAppMessageEvent`tipo. Anteriormente, los métodos estaban anotados para devolver un`BrazeInAppMessage`tipo, pero en realidad devolvían un `String`.
         - Si utilizas alguna de las API de suscripción, asegúrate de que el comportamiento de tus mensajes dentro de la aplicación no haya cambiado tras actualizar a esta versión. Consulta nuestro código de ejemplo en `BrazeProject.tsx`.
    - Las API `logInAppMessageClicked`,  `logInAppMessageImpression`y`logInAppMessageButtonClicked`  ahora solo aceptan un`BrazeInAppMessage`objeto  para que coincida con su interfaz pública existente.
        - Anteriormente, aceptaba tanto un`BrazeInAppMessage`objeto como un `String`.
    - `BrazeInAppMessage.toString()` ahora devuelve una cadena legible para los humanos en lugar de la representación de cadena JSON.
        - Para obtener la representación de cadena JSON de un mensaje dentro de la aplicación, utiliza `BrazeInAppMessage.inAppMessageJsonString`.
    - En iOS,`[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]`  se ha trasladado a `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`.
        - Este nuevo método es ahora un método de clase en lugar de un método de instancia.
    - Añade anotaciones de nulabilidad a`BrazeReactUtils`los métodos.
    - Elimina los siguientes métodos y propiedades obsoletos de la API:
        - `getInstallTrackingId(callback:)` a favor de `getDeviceId`.
        - `registerAndroidPushToken(token:)` a favor de `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` a favor de `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` a favor de `payload_type`.
        - `PushNotificationEvent.deeplink` a favor de `url`.
        - `PushNotificationEvent.content_text` a favor de `body`.
        - `PushNotificationEvent.raw_android_push_data` a favor de `android`.
        - `PushNotificationEvent.kvp_data` a favor de `braze_properties`.
    - Actualiza los enlaces de la versión nativa del SDK de Android [de Braze Android SDK 39.0.0 a 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK de .NET MAUI (Xamarin) versión 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Se ha actualizado el enlace iOS [de Braze SWIFT SDK 12.1.0 a 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Esto incluye compatibilidad con Xcode 26.
- [SDK de Flutter 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Actualiza el puente nativo de Android [de Braze Android SDK 39.0.0 a 40.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze SWIFT SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK web 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [SDK de Android 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## Lanzamiento el 14 de octubre de 2025.

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) sustituye las pruebas A/B por decisiones basadas en inteligencia artificial que realizan la personalización de todo y maximizan cualquier métrica: impulsa los ingresos, no los clics. Con BrazeAI Decisioning Studio™, puedes optimizar cualquier KPI empresarial. Consulta nuestra sección dedicada [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) para ver ejemplos de casos de uso y características clave.

### Flexibilidad de los datos

#### Eventos de New Currents

Se han añadido estos nuevos eventos al [glosario]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) de [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events):

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

Estos nuevos campos se han añadido a los siguientes eventos de Currents:

- `is_sms_fallback`: 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id`, `in_reply_to`, `flow_id`, `flow_response_json`, `product_id`, `catalog_id`: 
  - `users.messages.whatsapp.InboundReceive`
- `message_id`, `flow_id`, `template_name`: 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Listas de supresión

{% multi_lang_include release_type.md release="General availability" %}

[Las listas de supresión]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) son grupos de usuarios que automáticamente no reciben ninguna campaña ni Canvases. Las listas de supresión se definen mediante filtros de segmento, y los usuarios entran y salen de las listas de supresión a medida que cumplen los criterios de filtrado.

#### Personalización sin copia

{% multi_lang_include release_type.md release="Early access" %}

Sincroniza los activadores de Canvas utilizando la ingesta de datos para [desencadenar la personalización sin copias]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). Esta característica accede a información específica del usuario desde tu solución de almacenamiento de datos y la transfiere a un Canvas de destino. Los pasos en Canvas pueden incluir opcionalmente campos de personalización que no se conservan en los perfiles de usuario de Braze.

#### Variables de contexto de Canvas para los pasos «Ruta de audiencia» y «Paso para la división de decisiones»

{% multi_lang_include release_type.md release="Early access" %}

Puedes [crear filtros de variables de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters) que utilicen variables de contexto previamente declaradas en los pasos [de ruta de audiencia]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) y paso [para la división de decisiones]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

### Desbloquear la creatividad

#### Tarjetas de oferta para correos electrónicos

Utiliza [las tarjetas de oferta]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab) para proporcionar información clave sobre la oferta directamente en la parte superior del cuerpo del correo electrónico. Esto permite a los destinatarios comprender rápidamente los detalles de la oferta y tomar medidas.

#### Plantillas para banners

Al [crear tu banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create), ahora puedes empezar con una plantilla en blanco, utilizar una plantilla de Braze o seleccionar una plantilla de banner guardada.

### Canales robustos

#### Listas de supresión

{% multi_lang_include release_type.md release="General availability" %}
 
[Las listas de supresión]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists/) especifican grupos de usuarios que nunca recibirán mensajes. Los administradores pueden crear listas de supresión con filtros de segmentación para reducir un grupo de usuarios de la misma manera que lo harías para la segmentación.

#### Seguimiento de clics de LINE

{% multi_lang_include release_type.md release="General availability" %}

Cuando se activa [el seguimiento de clics de LINE]({{site.baseurl}}/line/click_tracking/), Braze acorta automáticamente tus URL, añade mecanismos de seguimiento y registra los clics en tiempo real. Mientras que LINE ofrece datos agregados sobre clics, Braze proporciona información detallada sobre los usuarios que es oportuna y útil. Estos datos te permiten crear estrategias de segmentación y reorientación más específicas, como segmentar a los usuarios en función de su comportamiento de clics y desencadenar mensajes en respuesta a clics específicos.

#### Filtrado de clics de bots SMS y RCS

{% multi_lang_include release_type.md release="General availability" %}

[El filtrado de clics de bots SMS y RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/) mejora el análisis de campañas y los flujos de trabajo al excluir los clics sospechosos de bots. Un «clic de bot» se refiere a los clics automatizados en enlaces acortados en mensajes SMS y RCS, como los de los rastreadores web, las vistas previas de enlaces de Android e iOS o el software de seguridad CPaaS. Esta característica facilita la elaboración de informes precisos, la segmentación y la orquestación para atraer a usuarios reales.

#### Transferir números de teléfono de WhatsApp

Transfiere un número de teléfono de WhatsApp Business Account (WABA) y su grupo de suscripción asociado [de un espacio de trabajo a otro]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) dentro de Braze.

#### WhatsApp Flows: mensajes de respuesta y vista previa

En un Canvas, puedes crear un paso de mensaje de WhatsApp que utilice un [mensaje de respuesta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) y un mensaje de flujo. También puedes seleccionar **Vista previa del flujo** para obtener una vista previa del flujo directamente en Braze y confirmar que funciona según lo esperado.

#### Mensajes sobre productos de WhatsApp

[Los mensajes de productos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/) te permiten enviar mensajes interactivos de WhatsApp que muestran productos directamente desde tu catálogo de Meta.

#### Integración de Braze y WhatsApp con un sistema externo

[Aprovecha el poder de los chatbots con IA y los traspasos a agentes en vivo]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) en el canal de WhatsApp para optimizar tus operaciones de atención al cliente. Al automatizar las consultas rutinarias y pasar fácilmente a los agentes humanos cuando sea necesario, puedes mejorar significativamente los tiempos de respuesta y la experiencia del cliente.

### Automatización de IA y ML

#### Agentes de Braze

{% multi_lang_include release_type.md release="Beta" %}

[Los agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/) son asistentes basados en inteligencia artificial que puedes crear dentro de Braze. Los agentes pueden generar contenido, tomar decisiones inteligentes y enriquecer tus datos para que puedas entregar experiencias del cliente más personalizadas.

### Nuevas asociaciones Braze

#### Jasper - Plantillas

La integración de [Jasper]({{site.baseurl}}/partners/jasper/) con Braze te permite optimizar la creación de contenido y la ejecución de campañas. Con Jasper, tus equipos de marketing pueden generar textos de alta calidad y acordes con la marca en cuestión de minutos. A continuación, Braze facilita la entrega de estos mensajes a la audiencia adecuada en el momento óptimo. Esta integración fomenta flujos de trabajo fáciles, reduce el esfuerzo manual y genera resultados de interacción más sólidos.

#### Swym: fidelización y reorientación

[Swym]({{site.baseurl}}/partners/swym/) ayuda a las marcas de comercio electrónico a captar la intención de compra con listas de deseos, guardar para más tarde, registro de regalos y alertas de reposición de existencias. Gracias al uso de datos enriquecidos y basados en permisos, puedes crear campañas hiperorientadas y entregar experiencias de compra personalizadas que impulsen la interacción, aumenten las conversiones y mejoren la fidelización.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las últimas novedades se enumeran a continuación; puedes encontrar el resto de novedades consultando los registros de cambios del SDK correspondiente.

- [SDK de Cordova 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Se ha actualizado el puente nativo de Android [de Braze Android SDK 37.0.0 a 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - La versión mínima requerida de GradlePluginKotlinVersion es ahora 2.1.0.
    - Se ha actualizado el puente nativo de iOS [de Braze SWIFT SDK 12.0.0 a 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Esto incluye compatibilidad con Xcode 26.
    - Elimina la compatibilidad con el canal de noticias. Se han eliminado las siguientes API:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Actualiza los enlaces de la versión nativa del SDK de Android [de Braze Android SDK 37.0.0 a 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Elimina la compatibilidad con el canal de noticias. Se han eliminado las siguientes API:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [SDK web 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [SDK de Flutter 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [SDK de Unity 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Se ha actualizado el puente nativo de iOS [de Braze SWIFT SDK 12.0.0 a 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Esto incluye compatibilidad con Xcode 26.

{% enddetails %}
{% details September 16, 2025 %}

## Lanzamiento el 16 de septiembre de 2025.

### Flexibilidad de los datos

#### Plataforma de datos Braze

Braze Data Platform es un conjunto completo y modulable de capacidades de datos e integraciones del socio que te permite crear experiencias personalizadas e impactantes a lo largo del ciclo de vida del cliente. Más información sobre las tres tareas relacionadas con los datos que hay que realizar: 

- [Unificación de datos]({{site.baseurl}}/user_guide/data/unification)
- [Activación de datos]({{site.baseurl}}/user_guide/data/activation)
- [Distribución de datos]({{site.baseurl}}/user_guide/data/distribution)

#### Propiedades del banner personalizado

{% multi_lang_include release_type.md release="Early access" %}

Puedes utilizar propiedades personalizadas de tu campaña de Banner para recuperar datos clave-valor a través del SDK y modificar el comportamiento o la apariencia de tu aplicación. Para obtener más información, consulta [Propiedades del banner personalizado]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Autenticación por token

{% multi_lang_include release_type.md release="General availability" %}

Al utilizar Braze Connected Content, es posible que determinadas API requieran un token en lugar de un nombre de usuario y una contraseña. Braze puede almacenar credenciales que contienen [valores de encabezado de autenticación de tokens]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication).

#### Códigos de promoción

Puedes guardar los códigos promocionales en el perfil de usuario mediante el paso Actualización de usuario. Para obtener más información, consulta [Guardar códigos promocionales en los perfiles de usuario]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile).

### Desbloquear la creatividad

#### Braze Pilot

[Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot) es una aplicación disponible públicamente para Android e iOS que te permite enviar mensajes desde tu panel de Braze a tu teléfono. Consulta [Introducción a Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started) para obtener una guía paso a paso sobre cómo descargar la aplicación, iniciar la conexión con tu panel de Braze y completar la configuración.

### Nuevas asociaciones Braze

#### Blings: contenido visual e interactivo

[Blings]({{site.baseurl}}/partners/blings/) es una plataforma de vídeo personalizada de última generación que te habilita para entregar experiencias de vídeo en tiempo real, interactivas y basadas en datos a través de múltiples canales a gran escala.

#### Integración estándar de Shopify con herramientas de terceros

Para las tiendas online de Shopify, recomendamos utilizar el método de integración estándar de Braze para admitir los SDK de Braze en tu sitio web.

Sin embargo, entendemos que es posible que prefieras utilizar una herramienta de terceros, como Google Tag Manager, por lo que hemos elaborado una guía sobre cómo hacerlo. Para empezar, consulta [Shopify: Etiquetado por terceros]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK Braze Flutter 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Actualiza el puente nativo de Android desde Braze Android SDK`36.0.0`a `39.0.0`.
    - Actualiza el puente nativo de iOS de Braze SWIFT SDK`12.0.0`a `13.2.0`. Esto incluye compatibilidad con Xcode 26.

- [Braze SWIFT SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Actualiza los enlaces del SDK Swift de Braze para que requieran versiones de la denominación `13.0.0+` SemVer. Esto permite la compatibilidad con cualquier versión del SDK de Braze desde `13.0.0` hasta, pero sin incluir, `14.0.0`.

{% enddetails %}
{% details August 19, 2025 %}

## Lanzamiento el 19 de agosto de 2025.

### Estandarización de la coherencia de las zonas horarias en Canvas Context

{% multi_lang_include release_type.md release="Early access" %}

Si participas en el [acceso anticipado al paso en]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) [Canvas Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), todas las marcas de tiempo con un tipo de fecha y hora de las propiedades del evento en lienzos basados en acciones siempre se normalizarán a [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Para obtener más información al respecto, consulta [Estandarización]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization) de [la coherencia de las zonas horarias]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization).

### Flexibilidad de los datos

#### Dominios personalizados de autoservicio

{% multi_lang_include release_type.md release="General access" %}

[Los dominios personalizados de autoservicio]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) te permiten configurar y administrar tus propios dominios personalizados para SMS, RCS y WhatsApp, directamente desde tu panel de Braze. Puedes añadir, supervisar y administrar fácilmente hasta 10 dominios personalizados en un solo lugar.

#### Estadísticas del embudo de segmentos

Selecciona [Ver estadísticas del embudo]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics) para mostrar las estadísticas de ese grupo de filtros y ver cómo cada filtro añadido afecta a las estadísticas de tu segmento. Verás un recuento estimado y un porcentaje de los usuarios a los que se aplican todos los filtros hasta ese momento. Una vez que se muestran las estadísticas de un grupo de filtros, se actualizarán automáticamente cada vez que cambies los filtros. 

#### Nuevos campos de respuesta para`/campaigns/details`el punto final de las notificaciones push

La`messages`respuesta para las notificaciones push ahora incluye dos nuevos campos:

- `image_url`: Una URL de imagen para una imagen de notificación de Android, una imagen de notificación de iOS o una imagen de icono de notificación push web.
- `large_image_url`: Una URL de imagen de notificación web para acciones de notificación push web de Android Chrome y Windows.

#### Definición de campos de información de identificación personal (PII)

Seleccionar y [definir determinados campos como campos de información de identificación personal (PII)]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) solo afecta a lo que los usuarios pueden ver en el panel de Braze y no influye en cómo se gestionan los datos de los usuarios finales en dichos campos PII.

Consulta con tu equipo jurídico para ajustar la configuración de tu panel a las normativas y políticas de privacidad aplicables a tu empresa, incluidas las relacionadas con [la retención de datos]({{site.baseurl}}/api/data_retention/).

#### Compartir un enlace de descarga del generador de informes

Puedes [compartir un enlace]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) al informe [del panel]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) seleccionando **Compartir** y, a continuación**, Compartir un enlace** o **Enviar o programar un correo electrónico**.

### Desbloquear la creatividad

#### Etiquetas de encabezado personalizadas para correos electrónicos de arrastrar y soltar

Utiliza`<head>`etiquetas para añadir CSS y metadatos en tu mensaje de correo electrónico. Por ejemplo, puedes utilizar estas etiquetas para añadir una hoja de estilos o un favicon. Liquid es compatible con`<head>`las etiquetas .

### Canales robustos

#### Mejores prácticas difusas

Hemos añadido una [sección de prácticas recomendadas]({{site.baseurl}}) para ayudarte a configurar cuidadosamente tu mensaje de exclusión difusa y crear una experiencia clara, conforme y positiva para tus suscriptores.

#### WhatsApp Flows

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) es una mejora del canal WhatsApp existente que te permite crear experiencias de mensajería interactivas y dinámicas. 

#### Preguntas sobre productos recibidas a través de WhatsApp

Los usuarios pueden responder a tu mensaje sobre el producto o catálogo con [preguntas sobre el producto]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions). Estos llegan como mensajes entrantes, que luego pueden clasificarse con una ruta de acción.

Además, Braze extrae el ID del producto y el ID del catálogo de estas preguntas, por lo que, si deseas automatizar las respuestas o enviar preguntas a otro equipo (como el de atención al cliente), puedes incluir esos detalles.

### Automatización de IA y ML

#### Nuevos artículos sobre casos de uso de BrazeAI™

Hemos añadido nuevos artículos sobre casos de uso para ayudarte a sacar el máximo partido a BrazeAI™. Estas guías destacan formas prácticas de aplicar la IA a tus estrategias de interacción, entre las que se incluyen:

- [Predictive Churn]({{site.baseurl}}/user_guide/brazeai/predictive_churn/use_case): Identifica a los clientes con riesgo de abandono y toma medidas a tiempo.
- [Eventos de predicción]({{site.baseurl}}/user_guide/brazeai/predictive_events/use_case): Anticipa las acciones clave de los usuarios y da forma a las experiencias en tiempo real.
- [Recomendaciones]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): Entregar contenidos y productos más relevantes basados en el comportamiento del cliente.

#### servidor MCP

{% multi_lang_include release_type.md release="Beta" %}

El [servidor MCP de]({{site.baseurl}}/user_guide/brazeai/mcp_server/) [Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server/), una conexión segura y de solo lectura, permite que herramientas de IA como Claude y Cursor accedan a datos de Braze que no son PII para responder preguntas, analizar tendencias y proporcionar información sin alterar los datos.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK de Swift 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Amplía la funcionalidad de`BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`  para que se desencadene en caso de errores de autenticación «opcionales».
        - El método delegado `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`ahora se desencadenará para los errores de autenticación «Obligatorio» y «Opcional».
        - Si solo deseas gestionar los errores de autenticación «obligatorios» del SDK, añade una comprobación que garantice que`BrazeSDKAuthError.optional`  es falso dentro de la implementación de este método delegado.
    - Corrige el uso de`Braze.Configuration.sdkAuthentication`  para que surta efecto cuando se habilita.
        - Anteriormente, el SDK no consumía el valor de esta configuración y el token siempre se adjuntaba a las solicitudes si estaba presente.
        - Ahora, el SDK solo adjuntará el token de autenticación del SDK a las solicitudes de red salientes cuando se habilite esta configuración.
    - Se han creado los configuradores para todas las`Braze.Banner` propiedades`private` de`Braze.FeatureFlag`  y todas las propiedades de . Las propiedades de estas clases ahora son de solo lectura.
    - Elimina la`Braze.Banner.id`propiedad, que quedó obsoleta en la versión `11.4.0`.
        - En su lugar, utiliza`Braze.Banner.trackingId`  para leer el ID de seguimiento de la campaña de un banner.
- [SDK React Native 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Actualiza los enlaces de la versión nativa del SDK de Android de [Braze Android SDK 36.0.0 a 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualiza los enlaces de la versión nativa del SDK de SWIFT de [Braze SWIFT SDK 12.0.0 a 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - El`sdkAuthenticationError`evento ahora desencadenará para los errores de autenticación «Obligatorios» y para los «Opcionales».
- [SDK de Xamarin 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Se ha añadido compatibilidad con .NET 9.0 para los enlaces iOS y Android.
        - Esto elimina la compatibilidad con .NET 8.0.
        - Para ello, se requiere una [versión mínima de iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0).
    - Actualización del enlace Android de [Braze Android 32.0.0 a 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Actualización del enlace iOS de [Braze SWIFT SDK 10.0.0 a 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Esta versión contiene API para la característica Banners, pero actualmente no es totalmente compatible con este SDK. Si deseas utilizar banners en tu aplicación .NET MAUI, ponte en contacto con tu administrador de atención al cliente antes de realizar la integración.
- [SDK de Cordova 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Se ha actualizado la implementación interna de iOS del`enableSdk`método  para utilizar `setEnabled`: en lugar de `_requestEnableSDKOnNextAppRun`, que quedó obsoleto en el SDK de SWIFT.
    - Al llamar a este método, ya no es necesario reiniciar la aplicación para que surta efecto. El SDK se habilitará tan pronto como se ejecute este método.
    - Se ha actualizado el puente nativo de Android desde [Braze Android SDK`36.0.0`a `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

{% enddetails %}
{% details July 22, 2025 %}

## Lanzamiento el 22 de julio de 2025.

### Exportación de eventos de seguridad con Amazon S3

Puedes [exportar]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/) automáticamente [los eventos de seguridad a Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/), un proveedor de almacenamiento en la nube, con una tarea diaria que se ejecuta a medianoche UTC. Una vez configurado, no es necesario exportar manualmente los eventos de seguridad desde el panel.

### Flexibilidad de los datos

#### Importación CSV

{% multi_lang_include release_type.md release="General availability" %}

Puedes utilizar la importación CSV para registrar y actualizar atributos de usuario y eventos personalizados en Braze, como `first_name`,`last_destination_searched` , y `trip_booked`. Para empezar, consulta [Importación CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### Alertas de uso de API

{% multi_lang_include release_type.md release="General availability" %}

Las alertas de uso de API proporcionan una visibilidad crítica del uso de tus API, lo que te permite detectar de forma proactiva el tráfico inesperado. Al configurar estas alertas para realizar el seguimiento de los volúmenes de solicitudes API clave, podrás recibir notificaciones en tiempo real y resolver los problemas antes de que afecten a tus campañas de marketing.

#### Límites de velocidad de la API del espacio de trabajo

Con los límites de velocidad de la API del espacio de trabajo, puedes establecer un número máximo de solicitudes de API que un espacio de trabajo puede realizar a un punto final de ingestión específico, como`/users/track`  o datos SDK. También puedes aplicar límites de velocidad a un grupo de espacios de trabajo, lo que significa que el límite se comparte entre todos los espacios de trabajo de ese grupo.

#### Eventos de New Currents

Se han añadido estos nuevos eventos al glosario de Currents:

- [Eventos de abortar banner]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Eventos de clic en banners]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Eventos de impresiones de banners]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [Banner Eventos vistos]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Eventos de fallo de webhook]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### Intervalo de tiempo predeterminado para el análisis de campañas

De forma predeterminada, el intervalo de tiempo para [**el análisis de campañas**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) mostrará los últimos 90 días desde el momento actual. Esto significa que si la campaña se lanzó hace más de 90 días, los análisis mostrarán «0» para el intervalo de tiempo indicado. Para ver todos los análisis de campañas anteriores, ajusta el intervalo de tiempo del informe.

#### Comportamiento actualizado para el paso de ruta de experimentos en Canvas

Si tu Canvas tiene un [experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) activo o en curso y actualizas el Canvas activo (aunque no sea en el paso «Ruta de experimentos»), el experimento en curso finalizará. Para reiniciar el experimento, puedes desconectar la ruta de experimentos existente e iniciar una nueva, o duplicar el Canvas y crear uno nuevo. 

Para más información, consulta [Editar Canvas después del lanzamiento]({{site.baseurl}}/post-launch_edits/).

#### Límite de velocidad más rápido disponible para`/users/export/ids`el punto final

También puedes aumentar el [límite de velocidad para el punto final /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) a 40 solicitudes por segundo si cumples los siguientes requisitos:

- Tu espacio de trabajo tiene habilitado el límite de velocidad predeterminado (250 solicitudes por minuto). Ponte en contacto con tu director de cuentas de Braze para obtener más ayuda sobre cómo eliminar cualquier límite de velocidad preexistente que puedas tener.
- Tu solicitud incluye elfields_to_exportparámetro para enumerar todos los campos que deseas recibir.

#### Nueva traducción para las plantillas de correo electrónico de los puntos finales.

{% multi_lang_include release_type.md release="Early access" %}

Utiliza estos puntos finales para ver y actualizar las traducciones y configuraciones regionales de las plantillas de correo electrónico:

- [GET: Ver las traducciones originales]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [GET: Ver una traducción y configuración regional específicas para el punto final de la plantilla de correo electrónico.]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_locale_template)
- [GET: Ver todas las traducciones y configuraciones de localización de una plantilla de correo electrónico]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_template)
- [PUT: Actualizar las traducciones de una plantilla de correo electrónico]({{site.baseurl}}/api/endpoints/translations/email_templates/put_update_template)

### Desbloquear la creatividad

#### Páginas de destino

Puedes hacer que tu página de destino [sea receptiva al tamaño del dispositivo del usuario]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) apilando verticalmente las columnas en pantallas más pequeñas. Para ello, añade una columna a la fila que deseas que sea receptiva y, a continuación, alterna la opción **Apilar verticalmente en pantallas más pequeñas** en la sección **Personalizar columnas**.

### Canales robustos

#### Filtrado de bots para correos electrónicos

{% multi_lang_include release_type.md release="General availability" %}

Configura el filtrado de bots en tus [preferencias de correo electrónico]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) para excluir todos los clics sospechosos de máquinas o bots. Un «clic de bot» en un correo electrónico se refiere a un clic en hipervínculos dentro de un correo electrónico generado por un programa automatizado. Al filtrar estos clics de bots, puedes desencadenar y entregar mensajes de forma intencionada a los destinatarios que están en interacción.

#### Bloques de productos arrastrar y soltar

{% multi_lang_include release_type.md release="Early access" %}

El [editor de arrastrar y soltar]({{site.baseurl}}/dnd_product_blocks/) te permite añadir y configurar rápidamente bloques de productos en tus mensajes para mostrar los productos fácilmente, sin necesidad de crear código Liquid personalizado. La característica de arrastrar y soltar bloques de productos solo está disponible actualmente para el correo electrónico.

#### Texto para páginas de destino y mensajes dentro de la aplicación

El texto Span te permite aplicar estilos específicos a bloques de texto sin necesidad de código personalizado para tus [páginas de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) y [mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks). Para ello, resalta el texto al que deseas aplicar el estilo y, a continuación, selecciona **Ajustar con span para el estilo**. 

#### Haz clic para enviar a WhatsApp

[Los anuncios que realizan un clic para dirigirse a WhatsApp]({{site.baseurl}}/whatsapp_use_cases/) son una forma eficaz de atraer tanto a clientes nuevos como a clientes existentes desde los anuncios de Meta en Facebook, Instagram u otras plataformas. Utiliza estos anuncios para promocionar tus productos y servicios, al tiempo que das a conocer tu presencia en WhatsApp a los usuarios. 

### Nuevas asociaciones Braze

#### API Visitory de Shopify — Comercio electrónico

Braze recopila información de los visitantes, como direcciones de correo electrónico y números de teléfono, a través de mensajes en el explorador. A continuación, esta información se envía a Shopify. Estos datos ayudan a los comerciantes a reconocer a los visitantes de su tienda y a crear una experiencia de compra más personalizada.

#### Okendo — Comercio electrónico

La integración de Braze y [Okendo]({{site.baseurl}}/partners/okendo/) funciona en múltiples productos de la plataforma de Okendo, incluyendo reseñas, fidelización, referidos, cuestionarios y encuestas. Okendo envía eventos personalizados y atributos del cliente a Braze, que pueden utilizarse para realizar personalización y desencadenar mensajes.

#### Lemnisk — Plataforma de datos de los clientes

La integración de Braze y [Lemnisk]({{site.baseurl}}/partners/lemnisk/) permite a las marcas y empresas aprovechar todo el potencial de Braze, ya que actúa como una capa de inteligencia basada en CDP que unifica los datos de usuario en todas las plataformas en tiempo real y envía la información y los comportamientos de los usuarios recopilados a Braze en tiempo real.

### Actualizaciones del SDK

Se han publicado las siguientes actualizaciones del SDK. Las actualizaciones de última hora se enumeran a continuación; todas las demás actualizaciones se pueden encontrar consultando los correspondientes registros de cambios del SDK.

- [SDK Web 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Se han eliminado las`Banner.html`propiedades  y`logBannerImpressions``logBannerClick` . En su lugar, utiliza[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner)  que gestiona automáticamente el seguimiento de impresiones y clics.
    - Se ha eliminado la compatibilidad con la característica heredada del canal de noticias. Esto incluye la eliminación de la clase Fuente y sus métodos asociados.
    - Los campos «created» y «categories» que utilizaban las tarjetas de canal de noticias heredadas se han eliminado de[`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)las subclases.
    - El campo linkText también se eliminó de la [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)subclase de tarjetas y de su constructor.
    - Se han aclarado las definiciones y actualizado los tipos para indicar que ciertos métodos del SDK devuelven explícitamente un valor indefinido cuando el SDK no está inicializado, alineando los tipos con el comportamiento real en tiempo de ejecución. Esto podría introducir nuevos errores de TypeScript en proyectos que dependían de los tipos anteriores (incompletos).
    - Las imágenes de los mensajes dentro de la aplicación con`cropType`  de`CENTER_CROP`  (como`FullScreenMessage`  predeterminado) ahora se representan mediante una`<img>`etiqueta  en lugar de`<span>`  para mejorar la accesibilidad. Esto puede romper las personalizaciones CSS existentes para la`.ab-center-cropped-img`clase o sus elementos secundarios.
- [SDK de Cordova 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Se ha actualizado la implementación interna de iOS del`enableSdk`método para utilizar setEnabled: en lugar de `_requestEnableSDKOnNextAppRun`, que quedó obsoleto en el SDK de SWIFT.
        - Al llamar a este método, ya no es necesario reiniciar la aplicación para que surta efecto. El SDK se habilitará tan pronto como se ejecute este método.
    - Actualización del puente nativo de Android [de Braze Android SDK 36.0.0 a 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK de Android 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [SDK de Swift 12.0.1-12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
