---
nav_title: Preguntas frecuentes
article_title: Preguntas frecuentes sobre plantillas de correo electrónico y enlaces
page_order: 10

page_type: FAQ
description: "Esta página contiene las preguntas más frecuentes sobre plantillas de correo electrónico y plantillas de enlaces."
tool:
  - Templates
channel: email

---

# Preguntas más frecuentes

> Esta página ofrece respuestas a algunas preguntas frecuentes sobre plantillas de correo electrónico y plantillas de enlaces.

## Plantillas de correo electrónico

### ¿Puedo añadir un enlace "ver este correo en un navegador" a mis correos electrónicos?

No, Braze no ofrece esta funcionalidad. Esto se debe a que una mayoría cada vez mayor del correo electrónico se abre en dispositivos móviles y clientes de correo modernos, que renderizan imágenes y contenidos sin problemas.

**Solución:** Para lograr este mismo resultado, puede alojar el contenido de su correo electrónico en una página de destino externa (como su sitio web), a la que se puede enlazar desde la campaña de correo electrónico que está creando utilizando la herramienta **Enlace** al editar el cuerpo del correo electrónico.

### ¿Cómo puedo crear un enlace de cancelación de suscripción personalizado para mis plantillas de correo electrónico?

Existe una opción de redirección para la página de baja.

Podría cambiar el enlace para darse de baja en el pie de página personalizado de {% raw %} `{{${set_user_to_unsubscribed_url}}}` {% endraw %} a un enlace a su propio sitio web con un parámetro de consulta que incluya el ID de usuario. Un ejemplo:
{% raw %} 
> https://www.braze.com/unsubscribe?user_id={{${user_id}}}
{% endraw %}

A continuación, podrías llamar al [punto final `/email/status`]({{site.baseurl}}/api/endpoints/email/post_email_subscription_status/) para actualizar el estado de suscripción del usuario. Para más detalles, consulte nuestra documentación sobre cómo [cambiar el estado de la suscripción por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#changing-email-subscriptions).

Para guardar este nuevo enlace, la etiqueta de cancelación de suscripción predeterminada de Braze {%raw%}(``${set_user_to_unsubscribed_url}``){%endraw%} debe estar en el pie de página. Esto significa que tendrá que incluir el enlace predeterminado "ocultándolo" colocando la etiqueta en un comentario o en una etiqueta oculta de `<div>`.

- **Ejemplo de etiqueta en comentario:** ejemplo de poner etiqueta en comentario: `<!-- ${set_user_to_unsubscribed_url} -->`
- **Ejemplo de comentario en la etiqueta oculta `<div>`:** {%raw%}`<div style="display:none;max-height:0px;overflow:hidden;">${set_user_to_unsubscribed_url}</div>`{%endraw%}

### ¿Qué ocurre si edito una plantilla de correo electrónico que se está utilizando actualmente en una campaña?

Las modificaciones realizadas en una plantilla existente no se reflejarán en las campañas creadas con versiones anteriores de esa plantilla. Para las campañas API que utilicen una plantilla en el cuerpo de la API REST, Braze utilizará la última versión de la plantilla en el momento del envío.  

## Plantillas de enlaces

### ¿Puedo cargar varias plantillas de enlaces en mi correo electrónico?

Sí, puede insertar tantas plantillas como desee en sus mensajes de correo electrónico. Como buena práctica, debería probar sus correos electrónicos para asegurarse de que los enlaces no superan los 2.000 caracteres, ya que la mayoría de los navegadores acortan o cortan los enlaces.

### ¿Cómo puedo previsualizar mis enlaces con todas las etiquetas aplicadas?

Hay varias formas de previsualizar sus enlaces. Una vez aplicada la [plantilla de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_template/), puede enviarse a sí mismo un [correo electrónico de prueba]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages/) para ver todos los enlaces. 

Desde el panel de vista previa en una nueva pestaña, también puede abrir los enlaces para ver los vínculos. También puede pasar el ratón por encima de los enlaces en el panel de vista previa y verlos en la parte inferior de su navegador.

### ¿Cómo funciona la plantilla de enlaces con Liquid?

Las plantillas de enlaces se expanden y se añaden a cada URL antes de que se produzca cualquier expansión de Liquid. Si parte de tu URL se genera utilizando un fragmento de código de Liquid, recomendamos que la base de la URL y el signo de interrogación (?) estén codificados para que las plantillas de enlace se expandan correctamente. 

Evite añadir el signo de interrogación (?) a su Liquid, ya que esto hará que las plantillas de enlace añadan primero un signo de interrogación (?), y más tarde el proceso de expansión de Liquid añadirá un segundo signo de interrogación (?).

## Alias de enlace

### ¿Cómo afectará a mis bloques de contenido y plantillas de enlaces la activación del alias de enlaces?

Para todos los nuevos bloques de contenido que se creen, el alias de enlace se aplica en todos los espacios de trabajo, ya que se trata de una función a nivel de empresa. 

Los bloques de contenido existentes no se modificarán cuando se active el alias de enlace. Mientras que las plantillas de enlace existentes no se modificarán, la sección de plantilla de enlace existente en un mensaje se eliminará. Para más información, consulte [Alias de enlaces en bloques de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#link-aliasing-in-content-blocks).

### ¿Puedo utilizar la lógica condicional de Liquid completamente dentro de una etiqueta de anclaje HTML?

No, Braze link aliasing no reconocerá el HTML correctamente. 

Cuando una lógica de este tipo se utiliza junto con funciones que necesitan analizar el HTML (como un preencabezado o la creación de plantillas de enlaces), la biblioteca utilizada para analizar el HTML puede modificar la etiqueta de anclaje de forma que impida que se cree la plantilla `href` adecuada. La biblioteca determinará entonces que el HTML no es válido porque es agnóstica al código Liquid. 

En su lugar, utilice una lógica líquida que contenga una etiqueta de anclaje completa en cada etapa. Esto no interferirá con el análisis sintáctico de HTML porque la lógica incluye múltiples instancias de HTML válido. También puede simplificar su lógica asignando y luego planificando una variable en la etiqueta de anclaje apropiada.
