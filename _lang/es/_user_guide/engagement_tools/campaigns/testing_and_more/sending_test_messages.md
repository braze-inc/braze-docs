---
nav_title: Cómo enviar mensajes de prueba
article_title: Cómo enviar mensajes de prueba
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Este artículo de referencia explica cómo enviar mensajes de prueba a través de los distintos canales Braze y cómo incorporar propiedades de eventos personalizados o atributos de usuario."

---

# Envío de mensajes de prueba

> Antes de enviar una campaña de mensajería a tus usuarios, como mejor práctica sugerida, te recomendamos que la pruebes para asegurarte de que tiene el aspecto adecuado y funciona según lo previsto. Puede crear y enviar mensajes de prueba a determinados dispositivos o miembros del equipo mediante las herramientas del panel Braze.

{% alert important %}
Asegúrese de guardar el borrador de la campaña después de probarla para evitar que se borre. Puedes enviar mensajes de prueba sin guardar el mensaje como borrador.
{% endalert %}

## Paso 1: Identifica a tus usuarios de prueba

Antes de probar su campaña de mensajería, es importante identificar a sus usuarios de prueba. Estos usuarios pueden ser ID de usuario o direcciones de correo electrónico existentes, o bien usuarios nuevos que se utilizan exclusivamente para probar campañas de mensajería. 

### Opcional: Crear un grupo de prueba de contenidos

Una forma práctica de organizar a los usuarios de prueba es crear un [Grupo de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), que incluye un grupo de usuarios que recibirán mensajes de prueba de las campañas. Puede añadir este grupo de prueba en el campo **Añadir grupos de prueba de contenido** bajo **Destinatarios de prueba** en su campaña, y lanzar sus pruebas sin crear o añadir usuarios de prueba individuales.

## Paso 2: Enviar mensajes de prueba específicos del canal

Para conocer los pasos para enviar mensajes de prueba, consulte la siguiente sección para su canal respectivo.

{% tabs %}
{% tab Correo electrónico %}

1. Redacte su mensaje de correo electrónico.
2. Haga clic en **Previsualizar y probar**.
3. Seleccione la pestaña **Enviar prueba** y añada su dirección de correo electrónico o ID de usuario en el campo **Añadir usuarios individuales**. 
4. Haga clic en **Enviar prueba** para enviar el borrador de correo electrónico a su bandeja de entrada.

![Correo electrónico de prueba]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Notificaciones push móvil

1. Redacta tu push móvil.
2. Seleccione la pestaña **Configuración** y añada su dirección de correo electrónico o ID de usuario en el campo **Añadir usuarios individuales**.
3. Haz clic en **Enviar prueba** para enviar el mensaje redactado a tu dispositivo.

![Push de prueba]({% image_buster /assets/img_archive/testpush.png %})

#### Web push

1. Crea tu notificación push web.
2. Seleccione la pestaña **Prueba**. 
3. Comprueba **Enviar prueba a mí mismo**.
4. Haga clic en **Enviar prueba** para enviar su web push a su navegador web.

![Notificación push web de prueba]({% image_buster /assets/img_archive/testwebpush.png %})

Si ya has aceptado mensajes push desde el salpicadero de Braze, el push aparecerá en la esquina de tu pantalla. De lo contrario, haga clic en **Permitir** cuando se le solicite y aparecerá el mensaje.

{% endtab %}
{% tab Mensaje en la aplicación %}

Si tienes configuradas notificaciones push en tu aplicación y en tu dispositivo de prueba, puedes enviar mensajes de prueba a tu aplicación para ver cómo se ve en tiempo real. 

1. Redacta tu mensaje en la aplicación.
2. Seleccione la pestaña **Prueba** y añada su dirección de correo electrónico o ID de usuario en el campo **Añadir usuarios individuales**. 
3. Haga clic en **Enviar prueba** para enviar el mensaje push al dispositivo.

