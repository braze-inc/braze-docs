---
nav_title: Configuración del estilo
article_title: "Configuración del estilo de los mensajes dentro de la aplicación"
description: "Este artículo de referencia cubre las opciones de estilo disponibles al crear un mensaje dentro de la aplicación con el editor de arrastrar y soltar."
page_order: 3
---

# Configuración del estilo de mensajería dentro de la aplicación

> La experiencia de edición arrastrando y soltando se divide en dos secciones: **Compilación** y **vista previa & Prueba**. Este artículo cubre lo que necesitas saber para trabajar dentro de la pestaña **Construir** del editor y asume que ya has [creado un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/).

\![ pestaña "Estilos de mensajes".]({% image_buster /assets/img_archive/dnd_iam_message_styles.png %}){: style="float:right;max-width:25%;margin-left:15px;max-width:30%"}

## Estilos a nivel de mensaje

Puedes configurar determinados estilos para que se apliquen a todos los bloques relevantes de tu mensaje dentro de la aplicación desde la pestaña **Estilos de mensaje**. Por ejemplo, puede que quieras personalizar el tipo de letra de todo el texto o el color de todos los enlaces de tu mensaje.

Los estilos de esta sección se utilizan en todas las partes de tu mensaje, excepto cuando los anulas para un bloque específico. Si tu mensaje tiene [varias páginas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page), también puedes anular los estilos a nivel de mensaje para páginas individuales, excepto para el tipo de visualización y la anchura máxima.

Para facilitar el diseño, te recomendamos que configures los estilos a nivel de mensaje antes de personalizar los estilos a nivel de bloque.

Para volver a la pestaña **Estilos de mensaje** en cualquier momento:

- Haz clic en el botón cerrar X en las propiedades individuales de los bloques
- Selecciona el contenedor de mensajes, el botón X de cierre de mensajes o el fondo del editor

### Fuentes personalizadas

Aceptamos los siguientes tipos de archivo para fuentes: `.ttf`, `.woff`, `.otf`, y `.woff2`. Para más información, consulta [Ficheros de activos]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/html_in-app_messages#asset-files).

Puedes añadir múltiples variaciones de una familia de fuentes, ya que algunas opciones de estilo pueden no estar disponibles para las fuentes personalizadas. Actualmente no podemos añadir fuentes mediante URL.

Para añadir una fuente personalizada:

1. Ve a la sección **Contenido** de la pestaña **Estilos de mensaje**.
2. Haz clic en **Añadir fuente personalizada**.
3. Sube tu fuente utilizando la biblioteca multimedia. 

{% alert note %}
La fuente a nivel de mensaje sólo se aplicará al mensaje actual y a cualquier mensaje duplicado, pero no a futuras plantillas.
{% endalert %}

## Componentes de los mensajes

GIF que muestra la creación de un mensaje promocional dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_create.gif %})

El editor de arrastrar y soltar utiliza dos componentes clave para componer mensajes dentro de la aplicación: **filas** y **bloques**. Todos los bloques deben colocarse en fila.

### Cerrar botón x

Para los mensajes dentro de la aplicación Modal y Pantalla completa, puedes personalizar el botón de cierre que se muestra como <i class="fa-solid fa-xmark"></i> en la esquina superior derecha de tu mensaje. Las opciones de personalización incluyen la posición del botón, el tamaño, el color de relleno, el color de fondo, el estilo del borde y el radio del borde.

Opciones para personalizar el botón Cerrar x en los mensajes dentro de la aplicación, incluidos el tamaño del botón, el color de relleno, el color de fondo, el estilo del borde y el radio del borde.]({% image_buster /assets/img_archive/close_x_button.png %}){: style="max-width:40%"}

### Estilo Span

Añadir un estilo personalizado al texto de los mensajes dentro de la aplicación habilita el uso de diferentes colores, fuentes y tamaños de texto. El estilo Span proporciona a tus usuarios una experiencia más atractiva y visualmente más atractiva, llamando su atención sobre la información clave y mejorando la claridad general del mensaje.

