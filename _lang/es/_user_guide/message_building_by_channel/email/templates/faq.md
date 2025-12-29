---
nav_title: PREGUNTAS FRECUENTES
article_title: Preguntas frecuentes sobre plantillas de correo electrónico y enlaces
page_order: 10

page_type: FAQ
description: "Esta página cubre las preguntas más frecuentes sobre plantillas de correo electrónico y plantillas de enlaces."
tool:
  - Templates
channel: email

---

# Preguntas más frecuentes

> Esta página ofrece respuestas a algunas preguntas frecuentes sobre plantillas de correo electrónico y plantillas de enlaces.

## Plantillas de correo electrónico

### ¿Puedo añadir un enlace "ver este correo electrónico en un navegador" a mis correos electrónicos?

No, Braze no ofrece esta funcionalidad. Esto se debe a que una mayoría cada vez mayor del correo electrónico se abre en dispositivos móviles y clientes de correo electrónico modernos, que reproducen imágenes y contenidos sin problemas.

**Solución:** Para conseguir este mismo resultado, puedes alojar el contenido de tu correo electrónico en una página de destino externa (como tu sitio web), a la que luego se puede enlazar desde la campaña de correo electrónico que estás creando utilizando la herramienta **Enlace** al editar el cuerpo del correo electrónico.

### ¿Cómo creo un enlace personalizado para cancelar suscripción en mis plantillas de correo electrónico?

Hay una opción de redirección para la página de cancelar suscripción.

Podrías cambiar el enlace de cancelar suscripción en el pie de página personalizado de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} a un enlace a tu propio sitio web con un parámetro de consulta que incluya el ID de usuario. Un ejemplo es:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

A continuación, podrías llamar al [punto final`/email/status` ]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) para actualizar el estado de suscripción del usuario. Para más detalles, consulta nuestra documentación sobre cómo [cambiar el estado de la suscripción por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Para guardar este nuevo enlace, la etiqueta predeterminada de Braze para cancelar suscripción {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} debe estar en el pie de página. Esto significa que tendrás que incluir el enlace predeterminado "ocultándolo" colocando la etiqueta en un comentario o en una etiqueta oculta de `<div>`.

- **Ejemplo de etiqueta en comentario:** poner etiqueta en comentario ejemplo: `<!-- ${set_user_to_unsubscribed_url} -->`
- **Comentario en el ejemplo de etiqueta oculta `<div>`:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### ¿Qué ocurre si edito una plantilla de correo electrónico que se está utilizando actualmente en una campaña?

Las modificaciones realizadas en una plantilla existente no se reflejarán en las campañas creadas con versiones anteriores de esa plantilla. Para las campañas API que utilicen una plantilla en el cuerpo de la API REST, Braze utilizará la última versión de la plantilla en el momento del envío.  

## Plantillas de enlaces

### ¿Puedo cargar varias plantillas de enlaces en mi correo electrónico?

Sí, puedes insertar tantas plantillas como quieras en tus mensajes de correo electrónico. Como práctica recomendada, deberías probar tus correos electrónicos para asegurarte de que los enlaces no superan los 2.000 caracteres, ya que la mayoría de los navegadores acortan o cortan los enlaces.

### ¿Cómo puedo obtener una vista previa de mis enlaces con todas las etiquetas aplicadas?

Hay varias formas de previsualizar tus enlaces. Después de aplicar la [plantilla de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/), puedes enviarte un [correo electrónico de]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) prueba para ver todos los enlaces. 

Desde el panel de vista previa en una pestaña nueva, también puedes abrir los enlaces para ver los vínculos. También puedes pasar el ratón por encima de los enlaces en el panel de vista previa y verlos en la parte inferior de tu navegador.

### ¿Cómo funciona la plantilla de enlaces con Liquid?

Las plantillas de enlaces se expanden y se añaden a cada URL antes de que se produzca cualquier expansión de Liquid. Si parte de tu URL se genera utilizando un fragmento de código de Liquid, recomendamos que la base de la URL y el signo de interrogación (?) estén codificados para que las plantillas de enlaces se expandan correctamente. 

Evita añadir el signo de interrogación (?) a tu Liquid, ya que esto hará que las plantillas de enlaces añadan primero un signo de interrogación (?), y más tarde el proceso de expansión de Liquid añadirá un segundo signo de interrogación (?).

## Aliasing de enlaces

### ¿Cómo afectará la habilitación del aliasing de enlaces a mis bloques de contenido y plantillas de enlaces?

Para todos los nuevos bloques de contenido que se creen, se aplica el aliasing de enlaces en todos los espacios de trabajo, ya que se trata de una característica a nivel de empresa. 

Los bloques de contenido existentes no se modificarán cuando se habilite el aliasing de enlaces. Aunque no se modificarán las plantillas de enlace existentes, se eliminará la sección de plantilla de enlace existente en un mensaje. Consulta [Aliasing de enlaces en bloques de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#link-aliasing-in-content-blocks) para obtener más información.

### ¿Puedo utilizar la lógica condicional de Liquid completamente dentro de una etiqueta de anclaje HTML?

No, Braze aliasing de enlaces no reconocerá el HTML correctamente. 

Cuando se utiliza una lógica como ésta junto con características que necesitan analizar el HTML (como un preencabezado o una plantilla de enlace), la biblioteca utilizada para analizar el HTML puede modificar la etiqueta de anclaje de forma que impida que se cree la plantilla `href` adecuada. La biblioteca determinará entonces que el HTML no es válido porque es agnóstico al código Liquid. 

En su lugar, utiliza la lógica Liquid que contiene una etiqueta de anclaje completa en cada etapa. Esto no interferirá con el análisis sintáctico de HTML porque la lógica incluye múltiples instancias de HTML válido. También puedes simplificar tu lógica asignando y luego planificando una variable en la etiqueta de anclaje adecuada.
