---
nav_title: Envío de mensajes de prueba
article_title: Envío de mensajes de prueba
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Este artículo de referencia explica cómo enviar mensajes de prueba a través de los distintos canales Braze y cómo incorporar propiedades de eventos personalizados o atributos de usuario."

---

# Envío de mensajes de prueba

> Antes de enviar una campaña de mensajería a tus usuarios, como mejor práctica sugerida, te recomendamos que la pruebes para asegurarte de que tiene el aspecto adecuado y funciona según lo previsto. Puedes crear y enviar mensajes de prueba a determinados dispositivos o miembros del equipo utilizando las herramientas del panel de Braze.

{% alert important %}
Asegúrate de guardar el borrador de tu campaña después de probarla para evitar que se borre. Puedes enviar mensajes de prueba sin guardar el mensaje como borrador.
{% endalert %}

## Paso 1: Identifica a tus usuarios de prueba

Antes de probar tu campaña de mensajería, es importante identificar a tus usuarios de prueba. Estos usuarios pueden ser ID de usuario o direcciones de correo electrónico existentes, o usuarios nuevos que se utilizan exclusivamente para probar campañas de mensajería. 

### Opcional: Crear un grupo de prueba de contenidos

Una forma práctica de organizar a tus usuarios de prueba es crear un [Grupo de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), que incluye un grupo de usuarios que recibirán mensajes de prueba de las campañas. Puedes añadir este grupo de prueba al campo **Añadir grupos de prueba de contenido** en **Destinatarios de prueba** de tu campaña, y lanzar tus pruebas sin crear ni añadir usuarios de prueba individuales.

## Paso 2: Enviar mensajes de prueba específicos del canal

Para conocer los pasos para enviar mensajes de prueba, consulta la sección siguiente para tu canal respectivo.

{% tabs local %}
{% tab Email %}

1. Redacta tu mensaje de correo electrónico.
2. Selecciona **Vista previa y Prueba**.
3. Selecciona la pestaña **Envío de prueba** y añade tu dirección de correo electrónico o ID de usuario en el campo **Añadir usuarios individuales**. 
4. Selecciona **Enviar prueba** para enviar el correo electrónico redactado a tu buzón de entrada.

\![Correo electrónico de prueba]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab Push %}

#### Push móvil

1. Redacta tu push móvil.
2. Selecciona la pestaña **Configuración** y añade tu dirección de correo electrónico o ID de usuario en el campo **Añadir usuarios individuales**.
3. Selecciona **Enviar prueba** para enviar tu mensaje redactado a tu dispositivo.

\![Prueba push]({% image_buster /assets/img_archive/testpush.png %})

#### Web push

1. Crea tu notificación push web.
2. Selecciona la pestaña **Prueba**. 
3. Selecciona **Enviar prueba a mí mismo**.
4. Selecciona **Enviar prueba** para enviar tu notificación push web a tu navegador web.

\![Prueba push web]({% image_buster /assets/img_archive/testwebpush.png %})

Si ya has aceptado mensajes push desde el panel de Braze, el push aparecerá en la esquina de tu pantalla. De lo contrario, haz clic en **Permitir** cuando se te solicite y aparecerá el mensaje.

{% endtab %}
{% tab In-App Message %}

Si tienes configuradas notificaciones push dentro de tu aplicación y en tu dispositivo de prueba, puedes enviar mensajes dentro de la aplicación de prueba a tu aplicación para ver cómo es en tiempo real. 

1. Redacta tu mensaje dentro de la aplicación.
2. Selecciona la pestaña **Prueba** y añade tu dirección de correo electrónico o ID de usuario en el campo **Añadir usuarios individuales**. 
3. Selecciona **Enviar prueba** para enviar tu mensaje push a tu dispositivo.

Aparecerá un mensaje push de prueba en la parte superior de la pantalla de tu dispositivo.

Prueba en la aplicación]({% image_buster /assets/img_archive/test-in-app.png %})

Si haces clic directamente y abres el mensaje push, accederás a tu aplicación, donde podrás ver tu prueba de mensajes dentro de la aplicación. Ten en cuenta que esta característica de prueba de mensajes dentro de la aplicación depende de que el usuario haga clic en una notificación push de prueba para desencadenar el mensaje dentro de la aplicación. Como tal, el usuario debe ser elegible para recibir notificaciones push en la aplicación correspondiente para la entrega correcta de la notificación push de prueba.

{% endtab %}
{% tab Content Card %}

Después de crear tu tarjeta de contenido, puedes enviar una tarjeta de contenido de prueba a tu aplicación para ver qué aspecto tendrá en tiempo real.

1. Redacta tu tarjeta de contenido.
2. Selecciona la pestaña **Prueba** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba. 
3. Selecciona **Enviar prueba** para enviar tu tarjeta de contenido a tu aplicación.

\![Tarjeta de contenido de prueba]({% image_buster /assets/img/contentcard_test.png %})

{% endtab %}
{% tab SMS/MMS %}

Después de crear tu mensaje SMS o MMS, puedes enviar un mensaje de prueba a tu teléfono para ver qué aspecto tendrá en tiempo real. 

1. Redacta tu mensaje SMS o MMS.
2. Selecciona la pestaña **Prueba** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba. 
3. Selecciona **Enviar prueba** para enviar tu mensaje de prueba.

\![Tarjeta de contenido de prueba]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Después de crear tu webhook, puedes hacer un envío de prueba para comprobar la respuesta del webhook. Selecciona la pestaña **Prueba** y selecciona **Enviar prueba** para realizar un envío de prueba a la URL del webhook suministrado. También puedes seleccionar un usuario individual para obtener una vista previa de la respuesta como usuario específico. 