\![Opción que se muestra al resaltar texto en un mensaje dentro de la aplicación. Un pequeño icono de pincel muestra que puedes envolver con palmo para darle estilo.]({% image_buster /assets/img_archive/span_1.png %}){: style="max-width:40%"}

\![Panel lateral para "Propiedades de Span" que permite al usuario final personalizar la familia de fuentes, el peso de la fuente, el tamaño de la fuente, el espaciado entre letras y el color del texto.]({% image_buster /assets/img_archive/span_2.png %}){: style="max-width:40%"}

### Filas

Las filas son unidades estructurales que definen la composición horizontal de una sección del mensaje mediante celdas.

\![Filas que puedes añadir en tu mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/dnd_iam_rows.png %}){: style="max-width:40%"}

Cuando se selecciona una fila, puedes añadir o eliminar el número de columnas que necesites en la sección **Personalización de columnas** para colocar diferentes elementos de contenido uno junto a otro. 

También puedes deslizar para ajustar el tamaño de las columnas existentes.

\![Ajustar las columnas desde la sección "Personalización de columnas".]({% image_buster /assets/img_archive/dnd_iam_column_customization.gif %}){: style="max-width:40%"}

Como práctica recomendada, da formato a las propiedades de las filas y columnas antes de dar formato a los bloques de las filas. Hay muchos lugares donde puedes ajustar el espaciado y la alineación, por lo que empezar desde la base facilita la edición sobre la marcha.

### Bloquea

Los bloques representan distintos tipos de contenido que puedes utilizar en tu mensaje. Arrastra uno dentro de un segmento de fila existente y se ajustará automáticamente a la anchura de la celda.

{% alert tip %}
Antes de añadir bloques, configura [estilos a nivel de mensaje](#set-message-level-styles) para el contenedor de mensajes, la fuente, los colores y cualquier otra cosa que quieras personalizar. Luego puedes personalizar bloques individuales según necesites. El **botón Cerrar** permanecerá en la parte superior de tu mensaje para que los usuarios siempre tengan la opción de descartar el mensaje.
{% endalert %}

\![Arrastra y suelta cuadros para seleccionar.]({% image_buster /assets/img_archive/dnd_iam_editor_blocks.png %}){: style="max-width:40%"}

Cada bloque tiene sus configuraciones, como el control granular del relleno. El panel de la derecha cambia automáticamente a un panel de estilo para el elemento de contenido seleccionado. Para más información, consulta [Propiedades del bloque de editor]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/drag_and_drop_editor_blocks/?sdktab=in-app%20messages#inappmessages_properties).

Mientras creas tu mensaje dentro de la aplicación, puedes seleccionar una vista de móvil, tableta o escritorio en la barra de herramientas para obtener una vista previa del aspecto que tendrá tu mensaje dentro de la aplicación para tus grupos de usuarios. Esto garantizará que tu contenido sea receptivo, y podrás hacer los ajustes necesarios sobre la marcha.

## Detalles creativos

### Pantalla completa en pantallas grandes {#fullscreen}

En una tableta o navegador de escritorio, un mensaje dentro de la aplicación a pantalla completa se situará en el centro de la pantalla de la aplicación. Cualquier modificación de la anchura máxima del mensaje a pantalla completa sólo se aplicará a los dispositivos de tableta y escritorio. 

\![Ejemplo de mensaje dentro de la aplicación a pantalla completa.]({% image_buster /assets/img_archive/dnd_iam_fullscreen_example.png %}){: style="border:none"}

### Añadir una imagen de fondo

Puedes añadir una imagen al fondo de tu mensaje desde la pestaña **Estilos de mensaje**. 

1. En el área del lienzo, selecciona el contenedor de fondo. Esta es la sección desplazable de tu mensaje.
2. En la pestaña **Estilos de mensaje**, activa **Imagen de fondo**.
3. Añade una imagen de tu biblioteca multimedia o introduce la URL donde está alojada tu imagen.

{% alert tip %}
Si tienes problemas para seleccionar un bloque determinado, puedes utilizar la flecha hacia arriba de la barra de herramientas en línea del bloque para desplazar el foco hacia arriba, a cada bloque padre.
{% endalert %}

### Añadir Liquid

Icono para añadir personalización de Liquid.]({% image_buster /assets/img_archive/dnd_iam_liquid.png %}){: style="float:right;max-width:25%;margin-left:15px"}

