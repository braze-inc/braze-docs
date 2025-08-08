---
nav_title: Configuración de Shopify
article_title: "Configuración de Shopify"
description: "Este artículo de referencia describe cómo configurar Shopify después de integrarlo en tu SDK Braze Web."
page_type: partner
search_tag: Partner
alias: "/shopify_subscription_states/"
alias: "/setting_up_shopify_legacy/"
page_order: 2
---

# Configuración de Shopify en Braze

> Este artículo describe cómo terminar de configurar la integración de Shopify con Braze. Sigue estas instrucciones después de haber [implementado el SDK Braze Web]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) en tu sitio web de Shopify.

{% multi_lang_include alerts.md alert='Shopify obsoleto' %}

## Configuración de la integración de Shopify en Braze

### Paso 1: Conecta tu tienda Shopify

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y busca "Shopify".

{% alert note %}
Si utilizas la navegación antigua, puedes encontrar a los **socios tecnológicos** en **Integraciones**.
{% endalert %}

En la página de socios de Shopify, selecciona **Ir a Shopify App Store** para iniciar el proceso de integración.

![]({% image_buster /assets/img/Shopify/shop_setup_1.png %}){: style="max-width:70%"}

A continuación, se te dirigirá a la tienda de aplicaciones de Shopify para que instales la aplicación Braze.

{% alert note %}
Si tu cuenta de Shopify está asociada a más de una tienda, puedes cambiar a qué tienda estás conectado seleccionando el icono de la tienda en la parte superior derecha de la página y seleccionando **Cambiar de tienda**.
{% endalert %}

![]({% image_buster /assets/img/Shopify/switch_stores.png %}){: style="max-width:30%"}

Después de seleccionar la tienda que prefieras, selecciona **Instalar** en la página de la aplicación Braze. 

![]({% image_buster /assets/img/Shopify/braze_install.png %}){: style="max-width:70%"}

Después de instalar la aplicación Braze, serás redirigido a Braze para confirmar el espacio de trabajo que deseas conectar a Shopify. 

![]({% image_buster /assets/img/Shopify/confirm_workspace.png %}){: style="max-width:50%"}

Después de confirmar que estás en el espacio de trabajo correcto, puedes completar la configuración de tu integración con Shopify seleccionando **Comenzar configuración**.

![]({% image_buster /assets/img/Shopify/begin_setup.png %}){: style="max-width:70%"}

{% alert note %}
En este momento sólo puedes conectar una tienda por espacio de trabajo. Si tienes varias tiendas de Shopify que te gustaría conectar a tu espacio de trabajo, ponte en contacto con tu gestor de éxito de clientes para obtener más detalles sobre la beta de tiendas múltiples de Shopify.
{% endalert %}

### Paso 2: Eventos seleccionados y relleno histórico

Después de conectar tu tienda Shopify, procede al Paso 2 y selecciona los eventos a incluir como parte de tu integración. Debes seleccionar al menos un evento.

![]({% image_buster /assets/img/Shopify/shopify_step_2_events.png %}){: style="max-width:70%"}

Si seleccionas los eventos **Producto visto**, **Producto clicado** o **Carrito abandonado**, necesitarás el SDK de la Web de Braze para el seguimiento. Si implementas el SDK para Web de Braze a través de [Shopify ScriptTag]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=shopify%20scripttag#supported-features) o directamente en tu sitio de Shopify [`theme.liquid`]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=theme.liquid#supported-features)Braze generará automáticamente los scripts de seguimiento y los cargará en tu sitio. Si implementas el SDK para Web en tu [sitio web de Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk), deberás activar manualmente el seguimiento de estos eventos. 

#### Datos históricos de relleno (opcional)

Puedes habilitar opcionalmente un backfill de compras de los últimos 90 días anteriores a tu instalación. Al sincronizar automáticamente los datos de clientes y compras anteriores, puedes empezar inmediatamente a dirigirte a tus clientes e interactuar con ellos. Para saber más, consulta el relleno histórico de Shopify.

![]({% image_buster /assets/img/Shopify/shop_setup_4.png %}){: style="max-width:70%"}

{% alert warning %}
Para que el backfill pueda importar Eventos creados por pedido y Eventos de compra de Braze, debes haber seleccionado **Evento creado por pedido** y **Evento de compra de Braze** para incluirlos como parte de tu integración.
{% endalert %}

### Paso 3: Recoger suscriptores (opcional)