Aparecerá un mensaje push de prueba en la parte superior de la pantalla de tu dispositivo.

![Pruebe In App]({% image_buster /assets/img_archive/test-in-app.png %})

Al hacer clic directamente en el mensaje push y abrirlo, accederá a su aplicación, donde podrá ver su prueba de mensajes in-app. Tenga en cuenta que esta función de prueba de mensajes en la aplicación depende de que el usuario haga clic en una notificación push de prueba para activar el mensaje en la aplicación. Para que la notificación push de prueba se envíe correctamente, el usuario debe estar habilitado para recibir notificaciones push en la aplicación correspondiente.

#### Solución de problemas

* Si tu campaña de mensajes in-app no se activa con una campaña push, comprueba la segmentación de la campaña in-app para confirmar que el usuario se ajusta al público objetivo **antes de** recibir el mensaje push.
* En los envíos de prueba en Android e iOS, es posible que los mensajes in-app que utilizan el comportamiento **Solicitar permiso** push al hacer clic no se muestren en algunos dispositivos. Como solución:
  * **Android:** Los dispositivos deben tener Android 13 y nuestro SDK para Android versión 21.0.0. Otra razón puede ser que el dispositivo en el que se muestra el mensaje in-app ya tenga un aviso a nivel de sistema. Es posible que hayas seleccionado **No volver a preguntar**, por lo que puede que tengas que reinstalar la aplicación para restablecer los permisos de notificación antes de volver a probarla.
  * **iOS:** Recomendamos a su equipo de desarrolladores que revise la implementación de las notificaciones push para su aplicación y elimine manualmente cualquier código que solicite permisos push. Para más información, consulta [Mensajes push primer dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).
* Para que una campaña de mensajes in-app basada en acciones se entregue, los eventos personalizados deben registrarse a través del SDK Braze, no de las API REST, para que el usuario pueda recibir los mensajes in-app elegibles directamente en su dispositivo. Los usuarios pueden recibir el mensaje in-app si realizan el evento durante la sesión.

{% endtab %}
{% tab Tarjeta de contenido %}

Después de crear su tarjeta de contenido, puede enviar una tarjeta de contenido de prueba a su aplicación para ver qué aspecto tendrá en tiempo real.

1. Redacta tu tarjeta de contenido.
2. Seleccione la pestaña **Prueba** y seleccione al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba. 
3. Haga clic en **Enviar prueba** para enviar la tarjeta de contenido a la aplicación.

![Tarjeta de contenido de prueba]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

Después de crear tu mensaje SMS o MMS, puedes enviar un mensaje de prueba a tu teléfono para ver qué aspecto tendrá en tiempo real. 

1. Redacta tu mensaje SMS o MMS.
2. Seleccione la pestaña **Prueba** y seleccione al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba. 
3. Haga clic en **Enviar prueba** para enviar su mensaje de prueba.

![Tarjeta de contenido de prueba]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Después de crear tu webhook, puedes hacer un envío de prueba para comprobar la respuesta del webhook. Seleccione la pestaña **Prueba** y seleccione **Enviar prueba** para enviar un envío de prueba a la URL de webhook suministrada. También puede seleccionar un usuario individual para previsualizar la respuesta como un usuario específico. 

![Tarjeta de contenido de prueba]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab Canal de noticias %}

{% multi_lang_include deprecations/braze_sdk/news_feed.md %}

Para enviar una tarjeta de noticias de prueba es necesario configurar un segmento de prueba y enviar una campaña de prueba.

##### Paso 1: Crear un segmento de prueba designado

Una vez configurado un segmento de prueba, puede utilizar estos canales de mensajería. El proceso requiere unos breves pasos y, si se configura correctamente, sólo tendrá que hacerse una vez.

