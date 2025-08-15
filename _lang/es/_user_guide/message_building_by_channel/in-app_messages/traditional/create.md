---
nav_title: Crear un mensaje dentro de la aplicación
article_title: Crear un mensaje dentro de la aplicación
page_order: 1
description: "Este artículo de referencia explica cómo crear un mensaje in-app con la plataforma Braze utilizando campañas o Canvas."
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
toc_headers: h2
---

# Crear un mensaje in-app

> Puedes crear un mensaje dentro de la aplicación o un mensaje en el explorador utilizando la plataforma Braze mediante campañas, Canvas o como campaña API. Te recomendamos encarecidamente que planifiques tus mensajes y prepares todos los materiales con antelación utilizando nuestra práctica [guía de preparación de mensajes en la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

## Paso 1: Elige dónde construir tu mensaje {#create-new-campaign-in-app}

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para mensajes sencillos y únicos, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaña %}

1. Vaya a **Mensajería** > **Campañas** y seleccione **Crear campaña**.
2. Seleccione **Mensaje en la aplicación**. Tenga en cuenta que los mensajes in-app no están disponibles en las campañas multicanal.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añada [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puede filtrar por etiquetas concretas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puede elegir diferentes plataformas, tipos de mensaje y diseños para cada una de sus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si todos los mensajes de su campaña van a ser similares o van a tener el mismo contenido, redacte su mensaje antes de añadir variantes adicionales. A continuación, puede seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

1. [Cree su lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de lienzos.
2. Una vez que haya configurado su lienzo, añada un paso en el constructor de lienzos. Nombra tu paso con algo claro y significativo.
3. Elija un [programa de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifique un retraso según sea necesario. Tenga en cuenta que los pasos que contienen mensajes in-app no pueden estar basados en acciones.
4. Filtra tu audiencia para este paso, según sea necesario. Puede afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después de la demora, a la hora de envío de los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elija cualquier otro canal de mensajería que desee asociar a su mensaje.

{% alert important %}
No puedes tener múltiples variantes de mensajes in-app en un solo paso.
{% endalert %}

Puedes encontrar más información específica de Canvas en [mensajes dentro de la aplicación en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Paso 2: Especifica las plataformas de entrega

Empiece por elegir qué plataformas deben recibir el mensaje. Utilice esta selección para limitar la entrega de una campaña a un conjunto específico de aplicaciones. Por ejemplo, puede elegir **Navegadores web** para un mensaje en el navegador que anime a los usuarios a descargar su aplicación móvil para asegurarse de que no reciben el mensaje después de haber obtenido ya su aplicación. Como las selecciones de plataforma son específicas de cada variante, podrías probar la interacción de los mensajes por plataforma.

| Plataforma                        | Envío de mensajes        |
|---------------------------------|-------------------------|
| Aplicaciones móviles                     | SDK para iOS y Android      |
| Navegadores web                    | SDK Web                 |
| Tanto aplicaciones móviles como navegadores web | SDK para iOS, Android y Web |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Paso 3: Especifique sus tipos de mensajes

Una vez que hayas seleccionado una plataforma de envío, explora los tipos de mensaje, diseños y otras opciones asociadas a ella. Obtenga más información sobre el comportamiento esperado y el aspecto de cada uno de estos mensajes en nuestra página [Detalles creativos]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/), o haciendo clic en los tipos de mensaje vinculados en las tablas siguientes.

Cuando decidas qué tipo de mensaje utilizar, ten en cuenta cuánto espacio ocupará tu mensaje y lo perturbador que puede resultar para la experiencia del usuario.

- Los mensajes de **deslizamiento hacia arriba** son los menos intrusivos, ya que aparecen sutilmente sin bloquear el contenido.
- Los mensajes **modales** se sitúan en el centro, lo suficientemente prominentes como para captar la atención sin ocupar toda la pantalla.
- Los mensajes **a pantalla completa** son los que más llaman la atención y los mejores para anuncios críticos o promociones.

Cuanto más complejo sea tu contenido, más espacio necesitarás y más probable será que tu mensaje interrumpa el flujo del usuario.

### Tipos de mensajes

Estos mensajes in-app son aceptados tanto por aplicaciones móviles como por aplicaciones web.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>Tipo de mensaje</th>
    <th>Descripción del tipo</th>
    <th>Disposiciones disponibles</th>
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
      <li>Solo imagen</li>
      </ul>
    </td>
    <td>Orientación obligatoria del dispositivo (vertical u horizontal)</td>
    <td>¡Grande y audaz! Utilícelo cuando quiera asegurarse de que los usuarios ven su contenido, como sus campañas más críticas, notificaciones importantes o promociones masivas.<br><br>Ten en cuenta que en los dispositivos móviles, los mensajes en vertical y horizontal no se mostrarán si la orientación del dispositivo no coincide con la orientación del mensaje.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>Modal</a></td>
    <td>Mensajes que cubren toda la pantalla con una superposición de pantalla y un bloque de mensajes.</td>
    <td>
      <ul>
      <li>Texto (con imagen opcional)</li>
      <li>Solo imagen</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>Un buen término medio. Utilícelo cuando necesite una forma aparente de captar la atención del usuario, por ejemplo para animarle a probar una nueva función o aprovechar una promoción.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>deslizamiento hacia arriba</a></td>
    <td>Mensajes que se deslizan a la vista en un lugar designado sin bloquear el resto de la pantalla.</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>Discreto: ocupa el mínimo espacio en la pantalla. Se utiliza para avisar a los usuarios de pequeños fragmentos de información, como nuevas funciones, anuncios, uso de cookies, etc.<br></td>
  </tr>
</tbody>
</table>

### Tipos de mensajes avanzados

Estos mensajes in-app se pueden personalizar según tus necesidades.

<table class="tg">
<thead>
  <tr>
    <th>Tipo de mensaje</th>
    <th>Descripción del tipo</th>
    <th>Disposiciones disponibles</th>
    <th>Requisitos</th>
    <th>Uso recomendado</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>Mensaje HTML personalizado</a></td>
    <td>Mensajes personalizados que funcionan según lo definido en su código personalizado (HTML, CSS y/o JavaScript).</td>
    <td>N/A</td>
    <td>Debes configurar <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> opción de inicialización a <code>true</code> para que tu mensaje in-app funcione.</td>
    <td>Es una buena opción si quieres todas las ventajas de los IAM, pero necesitas una funcionalidad adicional o que la apariencia siga siendo "de marca". Puede modificar hasta el más mínimo detalle del mensaje: fuente, color, forma, tamaño, botones, etc. <br><br>Ejemplos de casos de uso: pedir a los usuarios su opinión sobre la aplicación, formularios de captura de correo electrónico o mensajes paginados.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>Formulario de captura de correo electrónico</a></td>
    <td>Normalmente se utiliza para capturar el correo electrónico del espectador.</td>
    <td>N/A</td>
    <td>Debes configurar <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> opción de inicialización a <code>true</code> para que tu mensaje in-app funcione.</td>
    <td>Cuando se pide a los usuarios que envíen su dirección de correo electrónico.</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>Web Modal con CSS</a></td>
    <td>Mensajes modales para web con CSS personalizable.</td>
    <td>
      <ul>
      <li>Texto (con imagen opcional)</li>
      <li>Solo imagen</li>
      </ul>
    </td>
    <td>El Modal Web con CSS es único del SDK Web y solo puede utilizarse tras seleccionar <b>Navegadores Web</b>.</td>
    <td>Cuando quieras cargar o escribir CSS personalizado para crear mensajes bonitos y con estilo personalizado. </td>
  </tr>
</tbody>
</table>

{% alert important %}
Si Braze detecta que no tiene un botón de cierre o de salida incluido en su código, le pediremos que añada uno. Para su comodidad, le proporcionamos un fragmento que puede copiar y pegar en su código: <br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## Paso 4: Redacta tu mensaje desde la aplicación

La pestaña **Redactar** te permite editar todos los aspectos del contenido y el comportamiento de tu mensaje.

![Un ejemplo de mensaje dentro de la aplicación de una marca para dar la bienvenida a nuevos clientes y pedirles que configuren un perfil de usuario.]({% image_buster /assets/img_archive/iam_compose.png %}){: style="max-width:85%" }

El contenido de la pestaña **Redactar** varía en función de las opciones de mensaje elegidas en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

### Idioma

Selecciona **Añadir idiomas** y selecciona los idiomas que desees de la lista proporcionada. Esto insertará [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) en tu mensaje. Le recomendamos que seleccione sus idiomas antes de escribir el contenido para que pueda rellenar el texto donde corresponda en el Líquido. Consulte nuestra [lista completa de idiomas disponibles]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported).

### Imagen

Dependiendo del tipo de mensaje, puedes **subir una imagen**, **elegir una insignia** o utilizar **Font Awesome**. Para cargar una imagen, haga clic en **Añadir imagen** o proporcione una URL de imagen. Al hacer clic en **Añadir imagen** se abre la **Biblioteca multimedia**, donde puede seleccionar una imagen cargada previamente o añadir una nueva. Cada tipo de mensaje y plataforma puede tener sus propias proporciones y requisitos; asegúrate de comprobarlos antes de encargar o crear una imagen desde cero.

### Cabecera y cuerpo

¡Escribe lo que quieras! Incluya textos totalmente personalizados (a menudo con funciones HTML personalizadas) con opciones para incluir [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) y otros tipos de personalización. Cuanto antes transmita su mensaje y consiga que su cliente haga clic, ¡mejor! Recomendamos encabezados y contenidos de mensaje claros y concisos.

Algunos tipos de mensaje no necesitan cabeceras y, por tanto, no las solicitan.

#### Consejos 

##### Generar copia de IA

¿Necesitas ayuda para crear textos impactantes? Prueba a utilizar el [asistente de redacción de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduzca el nombre o la descripción de un producto y la IA generará un texto de marketing similar al humano para utilizarlo en sus mensajes.

![Inicia el botón de redactor de IA, situado en el campo Mensaje del compositor de SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### Crear mensajes de derecha a izquierda

¿Necesitas ayuda para crear mensajes de derecha a izquierda en idiomas como el árabe y el hebreo? Consulta [Crear mensajes de derecha a]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) izquierda para conocer las mejores prácticas.

### Texto del botón {#buttons}

Cuando esté disponible para su tipo de mensaje, puede hacer que aparezcan hasta dos botones debajo del cuerpo del texto. Puede crear y editar el texto y el color de los botones personalizados. También puede añadir un enlace a las Condiciones del servicio en los formularios de captura de correo electrónico.

Si decide utilizar un solo botón, éste se ajustará automáticamente para ocupar el espacio disponible en la parte inferior de su mensaje en lugar de dejar espacio para un botón adicional.

#### Elegir un botón principal

Si decide dar formato a estos botones con sus propios colores, le recomendamos que utilice el Botón 2 para obtener el resultado que prefiera.

En otras palabras, si quiere que su usuario haga clic en un botón más que en otro, asegúrese de que está a la derecha. El botón derecho suele tener más posibilidades de que se haga clic en él, sobre todo si tiene un color que contraste o destaque del resto del mensaje. Esto solo se acentúa cuando el botón de la izquierda se funde más visualmente con el mensaje.

![Botones primario y secundario en un mensaje dentro de la aplicación]({% image_buster /assets/img/primary-secondary-buttons.png %})

### Comportamiento al hacer clic {#button-actions}

Cuando su cliente pulsa un botón en su mensaje in-app, dispone de las siguientes acciones. 

| Acción | Descripción |
|---|---|
| Redirigir a URL de página web | Abrir una página web no nativa. |
| [Vínculo profundo a la aplicación]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | Enlace profundo a una pantalla existente en su aplicación. |
| Cerrar mensaje | Cierra el mensaje activo en ese momento. |
| Registrar evento personalizado | Elija un [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) para activar. Puede utilizarse para mostrar otro mensaje dentro de la aplicación o activar mensajes adicionales. |
| Registrar atributo personalizado | Elija un [atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/) para establecer para el usuario actual. |
| Solicitar permiso push | Muestra el permiso push nativo. Lee más sobre [la preparación para las notificaciones push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/), así como sobre [las mejores prácticas]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices) para preparar a los usuarios para el push. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Nota: las opciones __Request Push Permission__, __Log Custom Event__ y __Log Custom Attribute__ requieren las siguientes versiones mínimas del SDK:

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### Opciones de dispositivos iOS

Si lo deseas, puedes restringir tu mensaje in-app para que sólo se envíe a dispositivos iOS. Para ello, haz clic en **Cambiar** y selecciona **Sólo enviar a dispositivos iOS**.

### Cierre del mensaje

Elija entre las siguientes opciones:
 
- **Descartar automáticamente:** Seleccione cuántos segundos permanecerá el mensaje en la pantalla.
- **Espere a que el usuario pase el dedo o lo toque:** Requiere una opción de despido o cierre.

### Posición de deslizamiento hacia arriba

Esta configuración solo se aplica al tipo de mensaje Deslizamiento hacia arriba. Elige si quieres que el slideup aparezca **en la parte inferior de la pantalla** o **en la parte superior**.

### HTML y activos

Este ajuste sólo se aplica al tipo de mensaje Código personalizado. Copia y pega HTML en el espacio disponible y sube tus activos mediante un archivo ZIP.

### Marcador de posición de entrada de datos de la captura de correo electrónico

Esta configuración sólo se aplica al tipo de mensaje del formulario de captura de correo electrónico. Introduzca la copia personalizada que aparecerá como texto de marcador de posición para el campo de entrada de correo electrónico. La opción predeterminada es "Introduzca su dirección de correo electrónico".

## Paso 5: Estiliza tu mensaje in-app

La pestaña **Estilo** te permite ajustar todos los aspectos visuales de tu mensaje. Sube una imagen o insignia, o elige un icono de insignia prediseñado. Cambie los colores del encabezado y del cuerpo del texto, de los botones y del fondo seleccionándolos de una paleta o introduciendo un código hexadecimal, RGB o HSB.

El contenido de la pestaña **Estilo** varía en función de las opciones de mensaje elegidas en el paso anterior, pero puede incluir cualquiera de las siguientes opciones:

| Formato | Entrada de datos | Descripción |
|---|---|---|
|[Perfil del color]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css) | Aplícalo desde la galería de plantillas de mensajes de la aplicación. | Selecciona **Aplicar plantilla** y elige de la galería. A continuación, selecciona **Guardar**. |
|Alineación de texto | Izquierda, centro o derecha.  | Sólo disponible para las nuevas versiones de Braze SDK. |
|Encabezado | Código de color HEX. | Aparecerá el color HEX que desee. También podrás elegir la opacidad del color.  |
|Texto | Código de color HEX. | Aparecerá el color HEX que desee. También podrás elegir la opacidad del color. |
|Botones de acción | Código de color HEX. | Aparecerán los colores HEX que desee. También podrás elegir la opacidad de los colores. Puede elegir colores para: el fondo del botón Cerrar del mensaje, así como para el fondo, el texto y el borde de cada botón. |
| Borde del botón | Código de color HEX. | Novedad Esto le permitirá diferenciar sus botones primario y secundario. Sugerimos delinear los botones con colores que contrasten. |
|Color de fondo | Código de color HEX. | Aparecerá el color HEX que desee. También podrás elegir la opacidad del color. Este es el fondo de todo el mensaje y se mostrará claramente detrás del cuerpo del texto. |
|Superposición de pantalla | Código de color HEX. | Aparecerá el color HEX que desee. También podrás elegir la opacidad del color. Sólo disponible para las nuevas versiones de Braze SDK. Este es el marco que rodea todo el mensaje. |
|Chevron u otra opción de mensaje de cierre | Código de color HEX. | Aparecerá el color HEX que desee. También podrás elegir la opacidad del color. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Previsualice y pruebe]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) siempre su mensaje antes de enviarlo.

