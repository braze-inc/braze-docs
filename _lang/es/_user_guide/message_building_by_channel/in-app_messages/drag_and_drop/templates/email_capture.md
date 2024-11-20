---
nav_title: Formulario de inscripción por correo electrónico
article_title: Formulario de inscripción por correo electrónico
alias: "/email_capture/"
description: "Esta página de referencia explica cómo crear un formulario de suscripción por correo electrónico con el editor de mensajes de arrastrar y soltar de la aplicación."
---

# Formulario de inscripción por correo electrónico

> Utiliza la plantilla de mensajes in-app de registro por correo electrónico de arrastrar y soltar para recopilar las direcciones de correo electrónico de los usuarios y hacer crecer tus grupos de suscripción.

## Requisitos del SDK

### Versiones mínimas del SDK

Los mensajes creados con el editor de arrastrar y soltar sólo pueden enviarse a usuarios de las siguientes versiones mínimas del SDK. Consulte la sección [Requisitos previos][1] del artículo [Crear un mensaje in-app con arrastrar y soltar]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) para obtener más detalles y matices a tener en cuenta.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### Versiones del SDK para enlaces de texto

Si desea incluir enlaces de texto que no descarten el mensaje, los usuarios deben estar en las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
Si incluyes un enlace en tu mensaje dentro de la aplicación que redirija a una URL y el usuario no está en las versiones mínimas de SDK especificadas, al hacer clic en el enlace se cerrará el mensaje y el usuario no podrá volver al mensaje para enviar el formulario.
{% endalert %}

## Crear un formulario de inscripción por correo electrónico

Cuando crees un mensaje dentro de la aplicación arrastrando y soltando, selecciona **Registro por correo electrónico** para tu plantilla y selecciona **Crear mensaje**. Esta plantilla es compatible tanto con aplicaciones móviles como con navegadores web.

### Paso 1: Configura tus estilos de mensaje

Antes de empezar a personalizar tu plantilla, puedes establecer estilos a nivel de mensaje para todo el mensaje utilizando el menú lateral. Por ejemplo, puede que desee personalizar el tipo de letra de todo el texto o el color de todos los enlaces incluidos en su mensaje. También puede hacer que el mensaje sea de tipo modal o de pantalla completa.

### Paso 2: Personalice su componente de inscripción por correo electrónico

Para empezar a crear su formulario de suscripción por correo electrónico, seleccione el elemento de captura de correo electrónico en el editor. Por defecto, las direcciones de correo electrónico recopiladas tendrán el grupo de suscripción global **Suscrito**. Para incluir usuarios en grupos de suscripción específicos, consulte [Actualización de los estados de suscripción de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Puede personalizar el texto del marcador de posición y el texto de la etiqueta del elemento de captura de correo electrónico.

#### Validación del correo electrónico

Si el usuario introduce una dirección de correo electrónico que incluye caracteres especiales no aceptados, verá un indicador de error genérico y no podrá enviar el formulario. Este mensaje de error no es personalizable. Puede ver el comportamiento del error en la pestaña **Vista previa y prueba** y en su dispositivo de prueba. Más información sobre cómo Braze da formato a las direcciones de correo electrónico en [Validación de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

### Paso 3: Añadir cláusula de exención de responsabilidad (opcional)

Le recomendamos que incluya en su mensaje un texto de aceptación y enlaces a la política de privacidad y los términos y condiciones de su marca. Hemos incluido una cláusula de exención de responsabilidad en la plantilla a modo de ejemplo, pero no debe utilizarse a efectos de cumplimiento. Asegúrese de trabajar con su equipo jurídico para desarrollar un lenguaje adaptado a su marca específica.

{% alert note %}
Las mejores prácticas de entrega a menudo superan los requisitos legales, y nuestra recomendación es obtener siempre el consentimiento explícito para enviar correos electrónicos y permitir a los usuarios rechazarlos fácilmente.
{% endalert %}

### Paso 4: Estiliza tu mensaje

Puedes personalizar el aspecto de tu mensaje arrastrando y soltando [los componentes del mensaje dentro de la aplicación][3].

## Informe

Una vez lanzada tu campaña, puedes analizar los resultados en tiempo real para ver cuántos usuarios han interactuado con ella. Para ver cuántos usuarios han optado por el grupo de suscripción, puede [crear un segmento][5] de usuarios suscritos al grupo de suscripción filtrando por usuarios que hayan recibido el mensaje in-app y enviado el formulario.

## Buenas prácticas

### Doble verificación de adhesión voluntaria

Para asegurarte de que todos los que se inscribieron en tu lista querían inscribirse en ella y proporcionaron la dirección de correo electrónico correcta, te recomendamos obtener una segunda confirmación de todos los que se inscribieron a través de tu formulario de inscripción por correo electrónico mediante el envío de un flujo de [doble adhesión voluntaria](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in).

Una de las formas de configurar esto es a través de Canvas Flow:

1. Cree un Canvas basado en acciones y configúrelo para que se active cuando un usuario añada una dirección de correo electrónico a Braze. Asegúrese de que permite dirigirse a usuarios que son nuevos en la plataforma (por ejemplo, utilizando un segmento sin filtros en el Canvas).
2. Crea un paso de mensaje por correo electrónico con una CTA que tenga un hipervínculo a la etiqueta de Liquid {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}. Esto cambiará el estado de suscripción de correo electrónico del usuario a `opted_in` cuando haga clic en el botón.
3. Añade un [paso de Ruta de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths).
4. Para la primera ruta, active un correo electrónico cuando un usuario cambie su estado de suscripción de correo electrónico a `opted_in`. Este correo electrónico debe informar a los usuarios de que su correo electrónico ha sido confirmado.
5. Configure la otra ruta para salir del Canvas después de que expire la ventana.

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/
