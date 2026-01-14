---
nav_title: Crear un correo electrónico
article_title: Crear un correo electrónico con arrastrar y soltar
alias: "/dnd/overview/"
channel: email
page_order: 0
description: "Este artículo explica cómo configurar y utilizar correctamente el editor de arrastrar y soltar para mensajes de correo electrónico."
tool:
- Campaigns
- Canvas
---

# Crear un correo electrónico con arrastrar y soltar

> Utilizando el editor de arrastrar y soltar, puedes crear mensajes de correo electrónico completamente personalizados para campañas o Lienzos, todo ello sin utilizar HTML para construir el cuerpo de tu correo electrónico.

## Sobre el editor

El editor de arrastrar y soltar utiliza [Contenido](#content) y [Filas](#rows) como los dos componentes clave para simplificar tu flujo de trabajo, sin uso adicional de HTML.

<table style="width: 100%; table-layout: fixed;">
    <tr>
        <th style="width: 50%;">Contenido</th>
        <th style="width: 50%;">Filas</th>
    </tr>
    <tr>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_content.png %}" alt="La pestaña &quot;Filas&quot; que incluye diferentes combinaciones estructurales para el diseño de tu correo electrónico." style="max-width: 100%; height: auto;">
        </td>
        <td style="text-align: center;">
            <img src="{% image_buster /assets/img/dnd/dnd_rows.png %}" alt="La pestaña &quot;Contenido&quot; que incluye bloques básicos, multimedia y avanzados" style="max-width: 100%; height: auto;">
        </td>
    </tr>
</table>
{: .reset-td-br-1 role="presentation"}

### Contenido

**El contenido** incluye una serie de mosaicos que representan distintos tipos de contenido que puedes utilizar en tu mensaje. Están organizados en tres categorías: básicos, medios y avanzados. 

{% tabs %}
{% tab Basic %}

Los bloques básicos son la base de tu correo electrónico. Utilizando estos bloques, puedes añadir cualquiera de los siguientes elementos en el cuerpo de tu correo electrónico:

- Título
- Párrafo
- Lista
- Botón
- Divisor
- Espaciador

{% endtab %}
{% tab Media %}

Con los bloques de contenido multimedia, puedes añadir diferentes contenidos visuales como imágenes, videos, iconos y enlaces de redes sociales e iconos personalizables.

{% endtab %}
{% tab Advanced %}

Aunque el editor de arrastrar y soltar simplifica tu flujo de trabajo con estos bloques, también puedes utilizar bloques avanzados para insertar HTML o añadir un menú al cuerpo de tu correo electrónico. Ten en cuenta que el uso de tu propio HTML puede afectar a la forma en que se muestra el mensaje.

{% endtab %}
{% endtabs %}

### Filas

**Las filas** son unidades estructurales que definen la composición horizontal de una sección del mensaje mediante columnas. Puedes vaciar filas o [bloques de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). Utilizar más de una columna te permite poner diferentes elementos de contenido uno al lado del otro. De este modo, puedes añadir a tu mensaje todos los elementos estructurales que necesites, independientemente de la plantilla que hayas seleccionado al empezar.

#### Estilo de las tarjetas

**El Estilo de tarjeta** es una propiedad de fila que te permite añadir espaciado entre columnas y redondear sus esquinas. Con el formato de tarjeta, puedes crear diseños visualmente más atractivos que te ayuden a destacar tus contenidos más importantes, como características de nuevos productos, testimonios, ofertas especiales, actualizaciones de noticias y mucho más.

## Utilizar el editor de arrastrar y soltar

¿No estás seguro de si tu mensaje de correo electrónico debe enviarse utilizando una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y sencillas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

Después de haber seleccionado dónde construir tu mensaje, vamos a sumergirnos en los pasos para crear un correo electrónico arrastrando y soltando.

### Paso 1: Selecciona tu plantilla

Después de seleccionar el editor de arrastrar y soltar como tu experiencia de edición, puedes elegir:

- Empieza con una plantilla en blanco.
- Utiliza una plantilla prediseñada de correo electrónico Braze de arrastrar y soltar.
- Utiliza una plantilla de correo electrónico guardada de arrastrar y soltar.