{% alert important %}
Algunos tipos de mensajes dentro de la aplicación no tienen la opción de estilo personalizado más allá de subir HTML (o CSS o JavaScript) y activos personalizados utilizando un archivo ZIP. [Web Modal con CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) le permite cargar o escribir CSS personalizado para crear mensajes hermosos y con estilo personalizado.
{% endalert %}

## Paso 6: Configurar ajustes adicionales (opcional)

### Pares clave-valor

Puedes añadir [pares clave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) para enviar campos personalizados adicionales a los dispositivos de los usuarios.

## Paso 7: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaña %}

Construya el resto de su campaña; consulte las siguientes secciones para obtener más orientación sobre cómo utilizar mejor nuestras herramientas para construir mensajes in-app.

#### Elige un desencadenante

Seleccione la acción a partir de la cual desea activar su mensaje, así como las horas de inicio y fin de su campaña o Canvas.

{% alert important %}
Ten en cuenta que si pretendes desencadenar tu mensaje dentro de la aplicación basándote en un evento personalizado, ese evento personalizado debe enviarse utilizando el SDK.
{% endalert %}

![Campaña basada en acciones con la acción desencadenante establecida en "Iniciar sesión".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

La entrega de mensajes en la aplicación se basa totalmente en los siguientes desencadenantes de acciones:

- Realizar una compra
- Abrir la aplicación/página web
- Realización de un evento personalizado (sólo funciona con eventos enviados mediante el SDK)
- Abrir un mensaje push específico
- Programe automáticamente las campañas para que se envíen a una hora determinada con respecto a la hora local de cada uno de sus usuarios.
- Los mensajes también pueden configurarse para que se repitan diaria, semanal (opcionalmente en días concretos) o mensualmente.

Debes seleccionar una fecha y hora de inicio; sin embargo, la fecha de finalización es opcional. Una fecha de finalización impedirá que ese mensaje in-app específico aparezca en los dispositivos después de la fecha/hora especificada.

Consulte nuestra documentación para desarrolladores sobre [la activación de eventos en el servidor]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) y la [entrega local de mensajes dentro de la aplicación]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages).

