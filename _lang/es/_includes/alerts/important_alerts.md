{% if include.alert == "Shopify deprecation" %}

{% alert important %}
Una [nueva versión de la integración con Shopify]({{site.baseurl}}/partners/shopify/#new-shopify-integration) se lanzará por fases a partir de abril de 2025. Las fases se basarán en el tipo de tienda Shopify y en el ID externo utilizado para configurar la integración inicial. <br><br>**La versión antigua de la integración dejará de estar disponible a partir del 28 de agosto de 2025. Actualiza a la nueva versión antes de esta fecha para seguir utilizando la integración sin problemas.**
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
Hay ciertos navegadores, como las aplicaciones Naver para Android e iOS, que no son compatibles con el centro de preferencias Braze. Si prevés que algunos de tus usuarios utilizan estos navegadores, considera la posibilidad de proporcionarles métodos alternativos para gestionar sus preferencias de correo electrónico.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
Los planes para eliminar gradualmente el acto de compra se anunciarán a finales de 2025. A largo plazo, el evento de compra será sustituido por nuevos [eventos recomendados de comercio electrónico]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), que vendrán con características mejoradas de segmentación, informes, análisis y mucho más. Sin embargo, los nuevos eventos de comercio electrónico no serán compatibles con las características existentes relacionadas con el evento de compra, como el valor de duración (LTV) o los informes de ingresos en Lienzos o campañas. Para obtener una lista completa de las características relacionadas con los eventos de compra, consulta [Registrar eventos de compra]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Los archivos de exportación almacenados en los contenedores de S3 se eliminan automáticamente cuando caduca el enlace de descarga (cuatro horas desde que se envía el correo electrónico de exportación, a menos que se indique lo contrario).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
La integración de Shopify es compatible con los webhooks de creación y actualización de clientes de Shopify, que se encuentran en tus ajustes de configuración de datos. Cuando se cree o actualice un perfil de usuario en Shopify, se creará o actualizará el correspondiente perfil de usuario en Braze. <br><br>Estas acciones no desencadenan eventos personalizados en Braze y se utilizan únicamente para [sincronizar los datos de usuario de Shopify con Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works). Los datos sincronizados incluyen [atributos personalizados]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), [atributos estándar]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes) y, si están habilitados en tu configuración, [estados de grupo de suscripción]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Si participas en el acceso anticipado al Contexto de Canvas, las propiedades de entrada de Canvas forman parte de las variables de contexto de Canvas. Esto significa que `canvas_entry_properties` se denomina ahora `context`. Cada variable contextual incluye un nombre, un tipo de datos y un valor que puede incluir Liquid. Actualmente, `canvas_entry_properties` sigue siendo compatible con versiones anteriores. Para más detalles, consulta [Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) y [objeto contextual Canvas]({{site.baseurl}}/api/objects_filters/context_object).
{% endalert %}

{% endif %}