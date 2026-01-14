---
nav_title: Crear un mensaje dentro de la aplicación
article_title: Crear un mensaje dentro de la aplicación
page_order: 1
description: "Este artículo de referencia explica cómo crear un mensaje dentro de la aplicación utilizando la plataforma Braze mediante campañas o Canvas."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Crear un mensaje dentro de la aplicación

> Puedes crear un mensaje dentro de la aplicación o un mensaje en el explorador utilizando la plataforma Braze mediante campañas, Canvas o como campaña API. Te recomendamos encarecidamente que planifiques tus mensajes y prepares todos los materiales con antelación utilizando nuestra práctica [guía de preparación de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Paso 1: Elige dónde construir tu mensaje {#create-new-campaign-in-app}

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y sencillas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Selecciona **Mensaje dentro de la aplicación**. Ten en cuenta que los mensajes dentro de la aplicación no están disponibles en las campañas multicanal.
3. Pon a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por determinadas etiquetas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puedes elegir diferentes plataformas, tipos de mensaje y diseños para cada una de tus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o van a tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. A continuación, puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Nombra tu paso con algo claro y significativo.
3. Elige un [programa de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifica un retraso según sea necesario. Ten en cuenta que los pasos que contienen mensajes dentro de la aplicación no pueden basarse en acciones.
4. Filtra tu audiencia para este paso, según sea necesario. Puedes afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso, en el momento en que se envíen los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elige cualquier otro canal de mensajería que quieras asociar a tu mensaje.

{% alert important %}
No puedes tener múltiples variantes de mensajes dentro de la aplicación en un solo paso.
{% endalert %}

Puedes encontrar más información específica de Canvas en [Mensajes dentro de la aplicación en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Paso 2: Especifica las plataformas de entrega

Empieza por elegir qué plataformas deben recibir el mensaje. Utiliza esta selección para limitar la entrega de una campaña a un conjunto específico de aplicaciones. Por ejemplo, puedes elegir **los navegadores Web** para un mensaje en el explorador que anime a los usuarios a descargar tu aplicación móvil para asegurarte de que no reciben el mensaje después de haber obtenido ya tu aplicación. Como las selecciones de plataforma son específicas de cada variante, podrías probar la interacción de los mensajes por plataforma.

| Plataforma                        | Entrega de mensajes        |
|---------------------------------|-------------------------|
| Aplicaciones móviles                     | iOS & SDK para Android      |
| Navegadores web                    | SDK Web                 |
| Ambas aplicaciones móviles & Navegadores web | iOS, Android & SDKs Web |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 3: Especifica tus tipos de mensajes

Una vez que hayas seleccionado una plataforma de envío, explora los tipos de mensajes, diseños y otras opciones asociadas a ella. Obtén más información sobre el comportamiento esperado y el aspecto de cada uno de estos mensajes en nuestra página [Detalles creativos]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/), o haciendo clic en los tipos de mensajes vinculados en las tablas siguientes.

Cuando decidas qué tipo de mensaje utilizar, ten en cuenta cuánto espacio ocupará tu mensaje y lo perturbador que puede resultar para la experiencia del usuario.

- Los mensajes de **deslizamiento hacia arriba** son los menos intrusivos, ya que aparecen sutilmente sin bloquear el contenido.
- Los mensajes **modales** se sitúan en el centro, lo suficientemente prominentes como para captar la atención sin ocupar toda la pantalla.
- Los mensajes **a pantalla completa** son los que más llaman la atención y los mejores para anuncios críticos o promociones.

Cuanto más complejo sea tu contenido, más espacio necesitarás y más probable será que tu mensaje interrumpa el flujo del usuario.

### Tipos de mensajes

Estos mensajes dentro de la aplicación son aceptados tanto por las aplicaciones móviles como por las aplicaciones Web.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Tipo de mensaje</th>
    <th>Tipo Descripción</th>
    <th>Diseños disponibles</th>
    <th>Otras opciones</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>Pantalla completa</a></td>
    <td>Mensajes que cubren toda la pantalla con un bloque de mensajes.</td>
    <td>
      <ul>
      <li>Imagen y texto</li>
      <li>Sólo imagen</li>
      </ul>
    </td>
    <td>Orientación forzada del dispositivo (Vertical u Horizontal)</td>
    <td>¡Grande y audaz! Utilízalo cuando quieras asegurarte de que los usuarios ven tu contenido, como tus campañas más críticas, notificaciones importantes o promociones masivas.<br><br>Ten en cuenta que en los dispositivos móviles, los mensajes en vertical y horizontal no se mostrarán si la orientación del dispositivo no coincide con la orientación del mensaje.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Modal</a></td>
    <td>Mensajes que cubren toda la pantalla con una superposición de pantalla y un bloque de mensajes.</td>
    <td>
      <ul>
      <li>Texto (con imagen opcional)</li>
      <li>Sólo imagen</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Un buen término medio. Utilízalo cuando necesites una forma aparente de captar la atención de tu usuario, como animar a los usuarios a probar una nueva característica o aprovechar una promoción.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>Deslizamiento hacia arriba</a></td>
    <td>Mensajes que se deslizan a la vista en un lugar designado sin bloquear el resto de la pantalla.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Discreto: ocupa el mínimo espacio en la pantalla. Se utiliza para avisar a los usuarios de pequeños fragmentos de información, como nuevas características, anuncios, uso de cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Tipos de mensajes avanzados

Estos mensajes dentro de la aplicación se pueden personalizar según tus necesidades.

<table class="tg">
<thead>
  <tr>
    <th>Tipo de mensaje</th>
    <th>Tipo Descripción</th>
    <th>Diseños disponibles</th>
    <th>Requisitos</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>Mensaje HTML personalizado</a></td>
    <td>Mensajes personalizados que rinden según lo definido en tu código personalizado (HTML, CSS y/o JavaScript).</td>
    <td>N/A</td>
    <td>Debes configurar <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> a <code>true</code> para que tu mensaje dentro de la aplicación funcione.</td>
    <td>Es una buena opción si quieres todas las ventajas de los IAM, pero necesitas una funcionalidad adicional o que la apariencia siga siendo "de marca". Puedes modificar hasta el más mínimo detalle del mensaje: fuente, color, forma, tamaño, botones, etc. <br><br>Algunos ejemplos de casos de uso son pedir a los usuarios su opinión sobre la aplicación, formularios de captura de correo electrónico o mensajes paginados</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Formulario de captura de correo electrónico</a></td>
    <td>Normalmente se utiliza para capturar el correo electrónico del espectador.</td>
    <td>N/A</td>
    <td>Debes configurar <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> a <code>true</code> para que tu mensaje dentro de la aplicación funcione.</td>
    <td>Al pedir a los usuarios que envíen su dirección de correo electrónico.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>Web Modal con CSS</a></td>
    <td>Mensajes modales para Web con CSS personalizable.</td>
    <td>
      <ul>
      <li>Texto (con imagen opcional)</li>
      <li>Sólo imagen</li>
      </ul>
    </td>
    <td>El Modal Web con CSS es único del SDK Web y sólo puede utilizarse tras seleccionar <b>Navegadores Web</b>.</td>
    <td>Cuando quieras cargar o escribir CSS personalizado para crear mensajes bonitos y con un estilo personalizado. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Si Braze detecta que no tienes incluido en tu código un botón de cierre o rechazo, te pediremos que añadas uno. Para tu comodidad, hemos proporcionado un fragmento de código que puedes copiar y pegar en tu código: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Paso 4: Redacta tu mensaje dentro de la aplicación

La pestaña **Redactar** te permite editar todos los aspectos del contenido y comportamiento de tu mensaje.

\![Un ejemplo de mensaje dentro de la aplicación de una marca para dar la bienvenida a nuevos clientes y pedirles que configuren un perfil de usuario.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

El contenido de la pestaña **Redactar** varía en función de las opciones de mensaje que hayas elegido en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

### Lengua

Selecciona **Añadir idiomas** y selecciona los idiomas que desees de la lista proporcionada. Esto insertará [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) en tu mensaje. Te recomendamos que selecciones tus idiomas antes de escribir el contenido, para que puedas rellenar el texto donde corresponda en el Liquid. Consulta nuestra [lista completa de idiomas disponibles]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

### Imagen

Dependiendo del tipo de mensajería, puedes **subir una imagen**, **elegir una señal** o utilizar **Font Awesome**. Para subir una imagen, haz clic en **Añadir imagen** o proporciona una URL de imagen. Al hacer clic en **Añadir imagen**, se abre la **biblioteca multimedia**, donde puedes seleccionar una imagen cargada previamente o añadir una nueva. Cada tipo de mensaje y plataforma puede tener sus propias proporciones y requisitos sugeridos: ¡asegúrate de comprobarlos antes de encargar o crear una imagen desde cero!

### Cabecera y cuerpo

¡Escribe lo que quieras! Incluye una copia completamente personalizada (a menudo con capacidades HTML personalizadas) con las opciones de incluir [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) y otros tipos de personalización. Cuanto más rápido transmitas tu mensaje y consigas que tu cliente haga clic, ¡mejor! Recomendamos encabezamientos y contenidos de mensaje claros y concisos.

Algunos tipos de mensajes no necesitan cabeceras y, por tanto, no las piden.

#### Consejos 

##### Generar copia de IA

¿Necesitas ayuda para crear un texto impresionante? Prueba a utilizar el [asistente de redacción AI]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduce el nombre o la descripción de un producto y la IA generará textos de marketing similares a los humanos para que los utilices en tus mensajes.

Inicia el botón AI Copywriter, situado en el campo Mensaje del creador de mensajes dentro de la aplicación.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Crear mensajes de derecha a izquierda

¿Necesitas ayuda para crear mensajes de derecha a izquierda en idiomas como el árabe y el hebreo? Consulta [Crear mensajes de derecha a]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) izquierda para conocer las mejores prácticas.

### Texto del botón {#buttons}

Cuando esté disponible para tu tipo de mensaje, puedes hacer que aparezcan hasta dos botones debajo del cuerpo del texto. Puedes crear y editar texto y color personalizados para los botones. También puedes añadir un enlace a las Condiciones de servicio en los formularios de captura de correo electrónico.

Si decides utilizar sólo un botón, éste se ajustará automáticamente para ocupar el espacio disponible en la parte inferior de tu mensaje en lugar de dejar espacio para un botón adicional.

#### Elegir un botón principal

Si decides dar formato a estos botones con tus propios colores, te recomendamos que utilices el Botón 2 para obtener el resultado que prefieras.

En otras palabras, si quieres que tu usuario haga clic en un botón más que en otro, asegúrate de que esté a la derecha. El botón derecho suele tener más posibilidades de que se haga clic en él, sobre todo si tiene un color que contraste o destaque del resto del mensaje. Esto sólo se acentúa cuando el botón de la izquierda se funde más visualmente con el mensaje.

\![Botones principal y secundario en un mensaje dentro de la aplicación]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportamiento al hacer clic {#button-actions}

Cuando tu cliente haga clic en un botón de tu mensaje dentro de la aplicación, estarán disponibles las siguientes acciones. 

| Acción | Descripción |
|---|---|
| Redirigir a URL Web | Abre una página Web no nativa. |
| [Enlace profundo a la aplicación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Vincula en profundidad una pantalla existente en tu aplicación. |
| Cerrar mensaje | Cierra el mensaje activo en ese momento. |
| Registrar evento personalizado | Elige un [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) para desencadenar. Puede utilizarse para mostrar otro mensaje dentro de la aplicación o desencadenar mensajería adicional. |
| Atributo personalizado de registro | Elige un [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) para el usuario actual. |
| Solicitar permiso push | Muestra el permiso push nativo. Lee más sobre [la preparación]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) para las notificaciones push, así como sobre [las mejores prácticas]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices) para preparar a los usuarios para el push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Nota: las opciones __Solicitar permiso push__, __Registrar evento personalizado__ y __Registrar atributo__ personalizado requieren las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Opciones del dispositivo iOS

Si lo deseas, puedes restringir tu mensaje dentro de la aplicación para que sólo se envíe a dispositivos iOS. Para ello, haz clic en **Cambiar** y selecciona **Sólo enviar a dispositivos iOS**.

### Cerrar mensaje

Elige entre las siguientes opciones:
 
- **Descartar automáticamente:** Selecciona cuántos segundos permanecerá el mensaje en la pantalla.
- **Espera a que el usuario pase el dedo o lo toque:** Requiere una opción de despido o cierre.

### Deslizar hacia arriba

Esta configuración sólo se aplica al tipo de mensaje Deslizamiento hacia arriba. Elige entre que tu deslizamiento aparezca **Desde la parte inferior de la pantalla** **de la aplicación** o **Desde la parte superior de la pantalla de la aplicación**.

### HTML y activos

Esta configuración sólo se aplica al tipo de mensaje Código personalizado. Copia y pega HTML en el espacio disponible y sube tus activos mediante un archivo ZIP.

### Marcador de posición de entrada de captura de correo electrónico

Esta configuración sólo se aplica al tipo de mensaje del formulario de captura de correo electrónico. Introduce una copia personalizada que aparecerá como texto del marcador de posición del campo de entrada de correo electrónico. La opción predeterminada es "Introduce tu dirección de correo electrónico".

## Paso 5: Estiliza tu mensaje dentro de la aplicación

La pestaña **Estilo** te permite ajustar todos los aspectos visuales de tu mensaje. Sube una imagen o una señal, o elige un icono de señal prediseñado. Cambia los colores del texto de la cabecera y del cuerpo, de los botones y del fondo seleccionándolos de una paleta o introduciendo un código hexadecimal, RGB o HSB.

El contenido de la pestaña **Estilo** varía en función de las opciones de mensaje que hayas elegido en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

| Formato | Entrada | Descripción |
|---|---|---|
|[Perfil de color]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css) | Aplícalo desde la galería de plantillas de mensajes dentro de la aplicación. | Selecciona **Aplicar plantilla** y elige de la galería. A continuación, selecciona **Guardar**. |
|Alineación del texto | Izquierda, centro o derecha.  | Sólo disponible para las versiones más recientes del SDK de Braze. |
|Cabecera | Código de color HEX. | Aparecerá el color HEX que desees. También podrás elegir la opacidad del color.  |
|Texto | Código de color HEX. | Aparecerá el color HEX que desees. También podrás elegir la opacidad del color. |
|Botones | Código de color HEX. | Aparecerán los colores HEX que desees. También podrás elegir la opacidad de los colores. Puedes elegir colores para: el Fondo del Botón Cerrar del mensaje, así como para el Fondo, el Texto y el Borde de cada botón. |
| Borde del botón | Código de color HEX. | Novedad Esto te permitirá separar los botones principal y secundario. Sugerimos perfilar los botones con colores que contrasten. |
|Color de fondo | Código de color HEX. | Aparecerá el color HEX que desees. También podrás elegir la opacidad del color. Es el fondo de todo el mensaje y se mostrará claramente detrás de tu cuerpo de texto. |
|Superposición de pantalla | Código de color HEX. | Aparecerá el color HEX que desees. También podrás elegir la opacidad del color. Sólo disponible para las versiones más recientes del SDK de Braze. Es el marco que rodea todo el mensaje. |
|Chevron u otra Opción de Cerrar Mensaje | Código de color HEX. | Aparecerá el color HEX que desees. También podrás elegir la opacidad del color. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Obtén]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) siempre [una vista previa y prueba]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) tu mensaje antes de enviarlo.