##### Activación en línea o fuera de línea

Los mensajes in-app funcionan enviando el mensaje y los activadores al dispositivo del usuario. Después de que los mensajes dentro de la aplicación estén en un dispositivo, espera a mostrarlos hasta que se cumpla la condición desencadenante. Si los mensajes dentro de la aplicación ya están almacenados en caché en el dispositivo del usuario, puedes incluso desencadenar mensajes dentro de la aplicación sin conexión a Braze (por ejemplo, en modo Avión).

{% alert important %}
Una vez que se ha detenido un mensaje in-app, puede haber algunos usuarios que sigan viendo el mensaje si iniciaron una sesión antes de que se detuviera el mensaje y posteriormente realizan el evento desencadenante. Estos usuarios se contabilizarán como una impresión única incluso después de que se haya detenido la campaña.
{% endalert %}

#### Elija una prioridad

Por último, una vez seleccionada la acción que desencadenará el mensaje dentro de la aplicación, también debes establecer una prioridad. Si dos mensajes se activan a partir de la misma acción, los mensajes de alta prioridad se programarán para que aparezcan en los dispositivos de los usuarios antes que los mensajes de menor prioridad. 

Puede elegir entre las siguientes prioridades de mensajes:

- Baja prioridad (se muestra después de otros mensajes)
- Prioridad media
- Alta prioridad (se muestra antes que otros mensajes)

