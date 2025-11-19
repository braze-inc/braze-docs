---
nav_title: Preferencias de correo electrónico
article_title: Preferencias de correo electrónico
page_type: reference
page_order: 14
description: "Este artículo de referencia cubre las preferencias de correo electrónico en el panel de Braze, incluidas las configuraciones de envío, los píxeles de seguimiento de apertura, la página de suscripción y los pies de página, y mucho más."
tool: Dashboard
channel: email

---

# Preferencias de correo electrónico

> Preferencias de correo electrónico es donde puedes establecer configuraciones específicas de correo electrónico saliente, como pies de página personalizados, páginas de adhesión voluntaria y de exclusión voluntaria personalizadas, etc. Si incluyes estas opciones en tus correos electrónicos salientes, conseguirás una experiencia fluida y cohesionada para tus usuarios.

**Las Preferencias de correo electrónico** se encuentran en **Configuración**, en el panel de control.

## Configuración de envío

La configuración del correo electrónico en la sección **Configuración de envío** determina qué detalles se incluyen en tus campañas de correo electrónico. En concreto, estas configuraciones están relacionadas principalmente con lo que tu usuario ve cuando recibe un correo electrónico de Braze.

### Configuración del correo electrónico saliente

Al configurar tus ajustes de correo electrónico, tus ajustes de correo electrónico saliente identifican qué nombre y direcciones de correo electrónico se utilizan cuando Braze envía correos electrónicos a tus usuarios.

{% tabs local %}
{% tab Display Name Address %}

En esta sección, puedes añadir los nombres y direcciones de correo electrónico que se pueden utilizar cuando Braze envíe correos electrónicos a tus usuarios. Los nombres para mostrar y las direcciones de correo electrónico estarán disponibles en las opciones de **Editar información de envío** cuando compongas tu campaña de correo electrónico. Ten en cuenta que las actualizaciones realizadas en la configuración del correo electrónico saliente no afectan retroactivamente a los envíos existentes.

\!["Configuración del correo electrónico saliente" sección con campos para diferentes nombres de visualización y dominios.]({% image_buster /assets/img/email_settings/display_name_address.png %})

#### Personalización con Liquid

También puedes utilizar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) en los campos **De nombre para mostrar** y **Parte local** para crear plantillas dinámicas para el envío por correo electrónico basadas en atributos personalizados. Por ejemplo, puedes utilizar la lógica condicional para enviar desde diferentes marcas o regiones:

