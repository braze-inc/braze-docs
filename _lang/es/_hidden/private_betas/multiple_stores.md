---
nav_title: Soporte para varias tiendas
permalink: "/shopify_multiple_store/"
hidden: true
---

# Soporte para múltiples tiendas Shopify

> Conecta varias tiendas de Shopify a un único espacio de trabajo con nuestra nueva versión beta de compatibilidad con varias tiendas para tener una visión holística de tus clientes en todos los mercados. Construye y lanza programas y viajes de automatización en un único espacio de trabajo, sin duplicar esfuerzos en varias instancias. 

{% alert important %}
La compatibilidad con varias tiendas Shopify está disponible en versión beta, que puede contener errores. Esta característica está sujeta a cambios a medida que continúe el desarrollador.
{% endalert %}

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Crear un [grupo de suscripción por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group) para cada tienda | Una vez creado el grupo de suscripción por correo electrónico, lo designarás a la tienda específica durante el paso "[Recopilar suscriptores por correo electrónico o SMS]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers)" del flujo de configuración.<br><br>Esto es necesario para que puedas hacer un seguimiento del grupo de suscripción al correo electrónico de la tienda al que pertenecen tus usuarios por motivos de cumplimiento. |
| Audita y actualiza segmentos, campañas y Canvas utilizando los atributos de Shopify. | Los atributos personalizados recogidos de varias tiendas tendrán el formato de un objeto anidado, que difiere de la estructura actual utilizada en la integración general de Shopify, que tiene el formato de un valor de cadena. Como resultado, tendrás que actualizar todos los segmentos, campañas o Canvas al nuevo formato después de conectar varias tiendas para utilizar el filtro "Atributo personalizado anidado" o actualizar el evento desencadenante "Cambiar atributo personalizado".<br><br>Si hoy no utilizas ninguno de los atributos, puedes ignorar esto. |
| Auditar y actualizar el alias de Shopify | El alias `shopify_customer_id` se migrará a {% raw %}`shopify_customer_id_{{storename}}`{% endraw %} cuando conectes más de una tienda. Asegúrate de que actualizas los sistemas internos para que utilicen el nuevo alias. El alias anterior, `shopify_customer_id`, quedará obsoleto. Si hoy no utilizas el alias, puedes ignorar esto. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integración
Con el soporte para múltiples tiendas de Braze, puedes:
- Ten una visión de 360° de tus clientes en todas las tiendas
- Crea segmentos de tus clientes con datos agregados de la tienda 
- Configura mensajes o recorridos a medida que tus clientes se mueven por diferentes tiendas
- Gestiona las suscripciones por correo electrónico y SMS en diferentes tiendas

{% alert important %}
Admitir varias marcas en un mismo espacio de trabajo aumenta la probabilidad de que se dupliquen los perfiles de usuario, ya que los usuarios pueden comprar entre esas marcas. Sugerimos colocar cada marca en su propio espacio de trabajo.
{% endalert %}

### Configurar una tienda adicional
1. Después de instalar tu primera tienda, selecciona la opción **\+ Conectar nueva tienda**.<br>![][1]{: style="max-width:70%;"}<br><br>
2. Repasa el flujo de incorporación de esta nueva tienda. Puedes encontrar más detalles en nuestra guía [Configurar Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/).<br><br>Ten en cuenta que la configuración de la tienda anterior puede conservarse, pero puedes actualizar la configuración en consecuencia a medida que avances en tu incorporación.<br><br>
3. Para el paso de recopilar suscriptores de correo electrónico o SMS:
- Para recopilar adecuadamente las suscripciones por correo electrónico y SMS de cada tienda, debes asignar grupos de suscripción únicos a la configuración de cada tienda. 
- Te sugerimos que **no** habilites la opción "Anular el estado global existente para los usuarios", ya que puede cancelar suscripción de forma global a tus clientes si han interactuado con más de una de tus tiendas.<br><br>
4. Repite esta instalación para tantas tiendas como necesites.<br><br>
5. Para ver la integración de cada tienda y configurar los ajustes avanzados, haz clic en una tienda del menú desplegable:<br>![][2]{: style="max-width:70%;"}

## Datos de Shopify

### Alias de Shopify