1. Vaya a la página **Segmentos** y [cree un nuevo segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/). 
2. Haga clic en el menú desplegable de **Añadir filtro** y localice los filtros de comprobación en la parte inferior de la lista <br><br>![Prueba de filtros]({% image_buster /assets/img_archive/testmessages1.png %})<br><br>
3. Utilice los filtros de comprobación para seleccionar usuarios con direcciones de correo electrónico específicas o [ID de usuario]({{site.baseurl}}/developer_guide/analytics/setting_user_ids/?tab=swift) externos.<br><br>![Prueba de las opciones de filtro]({% image_buster /assets/img_archive/testmessages2.png %})
<br><br>Estos filtros tienen las siguientes opciones:
- **Es igual**: Busca una coincidencia exacta con el correo electrónico o el ID de usuario que proporcione. Utilízalo si solo quieres enviar las campañas de prueba a dispositivos asociados a un único correo electrónico o ID de usuario.
- **No es igual**: Excluye un determinado correo electrónico o ID de usuario de las campañas de prueba.
- **Partidos**: Busca usuarios que tengan direcciones de correo electrónico o ID de usuario que coincidan con parte del término de búsqueda que proporciones. Podrías utilizarlo para encontrar sólo a los usuarios con una dirección "@yourcompany.com", lo que te permitiría enviar mensajes a todos los miembros de tu equipo.
<br><br>
Estos filtros también pueden utilizarse conjuntamente para limitar la lista de usuarios de prueba. Por ejemplo, el segmento de prueba podría incluir un filtro de direcciones de correo electrónico que `matches` "@braze.com" y otro filtro que `does not equal` "sales@braze.com". También puedes seleccionar varios correos electrónicos específicos utilizando la opción `matches` y separando las direcciones de correo electrónico con un carácter "|" (por ejemplo, `matches` "email1@braze.com|email2@braze.com").
<br><br>
4. Añada los filtros de prueba a su segmento de prueba.
5. Haga clic en **Vista previa** en la parte superior del editor de segmentos o exporte los datos de usuario de ese segmento a CSV para verificar que ha seleccionado sólo los usuarios que pretendía.
6. Haga clic en el menú desplegable **Datos de usuario** y seleccione **CSV Exportar todos los datos de usuario** para exportar los datos de usuario del segmento. 

![Verificar segmento de prueba]({% image_buster /assets/img_archive/testmessages3.png %})

> Exportar los datos de usuario del segmento en formato CSV te dará la imagen más precisa de quién se incluye en ese segmento. La ficha **Vista previa** es sólo una muestra de los usuarios del segmento y, por lo tanto, puede parecer que no se han seleccionado todos los miembros previstos. Para más información, consulte [Visualización y comprensión de datos de segmentos][7].

Una vez que haya confirmado que sólo se dirige a los usuarios que desea que reciban el mensaje de prueba, puede seleccionar este segmento en una campaña existente que desee probar o hacer clic en el botón **Iniciar campaña** del menú de segmentos.

##### Paso 2: Enviar una campaña de prueba

Para enviar tarjetas de noticias de prueba, debe dirigirse al segmento de prueba creado previamente. Empiece por crear una campaña multicanal y siga los pasos habituales. Cuando llegue al paso **Usuarios objetivo**, seleccione su segmento de prueba como se muestra en la siguiente imagen.

![Segmento de prueba]({% image_buster /assets/img_archive/test_segment.png %})

Termina de confirmar la campaña y lánzala para probar tus tarjetas de canal de noticias.

> Si tiene intención de utilizar una sola campaña para enviarse un mensaje de prueba más de una vez, marque la casilla "Permitir que los usuarios vuelvan a ser elegibles para recibir la campaña" en la parte **Programación** del compositor de la campaña.

{% endtab %}
{% endtabs %}

## Probar campañas personalizadas 

Si está probando campañas que rellenan datos de usuario o utilizan propiedades de evento personalizadas, tendrá que tomar medidas adicionales o diferentes.

### Probar campañas personalizadas con atributos de usuario

