---
nav_title: Desinfección
article_title: Desinfección
page_order: 4
description: "Este artículo define la desinfección y su propósito para la mensajería de correo electrónico en Braze."
channel:
  - email

---

# Acerca de la higienización

> La desinfección es un proceso que tiene lugar cuando Braze detecta un tipo específico de JavaScript en su mensaje de correo electrónico.

## ¿Por qué realizamos el saneamiento?

El objetivo principal de la desinfección es evitar que los actores malintencionados accedan a los datos de sesión de otros usuarios del salpicadero Braze. Sin sanitización, un actor malicioso con acceso básico de sólo lectura puede crear un correo electrónico utilizando el CKEditor con JavaScript que "envía la sesión actual del navegador" a cualquier lugar que el actor malicioso desee utilizando una petición de red.

Cuando otro usuario del panel de control abra esa plantilla de correo electrónico, el JavaScript se ejecutará y enviará los datos de sesión del usuario actual al actor malicioso.

Como nota, la mayoría de los proveedores de buzones de correo electrónico no procesan JavaScript, por lo que esta medida también está pensada para eliminar la acumulación innecesaria de correos electrónicos y reducir su tamaño. 

## ¿Cómo sanea Braze los mensajes?

Si Braze detecta JavaScript que supone un riesgo para la seguridad, antes de ir a la pestaña **Vista previa y prueba** o al editor HTML para ver el mensaje de correo electrónico, le pediremos que confirme que Braze puede eliminar el JavaScript de su mensaje antes de continuar.

![]({% image_buster /assets/img/email_sanitization.png %})

## ¿Cuándo persisten los saneamientos?

Tanto en el editor de arrastrar y soltar como en el editor HTML, desinfectamos, pero no persistimos en los resultados desinfectados para los siguientes escenarios:

* El correo electrónico se presenta en las siguientes áreas:
    * Sección **Inbox Vision** y pestaña **Spam Testing** 
    * Sección **Vista previa y mapa de calor** en el panel **Rendimiento del correo electrónico** 
* El correo electrónico se envía en un envío de prueba

Para el editor de arrastrar y soltar, sanitizamos y también persistimos la sanitización en el mensaje cuando el botón
se cierra el editor y se guarda la campaña. Para el editor HTML, saneamos y también persistimos el saneamiento en el mensaje cuando un usuario cambia entre tipos de editor y se guarda la campaña.

En todos estos casos, aparece un mensaje si la limpieza ha modificado el HTML. El usuario debe aceptarlo antes de que se complete la desinfección.