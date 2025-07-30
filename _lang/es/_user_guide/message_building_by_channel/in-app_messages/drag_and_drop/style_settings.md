---
nav_title: Configuración de estilo
article_title: "Configuración del estilo de los mensajes en la aplicación"
description: "Este artículo de referencia cubre las opciones de estilo disponibles al crear un mensaje in-app con el editor de arrastrar y soltar."
page_order: 3
---

# Configuración del estilo de los mensajes de la aplicación

> La experiencia de edición mediante arrastrar y soltar se divide en dos secciones: **Construir** y **Vista previa y prueba**. Este artículo cubre lo que necesitas saber para trabajar dentro de la pestaña **Construir** del editor y asume que ya has [creado un mensaje in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/).

!["Estilos de mensajes" pestaña.]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Estilos de mensaje

En la pestaña **Estilos de mensaje** puedes definir determinados estilos que se aplicarán a todos los bloques relevantes de tu mensaje in-app. Por ejemplo, puede que desee personalizar el tipo de letra de todo el texto o el color de todos los enlaces de su mensaje.

Los estilos de esta sección se utilizan en todas las partes del mensaje, excepto cuando se anulan para un bloque específico. Si su mensaje tiene [varias páginas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page), también puede anular los estilos a nivel de mensaje para páginas individuales, excepto para el tipo de visualización y el ancho máximo. Si intentas aplicar estilos a nivel de página y a nivel de mensaje, el estilo a nivel de página prevalecerá sobre el estilo a nivel de mensaje.

Para facilitar el diseño, recomendamos configurar los estilos a nivel de mensaje antes de personalizar los estilos a nivel de bloque.

Para volver a la pestaña **Estilos de mensajes** en cualquier momento:

- Haga clic en el botón Cerrar X de las propiedades de cada bloque
- Seleccione el contenedor de mensajes, el botón X de cierre de mensajes o el fondo del editor

### Fuentes personalizadas

Aceptamos los siguientes tipos de archivo para fuentes: `.ttf`, `.woff`, `.otf`, y `.woff2`. Para más información, consulta [Archivos de activos]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files).

Puede añadir múltiples variaciones de una familia de fuentes, ya que algunas opciones de estilo pueden no estar disponibles para las fuentes personalizadas. Actualmente, no es posible añadir fuentes a través de una URL.

Para añadir una fuente personalizada:

1. Vaya a la sección **Contenido** de la pestaña **Estilos de mensaje**.
2. Haga clic en **Añadir fuente personalizada**.
3. Sube tu fuente utilizando la biblioteca multimedia. 

{% alert note %}
La fuente a nivel de mensaje sólo se aplicará al mensaje actual y a cualquier mensaje duplicado, pero no a futuras plantillas.
{% endalert %}

## Componentes de los mensajes

