---
nav_title: "Formulario de registro de SMS, RCS y WhatsApp"
article_title: "Formulario de registro de SMS, RCS y WhatsApp"
alias: "/phone_number_capture/"
page_order: 1
description: "Esta página explica cómo crear un formulario de registro de SMS, RCS y WhatsApp con el editor de arrastrar y soltar mensajes dentro de la aplicación."
---

# Formulario de registro de SMS, RCS y WhatsApp

> Los formularios de registro de SMS, RCS y WhatsApp son plantillas disponibles en el editor de arrastrar y soltar para mensajes dentro de la aplicación. Utiliza estas plantillas para recopilar los números de teléfono de los usuarios y hacer crecer tus grupos de suscripción a SMS, MMS, RCS y WhatsApp.

Tres ejemplos de mensajes dentro de la aplicación creados con la plantilla del formulario de registro del teléfono.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_example2.png %})

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Crear un formulario de registro de número de teléfono

### Paso 1: Elige tu plantilla

Cuando crees un mensaje dentro de la aplicación arrastrando y soltando, selecciona Registro **de SMS** (esto se adapta al registro de RCS) o **Registro de WhatsApp** para tu plantilla y, a continuación, selecciona **Crear mensaje**. Estas plantillas son compatibles tanto con aplicaciones móviles como con navegadores web.

Modal para seleccionar el registro en SMS o WhatsApp como plantilla al crear un mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_template.png %}){: style="max-width:80%"}

### Paso 2: Configura los estilos de tus mensajes

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

Flujo de trabajo de carga y selección de una fuente personalizada.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_custom_font.gif %})

### Paso 3: Personaliza el componente de introducción del número de teléfono

Para empezar a crear tu formulario de registro, selecciona el componente de entrada de número de teléfono en el editor.

\![Área de vista previa al crear un formulario de registro con el componente de entrada de número de teléfono seleccionado.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%"}

En el menú lateral, especifica para qué grupo de suscripción recogerá números de teléfono esta plantilla. Para adherirte a las mejores prácticas de cumplimiento, sólo puedes recoger el consentimiento de un grupo de suscripción por formulario de registro de número de teléfono. Sin embargo, si lo deseas, puedes utilizar varios formularios para recoger el consentimiento de otros grupos de suscripción.

Desplegable de grupo de suscripción con un grupo de suscripción seleccionado.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_subscription.png %}){: style="max-width:40%"}

Por predeterminado, recopilamos números globalmente, pero puedes limitar el número de países de los que recopilamos números. Esto es útil si pretendes enviar mensajes sólo a usuarios que tengan números de teléfono en países específicos, y puede ayudarte con la limpieza de la lista. Para ello, desactiva **Recoger números de todos los países** y utiliza el desplegable para seleccionar países concretos. Tus usuarios sólo podrán seleccionar los países que hayas añadido explícitamente.

\![Desplegable Países para seleccionar los países de los que quieres recopilar números.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_countries.png %}){: style="max-width:40%"}

#### Números de teléfono no válidos

Si tus usuarios introducen un número de teléfono que incluya caracteres especiales no aceptados, verán un indicador de error genérico no personalizable y no podrán enviar el formulario. Puedes ver el comportamiento del error en la pestaña de **prueba de la vista previa & ** y en tu dispositivo de prueba. Consulta este artículo para saber [cómo formatea Braze los números de teléfono]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers).

### Paso 4: Añade una cláusula de exención de responsabilidad (para los formularios de registro de SMS y RCS)

Para los formularios de registro de SMS y RCS, es importante comunicar claramente el tipo de SMS o RCS que vas a enviar. Asegúrate de que el crecimiento de tu lista cumple la normativa incluyendo la siguiente información en tu formulario:

- Descripción de los tipos de mensajes SMS y RCS que pueden esperar tus clientes (recordatorios de carrito, promociones y ofertas, recordatorios de citas, etc.). No es necesario que enumere todos los casos de uso, pero debe proporcionar una descripción de los tipos de mensajes que enviará su marca.
- Ten en cuenta que el consentimiento no es una condición para ninguna compra (si procede).
- Frecuencia de los mensajes y recordatorio de que se aplican las tasas de mensajes y datos. Si no conoces la frecuencia exacta de los mensajes, puedes decir que la frecuencia puede variar.
- Enlaces a tus Condiciones & Condiciones y Política de Privacidad de SMS y RCS.
- Recordatorio de las palabras clave de ayuda y exclusión voluntaria (HELP para ayuda; STOP para cancelar).

Hemos incluido un marcador de posición de exención de responsabilidad en la plantilla únicamente a modo de ejemplo: no constituye asesoramiento jurídico y no debe utilizarse a efectos de cumplimiento. Es importante trabajar con tu equipo jurídico para desarrollar un lenguaje adaptado a tu marca específica.

{% alert note %}
Esta documentación no pretende proporcionar asesoramiento jurídico, ni puede considerarse como tal.
{% endalert %}

Para más información sobre el cumplimiento de SMS y RCS, consulta [Leyes y normativas sobre SMS, MMS y RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

### Paso 5: Estiliza tu mensaje

Personaliza el aspecto de tu mensaje utilizando [los componentes de]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) arrastrar y soltar [de los mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components).

## Analizar los resultados

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

\![Panel de rendimiento de los mensajes dentro de la aplicación que muestra los clics de cada enlace del mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_analytics.png %})


