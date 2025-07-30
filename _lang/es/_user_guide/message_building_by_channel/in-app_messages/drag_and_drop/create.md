---
nav_title: Crear un mensaje dentro de la aplicación
article_title: "Crear un mensaje In-App con arrastrar y soltar"
description: "Este artículo de referencia trata sobre la creación de un mensaje in-app con el editor de arrastrar y soltar, los requisitos previos, los detalles creativos y mucho más."
alias: "/create_dnd_iam/"
page_order: 1
local_redirect: #set-message-level-styles, #add-a-custom-font, #drag-and-drop-in-app-message-components, #creative-details
  set-message-level-styles: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-level-styles'
  add-a-custom-font: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#custom-fonts'
  drag-and-drop-in-app-message-components: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#message-components'
  creative-details: '/docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#creative-details'
---

# Crear un mensaje in-app con arrastrar y soltar

> Con el editor de arrastrar y soltar, puedes crear mensajes dentro de la aplicación completamente personalizados, tanto en campañas como en Canvas, utilizando la experiencia de edición de arrastrar y soltar.

Si desea utilizar sus plantillas HTML personalizadas existentes o plantillas creadas por terceros, deberá volver a crearlas en el editor de arrastrar y soltar.

¿No estás seguro de si tu mensaje in-app debe enviarse utilizando una campaña o un [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)? Las campañas son mejores para mensajes sencillos y únicos, mientras que los lienzos son mejores para recorridos de usuario de varios pasos. Una vez que hayas seleccionado dónde crear tu mensaje, vamos a ver los pasos para crear un mensaje in-app de arrastrar y soltar.

## Requisitos previos

### Requisitos del SDK

| Versión mínima del SDK                                                          | Versión del SDK recomendada                                                       |
| ---------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}{:/} | {::nomarkdown}{% sdk_min_versions swift:6.5.0 android:26.0.0 web:4.8.1 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% details Más información sobre los SDK mínimos %}

Los mensajes creados con el editor de arrastrar y soltar sólo pueden enviarse a usuarios con las versiones mínimas del SDK (véase la tabla anterior). Si un usuario no ha actualizado su aplicación (es decir, está en una versión anterior del SDK), no recibirá el mensaje in-app.

Para aprovechar todas las funciones disponibles en el editor de arrastrar y soltar, actualice sus SDK a las versiones de SDK recomendadas. Esto le permite aprovechar las siguientes funciones adicionales:

- Enlaces de texto que no descartan el mensaje
- Botón de acción para solicitar push primer

A continuación se describen los requisitos mínimos individuales del SDK para estas funciones:

