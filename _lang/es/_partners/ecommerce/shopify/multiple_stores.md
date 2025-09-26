---
nav_title: Conectar varias tiendas
article_title: Soporte para múltiples tiendas en Shopify
alias: /shopify_connecting_multiple_stores/
page_order: 5
description: "Este artículo de referencia explica cómo conectar y configurar varias tiendas Shopify a un único espacio de trabajo."
---

# Conectar varias tiendas Shopify

> Conecta varios dominios de tiendas Shopify a un único espacio de trabajo para tener una visión holística de tus clientes en todos los mercados. Construye y lanza programas y viajes de automatización en un único espacio de trabajo sin duplicar esfuerzos en las tiendas regionales.  

{% alert important %}
Esta característica no es compatible con Shopify Markets o Markets Pro. Si quieres solicitar asistencia para ellos, envía una [solicitud de producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% endalert %}

## Requisitos

| Requisito | Descripción |
| ----------- | ----------- |
| Habilitación de múltiples tiendas | Ponte en contacto con tu administrador del éxito del cliente para habilitar la compatibilidad con múltiples tiendas de Shopify. |
| Configurar una tienda Shopify | Asegúrate de que ya has [configurado al menos una tienda de Shopify con Braze]({{site.baseurl}}/shopify_overview/). |
| Dominios de tienda Shopify únicos para cada región | El soporte para múltiples tiendas está pensado para usarse con dominios de tienda Shopify únicos para diferentes escaparates regionales. <br><br>Si quieres conectar varias submarcas a Braze, te recomendamos que crees espacios de trabajo separados para cada submarca. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Conectar una tienda adicional
Después de instalar la aplicación Braze en tu tienda Shopify e instalar tu primera tienda, selecciona **\+ Conectar nueva tienda**.

![El botón "+ Conectar nueva tienda" en la página de integración de Shopify.]({% image_buster /assets/img/Shopify/begin_setup_button.png %}){: style="max-width:80%;"}

Para tu tienda regional adicional de Shopify, selecciona **Comenzar configuración**.

![La sección "Configuración de la integración" con un botón para "Comenzar la configuración".]({% image_buster /assets/img/Shopify/multiple_stores.png %}){: style="max-width:80%;"}

Como en la primera integración de tu tienda Shopify, puedes elegir entre una configuración estándar o personalizada.

!["Habilitar los SDK Braze" sección con opciones para implementar el SDK Braze Web con la configuración estándar o personalizada.]({% image_buster /assets/img/Shopify/standard_or_custom.png %}){: style="max-width:80%;"}

Elige la opción que mejor se adapte a tus necesidades:

{% multi_lang_include shopify.md section='Integration Tabs' %}

Para ver la integración de cada tienda y configurar los ajustes avanzados, selecciona una tienda en el menú desplegable.

!["Configuración de integración" con un menú desplegable para seleccionar una tienda Shopify.]({% image_buster /assets/img/Shopify/store_dropdown_menu.png %})

## Sincronización de usuarios entre tiendas

### Alias de Shopify

Cuando conectes varias tiendas, los usuarios de Shopify sincronizados que hayan iniciado sesión o realizado un pedido recibirán un nuevo alias con el formato: {% raw %}`shopify_customer_id_{{storename}}`{% endraw %}.

### Braze ID externo

Puedes elegir entre las siguientes opciones para tu ID externo Braze:

|Opción|Descripción|
|------|-----------|
|ID de cliente de Shopify|Si utilizas el ID de cliente de Shopify como ID externo de Braze, cada tienda generará un ID de cliente único para cada usuario. Esto significa que si un usuario interactúa con varias tiendas, tendrá perfiles distintos en Braze.|
|Correo electrónico, correo electrónico codificado o ID externo personalizado|Si utilizas los tipos de correo electrónico, correo electrónico con hash o ID externo personalizado, los perfiles de los usuarios que interactúan con varias tiendas se fusionarán en un único perfil consolidado cuando se conecten o realicen un pedido.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Campos fusionados

