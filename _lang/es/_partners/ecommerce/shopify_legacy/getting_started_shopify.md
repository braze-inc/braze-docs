---
nav_title: Guía de inicio
article_title: "Primeros pasos con Shopify"
description: "Este artículo de referencia describe cómo implementar el SDK Braze Web en tu sitio web de Shopify."
page_type: partner
search_tag: Partner
alias: /getting_started_shopify_legacy/
page_order: 1
---

# Primeros pasos con Shopify

> Este artículo describe cómo implementar el SDK Braze Web en tu sitio web de Shopify. Después de la implementación, consulte [Configuración de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview) para aprender a terminar de configurar la integración de Shopify con Braze.

{% multi_lang_include alerts.md alert='Shopify obsoleto' %}

## Lista de comprobación para la integración

1. [Implementar el SDK Web Braze](#implement-web-sdk)
2. [Configurar Shopify en Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview)
3. Probar la integración con Shopify

## Implementación del SDK Web en tu sitio web de Shopify {#implement-web-sdk}

El [SDK para Web de Braze]({{site.baseurl}}/user_guide/getting_started/web_sdk/) es una potente herramienta utilizada para hacer un seguimiento del comportamiento de los clientes de tu tienda Shopify. Con el SDK Web, puede recopilar datos de sesión, identificar usuarios y registrar datos de comportamiento de los usuarios desde un navegador web o móvil. También puedes desbloquear canales de mensajería nativos como los mensajes dentro del navegador.

Aunque la integración de Shopify ofrece un robusto conjunto de características por defecto, ten en cuenta que si tienes casos de uso para añadir seguimiento in situ para [eventos no soportados por la integración de Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/using_shopify/shopify_data_in_braze/) o quieres añadir canales como [Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards), necesitas implementar el Web SDK directamente en tu sitio de Shopify.

Antes de comenzar la incorporación de la integración, revisa lo siguiente con tu equipo sobre qué camino quieres seguir para implantar el SDK Web.

### Características compatibles

|Ícono| Definición 
|-------------|-------------
|<i aria-hidden="true" class="fas fa-check" title="Apoyado"></i><span class="sr-only">Apoyado</span> | Apoyado
|<i aria-hidden="true" class="fas fa-times" title="No admitido"></i><span class="sr-only">Compatible</span> | No se admite
{: .reset-td-br-1 .reset-td-br-2 role="presentation" } 

| Características | SDK web a través de Shopify ScriptTag | Integración directa del SDK web a través de theme.liquid | Integración directa de SDK Web a través de Shopify Hydrogen
|-------------|-------------|-------------|------------
| Seguimiento in situ por defecto      | <i class="fas fa-check" title="Con soporte"></i> | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-times" title="Sin soporte"></i>          
| Conciliación del usuario del formulario de captura (Requiere poca ingeniería)   | <i class="fas fa-check" title="Con soporte"></i> | <i class="fas fa-check" title="Con soporte"></i> | <i class="fas fa-times" title="Sin soporte"></i> 
| Conciliación de usuarios de compra     | <i class="fas fa-check" title="Con soporte"></i>  | <i class="fas fa-times" title="Sin soporte"></i>   | <i class="fas fa-times" title="Sin soporte"></i>                                        
| Producto visto<br> Producto clicado<br> Carrito abandonado   | <i class="fas fa-check" title="Con soporte"></i> |<i class="fas fa-check" title="Con soporte"></i> | <i class="fas fa-times" title="Sin soporte"></i> 
| Compra abandonada<br> Pedido creado<br> Compra de Braze<br> Pedido pagado<br> Pedido parcialmente cumplido<br> Pedido cumplido<br> Pedido cancelado<br> Reembolso creado<br> Creación y actualización de clientes | <i class="fas fa-check" title="Con soporte"></i> | <i class="fas fa-check" title="Con soporte"></i> | <i class="fas fa-check" title="Con soporte"></i>
| Relleno histórico | <i class="fas fa-check" title="Con soporte"></i>  | <i class="fas fa-check" title="Con soporte"></i>  | <i class="fas fa-check" title="Con soporte"></i>  
| Sincronización de catálogos  |<i class="fas fa-check" title="Con soporte"></i> |<i class="fas fa-check" title="Con soporte"></i>  |<i class="fas fa-check" title="Con soporte"></i>
| Recogida de suscriptores por correo electrónico y SMS    | <i class="fas fa-check" title="Con soporte"></i>| <i class="fas fa-check" title="Con soporte"></i>  | <i class="fas fa-check" title="Con soporte"></i>     
| Soporte de mensajes in-app por defecto   | <i class="fas fa-check" title="Con soporte"></i>  | <i class="fas fa-check" title="Con soporte"></i>  | <i class="fas fa-times" title="Sin soporte"></i>     
| Tarjetas de contenido predeterminadas   | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-times" title="Sin soporte"></i>   
| Compatibilidad predeterminada con web push     | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-times" title="Sin soporte"></i> | <i class="fas fa-times" title="Sin soporte"></i>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }    

{% tabs %}
{% tab ScriptTag Shopify %}

### Implementación de Braze Web SDK a través de Shopify ScriptTag

[Shopify ScriptTag](https://shopify.dev/api/admin-rest/2021-10/resources/scripttag#top) es un código JavaScript remoto que se carga en las páginas de tu tienda o en la página de estado del pedido en el checkout. Cuando se carga la página de una tienda, Shopify comprobará si es necesario cargar alguna etiqueta de script en la página del sitio. 

Si quieres empezar a usar Braze rápidamente, tienes la opción de permitir que Braze cargue un script predefinido para el SDK Braze Web directamente en el sitio de tu tienda Shopify.

{% alert important %}
El script predefinido para Braze Web SDK para este método de integración no es personalizable.
{% endalert %}

#### Cómo funciona con la integración de Shopify

Cuando se carga tu página de Shopify, Shopify comprobará si es necesario cargar alguna etiqueta de script en la página. Durante el proceso, los scripts de Braze Web SDK se cargarán en las páginas de su tienda o en la página de estado del pedido de pago. 

También añadiremos scripts predefinidos si has seleccionado eventos de producto visto, producto clicado y carrito abandonado que requieran Shopify ScriptTag o mensajería in-app como canal.  

#### Cómo activar

Para habilitar automáticamente los scripts Braze Web SDK como parte de tu integración, selecciona los eventos Shopify ScriptTag compatibles o habilita la mensajería in-app como canal durante la [configuración de tu integración con Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview). 

Desde el compositor de configuración de Shopify, los eventos marcados con un asterisco (\*) son soportados por el SDK Web. Si selecciona estos eventos o incluye mensajería dentro del navegador, Braze añadirá la implementación del SDK web a través de Shopify ScriptTag a su tienda Shopify como parte de su configuración.

#### Formularios de captura de correo electrónico de Shopify y reconciliación de usuarios 

Los formularios de captura obtienen información identificable sobre el cliente en una fase temprana del ciclo de vida de éste para su posterior envío de mensajes y compromiso. 

El SDK de la Web realiza un seguimiento del comportamiento en el sitio de Shopify y de los usuarios anónimos utilizando la dirección `device_id`. La integración Braze Shopify ScriptTag asigna correos electrónicos de formularios de captura de correo electrónico de Shopify, como la suscripción a un boletín, a la dirección `device_id` del usuario.

Los formularios típicos de captura de correo electrónico incluyen: 
- Formulario de captura de correo electrónico 
- Formulario de suscripción al boletín

Hay dos formas de conciliar el correo electrónico del usuario y `device_id`: 
- Utilizando el script Braze de captura automatizada de correo electrónico 
- Llamada a los métodos `setEmail` o `setPhoneNumber` 

##### Captura de suscripciones por correo electrónico o teléfono

Con Braze, puedes utilizar nuestros formularios de inscripción [por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) y [SMS y WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) para aprovechar el SDK web y los mensajes in-app. 

Si utilizas un formulario de captura de correo electrónico o número de teléfono de Shopify, o un formulario de captura de terceros, puedes configurarlo directamente en el usuario al que realiza el seguimiento el SDK de la Web de Braze. Por ejemplo, si obtiene la dirección de correo electrónico del cliente, puede establecerla en su perfil de usuario de la siguiente manera:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

Para más detalles sobre la configuración de estos valores, consulte estos recursos de Javascript:

- Establecer el [correo electrónico](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) del usuario
- Establecer el [número de teléfono](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) del usuario

También puede establecer el estado de suscripción de los usuarios a medida que recopila su correo electrónico o número de teléfono, de esta forma:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

Para más detalles sobre la configuración de estos valores, consulte estos recursos de Javascript:

- Establecer el [tipo de suscripción de notificación por correo electrónico](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) del usuario
- Añadir el usuario a un [grupo de suscripción](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Ejemplo de implementación de formulario de captura de terceros**

1. En `theme.liquid`, copie el siguiente fragmento en `head tag`:

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\. Primero llamamos a `setInterval` para que el script se cargue primero
3\. Sustituya `{FORM_ID}` por el ID del elemento del formulario que desea capturar
(como "PieDeContacto").
4\. Sustituya `{INPUT_EMAIL_ID}` por el ID del elemento del campo de entrada de correo electrónico dentro del formulario.
5\. Cuando se envíe el formulario, el script llamará a `setEmail` con el valor de la entrada de correo electrónico
6\. Después de cargar el guión, llamamos a `clearInterval` para que sólo se cargue una vez.

{% alert note %}
En este momento, el formulario de captura de correo electrónico Braze no creará un cliente de Shopify. Como resultado, podrías tener perfiles de usuario Braze sin perfiles de usuario Shopify asociados hasta que el cliente pase por caja o cree una cuenta.
{% endalert %}

#### Qué esperar tras la aplicación

**Inicialización del SDK Web Braze**

El SDK Web se inicializará al iniciar la sesión. Braze necesitará recopilar `device_id` para rastrear datos de usuarios anónimos, ya que otros identificadores como el ID de cliente de Shopify, el correo electrónico o el número de teléfono pueden no estar fácilmente disponibles para los visitantes invitados de su tienda Shopify.

`device_id` también se utilizará para conciliar los datos del usuario con el perfil de usuario anónimo cuando un cliente proporcione más información identificable (como una dirección de correo electrónico o un número de teléfono) después del proceso de pago.

**Versión del SDK Web de Braze**

La versión actual del SDK de la Web de Braze a través de la integración de Shopify ScriptTag es la v4.2.

**Usuarios activos mensuales (MAU)**

El SDK Web rastrea las sesiones de tus clientes y huéspedes de Shopify. Como resultado, esto se acumulará como MAU en los informes del panel de control de Braze y en sus asignaciones de MAU. Es importante tener en cuenta que los usuarios anónimos también contarán para su MAU. En el caso de los dispositivos móviles, los usuarios anónimos dependen del dispositivo. En el caso de los internautas, los usuarios anónimos dependen de la caché del navegador.

{% endtab %}

{% tab tema Liquid %}

### Implementar el SDK Web directamente en el sitio web de Shopify theme.liquid

Braze ofrece múltiples formas de implementar el SDK Web, entre ellas:
- Añadir el SDK Web directamente a tu archivo de Shopify `theme.liquid` 
- Google Tag Manager 

Si ya tienes el Web SDK instalado en tu tienda Shopify, puedes proceder con la configuración del Shopify ScriptTag dentro del proceso de onboarding. 

Durante el proceso de instalación, Braze comprobará si ya hay instancias del SDK web disponibles en tu tienda Shopify. Si existe una implementación, Braze no cargará los scripts predefinidos para habilitar el SDK Web. A continuación, añadiremos los scripts necesarios para asegurarnos de que puede realizar un seguimiento de los eventos seleccionados o activar la mensajería dentro del navegador.

#### Cómo activar

Para implementar manualmente el SDK Web, consulta [Configuración inicial del SDK]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web). Para implementar el SDK para Web a través de Google Tag Manager, consulta [Google Tag Manager para Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/google_tag_manager#google-tag-manager). 

Con cualquier ruta de implementación, asegúrese de que su integración Web SDK incluye lo siguiente o la integración de Shopify no será compatible: 
- Versión del SDK Web de v4.0+
- El SDK Web se inicializa al iniciar la sesión

#### Formularios de captura de correo electrónico de Shopify y reconciliación de usuarios 

Los formularios de captura obtienen información identificable sobre el cliente en una fase temprana del ciclo de vida de éste para su posterior envío de mensajes y compromiso. 

El SDK de la Web realiza un seguimiento del comportamiento en el sitio de Shopify y de los usuarios anónimos utilizando la dirección `device_id`. La integración Braze Shopify ScriptTag asigna correos electrónicos de formularios de captura de correo electrónico de Shopify, como la suscripción a un boletín, a la dirección `device_id` del usuario.

Los formularios típicos de captura de correo electrónico incluyen: 
- Formulario de captura de correo electrónico 
- Formulario de suscripción al boletín

Hay dos formas de conciliar el correo electrónico del usuario y `device_id`: 
- Utilizando el script Braze de captura automatizada de correo electrónico 
- Llamada a los métodos `setEmail` o `setPhoneNumber` 

##### Captura de suscripciones por correo electrónico o teléfono

Con Braze, puedes utilizar nuestros formularios de inscripción [por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/#step-1-create-an-in-app-message-campaign) y [SMS y WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) para aprovechar el SDK web y los mensajes in-app. 

Si utiliza una captura de correo electrónico o número de teléfono de Shopify, o un formulario de captura de terceros, se puede establecer directamente en el objeto de usuario que es rastreado por el SDK Braze Web. Por ejemplo, si obtiene la dirección de correo electrónico del cliente, puede establecerla en su perfil de usuario de la siguiente manera:

{% raw %}
```javascript
braze.getUser().setEmail(<email address>);
```
{% endraw %}

Para más detalles sobre la configuración de estos valores, consulte estos recursos de Javascript:

- Establecer el [correo electrónico](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) del usuario
- Establecer el [número de teléfono](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setphonenumber) del usuario

También puede establecer el estado de suscripción de los usuarios a medida que recopila su correo electrónico o número de teléfono de esta manera:

{% raw %}
```javascript
braze.getUser().setEmailNotificationSubscriptionType(braze.User.NotificationSubscriptionTypes.SUBSCRIBED);
```
{% endraw %}

Para más detalles sobre la configuración de estos valores, consulte estos recursos de Javascript:

- Establecer el [tipo de suscripción de notificación por correo electrónico](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype) del usuario
- Añadir el usuario a un [grupo de suscripción](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup)

**Ejemplo de implementación de formulario de captura de terceros**

1. En `theme.liquid`, copie el siguiente fragmento en `head tag`:

{% raw %}
```javascript
<script>
  const emailInputPoller = setInterval(()=>{
    if (document.getElementById('{FORM_ID}')) {
      document.getElementById('{FORM_ID}').addEventListener("submit",
        function() {  
          var email = document.getElementById('{INPUT_EMAIL_ID}').value
          braze.getUser().setEmail(email)
        }
      );
    }
    clearInterval(emailInputPoller)
  }, 2000)
</script>
```
{% endraw %}

{: start="2"}
2\. Primero llamamos a `setInterval` para que el script se cargue primero
3\. Sustituya `{FORM_ID}` por el ID del elemento del formulario que desea capturar
(como "PieDeContacto").
4\. Sustituya `{INPUT_EMAIL_ID}` por el ID del elemento del campo de entrada de correo electrónico dentro del formulario.
5\. Cuando se envíe el formulario, el script llamará a `setEmail` con el valor de la entrada de correo electrónico
6\. Después de cargar el guión, llamamos a `clearInterval` para que sólo se cargue una vez.

{% alert note %}
En este momento, el formulario de captura de correo electrónico Braze no creará un cliente de Shopify. Como resultado, podrías tener perfiles de usuario Braze sin perfiles de usuario Shopify asociados hasta que el cliente pase por caja o cree una cuenta.
{% endalert %}

#### Qué esperar tras la integración

**Inicialización del SDK Web Braze**

El SDK Web se inicializará al iniciar la sesión. Braze necesitará recopilar `device_id` para rastrear datos de usuarios anónimos, ya que otros identificadores como el ID de cliente de Shopify, el correo electrónico o el número de teléfono pueden no estar fácilmente disponibles para los visitantes invitados de su tienda Shopify.

`device_id` también se utilizará para conciliar los datos del usuario con el perfil de usuario anónimo a medida que el cliente proporcione más información identificable (como su correo electrónico o número de teléfono) durante y después del proceso de compra.

**Versión del SDK Web de Braze**

La versión actual del SDK de la Web de Braze debe ser v4.0+.

**Usuarios activos mensuales (MAU)**

El SDK Web rastrea las sesiones de tus clientes e invitados de Shopify. Como resultado, esto se acumulará como MAU en los informes del panel de control de Braze y en sus asignaciones de MAU. Es importante tener en cuenta que los usuarios anónimos también contarán para su MAU. En el caso de los dispositivos móviles, los usuarios anónimos dependen del dispositivo. En el caso de los internautas, los usuarios anónimos dependen de la caché del navegador.

{% endtab %}
{% tab Sitio Shopify sin encabezado %}

### Implementar el SDK Web directamente en tu sitio web de Shopify sin encabezado {#headless-site}

La integración Braze Shopify ScriptTag es incompatible con los sitios de Shopify sin encabezado. Como resultado, no podrá obtener soporte por defecto para los eventos de producto visto, producto pulsado o carrito abandonado, ni habilitar la mensajería dentro de la aplicación a través de nuestros scripts predefinidos. 

#### Cómo activar

Para integrar directamente el SDK Web en tu sitio web de Shopify, consulta [Configuración del SDK Inital para Web]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=web).

Asegúrate de que tu integración de SDK Web incluye lo siguiente: 
- La versión del Web SDK debe ser v4.0+.
- El SDK Web se inicializa al iniciar la sesión

#### Configurar formularios de Shopify para la conciliación de usuarios

Es probable que las marcas de comercio electrónico tengan experiencias en su sitio de Shopify para capturar información identificable de los clientes antes del pago, como formularios de captura de correo electrónico.

El SDK Web realiza un seguimiento del comportamiento en el sitio de Shopify y de los usuarios anónimos con la dirección `device_id`. Para confirmar que las direcciones de correo electrónico se añaden al perfil de usuario anónimo, añada lo siguiente a un boletín o formulario de captura de correo electrónico: 
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail) 
  - Para captar correos electrónicos o suscribirse a boletines
- [addAlias](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addalias) 
  - "alias_label": "shopify_email" 
  - "alias_name": "example@email.com"

Cuando los usuarios se registran o inician sesión en su cuenta, es posible que desee [identificar el perfil de usuario]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#identified-user-profiles) con un ID externo. Después de que el usuario se registre e inicie sesión, añada el método [changeUser](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser) para asignar un ID externo si un usuario crea una cuenta o inicia sesión. 

{% alert note %}
Si establece un alias temporal en el perfil de usuario, puede proceder a realizar una solicitud al [punto final users/merge]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) para identificar al usuario en un momento posterior.
{% endalert %}

#### Configuración de la conciliación de usuarios de caja {#headless-checkout}

Cuando habilites el evento de caja abandonada, Braze recibirá el webhook de Shopify compras/crear. Braze intentará coincidir con un perfil de usuario existente, ya sea por dirección de correo electrónico, número de teléfono o ID de cliente de Shopify. Si no existe ninguna coincidencia, Braze creará un perfil de alias. 

Para asegurarse de que el perfil de usuario rastreado in situ se fusiona con el perfil de usuario de alias de Shopify creado por los webhooks de Shopify, puede utilizar el [endpoint`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) siguiendo los pasos que se indican a continuación. 

{% alert tip %}
Puede registrar un evento personalizado a través del SDK o una llamada a la API realizada en el archivo `theme.liquid` para activar un Canvas que incluya una solicitud al punto final `users/merge`. Estos métodos se describen a continuación.
{% endalert %}

En cuanto un cliente visita su sitio Shopify, se crea un usuario anónimo. A este usuario se le asigna automáticamente un Braze `device_id`. 

1. Asigne aleatoriamente un [alias de usuario]({{site.baseurl}}/api/objects_filters/user_alias_object#user-alias-object-specification) único para el visitante de su sitio al iniciar una nueva sesión.

2. A medida que los usuarios realizan acciones en su sitio, regístrelas como [eventos personalizados]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web) o [capture atributos de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=web). Cuando el usuario procede al pago e introduce su correo electrónico en un formulario de Shopify, se crea un ID de cliente de Shopify. Braze procesará los webhooks de Shopify y creará un nuevo perfil de usuario si el correo electrónico, el teléfono o el alias de Shopify no coinciden con un usuario existente.

{% raw %}
```javascript
{
  "user_alias": {
    "alias_name": 1234,
    "alias_label": "temp_user_id"
  }
}
```
{% endraw %}

{% subtabs %}
{% subtab API approach %}

{: start="3"}
3\. Para evitar perfiles de usuario duplicados, debe fusionar el perfil de usuario que contiene el Braze `device_id` con el perfil de usuario que contiene el perfil de alias de Shopify. Puede crear un Canvas activado por la API que establezca un retardo, actualice su usuario con el atributo `do_not_merge` y realice una solicitud al [punto final`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/). También puede registrar un evento personalizado como `merge_user` para activar su Canvas. 


{% endsubtab %}
{% subtab Non-API approach %}

{: start="3"}
3\. Cuando los usuarios salen del flujo o completan el pago, puede registrar un evento personalizado, como `merge_user`, para activar un Canvas que establecerá un retraso, actualizará su usuario con el atributo `do_not_merge` y realizará una solicitud al [endpoint`/users/merge` ]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).

