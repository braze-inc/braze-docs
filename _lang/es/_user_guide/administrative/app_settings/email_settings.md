---
nav_title: Preferencias de correo electrónico
article_title: Preferencias de correo electrónico
page_type: reference
page_order: 14
description: "Este artículo de referencia trata sobre las preferencias de correo electrónico en el panel de control de Braze, incluidas las configuraciones de envío, los píxeles de seguimiento de apertura, la página de suscripción y los pies de página, etc."
tool: Dashboard
channel: email

---

# Preferencias de correo electrónico

> Preferencias de correo electrónico es donde puede establecer la configuración específica del correo electrónico saliente, como pies de página personalizados, páginas opt-in y opt-out personalizadas, etc. Si incluyes estas opciones en tus correos electrónicos salientes, conseguirás una experiencia fluida y cohesionada para tus usuarios.

**Las preferencias de correo electrónico** se encuentran en la sección **Configuración** del panel de control.

## Configuración de envío

Los ajustes de correo electrónico en la sección **Configuración de envío** determinan qué detalles se incluyen en sus campañas de correo electrónico. En concreto, estos ajustes están relacionados principalmente con lo que el usuario ve cuando recibe un correo electrónico de Braze.

### Configuración del correo electrónico saliente

Al configurar sus ajustes de correo electrónico, sus ajustes de correo electrónico saliente identifican qué nombre y direcciones de correo electrónico se utilizan cuando Braze envía correos electrónicos a sus usuarios.

{% tabs local %}
{% tab Dirección del nombre para mostrar %}

En esta sección, puede añadir los nombres y direcciones de correo electrónico que se utilizarán cuando Braze envíe correos electrónicos a sus usuarios. Los nombres para mostrar y las direcciones de correo electrónico estarán disponibles en las opciones de **Editar información de envío** cuando redacte su campaña de correo electrónico. Tenga en cuenta que las actualizaciones realizadas en la configuración del correo electrónico saliente no afectan retroactivamente a los envíos existentes. 

![]({% image_buster /assets/img/email_settings/display_name_address.png %})

{% endtab %}
{% tab Dirección de respuesta %}

Si añade una dirección de correo electrónico en esta sección, podrá seleccionarla como dirección de respuesta para su campaña de correo electrónico. También puede hacer que una dirección de correo electrónico sea la predeterminada seleccionando **Hacer predeterminada**. Estas direcciones de correo electrónico estarán disponibles en las opciones de **Editar información de envío** cuando redacte su campaña de correo electrónico.

![]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

{% endtab %}
{% tab Dirección CCO %}

Esta sección permite añadir y gestionar las direcciones CCO que pueden adjuntarse a los mensajes de correo electrónico salientes enviados desde Braze. Las direcciones CCO sólo están disponibles para SendGrid y SparkPost. Como alternativa a las direcciones CCO, te recomendamos que utilices [el archivo de mensajería]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) para guardar una copia de los mensajes enviados a los usuarios con fines de archivo o cumplimiento.

Si añades una dirección CCO a un mensaje de correo electrónico, se enviará una copia idéntica del mensaje que reciba tu usuario a tu buzón de entrada CCO. Se trata de una herramienta útil para conservar copias de los mensajes que enviaste a tus usuarios por requisitos de cumplimiento o problemas de atención al cliente. Los correos electrónicos CCO no se incluyen en los informes y análisis de correo electrónico.

{% alert important %}
Si añades una dirección CCO a tu campaña o Canvas, se duplicarán tus correos electrónicos facturables para la campaña o el componente Canvas, ya que Braze enviará un mensaje a tu usuario y otro a tu dirección CCO.
{% endalert %}

