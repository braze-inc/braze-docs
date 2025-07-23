---
nav_title: Configuración de estilo global del correo electrónico
article_title: Configuración de estilo global del correo electrónico
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Este artículo de referencia explica cómo establecer la configuración global del estilo de correo electrónico en el editor de arrastrar y soltar para tus campañas y lienzos."
tool: 
  - Campaigns
  - Canvas
---

# Configuración global del estilo del correo electrónico

> Con los ajustes de estilo globales, puede personalizar el aspecto de sus campañas de correo electrónico y de sus lienzos. Puede añadir y personalizar un tema predeterminado para su editor de arrastrar y soltar. Esto incluye la edición de tus estilos para títulos de correo electrónico, texto, botones y mucho más. Utilizar una combinación de estos ajustes puede ayudar a crear un aspecto coherente en todos sus mensajes de correo electrónico.

Para editar la configuración global de estilo, vaya a **Configuración** > **Preferencias de correo electrónico** > **Preferencias de correo electrónico de arrastrar y soltar**. Después de editar los estilos en el editor de correo electrónico de arrastrar y soltar, haga clic en **Guardar**. Para personalizar aún más sus campañas de correo electrónico y Canvases, compruebe cómo puede incorporar [bloques de edición de arrastrar y soltar][8].

![][1]

{% alert note %}
Las actualizaciones realizadas en los ajustes de estilo globales se aplicarán a todas las campañas de correo electrónico y lienzos futuros.
{% endalert %} 

## Estilo básico 

En **Estilos básicos**, puede establecer los colores de fondo predeterminados del correo electrónico y del contenido para sus campañas de correo electrónico y lienzos. También puede seleccionar una fuente predeterminada, añadir una fuente personalizada y editar los colores de los enlaces.

![Opciones básicas de estilo que incluyen opciones para editar los colores de fondo del correo electrónico y del contenido, el nombre de la fuente predeterminada y el color predeterminado de los enlaces.][2] 

## Fuente personalizada

Con las fuentes personalizadas, puede añadir manualmente una fuente web para dar coherencia a la marca en varias plataformas de correo electrónico. Puede añadir una fuente personalizada por sección. 

Antes de añadir una fuente personalizada, compruebe que el archivo de fuente personalizada cumple los siguientes requisitos:

- CORS debe estar activado en el servidor que proporciona el archivo de fuentes personalizadas. Normalmente lo gestiona tu equipo de TI. 
  - El archivo de fuentes personalizadas debe tener la cabecera `Access-Control-Allow-Origin: *`
- La URL del archivo debe apuntar a un archivo CSS (no WOFF, OTF, etc.)
- El nombre de la fuente personalizada debe coincidir con el nombre de la fuente en el archivo CSS.

Para añadir una fuente personalizada:

1. Haga clic en **Añadir una fuente personalizada** debajo del **Nombre de fuente predeterminado** de la sección de estilo.
2. En el campo **Nombre de fuente**, introduzca el mismo nombre de fuente que aparece en su archivo fuente personalizado. Asegúrese de que el nombre está escrito en mayúsculas y a espacio correcto. 
3. Introduzca la URL correspondiente en el campo **URL de fuente**.
4. Comprueba que la vista previa muestra tu fuente personalizada antes de guardar. 
5. Haga clic en **Guardar** para utilizar la fuente personalizada como fuente predeterminada de correo electrónico. 

{% alert important %}
Gmail no admite fuentes personalizadas, por lo que es posible que tu fuente personalizada se muestre como fuente predeterminada del sistema. Para otras plataformas de correo electrónico, compruebe que su fuente personalizada se muestra correctamente antes de enviar su mensaje de correo electrónico.
{% endalert %}

Tenga en cuenta que el proveedor de fuentes personalizadas puede recopilar datos personales de sus destinatarios. Debes revisar las políticas de tu proveedor de fuentes antes de utilizarlas.

Para utilizar fuentes personalizadas alternativas en sus campañas de correo electrónico, tiene la opción de crear una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) o [Bloques de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). Asegúrese de que la fuente elegida sigue siendo segura para la web y compatible con sus plataformas de correo electrónico. 

### Fuente alternativa