{% raw %}
```liquid
{% if ${language} == 'en' %} 
English Display Name 
{% elsif ${language} == 'de' %} 
German Display Name 
{% else %} 
Default to English Display Name
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab Reply-To Address %}

Si añades una dirección de correo electrónico en esta sección, podrás seleccionarla como dirección de respuesta a tu campaña de correo electrónico. También puedes hacer que una dirección de correo electrónico sea la predeterminada seleccionando **Hacer predeterminada**. Estas direcciones de correo electrónico estarán disponibles en las opciones de **Editar información de envío** cuando redactes tu campaña de correo electrónico.

\!["Dirección de respuesta" sección con campos para introducir varias direcciones de respuesta a.]({% image_buster /assets/img/email_settings/reply_to_address.png %}){: style="max-width:75%;" }

#### Personalización con Liquid

También puedes utilizar [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) en el campo **Dirección de respuesta** para crear una plantilla dinámica de la dirección de respuesta basada en atributos personalizados. Por ejemplo, puedes utilizar la lógica condicional para enviar respuestas a distintas regiones o departamentos:

{% raw %}
```liquid
{% if {{custom_attribute.${region}}} == 'US' %}
us-support@company.com
{% elsif {{custom_attribute.${region}}} == 'EU' %}
eu-support@company.com
{% else %}
global-support@company.com
{% endif %}
```
{% endraw %}

{% endtab %}
{% tab BCC Address %}

Esta sección te permite añadir y gestionar las direcciones CCO que se pueden añadir a los mensajes de correo electrónico salientes enviados desde Braze. Las direcciones CCO sólo están disponibles para SendGrid y SparkPost. Como alternativa a las direcciones CCO, te recomendamos que utilices [el archivo de mensajería]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/) para guardar una copia de los mensajes enviados a los usuarios con fines de archivo o cumplimiento.

Si añades una dirección CCO a un mensaje de correo electrónico, se enviará una copia idéntica del mensaje que reciba tu usuario a tu buzón de entrada CCO. Se trata de una herramienta útil para conservar copias de los mensajes que enviaste a tus usuarios por requisitos de cumplimiento o problemas de atención al cliente. Los correos electrónicos con CCO no se incluyen en los informes y análisis de correo electrónico.

{% alert important %}
Si añades una dirección CCO a tu campaña o Canvas, se duplicarán tus correos electrónicos facturables para la campaña o el componente Canvas, ya que Braze enviará un mensaje a tu usuario y otro a tu dirección CCO.
{% endalert %}

\![Sección Dirección CCO de la pestaña Configuración de correo electrónico.]({% image_buster /assets/img/email_settings/bcc_address.png %}){: style="max-width:75%;" }

Después de añadir una dirección, ésta estará disponible para seleccionarla cuando redactes un correo electrónico en campañas o pasos en Canvas. Selecciona **Establecer como predeterminada** junto a una dirección para establecer que esta dirección se seleccione por defecto al lanzar una nueva campaña de correo electrónico o un componente de Canvas. Para anular esto a nivel de mensaje, puedes seleccionar **Sin CCO** al configurar tu mensaje.

Si necesitas que todos los mensajes de correo electrónico enviados desde Braze incluyan una **dirección C** CO, puedes alternar la opción **Requerir una dirección CCO para todas tus campañas de correo electrónico**. Esto requerirá que selecciones una dirección predeterminada, que se seleccionará automáticamente en las nuevas campañas de correo electrónico o pasos en Canvas. La dirección predeterminada también se añadirá automáticamente a todos los mensajes desencadenados a través de nuestra API REST. No es necesario modificar la solicitud API existente para incluir la dirección.

{% endtab %}
{% endtabs %}

## Píxel de seguimiento abierto

[![Curso de Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/email-open-tracking-pixel/){: style="float:right;width:120px;border:0;" class="noimgborder"}

El píxel de seguimiento de apertura de correo electrónico es una imagen invisible de 1 x 1 px que se inserta automáticamente en el HTML de tu correo electrónico. Este píxel ayuda a Braze a detectar si los usuarios finales han abierto tu correo electrónico. La información sobre la apertura del correo electrónico puede ser muy útil, ya que ayuda a los usuarios a determinar estrategias de marketing eficaces conociendo las tasas de apertura correspondientes.

### Colocar el píxel de seguimiento

El comportamiento predeterminado en Braze es añadir el píxel de seguimiento al final de tu correo electrónico. Para la mayoría de los usuarios, éste es el lugar ideal para colocar el píxel. Aunque el píxel ya está diseñado para provocar los menores cambios visuales posibles, cualquier cambio visual involuntario sería lo menos visible en la parte inferior de un correo electrónico. Esto también está predeterminado para proveedores de correo electrónico como SendGrid y SparkPost.

### Cambio de ubicación del píxel de seguimiento

Braze admite actualmente anular la ubicación predeterminada del píxel de seguimiento de apertura del ESP (la última etiqueta en `<body>` de un correo electrónico) para moverlo a la primera etiqueta en `<body>`.
  
Abre la sección "Píxel de seguimiento" con las opciones para moverte por SendGrid, SparkPost o Amazon SES.]({% image_buster /assets/img/open_pixel.png %}){: style="max-width:80%;" }

Para cambiar la ubicación:

1. En Braze, ve a **Configuración** > **Preferencias de correo electrónico**.
2. Selecciona una de las siguientes opciones: **Muévete por SendGrid**, **Muévete por SparkPost** o **Muévete por Amazon SES**
3. Selecciona **Guardar**.

Una vez guardado, Braze enviará instrucciones especiales al ESP para colocar el píxel de seguimiento de apertura en la parte superior de todos los correos electrónicos HTML.
  
{% alert important %}
La habilitación SSL envolverá la URL del píxel de seguimiento con HTTPS en lugar de HTTP. Si tu SSL está mal configurado, puede afectar a la eficacia del píxel de seguimiento.
{% endalert %}

## Cabecera de cancelar suscripción a la lista {#list-unsubscribe}

{% alert note %}
A partir del 15 de febrero de 2024, las nuevas empresas tendrán habilitada por defecto la cabecera de cancelar suscripción (con un clic para darse de baja).
{% endalert %}

Utilizar una cabecera de cancelación de suscripción de lista permite a tus destinatarios darse de baja fácilmente de los correos electrónicos de marketing mostrando un botón de **Cancelar suscripción** dentro de la interfaz de usuario del buzón, y no en el cuerpo del mensaje.

\![]({% image_buster /assets/img_archive/list_unsub_img1.png %}){: style="float:right;max-width:60%;margin-left:15px;"}

Cuando un destinatario hace clic en **Cancelar suscripción**, el proveedor de buzones envía la solicitud de cancelación de suscripción al destino definido en el encabezado del correo electrónico.

Habilitar la opción de cancelar suscripción es una buena práctica de capacidad de entrega y un requisito de algunos de los principales proveedores de buzones de correo. Anima a los usuarios finales a eliminar de forma segura los mensajes no deseados frente a pulsar el botón de correo no deseado en un cliente de correo electrónico, lo cual es perjudicial para la reputación del remitente y la capacidad de entrega del correo electrónico.

### Asistencia al proveedor de buzones

La siguiente tabla resume la compatibilidad del proveedor de buzones con el encabezado "mailto:", la URL de cancelación de suscripción y la cancelación de suscripción con un clic[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)).

| Cabecera de cancelar suscripción a la lista | Encabezado Mailto: | URL para cancelar suscripción a la lista | Cancelar suscripción con un clic (RFC 8058) | 
| ----- | --- | --- | --- |
| Gmail | Apoyado* | Apoyado | Apoyado |
| Gmail Móvil | No se admite | No se admite | No se admite |
| Correo de Apple | Apoyado | No se admite | No se admite |
| Outlook.com | Apoyado | No se admite | No se admite |
| ¡Yahoo! Correo | Apoyado* | No se admite | Apoyado |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

_\*Yahoo y Gmail acabarán eliminando la cabecera "mailto:" y sólo admitirán un clic._

La visualización de la cabecera la determina en última instancia el proveedor del buzón. Para comprobar si la cabecera cancelar suscripción está incluida en el correo electrónico sin formato (texto) del destinatario en Gmail, haz lo siguiente:

1. Selecciona **Mostrar original** en el correo electrónico. Esto abre una nueva pestaña con la versión sin procesar del correo electrónico y sus cabeceras.
2. Busca "Cancelar suscripción".

Si la cabecera está en la versión sin procesar del correo electrónico pero no se muestra, el proveedor de buzón de correo ha decidido no mostrar la opción de cancelar suscripción, lo que significa que no tenemos más información sobre por qué el proveedor de buzón de correo no muestra la cabecera. Ver el encabezado cancelar suscripción se basa en última instancia en la reputación. En la mayoría de los casos, cuanto mejor sea tu reputación del remitente con el proveedor de buzones, más probable será que aparezca el encabezado de cancelar suscripción.

### Cabecera de cancelar suscripción por correo electrónico en los espacios de trabajo

\![Seleccionar los "usuarios suscritos o con adhesión voluntaria" para saber a qué usuarios enviar.]({% image_buster /assets/img/email_settings/email_unsub_header_workspaces.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Cuando está activada la característica de cancelar suscripción a la cabecera del correo electrónico, esta configuración se aplica a todo el espacio de trabajo, no a nivel de empresa. Se añade a las campañas y los Canvases configurados para enviar a usuarios suscritos o con adhesión voluntaria, o a usuarios con adhesión voluntaria en el paso **Audiencia objetivo** de los creadores de campañas y Canvas.

Cuando se utiliza el "espacio de trabajo predeterminado", Braze no añade el encabezado de cancelar suscripción con un clic para las campañas que se consideran transaccionales, que están configuradas para "enviar a todos los usuarios, incluidos los usuarios dados de baja". Para anular esto y añadir el encabezado de cancelar suscripción con un clic al enviar a usuarios dados de baja, puedes seleccionar **Cancelar suscripción globalmente de todos los mensajes de correo electrónico** en la configuración de cancelación de suscripción con un clic de la lista a nivel de mensaje.

### Encabezado predeterminado de cancelar suscripción a la lista

{% alert important %}
Gmail pretende que los remitentes implementen la cancelación suscripción con un clic para todos sus mensajes comerciales y promocionales salientes a partir del 1 de junio de 2024. Para obtener más información, consulta [las directrices para remitentes](https://support.google.com/mail/answer/81126?hl=en#subscriptions&zippy=%2Crequirements-for-sending-or-more-messages-per-day:~:text=Make%20it%20easy%20to%20unsubscribe) [de Gmail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages) y [las Preguntas frecuentes sobre directrices para remitentes de correo electrónico de Gmail](https://support.google.com/a/answer/14229414#zippy=%2Cwhat-time-range-or-duration-is-used-when-calculating-spam-rate%2Cif-the-list-header-is-missing-is-the-message-body-checked-for-a-one-click-unsubscribe-link%2Cif-unsubscribe-links-are-temporarily-unavailable-due-to-maintenance-or-other-reasons-are-messages-flagged-as-spam%2Ccan-a-one-click-unsubscribe-link-to-a-landing-or-preferences-page%2Cwhat-is-a-bulk-sender%2Chow-can-bulk-senders-make-sure-theyre-meeting-the-sender-guidelines%2Cdo-the-sender-guidelines-apply-to-messages-sent-to-google-workspace-accounts%2Cdo-the-sender-guidelines-apply-to-messages-sent-from-google-workspace-accounts%2Cwhat-happens-if-senders-dont-meet-the-requirements-in-the-sender-guidelines%2Cif-messages-are-rejected-because-they-dont-meet-the-sender-guidelines-do-you-send-an-error-message-or-other-alert%2Cwhat-happens-when-sender-spam-rate-exceeds-the-maximum-spam-rate-allowed-by-the-guidelines%2Cwhat-is-the-dmarc-alignment-requirement-for-bulk-senders%2Cif-messages-fail-dmarc-authentication-can-they-be-delivered-using-ip-allow-lists-or-spam-bypass-lists-or-will-these-messages-be-quarantined%2Ccan-bulk-senders-get-technical-support-for-email-delivery-issues%2Cdo-all-messages-require-one-click-unsubscribe:~:text=for%20mitigations.-,Unsubscribe%20links,-Do%20all%20messages). Yahoo anunció un plazo de principios de 2024 para los requisitos de actualización. Para más información, consulta [Más seguridad, menos correo no deseado: Aplicación de las normas de correo electrónico para una mejor experiencia](https://blog.postmaster.yahooinc.com/).
{% endalert %}

Para utilizar la característica de cancelar suscripción de Braze para procesar directamente las bajas, selecciona **Incluir un encabezado de correo electrónico de lista de baja (mailto y HTTP) con un solo clic para los correos electrónicos enviados a usuarios suscritos o con adhesión voluntaria** y selecciona **Braze predeterminado** como URL y mail-to estándar de Braze. 

\![Opción de incluir automáticamente una cabecera de cancelar suscripción en los correos electrónicos enviados a usuarios suscritos o con adhesión voluntaria.]({% image_buster /assets/img/email_settings/email_unsubscribe_header.png %})

Braze admite las siguientes versiones del encabezado cancelar suscripción:

| Versión de la lista para cancelar suscripción | Descripción | 
| ----- | --- |
| Un clic (RFC 8058) | Ofrece a los destinatarios una forma sencilla de darse de baja de los correos electrónicos con un solo clic. Es un requisito de Yahoo y Gmail para los remitentes masivos. |
| URL para cancelar suscripción a la lista o HTTPS | Proporciona a los destinatarios un enlace que les dirige a una página Web donde pueden cancelar suscripción. |
| Mailto | Especifica una dirección de correo electrónico como destino del mensaje de solicitud de cancelar suscripción que el destinatario enviará a la marca. <br><br> _Para procesar las solicitudes de cancelación de suscripción a listas de correo, dichas solicitudes de cancelación de suscripción deben incluir la dirección de correo electrónico almacenada en Braze del Usuario final que se está dando de baja. Puede proporcionarlo la "dirección de origen" del correo electrónico desde el que el usuario final se está dando de baja, el asunto codificado o el cuerpo codificado del correo electrónico recibido por el usuario final del que se está dando de baja. En casos muy limitados, algunos proveedores de buzón de entrada no se adhieren al protocolo [RFC 2368](https://datatracker.ietf.org/doc/html/rfc2368), lo que provoca que la dirección de correo electrónico no se transmita correctamente. Esto puede provocar que una solicitud de cancelar suscripción no pueda procesarse en Braze._ |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Cuando Braze recibe una solicitud de cancelar suscripción a una lista de un usuario a través de cualquiera de los métodos anteriores, el estado global de suscripción por correo electrónico de este usuario se establece como cancelado. Si no hay ninguna coincidencia, Braze no procesará esta solicitud.

### Cancelar suscripción con un clic

El uso de cancelar suscripción con un clic para la cabecera de baja de lista[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) se centra en proporcionar una forma sencilla de que los destinatarios puedan darse de baja de los correos electrónicos.

### Lista para cancelar suscripción a nivel de mensaje con un clic

La configuración de cancelar suscripción a la lista de mensajes con un clic anulará la característica del encabezado de cancelación de suscripción de correo electrónico para los espacios de trabajo. Aplica el comportamiento de cancelar suscripción con un clic por campaña o paso en Canvas para los siguientes usos:

- Añade una cancelación suscripción Braze con un clic para un grupo de suscripción específico para dar soporte a múltiples marcas/listas dentro de un espacio de trabajo
- Alterna entre la URL predeterminada de Braze para cancelar suscripción o la personalizada
- Añade tu URL personalizada para cancelar suscripción con un clic
- Omitir cancelar suscripción con un clic en este mensaje

{% alert note %}
La configuración de cancelar suscripción con un clic a nivel de mensaje sólo está disponible cuando se utiliza el editor de arrastrar y soltar y el editor HTML actualizado. Si estás utilizando el editor HTML anterior, cambia al editor HTML actualizado para utilizar esta característica.
{% endalert %}

En tu editor de correo electrónico, ve a **Configuración de envío** > **Información de envío**. Selecciona una de las siguientes opciones:

- **Utiliza el espacio de trabajo predeterminado**: Utiliza la configuración **del encabezado de cancelar suscripción de correo electrónico** establecida en **Preferencias de correo electrónico**. Cualquier cambio realizado en esta configuración se aplicará a todos los mensajes.
- **Cancelar suscripción global a todos los correos electrónicos**: Utiliza el encabezado predeterminado de cancelar suscripción con un clic de Braze. Los usuarios que hagan clic en el botón cancelar suscripción tendrán su estado de suscripción global de correo electrónico establecido en "Desuscrito".
- **Cancelar suscripción a un grupo de suscripción específico**: Utiliza el grupo de suscripción especificado. Los usuarios que hagan clic en el botón cancelar suscripción se darán de baja del grupo de suscripción seleccionado.
    - Cuando selecciones un grupo de suscripción, añade el filtro **de grupo de suscripción** en **Audiencias objetivo** para dirigirte sólo a los usuarios que estén suscritos a este grupo específico. El grupo de suscripción seleccionado para cancelar suscripción con un clic debe coincidir con el grupo de suscripción al que te diriges. Si hay una falta de coincidencia en el grupo de suscripción, puedes arriesgarte a enviar a un usuario que está intentando cancelar suscripción de un grupo de suscripción del que ya se ha dado de baja.

{% alert important %}
La configuración **de cancelar suscripción de un grupo de suscripción específico** sólo se aplica al encabezado de cancelar suscripción de la lista con un clic. El encabezado de la lista de correo para cancelar suscripción no se ve afectado al seleccionar esta opción. Esto significa que un destinatario que cancele suscripción utilizando este método registrará una cancelación de suscripción global, no una cancelación de suscripción del grupo de suscripción específico. Para excluir la cabecera mailto list-unsubscribe de cancelar suscripción globalmente a los usuarios, cuando selecciones esta configuración, ponte en contacto con [el Soporte]({{site.baseurl}}/support_contact/).
{% endalert %}

- **Personalizados:** Añade tu URL personalizada de cancelar suscripción con un clic para que puedas procesar directamente las bajas.
- **Excluir cancelar suscripción**

{% alert important %}
Excluir la cancelación suscripción con un clic o cualquier mecanismo de cancelación de suscripción sólo debe hacerse para la mensajería transaccional, como restablecimiento de contraseñas, recibos y correos electrónicos de confirmación.
{% endalert %}

Ajustar esta configuración anulará el comportamiento predeterminado para cancelar suscripción a la lista con un clic en este correo electrónico.

\![]({% image_buster /assets/img/email_settings/one_click_list_unsubscribe_message_level.png %}){: style="max-width:70%;"}

#### Requisitos

Si envías correos electrónicos utilizando tu propia funcionalidad personalizada para cancelar suscripción, debes cumplir los siguientes requisitos para asegurarte de que la URL de cancelación de suscripción con un clic que configures se ajusta a la RFC 8058:

* La URL debe poder gestionar las solicitudes POST de cancelar suscripción.
* La URL debe empezar por `https://`.
* La URL no debe devolver una redirección HTTPS ni un cuerpo. Los enlaces para cancelar suscripción con un clic que van a una página de aterrizaje u otro tipo de página Web no cumplen la RFC 8058.
* Las solicitudes POST no deben establecer cookies.

