---
nav_title: Información general de Shopify
article_title: "Información general de Shopify"
description: "Este artículo de referencia describe la asociación con Braze y Shopify, una empresa de comercio global que te permite conectar fácilmente su tienda Shopify con Braze para pasar determinados webhooks de Shopify a Braze. Aprovecha las estrategias Braze multicanal y Canvas para animar a los clientes a completar sus compras o reorientar a los usuarios en función de sus compras anteriores."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Información general de Shopify

> [Shopify](https://www.shopify.com/) es una empresa líder en comercio global que proporciona herramientas de confianza para iniciar, hacer crecer, comercializar y administrar un negocio de cualquier tamaño. Shopify hace que el comercio sea mejor para todos con una plataforma y unos servicios diseñados para ser fiables y entregar una mejor experiencia de compra a los consumidores de todo el mundo.

La integración de Braze con Shopify proporciona una potente solución para las empresas de comercio electrónico que buscan mejorar su interacción con los clientes e impulsar esfuerzos de marketing personalizados. Esta integración conecta fácilmente las sólidas capacidades de comercio electrónico de Shopify con nuestra avanzada plataforma de interacción con los clientes, habilitándote para entregar mensajes específicos, relevantes y oportunos a tus usuarios, basados en comportamientos de compra en tiempo real y datos de transacciones.

## Requisitos

| Requisito | Descripción |
| --- | --- |
| Tienda de Shopify | Tienes una tienda Shopify activa. |
| Permisos del propietario o del personal de la tienda Shopify | {::nomarkdown}<ul><li>Accede a todas las configuraciones Generales y de la Tienda Online.</li><li> Permisos de administrador adicionales:</li><ul><li>Pedidos: Visualizar</li><li>Cliente: LecturaEscritura</li><li>Ver eventos de clientes (píxeles Web)</li><li>Administrar configuración</li><li>Ver aplicaciones desarrolladas por personal/colaboradores</li><li>Administrar/Instalar aplicaciones y canales</li><li>Administrar/Añadir píxeles personalizados</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cómo integrar 

Braze ofrece dos opciones de integración para los comerciantes de Shopify que están diseñadas para satisfacer las diversas necesidades de las empresas de comercio electrónico: **Integración estándar** e **integración personalizada**.

{% multi_lang_include shopify.md section='Integration Tabs' %}

## Cómo funciona la integración

Si ya has configurado y activado el relleno histórico en tus ajustes de configuración, la sincronización inicial de datos comenzará inmediatamente. Braze importará todos los clientes y eventos de pedidos realizados de los últimos 90 días anteriores a tu conexión de integración con Shopify. Cuando Braze importe tus clientes de Shopify, les asignaremos el tipo `external_id` que hayas elegido en tus ajustes de configuración.

Si planeas realizar la integración con un ID externo personalizado (ya sea para la [integración estándar]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users) o para la [integración personalizada]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)), deberás añadir tu ID externo personalizado como metacampo de cliente de Shopify a todos los perfiles de cliente de Shopify existentes y, a continuación, realizar el [relleno histórico]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill). 

Tras la sincronización inicial de datos, Braze hará un seguimiento continuo de los nuevos datos y actualizaciones, directamente desde los SDK de Shopify y Braze.

{% alert note %}
Si ya eres cliente de Braze con campañas o Lienzos activos, revisa [el histórico de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) para obtener información importante. Para ver qué datos específicos de clientes se están rellenando, consulta las [características de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).
{% endalert %}

### Sincronización de usuarios y datos

Una vez que la integración esté en vivo, Braze recopilará datos de usuario de dos fuentes clave a través de la integración de Shopify:
- **API de píxeles Web de Shopify e incrustaciones de aplicaciones:** Esto impulsa el SDK Web y el SDK Javascript de Braze para dar soporte al seguimiento in situ, la gestión de identidades, los datos de comportamiento del comercio electrónico y potenciar canales de mensajería como los mensajes dentro de la aplicación.
- **Webhooks de Shopify:** datos de comportamiento de comercio electrónico, sincronización de productos y recopilación de suscriptores

Durante la incorporación de la integración, tendrás que seleccionar cuándo los SDK de Braze se inicializan y cargan tu sitio de Shopify: 
- En el momento de la visita (como el inicio de la sesión)
    - **Qué hace:** Realiza un seguimiento de los usuarios anónimos -como los compradores invitados- para acceder a más datos que permitan una personalización más profunda. 
- Al registrar la cuenta (como iniciar sesión en la cuenta) 
    - **Qué hace:** Impide el seguimiento del usuario anónimo para un enfoque más conservador y orientado a la privacidad, de modo que la actividad del usuario se sigue *después de* que éste inicie sesión en su cuenta.

