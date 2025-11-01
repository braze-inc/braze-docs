---
nav_title: Perfiles de color y plantillas CSS
article_title: Perfiles de color y plantillas CSS para mensajes dentro de la aplicación
page_order: 4
page_type: reference
description: "Este artículo ofrece un resumen de los perfiles de color de los mensajes dentro de la aplicación y de las plantillas CSS."
channel:
  - in-app messages
---

# Perfiles de color y plantillas CSS {#reusable-color-profiles}

> Puedes guardar plantillas de mensajes dentro de la aplicación y mensajes en el explorador en el panel para crear rápidamente nuevas campañas y mensajes con tu estilo. 

Ve a **Plantillas** > Plantillas de mensajes dentro de la aplicación **.**

Desde esta página, puedes editar las plantillas existentes o hacer clic en **\+ Crear** y elegir **Perfil de color** o **Plantilla CSS** para crear nuevas plantillas y utilizarlas en tus mensajes dentro de la aplicación.

## Perfil de color

Puedes personalizar la combinación de colores de tu plantilla de mensajes introduciendo un código de color HEX o haciendo clic en la casilla de color y seleccionando un color con el selector de color.

Haz clic en **Guardar perfil de color** cuando hayas terminado.

### Administrador de perfiles de color

¡También puedes [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) y [archivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) plantillas! Obtén más información sobre cómo crear y administrar plantillas y contenido creativo en [Plantillas & Medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Plantilla CSS {#in-app-message-templates}

Puedes personalizar una plantilla CSS completa para tu [mensaje modal web dentro de la aplicación](#web-modal-css).

Nombra y etiqueta tu Plantilla CSS, y luego elige si será o no tu plantilla predeterminada. Puedes escribir tu propio CSS en el espacio proporcionado. Este espacio ya está rellenado previamente con el CSS que se muestra en la vista previa de tu mensaje, y debes sentirte libre de ajustarlo ligeramente para satisfacer tus necesidades.

```css
.ab-message-header, .ab-message-text {
  color: #333333;
  text-align: center;
}

.ab-message-header {
  font-size: 20px;
  font-weight: bold;
}

.ab-message-text {
  font-size: 14px;
  font-weight: normal;
}

.ab-close-button svg {
  fill: #9b9b9b;
}

.ab-message-button {
  border: 1px solid #1b78cf;
  font-size: 14px;
  font-weight: bold;
}
.ab-message-button:first-of-type {
  background-color: white;
  color: #1b78cf;
}
.ab-message-button:last-of-type, .ab-message-button:first-of-type:last-of-type {
  background-color: #1b78cf;
  color: white;
}

.ab-background {
  background-color: white;
}

.ab-icon {
  background-color: #0073d5;
  color: white;
}

.ab-page-blocker {
  background-color: rgba(51, 51, 51, .75);
}
```

Como puedes ver, puedes editarlo todo, desde el color de fondo hasta el tamaño y el peso de la fuente, y mucho más.

### Administrador de plantillas CSS

¡También puedes [duplicar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) y [archivar]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/managing_templates/) plantillas! Obtén más información sobre cómo crear y administrar plantillas y contenido creativo en [Plantillas & Medios]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/).

## Modal con CSS (sólo Web) {#web-modal-css}

Si decides utilizar un Modal Web sólo con mensaje CSS, puedes aplicar tu propia plantilla o escribir tu propio CSS en el espacio proporcionado. Este espacio ya está rellenado previamente con el CSS que se muestra en la vista previa de tu mensaje, pero siéntete libre de ajustarlo ligeramente para satisfacer tus necesidades.

Si decides aplicar tu propia plantilla, haz clic en **Aplicar plantilla** y elige de la galería de plantillas de mensajes dentro de la aplicación. Si no tienes ninguna opción, puedes subir una [plantilla CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css/#in-app-message-templates) utilizando el constructor de plantillas CSS.


