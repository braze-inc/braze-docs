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
{% endtabs %}

## Probar campañas personalizadas 

Si está probando campañas que rellenan datos de usuario o utilizan propiedades de evento personalizadas, tendrá que tomar medidas adicionales o diferentes.

### Probar campañas personalizadas con atributos de usuario

Si utilizas [la personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/) en tu mensaje, tendrás que tomar medidas adicionales para previsualizar adecuadamente tu campaña y comprobar que los datos de usuario rellenan correctamente el contenido.

Cuando envíe un mensaje de prueba, asegúrese de elegir la opción **Seleccionar usuario existente** o Vista previa como **usuario personalizado**.

![Probar un mensaje personalizado]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Seleccionar un usuario existente

Si selecciona un usuario existente, introduzca el ID de usuario específico o el correo electrónico en el campo de búsqueda. A continuación, utiliza la vista previa del panel de control para ver qué aspecto tendría tu mensaje para ese usuario y envía un mensaje de prueba a tu dispositivo que refleje lo que vería ese usuario.

![Selecciona un usuario]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Seleccionar un usuario personalizado

Si realiza una vista previa como usuario personalizado, introduzca texto para los distintos campos disponibles para la personalización, como el nombre del usuario y cualquier atributo personalizado. Una vez más, puedes ingresar tu propia dirección de correo electrónico para enviar una prueba a tu dispositivo.

![Usuario personalizado]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

### Probar campañas personalizadas con propiedades de eventos personalizadas

Probar campañas personalizadas con [propiedades del evento personalizadas]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#custom-event-properties) difiere ligeramente de probar otros tipos de campañas esbozadas. La forma más sólida de probar campañas personalizadas utilizando propiedades de eventos personalizados es activar la campaña usted mismo haciendo lo siguiente:

1. Escribe la copia que implica la propiedad del evento. ![Componer mensaje de prueba con propiedades]({% image_buster /assets/img_archive/testeventproperties-compose.png %})
2. Utiliza la [entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para entregar la campaña cuando se produzca el evento.

{% alert note %}
Si estás probando una campaña push para iOS, debes establecer el retraso en 1 minuto para que te dé tiempo a salir de la aplicación, ya que iOS no entrega notificaciones push para la aplicación abierta en ese momento. Otros tipos de campañas pueden configurarse para delivery inmediato.
{% endalert %}

![Prueba de entrega de mensajes]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3\. Seleccione a los usuarios como lo haría para las pruebas utilizando un filtro de pruebas o seleccionando su propia dirección de correo electrónico y termine de crear la campaña. 

![Prueba de orientación de mensajes]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4\. Entra en tu aplicación y completa el evento personalizado.

La campaña se activará y mostrará el mensaje personalizado con la propiedad de evento.

![Ejemplo de mensaje de prueba]({% image_buster /assets/img_archive/testeventproperties-message.PNG %})

Alternativamente, si guardas ID de usuario personalizadas, también puedes probar la campaña enviándote un mensaje de prueba personalizado a ti mismo.

1. Escriba el texto de su campaña.
2. Seleccione la pestaña **Prueba** y elija **Usuario personalizado**. 
3. Añade la propiedad del evento personalizado en la parte inferior de la página, y añade tu ID de usuario o dirección de correo electrónico en la casilla superior.
4. Haga clic en **Enviar prueba** para recibir un mensaje personalizado con la propiedad.

![Pruebas mediante usuario personalizado]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

