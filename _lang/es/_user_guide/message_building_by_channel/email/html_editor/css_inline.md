---
nav_title: CSS Inlining
article_title: CSS Inlining
page_order: 5.1
description: "Este artículo de referencia explica cómo habilitar la inserción de CSS y algunas buenas prácticas."
channel:
  - email

---

# Inserción de CSS

> CSS inlining es una forma de preprocesamiento de correo electrónico que traslada los estilos de una hoja de estilos CSS al cuerpo de un correo electrónico HTML. El término "inlining" se refiere al hecho de que los estilos se aplican "en línea" a elementos HTML individuales.

Para algunos clientes de correo electrónico, la inserción de CSS puede mejorar la presentación de los mensajes y confirmar que tienen el aspecto esperado. Si ya tienes la mayor parte del CSS alineado o estás seguro de que tu HTML y CSS son compatibles con los requisitos de la mayoría de los clientes de correo, puede que no sea necesario activar esta característica. Puede hacer que los estilos incrustados dinámicamente entren en conflicto con tus estilos en línea existentes y puede alterar la previsualización esperada y la representación del correo electrónico.

## Utilizar la inserción de CSS

Puedes controlar si la incrustación de CSS está activada o desactivada para cualquier mensaje de correo electrónico utilizando la pestaña **Habilitar CSS incrustado** en la pestaña **Información de envío** del editor HTML.

![Casilla de verificación para administrar la inserción de CSS en HTML Composer.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Estado de inserción predeterminado

Puede establecer un estado predeterminado de activación o desactivación de forma global desde **Configuración** > **Preferencias de correo electrónico**. Localiza la configuración de **Inserción de CSS**. Este parámetro determina el valor por defecto con el que comenzarán todos los nuevos mensajes de correo electrónico. Tenga en cuenta que el cambio de esta configuración no afectará a ninguno de sus mensajes de correo electrónico existentes. También puede anular este valor predeterminado en cualquier momento mientras redacta mensajes de correo electrónico.

![CSS en línea en nuevos correos electrónicos por opción predeterminada ubicada en la configuración de correo electrónico.]({% image_buster /assets/img_archive/css-inline1.png %})

