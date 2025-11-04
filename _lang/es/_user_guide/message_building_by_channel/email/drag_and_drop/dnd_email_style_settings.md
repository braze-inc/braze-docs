---
nav_title: Configuración global del estilo de correo electrónico
article_title: Configuración global del estilo de correo electrónico
alias: "/dnd/global_style_settings/"
channel: email
page_order: 3
description: "Este artículo de referencia explica cómo establecer la configuración global del estilo de correo electrónico en el editor de arrastrar y soltar para tus campañas y Lienzos."
tool: 
  - Campaigns
  - Canvas
---

# Configuración del estilo global del correo electrónico

> Con la configuración global de estilo, puedes personalizar el aspecto de tus campañas de correo electrónico y de tus Lienzos. Puedes añadir y personalizar un tema predeterminado para tu editor de arrastrar y soltar. Esto incluye la edición de tus estilos para títulos de correo electrónico, texto, botones y mucho más. Utilizar una combinación de estas configuraciones puede ayudar a crear un aspecto coherente en toda tu mensajería electrónica.

Para editar tu configuración global de estilo, ve a **Configuración** > **Preferencias de correo electrónico** > **Preferencias de arrastrar y soltar correo electrónico**. Después de editar los estilos en el editor de arrastrar y soltar de correo electrónico, selecciona **Guardar**. Para personalizar aún más tus campañas de correo electrónico y tus Lienzos, comprueba cómo puedes incorporar [bloques de editor de arrastrar y soltar]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks).

\![Sección Configuración de estilo global de correo electrónico en la pestaña Configuración del editor de arrastrar y soltar correo electrónico.]({% image_buster /assets/img_archive/dnd_global_style_settings.png %})

{% alert note %}
Las actualizaciones realizadas en la configuración de estilo global se aplicarán a todas las campañas de correo electrónico y Lienzos futuros.
{% endalert %} 

## Estilo básico 

En **Estilos básicos**, puedes establecer los colores predeterminados de fondo del correo electrónico y del contenido para tus campañas de correo electrónico y Lienzos. También puedes seleccionar una fuente predeterminada, añadir una personalizada y editar los colores de los enlaces.

\![Opciones básicas de estilo que incluyen opciones para editar los colores de fondo del correo electrónico y del contenido, el nombre predeterminado de la fuente y el color predeterminado del enlace.]({% image_buster /assets/img_archive/dnd_basic_styling.png %}) 

## Fuente personalizada

Con las fuentes personalizadas, puedes añadir manualmente una fuente Web para dar coherencia a la marca en varias plataformas de correo electrónico. Puedes añadir una fuente personalizada para cada sección de estilo personalizado.

### Requisitos

Antes de añadir una fuente personalizada, comprueba que el archivo de la fuente personalizada cumple los siguientes requisitos:

- CORS debe estar habilitado en el servidor que proporciona el archivo de fuentes personalizado. Normalmente lo gestiona tu equipo de TI. 
  - El archivo de fuente personalizado debe tener la cabecera: `Access-Control-Allow-Origin: *`
- La URL del archivo debe apuntar a un archivo CSS (no WOFF ni OTF).
- El nombre de la fuente personalizada debe coincidir con el nombre de la fuente en el archivo CSS.

Ten en cuenta que el proveedor de fuentes personalizadas puede recopilar datos personales de tus destinatarios. Debes revisar las políticas de tu proveedor de fuentes antes de utilizarlas.

### Añadir una fuente personalizada

Para añadir una fuente personalizada, haz lo siguiente:

1. En la sección **Nombre de fuente predeterminado** de **Estilos básicos**, selecciona **Añadir una fuente personalizada**.
2. En el campo **Nombre de** fuente, introduce el mismo nombre de fuente que aparece en tu archivo fuente personalizado. Asegúrate de que este nombre se escribe en mayúsculas y a espacio correcto.
3. Introduce la URL correspondiente para el campo **URL de la fuente**.
4. Comprueba que la vista previa muestra tu fuente personalizada.
5. Selecciona **Guardar** para utilizar la fuente personalizada como fuente predeterminada de tu correo electrónico. 

{% alert important %}
Gmail no admite fuentes personalizadas, por lo que tu fuente personalizada puede mostrarse como una fuente predeterminada del sistema. Para otras plataformas de correo electrónico, comprueba que tu fuente personalizada se muestra correctamente antes de enviar tu mensaje de correo electrónico.
{% endalert %}

Para utilizar otras fuentes personalizadas en tus campañas por correo electrónico, puedes crear una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/) o [bloques de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/) que incluyan la fuente personalizada. Por ejemplo, puedes crear una plantilla de correo electrónico específica diseñada con fuentes festivas personalizadas adaptadas al tema de tu venta. Asegúrate de que la fuente elegida sigue siendo segura para la Web y compatible con tus plataformas de correo electrónico.

