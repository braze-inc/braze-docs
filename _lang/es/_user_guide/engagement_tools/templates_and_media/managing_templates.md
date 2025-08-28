---
nav_title: Gestión de plantillas
article_title: Gestión de plantillas
page_order: 3

page_type: reference
description: "Este artículo de referencia describe cómo duplicar y archivar plantillas en la sección Plantillas y medios del panel Braze."
tool:
  - Templates
  - Media

---

# Gestión de plantillas

> Archivar o duplicar plantillas puede ayudar a organizarlas y gestionarlas mejor. Este artículo de referencia explica cómo archivar y duplicar plantillas en la sección **Plantillas** del panel de control de Braze.

## Duplicar plantillas

### Plantilla individual

![Menú desplegable con opción de duplicado.]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Para duplicar una plantilla individual, seleccione el icono de engranaje <i class="fas fa-cog"></i> de la plantilla individual y seleccione **Duplicar** en el menú desplegable.
<br><br>

{% alert note %}
Para las plantillas de [Bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/), se crea una copia borrador. Para todas las demás plantillas se crea automáticamente una nueva copia duplicada.
{% endalert %}

### Múltiples plantillas

{% raw %}

Para duplicar varias plantillas, marque la casilla situada junto al nombre de la plantilla. Primero, selecciona las plantillas y luego **Duplicar**.

Las plantillas duplicadas pueden encontrarse ordenando la columna **Última edición**. Por defecto, las nuevas plantillas se denominarán `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

![Tres plantillas ordenadas por la hora en que se editaron por última vez, con una plantilla copiada al principio de la lista.]({% image_buster /assets/img/duplicate_multiple_template.gif %})

## Archivando plantillas

![Menú desplegable de ajustes ampliado que muestra tres opciones: "Archivar", "Duplicar" y "Copiar al espacio de trabajo" con la opción "Archivar" resaltada.]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

Para archivar una plantilla individual, seleccione el icono de configuración en la pantalla de la parrilla de plantillas y seleccione **Archivar**. Cuando se archiva una plantilla, ten en cuenta los siguientes escenarios diferentes:

- Las campañas activas siguen utilizando la plantilla archivada sin interrupción.
- Los borradores de las campañas conservan el contenido de la plantilla archivada y pueden editarse y lanzarse.
- Para editar una plantilla archivada, primero debe desarchivarla. Del mismo modo, para utilizar una plantilla archivada para una campaña, primero debe desarchivar la plantilla.

Para archivar varias plantillas, seleccione la casilla situada junto a cada plantilla que desee archivar. Cuando hayas seleccionado varias plantillas, selecciona **Archivar**. Puede encontrar sus plantillas archivadas seleccionando **Archivadas** en **Mostrar** en la cuadrícula de plantillas.

![Sección de plantillas de correo electrónico de soltar y soltar guardadas que muestra dos plantillas seleccionadas y una barra de herramientas con la opción de archivar.]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
El archivado no está disponible actualmente para [las plantillas de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}

