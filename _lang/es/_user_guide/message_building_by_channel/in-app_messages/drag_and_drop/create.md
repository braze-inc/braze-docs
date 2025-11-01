---
nav_title: Crear un mensaje dentro de la aplicación
article_title: "Crear un mensaje dentro de la aplicación con arrastrar y soltar"
description: "Este artículo de referencia cubre la creación de un mensaje dentro de la aplicación con el editor de arrastrar y soltar, los requisitos previos, los detalles creativos y mucho más."
alias: "/create_dnd_iam/"
page_order: 1
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-level-styles'
  add-a-custom-font: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components'
  creative-details: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#creative-details'
---

# Crear un mensaje dentro de la aplicación con arrastrar y soltar

> Con el editor de arrastrar y soltar, puedes crear mensajes dentro de la aplicación completamente personalizados, tanto en campañas como en Canvas, utilizando la experiencia de edición de arrastrar y soltar.


{% multi_lang_include video.html id="j94omgo73o" align="right" source="wistia" %}

Si quieres utilizar tus plantillas HTML personalizadas existentes o plantillas creadas por terceros, debes volver a crearlas en el editor de arrastrar y soltar.

¿No estás seguro de si tu mensaje dentro de la aplicación debe enviarse utilizando una campaña o un [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)? Las campañas son mejores para campañas de mensajería únicas y sencillas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos. Una vez que hayas seleccionado dónde construir tu mensaje, vamos a sumergirnos en los pasos para crear un mensaje dentro de la aplicación arrastrando y soltando.

## Requisitos previos

### Requisitos del SDK

| Versión mínima del SDK                                                          | Versión recomendada del SDK                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% details More information on minimum SDKs %}

Los mensajes creados con el editor de arrastrar y soltar sólo pueden enviarse a los usuarios de las versiones mínimas del SDK (consulta la tabla anterior). Si un usuario no ha actualizado su aplicación (es decir, está en una versión antigua del SDK), no recibirá el mensaje dentro de la aplicación.

Para aprovechar todas las características disponibles en el editor de arrastrar y soltar, actualiza tus SDK a las versiones de SDK recomendadas. Esto te permite aprovechar las siguientes características adicionales:

- Enlaces de texto que no descartan el mensaje
- Botón de acción para solicitar push primer

A continuación se describen los requisitos mínimos individuales del SDK para estas características:

| Enlaces de texto\*.                                                         | Solicitar imprimación push                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\*Si incluyes un enlace en tu mensaje dentro de la aplicación que redirija a una URL y el usuario final no está en las versiones mínimas de SDK especificadas, al seleccionar el enlace se cerrará el mensaje y el usuario no podrá volver al mensaje para enviar el formulario.

{% enddetails %}

### Requisitos adicionales

- Para el SDK Web, la opción de inicialización [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) debe estar en `true`. La opción `enableHtmlInAppMessages` también permitirá que estos mensajes funcionen, pero está obsoleta y debería actualizarse a `allowUserSuppliedJavascript`.
- Si utilizas Google Tag Manager, debes habilitar "Permitir mensajes HTML dentro de la aplicación" en la configuración de GTM.

## Paso 1: Crear un mensaje dentro de la aplicación

Crea un nuevo mensaje dentro de la aplicación o un paso en Canvas y, a continuación, selecciona **Editor de arrastrar y soltar** como experiencia de edición.

## Paso 2: Selecciona tu plantilla

Después de seleccionar el editor de arrastrar y soltar como tu experiencia de edición, puedes elegir:

- Empieza con una plantilla modal en blanco
- Utiliza una plantilla de mensajes dentro de la aplicación Braze de arrastrar y soltar
- Selecciona una plantilla de mensajes dentro de la aplicación guardada mediante arrastrar y soltar

Selecciona **Crear mensaje** para empezar a diseñar tu mensaje dentro de la aplicación en el editor de arrastrar y soltar.

\![La sección Plantillas de Braze, donde puedes elegir una plantilla básica, de imagen de fondo, de captura de número de teléfono o en blanco.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

También puedes acceder a todas las plantillas desde la sección **Plantillas** del panel.

## Paso 3: Añadir páginas adicionales (opcional) {#multi-page}

Añadir páginas a tu mensaje dentro de la aplicación te permite guiar a los usuarios a través de un flujo secuencial, como un flujo de incorporación o un viaje de bienvenida. Puedes administrar páginas desde la sección **Páginas** de la pestaña **Construir**.

\![Un mensaje dentro de la aplicación para una empresa sanitaria que consta de tres páginas.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Adding pages %}

Los mensajes dentro de la aplicación comienzan con una página predeterminada. Para añadir una nueva página:

1. Selecciona **\+ Añadir página**.
2. Selecciona de la lista de plantillas personalizadas o proporcionadas por Braze.
3. Pon a la página un nombre significativo. Esto te ayudará a conectar las páginas entre sí.

{% alert tip %}
Puedes añadir hasta 10 páginas por mensaje dentro de la aplicación.
{% endalert %}

Para duplicar una página existente:

1. Pasa el ratón por encima de la página en la lista y selecciona <i class="fas fa-ellipsis-vertical"></i> para abrir más opciones.
2. Selecciona **Duplicar**.
3. Pon a la página un nombre significativo. Esto te ayudará a conectar las páginas entre sí.

{% endtab %}
{% tab Deleting or renaming pages %}

Para borrar o renombrar una página:

1. Pasa el ratón por encima de la página en la lista y selecciona <i class="fas fa-ellipsis-vertical"></i> para abrir más opciones.
2. Selecciona **Renombrar** o **Eliminar**.

{% endtab %}
{% endtabs %}

### Paso 3a: Conectar páginas entre sí

Los mensajes dentro de la aplicación de varias páginas son secuenciales, lo que significa que los usuarios interactúan con el mensaje tocando o haciendo clic para pasar a la página siguiente en el flujo.

Para unir páginas:

1. Selecciona tu página de inicio.
2. Selecciona un botón o un elemento de imagen en el Canvas.
3. Configura el **comportamiento Al hacer clic** como **Ir a la página**.
4. Selecciona la página a la que quieres enlazar desde la página de inicio.
5. Continúa hasta que todas las páginas estén enlazadas.

Un usuario está editando el botón de acción principal para ir a la página 2 del mensaje dentro de la aplicación.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

Si una página no está vinculada a ninguna otra, el mensaje no se puede lanzar.

{% alert note %}
Los usuarios pueden seleccionar el botón de cerrar X para salir del mensaje en cualquier momento. Este botón no se puede quitar.
{% endalert %}

## Paso 4: Crea y diseña tu mensaje dentro de la aplicación

Aquí es donde tu mensaje se pavonea por la pasarela, vestido con el estilo característico de tu marca. Utilizando una combinación de bloques de editor y configuraciones de estilo, puedes personalizar y diseñar tu mensaje dentro de la aplicación.

- Para ver una lista de los bloques de editor disponibles y sus propiedades, consulta [Bloques de editor]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).
- Si necesitas ayuda para personalizar el aspecto de tu mensaje, consulta [Configuración de estilo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/).
- Para conocer las mejores prácticas para crear mensajes de [derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/), consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Paso 5: Prueba tu mensaje dentro de la aplicación

La sección **Vista previa & Prueba** te permite previsualizar tus mensajes dentro de la aplicación en diferentes dispositivos y enviar un mensaje de prueba a tu dispositivo. Aquí puedes asegurarte de que los detalles están alineados en todas tus plataformas para tu campaña de mensajes dentro de la aplicación, arrastrando y soltando. 

Es importante que siempre pruebes tus mensajes dentro de la aplicación antes de enviar tus campañas para ayudarte a visualizar cómo será tu mensaje final desde la perspectiva de tu usuario.

### Vista previa del mensaje como usuario

{% alert warning %}
Para enviar una prueba a Grupos de Prueba de Contenidos o a usuarios individuales, antes de enviarla debe habilitarse la función push en tus dispositivos de prueba.
{% endalert %}

Puedes obtener una vista previa de los mensajes desde la pestaña **Vista previa & Test**, como si fueras un usuario. Puedes seleccionar un usuario concreto, un usuario aleatorio o crear un usuario personalizado:

- **Usuario aleatorio:** Braze seleccionará aleatoriamente a un usuario de la base de datos y previsualizará el mensaje dentro de la aplicación basándose en sus atributos o en la información del evento.
- **Selecciona Usuario:** Puedes seleccionar un usuario concreto basándote en su dirección de correo electrónico o `external_id`. El mensaje dentro de la aplicación tendrá una vista previa basada en los atributos de ese usuario y en la información del evento.
- **Usuario personalizado:** Puedes personalizar un usuario. Braze ofrecerá entradas para todos los atributos y eventos disponibles. Introduce la información que quieras ver en la vista previa del correo electrónico.

### Lista de control

Ten en cuenta las siguientes preguntas cuando pruebes tu mensaje dentro de la aplicación:

- ¿Has probado el mensaje en distintos dispositivos?
- ¿Aparecen las imágenes y los medios y actúan como se espera de ellos?
- ¿Funciona el Liquid como se esperaba? ¿Has previsto un valor de atributo predeterminado para el caso de que Liquid no devuelva información?
- ¿Es tu texto claro, conciso y correcto?
- ¿Tus botones dirigen al usuario a dónde debe ir?

## Preguntas más frecuentes

#### ¿Por qué no aparecen los clics en el cuerpo en mi página de análisis?

Los clics en el cuerpo no se recogen automáticamente para los mensajes dentro de la aplicación creados con el editor de arrastrar y soltar. Para más detalles, consulta los registros de cambios del SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) y [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

#### ¿Puedo segmentar en función de los clics en los botones?

Sí, puedes segmentar en función de los clics en los botones de hasta dos botones de tu mensaje. Para ello, establece el **Identificador para informes** para tus botones en "0" y "1", que corresponderán a los filtros de segmentación "Botón de mensaje dentro de la aplicación pulsado 1" y "Botón de mensaje dentro de la aplicación pulsado 2" respectivamente.

\![El campo "Identificador para informar" con valor "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

#### ¿Puedo personalizar mi mensaje dentro de la aplicación utilizando HTML o JavaScript personalizados o transferir mensajes HTML existentes al editor?

No puedes transferir directamente mensajes HTML existentes al editor, pero puedes insertar HTML, CSS y JavaScript sin procesar en un bloque de código personalizado. Puedes utilizar bloques de código personalizados para incrustar videos de terceros y Liquid avanzado, como Contenido conectado o declaraciones condicionales.

#### ¿Cómo puedo crear un mensaje deslizamiento hacia arriba dentro de la aplicación?

Actualmente el editor está limitado sólo a mensajes modales y a pantalla completa. Puedes cambiar entre los tipos de visualización en la sección **Contenedor de mensajes** del panel **Estilos de mensaje**.

#### ¿Puedo guardar mi mensaje dentro de la aplicación como plantilla después de crearlo dentro de mi campaña o Canvas?

Sí. Para cualquier mensaje dentro de la aplicación que quieras reutilizar en una futura campaña o paso en Canvas, puedes guardarlo como una plantilla personalizada utilizando el botón **Guardar como plantilla**, disponible después de salir del editor. Antes de poder guardarla como plantilla, primero debes lanzar la campaña O guardarla como borrador.

Vista previa de un mensaje dentro de la aplicación para la visita a un producto.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

También puedes crear y guardar plantillas de mensajes dentro de la aplicación accediendo a **Plantillas** > Plantillas de mensajes dentro de la aplicación **.**