Usando la integración de Shopify, puedes recoger suscriptores de correo electrónico y SMS de tu tienda Shopify a Braze. Para más información, consulta [Sincronizar suscriptores de Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_features/shopify_user_identity/#syncing-shopify-subscribers).

![]({% image_buster /assets/img/Shopify/shopify_step_3_email.png %}){: style="max-width:70%"}

### Paso 4: Configurar la sincronización de productos de Shopify (opcional)

Opcionalmente, puedes sincronizar tus productos casi en tiempo real desde tu tienda Shopify a un catálogo Braze, automatizando el proceso para introducir datos de productos para una personalización más profunda de tus mensajes. Para saber más, consulta la [sincronización de productos de Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![]({% image_buster /assets/img/Shopify/shopify_step_4_catalog.png %}){: style="max-width:70%"}

### Paso 5: Activar la mensajería en el navegador 

Opcionalmente, puedes utilizar un canal adicional en tu tienda Shopify para los mensajes en el navegador mediante la activación de esta función. Esto te permite utilizar nuestros tipos de mensajes básicos como deslizamiento hacia arriba, modal, pantalla completa, encuestas simples y HTML personalizado.

![]({% image_buster /assets/img/Shopify/shopify_step_5_channels.png %}){: style="max-width:70%"}

Si habilitas los mensajes en el explorador, debe implementarse el SDK Braze Web para el seguimiento. Si implementas el SDK Braze Web a través de [Shopify ScriptTag]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=shopify%20scripttag#supported-features) o directamente en tu sitio de Shopify [`theme.liquid`]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=theme.liquid#supported-features), Braze generará automáticamente el script básico de implementación de mensajes en navegador en su sitio. Si implementas el Web SDK a tu [sitio Shopify headless]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/#implement-web-sdk) o planeas agregar personalizaciones a los mensajes en el explorador, debes agregar manualmente los mensajes en el explorador a tu sitio usando nuestra [guía para desarrolladores]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=web). 

### Paso 6: Configuración de acabado

Después de configurar tu configuración, selecciona **Finalizar configuración**.

![]({% image_buster /assets/img/Shopify/finish_setup.png %}){: style="max-width:70%"}

Eso es todo. El estado "Pendiente de conexión" se actualizará a "Conectado" y mostrará la fecha y hora en que se estableció la conexión. También verás si cada característica de Shopify ha sido habilitada con éxito en la página. 

![]({% image_buster /assets/img/Shopify/shopify_connected_store.png %}){: style="max-width:70%"}

### Configuración avanzada (opcional) 

#### Actualizar los retrasos por carrito abandonado y pago abandonado

Por defecto, Braze establece automáticamente el retraso para activar los eventos `shopify_abandoned_checkout` y `shopify_abandoned_cart` a una hora de inactividad. Puedes establecer el **Retraso de Carrito Abandonado** y el **Retraso de Pago Abandonado** para cada evento desde 5 minutos hasta 24 horas seleccionando el desplegable y luego seleccionando **Establecer Retraso** en la página de socio de Shopify.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_abandonment.png %}){: style="max-width:30%"}

#### Configura tu identificador de producto preferido

Si has incluido eventos de compra de Braze en la configuración de tu integración con Shopify, por defecto, Braze establecerá el ID de producto de Shopify como el `product_id` utilizado dentro del evento de compra de Braze. Se utilizará cuando filtres por productos comprados en Y días o personalices el contenido de tu mensaje utilizando Liquid.

También puedes optar por establecer el SKU o el título del producto de Shopify en lugar del ID de producto de Shopify.

![]({% image_buster /assets/img/Shopify/shop_setup_advanced_productid.png %}){: style="max-width:30%"}

## Solución de problemas

{% details ¿Por qué sigue pendiente la instalación de mi aplicación de Shopify? %}
Es posible que tu instalación siga pendiente por alguna de las siguientes razones:
 - Cuando Braze está configurando tus webhooks de Shopify
 - Cuando Braze se comunica con Shopify


Si la instalación de tu aplicación está pendiente durante 1 hora, Braze fallará la instalación y se te pedirá que reintentes la configuración.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration8.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details ¿Por qué falló la instalación de mi aplicación de Shopify? %}
Tu instalación puede haber fallado por una de las siguientes razones:
 - Braze no pudo llegar a Shopify
 - Braze no ha podido procesar la solicitud
 - Tu token de acceso a Shopify no es válido
 - La aplicación Braze Shopify ha sido eliminada de tu página de administración de Shopify.


Si esto ocurre, podrás seleccionar **Reintentar instalación** y comenzar de nuevo el proceso de instalación.<br><br>
![Shopify]({% image_buster /assets/img/Shopify/shopify_integration16.png %}){: style="max-width:70%;"}
{% enddetails %}


{% details ¿Cómo desinstalo la aplicación Braze de mi tienda Shopify? %}

Hay dos formas de desinstalar Braze de tu tienda Shopify:

1. En la página del socio de Shopify, selecciona **Desconectar**.<br><br> ![La sección "Desconectar integración" con un enlace para desconectarse.]({% image_buster /assets/img/Shopify/disconnect_integration.png %}){: style="max-width:70%;"}

2. Ve a tu página de administración de Shopify ubicada en **Apps**. A continuación, verás una opción para eliminar la aplicación Braze.<br><br> ![Un modal pidiendo confirmación de que desea eliminar la aplicación Braze.]({% image_buster /assets/img/Shopify/shopify_integration12.png %}){: style="max-width:70%;"}
{% enddetails %}

{% details Me cuesta conciliar a mis usuarios. ¿Cuál puede ser la razón? %}

El tipo de soporte que necesitarás para la conciliación de usuarios viene determinado por cómo hayas implementado el SDK Web. Para más información, consulta [Cómo empezar con Shopify]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/). 

- Si estás en un sitio headless de Shopify, comprueba la [implementación headless]({{site.baseurl}}/partners/ecommerce/shopify_legacy/getting_started_shopify/?tab=headless%20shopify%20site#supported-features) para asegurarte de que has habilitado la conciliación de usuarios en el proceso de pago.
- Si encuentras perfiles de usuario duplicados con el mismo correo electrónico o número de teléfono, puedes utilizar las siguientes herramientas de Braze para fusionar los duplicados en un solo perfil: 
    - Punto final [`users/merge`]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/)
    - [Fusión masiva]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging)
- Si utilizas la integración ScriptTag y tu tienda Shopify ofrece una opción "Comprar ahora" que omite el carro, Braze puede tener problemas para conciliar usuarios, ya que Shopify no permite que las etiquetas de script recuperen un `device_id` para asignar los eventos a un usuario que omite el carro.

{% enddetails %}