\![Tarjeta de contenido de prueba]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% endtabs %}

## Probar campañas personalizadas 

Si estás probando campañas que rellenan datos de usuario o utilizan propiedades del evento personalizadas, tendrás que dar pasos adicionales o diferentes.

### Campañas de prueba personalizadas con atributos de usuario

Si utilizas [la personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/) en tu mensaje, tendrás que tomar medidas adicionales para previsualizar adecuadamente tu campaña y comprobar que los datos de usuario rellenan correctamente el contenido.

Cuando envíes un mensaje de prueba, asegúrate de elegir la opción **Seleccionar usuario existente** o la vista previa como **Usuario personalizado**.

\![Probar un mensaje personalizado]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Seleccionar un usuario existente

Si seleccionas un usuario existente, introduce el ID de usuario o correo electrónico específico en el campo de búsqueda. A continuación, utiliza la vista previa del panel para ver cómo le aparecería tu mensaje a ese usuario, y envía un mensaje de prueba a tu dispositivo que refleje lo que vería ese usuario.

\![Selecciona un usuario]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Seleccionar un usuario personalizado

Si la vista previa es como usuario personalizado, introduce texto para los distintos campos disponibles para la personalización, como el nombre del usuario y cualquier atributo personalizado. Una vez más, puedes introducir tu propia dirección de correo electrónico para enviar una prueba a tu dispositivo.

Usuario personalizado]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

### Probar campañas personalizadas con propiedades del evento personalizadas

Probar campañas personalizadas con [propiedades del evento personalizadas]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) difiere ligeramente de probar otros tipos de campañas esbozadas. 

{% tabs local %}
{% tab Trigger manually %}

#### Método 1: Desencadenar la campaña manualmente

Puedes desencadenar tú mismo la campaña como una forma sólida de probar campañas personalizadas utilizando propiedades del evento personalizadas:

1. Escribe la copia relativa a la propiedad del evento. 

\![Componer mensaje de prueba con propiedades]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2\. Utiliza la [entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para entregar la campaña cuando se produzca el evento.

{% alert note %}
Si estás probando una campaña push de iOS, debes establecer el retraso en un minuto para que te dé tiempo a salir de la aplicación, ya que iOS no entrega notificaciones push para la aplicación abierta en ese momento. Otros tipos de campañas pueden configurarse para que se entreguen inmediatamente.
{% endalert %}

\![Prueba de entrega de mensajes]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3\. Dirígete a los usuarios como lo harías para las pruebas, utilizando un filtro de pruebas o dirigiéndote a tu propia dirección de correo electrónico, y termina de crear la campaña. 

\![Prueba de selección de mensajes]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4\. Entra en tu aplicación y completa el evento personalizado.

La campaña desencadenará y mostrará el mensaje personalizado con la propiedad del evento.

\![Ejemplo de mensaje de prueba]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Test message %}

#### Método 2: Enviarte un mensaje de prueba

Alternativamente, si guardas ID de usuario personalizados, también puedes probar la campaña enviándote a ti mismo un mensaje de prueba personalizado.

1. Escribe el texto de tu campaña.
2. Selecciona la pestaña **Prueba** y elige **Usuario personalizado**. 
3. Añade la propiedad del evento personalizado en la parte inferior de la página, y añade tu ID de usuario o dirección de correo electrónico en la casilla superior.
4. Selecciona **Enviar prueba** para recibir un mensaje personalizado con la propiedad.

\![Pruebas con usuario personalizado]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Método 3: Utilizar Liquid

Puedes probar las propiedades del evento personalizado introduciendo manualmente los valores con Liquid. 

1. En el editor de mensajes, introduce valores para tus propiedades del evento personalizadas.
2. Selecciona la pestaña **Vista previa como usuario** para comprobar que se muestra el mensaje correcto.

{% endtab %}
{% endtabs %}

## Solución de problemas

### Mensajes dentro de la aplicación

Si tu campaña de mensajes dentro de la aplicación no está desencadenada por una campaña push, comprueba la segmentación de la campaña dentro de la aplicación para confirmar que el usuario cumple con la audiencia objetivo **antes de** recibir el mensaje push.

En los envíos de prueba en Android e iOS, es posible que los mensajes dentro de la aplicación que utilizan el comportamiento **Solicitar permiso** push al hacer clic no se muestren en algunos dispositivos. Como solución:
- **Android:** Los dispositivos deben tener Android 13 y nuestro SDK para Android versión 21.0.0. Otra razón puede ser que el dispositivo en el que se muestra el mensaje dentro de la aplicación ya tenga un aviso a nivel de sistema. Es posible que hayas seleccionado **No volver a preguntar**, por lo que puede que tengas que reinstalar la aplicación para restablecer los permisos de notificación antes de volver a probarla.
- **iOS:** Recomendamos a tu equipo de desarrolladores que revise la implementación de las notificaciones push de tu aplicación y elimine manualmente cualquier código que solicite permisos push. Para más información, consulta [Push primer mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

Para entregar una campaña de mensajería dentro de la aplicación basada en acciones, los eventos personalizados deben registrarse a través del SDK de Braze, no de las API REST, para que el usuario pueda recibir mensajes elegibles dentro de la aplicación directamente en su dispositivo. Los usuarios pueden recibir el mensaje dentro de la aplicación si realizan el evento durante la sesión.
