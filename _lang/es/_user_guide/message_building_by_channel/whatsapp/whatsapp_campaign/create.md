---
nav_title: Crear un mensaje de WhatsApp
article_title: Crear un mensaje de WhatsApp
page_order: 0
description: "Este artículo de referencia cubre los pasos necesarios para crear un mensaje de WhatsApp."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
search_rank: 1
---

# Crear un mensaje de WhatsApp

> Las campañas de WhatsApp son ideales para llegar directamente a sus clientes y conversar con ellos de forma programática. Puede utilizar Liquid y otros contenidos dinámicos para crear una experiencia personal con sus usuarios y crear un entorno que fomente y mejore una experiencia discreta del usuario con su marca. 

## Requisitos previos

Antes de poder crear mensajes de WhatsApp, tienes que revisar y completar lo siguiente del [resumen de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/):
  - Reconocer las políticas, los límites y las normas de contenido
  - Configura tu conexión de WhatsApp
  - Elabore plantillas iniciales en Meta para utilizarlas en sus mensajes

## Crear un mensaje

### Paso 1: Elige dónde construir tu mensaje

{% alert note %}
WhatsApp crea [plantillas de mensajes](#template-messages) diferentes para cada idioma. O bien crea una campaña para cada idioma con segmentación para servir la plantilla correcta a los usuarios, o bien utiliza Canvas.
{% endalert %}

¿No estás seguro de si tu mensaje debe enviarse mediante una campaña o un Canvas? Las campañas son mejores para campañas de mensajería únicas y específicas, mientras que los lienzos son mejores para recorridos de usuario de varios pasos.

{% tabs %}
{% tab Campaign %}

**Pasos:**

1. Vaya a la página **Campañas** y haga clic en <i class="fas fa-plus"></i> **Crear campaña**.
2. Seleccione **WhatsApp** o, para campañas dirigidas a varios canales, seleccione **Campaña multicanal**.
3. Ponle a tu campaña un nombre claro y significativo.
4. Añada [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) y [etiquetas]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) según sea necesario.
   * Las etiquetas facilitan la búsqueda de sus campañas y la elaboración de informes a partir de ellas. Por ejemplo, al utilizar el [Generador de informes]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), puede filtrar por etiquetas concretas.
5. Añade y nombra tantas variantes como necesites para tu campaña. Puede elegir diferentes plataformas, tipos de mensaje y diseños para cada una de sus variantes añadidas. Para saber más sobre este tema, consulta [Multivariante y pruebas A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

{% alert tip %}
Si todos los mensajes de su campaña son similares o tienen el mismo contenido, redacte su mensaje antes de añadir variantes adicionales. A continuación, puede seleccionar **Copiar de variante** en el desplegable **Añadir variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Pasos:**

1. [Cree su lienzo]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) utilizando el compositor de lienzos.
2. Una vez que haya configurado su lienzo, añada un paso en el constructor de lienzos. Nombra tu paso con algo claro y significativo.
3. Elija un [programa de pasos]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) y especifique un retraso según sea necesario.
4. Filtra tu audiencia para este paso, según sea necesario. Puede afinar aún más los destinatarios de este paso especificando segmentos y añadiendo filtros adicionales. Las opciones de audiencia se comprobarán después del retraso en el momento de enviar los mensajes.
5. Elige tu [comportamiento de avance]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Elige cualquier otro canal de mensajería que quieras asociar a tu mensaje.

{% alert tip %}
Si un Canvas basado en acciones es desencadenado por un mensaje entrante de WhatsApp, puedes hacer referencia a las propiedades de WhatsApp en cualquier paso en Canvas hasta la siguiente ruta de acción.
{% endalert %}

{% endtab %}
{% endtabs %}

### Paso 2: Redacta tu mensaje de WhatsApp

Selecciona si quieres crear un [mensaje de plantilla de](#template-messages) WhatsApp o un mensaje de respuesta, dependiendo de tu caso de uso. Cualquier conversación iniciada por la empresa debe partir de una plantilla aprobada, mientras que los mensajes de respuesta pueden utilizarse en respuestas a mensajes entrantes de usuarios dentro de un plazo de 24 horas.

![La sección Variantes de mensajes le permite seleccionar un grupo de suscripción y uno de los dos tipos de mensajes: Plantilla de mensaje de WhatsApp y mensaje de respuesta.]({% image_buster /assets/img/whatsapp/whatsapp_message_variants.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Template messages %}

Puede utilizar [mensajes de plantilla de WhatsApp aprobados]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-3-create-whatsapp-templates
) para iniciar conversaciones con sus usuarios en WhatsApp. Estos mensajes se envían previamente a WhatsApp para que apruebe su contenido, lo que puede tardar hasta 24 horas en aprobarse. Cualquier modificación que hagas en la copia debe ser editada y reenviada a WhatsApp.

Los campos de texto deshabilitados (resaltados en gris) no pueden editarse, ya que forman parte de la plantilla de WhatsApp aprobada. Para actualizar el texto desactivado, debe editar su plantilla y volver a aprobarla.

#### Idiomas

Cada plantilla tiene un idioma asignado, por lo que es necesario crear una campaña o paso de Canvas para cada idioma para configurar correctamente la correspondencia de usuarios. Por ejemplo, si está creando un lienzo que utiliza plantillas asignadas con el indonesio y el inglés, necesita crear un paso de lienzo para la plantilla indonesia y un paso de lienzo para la plantilla inglesa.

![Lista de plantillas con previsualización de sus mensajes, idiomas asignados y estado de aprobación.]({% image_buster /assets/img/whatsapp/whatsapp_templates.png %}){: style="max-width:80%;"}

Si añades texto en un idioma escrito de derecha a izquierda, ten en cuenta que el aspecto final de los mensajes escritos de derecha a izquierda depende en gran medida de cómo los rendericen los proveedores de servicios. Para conocer las mejores prácticas de elaboración de mensajes de derecha a izquierda que se muestren con la mayor precisión posible, consulta [Crear mensajes de derecha a izquierda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

#### Variables

Si has añadido variables al crear la plantilla de WhatsApp en el Meta Business Manager, esas variables aparecerán como espacios en blanco en el compositor del mensaje. Sustituya estos espacios en blanco por Liquid o texto sin formato. Para utilizar texto sin formato, utilice el formato "texto aquí" entre llaves dobles. Si has optado por incluir imágenes al crear tu plantilla, puedes cargar o añadir imágenes desde la biblioteca de medios o haciendo referencia a una URL de imagen. Cuando sea posible, te recomendamos que subas las imágenes directamente a tu biblioteca multimedia para garantizar la coherencia y la fiabilidad.

Tenga en cuenta que los campos de texto desactivados (resaltados en gris) no pueden editarse, ya que forman parte de la plantilla de WhatsApp aprobada. Si desea actualizar el texto desactivado, debe editar su plantilla y volver a aprobarla.

{% alert tip %}
{% raw %}
Si piensa utilizar Liquid, asegúrese de incluir un valor predeterminado para la personalización elegida, de modo que en caso de que el perfil de usuario del destinatario esté incompleto, no reciba el mensaje. Los mensajes en los que falten variables de Liquid no serán enviados por WhatsApp.
{% endraw %}
{% endalert %}

![La herramienta Añadir personalización con el atributo "first_name" y el valor predeterminado "tú".]({% image_buster /assets/img/whatsapp/whatsapp7.png %}){: style="max-width:80%;"}

### Enlaces dinámicos 

Las URL de llamada a la acción pueden contener variables, aunque Meta exige que estén al final de la URL, como `{% raw %}https://example.com/{{variable}}{% endraw %}`, donde la variable puede sustituirse en Braze por Liquid. Los enlaces también pueden incluirse en el cuerpo del texto como parte de la plantilla. Ambos enlaces pueden acortarse y seguirse mediante [el seguimiento de clics]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/).

### Imágenes dinámicas

{% multi_lang_include alerts/important_alerts.md alert='dynamic image URL' %}

{% endtab %}
{% tab Response messages %}

Puedes utilizar los mensajes de respuesta para contestar a los mensajes entrantes de tus usuarios. Estos mensajes se crean in-app en Braze durante tu experiencia de composición y pueden editarse en cualquier momento. Puede utilizar Liquid para adaptar el idioma de los mensajes de respuesta a los usuarios adecuados.

Hay cinco diseños de mensajes de respuesta que puedes utilizar:
- Respuesta rápida
- Mensaje de texto
- Mensaje con medios
- Botón de llamada a la acción
- Mensaje de la lista

![El compositor del mensaje de respuesta para un Mensaje de Respuesta que da la bienvenida a nuevos usuarios con un código de descuento.]({% image_buster /assets/img/whatsapp/whatsapp_response_messages.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

### Paso 3: Vista previa y prueba de tu mensaje

Braze recomienda siempre previsualizar y probar el mensaje antes de enviarlo. Cambie a la pestaña **Prueba** para enviar un mensaje de WhatsApp de prueba a [grupos de prueba de contenido]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) o a usuarios individuales, o previsualice el mensaje como usuario directamente en Braze.

![Un mensaje de vista previa para un usuario personalizado llamado Max.]({% image_buster /assets/img/whatsapp/whatsapp8.png %}){: style="max-width:80%;"}

{% alert note %}
Se necesita una ventana de conversación para enviar mensajes de respuesta, incluidos los mensajes de prueba. Para iniciar una ventana de conversación, envía un mensaje de WhatsApp al número de teléfono asociado al grupo de suscripción que estás utilizando para este mensaje. El número de teléfono asociado aparece en la alerta de la pestaña **Prueba**.
{% endalert %}

![Una alerta que dice: "Para probar, abre primero una ventana de conversación enviando un mensaje de WhatsApp al +1 217-582-9414. Luego, envía tu mensaje de respuesta al usuario de prueba."]({% image_buster /assets/img/whatsapp/whatsapp_test_phone_number.png %}){: style="max-width:70%;"}

### Paso 4: Construye el resto de tu campaña o Canvas

{% tabs %}
{% tab Campaign %}

A continuación, ¡construye el resto de tu campaña! Consulte las secciones siguientes para obtener más información sobre la mejor manera de utilizar nuestras herramientas para crear mensajes de WhatsApp.

#### Elige la programación o desencadenante de la entrega

Los mensajes de WhatsApp pueden entregarse en función de una hora programada, una acción o un desencadenante de la API. Para más información, consulta [Programar tu campaña]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para la entrega basada en acciones, también puedes configurar la duración de la campaña y [las horas tranquilas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

En este paso también puede especificar controles de entrega, como permitir que los usuarios [vuelvan a ser elegibles]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para recibir la campaña o activar reglas de [limitación de frecuencia]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Elige los usuarios a los que dirigirte

A continuación, debes [dirigirte a los usuarios]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) eligiendo segmentos o filtros para limitar tu audiencia. Ya deberías haber elegido el grupo de suscripción, que restringe a los usuarios según el nivel o categoría de comunicación que quieren tener contigo. En este paso, seleccionas la audiencia más amplia de tus segmentos y acotas aún más ese segmento con nuestros filtros. Automáticamente recibirás una instantánea de cómo es esa población aproximada de segmentos. Recuerda que la pertenencia exacta a un segmento siempre se calcula antes de enviar el mensaje.

{% multi_lang_include target_audiences.md %}

#### Elegir eventos de conversión

Braze le permite realizar un seguimiento de la frecuencia con la que los usuarios realizan acciones específicas, [eventos de conversión]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), tras recibir una campaña. Puede permitir una ventana de hasta 30 días durante la cual se contabilizará una conversión si el usuario realiza la acción especificada.

También puede establecer eventos de conversión personalizados basados en su caso de uso específico. Sea creativo y piense cómo quiere medir realmente el éxito de esta campaña.

{% endtab %}

{% tab Canvas %}

Si aún no lo ha hecho, complete las secciones restantes de su componente Canvas. Para más detalles sobre cómo construir el resto de su Canvas, implementar pruebas multivariantes y Selección Inteligente, y más, consulte el paso [Construya su Canvas]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/) de nuestra documentación de Canvas.