![Sección Dirección CCO de la pestaña Configuración de correo electrónico.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Después de añadir una dirección, ésta estará disponible para seleccionarla cuando redactes un correo electrónico en campañas o pasos en Canvas. Seleccione **Establecer como predeterminada** junto a una dirección para establecer que esta dirección se seleccione por defecto al iniciar una nueva campaña de correo electrónico o componente Canvas. Para anular esta opción a nivel de mensaje, puede seleccionar **Sin CCO** al configurar el mensaje.

Si necesitas que todos los mensajes de correo electrónico enviados desde Braze incluyan una dirección CCO, puedes alternar la opción **Requerir una dirección CCO para todas tus campañas de correo electrónico**. Esto requerirá que selecciones una dirección predeterminada, que se seleccionará automáticamente en las nuevas campañas de correo electrónico o pasos en Canvas. La dirección predeterminada también se añadirá automáticamente a todos los mensajes activados a través de nuestra API REST. No es necesario modificar la solicitud API existente para incluir la dirección.

{% endtab %}
{% endtabs %}

## Abrir píxel de seguimiento

[![Curso Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

El píxel de seguimiento de apertura de correo electrónico es una imagen invisible de 1 x 1 px que se inserta automáticamente en el HTML de su correo electrónico. Este píxel ayuda a Braze a detectar si los usuarios finales han abierto su correo electrónico. La información sobre la apertura del correo electrónico puede ser muy útil, ya que ayuda a los usuarios a determinar estrategias de marketing eficaces al conocer las tasas de apertura correspondientes.

### Colocación del píxel de seguimiento

El comportamiento predeterminado de Braze es añadir el píxel de seguimiento en la parte inferior del correo electrónico. Para la mayoría de los usuarios, éste es el lugar ideal para colocar el píxel. Aunque el píxel ya está diseñado para provocar los menores cambios visuales posibles, cualquier cambio visual involuntario sería lo menos visible en la parte inferior de un correo electrónico. Este es también el valor predeterminado para los proveedores de correo electrónico como SendGrid y SparkPost.

### Cambiar la ubicación del píxel de seguimiento

Actualmente, Braze permite anular la ubicación predeterminada del píxel de seguimiento de apertura del ESP (la última etiqueta de `<body>` de un correo electrónico) para moverlo a la primera etiqueta de `<body>`.
  
!["Abrir la sección Píxel de seguimiento" con las opciones para mover para SendGrid, SparkPost o Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Para cambiar la ubicación:

1. En Braze, ve a **Configuración** > **Preferencias de correo electrónico**.
2. Seleccione una de las siguientes opciones: **Muévete por SendGrid**, **Muévete por SparkPost** o **Muévete por Amazon SES**
3. Seleccione **Guardar**.

Una vez guardado, Braze enviará instrucciones especiales al ESP para colocar el píxel de seguimiento de apertura en la parte superior de todos los correos electrónicos HTML.
  
{% alert important %}
La habilitación SSL envolverá la URL del píxel de seguimiento con HTTPS en lugar de HTTP. Si tu SSL está mal configurado, puede afectar a la eficacia del píxel de seguimiento.
{% endalert %}

## Encabezado de cancelar suscripción a la lista {#list-unsubscribe}

{% alert note %}
A partir del 15 de febrero de 2024, las nuevas empresas tendrán habilitado por defecto el encabezado de cancelar suscripción (cancelar suscripción con un clic).
{% endalert %}

El uso de un encabezado de cancelación de suscripción permite a los destinatarios darse de baja fácilmente de los correos electrónicos de marketing mostrando un botón de **cancelación de suscripción** en la interfaz de usuario del buzón, y no en el cuerpo del mensaje.

![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Cuando un destinatario hace clic en **Cancelar suscripción**, el proveedor de buzones envía la solicitud de cancelación de suscripción al destino definido en el encabezado del correo electrónico.

Habilitar la cancelación de la suscripción a listas es una práctica recomendada de entregabilidad y un requisito de algunos de los principales proveedores de buzones de correo. Anima a los usuarios finales a retirarse de forma segura de los mensajes no deseados en lugar de pulsar el botón de spam en un cliente de correo electrónico, lo cual es perjudicial para la reputación de envío y la entregabilidad del correo electrónico.

### Soporte al proveedor de buzones

La siguiente tabla resume la compatibilidad del proveedor de buzones con el encabezado "mailto:", la URL de cancelar suscripción a la lista y cancelar suscripción con un solo clic ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| Encabezado de cancelar suscripción a la lista | Mailto: encabezado | URL de cancelación de suscripción | Cancelar suscripción con un clic (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | Compatible* | Compatible | Compatible |
| Gmail móvil | No se admite | No se admite | No se admite |
| Apple Mail | Compatible | No se admite | No se admite |
| Outlook.com | Compatible | No se admite | No se admite |
| ¡Yahoo! Correo | Compatible* | No se admite | Compatible |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*Con el tiempo, Yahoo y Gmail dejarán de utilizar el encabezado "mailto:" y sólo admitirán un clic._

La visualización de la cabecera la determina en última instancia el proveedor del buzón. Para comprobar si el encabezado de cancelación de suscripción está incluido en el correo electrónico sin formato (texto) del destinatario en Gmail, haz lo siguiente:

1. Seleccione **Mostrar original** en el correo electrónico. Esto abre una nueva pestaña con la versión sin procesar del correo electrónico y sus cabeceras.
2. Buscar "Cancelar suscripción a la lista".

Si la cabecera está en la versión sin procesar del correo electrónico pero no se muestra, el proveedor de buzón de correo ha decidido no mostrar la opción de cancelar suscripción, lo que significa que no tenemos más información sobre por qué el proveedor de buzón de correo no muestra la cabecera. Ver el encabezado de cancelar suscripción a la lista se basa, en última instancia, en la reputación. En la mayoría de los casos, cuanto mejor sea la reputación del remitente en la bandeja de entrada, menos probable será que aparezca el encabezado de cancelación de suscripción.

### Cabecera de cancelación de suscripción de correo electrónico en los espacios de trabajo

![Selección de los "usuarios suscritos o con adhesión voluntaria" a los que enviar.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Cuando está activada la característica de cancelar suscripción a la cabecera del correo electrónico, esta configuración se aplica a todo el espacio de trabajo, no a nivel de empresa. Se añade a las campañas y los Canvases que se configuran para enviar a usuarios suscritos o con adhesión voluntaria, o a usuarios con adhesión voluntaria en el paso **Audiencia objetivo** de los creadores de campañas y Canvas.

Cuando se utiliza el "espacio de trabajo predeterminado", Braze no añade el encabezado de cancelar suscripción con un clic para las campañas que se consideran transaccionales, que están configuradas para "enviar a todos los usuarios, incluidos los usuarios dados de baja". Para anular esto y añadir el encabezado de cancelar suscripción con un clic al enviar a usuarios dados de baja, puedes seleccionar **Cancelar suscripción globalmente de todos los mensajes de correo electrónico** en la configuración de cancelación de suscripción con un clic de la lista a nivel de mensaje.

### Cabecera predeterminada de cancelación de suscripción

{% alert important %}
Gmail pretende que los remitentes implementen la cancelación de suscripción con un solo clic para todos sus mensajes comerciales y promocionales salientes a partir del 1 de junio de 2024. Para obtener más información, consulta [las directrices para remitentes de Gmail](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) y [las Preguntas frecuentes sobre directrices para remitentes de correo electrónico de Gmail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo anunció un plazo de principios de 2024 para los requisitos de actualización. Para más información, consulta [Más seguridad, menos correo no deseado: Aplicación de las normas de correo electrónico para mejorar la experiencia](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Para utilizar la característica de cancelación de suscripción de Braze para procesar directamente las cancelaciones de suscripción, selecciona **Incluir un encabezado de correo electrónico de cancelación de suscripción de lista (mailto y HTTP) con un solo clic para los correos electrónicos enviados a usuarios suscritos o con adhesión voluntaria** y selecciona **Braze predeterminado** como URL y mail-to estándar de Braze. 

![Opción para incluir automáticamente una cabecera de cancelar suscripción en los correos electrónicos enviados a usuarios suscritos o que han optado por recibirlos.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze admite las siguientes versiones de la cabecera list-unsubscribe:

| Versión para cancelar suscripción a la lista | Descripción | 
| ----- | --- |
| Un clic (RFC 8058) | Ofrece a los destinatarios una forma sencilla de darse de baja de los correos electrónicos con un solo clic. Este es un requisito de Yahoo y Gmail para los remitentes masivos. |
| URL o HTTPS para cancelar suscripción a la lista | Proporciona a los destinatarios un enlace que les dirige a una página web donde pueden darse de baja. |
| Mailto | Especifica una dirección de correo electrónico como destino del mensaje de solicitud de cancelar suscripción que el destinatario enviará a la marca. <br><br> _Para procesar las solicitudes de cancelación de suscripción a listas de correo, dichas solicitudes deben incluir la dirección de correo electrónico almacenada en Braze del Usuario final que desea cancelar la suscripción. Puede proporcionarlo la "dirección de origen" del correo electrónico desde el que el usuario final se está dando de baja, el asunto codificado o el cuerpo codificado del correo electrónico recibido por el usuario final del que se está dando de baja. En casos muy limitados, algunos proveedores de buzón de entrada no se adhieren al protocolo [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), lo que provoca que la dirección de correo electrónico no se transmita correctamente. Esto puede provocar que una solicitud de cancelar suscripción no pueda procesarse en Braze._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Cuando Braze recibe una solicitud de cancelación de suscripción de un usuario a través de cualquiera de los métodos anteriores, el estado global de suscripción de correo electrónico de este usuario se establece como cancelado. Si no hay ninguna coincidencia, Braze no procesará esta solicitud.

### Cancelar suscripción con un clic

El uso de cancelar suscripción con un clic para la cabecera de baja de lista[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) se centra en proporcionar una forma sencilla de que los destinatarios puedan darse de baja de los correos electrónicos.

### Cancelación de la suscripción con un solo clic a nivel de mensaje

La configuración de cancelación de suscripción con un solo clic a nivel de mensaje anulará la función de cancelación de suscripción del encabezado de correo electrónico para los espacios de trabajo. Aplique el comportamiento de cancelación de suscripción con un solo clic por campaña o paso de Canvas para los siguientes usos:

- Añadir un Braze one-click unsubscribe para un grupo de suscripción específico para apoyar múltiples marcas/listas dentro de un espacio de trabajo.
- Alternar entre la URL de cancelación de suscripción predeterminada de Braze o la personalizada
- Añade tu URL personalizada de cancelación de suscripción con un solo clic
- Omitir la cancelación de suscripción con un clic en este mensaje

{% alert note %}
La configuración de cancelar suscripción con un clic a nivel de mensaje sólo está disponible cuando se utiliza el editor de arrastrar y soltar y el editor HTML actualizado. Si utiliza el editor HTML anterior, cambie al editor HTML actualizado para utilizar esta función.
{% endalert %}

En su editor de correo electrónico, vaya a **Configuración de envío** > **Información de envío**. Seleccione una de las siguientes opciones:

- **Utilizar el espacio de trabajo por defecto**: Utiliza la configuración **del encabezado de cancelación de suscripción de correo electrónico** establecida en **Preferencias de correo electrónico**. Los cambios realizados en esta configuración se aplicarán a todos los mensajes.
- **Darse de baja a nivel global de todos los correos electrónicos**: Utiliza el encabezado predeterminado para cancelar suscripción en un clic. Los usuarios que hagan clic en el botón de cancelar suscripción tendrán su estado global de suscripción de correo electrónico establecido en "Cancelar suscripción".
- **Darse de baja de un grupo de suscripción específico**: Utiliza el grupo de suscripción especificado. Los usuarios que hagan clic en el botón de baja se darán de baja del grupo de suscripción seleccionado.
    - Al seleccionar un grupo de suscripción, añada el filtro **Grupo de suscripción** en **Público objetivo** para dirigirse únicamente a los usuarios suscritos a este grupo específico. El grupo de suscripción seleccionado para cancelar la suscripción con un clic debe coincidir con el grupo de suscripción al que se dirige. Si hay una falta de coincidencia en el grupo de suscripción, puedes arriesgarte a enviar a un usuario que está intentando cancelar suscripción de un grupo de suscripción del que ya se ha dado de baja.
- **Personalizado:** Añade tu URL para cancelar suscripciones en un solo clic de modo que tú puedas cancelarlas directamente.
- **Excluir cancelación de suscripción**

{% alert important %}
La exclusión de la cancelación de la suscripción con un solo clic o de cualquier mecanismo de cancelación de la suscripción sólo debe hacerse para la mensajería transaccional, como el restablecimiento de contraseñas, los recibos y los correos electrónicos de confirmación.
{% endalert %}

Al ajustar esta opción, se anulará el comportamiento predeterminado para la cancelación de la suscripción a la lista con un solo clic en este correo electrónico.

![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Requisitos

Si envía mensajes de correo electrónico utilizando su propia funcionalidad de cancelación de suscripción personalizada, debe cumplir los siguientes requisitos para asegurarse de que la URL de cancelación de suscripción con un solo clic que ha configurado cumple la RFC 8058:

* La URL debe poder gestionar las solicitudes POST de cancelar suscripción.
* La URL debe empezar por `https://`.
* La URL no debe devolver una redirección HTTPS ni un cuerpo. Los enlaces para darse de baja con un solo clic que dirigen a una página de aterrizaje u otro tipo de página web no cumplen la norma RFC 8058.
* Las solicitudes POST no deben establecer cookies.

Seleccione **Encabezado de cancelación de suscripción de lista personalizado** para añadir su propio punto final de cancelación de suscripción con un solo clic configurado y un "mailto:" opcional. Braze requiere una entrada para que la URL admita un encabezado de cancelación de suscripción personalizado porque la cancelación de suscripción HTTP con un solo clic es un requisito de Yahoo y Gmail para los remitentes masivos.

![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Añada líneas de asunto de correo electrónico

Alterna para incluir "[TEST]" y "[SEED]" en las líneas del asunto de tus correos electrónicos de prueba e inicializados. Esto puede ayudar a identificar cualquier campaña de correo electrónico enviada como prueba.

![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## CSS en línea en los nuevos correos electrónicos por defecto

El CSS en línea es una técnica que encierra automáticamente estilos CSS para tus correos electrónicos y nuevos correos. En algunos clientes de correo electrónico, esto puede mejorar la presentación de tu correo electrónico.

La modificación de esta configuración no afectará a tus mensajes o plantillas de correo electrónico existentes. Puedes sustituir este valor predeterminado en cualquier momento mientras creas mensajes o plantillas. Para más información, consulta [CSS inlining]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/).

## Volver a suscribir a los usuarios cuando cambie su dirección de correo electrónico

Puede volver a suscribir automáticamente a los usuarios cuando cambien de dirección de correo electrónico. Por ejemplo, si un usuario del espacio de trabajo que se ha dado de baja cambia su dirección de correo electrónico por otra que no esté en la lista de cancelación de suscripción de Braze, se volverá a suscribir automáticamente.

![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Páginas de suscripción y pies de página

{% tabs local %}
{% tab Pie de página personalizado %}

En el caso de los correos electrónicos comerciales, la [Ley CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que todos los correos comerciales incluyan una opción para darse de baja. Con la configuración personalizada del pie de página, podrá seguir cumpliendo con la normativa CAN-SPAM a la vez que personaliza su pie de página de exclusión de correo electrónico. Para seguir cumpliendo la normativa, debe añadir su pie de página personalizado a todos los correos electrónicos enviados como parte de las campañas de este espacio de trabajo.

Tenga en cuenta los siguientes requisitos al crear un pie de página personalizado para sus mensajes de correo electrónico:
- Debe incluir una URL para darse de baja y una dirección postal física.
- Debe ser inferior a 100 KB.

![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Para obtener más información sobre las plantillas personalizadas para el pie de página Liquid, consulte nuestra documentación sobre [Pies de página personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Página personalizada para cancelar suscripción %}

Braze le permite configurar una **página de cancelación de suscripción personalizada** con su propio HTML. Esta página aparecerá después de que un usuario haya seleccionado darse de baja en la parte inferior de un correo electrónico. Ten en cuenta que esta página debe ocupar menos de 750 KB. 

![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Obtenga más información sobre las mejores prácticas para la gestión de listas de correo electrónico en [Gestión de suscripciones de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Página de suscripción personalizada %}

Puedes crear una página de adhesión voluntaria personalizada utilizando tu propio HTML. Incluir esto en su correo electrónico puede ser especialmente beneficioso si desea que su marca y su mensaje permanezcan coherentes durante todo el ciclo de vida del usuario. Ten en cuenta que esta página debe ocupar menos de 750 KB. 

![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Obtenga más información sobre las mejores prácticas para la gestión de listas de correo electrónico en [Gestión de suscripciones de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

## Preguntas más frecuentes

### Cancelar suscripción con un clic

{% details ¿Puede la URL de cancelación de suscripción con un solo clic (a través del encabezado de cancelación de suscripción de la lista) enlazar con un centro de preferencias? %}
No, eso no se ajusta a la RFC 8058, lo que significa que no cumplirás el requisito de cancelar suscripción con un clic de Yahoo y Gmail.
{% enddetails %}

{% details ¿Por qué recibo el mensaje de error "El cuerpo de tu correo electrónico no incluye un enlace para cancelar suscripción" al redactar mi centro de preferencias? %}
Un centro de preferencias no se considera un enlace para cancelar suscripción. Los destinatarios de sus correos electrónicos deben tener la opción de darse de baja de cualquier correo electrónico comercial para seguir cumpliendo la normativa CAN-SPAM.
{% enddetails %}

{% details ¿Tendré que editar las campañas de correo electrónico y los lienzos anteriores para aplicar la configuración de cancelación de suscripción con un solo clic después de activarla? %}
Si no tienes ninguno de los casos de uso para la configuración de cancelación de suscripción con un solo clic a nivel de mensaje, no es necesario realizar ninguna acción siempre que la configuración esté activada en **Preferencias de correo electrónico**. Braze añadirá automáticamente los encabezados de cancelación de suscripción con un solo clic a todos los mensajes promocionales y de marketing salientes. Sin embargo, si necesitas configurar el comportamiento de cancelar suscripción con un clic a nivel de mensaje, tendrás que actualizar las campañas anteriores y los pasos en Canvas con el correo electrónico en consecuencia.
{% enddetails %}

{% details Puedo ver el encabezado de cancelación de suscripción con un clic y de cancelación de suscripción con una lista en el mensaje original o en los datos sin procesar, pero ¿por qué no veo el botón Cancelar suscripción en Gmail o Yahoo? %}
Gmail y Yahoo deciden en última instancia si mostrar o no el encabezado de cancelación de suscripción con lista o con un solo clic. En el caso de remitentes nuevos o con poca reputación del remitente, esto puede hacer que ocasionalmente no se muestre el botón de cancelar suscripción.
{% enddetails %}

{% details ¿Es compatible con Liquid el encabezado personalizado para darse de baja con un solo clic? %}
Sí, Liquid y la lógica condicional son compatibles para permitir URL dinámicas de cancelación de suscripción con un solo clic para el encabezado.
{% enddetails %}

{% alert tip %}
Si añades lógica condicional, evita tener valores de salida que añadan espacios en blanco a tu URL, ya que Braze no los elimina.
{% endalert %}

### Cancelación de la suscripción con un solo clic a nivel de mensaje

{% details Si añado manualmente las cabeceras de correo electrónico para un clic, y tengo activada la cabecera de cancelar suscripción por correo electrónico, ¿cuál es el comportamiento esperado? %}
Las cabeceras de correo electrónico añadidas para la lista de cancelación de suscripción con un solo clic se aplicarán a todos los envíos futuros de esta campaña.
{% enddetails %}

{% details ¿Por qué los grupos de suscripción tienen que coincidir en todas las variantes de mensajes para poder lanzarse? %}
Para una campaña con pruebas A/B, Braze enviará aleatoriamente a un usuario una de las variantes. Si tienes dos grupos de suscripción diferentes configurados en la misma campaña (la variante A está configurada en el grupo de suscripción A, y la variante B está configurada en el grupo de suscripción B), no podemos garantizar que los usuarios que sólo estén suscritos al grupo de suscripción B reciban la variante B. Puede darse el caso de que los usuarios estén cancelando suscripción de un grupo de suscripción del que ya se han dado de baja.
{% enddetails %}

{% details La configuración del encabezado de cancelación de suscripción de correo electrónico está desactivada en Preferencias de correo electrónico, pero en la información de envío de mi campaña, la configuración de cancelación de suscripción de lista con un solo clic está establecida en "Utilizar espacio de trabajo predeterminado". ¿Es un error? %}
No. Si la configuración del espacio de trabajo está desactivada y la configuración del mensaje está establecida en **Utilizar espacio de trabajo predeterminado**, Braze seguirá lo que esté configurado en **Preferencias de correo electrónico**. Esto significa que no añadiremos el encabezado de cancelar suscripción con un clic para la campaña.
{% enddetails %}

{% details ¿Qué ocurre si se archiva un grupo de suscripción? ¿Interrumpirá esto la cancelación de la suscripción con un solo clic en los correos electrónicos enviados? %}
Si se archiva un grupo de suscripción al que se hace referencia en **Información de envío** para un clic, Braze seguirá procesando las cancelaciones de suscripción de un clic. El grupo de suscripción ya no se mostrará en el panel de control (filtro de segmentos, perfil de usuario y áreas similares).
{% enddetails %}

{% details ¿Está disponible la configuración de cancelar suscripción con un clic para las plantillas de correo electrónico? %}
No, actualmente no tenemos planes de añadir esto para las plantillas de correo electrónico, ya que estas plantillas no están asignadas a un dominio de envío. Si te interesa esta función para las plantillas de correo electrónico, envíanos [tus comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details ¿Comprueba esta función que la URL de cancelación de suscripción con un solo clic añadida a la opción personalizada es válida? %}
No, no comprobamos ni validamos ningún enlace en el panel de control de Braze. Asegúrese de probar correctamente su URL antes del lanzamiento.
{% enddetails %}


