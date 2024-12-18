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

> Las plantillas de enlaces te permiten añadir parámetros o anexar URL al principio de todos los enlaces en un mensaje de correo electrónico.

Las plantillas de enlaces se utilizan con mayor frecuencia en los siguientes casos de uso:

1. Aplicación de parámetros de consulta de Google Analytics a todos los enlaces de un mensaje de correo electrónico determinado
2. Añadir una URL a todos los enlaces de un mensaje de correo electrónico determinado

{% alert note %}
Las plantillas de enlaces son opcionales. Si en la sección **Plantillas** no aparece **Plantillas de enlaces de correo electrónico**, póngase en contacto con su gestor de cuenta para activar la función.
{% endalert %}

## Creación de una plantilla de enlace

![][11]{: style="float:right;max-width:20%;"}

Puede crear un número ilimitado de plantillas de enlaces para satisfacer sus distintas necesidades. Para crear una plantilla de enlace:

1. Vaya a **Plantillas** > **Plantillas de enlaces de correo electrónico**. 
2. Haga clic en **Crear plantilla de enlace**.

{% alert note %}
Si utiliza la [navegación antigua]({{site.baseurl}}/navigation), esta página se encuentra en **Compromiso** > **Plantillas y medios** > **Plantillas de enlaces**.
{% endalert %}

Puede crear dos tipos de plantillas de enlaces:

- [Plantilla de enlace que se inserta antes de una URL](#prepend-link-template)
- [Plantilla de enlace que se inserta después de una URL](#append-link-template)

Al utilizar plantillas de enlace y [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), Liquid sólo debe añadirse dentro de la etiqueta body para garantizar una representación coherente.

### Anteponer: Crear una plantilla de enlace que se inserta antes de una URL {#prepend-link-template}

Si desea añadir una cadena o URL antes de los enlaces en su mensaje de correo electrónico, cree una nueva plantilla de enlace y establezca la **Posición de la plantilla** en **Antes de URL**. A continuación, introduzca una cadena que se añadirá siempre a su URL. 

Se proporciona una sección de vista previa para darle un ejemplo del proceso de inserción.

![Campos Template Position, Prepend URL y Template Preview para el proceso de inserción de plantillas de enlace antes de una URL.]({% image_buster /assets/img_archive/link_template_preappend.png %}){: style="max-width:90%;"}

### Anexar: Crear una plantilla de enlace que se inserta después de una URL {#append-link-template}

Si desea añadir parámetros de consulta después de una URL en su mensaje de correo electrónico, cree una nueva plantilla de enlace y establezca la **Posición de la plantilla** en **Después de URL**. A continuación, introduce parámetros de consulta (`value=something`) al final de cada URL.

Puede añadir varios parámetros al final de una URL.

![Campos Posición de la plantilla, Parámetros de consulta y Vista previa de la plantilla para el proceso de inserción de plantillas de enlace tras una URL.]({% image_buster /assets/img_archive/link_template_postappend.png %}){: style="max-width:90%;"}

## Utilizar plantillas de enlaces en las campañas de correo electrónico

Una vez configuradas las plantillas de enlaces, puede seleccionar la plantilla que desea utilizar en su correo electrónico.

- **Editor HTML:** Vaya a la pestaña **Gestión de enlaces** en la sección **Contenido**. Selecciona **Añadir una plantilla de** enlace, elige tu plantilla de enlace y selecciona **Añadir**.

{% alert important %}
Para acceder a la pestaña **Gestión de enlaces** en el editor de correo electrónico HTML actualizado, debe tener activado el alias de enlaces. Para activar el alias de enlaces, póngase en contacto con el gestor de su cuenta.
{% endalert %}

- **Editor de arrastrar y soltar:** Seleccione **Contenido** > pestaña **Gestión de enlaces**. A continuación, selecciona **Añadir una plantilla de enlace**. Para acceder a las plantillas de enlaces en el editor de arrastrar y soltar, debe tener activado [el alias de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/).

![Pestaña Gestión de enlaces en el editor de arrastrar y soltar con una lista de ejemplos de plantillas de enlaces.][1]

{% alert note %}
Las plantillas de enlaces no se aplican al texto sin formato. Esto significa que Currents puede mostrar clics que no incluyan los parámetros de las plantillas de enlace, ya que esos clics pueden proceder de la versión de texto sin formato del correo electrónico.
{% endalert %}

A medida que añada plantillas de enlaces en la pestaña **Gestión de enlaces**, desplácese a la derecha para ver las plantillas que ha añadido.

## Gestión de plantillas de enlaces

También puede [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/duplicate/) plantillas de enlaces. Más información sobre la creación y gestión de plantillas y contenido creativo en [Plantillas y medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

{% alert important %}
El archivado de plantillas no está disponible actualmente para las plantillas de enlaces.
{% endalert %}

## Preguntas más frecuentes

Para obtener respuestas a las preguntas más frecuentes sobre las plantillas de enlaces, consulte nuestra página [Preguntas frecuentes sobre plantillas][10].

[1]:{% image_buster /assets/img_archive/link_template_messagecomposer2.png %}
[2]:{% image_buster /assets/img_archive/link_template_postappend.png %}
[3]:{% image_buster /assets/img_archive/link_template_preappend.png %}
[4]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/faq/
[11]: {% image_buster /assets/img_archive/create_link_template.png %}