Si utiliza [personalización][26] en su mensaje, tendrá que tomar medidas adicionales para previsualizar correctamente su campaña y comprobar que los datos del usuario rellenan correctamente el contenido.

Cuando envíe un mensaje de prueba, asegúrese de elegir la opción **Seleccionar usuario existente** o Vista previa como **usuario personalizado**.

![Probar un mensaje personalizado][23]{: style="max-width:70%;" }

#### Seleccionar un usuario existente

Si selecciona un usuario existente, introduzca el ID de usuario específico o el correo electrónico en el campo de búsqueda. A continuación, utiliza la vista previa del panel de control para ver qué aspecto tendría tu mensaje para ese usuario y envía un mensaje de prueba a tu dispositivo que refleje lo que vería ese usuario.

![Seleccionar un usuario][24]

#### Seleccionar un usuario personalizado

Si realiza una vista previa como usuario personalizado, introduzca texto para los distintos campos disponibles para la personalización, como el nombre del usuario y cualquier atributo personalizado. Una vez más, puedes ingresar tu propia dirección de correo electrónico para enviar una prueba a tu dispositivo.

![Usuario personalizado][25]

### Probar campañas personalizadas con propiedades de eventos personalizadas

Probar campañas personalizadas con [propiedades de eventos personalizados][19] difiere ligeramente de probar otros tipos de campañas descritas. La forma más sólida de probar campañas personalizadas utilizando propiedades de eventos personalizados es activar la campaña usted mismo haciendo lo siguiente:

1. Escribe la copia que implica la propiedad del evento. ![Composición de mensajes de prueba con propiedades][15]
2. Utilice [entrega basada en acciones][21] para entregar la campaña cuando se produzca el evento.

{% alert note %}
Si estás probando una campaña push para iOS, debes establecer el retraso en 1 minuto para que te dé tiempo a salir de la aplicación, ya que iOS no entrega notificaciones push para la aplicación abierta en ese momento. Otros tipos de campañas pueden configurarse para delivery inmediato.
{% endalert %}

![Entrega de mensajes de prueba][16]

{: start="3"}
3\. Seleccione a los usuarios como lo haría para las pruebas utilizando un filtro de pruebas o seleccionando su propia dirección de correo electrónico y termine de crear la campaña. 

![Segmentación de mensajes de prueba][17]

{: start="4"}
4\. Entra en tu aplicación y completa el evento personalizado.

La campaña se activará y mostrará el mensaje personalizado con la propiedad de evento.

![Ejemplo de mensaje de prueba][18]

Alternativamente, si guardas ID de usuario personalizadas, también puedes probar la campaña enviándote un mensaje de prueba personalizado a ti mismo.

1. Escriba el texto de su campaña.
2. Seleccione la pestaña **Prueba** y elija **Usuario personalizado**. 
3. Añade la propiedad del evento personalizado en la parte inferior de la página, y añade tu ID de usuario o dirección de correo electrónico en la casilla superior.
4. Haga clic en **Enviar prueba** para recibir un mensaje personalizado con la propiedad.

![Pruebas con el usuario personalizado][22]

[7]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#user-preview
[13]: {% image_buster /assets/img_archive/test-push-for-in-app.png %}
[15]: {% image_buster /assets/img_archive/testeventproperties-compose.png %}
[16]: {% image_buster /assets/img_archive/testeventproperties-delivery.png %}
[17]: {% image_buster /assets/img_archive/testeventproperties-target.png %}
[18]: {% image_buster /assets/img_archive/testeventproperties-message.PNG %}
[19]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties
[20]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/personalized_messaging/#personalized-messaging
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[22]: {% image_buster /assets/img_archive/testeventproperties-customuser.png %}
[23]: {% image_buster /assets/img_archive/personalized_testing.png %}
[24]: {% image_buster /assets/img_archive/personalized_testing_select.png %}
[25]: {% image_buster /assets/img_archive/personalized_testing_custom.png %}
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/
