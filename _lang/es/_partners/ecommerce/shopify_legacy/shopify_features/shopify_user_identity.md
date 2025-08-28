---
nav_title: Gestión de identidades de usuarios de Shopify
article_title: "Gestión de identidades de usuarios de Shopify"
description: "Este artículo de referencia describe la función de gestión de identidades de usuario de Shopify."
page_type: partner
search_tag: Partner
alias: "/shopify_user_identity/"
page_order: 3
---

# Gestión de identidades de usuarios de Shopify

> Braze recibirá señales de tus clientes de Shopify a través de sus comportamientos en el sitio y escuchando los webhooks de Shopify que configuraste como parte de tu integración. En el caso de los sitios Shopify sin encabezado, Braze ayudará a conciliar a los usuarios desde la página de pago. Para los sitios de Shopify sin encabezado, consulta nuestra guía de integración sobre cómo [conciliar los usuarios del proceso de compra]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#headless-checkout).

{% multi_lang_include alerts.md alert='Shopify obsoleto' %}

## Captura de información para perfiles de usuario 

### Seguimiento de usuarios de Shopify

Si los visitantes de tu tienda son invitados (es decir, anónimos), Braze capturará la dirección `device_id` para las sesiones de esos clientes en particular. Después de configurar la conciliación de usuarios para los formularios de Shopify durante la [implementación del SDK Web]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk), los correos electrónicos de los clientes se añadirán a los perfiles de usuarios anónimos cada vez que los clientes introduzcan su información en un formulario. 

Cada vez que los visitantes de la tienda introduzcan su correo electrónico en un boletín de Shopify o en un formulario de captura de correo electrónico, Braze recibirá un evento webhook de Shopify para crear el perfil de usuario. A continuación, Braze fusiona este perfil de usuario con el perfil de usuario anónimo rastreado por el SDK web y asigna el ID de cliente de Shopify como alias de usuario en el perfil de usuario. 