{% raw %}Después de conectar más de una tienda, todos los usuarios entrantes de Shopify tendrán un nuevo alias, `shopify_customer_id_{{storename}}` además del alias existente, `shopify_customer_id`. Ten en cuenta que `shopify_customer_id` es un alias heredado y quedará obsoleto cuando esta característica esté disponible de forma general. Deberías pasar a utilizar el nuevo alias en adelante. {% endraw %}

### Atributos personalizados de Shopify

Después de conectar más de una tienda, los siguientes atributos se sincronizarán como un objeto anidado que contiene el valor por tienda y el valor agregado:
- `shopify_tags`
- `shopify_order_count` (sólo disponible a través del Relleno Histórico)
- `shopify_total_spent` (sólo disponible a través del Relleno Histórico)

Para utilizar eventos personalizados al crear o editar un segmento, selecciona el filtro **Atributo personalizado anidado** y localiza tu atributo anidado. Si necesitas ayuda para identificar la ruta o el campo concreto del objeto, utiliza la herramienta [Generar esquema]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#generate-schema). Después de seleccionar los atributos anidados, aparecerá un campo con un botón más junto a los atributos seleccionados para que especifiques la ruta. Para saber más sobre los atributos anidados, consulta [Atributos personalizados anidados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/).

![3]{:style="max-width:70%;"}

Puedes especificar tu ruta escribiéndola en el campo o haciendo clic en el botón más y seleccionando la ruta.

![4]{:style="max-width:70%;"}

### Shopify eventos personalizados

Después de conectar más de una tienda, los eventos personalizados entrantes de Shopify contendrán ahora una nueva propiedad de evento, `shopify_storefront`. Consulta el [procesamiento de datos de Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events) para ver todos los eventos personalizados que admite esta integración. Esta propiedad del evento proporciona el dominio de la tienda Shopify de la que procede el evento.

### Entrega basada en acciones o seguimiento de la conversión

Para desencadenar la mensajería a los usuarios que completen acciones con una tienda específica:

1. Ve al paso **Programar entrega** de tu campaña.
2. Selecciona **Realizar evento personalizado** como evento desencadenante.
![5]{:style="max-width:70%;"}
3. Selecciona un evento de Shopify como evento desencadenante, como **shopify_created_order**, y la casilla de verificación **Añadir filtros de propiedades**.
![6]{:style="max-width:70%;"}
4. Selecciona **Propiedad básica** en el desplegable **Añadir filtro**.
5. Selecciona **shopify_storefront** e introduce el dominio completo de Shopify de la tienda.
![7]{:style="max-width:70%;"}


### Fusión y sincronización de usuarios de Shopify

Si el ID de cliente de Shopify, la dirección de correo electrónico o el número de teléfono del usuario ya existen en Braze utilizando el alias, {% raw %}`shopify_customer_id_{{storefront_domain}}`, `shopify_email`, o `shopify_phone`, {% endraw %} entonces actualizaremos el perfil de usuario existente. Si esos alias no existen en Braze, crearemos un nuevo perfil de usuario. Ten en cuenta que es posible que los datos de un usuario (por ejemplo, la ciudad) difieran en varias tiendas Shopify para el mismo usuario. En tales casos, Braze siempre actualizará el perfil de usuario de la tienda con la actividad más reciente. 

{% alert warning %}
Braze actualizará el perfil de usuario con los datos de clientes de Shopify de la tienda con la actividad más reciente. Esto significa que cualquier atributo, como correo electrónico, número de teléfono, teléfono de envío, ciudad, etc., puede sobrescribirse con la actividad más reciente de la tienda. Por ejemplo, si un usuario tiene un número de teléfono diferente en dos tiendas distintas, Braze actualizará el perfil de usuario con el número de teléfono de la tienda con la actividad más reciente.
{% endalert %}

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
[3]: {% image_buster /assets/img/shopify_nested_attributes.png %}
[4]: {% image_buster /assets/img/shopify_tags.png %}
[5]: {% image_buster /assets/img/shopify_add_trigger.png %}
[6]: {% image_buster /assets/img/shopify_select_event.png %}
[7]: {% image_buster /assets/img/shopify_enter_storefront.png %}
