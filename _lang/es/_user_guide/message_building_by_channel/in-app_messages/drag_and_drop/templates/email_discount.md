---
nav_title: Inscripción por correo electrónico con descuento
article_title: Registro por correo electrónico con descuento
alias: "/email_discount/"
page_order: 3
description: "Esta página de referencia explica cómo utilizar el editor de arrastrar y soltar mensajes dentro de la aplicación para crear un formulario de registro por correo electrónico que ofrezca un descuento a los nuevos suscriptores."
---

# Inscripción por correo electrónico con descuento

> Utiliza el editor de arrastrar y soltar mensajes dentro de la aplicación para crear un formulario de registro por correo electrónico que ofrezca un descuento a los nuevos suscriptores.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Crear un formulario de registro por correo electrónico con un descuento

### Paso 1: Elige tu plantilla

Cuando crees un mensaje dentro de la aplicación arrastrando y soltando, selecciona **Registro por correo electrónico con descuento de bienvenida** para tu plantilla y, a continuación, selecciona **Crear mensaje**. Esta plantilla es compatible tanto con aplicaciones móviles como con navegadores web.

El editor de mensajes dentro de la aplicación con la plantilla para un formulario de registro por correo electrónico con descuento.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_discount.png %})

### Paso 2: Configura los estilos de tus mensajes

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Paso 3: Personaliza tu componente de registro por correo electrónico

Para empezar a crear tu formulario de registro por correo electrónico, selecciona el elemento de captura de correo electrónico en el editor. Por defecto, las direcciones de correo electrónico recopiladas tendrán el grupo de suscripción global **Suscrito**. Para incluir usuarios en grupos de suscripción específicos, consulta [Actualizar los estados de suscripción por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Puedes personalizar el texto del marcador de posición y el texto de la etiqueta del elemento de captura de correo electrónico.

El editor de mensajes dentro de la aplicación con un menú lateral para personalizar el elemento de captura de correo electrónico.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field.png %})

#### Validación del correo electrónico

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Paso 4: Añade una cláusula de exención de responsabilidad (opcional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Paso 5: Estiliza tu mensaje

Personaliza el aspecto de tu formulario de registro y descuento utilizando [los componentes de]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) arrastrar y soltar [de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components).

## Analizar los resultados

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Buenas prácticas

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}