Dado que las ventanas de conversación sólo pueden durar 24 horas por mensaje entrante, Braze comprobará que no haya retrasos superiores a 24 horas entre un mensaje entrante y un mensaje de respuesta. 

{% endtab %}
{% endtabs %}

### Paso 5: Revisar y desplegar

Cuando hayas terminado de crear lo último de tu campaña o Canvas, revisa sus detalles, pruébala y ¡envíala!

A continuación, consulta [los informes de WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign_analytics/) para saber cómo puedes acceder a los resultados de tus campañas de WhatsApp.

## Funciones de WhatsApp compatibles

### Mensajes salientes

Las siguientes características son compatibles con los mensajes salientes de WhatsApp que envíes a través de Braze:

| Característica | Detalles | Tamaño máximo | Formatos admitidos |
| ------- | ------- | ------------- | ---------------------- |
| Texto de cabecera | Se admiten cadenas y parámetros variables. | - | -
| Cuerpo del texto | Se admiten cadenas y parámetros variables. | - | - |
| Texto a pie de página | Se admiten cadenas y parámetros variables. | - | - |
| Enlaces CTA | Se admiten varios tipos de llamada a la acción (CTA). Para más detalles, consulta [Tipos de llamada a la acción](#ctas). | - | - |
| Imágenes | Las imágenes pueden incrustarse dentro del cuerpo del texto. Deben ser de 8 bits y utilizar un modelo de color RGB o RGBA. | < 5 MB | `.png`, `.jpg`, `.jpeg` |
| Documentos | Los documentos pueden incrustarse en el cuerpo del texto. Los archivos deben alojarse a través de la URL. | < 100 MB | `.txt`, `.xls`, `.xlsx`, `.doc`, `.docx`, `.ppt`, `.pttx`, `.pdf` |
| Vídeos | Los videos se pueden incrustar en el cuerpo del texto. Los archivos deben estar alojados a través de URL o en la [biblioteca multimedia de Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library). | < 16 MB | `.3gp`, `.mp4` |
| Audio | El audio sólo se admite a través de la mensajería de respuesta. Los archivos deben alojarse a través de la URL. | < 16 MB | `.aac`, `.amr`, `.mp3`, `.mp4`, `.ogg` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
Meta tiene un problema conocido que puede impedir que algunos videos MP4 se reproduzcan en dispositivos Android debido a una configuración específica de codificación o contenedor. Hasta que se disponga de una solución permanente, reformatear el archivo MP4 resuelve el problema para la mayoría de los remitentes. Prueba todos los videos en dispositivos Android para confirmar la correcta capacidad de entrega. <br><br>Puedes reformatear el archivo MP4 mediante una herramienta Web, como [CloudConvert](https://cloudconvert.com/mp4-converter). Sube tu archivo MP4 a la herramienta, conviértelo de nuevo a MP4 y, a continuación, descarga el archivo convertido.
{% endalert %}

### Mensajes entrantes

Las siguientes características son compatibles con los mensajes entrantes de WhatsApp que recibas a través de Braze:

| Característica | Detalles | Formatos admitidos |
| ------- | ------- | ------------------ |
| Cuerpo del texto | Sólo se admiten cadenas estándar. | - |
| Imágenes | Las imágenes deben ser de 8 bits y utilizar un modelo de color RGB o RGBA. Los archivos deben tener menos de 5 MB. | `.jpg`, `.png` |
| Audio | Sólo son compatibles los archivos Ogg codificados con el códec Opus. Otros formatos Ogg no lo son. | `.aac`, `.mp4`, `.mpeg`, `.amr`, `.ogg (Opus only)` |
| Documentos | La documentación se facilita adjuntando mensajes. | `.txt`, `.pdf`, `.ppt`, `.doc`, `.xls`, `.docx`, `.pptx`, `.xlsx` |
| Video | Solo admite el códec de video H.264 y el códec de audio AAC. Los videos deben tener un único flujo de audio o no tener flujo de audio. | `.mp4`, `.3gp` |
| Enlaces CTA | Se admiten varios tipos de llamada a la acción (CTA). Para más detalles, consulta [Tipos de llamada a la acción](#ctas). | - |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Tipos de llamada a la acción {#ctas}

Los siguientes tipos de llamada a la acción son compatibles con los mensajes de WhatsApp que envíes a través de Braze:

| Tipo de CTA    | Detalles |
| ----------- |---------------- | 
| Visitar el sitio web | Un botón como máximo (incluidos los parámetros variables). |
| Llamar al número de teléfono | Disponible sólo para plantillas de mensajes. <br>Un botón como máximo. |
| Botones personalizados de respuesta rápida | Tres botones como máximo. |
| Botón de cancelación de marketing | Por defecto, los estados de suscripción no se actualizan automáticamente. Para más información, consulta [Adhesiones voluntarias & Opt-Outs]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#marketing-opt-out-selection). |
| Plantillas de mensajes de código de cupón | Disponible sólo para plantillas de mensajes. <br>Se pueden abrir y editar como otras plantillas de mensajes, y son compatibles con los códigos promocionales Liquid y Braze. |
| Mensajes de respuesta CTA  | Crea un mensaje de respuesta que incluya un botón de llamada a la acción. |
| [Lista de mensajes de respuesta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#list-messages) | Crea un mensaje de respuesta que incluya una lista de hasta 10 opciones para que los usuarios elijan. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