{% alert important %}
Algunos tipos de mensajes dentro de la aplicación no tienen la opción de estilo personalizado más allá de subir HTML (o CSS o JavaScript) y activos personalizados utilizando un archivo ZIP. [Web Modal con CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) te permite cargar o escribir CSS personalizados para crear mensajes bonitos y con un estilo personalizado.
{% endalert %}

## Paso 6: Configurar ajustes adicionales (opcional)

### Pares clave-valor

Puedes añadir [pares clave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para enviar campos personalizados adicionales a los dispositivos de los usuarios.

## Paso 7: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

Construye el resto de tu campaña; consulta las secciones siguientes para obtener más orientación sobre cómo utilizar mejor nuestras herramientas para construir mensajes dentro de la aplicación.

#### Elige un desencadenante

Selecciona la acción a partir de la cual quieres desencadenar tu mensaje, así como las horas de inicio y fin de tu campaña o Canvas.

{% alert important %}
Ten en cuenta que si pretendes desencadenar tu mensaje dentro de la aplicación basándote en un evento personalizado, ese evento personalizado debe enviarse utilizando el SDK.
{% endalert %}

\![Campaña basada en acciones con la acción desencadenante establecida en "Iniciar sesión".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

La entrega de mensajes dentro de la aplicación se basa totalmente en las siguientes acciones desencadenantes:

- Hacer una compra
- Abrir la aplicación/página web
- Realización de un evento personalizado (sólo funciona con eventos enviados mediante el SDK)
- Abrir un mensaje push específico
- Programa automáticamente el envío de campañas a una hora determinada con respecto a la hora local de cada uno de tus usuarios.
- Los mensajes también pueden configurarse para que se repitan diaria, semanal (opcionalmente en días concretos) o mensualmente.

Debes seleccionar una fecha y hora de inicio; sin embargo, la fecha de finalización es opcional. Una fecha de finalización impedirá que ese mensaje dentro de la aplicación específico aparezca en los dispositivos después de la fecha/hora especificada.

Consulta nuestra documentación para desarrolladores sobre [la activación de eventos en el servidor]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) y la [entrega local de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

##### Desencadenamiento online frente a offline

Los mensajes dentro de la aplicación funcionan enviando el mensaje y los desencadenantes al dispositivo del usuario. Después de que los mensajes dentro de la aplicación estén en un dispositivo, espera a mostrarlos hasta que se cumpla la condición desencadenante. Si los mensajes dentro de la aplicación ya están almacenados en caché en el dispositivo del usuario, puedes incluso desencadenar mensajes dentro de la aplicación sin conexión a Braze (por ejemplo, en modo Avión).

{% alert important %}
Una vez que se ha detenido un mensaje dentro de la aplicación, puede haber algunos usuarios que sigan viendo el mensaje si iniciaron una sesión antes de que se detuviera el mensaje y posteriormente realizan el evento desencadenante. Estos usuarios se contabilizarán como una impresión única incluso después de que la campaña se haya detenido.
{% endalert %}

#### Elige una prioridad

Por último, después de seleccionar la acción que desencadenará el mensaje dentro de la aplicación, también debes establecer una prioridad. Si se desencadenan dos mensajes a partir de la misma acción, se programará que los mensajes de alta prioridad aparezcan en los dispositivos de los usuarios antes que los mensajes de menor prioridad. 

Puedes elegir entre las siguientes prioridades de mensajes:

- Prioridad baja (se muestra después de otros mensajes)
- Prioridad media
- Alta prioridad (se muestra antes que otros mensajes)

Las opciones alta, media y baja para las prioridades de los mensajes desencadenados son contenedores, por lo que varios mensajes podrían tener la misma prioridad seleccionada. Para establecer prioridades dentro de estos contenedores, haz clic en **Establecer prioridad exacta**, y podrás arrastrar y soltar campañas para ordenarlas con la prioridad correcta.

Un ejemplo de cómo se establece la prioridad para una campaña de mensajes dentro de la aplicación y Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Elige los usuarios a los que dirigirte

A continuación, tienes que [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. Automáticamente recibirás una instantánea de cómo es la población aproximada de ese segmento en este momento. Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

{% alert note %}
Si hay un retraso en el paso del mensaje dentro de la aplicación, la pertenencia a un segmento se evaluará después del retraso. Si el usuario es elegible, el mensaje dentro de la aplicación se sincronizará en la siguiente sesión disponible.
{% endalert %}

##### Reevaluar la elegibilidad de la campaña y Liquid

En algunos casos, puede que quieras reevaluar la elegibilidad de un usuario cuando desencadena la visualización de un mensaje dentro de la aplicación. Algunos ejemplos son las campañas dirigidas a un atributo personalizado que cambia con frecuencia o los mensajes que deben reflejar cualquier cambio de perfil de última hora.

\![Casilla de verificación de "Reevaluar la elegibilidad de la campaña antes de mostrarla" seleccionada.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Cuando selecciones **Volver a evaluar la elegibilidad de la campaña antes de mostrarla**, se realizará una solicitud adicional a Braze para confirmar que el usuario sigue siendo elegible para este mensaje antes de enviarlo. Además, cualquier variable de [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) o [Contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) se plantillará en ese momento antes de que se muestre el mensaje.

Esto impide que se envíen mensajes dentro de la aplicación a los usuarios de campañas caducadas o archivadas. Si no vuelves a evaluar la elegibilidad de un usuario, éste recibirá el mensaje dentro de la aplicación incluso después de que la campaña haya caducado o esté archivada, porque el mensaje está en tu SDK y esperando a que los usuarios lo desencadenen.

{% alert note %}
Si se habilita esta opción, se producirá un ligero retraso (< 100ms) entre el momento en que un usuario desencadena un mensaje dentro de la aplicación y el momento en que se muestra el mensaje, debido a la solicitud añadida de habilitación y plantilla.
<br><br>
No utilices esta opción para mensajes que puedan desencadenarse mientras un usuario está desconectado o cuando no se requiera la reevaluación de elegibilidad y Liquid.
{% endalert %}

#### Elige eventos de conversión

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), después de recibir una campaña. Tienes la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

{% endtab %}
{% tab Canvas %}

Si aún no lo has hecho, completa las secciones restantes de tu componente Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariantes e Intelligent Selection, y mucho más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación sobre Canvas.

Para obtener información sobre las opciones de mensajería dentro de la aplicación específicas de Canvas, consulta [Mensajes dentro de la aplicación en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Paso 8: Revisar y desplegar

Cuando hayas terminado de construir la última parte de tu campaña o Canvas, revisa sus detalles, [pruébala]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) y ¡envíala!

A continuación, consulta [los informes de mensajes dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) para saber cómo puedes acceder a los resultados de tus campañas de mensajería.

## Lo que debes saber

### Límites activos de la campaña de mensajería dentro de la aplicación

Braze valora la fiabilidad y la rapidez. Al igual que te sugerimos que envíes a Braze sólo los datos que necesites, también te recomendamos que desactives las campañas que ya no aporten ningún valor a tu marca.

Procesar campañas de mensajería dentro de la aplicación basadas en acciones que todavía están activas pero que ya no envían mensajes o que ya no son necesarias ralentiza el rendimiento general de los servicios Braze para ti y para otros clientes. Este tiempo extra necesario para procesar este gran número de campañas inactivas significa que cualquier mensaje dentro de la aplicación tardará más en aparecer en los dispositivos del usuario final, lo que repercute en la experiencia del usuario final.

{% alert important %}
Puedes tener hasta 200 campañas de mensajería dentro de la aplicación activas y basadas en acciones por espacio de trabajo para optimizar la velocidad de entrega de los mensajes y evitar los tiempos de espera. Esto no se aplica a los Lienzos.
{% endalert %}

El recuento de 200 incluye las campañas de mensajes dentro de la aplicación activas que aún no han llegado a su hora de finalización y las que no tienen hora de finalización. No se contabilizarán las campañas de mensajería dentro de la aplicación que hayan finalizado. El cliente medio de Braze tiene un total de 26 campañas activas a la vez, por lo que es poco probable que esta limitación te afecte.