Las fuentes de reserva se utilizan para el título, la cabecera y el cuerpo del texto cuando el proveedor de buzones de entrada o el sistema operativo no admiten la fuente predeterminada. Por defecto, Braze establece automáticamente Arial como fuente alternativa cuando se guardan los ajustes de estilo globales. También tiene la opción de añadir serif o sans serif como opciones para su familia de fuentes predeterminada.

![][11]

Puedes añadir hasta 17 fuentes de reserva. La primera fuente alternativa seleccionada será la que se intente primero. La fuente alternativa sólo se aplicará a las plantillas, campañas de correo electrónico y componentes de Canvas recién creados. La fuente alternativa no se establece automáticamente para los mensajes que se crearon antes de que se especificara la fuente alternativa. Recomendamos encarecidamente seleccionar fuentes alternativas similares a las de los mensajes de correo electrónico para mantener la coherencia de la marca.

## Estilo del título

Aquí puede ajustar los estilos de los títulos de sus correos electrónicos editando el tamaño de la fuente, el color y la alineación del texto. Esto se aplica a la cabecera principal y a la cabecera secundaria. 

![][9]

Opcionalmente, puede anular el estilo predeterminado del tema del editor de arrastrar y soltar. Haga clic en **Anular estilo predeterminado** para aplicar el estilo de título que desee. Esto puede incluir establecer un tipo de letra y un color de enlace diferentes.

## Estilo de párrafo

Para establecer un estilo de párrafo predeterminado, vaya a **Estilos de párrafo**, introduzca el **Tamaño de fuente** y seleccione **Color de fuente** para elegir un color de fuente. También puede ajustar el estilo del bloque para el cuerpo del texto editando los valores **Relleno superior**, **Relleno derecho**, **Relleno inferior** y **Relleno izquierdo**. Esto se aplicará al espaciado alrededor de las cuatro áreas que rodean el bloque de párrafo.

![][7]

## Estilo de la lista

Al añadir listas a su mensajería, la sección **Estilización de listas** crea coherencia en el estilo de sus listas. Esto incluye detalles como: 

- Tamaño de fuente
- Color de fuente
- Peso de fuente
- Altura de la línea
- Alineación
- Dirección del texto
- Espaciado de letras
- Espaciado de los elementos de la lista
- Sangría de los elementos de la lista
- Tipo de lista
- Tipo de estilo de la lista

Puede establecer que el **Tipo de lista** sea numerada o con viñetas. El **Tipo de estilo de lista** proporciona personalización adicional para el estilo de sus listas. Por ejemplo, puede establecer que los tipos de lista sean siempre con viñetas y que cada viñeta sea un cuadrado.  

![][10]

## Estilo de los botones

En la sección **Estilo del botón**, puedes editar los siguientes estilos predeterminados para el botón:
- Color de fondo
- Tamaño de fuente
- Color de fuente
- Radio del borde
- Color del borde
- Peso del borde
- Relleno de botones

![][12]

Al igual que con el resto de secciones de estilo, puede ajustar el estilo del bloque editando los valores de **Relleno superior**, **Relleno derecho**, **Relleno inferior** y **Relleno izquierdo**.

## Anchura de la plantilla de correo electrónico

Mediante la anchura de la plantilla de correo electrónico, puede ajustar y establecer una anchura para mantener la coherencia en todas sus campañas de correo electrónico. 

![][13]

## Anchura del bloque de contenido

También puede establecer el ancho del bloque de contenido en el editor de arrastrar y soltar de correo electrónico. Recomendamos que el ancho del bloque de contenido coincida con el ancho de la plantilla de correo electrónico.

![][14]


[1]: {% image_buster /assets/img_archive/dnd_global_style_settings.png %}
[2]: {% image_buster /assets/img_archive/dnd_basic_styling.png %}
[3]: {% image_buster /assets/img_archive/dnd_custom_font.png %}
[5]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[6]: {% image_buster /assets/img_archive/dnd_heading_styling.png %}
[7]: {% image_buster /assets/img_archive/dnd_paragraph_styling.png %}
[9]: {% image_buster /assets/img_archive/dnd_title_styling.png %}
[10]: {% image_buster /assets/img_archive/dnd_list_styling.png %}
[11]: {% image_buster /assets/img_archive/dnd_fallbacks.png %}
[12]: {% image_buster /assets/img_archive/dnd_button_styling.png %}
[13]: {% image_buster /assets/img_archive/dnd_email_template_width.png %}
[14]: {% image_buster /assets/img_archive/dnd_content_block_width.png %}
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks
