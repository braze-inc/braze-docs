{% if include.alert == "Shopify deprecation" %}

{% alert important %}
A partir de abril de 2025, se lanzará una [nueva versión de la integración con Shopify]({{site.baseurl}}/partners/shopify/#new-shopify-integration) por fases. Las fases se basarán en el tipo de tienda Shopify y en el ID externo utilizado para configurar la integración inicial. <br><br>**La versión antigua de la integración dejará de estar disponible después del 28 de agosto de 2025. Actualiza a la nueva versión antes de esta fecha para seguir utilizando la integración sin ningún problema.**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
Las ventanas de navegación privada no admiten notificaciones push web.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
Añadir una dirección BCC a tu campaña o Canvas hace que se dupliquen los correos electrónicos facturables para la campaña o el componente Canvas, ya que Braze envía un mensaje a tu usuario y otro a tu dirección BCC.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
La configuración de prioridad de visualización de notificaciones ya no se utiliza en dispositivos con Android O o versiones posteriores. En estos dispositivos, configura la prioridad a través de [la configuración del canal de notificaciones](https://developer.android.com/training/notify-user/channels#importance).
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
No envíes correos electrónicos transaccionales legalmente requeridos a las pasarelas SMS, ya que es muy probable que esos correos electrónicos no se entreguen.
<br><br>
Aunque los correos electrónicos que envías utilizando un número de teléfono y el dominio de la pasarela del proveedor (conocido como MM3) pueden hacer que el correo electrónico se reciba como un mensaje SMS (de texto), algunos de nuestros proveedores de correo electrónico no admiten este comportamiento. Por ejemplo, si envías un correo electrónico a un número de teléfono de T-Mobile (como "9999999999@tmomail.net"), tu mensaje SMS se enviará a quien posea ese número de teléfono en la red de T-Mobile.
<br><br>
Ten en cuenta que aunque estos correos electrónicos no se entreguen a la pasarela de SMS, seguirán contando para tu facturación por correo electrónico. Para evitar enviar correos electrónicos a pasarelas no admitidas, revisa la [lista de nombres de dominio de pasarelas no admitidas](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
Para mayor seguridad, te recomendamos que añadas nuestra característica [de Autenticación SDK]({{site.baseurl}}/developer_guide/authentication/) para evitar la suplantación de identidad de usuarios.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Hay ciertos navegadores, como las aplicaciones Naver para Android e iOS, que no son compatibles con el centro de preferencias de Braze. Si prevés que algunos de tus usuarios utilizan estos navegadores, considera la posibilidad de proporcionarles métodos alternativos para gestionar sus preferencias de correo electrónico.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
Los planes para eliminar gradualmente el evento de compra se anunciarán en 2026. El evento de compra acabará siendo sustituido por nuevos [eventos recomendados para el comercio electrónico]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), que incluirán características mejoradas para la segmentación, la elaboración de informes, el análisis y mucho más. Sin embargo, los nuevos eventos de comercio electrónico no admitirán las características existentes relacionadas con el evento de compra, como el valor de duración del ciclo de vida (LTV) o los informes de ingresos en lienzos o campañas. Para obtener una lista completa de las características relacionadas con los eventos de compra, consulta [Registro]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events) de [eventos de compra]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
Los planes para eliminar gradualmente el evento de compra se anunciarán en 2026. El evento de compra acabará siendo sustituido por nuevos [eventos recomendados para el comercio electrónico]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), que incluirán características mejoradas para la segmentación, la elaboración de informes, el análisis y mucho más. Cuando esto ocurra, los filtros de segmento ya no aparecerán en el comportamiento de compra. Para obtener una lista completa de los eventos de compra, consulta [Registro]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events) de [eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Los archivos de exportación almacenados en los contenedores de S3 se eliminan automáticamente una vez que caduca el enlace de descarga (cuatro horas después del envío del correo electrónico de exportación, a menos que se indique lo contrario).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
La integración de Shopify admite webhooks de creación y actualización de clientes de Shopify, que se encuentran en la configuración de datos. Cuando se crea o actualiza un perfil de usuario en Shopify, se creará o actualizará el perfil de usuario correspondiente en Braze. <br><br>Estas acciones no desencadenan eventos personalizados en Braze y se utilizan únicamente para [sincronizar los datos de usuario de Shopify con Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works). Los datos sincronizados incluyen [atributos personalizados]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), [atributos estándar]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes) y, si está habilitado en tu configuración, [estados de grupos de suscripción]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Las propiedades de entrada de Canvas forman parte de las variables de contexto de Canvas. Esto significa que`canvas_entry_properties`  se referencia como `context`. Cada`context`variable incluye un nombre, un tipo de datos y un valor que puede incluir Liquid. Actualmente,`canvas_entry_properties`  son compatibles con versiones anteriores. Para obtener más información, consulta [Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) y [Objeto de contexto Canvas]({{site.baseurl}}/api/objects_filters/context_object).
{% endalert %}

{% endif %}

{% if include.alert == 'Braze Agents' %}

{% alert important %}
Este socio aparece en tu página **de socios tecnológicos** solo si tienes habilitados [los agentes de Braze]({{site.baseurl}}/user_guide/brazeai/agents/). Para obtener ayuda para empezar, ponte en contacto con tu administrador del éxito del cliente.
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**Elegir entre los tipos de filtro «Día del año» y «Hora**»: Al filtrar variables de contexto que contienen fechas, elige el tipo de comparación correcto en función de si la fecha se repite cada año:

- **Utiliza «Día del año»** cuando la fecha se repita cada año (por ejemplo, cumpleaños, aniversarios o fiestas como Navidad). Este tipo de comparación calcula en función del día del año (1-365/366), ignorando el componente del año.
- **Utiliza «Hora»** cuando la fecha sea una fecha absoluta que no se repita (por ejemplo, fechas de finalización de contratos, fechas de citas o fechas de renovación de suscripciones). Este tipo de comparación se calcula basándose en la marca de tiempo completa, incluido el año.

El uso de «Día del año» para fechas absolutas puede producir resultados incorrectos o inesperados, ya que el cálculo ignora el componente del año. Por ejemplo, si comparas la fecha de vencimiento de un contrato de futuros en abril para determinar si está dentro de los 63 días, el uso de «Día del año» puede hacer que las fechas coincidan incorrectamente, ya que solo compara los números de los días (119 frente a 359) sin tener en cuenta que, en realidad, quedan 188 días para abril.

**Directriz general**: ¿La fecha se repite cada año? **Sí** → Usa «Día del año». **No** → Usa «Tiempo».
{% endalert %}

{% endif %}

{% if include.alert == 'granular permissions ea' %}

{% alert important %}
Los permisos granulares se encuentran en fase de acceso anticipado. Cuando se planifique la migración para tu empresa, los administradores de Braze recibirán correos electrónicos y banners en el panel de control notificándoles la [migración]({{site.baseurl}}/granular_permissions_migration/) de [permisos granulares]({{site.baseurl}}/granular_permissions_migration/).
{% endalert %}

{% endif %}