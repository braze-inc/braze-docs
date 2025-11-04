---
nav_title: Registro por correo electrónico con confirmación
article_title: Registrarse por correo electrónico con página de confirmación
alias: "/email_confirmation_page/"
page_order: 6
description: "Esta página explica cómo utilizar el editor de arrastrar y soltar mensajes dentro de la aplicación para crear un formulario de registro por correo electrónico que tenga una página de confirmación."
---

# Registrarse por correo electrónico con página de confirmación

> Utiliza el editor de arrastrar y soltar mensajes dentro de la aplicación para crear un formulario de registro por correo electrónico con una página de confirmación.

{% multi_lang_include drag_and_drop/templates.md section='SDK requirements' %}

## Crear un formulario de registro por correo electrónico con una página de confirmación

### Paso 1: Elige tu plantilla

Cuando crees un mensaje dentro de la aplicación arrastrando y soltando, selecciona **Registro por correo electrónico con página de confirmación** para tu plantilla y, a continuación, selecciona **Crear mensaje**. Esta plantilla es compatible tanto con aplicaciones móviles como con navegadores web.

\![El editor de mensajes dentro de la aplicación con la plantilla para un formulario de registro por correo electrónico con página de confirmación.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_confirmation.png %})

### Paso 2: Configura los estilos de tus mensajes

{% multi_lang_include drag_and_drop/templates.md section='message style' %}

### Paso 3: Personaliza tu componente de registro por correo electrónico

Para empezar a crear tu formulario de registro por correo electrónico, selecciona el elemento de captura de correo electrónico en el editor. Por defecto, las direcciones de correo electrónico recopiladas tendrán el grupo de suscripción global **Suscrito**. Para incluir usuarios en grupos de suscripción específicos, consulta [Actualizar los estados de suscripción por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#updating-email-subscription-states).

Puedes personalizar el texto del marcador de posición y el texto de la etiqueta del elemento de captura de correo electrónico.

El editor de mensajes dentro de la aplicación con un menú lateral para personalizar el elemento de captura de correo electrónico.]({% image_buster /assets/img/drag_and_drop/templates/email_capture_field_confirmation.png %})

#### Validación del correo electrónico

{% multi_lang_include drag_and_drop/templates.md section='email validation' %}

### Paso 4: Añade una cláusula de exención de responsabilidad (opcional)

{% multi_lang_include drag_and_drop/templates.md section='email disclaimer' %}

### Paso 5: Estiliza tu mensaje

Personaliza el aspecto de tu formulario de registro por correo electrónico y de la página de confirmación utilizando [los componentes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components) que puedes arrastrar y soltar.

## Analizar los resultados

{% multi_lang_include drag_and_drop/templates.md section='reporting' %}

## Buenas prácticas

{% multi_lang_include drag_and_drop/templates.md section='email double opt-in' %}


