---
nav_title: Guardar borradores para Canvas
article_title: Guardar borradores para Canvas
alias: "/save_as_draft/"
page_order: 1
description: "Este artículo de referencia explica cómo guardar un borrador de un lienzo que ya se ha lanzado."
page_type: reference
tool: Canvas
---

# Guardar borradores para Canvas

> A medida que crea y lanza lienzos, puede editar un lienzo activo y guardarlo como borrador, lo que le permite comprobar los cambios antes de volver a lanzarlo. 

Si tienes un Canvas activo que requiere cambios a gran escala, puedes utilizar esta característica para crear, guardar y comprobar la calidad **antes** de lanzar estos cambios en el Canvas activo. 

Como en cualquier Canvas, sólo un usuario puede editar un borrador a la vez, y un Canvas sólo puede tener un borrador a la vez. Estos borradores no tienen ningún análisis porque todavía no se han lanzado los cambios de borrador.

![Un ejemplo de borrador de lienzo con un banner que indica al usuario que está editando un borrador de lienzo con una opción para ver el lienzo activo. El pie de página tiene opciones para volver a la vista de análisis, guardar como borrador o iniciar el borrador.]({% image_buster /assets/img_archive/canvas_draft1.png %})

## Crear un borrador

Para crear un borrador:

1. Ve a un Canvas activo.
2. Selecciona el botón **Guardar como borrador** en el pie de página del Canvas. 

Tenga en cuenta que no se pueden realizar ediciones en el lienzo activo mientras exista un borrador de un lienzo. Puede actualizar el lienzo para aplicar los cambios o descartar el borrador.

## Referencia al borrador activo

Para hacer referencia al lienzo activo, seleccione **Ver lienzo activo** en el pie de página de la vista de análisis o en la cabecera del lienzo del borrador. Para volver a un lienzo activo, seleccione **Editar borrador** en la vista de análisis o en la vista del lienzo activo.

Sólo puedes hacer referencia a pasos que ya se hayan lanzado antes de crear el borrador. Esto significa que si creaste un paso o canal **después ** de que se creara el borrador, no se podrá hacer referencia a él en tu borrador.

{% alert note %}
Si se hace referencia a un Bloque de contenido en un borrador de Canvas, éste aparece en el recuento de inclusión de Bloques de contenido. Sin embargo, si se hace referencia al Bloque de contenido en un borrador de un Canvas **activo**, el Canvas no aparecerá en el recuento de inclusión del Bloque de contenido.
{% endalert %}

### Priorización de mensajes en la aplicación

En el caso de los borradores de un lienzo activo, la prioridad de los mensajes dentro de la aplicación se actualizará inmediatamente cuando el usuario cambie la prioridad. Esto significa que la prioridad de los mensajes in-app a nivel de lienzo se aplica al lienzo activo inmediatamente, incluso cuando existe un borrador. 

Sin embargo, los cambios de prioridad de mensajes in-app a nivel de paso se guardan como borrador y se aplican cuando se actualiza el Lienzo. Por ejemplo, en un paso de Mensaje, el clasificador de prioridades se actualizará cuando un usuario inicie el borrador, ya que la configuración del paso se aplica a nivel de paso.