### Fuente alternativa

Las fuentes alternativas se utilizan para el título, la cabecera y el cuerpo del texto cuando el proveedor de buzón de entrada o el sistema operativo no admiten tu fuente predeterminada. Por predeterminado, Braze establece automáticamente Arial como fuente alternativa cuando se guarda la configuración de estilo global. También tienes la opción de añadir serif o sans serif como opciones para tu familia de fuentes predeterminada.

Un ejemplo de "Arial" como fuente alternativa con "Sans-serif" como familia de fuentes.]({% image_buster /assets/img_archive/dnd_fallbacks.png %})

Puedes añadir hasta 17 fuentes alternativas. La primera fuente alternativa seleccionada será la que se intente primero. La fuente alternativa sólo se aplicará a las plantillas recién creadas, a las campañas por correo electrónico y a los componentes de Canvas. La fuente alternativa no se establece automáticamente para los mensajes que se crearon antes de especificar la fuente alternativa. Te recomendamos encarecidamente que elijas fuentes alternativas similares a las de tu mensajería electrónica para mantener la coherencia de tu marca.

## Estilo del título

Aquí puedes ajustar los estilos de los títulos de tus correos electrónicos editando el tamaño de la fuente, el color de la fuente y la alineación del texto. Esto se aplica a la cabecera principal y a la cabecera secundaria. 

\![Título Configuración del estilo para un encabezado principal alineado al centro y un encabezado secundario.]({% image_buster /assets/img_archive/dnd_title_styling.png %})

Opcionalmente, puedes anular el estilo predeterminado del tema de tu editor de arrastrar y soltar. Selecciona **Anular estilo predeterminado** para aplicar el estilo de título que elijas. Esto puede incluir establecer un tipo de letra y un color de enlace diferentes.

## Estilo de párrafo

Para establecer un estilo de párrafo predeterminado, ve a **Estilo de párrafo**, introduce el **Tamaño de fuente** y selecciona **Color de fuente** para elegir un color de fuente. También puedes ajustar el estilo del bloque para el cuerpo del texto editando los valores **Relleno superior**, **Relleno derecho**, **Relleno inferior** y **Relleno izquierdo**. Esto se aplicará al espaciado alrededor de las cuatro áreas que rodean el bloque de párrafo.

\![Configuración de estilo de párrafo para texto con fuente de 14pt.]({% image_buster /assets/img_archive/dnd_paragraph_styling.png %})

## Estilo de la lista

Al añadir listas a tu mensajería, la sección **Estilización de listas** crea coherencia en el estilo de tus listas. Esto incluye detalles como 

- Tamaño de letra
- Color de fuente
- Peso de la fuente
- Altura de la línea
- Alineación
- Dirección del texto
- Espaciado entre letras
- Espaciado de los elementos de la lista
- Sangría del elemento de la lista
- Tipo de lista
- Tipo de estilo de lista

Puedes configurar el **Tipo de lista** para que sea numerada o con viñetas. El **Tipo de Estilo de Lista** proporciona una personalización adicional para el estilo de tus listas. Por ejemplo, puedes establecer que los tipos de lista sean siempre con viñetas y que cada viñeta sea un cuadrado.  

\![Lista Configuración del estilo de una lista con viñetas.]({% image_buster /assets/img_archive/dnd_list_styling.png %})

## Estilo de los botones

En la sección **Estilo del** botón, puedes editar los siguientes estilos predeterminados para el botón:
- Color de fondo
- Tamaño de letra
- Color de fuente
- Radio del borde
- Color del borde
- Peso del borde
- Relleno del botón

\![Botón Configuración del estilo de un botón rectangular con fondo azul.]({% image_buster /assets/img_archive/dnd_button_styling.png %})

Como en todas las demás secciones de estilo, puedes ajustar el estilo del bloque editando los valores de **Relleno superior**, **Relleno derecho**, **Relleno inferior** y **Relleno izquierdo**.

## Anchura de la plantilla de correo electrónico

Con la anchura de la plantilla de correo electrónico, puedes ajustar y establecer una anchura para que sea coherente en todas tus campañas de correo electrónico. 

\![Anchura de la plantilla de correo electrónico ajustada a 600px.]({% image_buster /assets/img_archive/dnd_email_template_width.png %})

## Anchura del bloque de contenido

Esta configuración será la preconfigurada para todos los futuros Bloques de contenido. Los bloques de contenido existentes no se actualizarán. Puedes establecer que todos los Bloques de contenido se fijen al 100%, respetando la anchura en la que se inserta un Bloque de contenido, o definir un valor de píxel específico.

Te recomendamos que hagas coincidir la anchura del bloque de contenido con la anchura de la plantilla de correo electrónico.

\![Anchura del bloque de contenido ajustada a 600px.]({% image_buster /assets/img_archive/dnd_content_block_width_update.png %})
