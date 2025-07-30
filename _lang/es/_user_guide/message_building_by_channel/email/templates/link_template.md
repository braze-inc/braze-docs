---
nav_title: Plantilla de enlaces
article_title: Plantilla de enlaces
page_order: 4
description: "Este artículo explica cómo crear diferentes tipos de plantillas de enlaces en sus correos electrónicos."
tool:
  - Templates
channel:
  - email

---

# Plantillas de enlaces

> Con las plantillas de enlaces, puedes crear enlaces dinámicos y reutilizables para tus campañas de correo electrónico añadiendo parámetros o URLs. Esto puede crear coherencia en las URL de tus campañas y mensajes. 

{% alert note %}
Las plantillas de enlaces son opcionales. Si en la sección **Plantillas** no aparece **Plantillas de enlaces de correo electrónico**, póngase en contacto con su gestor de cuenta para activar la función.
{% endalert %}

## Cómo funciona

Las plantillas de enlaces se utilizan con mayor frecuencia en los siguientes casos de uso:

- Aplicación de parámetros de consulta de Google Analytics a todos los enlaces de un mensaje de correo electrónico determinado
- Añadir una URL a todos los enlaces de un mensaje de correo electrónico determinado

Supongamos que estás realizando una campaña promocional por correo electrónico para el lanzamiento de un nuevo producto. Puedes utilizar una plantilla de enlace que dirija a los usuarios a la página del producto y personalizar el enlace para que incluya el nombre de tu usuario o un código promocional específico. Esto puede permitirte hacer un seguimiento de cuántos usuarios han hecho clic en el enlace y han realizado una compra. De este modo, puedes crear coherencia entre tus enlaces y realizar un mejor seguimiento de tus análisis.

## Creación de una plantilla de enlace

Puede crear un número ilimitado de plantillas de enlaces para satisfacer sus distintas necesidades. Para crear una plantilla de enlace, haz lo siguiente:

1. Vaya a **Plantillas** > **Plantillas de enlaces de correo electrónico**. 
2. Selecciona **Crear plantilla de enlace de correo electrónico**.
3. Dale un nombre a tu plantilla de enlaces.
4. (Opcional) Añade una descripción, un equipo o una etiqueta para añadir detalles sobre la plantilla de enlace.
5. (Opcional) Selecciona la opción de alternar para añadir automáticamente la plantilla de enlace a los enlaces en campañas de correo electrónico y Lienzos. Esto se aplica al añadir un nuevo enlace a cualquier correo electrónico nuevo o existente.

Puede crear dos tipos de plantillas de enlaces:

- [Plantilla de enlace que se inserta antes de una URL](#prepend-link-template)
- [Plantilla de enlace que se inserta después de una URL](#append-link-template)

Al utilizar plantillas de enlace y [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), Liquid sólo debe añadirse dentro de la etiqueta body para garantizar una representación coherente.

### Anteponer: Crear una plantilla de enlace que se inserta antes de una URL {#prepend-link-template}

Para añadir una cadena o URL antes de los enlaces en tu mensaje de correo electrónico, haz lo siguiente:

1. Crea una nueva plantilla de enlace.
2. Configura la **Posición de la plantilla** en **Antes de URL**. 
3. Introduce una cadena que siempre se añadirá a tu URL. 

La **vista previa de la** plantilla se proporciona para darte un ejemplo de cómo se insertará la plantilla de enlace antes de una URL.

![Campos Template Position, Prepend URL y Template Preview para el proceso de inserción de plantillas de enlace antes de una URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Anexar: Crear una plantilla de enlace que se inserta después de una URL {#append-link-template}

Si quieres añadir parámetros de consulta después de una URL en tu mensaje de correo electrónico:

1. Crea una nueva plantilla de enlace.
2. Configura la **Posición de la plantilla** en **Después de la URL**. 
3. Introduce los parámetros de consulta (`value=example`) al final de cada URL. Puede añadir varios parámetros al final de una URL.

![Campos Posición de la plantilla, Parámetros de consulta y Vista previa de la plantilla para el proceso de inserción de plantillas de enlace tras una URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Utilizar plantillas de enlaces en las campañas de correo electrónico

Una vez configuradas las plantillas de enlaces, puede seleccionar la plantilla que desea utilizar en su correo electrónico.

- **Editor HTML:** Vaya a la pestaña **Gestión de enlaces** en la sección **Contenido**. Selecciona **Añadir una plantilla de** enlace, elige tu plantilla de enlace y selecciona **Añadir**.

{% alert important %}
Para acceder a la pestaña **Gestión de enlaces** en el editor de correo electrónico HTML actualizado, debe tener activado el alias de enlaces. Para activar el alias de enlaces, póngase en contacto con el gestor de su cuenta.
{% endalert %}

- **Editor de arrastrar y soltar:** Seleccione **Contenido** > pestaña **Gestión de enlaces**. A continuación, selecciona **Añadir una plantilla de enlace**. Para acceder a las plantillas de enlaces en el editor de arrastrar y soltar, debe tener activado [el alias de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/).

![Pestaña de gestión de enlaces en el editor de arrastrar y soltar con una lista de ejemplo de plantillas de enlaces.]({% image_buster /assets/img_archive/link_template_messagecomposer2.png %})

{% alert note %}
Las plantillas de enlaces no se aplican al texto sin formato. Esto significa que Currents puede mostrar clics que no incluyan los parámetros de las plantillas de enlace, ya que esos clics pueden proceder de la versión de texto sin formato del correo electrónico.
{% endalert %}

A medida que añada plantillas de enlaces en la pestaña **Gestión de enlaces**, desplácese a la derecha para ver las plantillas que ha añadido. Si los enlaces existentes dentro de un correo electrónico ya tienen una plantilla de enlace añadida, los enlaces recién añadidos también tendrán la plantilla de enlace añadida de forma predeterminada.

## Gestión de plantillas de enlaces

También puede [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) plantillas de enlaces. Más información sobre la creación y gestión de plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
El archivado de plantillas no está disponible actualmente para las plantillas de enlaces.
{% endalert %}

## Preguntas más frecuentes

Para obtener respuestas a las preguntas más frecuentes sobre las plantillas de enlaces, consulta nuestra página [de Preguntas frecuentes sobre plantillas]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/).

