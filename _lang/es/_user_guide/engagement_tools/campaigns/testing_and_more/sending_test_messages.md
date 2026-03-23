---
nav_title: Enviar mensajes de prueba
article_title: Enviar mensajes de prueba
page_order: 0
tool: 
  - Campaigns
page_type: reference
description: "Este artículo de referencia explica cómo enviar mensajes de prueba a través de los distintos canales de Braze y cómo incorporar propiedades de eventos personalizados o atributos de usuario."

---

# Enviar mensajes de prueba

> Antes de enviar una campaña de mensajería a tus usuarios, como mejor práctica sugerida, te recomendamos que la pruebes para asegurarte de que tiene el aspecto adecuado y funciona según lo previsto. Puedes crear y enviar mensajes de prueba a determinados dispositivos o miembros del equipo mediante las herramientas del panel de Braze.

{% alert important %}
Asegúrate de guardar el borrador de la campaña después de probarla para evitar que se borre. Puedes enviar mensajes de prueba sin guardar el mensaje como borrador.
{% endalert %}

## Paso 1: Identifica a tus usuarios de prueba

Antes de probar tu campaña de mensajería, es importante identificar a tus usuarios de prueba. Estos usuarios pueden ser ID de usuario o direcciones de correo electrónico existentes, o bien usuarios nuevos que se utilizan exclusivamente para probar campañas de mensajería. 

### Opcional: Crear un grupo de prueba de contenidos

Una forma práctica de organizar a los usuarios de prueba es crear un [grupo de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/), que incluye un grupo de usuarios que recibirán mensajes de prueba de las campañas. Puedes añadir este grupo de prueba al campo **Añadir grupos de prueba de contenido** en **Destinatarios de prueba** de tu campaña, y lanzar tus pruebas sin crear ni añadir usuarios de prueba individuales.

## Paso 2: Enviar mensajes de prueba específicos del canal

Para conocer los pasos para enviar mensajes de prueba, consulta la siguiente sección para tu canal respectivo.

{% tabs local %}
{% tab Banners %}

{% alert important %}
Antes de que puedas probar mensajes de Banner en Braze, tendrás que crear una campaña de Banner en Braze. Además, comprueba que la ubicación que quieres probar ya está [colocada en tu aplicación o sitio web]({{site.baseurl}}/developer_guide/banners/placements).
{% endalert %}

Después de crear tu mensaje de Banner, puedes obtener una vista previa de tu Banner o enviar un mensaje de prueba.

1. Redacta tu mensaje de Banner.
2. Selecciona **Vista previa** para previsualizar tu Banner o enviar un mensaje de prueba.
3. Para enviar un mensaje de prueba, añade un grupo de prueba de contenido o uno o varios usuarios individuales como **Destinatarios de prueba** y, a continuación, selecciona **Enviar prueba**. 

Podrás ver tu mensaje de prueba en el dispositivo durante un máximo de 5 minutos.

![Pestaña vista previa del compositor del Banner.]({% image_buster /assets/img/banners/preview_banner.png %})

{% alert note %}
Ten en cuenta que tu vista previa puede no ser idéntica a la representación final en el dispositivo de un usuario debido a las diferencias entre el hardware.
{% endalert %}

### Lista de comprobación

- ¿Tu campaña de Banner está asignada a un emplazamiento?
- ¿Las imágenes y los medios se muestran y actúan como se espera en los tipos y tamaños de pantalla de los dispositivos a los que te diriges?
- ¿Tus enlaces y botones dirigen al usuario a donde debe ir?
- ¿Funciona Liquid como se esperaba? ¿Has previsto un valor de atributo predeterminado en caso de que Liquid no devuelva ninguna información?
- ¿Es tu texto claro, conciso y correcto?

{% endtab %}
{% tab Content Card %}

{% alert warning %}
Para enviar una prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) o a usuarios individuales, antes de enviarla debe estar habilitada la función push en los dispositivos de prueba con tokens de notificaciones push válidos registrados para el usuario de prueba. Los usuarios de iOS deben tocar la notificación push enviada por Braze para ver la tarjeta de contenido de la prueba. Este comportamiento solo se aplica a las tarjetas de contenido de prueba.
{% endalert %}

Las tarjetas de contenido de prueba se entregan a través de una notificación push. La tarjeta se empaqueta en la carga útil del push, y el SDK la extrae y almacena en caché localmente cuando se recibe el push.

Este proceso omite el sistema normal de entrega de tarjetas, por lo que push debe estar habilitado aunque estés probando una tarjeta de contenido.