{% alert note %}
Para utilizar una plantilla HTML personalizada existente o plantillas creadas por terceros, debes volver a crear la plantilla yendo a **Plantillas** > **Plantillas de correo electrónico** y seleccionando **Editor de arrastrar y soltar** como experiencia de edición.
{% endalert %}

También puedes acceder a todas las plantillas desde la sección **Plantillas**.

Tras seleccionar tu plantilla, verás un resumen de tu correo electrónico en **Variantes de correo electrónico**, que incluye la información de envío y el cuerpo del correo. 

A continuación, selecciona **Editar cuerpo del correo electrónico** para empezar a diseñar la estructura del correo electrónico en el editor de arrastrar y soltar. 

\![La sección "Variantes de correo electrónico" con un cuerpo de correo electrónico de ejemplo.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### Paso 2: Crea tu correo electrónico

La experiencia de edición arrastrando y soltando se divide en tres secciones: **Envío de configuración**, **contenido** y **vista previa & Prueba**. La magia de construir el cuerpo de tu correo electrónico ocurre en la sección **Contenido**. Antes de crear tu correo electrónico, es importante comprender los componentes clave que guían tu experiencia de creación de correos electrónicos. Si necesitas revisar, consulta [Acerca del editor](#about-the-editor).

Cuando estés listo, utiliza los bloques de contenido de arrastrar y soltar para construir tu correo electrónico.

1. Selecciona el panel **Filas**. Arrastra y suelta las configuraciones de las filas en el editor principal. Esto mapeará el diseño del contenido de tu correo electrónico.
- Ten en cuenta que las nuevas configuraciones deben arrastrarse a la parte superior o inferior de una sección existente.
- Cuando seleccionas la configuración de una fila, aparece la configuración de **Propiedades de fila** para personalizar aún más los colores de fondo de las filas, las imágenes y los tamaños personalizados de las columnas.
2. Selecciona el panel **Contenido**. Arrastra y suelta los mosaicos de contenido que desees en los componentes de la fila.
- También puedes arrastrar cualquiera de las fichas de **Contenido** al editor principal. Esto crea una fila para la ficha.
- Puedes refinar aún más el mosaico seleccionándolo y ajustando los campos en **Propiedades de contenido** y **Opciones de bloque**. Esto incluye editar el espaciado entre letras, el relleno, la altura de línea y mucho más.

Consulta [Otras personalizaciones](#other-customizations) para conocer otras formas de personalizar aún más tu correo electrónico arrastrando y soltando.

Mientras creas tu correo electrónico, puedes alternar entre una vista de escritorio y una vista móvil para obtener una vista previa del aspecto que tendrá tu mensajería electrónica para tus grupos de usuarios. Esto comprobará que tu contenido es receptivo, y podrás hacer los ajustes necesarios sobre la marcha.

{% alert tip %}
¿Necesitas ayuda para crear un texto impresionante? Prueba a utilizar el [asistente de redacción AI]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduce el nombre o la descripción de un producto y la IA generará textos de marketing similares a los humanos para que los utilices en tus mensajes.

\![Botón Copywriter, situado en el panel Contenido junto a Configuración de estilo en el editor de arrastrar y soltar.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Paso 3: Añade tu información de envío

Una vez que hayas terminado de diseñar y crear tu mensaje de correo electrónico, es hora de añadir tu información de envío en la sección **Configuración de envío**.

1. En **Información de envío**, selecciona un correo electrónico como **Nombre para mostrar de + Dirección**. También puedes personalizarlo seleccionando **Personalizar desde Nombre para mostrar + Dirección**.
2. Selecciona un correo electrónico como **dirección de respuesta**. También puedes personalizarlo seleccionando **Personalizar dirección de respuesta a**.
3. A continuación, selecciona un correo electrónico como **Dirección CCO** para que tu correo electrónico sea visible para esta dirección.
4. Añade una línea del asunto a tu correo electrónico. Opcionalmente, también puedes añadir un preencabezado y un espacio en blanco después del preencabezado.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Aparecerá una vista previa en el panel de la derecha con la información de envío que hayas añadido. Esta información también se puede actualizar accediendo a **Configuración** > **Preferencias de correo electrónico** > **Configuración de envío**.

#### Personalización del encabezamiento de tu correo electrónico (avanzado)

En **Configuración de envío**, puedes añadir personalización para las cabeceras y los extras del correo electrónico, lo que te permite enviar datos adicionales a otros proveedores de servicios de correo electrónico. La personalización del encabezamiento de un correo electrónico, como incluir el nombre del destinatario, también puede contribuir a la probabilidad de que abran tu correo electrónico.

{% alert note %}
La funcionalidad avanzada aparecerá en el compositor de la campaña o Canvas. En la funcionalidad avanzada, puedes modificar tu configuración CSS en línea e introducir un encabezado o pares clave-valor adicionales (si están configurados).
{% endalert %}

### Paso 4: Prueba tu correo electrónico

Después de añadir tu información de envío, es hora de probar finalmente tu correo electrónico. 

Ve a la sección **Vista previa y Prueba**. Aquí tienes la opción de obtener una vista previa de tu correo electrónico como usuario o de enviar un mensaje de prueba. Esta sección también incluye [la Visión de la Bandeja de Entrada]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/), que te permite comprobar que tu correo electrónico se ha mostrado correctamente en diferentes clientes móviles y Web.

{% alert tip %}
También puedes utilizar el alternador de **vista previa en modo oscuro** del panel de vista previa para ver el cuerpo de tu correo electrónico en modo oscuro y ajustar tu correo electrónico según sea necesario.
{% endalert %}

Dado que puedes ver tres versiones distintas del mismo correo electrónico en el editor real, en Inbox Vision y como correo de prueba real, es importante alinear los detalles en todas tus plataformas.

#### Vista previa y envío de prueba
 
En la pestaña **Vista previa como usuario**, puedes seleccionar los siguientes tipos de usuario para previsualizar tu mensaje.

- **Usuario aleatorio:** Braze seleccionará aleatoriamente un usuario de la base de datos y previsualizará el correo electrónico en función de sus atributos o de la información del evento.
- **Selecciona Usuario:** Puedes seleccionar un usuario concreto en función de su dirección de correo electrónico o ID externo. El correo electrónico tendrá una vista previa basada en los atributos de ese usuario y en la información del evento
- **Usuario personalizado:** Puedes personalizar un usuario. Braze ofrecerá entradas para todos los atributos y eventos disponibles. Puedes introducir cualquier información que quieras ver en la vista previa del correo electrónico.

{% alert note %}
El usuario aleatorio puede o no formar parte de tus criterios de segmentación. La segmentación se selecciona después, por lo que Braze desconoce tu audiencia objetivo en este momento.
{% endalert %}

También puedes seleccionar **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa compartible que muestre el aspecto que tendrá el correo electrónico para un usuario cualquiera. El enlace durará siete días antes de que sea necesario regenerarlo. 

Ten en cuenta que cualquier modificación realizada en una plantilla de correo electrónico no se reflejará en un enlace generado previamente. Tendrás que generar una nueva vista previa del enlace para ver las modificaciones.

\![Vista previa por correo electrónico con un botón para "Copiar enlace de vista previa" y copiar el enlace generado.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Utiliza Inbox Vision

Inbox Vision te permite ver tus campañas de correo electrónico desde la perspectiva de los clientes de correo electrónico y los dispositivos móviles. Para probar tu mensaje de correo electrónico utilizando **Visión de Bandeja de Entrada**, selecciona **Visión de Bandeja de Entrada** en la sección **Vista previa de prueba & ** y selecciona **Ejecutar Visión de Bandeja de Entrada**.

{% alert tip %}
Las imágenes de fondo en los mensajes de correo electrónico a veces pueden provocar la aparición de líneas blancas o desconexiones entre las imágenes, por lo que es importante que pruebes y compruebes los detalles de tu mensaje de correo electrónico.
{% endalert %}

Después de utilizar el editor de arrastrar y soltar para diseñar y crear tu mensaje de correo electrónico, continúa [construyendo]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) el resto de tu campaña o Canvas.

{% details About the updated HTML engine %}
Se ha optimizado y actualizado el motor subyacente que produce HTML a partir del editor de arrastrar y soltar, lo que se ha traducido en ventajas relacionadas con la compresión y el renderizado de archivos HTML.

Se ha reducido el tamaño medio de nuestra huella de datos HTML exportados, lo que se traduce en una carga y representación más rápidas, menos recortes en los móviles y un menor consumo de ancho de banda.

La representación HTML ha mejorado gracias a las siguientes actualizaciones que minimizan el número de comentarios condicionales y consultas de medios CSS. Como resultado, los archivos HTML son más pequeños y se codifican con mayor eficacia.
- Migración de un diseño basado en elementos `<div>` a una base de código con formato estándar `<table>` 
- [Los bloques de editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) se han codificado de nuevo para ser más concisos
- El código HTML final se comprime para eliminar los espacios en blanco entre etiquetas
- Los separadores transparentes se convierten automáticamente en relleno de contenido
{% enddetails %}

## Otras personalizaciones

A medida que sigas creando correos electrónicos arrastrando y soltando, puedes personalizar aún más el cuerpo de cada correo electrónico utilizando una combinación de estos detalles creativos para captar la atención y el interés de tu audiencia por tu mensaje.

{% alert tip %}
Puedes crear un tema personalizado para tu editor de arrastrar y soltar utilizando [la configuración global de estilo]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/).
{% endalert %}

### Imágenes de ancho automático

Las imágenes añadidas a tu correo electrónico se establecerán automáticamente en **Ancho automático**. Para ajustar esta configuración, alterna entre desactivar **Ancho automático** y ajustar el porcentaje de ancho según sea necesario.

\![Opción de anchura automática en la pestaña Contenido del editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd1.png %})

### Estratificación de colores

Utilizando la superposición de colores, puedes cambiar el color del fondo del correo electrónico, del área de contenido y de los distintos componentes del contenido. El orden de los colores de delante hacia atrás es: color del componente de contenido, color de fondo del área de contenido y color de fondo.

\![Ejemplo de superposición de colores en el editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd2.png %})

