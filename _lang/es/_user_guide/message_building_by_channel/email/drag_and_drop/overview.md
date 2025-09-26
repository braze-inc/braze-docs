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

El editor de arrastrar y soltar utiliza [Contenido](#content) y [Filas](#rows) como los dos componentes clave para simplificar su flujo de trabajo, sin uso adicional de HTML.

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

**Contenido** incluye una serie de mosaicos que representan diferentes tipos de contenido que puede utilizar en su mensaje. Están organizados en tres categorías: básicos, medios y avanzados. 

{% tabs %}
{% tab Básico %}

Los bloques básicos son la base de su correo electrónico. Utilizando estos bloques, puede añadir cualquiera de los siguientes elementos en el cuerpo de su correo electrónico:

- Título
- Párrafo
- Lista
- Botón
- Divisor
- Espaciador

{% endtab %}
{% tab Medios de comunicación %}

Con los bloques multimedia, puedes añadir diferentes contenidos visuales como imágenes, vídeos, iconos y enlaces de redes sociales e iconos personalizables.

{% endtab %}
{% tab Avanzado %}

Aunque el editor de arrastrar y soltar simplifica el flujo de trabajo con estos bloques, también puede utilizar bloques avanzados para insertar HTML o añadir un menú al cuerpo del mensaje. Tenga en cuenta que el uso de su propio HTML puede afectar a la representación del mensaje.

{% endtab %}
{% endtabs %}

### Filas

**Las filas** son unidades estructurales que definen la composición horizontal de una sección del mensaje mediante columnas. Puede vaciar filas o [bloques de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/). El uso de más de una columna permite colocar diferentes elementos de contenido uno al lado del otro. De esta forma, puedes añadir todos los elementos estructurales que necesites a tu mensaje, independientemente de la plantilla que hayas seleccionado al empezar.

#### Estilo de las tarjetas

**El Estilo de tarjeta** es una propiedad de fila que te permite añadir espaciado entre columnas y redondear sus esquinas. Con el formato de tarjeta, puedes crear diseños visualmente más atractivos que te ayuden a destacar tus contenidos más importantes, como características de nuevos productos, testimonios, ofertas especiales, actualizaciones de noticias y mucho más.

## Utilizar el editor de arrastrar y soltar

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para mensajes sencillos y únicos, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

Después de haber seleccionado dónde construir tu mensaje, vamos a sumergirnos en los pasos para crear un correo electrónico arrastrando y soltando.

### Paso 1: Selecciona tu plantilla

Después de seleccionar el editor de arrastrar y soltar como su experiencia de edición, puede optar por:

- Empiece con una plantilla en blanco.
- Utiliza una plantilla prediseñada de correo electrónico Braze de arrastrar y soltar.
- Utilice una plantilla de correo electrónico de arrastrar y soltar guardada.

{% alert note %}
Para utilizar una plantilla HTML personalizada existente o plantillas creadas por terceros, debes volver a crear la plantilla yendo a **Plantillas** > **Plantillas de correo electrónico** y seleccionando **Editor de arrastrar y soltar** como experiencia de edición.
{% endalert %}

También puede acceder a todas las plantillas desde la sección **Plantillas**.

Una vez seleccionada la plantilla, verá un resumen de su correo electrónico en **Variantes de correo electrónico**, que incluye la información de envío y el cuerpo del mensaje. 

A continuación, selecciona **Editar cuerpo del correo electrónico** para empezar a diseñar la estructura del correo electrónico en el editor de arrastrar y soltar. 

![La sección "Variantes de correo electrónico" con un cuerpo de correo electrónico de ejemplo.]({% image_buster /assets/img/dnd/dnd_emailvariant.png %})

### Paso 2: Crea tu correo electrónico

La experiencia de edición mediante arrastrar y soltar se divide en tres secciones: **Configuración de envío**, **Contenido** y **Vista previa y prueba**. La magia de construir el cuerpo de su correo electrónico ocurre en la sección **Contenido**. Antes de crear su correo electrónico, es importante entender los componentes clave que guían su experiencia de creación de correo electrónico. Si necesitas revisar, consulta [Acerca del editor](#about-the-editor).

Cuando estés listo, utiliza los bloques de contenido de arrastrar y soltar para construir tu correo electrónico.

1. Seleccione el panel **Filas**. Arrastre y suelte las configuraciones de las filas en el editor principal. Esto mapeará el diseño del contenido de tu correo electrónico.
- Tenga en cuenta que las nuevas configuraciones deben arrastrarse a la parte superior o inferior de una sección existente.
- Cuando seleccionas la configuración de una fila, aparece la configuración de **Propiedades de fila** para personalizar aún más los colores de fondo de las filas, las imágenes y los tamaños personalizados de las columnas.
2. Seleccione el panel **Contenido**. Arrastre y suelte los mosaicos de contenido que desee en los componentes de la fila.
- También puede arrastrar cualquiera de los mosaicos de **contenido** al editor principal. Esto crea una fila para el mosaico.
- Puede refinar aún más el mosaico seleccionándolo y ajustando los campos en **Propiedades de contenido** y **Opciones de bloque**. Esto incluye la edición del espaciado entre letras, el relleno, la altura de línea, etc.

Consulta [Otras personalizaciones](#other-customizations) para conocer otras formas de personalizar aún más tu correo electrónico arrastrando y soltando.

A medida que construyes tu correo electrónico, puedes alternar entre una vista de escritorio y una vista móvil para previsualizar cómo se verá tu mensaje de correo electrónico para tus grupos de usuarios. Esto comprobará que tu contenido es responsivo, y podrás hacer los ajustes necesarios sobre la marcha.

{% alert tip %}
¿Necesitas ayuda para crear textos impactantes? Prueba a utilizar el [asistente de redacción de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduce el nombre o la descripción de un producto y la IA generará textos de marketing similares a los humanos para que los utilices en tus mensajes.

![Botón Copywriter, situado en el panel Contenido junto a Ajustes de estilo en el editor de arrastrar y soltar.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_dnd.png %})
{% endalert %}

### Paso 3: Añade tu información de envío

Una vez que hayas terminado de diseñar y crear tu mensaje de correo electrónico, es hora de añadir la información de envío en la sección **Configuración de envío**.

1. En **Información de envío**, seleccione un correo electrónico como **Nombre de remitente + Dirección**. También puede personalizarlo seleccionando **Personalizar desde Nombre para mostrar + Dirección**.
2. Selecciona un correo electrónico como **dirección de responder a**. También puedes personalizarlo seleccionando **Personalizar dirección de respuesta a**.
3. A continuación, seleccione un correo electrónico como **dirección CCO** para que su correo electrónico sea visible para esta dirección.
4. Añada una línea de asunto a su correo electrónico. Opcionalmente, también puede añadir un preencabezado y un espacio en blanco después del preencabezado.

En el panel de la derecha aparecerá una vista previa con la información de envío que haya añadido. Esta información también puede actualizarse accediendo a **Configuración** > **Preferencias de correo electrónico** > **Configuración de envío**.

#### Personalización del encabezamiento de tu correo electrónico (avanzado)

En **Configuración de envío**, puede añadir personalización para las cabeceras y los extras del correo electrónico, lo que le permite enviar datos adicionales a otros proveedores de servicios de correo electrónico. Personalizar el encabezado de un correo electrónico, por ejemplo incluyendo el nombre del destinatario, también puede contribuir a aumentar la probabilidad de que se abra el mensaje.

{% alert note %}
La funcionalidad avanzada aparecerá en el compositor de campañas o Canvas. En la funcionalidad avanzada, puede modificar su configuración CSS en línea e introducir un encabezado o pares clave-valor adicionales (si están configurados).
{% endalert %}

### Paso 4: Pruebe su correo electrónico

Después de añadir tu información de envío, es hora de probar finalmente tu correo electrónico. 

Vaya a la sección **Previsualizar y probar**. Aquí tiene la opción de previsualizar su correo electrónico como usuario o enviar un mensaje de prueba. Esta sección también incluye [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/), que le permite comprobar que su correo electrónico se ha renderizado correctamente en diferentes clientes móviles y web.

{% alert tip %}
También puedes utilizar el conmutador de **vista previa en modo oscuro** del panel de vista previa para ver el cuerpo del correo electrónico en modo oscuro y ajustarlo según sea necesario.
{% endalert %}

Dado que puede ver tres versiones diferentes del mismo correo electrónico en el editor real, en Inbox Vision y como correo electrónico de prueba real, es importante alinear los detalles en todas sus plataformas.

#### Vista previa y envío de prueba
 
En la pestaña **Previsualizar como usuario**, puedes seleccionar los siguientes tipos de usuario para previsualizar tu mensaje.

- **Usuario aleatorio:** Braze seleccionará aleatoriamente un usuario de la base de datos y previsualizará el correo electrónico en función de sus atributos o de la información del evento.
- **Seleccionar usuario:** Puede seleccionar un usuario concreto en función de su dirección de correo electrónico o de su ID externo. El correo electrónico tendrá una vista previa basada en los atributos de ese usuario y en la información del evento
- **Usuario personalizado:** Puedes personalizar un usuario. Braze ofrecerá entradas para todos los atributos y eventos disponibles. Puede introducir cualquier información que desee ver en el correo electrónico de previsualización.

{% alert note %}
El usuario aleatorio puede o no formar parte de sus criterios de segmentación. La segmentación se selecciona a posteriori, por lo que Braze desconoce su público objetivo en este punto.
{% endalert %}

También puedes seleccionar **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa compartible que muestre el aspecto que tendrá el correo electrónico para un usuario cualquiera. El enlace durará siete días antes de que sea necesario regenerarlo. 

Ten en cuenta que cualquier modificación realizada en una plantilla de correo electrónico no se reflejará en un enlace generado previamente. Tendrás que generar una nueva vista previa del enlace para ver las modificaciones.

![Vista previa por correo electrónico con un botón para "Copiar enlace de vista previa" y copiar el enlace generado.]({% image_buster /assets/img/dnd_email_link_preview.png %})

#### Utilizar Inbox Vision

Inbox Vision le permite ver sus campañas de correo electrónico desde la perspectiva de los clientes de correo electrónico y los dispositivos móviles. Para probar tu mensaje de correo electrónico utilizando Visión de Bandeja de Entrada, selecciona **Visión de Bandeja de Entrada** en la sección **Vista previa y prueba** y selecciona **Ejecutar Visión de Bandeja de Entrada**.

{% alert tip %}
Las imágenes de fondo en los mensajes de correo electrónico pueden provocar a veces la aparición de líneas blancas o desconexiones entre las imágenes, por lo que es importante probar y comprobar los detalles de su mensaje de correo electrónico.
{% endalert %}

Después de utilizar el editor de arrastrar y soltar para diseñar y crear tu mensaje de correo electrónico, continúa [construyendo]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-4-build-the-remainder-of-your-campaign-or-canvas) el resto de tu campaña o Canvas.

{% details Acerca del motor HTML actualizado %}
El motor subyacente que produce HTML a partir del editor de arrastrar y soltar se ha optimizado y actualizado, lo que se traduce en ventajas relacionadas con la compresión y el renderizado de archivos HTML.

Se ha reducido el tamaño medio de nuestra huella de datos HTML exportados, lo que se traduce en una carga y representación más rápidas, menos recortes en los móviles y un menor consumo de ancho de banda.

La representación HTML ha mejorado gracias a las siguientes actualizaciones que minimizan el número de comentarios condicionales y consultas de medios CSS. Como resultado, los archivos HTML son más pequeños y se codifican de forma más eficiente.
- Migración de un diseño basado en elementos de `<div>` a una base de código con formato estándar `<table>` 
- [Los bloques de editor]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/) se han codificado de nuevo para ser más concisos
- El código HTML final se comprime para eliminar los espacios en blanco entre etiquetas
- Los separadores transparentes se convierten automáticamente en relleno de contenido
{% enddetails %}

## Otras personalizaciones

A medida que continúe creando mensajes de correo electrónico de arrastrar y soltar, puede personalizar aún más el cuerpo de cada mensaje utilizando una combinación de estos detalles creativos para captar la atención y el interés de su público en su mensaje.

{% alert tip %}
Puede crear un tema personalizado para su editor de arrastrar y soltar utilizando [la configuración de estilo global]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/).
{% endalert %}