A medida que los clientes avanzan en el proceso de compra y proporcionan otra información identificable, como números de teléfono, Braze debe capturar los datos relevantes del usuario desde los webhooks de Shopify y fusionarlos con el usuario anónimo con el `device_id`.
- Si implementaste el SDK web a través de Shopify ScriptTag, en un sitio Shopify sin encabezado o a través de Google Tag Manager, Braze se asegurará automáticamente de que los datos de usuario de la página de pago y los datos de sesión del perfil de usuario anónimo se fusionen en el perfil de alias de usuario con el ID de cliente de Shopify asignado.
- Si has implementado el SDK Web en un sitio sin encabezado de Shopify, debes asegurarte de que los datos de usuario enviados dentro de la página de pago se asignen correctamente al perfil de usuario correcto a través del SDK Web o de la API. Para obtener más información, consulta [Implementación del SDK Web directamente en tu sitio web de Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#headless-site).

A medida que los clientes continúan el proceso de pago, Braze comprueba si la dirección de correo electrónico, el número de teléfono o el ID de cliente de Shopify introducidos coinciden con un perfil de usuario existente. Si hay una coincidencia, Braze sincroniza los datos del usuario de Shopify con ese perfil.

Si la dirección de correo electrónico o el número de teléfono están asociados a varios perfiles de usuario identificados, Braze sincroniza los datos de Shopify con el perfil con la actividad más reciente.

Si Braze no encuentra ninguna coincidencia para la dirección de correo electrónico o el número de teléfono, Braze crea un nuevo perfil de usuario con los datos de Shopify compatibles.

### Cuando los clientes de Shopify se sincronizan con Braze

Braze actualiza los perfiles de usuario existentes o crea nuevos perfiles para clientes potenciales, inscripciones y registros de cuentas capturados en tu tienda Shopify. Puedes recopilar datos de perfil de usuario de los siguientes métodos en Shopify y otros:
- El cliente crea una cuenta
- La dirección de correo electrónico o el número de teléfono del cliente se recopila en un formulario de captura de Shopify
- La dirección de correo electrónico del cliente se recopila de un formulario de boletín informativo
- La dirección de correo electrónico o el número de teléfono del cliente se recopilan a través de una herramienta de terceros que está conectada a Shopify, como EcomSend

Braze intentará primero asignar los datos de Shopify compatibles a cualquier perfil de usuario existente utilizando la dirección de correo electrónico o el número de teléfono del cliente. 

Para evitar perfiles de usuario duplicados, es fundamental que revises las instrucciones de conciliación de usuarios para Shopify Forms correspondientes al método que utilizaste para [implementar el SDK Web en tu sitio web de Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk).

## Fusión de perfiles de usuario 

{% alert note %}
La integración predeterminada de Shopify proporciona herramientas para ayudar a fusionar tu perfil de usuario anónimo y el perfil de alias de Shopify. Si estás implementando la integración a un sitio de Shopify sin encabezado, revisa [Implementación del SDK Web directamente en su sitio de Shopify sin encabezado]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=headless%20shopify%20site#supported-features) para confirmar que estás conciliando correctamente a tus usuarios. <br><br> Si encuentras perfiles de usuario duplicados, puedes utilizar nuestra [herramienta de fusión masiva]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#bulk-merging/) para ayudarte a racionalizar sus datos.
{% endalert %}

Braze fusiona los campos del perfil de usuario anónimo con el perfil de usuario identificado cuando encontramos una coincidencia con uno de los siguientes datos:
- ID de cliente de Shopify
- Correo electrónico
- Número de teléfono

Braze fusiona los siguientes campos del perfil de usuario anónimo con el perfil de usuario identificado:
- Nombre
- Apellido
- Correo electrónico
- Género
- Fecha de nacimiento
- Número de teléfono
- Huso horario
- Ciudad de origen
- País
- Idioma
- Atributos personalizados
    - Datos personalizados de eventos y compras (excluidas las propiedades de los eventos, el recuento y las marcas de fecha de inicio y fin)
    - Propiedades personalizadas de eventos y eventos de compra para la segmentación "X veces en Y días" (donde X<=50 e Y<=30)
- Tokens de notificaciones push
- Historial de mensajes
- Cualquiera de los siguientes campos encontrados en el perfil de usuario anónimo o en el perfil de usuario identificado, como evento personalizado, recuento de eventos de compra y marcas de tiempo de primera fecha y última fecha
    - Estos campos fusionados actualizarán los filtros "para X eventos en Y días". Para los eventos de compra, estos filtros incluyen "número de compras en Y días" y "dinero gastado en los últimos Y días".

{% alert important %}
Los datos de sesión aún no se admiten como parte del proceso de fusión.
{% endalert %}

## Sincronización de suscriptores de Shopify

Durante el proceso de configuración de Shopify, Braze proporciona controles flexibles para sincronizar las direcciones de correo electrónico y los estados de suscripción por SMS de tus clientes con los grupos de suscripción y los estados de suscripción de los perfiles de usuario de Braze. 

### Recopilación de suscriptores por correo electrónico o SMS

Durante la configuración de la tienda Shopify en Braze, tendrá la opción de sincronizar tus suscriptores de correo electrónico y SMS de Shopify en Braze. 

#### Recopilar suscriptores de correo electrónico

Para activar la recopilación de suscriptores de correo electrónico, activa la función en la configuración de Shopify. Te recomendamos que asignes al menos un [grupo de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#subscription-groups) Braze, como los suscriptores de correo electrónico de Shopify. Braze añadirá tus suscriptores de correo electrónico a los grupos de suscripción especificados para que se incluyan en la segmentación de tu público cuando envíes un mensaje. 

![]({% image_buster /assets/img/Shopify/collect_email.png %})

Cuando esté activado, Braze sincronizará las actualizaciones de tus suscriptores de correo electrónico de Shopify y las actualizaciones de sus estados de suscripción de correo electrónico en tiempo real. Si no activas la opción de anulación, tus clientes de Shopify se suscribirán o anularán la suscripción del grupo de suscripción asociado a tu tienda Shopify.

Si activas la opción de anulación, Braze actualizará el estado de suscripción global en el perfil de usuario. Esto significa que si tus clientes están marcados como no suscritos en Shopify, Braze marcará el estado de suscripción global como no suscrito en el perfil del usuario y dará de baja al cliente de todos los grupos de suscripción por correo electrónico disponibles. En consecuencia, no se enviarán mensajes a los usuarios que se hayan dado de baja globalmente del correo electrónico.

#### Recopilar suscriptores de SMS

Para recopilar suscriptores de SMS de Shopify, debes crear [grupos de suscripción de SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) como parte de tu [configuración de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/sms_setup/sms_sending/). 

Cuando estés listo para recopilar tus suscriptores SMS de Shopify, habilita la recopilación de suscriptores SMS activándola dentro de la página de configuración de Shopify. Debes seleccionar al menos un grupo de suscripción SMS para poder orientar y enviar adecuadamente los mensajes SMS. 

![]({% image_buster /assets/img/Shopify/collect_sms.png %})

Cuando esté activado, Braze sincronizará las actualizaciones de tus suscriptores de SMS de Shopify y sus estados de suscripción de SMS en tiempo real. Si no activas la opción de anulación, tus clientes de Shopify se suscribirán o anularán la suscripción del grupo de suscripción asociado a tu tienda Shopify.

Los suscriptores de SMS no tienen estados de suscripción globales, por lo que no es necesario tenerlos en cuenta al utilizar una opción de anulación. Un usuario solamente puede darse de baja o de alta en un grupo de suscripción SMS.

#### Atributos personalizados heredados

Los clientes antiguos de Shopify pueden tener el antiguo método de recopilar suscriptores de correo electrónico y SMS a través de los atributos personalizados `shopify_accepts_marketing` y `shopify_sms_consent`. Si guardas la configuración anterior con la anulación activada, Braze eliminará los atributos personalizados de los perfiles de usuario y sincronizará esos valores con sus respectivos grupos de suscripción por correo electrónico y SMS.

Si tienes campañas o Canvas existentes que utilizan estos atributos personalizados heredados, elimínalos y confirma que las campañas o los Canvas utilizan el estado de suscripción, el grupo o ambos de forma correcta.