### Relleno de contenido

\![Opciones de bloque para el editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Para ajustar el relleno, desplázate hasta **Opciones de bloque** y selecciona **Más opciones**. Puedes ajustar el relleno para que tu correo electrónico tenga el aspecto adecuado.

### Contenido de fondo

Puedes añadir una imagen de fondo a la configuración de tus filas, lo que te permitirá incorporar más diseño y contenido visual a tu campaña de correo electrónico.

### Atributo de lengua

Puedes configurar el atributo de idioma yendo a la pestaña **Configuración** y seleccionando el idioma deseado. También puedes dirigirte al atributo de usuario {%raw%} `{{${language}}}` {%endraw%} si el mensaje va dirigido a usuarios con valores de idioma dinámicos.

\![Configurar el valor de "Idioma" de un correo electrónico.]({% image_buster /assets/img/dnd/language_setting_dnd.png %}){: style="max-width:70%;"}

### Personalización

Opciones para añadir personalización al editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Basic Liquid es compatible con el editor de arrastrar y soltar de correo electrónico. Para añadir personalización a tu correo electrónico:

1. Selecciona **Personalización** en la sección **Contenido**. 
2. Selecciona el tipo de personalización. Esto incluye atributos predeterminados (estándar), atributos de dispositivo, atributos personalizados, etc. 
3. Busca el atributo que hay que añadir.
4. Copia el fragmento de código de Liquid que has generado y pégalo en el cuerpo de tu correo electrónico.

La personalización Liquid no es compatible con los bloques de imagen y los campos de tipo enlace de botón. 

#### Imágenes dinámicas

Puedes incluir imágenes dinámicas en tu mensajería electrónica incluyendo Liquid en tu atributo de fuente de imagen. Por ejemplo, en lugar de una imagen estática, puedes insertar {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} como URL de la imagen para incluir el nombre de pila de un usuario en la imagen. Esto ayuda a personalizar tus envíos electrónicos a cada usuario.

### Dirección del texto

Al redactar tu mensaje, puedes alternar la dirección del texto entre izquierda-derecha y derecha-izquierda seleccionando el botón **Dirección del texto** correspondiente. Puedes utilizar esta opción cuando crees mensajes en idiomas como el árabe y el hebreo.

Menú del editor de arrastrar y soltar con botón para alternar la alineación del texto entre derecha-izquierda e izquierda-derecha.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

El aspecto final de los mensajes de derecha a izquierda depende en gran medida de cómo los presten los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha [a]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

### HTML

#### Atributos HTML a los enlaces

\![La sección "Atributos" con el atributo "clicktracking" desactivado para un enlace.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Cuando utilices enlaces, botones, imágenes y videos en el editor de arrastrar y soltar, selecciona **Añadir nuevo atributo** en **Atributos**, en la sección **Contenido**, para añadir información adicional a las etiquetas HTML de los correos electrónicos. Esto puede ser especialmente útil para la personalización, segmentación y estilización de mensajes.

Un caso de uso común es insertar un atributo en tu etiqueta de anclaje para desactivar el seguimiento de clics al enviar a través de Braze.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

Otro caso de uso común es marcar enlaces específicos como enlaces universales. Los enlaces universales son enlaces que redirigen a tu aplicación, proporcionando a tus usuarios una experiencia integrada.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` (hay que configurar una [sub-ruta personalizada](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) )

Para configurar los enlaces [universales]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/), consulta [Enlaces universales y Enlaces de aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).

Alternativamente, puedes integrarte con uno de nuestros socios de atribución, como [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) o [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking), para gestionar los enlaces universales.

Por último, hay disponibles atributos predefinidos para ayudar a que tu mensaje sea accesible. Obtén más información en nuestro artículo dedicado [Construir mensajes accesibles en Braze]({{site.baseurl}}/help/accessibility).

#### Etiquetas de cabecera personalizadas

Utiliza las etiquetas `<head>` para añadir CSS y metadatos en tu mensaje de correo electrónico. Por ejemplo, puedes utilizar estas etiquetas para añadir una hoja de estilos o un favicon. Liquid es compatible con las etiquetas `<head>`.

Todo lo que se añada fuera de las etiquetas `<head>` se añadirá después de la etiqueta `<body>` en tu correo electrónico. Esto significa que el contenido añadido se mostrará en el correo electrónico.

##### Etiquetas y atributos permitidos por etiqueta

| Nombre de la etiqueta | Descripción | Ejemplo |
| --- | --- | --- |
| `base` | Especifica la URL base para todas las URL relativas del mensaje. | `<base href="https://example.com" target="_blank">` |
| `link`| Define las relaciones entre el mensaje y los recursos externos. | `<link href="styles.css" rel="stylesheet" type="text/css">` |
| `meta` | Proporciona metadatos como la descripción de la página o palabras clave. | `<meta name="description" content="Free Web tutorials">` |
| `style` | Incorpora estilos CSS internos. | `<style type="text/css" media="screen">body { font-size: 16px; }</style>` |
| `title` | Establece el título del documento que se muestra en las pestañas del navegador. | `<title>StyleRyde</title>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

| Etiqueta | Atributo | Descripción | Ejemplo |
| --- | --- | --- | --- |
| `base` | `href` | URL base a utilizar para las URL relativas. | ```<base href="https://braze.com">``` |
| `base` | `target`| Objetivo predeterminado para todos los hipervínculos y formularios. | ```<base target="_blank">``` |
| `link` | `href` | URL del recurso externo. | ```<link href="style.css">``` |
| `link` | `rel` | Define las relaciones entre el mensaje actual y el vinculado. | ```<link rel="stylesheet">``` |
| `link` | `type` | Tipo de recurso enlazado. | ```<link type="text/css">``` |
| `link` | `sizes` | Especifica el tamaño de los iconos. | ```<link rel="icon" sizes="32x32" href="favicon-32.png">``` |
| `link` | `media` | Especifica el soporte o dispositivo al que se aplican los estilos. | ```<link rel="stylesheet" media="screen" href="style.css">``` |
| `meta` | `name` | Establece el título del documento que se muestra en las pestañas del navegador. | ```<meta name="viewport" content="width=device-width, initial-scale=1">``` |
| `meta` | `content` | Establece el título del documento que se muestra en las pestañas del navegador. | ```<meta name="description" content="Page about our newest products">``` |
| `meta` | `charset` | Declara la codificación de caracteres. | ```<meta charset="UTF-8">``` |
| `meta` | `property` | Establece el título del documento que se muestra en las pestañas del navegador. | ```<meta property="og:title" content="Website title">``` |
| `style` | `type` | Tipo MIME del contenido del estilo. | {% raw %}```<style type="text/css">p { color: red; }</style>```{% endraw %} |
| `style` | `media` | Especifica el soporte o dispositivo al que se aplican los estilos. | ```<style media="print">body { font-size: 12pt; }</style>``` |
| `title` | Sin atributos | La etiqueta `title` no acepta atributos. | ```<title>Kitchenerie</title>``` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }
