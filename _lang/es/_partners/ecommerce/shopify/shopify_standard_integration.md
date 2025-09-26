---
nav_title: Configuración de la integración estándar de Shopify
article_title: "Configuración de la integración estándar de Shopify"
description: "Este artículo de referencia describe cómo configurar la integración estándar de Shopify."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Configuración de la integración estándar de Shopify

> Esta página te explica cómo integrar Braze con Shopify utilizando nuestra integración estándar para usuarios con una tienda online en Shopify. Si utilizas un sitio web Shopify headless o buscas implementar soluciones más personalizadas, consulta [Configuración de la integración personalizada de Shopify]({{site.baseurl}}/shopify_custom_integration/).

## Paso 1: Conecta tu tienda Shopify

1. En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y busca "Shopify".

{% alert note %}
Si utilizas la navegación antigua, puedes encontrar a **los socios tecnológicos** en **Integraciones**.
{% endalert %}

{: start="2"}
2\. En la página del socio de Shopify, selecciona **Comenzar configuración** para iniciar el proceso de integración.<br><br>![Página de integración de Shopify con botón para comenzar la configuración.]({% image_buster /assets/img/Shopify/begin_setup.png %})<br><br> 
3\. En la tienda de aplicaciones de Shopify, instala la aplicación Braze.<br><br>![La página de la tienda de aplicaciones Braze con un botón para instalar la aplicación.]({% image_buster /assets/img/Shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
Si tu cuenta de Shopify está asociada a más de una tienda, puedes cambiar la tienda en la que has iniciado sesión seleccionando el icono de la tienda en la parte superior derecha de la página y seleccionando **Cambiar de tienda**.
{% endalert %}

{: start="4"}
4\. Tras instalar la aplicación Braze, se te redirigirá a Braze para que confirmes el espacio de trabajo que deseas conectar a Shopify. Una tienda Shopify sólo puede conectarse a un espacio de trabajo. Si necesitas cambiar, selecciona el espacio de trabajo correcto.<br><br>![Una ventana que te pide que confirmes que estás en el espacio de trabajo correcto.]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5\. Selecciona **Iniciar configuración**.<br><br>!["Configuración de la integración" con un campo para introducir el dominio y un botón para iniciar la configuración.]({% image_buster /assets/img/Shopify/choose_account.png %})

## Paso 2: Habilitación de los SDK Web de Braze

Para las tiendas online de Shopify, puedes seleccionar la configuración estándar para implementar automáticamente el SDK Web y el SDK JavaScript de Braze.

!["Habilitar Web SDK" paso con opciones para implementar a través de una configuración estándar o personalizada.]({% image_buster /assets/img/Shopify/sdk_setup.png %})

Después de seleccionar la ruta de incorporación de la configuración estándar, tendrás que elegir cuándo Braze debe inicializarse y cargar los SDK de una de las siguientes opciones: 
- En el momento de la visita, como el inicio de la sesión
    - Realiza un seguimiento tanto de los usuarios identificados como de los anónimos
- Al registrar la cuenta, como iniciar sesión en la cuenta
    - Rastrear solo a los usuarios identificados
    - Inicia el seguimiento de los datos cuando los visitantes del sitio se registran o acceden a sus cuentas

## Paso 3: Configura tus datos de Shopify

### Configuración de datos estándar

Ahora seleccionarás los datos de Shopify de los que quieres hacer seguimiento.

![Sección "Seguimiento de los datos de Shopify" con una casilla de verificación para seguir los eventos de comportamiento y los atributos de usuario.]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

Los siguientes eventos estarán habilitados por defecto en la integración estándar.

| Eventos recomendados por Braze | Shopify eventos personalizados | Atributos personalizados de Shopify |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Producto visto</li><li>Carrito actualizado</li><li>Pago iniciado</li><li>Pedido realizado</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_pedido_pagado</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_gastado</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_provincia</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

Para más información sobre los datos que se siguen a través de la integración, consulta [Características de los datos de Shopify]({{site.baseurl}}/shopify_data_features/).

### Configuración histórica del relleno

A través de la configuración estándar, tienes la opción de realizar una carga inicial de tus clientes y pedidos de Shopify de los últimos 90 días antes de tu conexión de integración con Shopify. Para ello, marca la casilla de verificación para incluir la carga inicial de datos como parte de tu integración. 

![Alternar el relleno de datos históricos.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

Esta tabla contiene los datos que se cargarán inicialmente a través del relleno.

| Eventos recomendados por Braze | Shopify eventos personalizados | Atributos estándar Braze | Estados de suscripción Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Pedido realizado</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_gastado</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_provincia</li></ul>{:/} | {::nomarkdown}<ul><li>Correo electrónico</li><li>Nombre</li><li>Apellido</li><li>Teléfono</li><li>Localidad</li><li>País</li></ul>{:/} | {::nomarkdown}<ul><li>Suscripciones de correo electrónico de marketing asociadas a esta tienda Shopify</li><li>Suscripciones de marketing por SMS asociadas a esta tienda Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

Cuando tus registros de cliente de Shopify se carguen en Braze, el ID de cliente de Shopify se utilizará como ID externo de Braze. 

{% alert note %}
Si ya eres cliente de Braze con campañas activas o Lienzos, revisa [las características de los datos de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) para obtener más detalles.
{% endalert %}

### (Avanzado) Configuración personalizada del seguimiento de datos

Con los SDK de Braze, puedes hacer un seguimiento de eventos personalizados o atributos personalizados que vayan más allá de los eventos estándar para esta integración. Los eventos personalizados capturan interacciones únicas en tu tienda, como:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">Eventos personalizados</th>
      <th style="width: 50%;">Atributos personalizados</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Usar un código de descuento personalizado</li>
          <li>Interactuar con una recomendación de productos personalizada</li>
          <li>Añadir un mensaje de regalo a su pedido</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Marcas o productos favoritos</li>
          <li>Categorías de compra preferidas</li>
          <li>Membresía o estado de fidelización</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

El seguimiento de datos de clientes te ayuda a obtener información más profunda sobre el comportamiento del usuario y a personalizar aún más su experiencia. Para implementar eventos personalizados, tienes que editar [el código del tema de](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) tu [tienda](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) en el archivo `theme.liquid`. Puede que necesites ayuda de tus desarrolladores.

Por ejemplo, el siguiente fragmento de código de JavaScript rastrea si el usuario actual se suscribe a un boletín de noticias y lo registra como un evento personalizado en su perfil de Braze:

```json
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@gmail.com’,
    sendOffers: true
  }
);

```

El SDK debe estar inicializado (a la escucha de la actividad) en el dispositivo de un usuario para registrar eventos o atributos personalizados. Para saber más sobre el registro de datos personalizados, consulta el [objeto Usuario](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) y el [objeto logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

## Paso 4: Configura cómo gestionas a los usuarios

Selecciona tu tipo de `external_id` en el desplegable. 

![Sección "Recoger suscriptores".]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
Utilizar una dirección de correo electrónico o una dirección de correo electrónico con hash como ID externo de Braze puede ayudarte a simplificar la gestión de identidades en todos tus orígenes de datos. Sin embargo, es importante tener en cuenta los riesgos potenciales para la privacidad de los usuarios y la seguridad de los datos.<br><br>

- **Información adivinable:** Las direcciones de correo electrónico son fáciles de adivinar, lo que las hace vulnerables a los ataques.
- **Riesgo de explotación:** Si un usuario malintencionado altera su navegador web para enviar la dirección de correo electrónico de otra persona como ID externo, podría acceder potencialmente a mensajes confidenciales o a información de la cuenta.
{% endalert %}

Si has seleccionado un tipo de ID externo personalizado, sigue los pasos 4.1 y 4.2. De lo contrario, continúa con el paso 4.3.

### Paso 4.1: Crear un personalizado `external_id`

Primero, ve a Shopify y crea el metacampo `braze.external_id`. Te recomendamos que sigas los pasos indicados en [Crear descripciones de metacampos personalizadas](https://help.shopify.com/en/manual/custom-data/metafields/metafield-definitions/creating-custom-metafield-definitions). Para **Espacio de nombres y clave**, introduce `braze.external_id`. Para el **Tipo**, te recomendamos que elijas un tipo de ID.

Después de crear el metacampo, escucha [los webhooks de`customer/create` ](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks) para que puedas escribir el metacampo cuando se cree un nuevo cliente. A continuación, utiliza [la API de administración](https://shopify.dev/docs/api/admin-graphql) o [la API de clientes](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para rellenar todos tus clientes creados previamente con este metacampo.

### Paso 4.2: Crear un punto final

Necesitas un punto final GET público para recuperar tu ID externo. Si Shopify no puede proporcionar el metacampo, Braze llamará a ese punto final para recuperar el ID externo.

Un ejemplo de punto final es `https://mystore.com/custom_id?shopify_customer_id=1234&email_address=raghav.narain@braze.com&shopify_storefront=dev-store.myshopify.com`

#### Respuesta

Braze espera un código de estado `200`. Cualquier otro código se considera un fallo del punto final. La respuesta debe ser:

{% raw %}
```json
{ "external_id": "my_external_id" }
```
{% endraw %}

Valida la dirección `shopify_customer_id` y la dirección de correo electrónico utilizando la API de administración o la API de cliente para confirmar que los valores de los parámetros coinciden con los valores del cliente en Shopify. Tras la validación, también podrías utilizar las API para recuperar el metacampo `braze.external_id` y devolver el valor del ID externo.

### Paso 4.3: Recoger tus adhesiones voluntarias por correo electrónico o SMS desde Shopify (opcional)

Tienes la opción de recopilar tus adhesiones voluntarias de marketing por correo electrónico o SMS desde Shopify. 

Si utilizas los canales de correo electrónico o SMS, puedes sincronizar tus estados de adhesión voluntaria por correo electrónico y marketing por SMS en Braze. Si sincronizas las adhesiones voluntarias de marketing por correo electrónico desde Shopify, Braze creará automáticamente un grupo de suscripción por correo electrónico para todos los usuarios asociados a esa tienda específica. Tienes que crear un nombre único para este grupo de suscripción.

![Sección "Recoger suscriptores" con opción de recoger las adhesiones voluntarias por correo electrónico o marketing por SMS.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
Como se menciona en el [resumen de Shopify]({{site.baseurl}}/shopify_overview/), si quieres utilizar un formulario de captura de terceros, tus desarrolladores necesitan integrar el código del SDK de Braze. Esto te permitirá capturar la dirección de correo electrónico y el estado global de suscripción por correo electrónico de los envíos de formularios. Concretamente, tienes que implementar y probar estos métodos en tu archivo `theme.liquid`:<br><br>
- [establecerCorreo](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Establece la dirección de correo electrónico en el perfil de usuario
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Actualiza el estado de la suscripción global por correo electrónico
{% endalert %}

## Paso 5: Sincronizar productos (opcional)

Puedes sincronizar todos los productos de tu tienda Shopify con un catálogo Braze para una mayor personalización de la mensajería. Las actualizaciones automáticas se producen casi en tiempo real para que tu catálogo refleje siempre los detalles más recientes de los productos. Para saber más, consulta la [sincronización de productos de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![Paso 4 del proceso de configuración con "Shopify Variant ID" como "Identificador del producto del catálogo".]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## Paso 6: Activar canales (opcional)

Puedes habilitar los mensajes dentro de la aplicación sin recurrir a un desarrollador configurándolos en tu configuración.

![Paso de configuración para activar canales, siendo la opción disponible la mensajería en el explorador.]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
Braze recopila información de los visitantes, como direcciones de correo electrónico y números de teléfono, a través de mensajes en el explorador. Esta información se envía a Shopify. Estos datos ayudan a los comerciantes a reconocer a los visitantes de su tienda y a crear una experiencia de compra más personalizada. Para más detalles, consulta la [API de Visitantes](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

### Compatibilidad con canales SDK adicionales

Los SDK de Braze habilitan varios canales de mensajería, incluidas las tarjetas de contenido.

#### Tarjetas de contenido y banderas de características

Para añadir tarjetas de contenido o banderas de características, tendrás que colaborar con tus desarrolladores para insertar el código SDK necesario directamente en tu archivo `theme.liquid`. Para obtener instrucciones detalladas, consulta [Integrar el SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/). 

#### Notificaciones push web

El push web no es compatible actualmente con la integración de Shopify. Si quieres que esto se admita en el futuro, envía una solicitud de producto a través del [portal de productos Braze]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

Si deseas que esto se admita en el futuro, envía una solicitud de producto a través del [portal de productos]({{site.baseurl}}/user_guide/administrative/access_braze/portal/) Braze.

## Paso 7: Configuración de acabado

1. Después de configurar tu configuración, selecciona **Finalizar configuración**.
2. Habilita la incrustación de la aplicación Braze en la configuración de tu tema de Shopify. Selecciona **Abrir Shopify** para ser redirigido a tu cuenta de Shopify y habilitar la incrustación de la aplicación en la configuración del tema de tu tienda. 

![Banner que dice que necesitas activar la incrustación de la aplicación Braze en Shopify y contiene un botón para abrir Shopify.]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3\. Después de habilitar la incrustación de la aplicación, ¡la configuración está completa!
Confirma que puedes ver tu configuración de integración, el estado de la sincronización inicial de datos y tus eventos de Shopify activos. <br><br>![Página del socio de Shopify que muestra la configuración de la integración.]({% image_buster /assets/img/Shopify/install_complete.png %})