{% endsubtab %}
{% endsubtabs %}

{: start="4"}
4\. En sus criterios de entrada de Canvas, diríjase sólo a perfiles de usuario no identificados, lo que significa que no tienen un ID externo y `do_not_merge` no es verdadero. <br><br>![El paso "Audiencia de entrada" en el compositor Canvas con `do_not_merge` como filtro.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_entrycriteria.png %})

{: start="5"}
5\. Después de configurar sus criterios de entrada al Lienzo, puede crear su Flujo del Lienzo. Haga que el primer paso de su Canvas sea un paso de **Retraso** para evitar posibles condiciones de carrera durante el procesamiento.<br><br>![Paso de demora en el creador de Canvas.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_delay.png %})

{: start="6"}
6\. Puede crear un paso de **Actualización de Usuario** para actualizar el atributo personalizado `do_not_merge` a "true" ya que estos usuarios serán fusionados en el siguiente paso. <br><br>![Paso de actualización del usuario en el creador de Canvas con `do_not_merge` seleccionado como atributo.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_userupdate.png %})

{: start="7"}
7\. A continuación, cree un paso de **Mensaje** con un webhook.<br><br>![Paso en mensajes en el creador de Canvas con un canal de mensajería Webhook.]({% image_buster /assets/img/Shopify/shop_usermerge_canvas_webhook.png %}) 

{% raw %}
```javascript
{
  "merge_updates": [
    {
      "identifier_to_merge": {
           "user_alias": {
                "alias_label": "temp_user_id",
                "alias_name": "{{canvas_entry_properties.${temp_user_id}}}"
            }
      },
      "identifier_to_keep": {
           "user_alias": {
                "alias_label": "shopify_customer_id",
                "alias_name": "{{canvas_entry_properties.${shopify_customer_id}}}"
            }
      }
    }
  ]
}
```
{% endraw %}

{% alert tip %}
Para obtener información sobre el comportamiento de `merge_users`, consulta [POST: Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge_updates-behavior).
{% endalert %}

{: start="8"}
8\. A medida que los usuarios salen del flujo o completan el pago, los webhooks de Shopify subsiguientes coincidirán por dirección de correo electrónico o número de teléfono o utilizando el alias de Shopify.

{% endtab %}
{% endtabs %}