Las opciones alta, media y baja para las prioridades de los mensajes activados son cubos y, como tales, varios mensajes podrían tener la misma prioridad seleccionada. Para establecer prioridades dentro de estos cubos, haga clic en **Establecer prioridad exacta**, y podrá arrastrar y soltar campañas para ordenarlas con la prioridad correcta.

![Un ejemplo de cómo se establece la prioridad para una campaña de mensajería dentro de la aplicación y Canvas.]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### Elige los usuarios a los que dirigirte

A continuación, tienes que [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. Automáticamente obtendrá una instantánea de cómo es la población de ese segmento aproximado en este momento. Tenga en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

{% alert note %}
Si hay un retraso en el paso del mensaje dentro de la aplicación, la pertenencia a un segmento se evaluará después del retraso. Si el usuario cumple los requisitos, el mensaje in-app se sincronizará en la siguiente sesión disponible.
{% endalert %}

##### Reevaluar la elegibilidad de la campaña y Liquid

En algunos casos, es posible que desee volver a evaluar la elegibilidad de un usuario a medida que activan un mensaje en la aplicación para mostrar. Algunos ejemplos son las campañas dirigidas a un atributo personalizado que cambia con frecuencia o los mensajes que deben reflejar cualquier cambio de perfil de última hora.

![Casilla de verificación de "Reevaluar la elegibilidad de la campaña antes de mostrarla" seleccionada.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}){:style="max-width:60%"}