Las tarjetas de contenido de prueba caducan aproximadamente cinco minutos después de ser enviadas.

Después de crear tu tarjeta de contenido, puedes enviar una tarjeta de contenido de prueba a tu aplicación para ver qué aspecto tendrá en tiempo real.

1. Redacta tu tarjeta de contenido.
2. Selecciona la pestaña **Prueba** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba. 
3. Selecciona **Enviar prueba** para enviar tu tarjeta de contenido a tu aplicación.

![Tarjeta de contenido de prueba]({% image_buster /assets/img/contentcard_test.png %})

### Vista previa

Puedes obtener una vista previa de tu tarjeta mientras la compones en la pestaña **Vista previa**. Esto te ayudará a visualizar el mensaje final desde la perspectiva del usuario.

{% alert note %}
En la pestaña **Vista previa** de tu compositor, la vista de tu mensaje puede no ser idéntica a su representación real en el dispositivo del usuario. Recomendamos enviar siempre un mensaje de prueba a un dispositivo para asegurarte de que los medios, el texto, la personalización y los atributos personalizados se generan correctamente.
{% endalert %}

### Lista de comprobación

- ¿Tu usuario de prueba tiene habilitado push con un token de notificaciones push válido?
- ¿Las imágenes y los medios se muestran y actúan como se esperaba?
- ¿Funciona Liquid como se esperaba? ¿Has previsto un [valor de atributo predeterminado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) si Liquid no devuelve información?
- ¿Es tu texto claro, conciso y correcto?
- ¿Tus enlaces dirigen al usuario a donde debe ir?

### Depurar

Una vez enviadas las tarjetas de contenido, puedes desglosar o depurar cualquier problema desde el [registro de usuarios del evento]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) en la consola para desarrolladores. 

Un caso de uso común es tratar de depurar por qué un usuario no puede ver una tarjeta de contenido en particular. Para ello, puedes buscar en los **registros de usuarios del evento** las tarjetas de contenido entregadas al SDK al inicio de la sesión, pero antes de una impresión, y rastrearlas hasta una campaña específica:

1. Ve a **Configuración** > **Registro de usuarios del evento**.
2. Localiza y amplía la solicitud de SDK para tu usuario de prueba.
3. Haz clic en **Datos brutos**.
4. Busca el `id` para tu sesión. A continuación se muestra un extracto de ejemplo:

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NDg2MTY5MmUtNmZjZS00MjE1LWJkMDUtMzI1NGZiOWU5MDU3"
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```
    
{: start="5"}
5. Utiliza una herramienta de decodificación como [Base64 Decode and Encode](https://www.base64decode.org/) para decodificar el `id` del formato Base64 y encontrar el `campaign_id` asociado. En nuestro ejemplo, el resultado es el siguiente:

    ```
    4861692e-6fce-4215-bd05-3254fb9e9057_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    Donde `4861692e-6fce-4215-bd05-3254fb9e9057` es el `campaign_id`.<br><br>

6. Ve a la página de **Campañas** y busca el `campaign_id`.

![Busca campaign_id en la página de Campañas]({% image_buster /assets/img_archive/cc_debug.png %}){: style="max-width:80%;"}

A partir de ahí, puedes revisar la configuración y el contenido de tus mensajes para determinar por qué un usuario no puede ver una tarjeta de contenido concreta.

{% endtab %}
{% tab Email %}

1. Redacta tu mensaje de correo electrónico.
2. Selecciona **Vista previa y prueba**.
3. Selecciona la pestaña **Envío de prueba** y añade tu dirección de correo electrónico o ID de usuario en el campo **Añadir usuarios individuales**. 
4. Selecciona **Enviar prueba** para enviar el correo electrónico redactado a tu buzón de entrada.

![Prueba de correo electrónico]({% image_buster /assets/img_archive/testemail.png %}){: style="max-width:40%;" }

{% endtab %}
{% tab In-app message %}

{% alert warning %}
Para enviar una prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) o a usuarios individuales, debe estar habilitada la función push en los dispositivos de prueba antes de enviarla. Por ejemplo, debes tener habilitada la función push en tu dispositivo iOS para poder tocar la notificación antes de que aparezca el mensaje de prueba. {% endalert %}

Si tienes configuradas notificaciones push en tu aplicación y en tu dispositivo de prueba, puedes enviar mensajes de prueba dentro de la aplicación para ver cómo se ven en tiempo real. 

