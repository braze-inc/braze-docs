---
nav_title: Formulario de inscripción SMS y WhatsApp
article_title: Formulario de inscripción SMS y WhatsApp
alias: "/phone_number_capture/"
description: "Esta página de referencia explica cómo crear un formulario de registro de SMS y WhatsApp con el editor de arrastrar y soltar mensajes de la aplicación."
---

# Formulario de inscripción SMS y WhatsApp

> Los formularios de registro de SMS y WhatsApp son plantillas disponibles en el editor de arrastrar y soltar para mensajes in-app. Utilice estas plantillas para recopilar los números de teléfono de los usuarios y hacer crecer sus grupos de suscripción a SMS y WhatsApp.

![Tres ejemplos de mensajes in-app creados con la plantilla de formulario de registro telefónico.][img7]

## Requisitos del SDK

### Versiones mínimas del SDK

Los mensajes creados con el editor de arrastrar y soltar sólo pueden enviarse a usuarios de las siguientes versiones mínimas del SDK. Consulte la sección [Requisitos previos][1] de [Creación de un mensaje in-app con arrastrar y soltar]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/) para obtener más detalles y matices a tener en cuenta.

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### Versiones del SDK para enlaces de texto

Si desea incluir enlaces de texto que no descarten el mensaje, los usuarios deben estar en las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
Si incluyes un enlace en tu mensaje in-app que redirige a una URL y el usuario final no está en las versiones SDK mínimas especificadas, al hacer clic en el enlace se cerrará el mensaje y el usuario no podrá volver al mensaje para enviar el formulario.
{% endalert %}

## Crear un formulario de registro de número de teléfono

Cuando crees un mensaje dentro de la aplicación de arrastrar y soltar, selecciona **Registro SMS** o **Registro WhatsApp** para tu plantilla.

![Modal para seleccionar el registro de SMS o el registro de WhatsApp como plantilla al crear un mensaje dentro de la aplicación.][img2]{: style="max-width:70%"}

Estas plantillas son compatibles tanto con aplicaciones móviles como con navegadores web.

### Paso 1: Configura tus estilos de mensaje

Antes de empezar a personalizar tu plantilla, puedes establecer estilos a nivel de mensaje para todo el mensaje utilizando el menú lateral. Por ejemplo, puede que desee personalizar el tipo de letra de todo el texto o el color de todos los enlaces incluidos en su mensaje. También puede hacer que el mensaje sea de tipo modal o de pantalla completa.

![Flujo de trabajo de carga y selección de una fuente personalizada.][img6]

### Paso 2: Personaliza el componente de entrada del número de teléfono

Para empezar a crear su formulario de inscripción, seleccione el componente de entrada de número de teléfono en el editor.

![Área de vista previa al crear un formulario de registro con el componente de entrada de número de teléfono seleccionado.][img3]{: style="max-width:40%"}

En el menú lateral, especifique para qué grupo de suscripción recopilará números de teléfono esta plantilla. Para adherirse a las mejores prácticas de cumplimiento, sólo puede recopilar el consentimiento para un grupo de suscripción por formulario de registro de número de teléfono. No obstante, si lo desea, puede utilizar varios formularios para recabar el consentimiento de otros grupos de suscripción.

![Desplegable de grupo de suscripción con un grupo de suscripción seleccionado.][img4]{: style="max-width:40%"}

Por defecto, recopilamos números de todo el mundo, pero puede limitar el número de países de los que recopilamos números. Esto es útil si sólo quieres enviar mensajes a usuarios que tengan números de teléfono en determinados países, y puede ayudarte con la limpieza de la lista. Para ello, desactive **Recoger números de todos los países** y utilice el menú desplegable para seleccionar países concretos. Sus usuarios sólo podrán seleccionar los países que usted haya añadido explícitamente.

![Desplegable de países para seleccionar los países de los que quieres recoger números.][img5]{: style="max-width:40%"}

#### Números de teléfono no válidos

Si sus usuarios introducen un número de teléfono que incluye caracteres especiales no aceptados, verán un indicador de error genérico no personalizable y no podrán enviar el formulario. Puede ver el comportamiento del error en la pestaña **Vista previa y prueba** y en su dispositivo de prueba. Consulte este artículo para saber [cómo formatea Braze los números de teléfono][2].

### Paso 3: Añadir una cláusula de exención de responsabilidad (para formularios de inscripción por SMS)

Para los formularios de inscripción por SMS, es importante comunicar claramente el tipo de SMS que se va a enviar. Asegúrate de que el crecimiento de tu lista cumple la normativa incluyendo la siguiente información en tu formulario:

- Descripción de los tipos de mensajes SMS que pueden esperar sus clientes (recordatorios de carritos, promociones y ofertas, recordatorios de citas, etc.). No es necesario que enumere todos los casos de uso, pero debe proporcionar una descripción de los tipos de mensajes que enviará su marca.
- Tenga en cuenta que el consentimiento no es condición para ninguna compra (si procede).
- Frecuencia de los mensajes y recordatorio de que se aplican tarifas de mensajes y datos. Si no conoce la frecuencia exacta del mensaje, puede decir que la frecuencia puede variar.
- Enlaces a sus Condiciones generales y a la Política de privacidad de SMS.
- Recordatorio de las palabras clave de ayuda y cancelación (HELP para ayuda; STOP para cancelar).

Hemos incluido una cláusula de exención de responsabilidad en la plantilla únicamente a modo de ejemplo; no constituye asesoramiento jurídico y no debe utilizarse a efectos de cumplimiento. Es importante trabajar con su equipo jurídico para desarrollar un lenguaje adaptado a su marca específica.

{% alert note %}
Esta documentación no pretende proporcionar asesoramiento jurídico completo, ni debe considerarse como tal.
{% endalert %}

Para obtener más información sobre el cumplimiento de los SMS, consulte [Leyes y normativas sobre SMS][4].

### Paso 4: Estiliza tu mensaje

Puedes personalizar el aspecto de tu mensaje arrastrando y soltando [los componentes del mensaje dentro de la aplicación][3].

## Informe

Una vez lanzada la campaña, puede analizar los resultados en tiempo real para ver cuántos usuarios han interactuado con ella. Para ver cuántos usuarios han optado por el grupo de suscripción, puede [crear un segmento][5] de usuarios suscritos al grupo de suscripción filtrando por los usuarios que han recibido el mensaje in-app y enviado el formulario.

![Panel de rendimiento de los mensajes dentro de la aplicación que muestra los clics de cada enlace del mensaje dentro de la aplicación.][img8]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#prerequisites
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#drag-and-drop-in-app-message-components
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/
[5]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/

[img1]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example.png %}
[img2]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}
[img3]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}
[img4]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}
[img5]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}
[img6]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %}
[img7]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %}
[img8]: {% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %}