{% alert note %}
- Las visitas al sitio web (sesiones) cuentan para tu asignación de usuarios activos al mes (MAU).
- Las versiones de Braze Web SDK y JavaScript SDK se establecerán automáticamente en v5.4.0.
{% endalert %}

Braze utiliza la integración de Shopify para dar soporte a múltiples identificadores que siguen a tus usuarios desde su experiencia de compra como invitados hasta que se convierten en usuarios identificados:

| Identificador de Braze | Descripción |
| --- | --- |
| Braze `device_id` | Un ID generado aleatoriamente y almacenado en el navegador que realiza un seguimiento de la actividad del usuario anónimo a través de los SDK de Braze. |
| Cart token alias de usuario | Un alias que Braze crea para realizar un seguimiento de los eventos de actualización del carrito. Este token se crea utilizando el token de carrito de Shopify. |
| Alias de usuario del token de pago | Un alias que Braze crea cuando el usuario inicia el proceso de pago. Este token se crea utilizando el token de pago de Shopify. |
| Alias del ID de cliente de Shopify | El ID de cliente de Shopify se asigna como alias cuando se asigna el ID externo al iniciar sesión en la cuenta o al realizar un pedido. |
| Braze `external_id` | Un identificador único que ayuda a seguir a los clientes a través de dispositivos y plataformas. Esto mantiene una experiencia de usuario consistente y mejora los análisis al evitar múltiples perfiles cuando los usuarios cambian de dispositivo o reinstalan la aplicación.<br><br>La integración de Shopify admite los siguientes tipos de `external_id`: <br><br>{::nomarkdown}<ul><li>ID de cliente de Shopify (predeterminado)</li><li>ID externo personalizado</li><li>Correo electrónico codificado (SHA-256)</li><li>Correo electrónico codificado (SHA-1)</li><li>Correo electrónico codificado (MD5)</li><li>Correo electrónico</li></ul>{:/}Braze asigna un `external_id` a tus usuarios llamando al método changeUser dentro de los SDKs cuando: <br><br>{::nomarkdown}<ul><li>Un usuario se conecta o crea una cuenta</li><li>Se hace un pedido</li></ul>{:/}<br> Para más información sobre lo que ocurre cuando asignas un `external_id` a un perfil anónimo, consulta [Ciclo de vida del perfil de usuario]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>Braze también aprovechará el `external_id` para atribuir los datos de comportamiento de comercio electrónico de los webhooks de Shopify.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La integración requiere que los SDK de Braze y los servicios de Shopify trabajen juntos para seguir y atribuir adecuadamente los datos de Shopify a los usuarios adecuados en tiempo casi real. Para obtener más información sobre los datos que se siguen a través de la integración, consulta [Datos de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

{% alert note %}
- Si estás probando la integración, te aconsejamos que utilices el modo de incógnito o borres las cookies para restablecer la dirección Braze `device_id` e imitar el comportamiento de un usuario anónimo.
- Aunque se genera un ID de cliente de Shopify cuando se introduce un correo electrónico en el pie de página del boletín de noticias de Shopify o durante el proceso de pago antes de realizar un pedido, ese ID de cliente no es accesible a través de los Píxeles Web de Shopify. Por ello, Braze no puede utilizar el método `changeUser` en estas dos situaciones.
{% endalert %}

### Sincronización de las adhesiones voluntarias al correo electrónico y al marketing por SMS de Shopify

Si habilitas la recopilación de suscriptores en tus ajustes de configuración, tendrás que asignar un grupo de suscripción para cada tienda que conectes a Braze. Esto significa que tus clientes se clasificarán como "suscritos" o "dados de baja" en el grupo de suscripción de tu tienda.

El estado de adhesión voluntaria al marketing por correo electrónico y SMS de Shopify se puede actualizar de las siguientes maneras:
- **Actualización manual:** Puedes cambiar manualmente el estado de adhesión voluntaria al marketing por correo electrónico o SMS de un usuario en tu administrador de Shopify.
- **Pie de página del boletín de Shopify:** Si un usuario introduce su correo electrónico en el pie de página predeterminado del boletín de Shopify, se actualizará su estado de adhesión voluntaria.
- **Proceso de pago:** Si un usuario actualiza su estado de adhesión voluntaria durante la compra.

{% alert note %}
El estado de adhesión voluntaria al marketing por correo electrónico de Shopify no cambiará el [estado de suscripción global al correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) de un usuario en Braze. El estado predeterminado de suscripción cuando se crea un perfil de usuario es "suscrito". Recuerda utilizar el grupo de suscripción como parte de los criterios de entrada de tu campaña o Canvas.
{% endalert %}

Esta tabla muestra qué estados de adhesión voluntaria al marketing de Shopify se correlacionan con los estados dentro de tu grupo de suscripción Braze. 

| Shopify marketing adhesión voluntaria estado | Estado del grupo de suscripción Braze |
| --- | --- |
| El correo electrónico está suscrito | Suscrito |
| El correo electrónico está desuscrito | No suscrito |
| El correo electrónico está pendiente de confirmación | No suscrito |
| El correo electrónico no es válido | No suscrito |
| SMS suscrito | Suscrito |
| SMS cancelar suscripción | No suscrito |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Formularios de registro

#### Pie de página del boletín de Shopify

Los usuarios que introduzcan su dirección de correo electrónico en el pie de página del boletín de Shopify experimentarán uno de estos flujos de trabajo:

##### Usuarios que no han iniciado sesión en su cuenta

1. Braze recibe un webhook entrante de Shopify cada vez que se crea o actualiza un cliente.
2. Braze crea un perfil de usuario que contiene la dirección de correo electrónico y el alias de ID de cliente de Shopify que están asociados a ese usuario.
3. El SDK de Braze actualiza el perfil anónimo con la dirección de correo electrónico.

{% alert note %}
Esto puede dar lugar a un perfil duplicado hasta que el usuario se identifique creando su cuenta, accediendo a ella o realizando un pedido. Braze ofrece herramientas de fusión masiva para ayudarte a automatizar la conciliación de perfiles duplicados. Consulta [Duplicar usuarios]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/) para más detalles.
{% endalert %}