1. Redacta tu mensaje dentro de la aplicación.
2. Selecciona la pestaña **Prueba** y añade tu dirección de correo electrónico o ID de usuario en el campo **Añadir usuarios individuales**. 
3. Selecciona **Enviar prueba** para enviar tu mensaje push a tu dispositivo.

Aparecerá un mensaje push de prueba en la parte superior de la pantalla de tu dispositivo.

![Prueba dentro de la aplicación]({% image_buster /assets/img_archive/test-in-app.png %})

{% alert important %}
Los envíos de prueba pueden hacer que se envíe más de un mensaje dentro de la aplicación a cada destinatario. 
{% endalert %}

Al hacer clic directamente en el mensaje push y abrirlo, accederás a tu aplicación, donde podrás ver tu prueba de mensaje dentro de la aplicación. Ten en cuenta que esta función de prueba de mensajes dentro de la aplicación depende de que el usuario haga clic en una notificación push de prueba para desencadenar el mensaje dentro de la aplicación. Para que la notificación push de prueba se entregue correctamente, el usuario debe ser elegible para recibir notificaciones push en la aplicación correspondiente.

### Vista previa

Puedes previsualizar tu mensaje dentro de la aplicación mientras lo redactas en la pestaña **Vista previa**. Esto te ayudará a visualizar el mensaje final desde la perspectiva del usuario. Puedes obtener una vista previa del aspecto que tendrá tu mensaje para un usuario aleatorio, un usuario específico o un usuario personalizado. También puedes obtener una vista previa de los mensajes para dispositivos móviles o tabletas.

![La pestaña Redactar al crear un mensaje dentro de la aplicación muestra una vista previa del aspecto que tendrá el mensaje. No se selecciona un usuario, por lo que el Liquid añadido en la sección del cuerpo se muestra tal cual.]({% image_buster /assets/img/in-app-message-preview.png %})

Braze dispone de tres generaciones de mensajes dentro de la aplicación. Puedes ajustar con precisión a qué dispositivos deben enviarse tus mensajes, en función de la generación que admitan.

![Cambio entre generaciones al previsualizar un mensaje dentro de la aplicación.]({% image_buster /assets/img/iam-generations.gif %}){: height="50%" width="50%"}

{% alert warning %}
En **Vista previa**, la vista de tu mensaje puede no ser idéntica a su representación real en el dispositivo del usuario. Siempre recomendamos enviar un mensaje de prueba a un dispositivo para asegurarte de que los medios, el texto, la personalización y los atributos personalizados se generan correctamente.
{% endalert %}

### Lista de comprobación

- ¿Las imágenes y los medios se muestran y actúan como se esperaba?
- ¿Funciona Liquid como se esperaba? ¿Has previsto un [valor de atributo predeterminado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values) si Liquid no devuelve información?
- ¿Es tu texto claro, conciso y correcto?
- ¿Tus botones dirigen al usuario a donde debe ir?

### Escáner de accesibilidad

Para respaldar las mejores prácticas de accesibilidad, Braze analiza automáticamente el contenido de los mensajes dentro de la aplicación creados con el editor HTML tradicional, comparándolo con las normas de accesibilidad. Este escáner ayuda a identificar el contenido que puede no cumplir las Pautas de Accesibilidad para el Contenido Web ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)). Las WCAG son un conjunto de normas técnicas reconocidas internacionalmente y desarrolladas por el Consorcio World Wide Web (W3C) para que los contenidos web sean más accesibles a las personas con discapacidad.

![Resultados del escáner de accesibilidad]({% image_buster /assets/img/Accessibilty_Scanner_IAM.png %})

{% alert note %}
El escáner de accesibilidad de mensajes dentro de la aplicación solo funciona con mensajes creados con HTML personalizado. 
{% endalert %}

#### Cómo funciona

El escáner se ejecuta automáticamente en mensajes HTML personalizados y evalúa todo tu mensaje HTML según el [conjunto completo de reglas WCAG 2.1 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.1&currentsidebar=%23col_customize&levels=aaa). Para cada problema detectado, muestra:

- El elemento HTML específico implicado
- Una descripción del problema de accesibilidad
- Un enlace a contexto adicional u orientaciones de corrección

#### Comprender las pruebas de accesibilidad automatizadas

{% multi_lang_include accessibility/automated_testing.md %}

{% endtab %}
{% tab LINE %}

1. Crea tu mensaje LINE.
2. Selecciona la pestaña **Prueba** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba.
3. Selecciona **Enviar prueba** para enviar tu mensaje.

![Mensaje de prueba de LINE.]({% image_buster /assets/img/line/test_preview.png %})