| Enlaces de texto\*.                                                         | Solicitar push primer                                                           |
| ------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| {::nomarkdown}{% sdk_min_versions swift:6.2.0 android:26.0.0 %}{:/} | {::nomarkdown}{% sdk_min_versions web:4.8.1 swift:6.5.0 android:26.0.0 %}{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

\*Si incluyes un enlace en tu mensaje dentro de la aplicación que redirija a una URL y el usuario final no está en las versiones mínimas de SDK especificadas, al seleccionar el enlace se cerrará el mensaje y el usuario no podrá volver al mensaje para enviar el formulario.

{% enddetails %}

### Requisitos adicionales

- Para el SDK Web, la opción de inicialización [`allowUserSuppliedJavascript`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initializationoptions) debe establecerse en `true`. La opción `enableHtmlInAppMessages` también permitirá que estos mensajes funcionen, pero está obsoleta y debería actualizarse a `allowUserSuppliedJavascript`.
- Si utilizas Google Tag Manager, debes habilitar "Permitir mensajes HTML dentro de la aplicación" en la configuración de GTM.

## Paso 1: Crear un mensaje en la aplicación

Cree un nuevo mensaje en la aplicación o un paso en el lienzo y, a continuación, seleccione **Editor de arrastrar y soltar** como experiencia de edición.

## Paso 2: Selecciona tu plantilla

Después de seleccionar el editor de arrastrar y soltar como su experiencia de edición, puede optar por:

- Empezar con una plantilla modal en blanco
- Utiliza una plantilla de mensaje Braze de arrastrar y soltar en la aplicación
- Selecciona una plantilla de mensaje guardada para arrastrar y soltar en la aplicación

Selecciona **Crear mensaje** para empezar a diseñar tu mensaje dentro de la aplicación en el editor de arrastrar y soltar.

![La sección de plantillas de Braze donde puedes elegir una plantilla básica, de imagen de fondo, de captura de número de teléfono o en blanco.]({% image_buster /assets/img_archive/dnd_iam_select_template.png %})

También puede acceder a todas las plantillas desde la sección **Plantillas** del panel de control.

## Paso 3: Añadir páginas adicionales (opcional) {#multi-page}

Añadir páginas a tu mensaje dentro de la aplicación te permite guiar a los usuarios a través de un flujo secuencial, como un flujo de incorporación o un viaje de bienvenida. Puede gestionar las páginas desde la sección **Páginas** de la pestaña **Construir**.

![Un mensaje dentro de la aplicación para una empresa sanitaria que se compone de tres páginas.]({% image_buster /assets/img_archive/dnd_iam_mockup.png %})

{% tabs %}
{% tab Añadir páginas %}

Los mensajes in-app empiezan con una página por defecto. Para añadir una nueva página:

1. Selecciona **\+ Añadir página**.
2. Seleccione de la lista de plantillas personalizadas o proporcionadas por Braze.
3. Nombra la página con algo significativo. Esto le ayudará a conectar las páginas entre sí.

{% alert tip %}
Puedes añadir hasta 10 páginas por mensaje in-app.
{% endalert %}

Para duplicar una página existente:

1. Pase el ratón por encima de la página en la lista y seleccione <i class="fas fa-ellipsis-vertical"></i> para abrir más opciones.
2. Selecciona **Duplicar**.
3. Nombra la página con algo significativo. Esto le ayudará a conectar las páginas entre sí.

{% endtab %}
{% tab Borrar o renombrar páginas %}

Para borrar o renombrar una página:

1. Pase el ratón por encima de la página en la lista y seleccione <i class="fas fa-ellipsis-vertical"></i> para abrir más opciones.
2. Seleccione **Renombrar** o **Borrar**.

{% endtab %}
{% endtabs %}

### Paso 3a: Conectar páginas

Los mensajes multipágina in-app son secuenciales, lo que significa que los usuarios interactúan con el mensaje pulsando o haciendo clic para pasar a la siguiente página del flujo.

Para unir páginas:

1. Seleccione su página de inicio.
2. Seleccione un botón o elemento de imagen en el lienzo.
3. Establezca el **comportamiento Al hacer clic** en **Ir a la página**.
4. Seleccione la página a la que desea enlazar desde la página de inicio.
5. Continúe hasta que todas las páginas estén enlazadas.

![Un usuario está editando el botón de acción principal para ir a la página 2 del mensaje dentro de la aplicación.]({% image_buster/assets/img_archive/dnd_iam_multipage.gif %})

Si una página no está vinculada a ninguna otra, el mensaje no puede lanzarse.

{% alert note %}
Los usuarios pueden seleccionar el botón de cerrar X para salir del mensaje en cualquier momento. Este botón no se puede quitar.
{% endalert %}

## Paso 4: Construye y diseña tu mensaje in-app

Aquí es donde su mensaje se pavonea por la pasarela, vestido con el estilo característico de su marca. Utilizando una combinación de bloques de editor y configuraciones de estilo, puedes personalizar y diseñar tu mensaje dentro de la aplicación.

- Para obtener una lista de los bloques de edición disponibles y sus propiedades, consulte [Bloques de edición]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/editor_blocks/).
- Si necesitas ayuda para personalizar el aspecto de tu mensaje, consulta [Configuración de estilo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/).
- Para conocer las mejores prácticas para crear mensajes de derecha a izquierda, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Paso 5: Prueba tu mensaje in-app

La sección **Vista previa y prueba** te permite previsualizar tus mensajes in-app en diferentes dispositivos y enviar un mensaje de prueba a tu dispositivo. Aquí, puede asegurarse de que los detalles están alineados en todas sus plataformas para su campaña de mensajes in-app de arrastrar y soltar. 

