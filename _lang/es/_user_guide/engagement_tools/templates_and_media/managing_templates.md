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

![][8]{: style="float:right;max-width:15%;margin-left:15px;"}

Para duplicar una plantilla individual, seleccione el icono de engranaje <i class="fas fa-cog"></i> de la plantilla individual y seleccione **Duplicar** en el menú desplegable.
<br><br>

{% alert note %}
Para las plantillas de [Bloques de contenido]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/), se crea una copia borrador. Para todas las demás plantillas se crea automáticamente una nueva copia duplicada.
{% endalert %}

### Múltiples plantillas

{% raw %}

Para duplicar varias plantillas, marque la casilla situada junto al nombre de la plantilla. En primer lugar, seleccione las plantillas y, a continuación, el botón **Duplicar** que aparece.

Las plantillas duplicadas pueden encontrarse ordenando la columna **Última edición**. Por defecto, las nuevas plantillas se denominarán `Copy of ORIGINAL_TEMPLATE_NAME`.

{% endraw %}

![GIF que muestra a un usuario seleccionando dos plantillas y haciendo clic en "Duplicar", lo que da como resultado un total de cuatro plantillas, ordenadas por la hora en que se editaron por última vez.][9]

## Archivando plantillas

![Menú desplegable de ajustes ampliado que muestra tres opciones: Editar, Archivar y Duplicar, donde resalta la opción Archivar.][10]{: style="float:right;max-width:20%;margin-left:15px;"}

Para archivar una plantilla individual, seleccione el icono de configuración en la pantalla de la parrilla de plantillas y seleccione **Archivar**. Cuando se archiva una plantilla, ten en cuenta los siguientes escenarios diferentes:

- Las campañas activas siguen utilizando la plantilla archivada sin interrupción.
- Los borradores de las campañas conservan el contenido de la plantilla archivada y pueden editarse y lanzarse.
- Para editar una plantilla archivada, primero debe desarchivarla. Del mismo modo, para utilizar una plantilla archivada para una campaña, primero debe desarchivar la plantilla.

Para archivar varias plantillas, seleccione la casilla situada junto a cada plantilla que desee archivar. Una vez seleccionadas varias plantillas, seleccione **Archivar seleccionados**. Puede encontrar sus plantillas archivadas seleccionando **Archivadas** en **Mostrar** en la cuadrícula de plantillas.

![Sección de plantillas de correo electrónico de soltar y soltar guardadas que muestra dos plantillas seleccionadas: "Prueba la plantilla Premium" y "Plantilla de bienvenida". El usuario resalta el botón "Archivo seleccionado".][11]

{% alert important %}
El archivado no está disponible actualmente para [las plantillas de enlaces]({{site.baseurl}}/user_guide/message_building_by_channel/email/link_templates/#link-templates).
{% endalert %}

[10]: {% image_buster /assets/img/template_archive_cog.png %}
[11]: {% image_buster /assets/img/archive_multiple_template.png %}
[8]: {% image_buster /assets/img/template_duplicate_cog.png %}
[9]: {% image_buster /assets/img/duplicate_multiple_template.gif %}