Cuando se sincroniza un perfil de usuario, se fusionan los siguientes campos. Para más detalles sobre el [comportamiento de la fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior), consulta [Comportamiento de la fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

- Información sobre el dispositivo
- Recuento total de sesiones (combinado de ambos perfiles)
- Datos personalizados de eventos y compras
- Propiedades del evento personalizadas para la segmentación (por ejemplo, "X veces en Y días" donde X ≤ 50 e Y ≤ 30)
- Recuento de eventos (combinado de ambos perfiles)
- Fechas de los primeros y últimos eventos (Braze selecciona la fecha más temprana y la más tardía)
- Datos de interacción de la campaña (campos de fecha más recientes)
- Resúmenes del flujo de trabajo (campos de fecha más recientes)
- Historial de mensajes e interacciones
- Grupos de suscripción

### Recoger suscriptores (opcional)

Puedes elegir recopilar suscriptores directamente a través de Braze (en la configuración de tu conector de Shopify) o a través de alternativas de API y SDK que sincronizan los datos desde Shopify.

{% tabs local %}
{% tab Conector Shopify %}
En el paso **Administrar usuarios** de la configuración de tu conector de Shopify, puedes utilizar Braze para recopilar las adhesiones voluntarias de suscriptores por correo electrónico y SMS y organizarlas en un grupo de suscripción dedicado:

1. Crea un grupo de suscripción único para cada tienda que conectes. Esto te ayuda a mantener datos precisos sobre la procedencia de los suscriptores.
2. Habilita la recogida de suscriptores por correo electrónico y SMS.
{% endtab %}

{% tab API o SDK Braze %}
Alternativamente, puedes sincronizar la información de adhesión al marketing por correo electrónico y SMS directamente desde Shopify utilizando la API o los SDK de Braze.

|Opción|Recursos|
|------|---------|
|API |- [Puntos finales de grupo de suscripción]({{site.baseurl}}/api/endpoints/subscription_groups/) para sustituir directamente lo que admite la integración<br>- [`Users/track` punto final]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#set-subscription-groups) para configurar los datos del grupo de suscripción o el [estado global de suscripción al correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#subscription-states)<br>- [Centro de preferencias Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/overview/) para más opciones personalizadas de recogida de adhesiones voluntarias de marketing|
|SDK |- [`NotificationSubscriptionTypes`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#notificationsubscriptiontypes)<br>- [`addToSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)<br>- [`removeFromSubscriptionGroup`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#removefromsubscriptiongroup)<br>- [`setEmailNotificationSubscriptionType`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype)|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}
{% endtabs %}

## Datos de Shopify 

### Atributos sincronizados

Cuando conectes más de una tienda, los siguientes atributos se sincronizarán con el estado más reciente del perfil de Shopify:
- Nombre
- Apellido
- Correo electrónico
- Género
- Fecha de nacimiento
- País
- Localidad
- Última aplicación usada
- Idioma
- Zona horaria
- Etiquetas Shopify
- Recuento de pedidos de Shopify
- Total gastado en Shopify

### Eventos subvencionados

#### Eventos recomendados en eCommerce 

Cuando conectes varias tiendas, los eventos recomendados de comercio electrónico entrantes incluirán una propiedad de evento de origen. Esta propiedad identifica la URL de la tienda en la que se originó el evento, lo que te permite utilizar esta información para la segmentación o para desencadenar casos de uso específicos.

![Un Canvas basado en acciones con un desencadenante para introducir a los usuarios que realizan el evento personalizado `ecommerce.order_placed`.]({% image_buster /assets/img/Shopify/ecommerce_order_placed.png %}){: style="max-width:80%;"}

Los eventos recomendados de comercio electrónico compatibles con la integración de Shopify son:

- `ecommerce.product_viewed`
- `ecommerce.cart_updated`
- `ecommerce.checkout_started`
- `ecommerce.order_placed`
- `ecommerce.order_cancelled`
- `ecommerce.order_refunded`

#### Shopify eventos personalizados 

Los eventos personalizados entrantes de Shopify incluyen una propiedad de evento llamada `shopify_storefront`. Esta propiedad indica de qué URL del escaparate procede el evento, lo que te permite aprovecharla para la segmentación o para desencadenar casos de uso.

![Un Canvas basado en acciones con un desencadenante para introducir a los usuarios que realizan el evento personalizado `shopify_paid_order`.]({% image_buster /assets/img/Shopify/shopify_paid_order.png %}){: style="max-width:80%;"}

Los eventos personalizados de Shopify compatibles son:

- `shopify_fulfilled_order`
- `shopify_partially_fulfilled_order`
- `shopify_paid_order`
- `shopify_account_login`

Para obtener un resumen completo de todas las cargas útiles de eventos, consulta las [características de los datos de Shopify]({{site.baseurl}}/shopify_data_features/).

### Sincronización de productos en Shopify 

Cuando conectas y configuras cada tienda de Shopify en Braze, puedes habilitar opcionalmente la sincronización de productos de Shopify como parte de la integración.

Si activas la sincronización de productos para cada tienda, Braze incluirá el nombre de tu tienda Shopify en el nombre del catálogo. Esto te ayuda a distinguir los productos de diferentes tiendas.

![Catálogos de Shopify con su tienda Shopify a su nombre.]({% image_buster /assets/img/Shopify/catalog_store_name.png %})