Es importante que siempre pruebes tus mensajes dentro de la aplicación antes de enviar tus campañas para ayudarte a visualizar cómo será tu mensaje final desde la perspectiva de tu usuario.

### Vista previa del mensaje como usuario

{% alert warning %}
Para enviar una prueba a grupos de prueba de contenido o a usuarios individuales, debe activarse la función push en los dispositivos de prueba antes de enviarla.
{% endalert %}

Puedes previsualizar los mensajes desde la pestaña **Previsualizar y probar**, como si fueras un usuario. Puede seleccionar un usuario específico, un usuario aleatorio o crear un usuario personalizado:

- **Usuario aleatorio:** Braze seleccionará aleatoriamente un usuario de la base de datos y previsualizará el mensaje en la aplicación en función de sus atributos o de la información del evento.
- **Seleccionar usuario:** Puedes seleccionar un usuario concreto basándote en su dirección de correo electrónico o `external_id`. El mensaje de la aplicación se previsualizará en función de los atributos del usuario y la información del evento.
- **Usuario personalizado:** Puedes personalizar un usuario. Braze ofrecerá entradas para todos los atributos y eventos disponibles. Introduce la información que quieras ver en la vista previa del correo electrónico.

### Lista de comprobación

Ten en cuenta las siguientes preguntas cuando pruebes tu mensaje dentro de la aplicación:

- ¿Has probado el mensaje en diferentes dispositivos?
- ¿Aparecen las imágenes y los medios de comunicación y actúan como se esperaba?
- ¿Funciona el Líquido como se esperaba? ¿Ha previsto un valor de atributo por defecto en caso de que Liquid no devuelva ninguna información?
- ¿Es su texto claro, conciso y correcto?
- ¿Sus botones dirigen al usuario hacia dónde debe ir?

## Preguntas más frecuentes

#### ¿Por qué no aparecen los clics en el cuerpo en mi página de análisis?

Los clics en el cuerpo no se recopilan automáticamente para los mensajes in-app creados con el editor de arrastrar y soltar. Para más detalles, consulta los registros de cambios del SDK para [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) y [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

#### ¿Puedo segmentar en función de los clics en los botones?

Sí, puede segmentar en función de los clics de hasta dos botones de su mensaje. Para ello, establezca el **Identificador para informes** para sus botones en "0" y "1", que corresponderán a los filtros de segmentación "Botón de mensaje dentro de la aplicación pulsado 1" y "Botón de mensaje dentro de la aplicación pulsado 2" respectivamente.

![El campo "Identificador para informes" con valor "0".]({% image_buster /assets/img/identifier_for_reporting.png %}){: style="max-width:50%;"}

#### ¿Puedo personalizar mi mensaje in-app utilizando HTML o JavaScript personalizado o transferir mensajes HTML existentes al editor?

No puede transferir directamente mensajes HTML existentes al editor, pero puede insertar HTML, CSS y JavaScript sin procesar en un bloque de código personalizado. Puede utilizar bloques de Código personalizado para incrustar vídeos de terceros y Líquido avanzado, como Contenido conectado o sentencias condicionales.

#### ¿Cómo puedo crear un deslizamiento hacia arriba de un mensaje dentro de la aplicación?

Actualmente, el editor está limitado únicamente a los mensajes modales y a pantalla completa. Puede cambiar entre los tipos de visualización en la sección **Contenedor de mensajes** del panel **Estilos de mensajes**.

#### ¿Puedo guardar mi mensaje in-app como una plantilla después de construirlo dentro de mi campaña o Canvas?

Sí. Para cualquier mensaje in-app que desee reutilizar en una futura campaña o paso de Canvas, puede guardarlo como una plantilla personalizada utilizando el botón **Guardar como plantilla**, disponible después de salir del editor. Antes de poder guardarla como plantilla, primero debe lanzar la campaña O guardarla como borrador.

![Una vista previa de un mensaje dentro de la aplicación para la visita de un producto.]({% image_buster /assets/img_archive/dnd_iam_save_as_template.png %})

También puedes crear y guardar plantillas de mensajes dentro de la aplicación accediendo a **Plantillas** > **Plantillas de mensajes dentro de la aplicación**.
