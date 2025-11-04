---
nav_title: Formulario de registro por correo electrónico
article_title: Formulario de registro por correo electrónico
alias: "/email_capture/"
page_order: 2
description: "Esta página explica cómo crear un formulario de registro por correo electrónico con el editor de arrastrar y soltar mensajes dentro de la aplicación."
---

# Formulario de registro por correo electrónico

> Utiliza la plantilla de mensajes dentro de la aplicación para registrarte por correo electrónico arrastrando y soltando para recopilar las direcciones de correo electrónico de los usuarios y hacer crecer tus grupos de suscripción.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Crear un formulario de registro por correo electrónico

### Paso 1: Elige tu plantilla

Cuando crees un mensaje dentro de la aplicación arrastrando y soltando, selecciona **Registro por correo electrónico** para tu plantilla y, a continuación, selecciona **Crear mensaje**. Esta plantilla es compatible tanto con aplicaciones móviles como con navegadores web.

El editor de mensajes dentro de la aplicación con la plantilla para un formulario de captura de correo electrónico.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_template1.png %})

### Paso 2: Configura los estilos de tus mensajes

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Paso 3: Personaliza tu componente de registro por correo electrónico

Para empezar a crear tu formulario de registro por correo electrónico, selecciona el elemento de captura de correo electrónico en el editor. Por defecto, las direcciones de correo electrónico recopiladas tendrán el grupo de suscripción global **Suscrito**. Para incluir usuarios en grupos de suscripción específicos, consulta [Actualizar los estados de suscripción por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Puedes personalizar el texto del marcador de posición y el texto de la etiqueta del elemento de captura de correo electrónico.

El editor de mensajes dentro de la aplicación con un menú lateral para personalizar el elemento de captura de correo electrónico.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field1.png %})

#### Validación del correo electrónico

Si el usuario introduce una dirección de correo electrónico que incluye caracteres especiales no aceptados, verá un indicador de error genérico y no podrá enviar el formulario. Este mensaje de error no es personalizable. Puedes ver el comportamiento del error en la pestaña de **prueba de la vista previa & ** y en tu dispositivo de prueba. Más información sobre cómo Braze da formato a las direcciones de correo electrónico en [Validación de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/).

### Paso 4: Añade una cláusula de exención de responsabilidad (opcional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Paso 5: Estiliza tu mensaje

Personaliza el aspecto de tu formulario de registro utilizando [los componentes de]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) arrastrar y soltar [de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components).

## Analizar los resultados

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Buenas prácticas

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}