##### Usuarios que ya han iniciado sesión en su cuenta

Braze creará un perfil de usuario que contenga la dirección de correo electrónico y el alias de ID de cliente de Shopify que están asociados a ese usuario. Braze no actualizará la dirección de correo electrónico del usuario conectado, porque suponemos que Shopify ya ha proporcionado esta información.

#### Formularios de registro Braze

Braze proporciona dos tipos de plantillas de formulario de registro:
- **[Formularios de registro por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/email_capture/):** Créalos utilizando el editor de arrastrar y soltar.
- **[Formulario de captura de correo electrónico del editor tradicional]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/):** Un formulario más sencillo para captar direcciones de correo electrónico.

Cuando utilizas estas plantillas de formulario de registro, Braze actualiza automáticamente el estado global de suscripción por correo electrónico en el perfil de usuario. Para más detalles sobre cómo se gestiona el estado global de suscripción por correo electrónico, incluida información sobre la validación del correo electrónico, consulta la documentación de cada tipo de plantilla de formulario.

{% alert note %}
- Asegúrate de incluir criterios de entrada en tu campaña o Canvas que incluyan tanto el estado de suscripción global por correo electrónico como el grupo de suscripción que están conectados a tu tienda de Shopify. Esto te ayudará a asegurarte de que te diriges a la audiencia adecuada. 
- Braze recopila información de los visitantes, como direcciones de correo electrónico y números de teléfono, a través de mensajes en el explorador. Esta información se envía a Shopify. Estos datos ayudan a los comerciantes a reconocer a los visitantes de su tienda y a crear una experiencia de compra más personalizada. Para más detalles, consulta la [API de Visitantes](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Formularios de registro de terceros 

Si utilizas una plataforma de terceros o un plugin de Shopify para tus formularios de registro, tienes que trabajar con tus desarrolladores para integrar el código SDK de Braze para capturar la dirección de correo electrónico y el estado global de suscripción por correo electrónico de los envíos de formularios. Para saber más, revisa la [configuración de integración estándar de Shopify]({{site.baseurl}}/shopify_standard_integration/) y [la configuración de integración personalizada de Shopify]({{site.baseurl}}/shopify_custom_integration/).

### Sincronización de productos 

Braze permite sincronizar los productos de tu tienda Shopify en un catálogo Braze. Para más detalles, consulta [Sincronización de productos de Shopify]({{site.baseurl}}/shopify_catalogs/).

## Solicitudes del interesado

Como parte de la integración de la plataforma Braze con Shopify, Braze recibe automáticamente [los webhooks de cumplimiento de Shopify](https://shopify.dev/docs/apps/build/privacy-law-compliance/). Sin embargo, dado que los clientes son los responsables del tratamiento de los datos de sus Usuarios finales, los clientes deben llevar a cabo todas las acciones necesarias para responder a las Solicitudes del Sujeto de Datos recibidas con respecto a los datos del Usuario final en Braze (incluidos los datos del Usuario final recibidos a través de la integración de Shopify). Para más detalles, consulta nuestra documentación de [Asistencia Técnica sobre Protección de Datos]({{site.baseurl}}/dp-technical-assistance).