---
nav_title: Crear una plantilla de correo electrónico
article_title: Crear una plantilla de correo electrónico
page_order: 0
description: "Este artículo de referencia explica cómo crear, personalizar y gestionar plantillas de correo electrónico."
tool:
  - Templates
channel:
  - email
alias: "/dnd/email_template/"
search_rank: 1
---

# Crear una plantilla de correo electrónico

> El panel de control de Braze cuenta con un editor de plantillas de correo electrónico que permite crear correos personalizados y llamativos y guardarlos para utilizarlos posteriormente en campañas. También puede cargar su propia [plantilla de correo electrónico HTML]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/).

## Paso 1: Vaya al editor de plantillas de correo electrónico

Vaya a **Plantillas** > **Plantillas de correo electrónico**.

## Paso 2: Seleccione su experiencia de edición 

Seleccione entre **el editor de arrastrar y soltar** o **el editor HTML** para su experiencia de edición. 

A continuación, puede elegir entre plantillas Braze prediseñadas, crear una nueva plantilla o editar una plantilla existente (simple o [mobile responsive][8]).

![Una plantilla de correo electrónico para las rebajas de primavera de una empresa con opciones para seleccionar el editor de arrastrar y soltar o el editor HTML, o para seleccionar entre las plantillas Braze.][2]

{% alert note %}
Cualquier plantilla HTML personalizada existente tendrá que volver a crearse utilizando el editor de arrastrar y soltar.
{% endalert %}

## Paso 3: Personaliza tu plantilla

Después de seleccionar su experiencia como editor, esta es su oportunidad para ser creativo con la personalización de su plantilla de correo electrónico. Puede utilizar HTML para crear y emular su marca en el editor HTML, o incluir una variedad de [detalles creativos]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) en el editor de arrastrar y soltar.

### Incluir un enlace para darse de baja

Cuando diseñe su plantilla de correo electrónico, si no incluye un enlace de cancelación de suscripción, Braze le pedirá que lo añada en su correo electrónico, ya que es obligatorio por ley en todos los correos electrónicos de marketing. Puede añadir este enlace de cancelación de suscripción como pie de página en la parte inferior de sus correos electrónicos utilizando la etiqueta Liquid {% raw %}``${email_footer}``{% endraw %}, o [personalizando el pie de página]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer) en su plantilla.

## Paso 4: Compruebe si hay errores en el correo electrónico

Los errores de correo electrónico se presentan en la pestaña **Redactar** del flujo de trabajo del mensaje. Los errores le impiden avanzar. Las "advertencias" indican recordatorios para ayudarle a seguir las mejores prácticas. Dependiendo de su negocio, puede optar por ignorarlos.

![Lista de errores y advertencias de un correo electrónico de ejemplo.][1]{: style="float:right;max-width:40%;margin-left:15px;"}

He aquí una lista de errores que se tienen en cuenta en nuestro editor:

- Sintaxis incorrecta de Liquid
- [Cuerpos de correo electrónico de más de 400kb; se recomienda encarecidamente que los cuerpos tengan menos de 102kb.][7]
- Plantillas sin enlace para darse de baja
- Correos electrónicos con el **cuerpo** o el **asunto** en blanco
- Correos electrónicos sin enlace para darse de baja

## Paso 5: Vista previa y prueba de tu mensaje

Cuando termine de componer su plantilla, puede probarla antes de enviarla.

En la parte inferior de la pantalla general, haga clic en **Vista previa y prueba**. Aquí puede previsualizar cómo aparecerá su correo electrónico en la bandeja de entrada de un cliente. Con la opción **Previsualizar como usuario** seleccionada, puede previsualizar su correo electrónico como un usuario aleatorio, seleccionar un usuario específico o crear un usuario personalizado. Esto le permite comprobar que su contenido conectado y las llamadas de personalización funcionan como deberían.

También puede alternar entre las vistas de escritorio, móvil y texto sin formato para hacerse una idea de cómo aparecerá su mensaje en diferentes contextos.

Cuando esté listo para una comprobación final, seleccione **Probar envío** y envíe un mensaje de prueba a usted mismo o a un grupo de evaluadores de contenido para asegurarse de que su correo electrónico se muestra correctamente en una variedad de dispositivos y clientes de correo electrónico.

![Ejemplo de vista previa de correo electrónico que se enviará para realizar pruebas.][6]

Si observa algún problema con su plantilla o desea realizar algún cambio, haga clic en **Editar correo electrónico** para volver al editor.

## Paso 6: Guarda tu plantilla

Asegúrese de guardar su plantilla haciendo clic en **Guardar plantilla**. Ahora está listo para utilizar esta plantilla en cualquier campaña o componente Canvas que elija. Para acceder a su plantilla, seleccione la experiencia de edición con la que la creó y, a continuación, selecciónela en la lista de plantillas disponibles.

{% alert note %}
Si modifica una plantilla existente, los cambios no se reflejarán en las campañas creadas con versiones anteriores de esa plantilla.
{% endalert %}

### Gestión de plantillas

A medida que cree más plantillas de correo electrónico, podrá [duplicarlas]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) y [archivarlas]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates). Obtén más información sobre cómo crear y gestionar tu biblioteca de plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

### Utilización de sus plantillas en campañas API

Para utilizar su correo electrónico en una campaña API, necesita un `email_template_id`, que puede encontrar en la parte inferior de cualquier plantilla de correo electrónico creada en Braze.

![Identificador API situado en la parte inferior de una plantilla de correo electrónico.][5]

### Comentarios sobre las plantillas de correo electrónico

Puedes colaborar y comentar plantillas de correo electrónico en el editor de arrastrar y soltar. 

1. Haga clic en el bloque de contenido o en la fila del cuerpo del correo electrónico que desee comentar.
2. Seleccione el icono de comentario <i class="fas fa-comment"></i>.
3. Escriba su comentario en la barra lateral y haga clic en **Enviar**.
4. Después de introducir sus comentarios, haga clic en **Listo**.
5. Haga clic en **Guardar plantilla** para guardar sus comentarios.

Una vez guardada la plantilla, los usuarios pueden ver iconos sobre los comentarios sin respuesta. Seleccione **Resolver** para resolver estos comentarios.

![Un comentario de plantilla de correo electrónico que dice "Me parece bien".][10]

Para obtener respuestas a las preguntas más frecuentes sobre plantillas de correo electrónico, consulte nuestras [Preguntas frecuentes sobre plantillas][9].

[1]: {% image_buster /assets/img/dnd_compose_error.png %}
[2]: {% image_buster /assets/img/email_templates/template2.png %}
[3]: {% image_buster /assets/img/email_templates/template3.png %}
[4]: {% image_buster /assets/img/email_templates/template4.png %}
[5]: {% image_buster /assets/img/email_templates/template5.png %}
[6]: {% image_buster /assets/img_archive/newEmailTest.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/
[8]: {{site.baseurl}}/help/release_notes/2018/may/#mobile-responsive-email-templates
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[10]: {% image_buster /assets/img/email_templates/template_comment.png %}
