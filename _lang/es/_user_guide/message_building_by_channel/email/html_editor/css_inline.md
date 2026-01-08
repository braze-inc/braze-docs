---
nav_title: Inserción de CSS
article_title: Inserción CSS
page_order: 5.1
description: "Este artículo de referencia explica cómo habilitar el inlining de CSS y algunas buenas prácticas."
channel:
  - email

---

# Inserción de CSS

> La incrustación de CSS es una forma de preprocesamiento de correo electrónico que traslada los estilos de una hoja de estilos CSS al cuerpo de un correo electrónico HTML. El término "inlining" se refiere al hecho de que los estilos se aplican "inline" a elementos HTML individuales.

Para algunos clientes de correo electrónico, la incrustación de CSS puede mejorar la forma en que se muestran los correos electrónicos y ayudar a confirmar que tus correos electrónicos tienen el aspecto que esperas. Si ya tienes la mayor parte del CSS alineado o estás seguro de que tu HTML y CSS son compatibles con los requisitos de la mayoría de los clientes de correo, puede que no sea necesario activar esta característica. Puede hacer que los estilos incrustados dinámicamente entren en conflicto con tus estilos en línea existentes y puede alterar la previsualización esperada y la representación del correo electrónico.

## Utilizar CSS inlining

Puedes controlar si la incrustación de CSS está activada o desactivada para cualquier mensaje de correo electrónico utilizando la pestaña **Habilitar CSS incrustado** en la pestaña **Información de envío** del editor HTML.

Casilla de verificación para gestionar la inserción de CSS en HTML Composer.]({% image_buster /assets/img_archive/css-inline2.png %}){: style="max-width:40%;"}

### Estado predeterminado de inlining

Puedes establecer un estado predeterminado de activado o desactivado globalmente desde **Configuración** > **Preferencias de correo electrónico**. Localiza la configuración de **CSS Inlining**. Esta configuración determina el valor predeterminado deseado con el que empiezan todos los mensajes de correo electrónico nuevos. Ten en cuenta que cambiar esta configuración no afectará a ninguno de tus mensajes de correo electrónico existentes. También puedes anular este valor predeterminado en cualquier momento mientras redactas mensajes de correo electrónico.

\![CSS inline en nuevos correos electrónicos por opción predeterminada ubicada en la configuración de correo electrónico.]({% image_buster /assets/img_archive/css-inline1.png %})