![Un GIF que muestra la creación de un mensaje promocional dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

El editor de arrastrar y soltar utiliza dos componentes clave para componer mensajes in-app: **filas** y **bloques**. Todos los bloques deben colocarse en fila.

### Filas

Las filas son unidades estructurales que definen la composición horizontal de una sección del mensaje mediante celdas.

![Filas que puedes añadir en tu mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Cuando se selecciona una fila, puede añadir o eliminar el número de columnas que necesite desde la sección **Personalización de columnas** para colocar diferentes elementos de contenido uno al lado del otro. 

También puede deslizar para ajustar el tamaño de las columnas existentes.

![Ajustar las columnas desde la sección "Personalización de columnas".]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

Como práctica recomendada, formatee las propiedades de las filas y columnas antes de formatear los bloques de las filas. Hay muchos lugares donde se puede ajustar el espaciado y la alineación, por lo que empezar desde la base facilita la edición sobre la marcha.

### Bloques

Los bloques representan distintos tipos de contenido que puedes utilizar en tu mensaje. Arrastre uno dentro de un segmento de fila existente y se ajustará automáticamente a la anchura de la celda.

{% alert tip %}
Antes de añadir bloques, configura [estilos a nivel de](#set-message-level-styles) mensaje para el contenedor de mensajes, la fuente, los colores y cualquier otra cosa que quieras personalizar. A continuación, puede personalizar bloques individuales según sus necesidades. El **botón Cerrar** permanecerá en la parte superior del mensaje para que los usuarios siempre tengan la opción de descartar el mensaje.
{% endalert %}

![Arrastra y suelta cuadros para seleccionar.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Cada bloque tiene sus ajustes, como el control granular del relleno. El panel de la derecha cambia automáticamente a un panel de estilos para el elemento de contenido seleccionado. Para más información, consulta [Propiedades del bloque de editor]({{site.baseurl}}/editor_blocks_dnd_iam/).

A medida que construyes tu mensaje in-app, puedes seleccionar una vista de móvil, tableta o escritorio en la barra de herramientas para previsualizar cómo se verá tu mensaje in-app para tus grupos de usuarios. De este modo se asegurará de que su contenido es receptivo y podrá realizar los ajustes necesarios sobre la marcha.

#### Extender texto

{% multi_lang_include span_text.md %}

## Detalles creativos

### Pantalla completa en pantallas grandes {#fullscreen}

En una tableta o en un navegador de escritorio, un mensaje a pantalla completa aparecerá en el centro de la pantalla de la aplicación. Cualquier modificación de la anchura máxima del mensaje a pantalla completa sólo se aplicará a los dispositivos de escritorio y tabletas. 

![Ejemplo de mensaje dentro de la aplicación a pantalla completa.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Añadir una imagen de fondo

Puedes añadir una imagen al fondo de tu mensaje desde la pestaña **Estilos de mensaje**. 

1. En el área del lienzo, seleccione el contenedor de fondo. Esta es la sección desplazable de su mensaje.
2. En la pestaña **Estilos de mensaje**, active **Imagen de fondo**.
3. Añade una imagen de tu biblioteca multimedia o introduce la URL donde está alojada tu imagen.

{% alert tip %}
Si tienes problemas para seleccionar un bloque determinado, puedes utilizar la flecha hacia arriba de la barra de herramientas en línea del bloque para desplazar el foco hacia arriba, a cada bloque padre.
{% endalert %}

### Añadir líquido

![Icono para añadir personalización de Liquid.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Para añadir [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) a tu mensaje in-app, selecciona <i class="fa-solid fa-circle-plus"></i> **Añadir personalización** en la barra de herramientas del editor. Aquí puede añadir varios tipos de personalización, como atributos predeterminados, atributos de dispositivo, atributos personalizados, etc.

A continuación, tome el fragmento de Liquid generado e insértelo en el mensaje. Después de diseñar y crear tu mensaje in-app, ve a **Vista previa y prueba** para previsualizar tu mensaje.

### Utilizar el redactor de IA

Cuando seleccione un bloque de texto en su mensaje in-app, haga clic en <i class="fa-solid fa-wand-magic-sparkles" title="Redactor AI"></i> en la barra de herramientas del bloque para iniciar el [asistente de redacción con inteligencia artificial]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). El asistente de redacción de textos de IA pasa un breve nombre o descripción del producto a la herramienta de generación de textos GPT3 de OpenAI para generar textos de marketing similares a los humanos para sus mensajes.

{% alert tip %}
Puede ahorrarse algunos clics resaltando el texto dentro del bloque antes de hacer clic en el icono. El texto resaltado se añadirá a la herramienta y se generará una copia inmediatamente.
{% endalert %}

![GIF del redactor de AI.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Restablecer los estilos al ajuste predeterminado

Las propiedades que ha cambiado de su estilo por defecto se marcan con un punto naranja. Para restablecer una propiedad específica a su estilo predeterminado, pase el ratón por encima del campo y seleccione **Restablecer a predeterminado**.

![Punto naranja que restablece el tamaño predeterminado de un texto.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

También puede restablecer todos los estilos de un elemento seleccionado seleccionando el botón <i class="fas fa-paintbrush" title="Copiar o pegar estilos"></i> junto al nombre del panel de propiedades y seleccionando **Restablecer estilos por defecto**.

### Copiar y pegar estilos

Después de realizar cambios en el estilo de un elemento, puede copiar y pegar esos estilos en otro elemento. Al pegar estilos, sólo se aplican las propiedades relevantes para ese elemento.

![Menú desplegable con opción de copiar estilos.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. Con el elemento seleccionado, seleccione <i class="fas fa-paintbrush" title="Copiar o pegar estilos"></i> junto al nombre del panel de propiedades (por ejemplo, si tiene seleccionado un botón, junto a "Propiedades de los botones").
2. Haga clic en **Copiar estilos** y seleccione el elemento en el que desea aplicar el estilo copiado.
3. Seleccione <i class="fas fa-paintbrush" title="Copiar o pegar estilos"></i> de nuevo y seleccione **Pegar estilos**.

#### Atajos de teclado

También puedes utilizar atajos de teclado para copiar y pegar estilos:

| Acción       | Mac                                            | Windows                                           |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| Copiar estilos  | <kbd>⌘</kbd> + <kbd>Shift</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Mayús</kbd> + <kbd>c</kbd> |
| Pegar estilos | <kbd>⌘</kbd> + <kbd>Mayús</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Mayús</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