Selecciona **Encabezado personalizado de cancelar suscripción** para añadir tu propio punto final de cancelar suscripción configurado con un clic, y un "mailto:" opcional. Braze requiere una entrada para que la URL admita un encabezado personalizado de cancelar suscripción porque la cancelación de suscripción HTTP con un clic es un requisito de Yahoo y Gmail para los remitentes masivos.

\![]({% image_buster /assets/img/email_settings/email_unsubscribe_header_custom.png %}){: style="max-width:80%;"}

## Añade líneas del asunto del correo electrónico

Alterna entre "[PRUEBA]" y "[SEMILLA]" en las líneas del asunto de tus correos electrónicos de prueba y semilla. Esto puede ayudar a identificar cualquier campaña de correo electrónico enviada como prueba.

\![]({% image_buster /assets/img/email_settings/test_and_seed_email_subject_line.png %}){: style="max-width:70%;"}

## CSS en línea en nuevos correos electrónicos predeterminados

El inlineado CSS es una técnica que inlinea automáticamente estilos CSS para tus correos electrónicos y nuevos correos. Para algunos clientes de correo electrónico, esto puede mejorar la forma en que se muestran tus correos electrónicos.

Cambiar esta configuración no afectará a ninguno de tus mensajes de correo electrónico o plantillas existentes. Puedes anular este valor predeterminado en cualquier momento mientras compones mensajes o plantillas. Para más información, consulta [CSS inlining]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/css_inline/).