Para añadir [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) a tu mensaje dentro de la aplicación, selecciona <i class="fa-solid fa-circle-plus"></i> **Añadir personalización** en la barra de herramientas del editor. Aquí puedes añadir varios tipos de personalización, como atributos predeterminados, atributos de dispositivo, atributos personalizados, etc.

A continuación, toma el fragmento de código Liquid generado e insértalo en tu mensaje. Después de diseñar y crear tu mensaje dentro de la aplicación, ve a **Vista previa & Prueba** para previsualizar tu mensaje.

### Utilizar el redactor AI

Cuando se selecciona un bloque de texto en tu mensaje dentro de la aplicación, haz clic en <i class="fa-solid fa-wand-magic-sparkles" title="Redactor AI"></i> en la barra de herramientas del bloque para iniciar el [asistente de redacción con IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). El asistente de redacción de IA pasa un breve nombre o descripción del producto a la herramienta de generación de textos GPT3 de OpenAI para generar textos de marketing similares a los humanos para tu mensajería.

{% alert tip %}
Puedes ahorrarte unos cuantos clics resaltando el texto dentro del bloque antes de hacer clic en el icono. El texto resaltado se añadirá a la herramienta, y se generará una copia inmediatamente.
{% endalert %}

\![GIF del redactor publicitario de la IA.]({% image_buster /assets/img_archive/dnd_iam_ai_copywriter.gif %})

### Restablecer estilos predeterminados

Las propiedades que has cambiado de su estilo predeterminado se marcan con un punto naranja. Para restablecer el estilo predeterminado de una propiedad concreta, pasa el ratón por encima del campo y selecciona **Restablecer predeterminado**.

\![Punto naranja que restablece el tamaño predeterminado de un texto.]({% image_buster /assets/img_archive/dnd_iam_reset_styles.gif %}){: style="max-width:45%"}

También puedes restablecer todos los estilos de un elemento seleccionado seleccionando el botón <i class="fas fa-paintbrush" title="Botón Copiar o pegar estilos"></i> junto al nombre del panel de propiedades y seleccionando **Restablecer estilos predeterminados**.

### Copiar y pegar estilos

Después de hacer cambios en el estilo de un elemento, puedes copiar y pegar esos estilos en otro elemento. Al pegar estilos, sólo se aplican las propiedades relevantes para ese elemento.

Menú desplegable con opción de copiar estilos.]({% image_buster /assets/img_archive/dnd_iam_copypaste_styles.png %}){: style="float:right;margin-left:15px;max-width:35%"}

1. Con el elemento seleccionado, selecciona <i class="fas fa-paintbrush" title="Copiar o pegar estilos"></i> junto al nombre del panel de propiedades (Por ejemplo, si tienes seleccionado un botón, junto a "Propiedades del botón").
2. Haz clic en **Copiar estilos** y selecciona el elemento donde quieras aplicar el estilo copiado.
3. Selecciona <i class="fas fa-paintbrush" title="Copiar o pegar estilos"></i> de nuevo y elige **Pegar estilos**.

#### Atajos de teclado

También puedes utilizar atajos de teclado para copiar y pegar estilos:

| Acción       | Mac                                            | Windows                                           |
| ------------ | ---------------------------------------------- | ------------------------------------------------- |
| Copiar estilos  | <kbd>⌘</kbd> + <kbd>Mayús</kbd> + <kbd>c</kbd> | <kbd>Ctrl</kbd> + <kbd>Mayús</kbd> + <kbd>c</kbd> |
| Pegar estilos | <kbd>⌘</kbd> + <kbd>Mayús</kbd> + <kbd>v</kbd> | <kbd>Ctrl</kbd> + <kbd>Mayús</kbd> + <kbd>v</kbd> |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