{% endtab %}
{% tab Push %}

#### Push móvil

1. Redacta tu push móvil.
2. Selecciona la pestaña **Prueba** y añade tu dirección de correo electrónico o ID de usuario en el campo **Añadir usuarios individuales**.
3. Selecciona **Enviar prueba** para enviar tu mensaje redactado a tu dispositivo.

![Prueba push]({% image_buster /assets/img_archive/testpush.png %})

#### Notificación push web

1. Crea tu notificación push web.
2. Selecciona la pestaña **Prueba**. 
3. Selecciona **Enviar prueba a mí mismo**.
4. Selecciona **Enviar prueba** para enviar tu notificación push web a tu navegador web.

![Prueba push web]({% image_buster /assets/img_archive/testwebpush.png %})

Si ya has aceptado mensajes push desde el dashboard de Braze, el push aparecerá en la esquina de tu pantalla. De lo contrario, haz clic en **Permitir** cuando se te solicite y aparecerá el mensaje.

{% endtab %}
{% tab SMS/MMS and RCS %}

Después de crear tu mensaje SMS, MMS o RCS, puedes enviar un mensaje de prueba a tu teléfono para ver qué aspecto tendrá en tiempo real. 

1. Redacta tu mensaje SMS, MMS o RCS.
2. Selecciona la pestaña **Prueba** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba. 
3. Selecciona **Enviar prueba** para enviar tu mensaje de prueba.

![Tarjeta de contenido de prueba]({% image_buster /assets/img/sms_test.png %})

{% endtab %}
{% tab Webhook %}

Después de crear tu webhook, puedes hacer un envío de prueba para comprobar la respuesta del webhook. Selecciona la pestaña **Prueba** y selecciona **Enviar prueba** para enviar un envío de prueba a la URL de webhook suministrada. También puedes seleccionar un usuario individual para previsualizar la respuesta como un usuario específico. 

![Tarjeta de contenido de prueba]({% image_buster /assets/img/webhook_test.png %})

{% endtab %}
{% tab WhatsApp %}

1. Crea tu mensaje de WhatsApp.
2. Selecciona la pestaña **Prueba** y selecciona al menos un grupo de prueba de contenido o un usuario individual para recibir este mensaje de prueba.
3. Inicia una ventana de conversación enviando un mensaje de WhatsApp al número de teléfono asociado al grupo de suscripción que estás utilizando para este mensaje. El número de teléfono asociado aparece en la alerta de la pestaña **Prueba**.
4. Selecciona **Enviar prueba** para enviar tu mensaje.

![Prueba el mensaje de WhatsApp.]({% image_buster /assets/img/whatsapp/whatsapp_test.png %})

{% endtab %}
{% endtabs %}

## Probar campañas personalizadas 

Si estás probando campañas que rellenan datos de usuario o utilizan propiedades de eventos personalizados, tendrás que tomar medidas adicionales o diferentes.

### Probar campañas personalizadas con atributos de usuario

Si utilizas [personalización]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/overview/) en tu mensaje, tendrás que tomar medidas adicionales para previsualizar adecuadamente tu campaña y comprobar que los datos de usuario rellenan correctamente el contenido.

Cuando envíes un mensaje de prueba, asegúrate de elegir la opción **Seleccionar usuario existente** o vista previa como **usuario personalizado**.

![Probar un mensaje personalizado]({% image_buster /assets/img_archive/personalized_testing.png %}){: style="max-width:70%;" }

#### Seleccionar un usuario existente

Si seleccionas un usuario existente, introduce el ID de usuario específico o el correo electrónico en el campo de búsqueda. A continuación, utiliza la vista previa del dashboard para ver qué aspecto tendría tu mensaje para ese usuario y envía un mensaje de prueba a tu dispositivo que refleje lo que vería ese usuario.

![Seleccionar un usuario]({% image_buster /assets/img_archive/personalized_testing_select.png %})

#### Seleccionar un usuario personalizado

Si realizas una vista previa como usuario personalizado, introduce texto para los distintos campos disponibles para la personalización, como el nombre del usuario y cualquier atributo personalizado. Una vez más, puedes ingresar tu propia dirección de correo electrónico para enviar una prueba a tu dispositivo.

![Usuario personalizado]({% image_buster /assets/img_archive/personalized_testing_custom.png %})

#### Personalizar un usuario existente

Puedes editar campos individuales de un usuario aleatorio o existente para ayudar a probar el contenido dinámico dentro de tu mensaje. Selecciona **Editar** para convertir el usuario seleccionado en un usuario personalizado que puedas modificar.

