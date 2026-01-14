---
nav_title: Crear un correo electrónico
article_title: Crear un correo electrónico con HTML personalizado
page_order: 1
description: "Este artículo de referencia explica cómo crear un correo electrónico utilizando la plataforma Braze. Se incluyen las mejores prácticas sobre cómo redactar tus mensajes, previsualizar tu contenido y programar tu campaña o Canvas."
tool:
  - Campaigns
channel:
  - email
search_rank: 1  
---

# Crear un correo electrónico con HTML personalizado

> Los mensajes de correo electrónico son estupendos para entregar contenido a tus usuarios según sus condiciones. También son herramientas excelentes para reactivar la interacción de usuarios que incluso pueden haber desinstalado tu aplicación. Enviar mensajes de correo electrónico personalizados y adaptados mejorará la experiencia de tus usuarios, y les ayudará a obtener el máximo valor de tu aplicación. 

Para ver ejemplos de campañas por correo electrónico, consulta nuestros [Casos de estudio](https://www.braze.com/customers). 

{% alert tip %}
Si es la primera vez que creas una campaña de correo electrónico, te recomendamos encarecidamente que eches un vistazo a estos cursos de Braze Learning:<br><br>
- [Adhesiones voluntarias y permisos por correo electrónico](https://learning.braze.com/messaging-channels-email)
- [Proyecto: Construye un programa básico de marketing por correo electrónico](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## Paso 1: Elige dónde construir tu mensaje

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y sencillas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

1. Ve a **Mensajería** > **Campañas** y selecciona **Crear campaña**.
2. Selecciona **Correo electrónico** o, para campañas dirigidas a varios canales, selecciona **Multicanal**.
3. Pon a tu campaña un nombre claro y significativo.
4. Añade [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de tus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puedes filtrar por determinadas etiquetas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si todos los mensajes de tu campaña van a ser similares o van a tener el mismo contenido, redacta tu mensaje antes de añadir variantes adicionales. A continuación, puedes elegir **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}
{% endtab %}
{% tab Canvas %}

1. [Crea tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de Canvas.
2. Después de configurar tu Canvas, añade un paso en el constructor de Canvas. Nombra tu paso con algo claro y significativo.
3. Elige un [programa de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifica un retraso según sea necesario.
4. Filtra tu audiencia para este paso, según sea necesario. Puedes afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso, en el momento en que se envíen los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elige cualquier otro canal de mensajería que quieras asociar a tu mensaje.
{% endtab %}
{% endtabs %}

{% multi_lang_include drag_and_drop/drag_and_drop_access.md variable_name='email html editor' %}

## Paso 2: Selecciona tu experiencia de edición {#step-2-choose-your-template-and-compose-your-email}

Braze ofrece dos experiencias de edición al crear una campaña de correo electrónico: nuestro [editor de arrastrar y soltar]({{site.baseurl}}/dnd/) y nuestro editor HTML estándar. Elige la ficha adecuada para la experiencia de edición que prefieras. 

\![Elige entre el editor de arrastrar y soltar, el editor HTML o las plantillas para tu experiencia de edición de correo electrónico.]({% image_buster /assets/img_archive/choose_email_creation.png %}){: style="max-width:75%" }

A continuación, puedes seleccionar una [plantilla de correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template) existente, [cargar una plantilla]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/) desde un archivo (sólo editor HTML) o utilizar una plantilla en blanco. 

{% alert tip %}
Recomendamos seleccionar una experiencia de edición por campaña de correo electrónico. Por ejemplo, elige el **editor** **HTML Clásico** o **Bloque** en una sola campaña de correo electrónico en lugar de cambiar entre editores.
{% endalert %}

## Paso 3: Redacta tu correo electrónico

Una vez seleccionada la plantilla, verás un resumen de tu correo electrónico en el que podrás saltar directamente al editor a pantalla completa para redactar tu correo electrónico, cambiar la información de envío y ver las advertencias sobre la capacidad de entrega o el cumplimiento de la ley. Puedes cambiar entre las pestañas HTML, clásico, texto sin formato y [AMP]({{site.baseurl}}/user_guide/message_building_by_channel/email/amphtml/) mientras redactas. 

\![El botón "Regenerar a partir de HTML".]({% image_buster /assets/img_archive/regenerate_from_html.png %}){: style="max-width:30%;float:right;margin-left:15px;border:none;" }

La versión en texto plano de tu correo electrónico siempre se actualizará automáticamente a partir de la versión HTML hasta que se detecte una edición en la versión en texto plano. Cuando se detecte una edición, Braze dejará de actualizar el texto sin formato, ya que suponemos que hiciste cambios intencionados que no deberían sobrescribirse. Puedes volver a la sincronización automática en la pestaña Texto sin **formato** seleccionando el icono **Regenerar a partir de HTML**, que sólo aparece si el texto sin formato no se está sincronizando.

{% alert tip %}
Para añadir movimiento en un correo electrónico con una vista previa precisa, utiliza GIFs en lugar de elementos que requieran JavaScript, ya que la mayoría de los buzones de entrada no admiten JavaScript.
{% endalert %}

\![Panel de variantes de correo electrónico para redactar tu correo electrónico.]({% image_buster /assets/img/email.png %}){: style="max-width:75%" }

{% alert important %}
Braze eliminará automáticamente los controladores de eventos HTML referenciados como atributos. Esto modificará el HTML, por lo que se recomienda volver a comprobar el correo electrónico una vez finalizado. Más información sobre [los controladores HTML](https://www.w3schools.com/tags/ref_eventattributes.asp).
{% endalert %}

{% alert tip %}
¿Necesitas ayuda para crear un texto impresionante? Prueba a utilizar el [asistente de redacción AI]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Introduce el nombre o la descripción de un producto y la IA generará textos de marketing similares a los humanos para que los utilices en tus mensajes.

\![Iniciar el botón AI Copywriter, situado en la pestaña Cuerpo del compositor de correo electrónico.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

¿Necesitas ayuda para crear mensajes de derecha a izquierda en idiomas como el árabe y el hebreo? Consulta [Crear mensajes de derecha a]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) izquierda para conocer las mejores prácticas.

### Paso 3a: Añade tu información de envío

Cuando hayas terminado de diseñar y crear tu mensaje de correo electrónico, es hora de añadir la información de envío en la sección **Configuración de envío**.

1. En **Información de envío**, selecciona un correo electrónico como **Nombre para mostrar de + Dirección**. También puedes personalizarlo seleccionando **Personalizar desde Nombre para mostrar + Dirección**.
2. Selecciona un correo electrónico como **dirección de respuesta**. También puedes personalizarlo seleccionando **Personalizar dirección de respuesta a**.
3. A continuación, selecciona un correo electrónico como **Dirección CCO** para que tu correo electrónico sea visible para esta dirección.
4. Añade una línea del asunto a tu correo electrónico. Opcionalmente, también puedes añadir un preencabezado y un espacio en blanco después del preencabezado.

{% multi_lang_include alerts/tip_alerts.md alert='Liquid email display name and reply-to address' %}

Aparecerá una vista previa en el panel de la derecha con la información de envío que hayas añadido. Esta información también se puede actualizar yendo a **Configuración** > **Preferencias de correo electrónico** > **Configuración de envío**.

#### Avanzado

En **Configuración de envío** > **Avanzado**, puedes activar el CSS en línea y añadir personalización para las cabeceras y los extras del correo electrónico, lo que te permite enviar datos adicionales a otros proveedores de servicios de correo electrónico.

##### Cabeceras de correo electrónico

Para añadir cabeceras de correo electrónico, selecciona **Añadir nueva cabecera**. Las cabeceras de correo electrónico contienen información sobre el correo electrónico que se envía. Estos [pares clave-valor]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) suelen contener información sobre el remitente, el destinatario, los protocolos de autenticación y la información de enrutamiento del correo electrónico. Braze añade automáticamente la información de cabecera necesaria que exige la RFC para que los correos electrónicos se entreguen correctamente a tu proveedor de correo electrónico.

Braze te permite la flexibilidad de añadir cabeceras de correo electrónico adicionales según sea necesario para casos de uso avanzados. Hay algunos campos reservados que la plataforma Braze sobrescribirá durante el envío. 

Evita utilizar las siguientes teclas:

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table id="reserved-fields">
<thead>
  <tr>
    <th>Campos reservados</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC</td>
    <td>dkim-firma</td>
    <td>Responder a</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>En</td>
    <td>Asunto</td>
  </tr>
  <tr>
    <td>Content-Transfer-Encoding</td>
    <td>Versión MIME</td>
    <td>A</td>
  </tr>
  <tr>
    <td>Tipo de contenido</td>
    <td>Recibido</td>
    <td>x-sg-eid</td>
  </tr>
  <tr>
    <td>Firma DKIM</td>
    <td>recibido</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### Añadir extras al correo electrónico

Los extras de correo electrónico te permiten enviar datos adicionales a otros proveedores de servicios de correo electrónico. Esto sólo es aplicable a casos de uso avanzado, por lo que sólo debes utilizar los extras de correo electrónico si tu empresa ya lo tiene configurado.

Para añadir extras de correo electrónico, ve a la **Información de envío** y selecciona **Añadir nuevo extra**.

{% alert warning %}
El total de pares clave-valor añadidos no debe superar 1 KB. De lo contrario, se cancelarán los mensajes.
{% endalert %}

Los valores extra del correo electrónico no se publican en Currents ni en Snowflake. Si quieres enviar metadatos adicionales o valores dinámicos a Currents o Snowflake, utiliza [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/) en su lugar.

### Paso 3b: Vista previa y prueba de tu mensaje

Cuando termines de redactar tu correo electrónico perfecto, tienes que probarlo antes de enviarlo. En la parte inferior de la pantalla de resumen, selecciona **Vista previa y Prueba**. 

Aquí puedes tener una vista previa de cómo aparecerá tu correo electrónico en el buzón de entrada de un cliente. Con la vista previa **como usuario** seleccionada, puedes previsualizar tu correo electrónico como un usuario aleatorio, seleccionar un usuario específico o crear un usuario personalizado. Esto te permite comprobar que tu Contenido Conectado y las llamadas de personalización funcionan como deberían. 

A continuación, puedes **Copiar enlace de vista previa** para generar y copiar un enlace de vista previa compartible que muestre el aspecto que tendrá el correo electrónico para un usuario cualquiera. El enlace durará siete días antes de que sea necesario regenerarlo.

También puedes alternar entre las vistas de escritorio, móvil y texto sin formato para hacerte una idea de cómo aparecerá tu mensaje en diferentes contextos.

{% alert tip %}
¿Tienes curiosidad por saber qué aspecto tiene tu correo electrónico para los usuarios del modo oscuro? Selecciona el conmutador de **vista previa de modo** oscuro situado en la sección **Vista previa y prueba** (sólo en el editor de arrastrar y soltar).
{% endalert %}

Cuando estés listo para una comprobación final, selecciona **Prueba de envío** y envía un mensaje de prueba a ti mismo o a un grupo de probadores de contenido para asegurarte de que tu correo electrónico se muestra correctamente en una variedad de dispositivos y clientes de correo electrónico.

\![Prueba la opción Enviar y la vista previa del correo electrónico de ejemplo cuando redactes tu correo electrónico.]({% image_buster /assets/img_archive/newEmailTest.png %})

Si ves algún problema con tu correo electrónico, o quieres hacer algún cambio, selecciona **Editar correo electrónico** para volver al editor.

{% alert tip %}
Los clientes de correo electrónico que admiten texto de vista previa siempre introducen suficientes caracteres para llenar todo el espacio de texto de vista previa disponible. Sin embargo, esto puede dejarte en situaciones en las que el texto de la vista previa esté incompleto o no esté optimizado.
<br><br>Para evitarlo, puedes crear un espacio en blanco después del texto de vista previa que desees, para que los clientes de correo electrónico no introduzcan otros textos o caracteres que distraigan en el contenido del sobre. Para ello, añade una cadena de espacios sin unión de anchura cero (`&zwnj;`) y espacios sin ruptura (`&nbsp;`) después del texto de vista previa que quieras que se muestre. <br><br>Cuando se añade al final de tu texto de vista previa en la sección de preencabezado, el siguiente fragmento de código para el editor HTML añadirá el espacio en blanco que estás buscando:<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```
Para el editor de arrastrar y soltar, añade sólo los no-enlazadores de ancho cero (`&zwnj;`) sin el formato `<div>` directamente en el preencabezado de la sección **Configuración de envío**.

{% endalert %}

### Paso 3c: Comprueba si hay errores en el correo electrónico

El editor señalará cualquier problema que detecte en tu mensaje antes de que lo envíes. Aquí tienes una lista de errores que se tienen en cuenta en nuestro editor:

- **De Nombre para mostrar** y **Encabezado** no especificados juntos
- Direcciones **De** y **Responder a** no válidas
- Claves de **cabecera** duplicadas
- Problemas de sintaxis líquida
- Cuerpos de correo electrónico mayores de 400kb (se recomienda encarecidamente que los cuerpos sean [menores de 102kb]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size))
- Correos electrónicos con el **cuerpo** o el **asunto** en blanco
- Correos electrónicos sin enlace para cancelar suscripción
- El correo electrónico desde el que envías no está en la lista de permitidos (los envíos estarán muy limitados para garantizar la capacidad de entrega).

## Paso 4: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}
A continuación, ¡construye el resto de tu campaña! Consulta las secciones siguientes para obtener más detalles sobre la mejor forma de utilizar nuestras herramientas para crear tu campaña de correo electrónico.

#### Elige el calendario o desencadenar la entrega

Los correos electrónicos se pueden entregar en función de una hora programada, de una acción o de un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

{% alert note %}
Para las campañas desencadenadas por API, cuando la acción desencadenante está configurada como **Interactuar con la campaña**, seleccionar una opción **Recibir** como interacción hará que tu nueva campaña se desencadene en cuanto Braze marque la campaña seleccionada como enviada, aunque ese mensaje rebote o no se entregue.
{% endalert %}

También puedes configurar la duración de la campaña, especificar [las horas tranquilas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours) y establecer normas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Elige los usuarios a los que dirigirte

A continuación, tienes que [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para reducir tu audiencia. Automáticamente obtendrás una vista previa de cómo es la población de ese segmento en este momento, incluyendo cuántos usuarios de ese segmento son localizables a través del correo electrónico. Ten en cuenta que la pertenencia exacta a un segmento siempre se calcula justo antes de enviar el mensaje.

{% multi_lang_include target_audiences.md %}

También puedes elegir enviar tu campaña sólo a usuarios que tengan un [estado de suscripción]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) específico, como los que estén suscritos y hayan optado por el correo electrónico.

Opcionalmente, también puedes limitar la entrega a un número determinado de usuarios dentro del segmento, o permitir que los usuarios reciban el mismo mensaje dos veces al repetirse la campaña.

##### Campañas multicanal con correo electrónico y push

Para las campañas multicanal dirigidas tanto al correo electrónico como a los canales push, puede que quieras limitar tu campaña para que sólo reciban el mensaje los usuarios que hayan optado explícitamente por ello (excluyendo a los usuarios suscritos o dados de baja). Por ejemplo, supongamos que tienes tres usuarios con diferentes estados de adhesión voluntaria:

- **El usuario A** está suscrito al correo electrónico y está habilitado para push. Este usuario no recibe el correo electrónico pero recibirá el push.
- **El usuario B** tiene la adhesión voluntaria al correo electrónico, pero no está habilitado para push. Este usuario recibirá el correo electrónico pero no recibe el push.
- **El usuario C** ha optado por la adhesión voluntaria al correo electrónico y está habilitado para push. Este usuario recibirá tanto el correo electrónico como el push.

Para ello, en **Resumen de audiencia**, selecciona enviar esta campaña a "sólo usuarios con adhesión voluntaria". Esta opción comprobará que sólo los usuarios con adhesión voluntaria recibirán tu correo electrónico, y Braze sólo enviará tu push a los usuarios que estén habilitados para push de forma predeterminada.

{% alert important %}
Con esta configuración, no incluyas ningún filtro en el paso **Audiencias objetivo** que limite la audiencia a un único canal (por ejemplo, `Foreground Push Enabled = True` o `Email Subscription = Opted-In`).
{% endalert %}

#### Elige eventos de conversión

Braze te permite hacer un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), después de recibir una campaña. Puedes especificar cualquiera de las siguientes acciones como evento de conversión:

- Abre la aplicación
- Realiza una compra (Puede ser una compra genérica o un artículo específico)
- Realiza un evento personalizado específico
- Abre el correo electrónico

Puedes permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada. Aunque Braze realiza un seguimiento automático de las aperturas y clics de tu campaña, es posible que desees configurar el evento de conversión para que se produzca cuando un usuario abra o haga clic en una dirección de correo electrónico para aprovechar las ventajas de [Intelligent Selection]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).
{% endtab %}

{% tab Canvas %}
Si aún no lo has hecho, completa las secciones restantes de tus componentes de Canvas. Para más detalles sobre cómo construir el resto de tu Canvas, implementar pruebas multivariantes e Intelligent Selection, y más, consulta el paso [Construye tu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nuestra documentación sobre Canvas.
{% endtab %}
{% endtabs %}

## Paso 5: Revisar y desplegar

La sección final te ofrecerá un resumen de la campaña que acabas de diseñar. Confirma todos los datos relevantes y selecciona **Lanzar campaña**. Ahora, ¡es hora de esperar a que lleguen todos los datos! 

Para saber cómo puedes acceder a los resultados de tus campañas por correo electrónico, consulta [Informes por correo electrónico]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/).

