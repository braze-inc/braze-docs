---
nav_title: Plantillas de administrador
article_title: Plantillas de administrador
page_order: 3

page_type: reference
description: "Este artículo de referencia describe cómo duplicar y archivar plantillas en la sección Plantillas y medios del panel de Braze."
tool:
  - Templates
  - Media

---

# Plantillas de administrador

> Archivar o duplicar plantillas puede ayudar a organizarlas y gestionarlas mejor. Este artículo de referencia explica cómo archivar y duplicar plantillas en la sección **Plantillas** del panel de Braze.

## Duplicar plantillas

### Plantilla individual

Menú desplegable con opción de duplicar.]({% image_buster /assets/img/template_duplicate_cog.png %}){: style="float:right;max-width:15%;margin-left:15px;"}

Para duplicar una plantilla individual, selecciona el icono de engranaje <i class="fas fa-cog"></i> de la plantilla individual y selecciona **Duplicar** en el menú desplegable.
<br><br>

{% alert note %}
Para las plantillas de [Bloque de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/), se crea una copia borrador. Para todas las demás plantillas se crea automáticamente una nueva copia duplicada.
{% endalert %}

### Múltiples plantillas

{% raw %}

Puedes duplicar varias plantillas seleccionando la casilla situada junto al nombre de la plantilla. Primero, selecciona las plantillas y luego **Duplicar**.

Las plantillas duplicadas se pueden encontrar ordenando la columna **Última edición**. Por predeterminado, las nuevas plantillas se llamarán `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

Tres plantillas ordenadas según el momento en que se editaron por última vez, con una plantilla copiada al principio de la lista.]({% image_buster /assets/img/duplicate_multiple_template.gif %})

## Plantillas de archivo

Menú desplegable de configuración ampliado que muestra tres opciones: "Archivar", "Duplicar" y "Copiar al espacio de trabajo" con la opción "Archivar" resaltada.]({% image_buster /assets/img/template_archive_cog.png %}){: style="float:right;max-width:20%;margin-left:15px;"}

Para archivar una plantilla individual, selecciona el icono de configuración en la pantalla de la parrilla de plantillas y selecciona **Archivar**. Cuando se archiva una plantilla, ten en cuenta los siguientes escenarios diferentes:

- Las campañas activas siguen utilizando la plantilla archivada sin ninguna interrupción.
- Los borradores de campaña conservan el contenido de la plantilla archivada y pueden editarse y lanzarse.
- Para editar una plantilla archivada, primero debes desarchivarla. Del mismo modo, para utilizar una plantilla archivada en una campaña, primero debes desarchivar la plantilla.

Para archivar varias plantillas, selecciona la casilla situada junto a cada plantilla que quieras archivar. Cuando hayas seleccionado varias plantillas, selecciona **Archivar**. Puedes encontrar tus plantillas archivadas seleccionando **Archivadas** en **Mostrar** en la cuadrícula de plantillas.

\![Gota Guardada & Gota Sección de plantillas de correo electrónico que muestra dos plantillas seleccionadas y una barra de herramientas con la opción de archivar.]({% image_buster /assets/img/archive_multiple_template.png %}){: style="max-width:60%;"}

{% alert important %}
El archivado no está disponible actualmente para [las plantillas de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}