Al seleccionar **Reevaluar elegibilidad de campaña antes de mostrar**, se realizará una solicitud adicional a Braze para confirmar que el usuario sigue siendo elegible para este mensaje antes de enviarlo. Además, cualquier variable [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) o [Contenido Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) será templado en ese momento antes de que se muestre el mensaje.

Esto evita que se envíen mensajes in-app a usuarios dentro de campañas caducadas o archivadas. Si no reevalúa la elegibilidad de un usuario, el usuario recibirá el mensaje in-app incluso después de que la campaña haya caducado o se haya archivado porque el mensaje está en su SDK y esperando a que los usuarios lo activen.

{% alert note %}
Al activar esta opción se producirá un ligero retraso (< 100 ms) entre el momento en que un usuario activa un mensaje in-app y el momento en que se muestra el mensaje, debido a la elegibilidad añadida y a la solicitud de plantillas.
<br><br>
No utilice esta opción para mensajes que puedan activarse mientras un usuario está desconectado o cuando no se requiera la reevaluación de la elegibilidad y el líquido.
{% endalert %}

#### Elegir eventos de conversión

Braze le permite realizar un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), tras recibir una campaña. Tiene la opción de permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

{% endtab %}
{% tab Canvas %}

Si aún no lo ha hecho, complete las secciones restantes de su componente Canvas. Para más detalles sobre cómo construir el resto de su Canvas, implementar pruebas multivariantes y Selección Inteligente, y más, consulte el paso [Construya su Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación de Canvas.

Para obtener información sobre las opciones de mensajería dentro de la aplicación específicas de Canvas, consulta [Mensajes dentro de la aplicación en Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/).

{% endtab %}
{% endtabs %}

## Paso 8: Revisar y desplegar

Cuando hayas terminado de crear lo último de tu campaña o Canvas, revisa sus detalles, [pruébala]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) y ¡envíala!