![La pestaña "Vista previa como usuario" con un botón "Editar".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Probar campañas personalizadas con propiedades de eventos personalizados

Probar campañas personalizadas con [propiedades de eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) difiere ligeramente de probar otros tipos de campañas descritas. 

{% tabs local %}
{% tab Trigger manually %}

#### Método 1: Desencadenar la campaña manualmente

Puedes desencadenar tú mismo la campaña como una forma sólida de probar campañas personalizadas utilizando propiedades de eventos personalizados:

1. Escribe el texto que incluye la propiedad del evento. 

![Composición de mensajes de prueba con propiedades]({% image_buster /assets/img_archive/testeventproperties-compose.png %})

{: start="2"}
2. Utiliza la [entrega basada en acciones]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) para entregar la campaña cuando se produzca el evento.

{% alert note %}
Si estás probando una campaña push de iOS, debes establecer el retraso en un minuto para que te dé tiempo a salir de la aplicación, ya que iOS no entrega notificaciones push para la aplicación abierta en ese momento. Otros tipos de campañas pueden configurarse para entrega inmediata.
{% endalert %}

![Entrega de mensajes de prueba]({% image_buster /assets/img_archive/testeventproperties-delivery.png %})

{: start="3"}
3. Segmenta a los usuarios como lo harías para las pruebas utilizando un filtro de pruebas o seleccionando tu propia dirección de correo electrónico y termina de crear la campaña. 

![Segmentación de mensajes de prueba]({% image_buster /assets/img_archive/testeventproperties-target.png %})

{: start="4"}
4. Entra en tu aplicación y completa el evento personalizado.

La campaña se desencadenará y mostrará el mensaje personalizado con la propiedad del evento.

![Ejemplo de mensaje de prueba]({% image_buster /assets/img_archive/testeventproperties-message2.png %})

{% endtab %}
{% tab Test message %}

#### Método 2: Enviarte un mensaje de prueba

Alternativamente, si guardas ID de usuario personalizados, también puedes probar la campaña enviándote un mensaje de prueba personalizado a ti mismo.

1. Escribe el texto de tu campaña.
2. Selecciona la pestaña **Prueba** y elige **Usuario personalizado**. 
3. Añade la propiedad del evento personalizado en la parte inferior de la página, y añade tu ID de usuario o dirección de correo electrónico en la casilla superior.
4. Selecciona **Enviar prueba** para recibir un mensaje personalizado con la propiedad.

![Pruebas con el usuario personalizado]({% image_buster /assets/img_archive/testeventproperties-customuser.png %})

{% endtab %}
{% tab Liquid %}

#### Método 3: Utilizar Liquid

Puedes probar las propiedades de eventos personalizados introduciendo manualmente los valores con Liquid. 

1. En el editor de mensajes, introduce valores para tus propiedades de eventos personalizados.
2. Selecciona la pestaña **Vista previa como usuario** para comprobar que se muestra el mensaje correcto.

{% endtab %}
{% endtabs %}

## Solución de problemas

### Mensajes dentro de la aplicación

Si tu campaña de mensajes dentro de la aplicación no se desencadena con una campaña push, comprueba la segmentación de la campaña dentro de la aplicación para confirmar que el usuario cumple con la audiencia objetivo **antes de** recibir el mensaje push.

En los envíos de prueba en Android e iOS, es posible que los mensajes dentro de la aplicación que utilizan el comportamiento **Solicitar permiso push** al hacer clic no se muestren en algunos dispositivos. Como solución:
- **Android:** Los dispositivos deben tener Android 13 y el SDK de Braze para Android versión 21.0.0. Otra razón puede ser que el dispositivo en el que se muestra el mensaje dentro de la aplicación ya tenga un aviso a nivel de sistema. Es posible que hayas seleccionado **No volver a preguntar**, por lo que puede que tengas que reinstalar la aplicación para restablecer los permisos de notificación antes de volver a probar.
- **iOS:** Recomendamos a tu equipo de desarrolladores que revise la implementación de las notificaciones push para tu aplicación y elimine manualmente cualquier código que solicite permisos push. Para más información, consulta [Mensajes push primer dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/).

Para entregar una campaña de mensajes dentro de la aplicación basada en acciones, debes registrar eventos personalizados a través del SDK de Braze, no de las API REST, para que los usuarios puedan recibir mensajes elegibles dentro de la aplicación directamente en su dispositivo. Los usuarios reciben el mensaje dentro de la aplicación si realizan el evento durante la sesión.