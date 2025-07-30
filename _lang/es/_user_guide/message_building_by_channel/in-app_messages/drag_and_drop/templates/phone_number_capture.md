---
nav_title: "Formulario de registro de SMS, RCS y WhatsApp"
article_title: "Formulario de registro de SMS, RCS y WhatsApp"
alias: "/phone_number_capture/"
page_order: 1
description: "Esta página explica cómo crear un formulario de registro de SMS, RCS y WhatsApp con el editor de arrastrar y soltar mensajes dentro de la aplicación."
---

# Formulario de registro de SMS, RCS y WhatsApp

> Los formularios de registro de SMS, RCS y WhatsApp son plantillas disponibles en el editor de arrastrar y soltar para mensajes dentro de la aplicación. Utiliza estas plantillas para recopilar los números de teléfono de los usuarios y hacer crecer tus grupos de suscripción a SMS, MMS, RCS y WhatsApp.

![Tres ejemplos de mensajes dentro de la aplicación creados utilizando la plantilla del formulario de registro telefónico.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='Requisitos SDK' %}

## Crear un formulario de registro de número de teléfono

### Paso 1: Elige tu plantilla

Cuando crees un mensaje dentro de la aplicación arrastrando y soltando, selecciona Registro **de SMS** (esto se adapta al registro de RCS) o **Registro de WhatsApp** para tu plantilla y, a continuación, selecciona **Crear mensaje**. Estas plantillas son compatibles tanto con aplicaciones móviles como con navegadores web.

![Modal para seleccionar el registro de SMS o el registro de WhatsApp como plantilla al crear un mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### Paso 2: Configura tus estilos de mensaje

{% multi_lang_include drag_and_drop/templates.md section='estilo del mensaje' %}

![Flujo de trabajo de carga y selección de una fuente personalizada.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### Paso 3: Personaliza el componente de entrada del número de teléfono

Para empezar a crear su formulario de inscripción, seleccione el componente de entrada de número de teléfono en el editor.

![Área de vista previa al crear un formulario de registro con el componente de entrada de número de teléfono seleccionado.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

En el menú lateral, especifique para qué grupo de suscripción recopilará números de teléfono esta plantilla. Para adherirse a las mejores prácticas de cumplimiento, sólo puede recopilar el consentimiento para un grupo de suscripción por formulario de registro de número de teléfono. No obstante, si lo desea, puede utilizar varios formularios para recabar el consentimiento de otros grupos de suscripción.

![Desplegable de grupo de suscripción con un grupo de suscripción seleccionado.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

Por defecto, recopilamos números de todo el mundo, pero puede limitar el número de países de los que recopilamos números. Esto es útil si sólo quieres enviar mensajes a usuarios que tengan números de teléfono en determinados países, y puede ayudarte con la limpieza de la lista. Para ello, desactive **Recoger números de todos los países** y utilice el menú desplegable para seleccionar países concretos. Sus usuarios sólo podrán seleccionar los países que usted haya añadido explícitamente.

![Desplegable de países para seleccionar los países de los que quieres recoger números.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Números de teléfono no válidos

Si sus usuarios introducen un número de teléfono que incluye caracteres especiales no aceptados, verán un indicador de error genérico no personalizable y no podrán enviar el formulario. Puede ver el comportamiento del error en la pestaña **Vista previa y prueba** y en su dispositivo de prueba. Consulte este artículo para saber [cómo formatea Braze los números de teléfono]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers).

### Paso 4: Añade una cláusula de exención de responsabilidad (para los formularios de registro de SMS y RCS)

Para los formularios de registro de SMS y RCS, es importante comunicar claramente el tipo de SMS o RCS que vas a enviar. Asegúrate de que el crecimiento de tu lista cumple la normativa incluyendo la siguiente información en tu formulario:

- Descripción de los tipos de mensajes SMS y RCS que pueden esperar tus clientes (recordatorios de carrito, promociones y ofertas, recordatorios de citas, etc.). No es necesario que enumere todos los casos de uso, pero debe proporcionar una descripción de los tipos de mensajes que enviará su marca.
- Tenga en cuenta que el consentimiento no es condición para ninguna compra (si procede).
- Frecuencia de los mensajes y recordatorio de que se aplican tarifas de mensajes y datos. Si no conoce la frecuencia exacta del mensaje, puede decir que la frecuencia puede variar.
- Enlaces a tus Condiciones generales y a la Política de privacidad de SMS y RCS.
- Recordatorio de las palabras clave de ayuda y cancelación (HELP para ayuda; STOP para cancelar).

Hemos incluido una cláusula de exención de responsabilidad en la plantilla únicamente a modo de ejemplo; no constituye asesoramiento jurídico y no debe utilizarse a efectos de cumplimiento. Es importante trabajar con su equipo jurídico para desarrollar un lenguaje adaptado a su marca específica.

{% alert note %}
Esta documentación no pretende proporcionar asesoramiento jurídico completo, ni debe considerarse como tal.
{% endalert %}

Para más información sobre el cumplimiento de SMS y RCS, consulta [Leyes y normativas sobre SMS, MMS y RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

### Paso 5: Estiliza tu mensaje

Personaliza el aspecto de tu mensaje utilizando los [componentes de arrastrar y soltar de los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components).

## Analizar los resultados

{% multi_lang_include drag_and_drop/templates.md section='informes' %}

![Panel de rendimiento del mensaje dentro de la aplicación que muestra los clics de cada enlace del mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})