A continuación, consulta [los informes de mensajes en la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/) para saber cómo puedes acceder a los resultados de tus campañas de mensajería.

## Lo que hay que saber

### Límites de las campañas activas de mensajes in-app

Braze valora la fiabilidad y la rapidez. Al igual que te sugerimos que envíes a Braze sólo los datos que necesites, también te recomendamos que desactives las campañas que ya no aporten ningún valor a tu marca.

El procesamiento de campañas de mensajes in-app basadas en acciones que siguen en estado activo pero que ya no envían mensajes o que ya no son necesarias ralentiza el rendimiento general de los servicios Braze para usted y otros clientes. Este tiempo adicional necesario para procesar este gran número de campañas inactivas significa que cualquier mensaje in-app tardará más en aparecer en los dispositivos de los usuarios finales, lo que repercute en su experiencia.

{% alert important %}
Puedes tener hasta 200 campañas de mensajería dentro de la aplicación activas y basadas en acciones por espacio de trabajo para optimizar la velocidad de entrega de los mensajes y evitar los tiempos de espera. Esto no se aplica a los Lienzos.
{% endalert %}

El recuento de 200 incluye las campañas de mensajes in-app activas que aún no han llegado a su hora de finalización y las que no tienen hora de finalización. No se contabilizarán las campañas de mensajería dentro de la aplicación que hayan finalizado. El cliente medio de Braze tiene un total de 26 campañas activas a la vez, por lo que es poco probable que esta limitación le afecte.


