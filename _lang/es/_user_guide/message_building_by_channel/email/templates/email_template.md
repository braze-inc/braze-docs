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





{% alert note %}
Cualquier plantilla HTML personalizada existente tendrá que volver a crearse utilizando el editor de arrastrar y soltar.
{% endalert %}

## Paso 3: Personaliza tu plantilla

Después de seleccionar su experiencia como editor, esta es su oportunidad para ser creativo con la personalización de su plantilla de correo electrónico. Puede utilizar HTML para crear y emular su marca en el editor HTML, o incluir una variedad de [detalles creativos]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details) en el editor de arrastrar y soltar.

### Incluir un enlace para darse de baja

Cuando diseñe su plantilla de correo electrónico, si no incluye un enlace de cancelación de suscripción, Braze le pedirá que lo añada en su correo electrónico, ya que es obligatorio por ley en todos los correos electrónicos de marketing. Puede añadir este enlace de cancelación de suscripción como pie de página en la parte inferior de sus correos electrónicos utilizando la etiqueta Liquid {% raw %}``${email_footer}``{% endraw %}, o [personalizando el pie de página]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#custom-footer) en su plantilla.

## Paso 4: Compruebe si hay errores en el correo electrónico

Los errores de correo electrónico se presentan en la pestaña **Redactar** del flujo de trabajo del mensaje. Los errores le impiden avanzar. Las "advertencias" indican recordatorios para ayudarle a seguir las mejores prácticas. Dependiendo de su negocio, puede optar por ignorarlos.



He aquí una lista de errores que se tienen en cuenta en nuestro editor:

- Sintaxis incorrecta de Liquid
- 
- Plantillas sin enlace para darse de baja
- Correos electrónicos con el **cuerpo** o el **asunto** en blanco
- Correos electrónicos sin enlace para darse de baja

## Paso 5: Vista previa y prueba de tu mensaje

Cuando termine de componer su plantilla, puede probarla antes de enviarla.

 Aquí puede previsualizar cómo aparecerá su correo electrónico en la bandeja de entrada de un cliente. Con la opción **Previsualizar como usuario** seleccionada, puede previsualizar su correo electrónico como un usuario aleatorio, seleccionar un usuario específico o crear un usuario personalizado. Esto le permite comprobar que su contenido conectado y las llamadas de personalización funcionan como deberían. 

 

También puede alternar entre las vistas de escritorio, móvil y texto sin formato para hacerse una idea de cómo aparecerá su mensaje en diferentes contextos.


 


Cuando esté listo para una comprobación final, seleccione **Probar envío** y envíe un mensaje de prueba a usted mismo o a un grupo de evaluadores de contenido para asegurarse de que su correo electrónico se muestra correctamente en una variedad de dispositivos y clientes de correo electrónico.





## Paso 6: Guarda tu plantilla

 Ahora está listo para utilizar esta plantilla en cualquier campaña o componente Canvas que elija. Para acceder a su plantilla, seleccione la experiencia de edición con la que la creó y, a continuación, selecciónela en la lista de plantillas disponibles.

{% alert note %}
Si modifica una plantilla existente, los cambios no se reflejarán en las campañas creadas con versiones anteriores de esa plantilla.
{% endalert %}

### Gestión de plantillas

A medida que cree más plantillas de correo electrónico, podrá [duplicarlas]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#duplicate-templates) y [archivarlas]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/#archive-templates). Obtén más información sobre cómo crear y gestionar tu biblioteca de plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

### Utilización de sus plantillas en campañas API

Para utilizar su correo electrónico en una campaña API, necesita un `email_template_id`, que puede encontrar en la parte inferior de cualquier plantilla de correo electrónico creada en Braze.



### Comentarios sobre las plantillas de correo electrónico

Puedes colaborar y comentar plantillas de correo electrónico en el editor de arrastrar y soltar. 

1. 
2. Seleccione el icono de comentario <i class="fas fa-comment"></i>.
3. 
4. 
5. 

Una vez guardada la plantilla, los usuarios pueden ver iconos sobre los comentarios sin respuesta. Seleccione **Resolver** para resolver estos comentarios.