## Reinscribir a los usuarios cuando cambie su correo electrónico

Puedes volver a suscribir automáticamente a los usuarios cuando cambien su dirección de correo electrónico. Por ejemplo, si un usuario de un espacio de trabajo previamente cancelado cambia su dirección de correo electrónico por otra que no esté en la lista de cancelación de suscripción de Braze, automáticamente volverá a estar suscrito.

\![]({% image_buster /assets/img/email_settings/resubscribe_users.png %}){: style="max-width:90%;" }

## Páginas de suscripción y pies de página

{% tabs local %}
{% tab Custom Footer %}

Para los correos electrónicos comerciales, la [Ley CAN-SPAM](https://en.wikipedia.org/wiki/CAN-SPAM_Act_of_2003) exige que todos los correos electrónicos comerciales incluyan una opción para cancelar la suscripción. Con la configuración personalizada del pie de página, puedes seguir cumpliendo la normativa CAN-SPAM y, al mismo tiempo, personalizar el pie de página de exclusión de tu correo electrónico. Para seguir cumpliendo la normativa, debes añadir tu pie de página personalizado a todos los correos electrónicos enviados como parte de campañas para este espacio de trabajo.

Ten en cuenta los siguientes requisitos al crear un pie de página personalizado para tu mensajería por correo electrónico:
- Debe incluir una URL para cancelar suscripción y una dirección postal física.
- Debe ser inferior a 100 KB.

\![]({% image_buster /assets/img/email_settings/custom_footer.png %})

Para obtener más información sobre la plantilla personalizada de pie de página Liquid, consulta nuestra documentación sobre [Pies de página personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

{% endtab %}
{% tab Custom Unsubscribe Page %}

Braze te permite configurar una **Página de cancelar suscripción personalizada** con tu propio HTML. Esta página aparecerá después de que un usuario haya seleccionado cancelar suscripción en la parte inferior de un correo electrónico. Ten en cuenta que esta página debe ocupar menos de 750 KB. 

\![]({% image_buster /assets/img/email_settings/custom_unsubscribe.png %})

Más información sobre las mejores prácticas para la gestión de listas de correo electrónico en [Gestión de suscripciones por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% tab Custom Opt-In Page %}

Puedes crear una página de adhesión voluntaria personalizada utilizando tu propio HTML. Incluir esto en tu correo electrónico puede ser especialmente beneficioso si quieres que tu marca y tu mensaje sean coherentes durante todo el ciclo de vida del usuario. Ten en cuenta que esta página debe ocupar menos de 750 KB. 

\![]({% image_buster /assets/img/email_settings/custom_opt_in.png %})

Más información sobre las mejores prácticas para la gestión de listas de correo electrónico en [Gestión de suscripciones por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/managing_email_subscriptions/#unsubscribed-email-addresses).

{% endtab %}
{% endtabs %}

## Preguntas más frecuentes

### Cancelar suscripción con un clic

{% details Can the one-click unsubscribe URL (via list-unsubscribe header) link to a preference center? %}
No, eso no se ajusta a la RFC 8058, lo que significa que no cumplirás el requisito de cancelar suscripción con un clic de Yahoo y Gmail.
{% enddetails %}

{% details Why do I receive the error message "Your email body does not include an unsubscribe link" when composing my preference center? %}
Un centro de preferencias no se considera un enlace para cancelar suscripción. Los destinatarios de tus correos electrónicos deben tener la opción de cancelar la suscripción a cualquier correo comercial para seguir cumpliendo la normativa CAN-SPAM.
{% enddetails %}

{% details Will I need to edit past email campaigns and Canvases to apply the one-click unsubscribe setting after enabling it? %}
Si no tienes ninguno de los casos de uso para la configuración de cancelar suscripción con un clic en la lista de correo electrónico a nivel de mensaje, no es necesaria ninguna acción, siempre y cuando la configuración esté activada en **Preferencias de correo electrónico**. Braze añadirá automáticamente las cabeceras de cancelar suscripción con un clic a todos los mensajes salientes de marketing y promocionales. Sin embargo, si necesitas configurar el comportamiento de cancelar suscripción con un clic a nivel de mensaje, tendrás que actualizar las campañas anteriores y los pasos en Canvas con el correo electrónico en consecuencia.
{% enddetails %}

{% details I can see the list-unsubscribe and one-click unsubscribe header in the original message or raw data, but why don't I see the Unsubscribe button in Gmail or Yahoo? %}
Gmail y Yahoo deciden en última instancia si muestran o no el encabezado de cancelar suscripción con un clic o con una lista. En el caso de remitentes nuevos o con poca reputación del remitente, esto puede hacer que ocasionalmente no se muestre el botón de cancelar suscripción.
{% enddetails %}

{% details Does the custom one-click unsubscribe header support Liquid? %}
Sí, Liquid y la lógica condicional son compatibles para permitir URL dinámicas de cancelar suscripción con un clic para el encabezado.
{% enddetails %}

{% alert tip %}
Si añades lógica condicional, evita tener valores de salida que añadan espacios en blanco a tu URL, ya que Braze no los elimina.
{% endalert %}

### Lista para cancelar suscripción a nivel de mensaje con un clic

{% details If I add the email headers for one-click manually, and I have the email unsubscribe header turned on, what is the expected behavior? %}
Las cabeceras de correo electrónico añadidas para cancelar suscripción con un clic se aplicarán a todos los envíos futuros de esta campaña.
{% enddetails %}

{% details Why do subscription groups have to match across message variants in order to launch? %}
Para una campaña con pruebas A/B, Braze enviará aleatoriamente a un usuario una de las variantes. Si tienes dos grupos de suscripción diferentes configurados en la misma campaña (la variante A está configurada en el grupo de suscripción A, y la variante B está configurada en el grupo de suscripción B), no podemos garantizar que los usuarios que sólo estén suscritos al grupo de suscripción B reciban la variante B. Puede darse el caso de que los usuarios estén cancelando suscripción de un grupo de suscripción del que ya se han dado de baja.
{% enddetails %}

{% details The email unsubscribe header setting is turned off in Email Preferences, but in my campaign's sending info, the one-click list-unsubscribe setting is set to "Use workspace default". Is this a bug? %}
No. Si la configuración del espacio de trabajo está desactivada y la configuración del mensaje está establecida en **Usar espacio de trabajo predeterminado**, entonces Braze seguirá lo que esté configurado en **Preferencias de correo electrónico**. Esto significa que no añadiremos el encabezado de cancelar suscripción con un clic para la campaña.
{% enddetails %}

{% details What happens if a subscription group is archived? Will this break the one-click unsubscribe on emails sent? %}
Si se archiva un grupo de suscripción al que se hace referencia en **Información de envío** para un clic, Braze seguirá procesando las cancelaciones de suscripción de un clic. El grupo de suscripción ya no se mostrará en el panel (filtro de segmentos, perfil de usuario y áreas similares).
{% enddetails %}

{% details Is the one-click unsubscribe setting available for email templates? %}
No, actualmente no tenemos planes de añadir esto para las plantillas de correo electrónico, ya que estas plantillas no están asignadas a un dominio de envío. Si te interesa esta característica para las plantillas de correo electrónico, envía [tus comentarios sobre el producto]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).
{% enddetails %}

{% details Does this feature check that the one-click unsubscribe URL added to the custom option is valid? %}
No, no comprobamos ni validamos ningún enlace en el panel de Braze. Asegúrate de probar adecuadamente tu URL antes del lanzamiento.
{% enddetails %}