### Imágenes de ancho automático

Las imágenes añadidas a su correo electrónico se establecerán automáticamente en **Ancho automático**. Para ajustar esta configuración, desactive **Ancho automático** y ajuste el porcentaje de ancho según sea necesario.

![Opción de anchura automática en la pestaña Contenido del editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd1.png %})

### Estratificación de colores

Mediante la superposición de colores, puede cambiar el color del fondo del correo electrónico, del área de contenido y de los distintos componentes del contenido. El orden de los colores de delante hacia atrás es: color del componente de contenido, color de fondo del área de contenido y color de fondo.

![Ejemplo de la superposición de colores en el editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd2.png %})

### Relleno de contenido

![Opciones de bloque para el editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd3.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Para ajustar el relleno, desplácese hasta **Opciones de bloque** y seleccione **Más opciones**. Puede ajustar el relleno para que su correo electrónico tenga el aspecto deseado.

### Fondo del contenido

Puede añadir una imagen de fondo a la configuración de sus filas, lo que le permitirá incorporar más diseño y contenido visual a su campaña de correo electrónico.

### Añadir personalización

![Opciones para añadir personalización para el editor de arrastrar y soltar.]({% image_buster /assets/img/dnd/dnd4.png %}){: style="float:right;max-width:25%;margin-left:15px;"}

Basic Liquid es compatible con el editor de correo electrónico de arrastrar y soltar. Para añadir personalización a su correo electrónico:

1. Seleccione **Personalización** en la sección **Contenido**. 
2. Seleccione el tipo de personalización. Esto incluye atributos por defecto (estándar), atributos de dispositivo, atributos personalizados, etc. 
3. Busque el atributo que desea añadir.
4. Copia el fragmento de código de Liquid que has generado y pégalo en el cuerpo de tu correo electrónico.

La personalización líquida no es compatible con los bloques de imágenes y los campos de tipo botón de enlace. 

#### Imágenes dinámicas

Puede optar por incluir imágenes dinámicas en sus mensajes de correo electrónico incluyendo Liquid en su atributo de fuente de imagen. Por ejemplo, en lugar de una imagen estática, puede insertar {% raw %} `https://example.com/images/?imageBanner={{first_name}}` {% endraw %} como URL de la imagen para incluir el nombre de pila de un usuario en la imagen. Esto ayuda a personalizar sus correos electrónicos para cada usuario.

### Cambiar la dirección del texto

Al redactar tu mensaje, puedes alternar la dirección del texto entre izquierda-derecha y derecha-izquierda seleccionando el botón **Dirección del texto** correspondiente. Puedes utilizar esta opción cuando crees mensajes en idiomas como el árabe y el hebreo.

![Menú del editor de arrastrar y soltar de correo electrónico con botón para alternar la alineación del texto entre derecha-izquierda e izquierda-derecha.]({% image_buster /assets/img/dnd/dnd_template1.png %}){: style="max-width:50%;"}

El aspecto final de los mensajes de derecha a izquierda depende en gran medida de cómo los presten los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

### Añadir atributos HTML a los enlaces

![La sección "Atributos" con el atributo "clicktracking" desactivado para un enlace.]({% image_buster /assets/img/dnd_custom_attributes.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

Cuando utilice enlaces, botones, imágenes y vídeos en el editor de arrastrar y soltar, seleccione **Añadir nuevo atributo** en **Atributos** de la sección **Contenido** para añadir información adicional a las etiquetas HTML de los mensajes de correo electrónico. Esto puede ser especialmente útil para la personalización, segmentación y estilización de mensajes.

Un caso de uso común es insertar un atributo en su etiqueta de anclaje para desactivar el seguimiento de clics cuando se envía a través de Braze.

* **SendGrid:** `clicktracking = "off"`
* **SparkPost:** `data-msys-clicktrack = "0"`

Otro caso de uso común es marcar enlaces específicos como enlaces universales. Los enlaces universales son enlaces que redirigen a su aplicación, ofreciendo a sus usuarios una experiencia integrada.

* **SendGrid:** `universal = "true"`
* **SparkPost:** `data-msys-sublink = "open-in-app"` (debe configurarse una [sub-ruta personalizada](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#custom-link-sub-paths) )

Para configurar enlaces universales, consulte [Enlaces universales y App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/).

También puede integrarse con uno de nuestros socios de atribución, como [Branch]({{site.baseurl}}/partners/message_orchestration/deeplinking/branch_for_deeplinking/) o [AppsFlyer]({{site.baseurl}}/partners/message_orchestration/attribution/appsflyer/appsflyer/#email-deep-linking-and-click-tracking), para gestionar los enlaces universales.

Por último, hay disponibles atributos predefinidos para ayudar a que tu mensaje sea accesible. Obtén más información en nuestro artículo dedicado [Construir mensajes accesibles en Braze]({{site.baseurl}}/help/accessibility).

### Configuración de un idioma para el correo electrónico

Puedes configurar el atributo de idioma yendo a la pestaña **Configuración** y seleccionando el idioma deseado. También puedes dirigirte al atributo de usuario {%raw%} `{{${language}}}` {%endraw%} si el mensaje va dirigido a usuarios con valores de idioma dinámicos.

![Configuración del valor "Idioma" de un correo electrónico.]({% image_buster /assets/img/dnd/language_setting_dnd.png %})

