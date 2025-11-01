{% if include.section == "SDK requirements" %}

## Requisitos previos

### Versiones mínimas del SDK

Los mensajes creados con el editor de arrastrar y soltar sólo pueden enviarse a usuarios de las siguientes versiones mínimas del SDK. Para más información, consulta [Crear un mensaje dentro de la aplicación con arrastrar y soltar: Requisitos previos]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites).

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### Versiones del SDK para enlaces de texto

Para incluir enlaces de texto que no descarten el mensaje, se requieren las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
Si incluyes un enlace en tu mensaje dentro de la aplicación que redirija a una URL y el usuario no está en las versiones mínimas de SDK especificadas, al hacer clic en el enlace se cerrará el mensaje y el usuario no podrá volver al mensaje para enviar el formulario.
{% endalert %}

{% endif %}

{% if include.section == "message style" %}

Antes de empezar a personalizar tu plantilla, puedes establecer estilos a nivel de mensaje para todo el mensaje utilizando el menú lateral. Por ejemplo, puede que desee personalizar el tipo de letra de todo el texto o el color de todos los enlaces incluidos en su mensaje. También puede hacer que el mensaje sea de tipo modal o de pantalla completa.

{% endif %}


<!-- Add this below after the disclaimers are added to all email sign-up templates: "We have provided a placeholder disclaimer in the template solely as an example, but this should not be relied upon for compliance purposes."-->

{% if include.section == "email disclaimer" %}

Le recomendamos que incluya en su mensaje un texto de aceptación y enlaces a la política de privacidad y los términos y condiciones de su marca. Asegúrese de trabajar con su equipo jurídico para desarrollar un lenguaje adaptado a su marca específica.

{% alert note %}
Las mejores prácticas de entrega a menudo superan los requisitos legales, y nuestra recomendación es obtener siempre el consentimiento explícito para enviar correos electrónicos y permitir a los usuarios rechazarlos fácilmente.
{% endalert %}

{% endif %}

{% if include.section == "email validation" %}

Si el usuario introduce una dirección de correo electrónico que incluye caracteres especiales no aceptados, verá un indicador de error genérico y no podrá enviar el formulario. Este mensaje de error no es personalizable. Puede ver el comportamiento del error en la pestaña **Vista previa y prueba** y en su dispositivo de prueba. Más información sobre cómo Braze da formato a las direcciones de correo electrónico en [Validación de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

{% endif %}

{% if include.section == "email double opt-in" %}

### Doble verificación de adhesión voluntaria

Para asegurarte de que todos los que se inscribieron en tu lista querían inscribirse en ella y proporcionaron la dirección de correo electrónico correcta, te recomendamos obtener una segunda confirmación de todos los que se inscribieron a través de tu formulario de inscripción por correo electrónico mediante el envío de un flujo de [doble adhesión voluntaria](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in).

Una de las formas de configurarlo es a través de Canvas:

1. Cree un Canvas basado en acciones y configúrelo para que se active cuando un usuario añada una dirección de correo electrónico a Braze. Asegúrese de que permite dirigirse a usuarios que son nuevos en la plataforma (por ejemplo, utilizando un segmento sin filtros en el Canvas).
2. Crea un paso de mensaje por correo electrónico con una CTA que tenga un hipervínculo a la etiqueta de Liquid {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %}. Esto cambiará el estado de suscripción de correo electrónico del usuario a `opted_in` cuando haga clic en el botón.
3. Añade un [paso de Ruta de acción]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths).
4. Para la primera ruta, active un correo electrónico cuando un usuario cambie su estado de suscripción de correo electrónico a `opted_in`. Este correo electrónico debe informar a los usuarios de que su correo electrónico ha sido confirmado.
5. Configure la otra ruta para salir del Canvas después de que expire la ventana.

{% endif %}

{% if include.section == "reporting" %}

Una vez lanzada tu campaña, puedes analizar los resultados en tiempo real para ver cuántos usuarios han interactuado con ella. Para ver cuántos usuarios han optado por el grupo de suscripción, puede [crear un segmento]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/) de usuarios suscritos al grupo de suscripción filtrando por usuarios que hayan recibido el mensaje in-app y enviado el formulario.

{% endif %}