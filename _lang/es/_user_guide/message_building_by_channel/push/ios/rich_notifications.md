---
nav_title: "Crear notificaciones enriquecidas"
article_title: "Crear notificaciones push enriquecidas para iOS"
page_order: 3
page_type: tutorial
description: "Este tutorial cubre los requisitos y pasos sobre cómo crear notificaciones enriquecidas de iOS para tus campañas Braze."

platform: iOS
channel:
  - push
tool:
  - Campaigns

---

# Crear notificaciones push enriquecidas para iOS

> Las notificaciones enriquecidas permiten una mayor personalización de tus notificaciones push añadiendo contenido adicional más allá del texto. Desde hace algún tiempo, las notificaciones de Android incluyen imágenes en las notificaciones push, con mensajes como "Imagen de notificación ampliada". A partir de iOS 10, tus clientes podrán recibir notificaciones push de iOS que incluyan GIFs, imágenes, videos o audio.

## Requisitos previos

Antes de crear una notificación push enriquecidas para iOS, ten en cuenta los siguientes detalles:

- Para asegurarte de que tu aplicación puede enviar notificaciones enriquecidas, sigue las instrucciones de [integración push de iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications), ya que tu desarrollador tendrá que añadir una extensión de servicio a tu aplicación.
- Los tipos de archivo que actualmente admitimos para la carga directa en nuestro panel son JPEG, PNG o GIF. Estos archivos también pueden introducirse en el campo URL de la plantilla junto con estos tipos de archivos adicionales: AIF, M4A, MP3, MP4 o WAV.
- Consulta [la documentación de Apple](https://developer.apple.com/reference/usernotifications/unnotificationattachment) para conocer las limitaciones y especificaciones de los soportes.
- Las notificaciones push enriquecidas de iOS no están disponibles al crear una campaña push rápida.
- iOS escalará las imágenes para que quepan en la pantalla y escalará las imágenes enriquecidas para la vista activa o bloqueada.

{% alert note %}
A partir de enero de 2020, las notificaciones push enriquecidas de iOS pueden manejar imágenes de 1038x1038 que no superen los 10 MB, pero recomendamos utilizar un tamaño de archivo lo más pequeño posible. En la práctica, enviar archivos de gran tamaño puede causar una tensión innecesaria en la red y hacer que los tiempos de espera de descarga sean más frecuentes.
{% endalert %}

### Recuento de caracteres

Aunque no podemos proporcionar una regla rígida y rápida sobre el número exacto de caracteres que se deben incluir en un push, [proporcionamos algunas directrices]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/) a tener en cuenta al diseñar mensajes para iOS. Puede haber alguna variación según la presencia de una imagen, el estado de notificación y la configuración de visualización del dispositivo del usuario, y el tamaño del dispositivo. En caso de duda, hazlo breve y dulce.

Como mejor práctica, Braze recomienda mantener cada línea de texto, tanto para el título opcional como para el cuerpo del mensaje, en aproximadamente 30-40 caracteres en una notificación push móvil.

#### Estados de notificación

Tus usuarios pueden ver las notificaciones push en una variedad de situaciones diferentes, y podrían ver diferentes longitudes de texto, como se indica a continuación.

<table>
<thead>
  <tr>
    <th>Pantalla de bloqueo o Centro de notificaciones</th>
    <th>Ampliado</th>
    <th>Dispositivo activo</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td width="33%">Éste es el escenario más habitual.<br><br><b>Título:</b> 1 línea de texto<br><b>Cuerpo:</b> 4 líneas de texto<br><b>Imagen:</b> miniatura cuadrada</td>
    <td width="33%">Cuando un usuario pulsa prolongadamente un mensaje.<br><br><b>Título:</b> 1 línea de texto<br><b>Cuerpo:</b> 7 líneas de texto<br><b>Imagen:</b> Relación de aspecto 2:1 (recomendada, ver nota siguiente)</td>
    <td width="33%">Cuando un usuario recibe un push mientras su teléfono está desbloqueado y activo.<br><br><b>Título:</b> 1 línea de texto<br><b>Cuerpo:</b> 2 líneas de texto</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

\![Ejemplo de notificaciones push para push mostradas en la pantalla de bloqueo, cuando se expanden y cuando el dispositivo está activo.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Aunque recomendamos una relación de aspecto de 2:1 para las notificaciones push ampliadas, se admite casi cualquier relación de aspecto. Las imágenes siempre ocuparán toda la anchura de la notificación, y la altura se ajustará en consecuencia.
{% endalert %}

#### Variables en el truncamiento de texto

Cuando crees contenido, ten en cuenta los siguientes escenarios que pueden afectar a la cantidad de texto que se muestra.

{% tabs %}
{% tab Timing %}

Dependiendo del momento en que un usuario interactúa con una notificación push, la marca de tiempo puede acortar el texto del título.

\![Ejemplo de notificación push con una marca de tiempo de "ahora" y un título de 35 caracteres.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Número de caracteres del título: **35**

Ejemplo de notificación push con una marca de tiempo de "hace 3 horas" y un título de 33 caracteres.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Número de caracteres del título: **33**

\![Ejemplo de notificación push con una marca de tiempo de "Ayer, 8:37 AM" y un título de 22 caracteres.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Número de caracteres del título: **22**

{% endtab %}
{% tab Images %}

El cuerpo del texto se acorta unos 10 caracteres por línea cuando hay una imagen.

\![Ejemplo de notificación push sin imagen y con un cuerpo de 179 caracteres.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Número de caracteres del cuerpo: **179**

\![Ejemplo de notificación push con una imagen y un cuerpo de 154 caracteres.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Número de caracteres del cuerpo: **154**

{% endtab %}
{% tab Interruption level %}

Para iOS 15, las denotaciones Sensible al tiempo y Crítico empujan el título a una nueva línea sin la marca de tiempo, dándole un poco más de espacio.

\![Ejemplo de notificación push sin indicación de Tiempo sensible o Crítico y con un título de 35 caracteres.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Número de caracteres del título: **35**

\![Ejemplo de notificación push con una denotación Sensible al tiempo y un título de 39 caracteres.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Número de caracteres del título: **39**

{% endtab %}
{% tab More %}

Los siguientes detalles también pueden influir en el truncamiento del texto:

- **Configuración de la pantalla del teléfono:** un usuario puede aumentar o disminuir el tamaño de la fuente de la IU global de su teléfono, normalmente por razones de accesibilidad.
- **Ancho del dispositivo:** el mensaje podría mostrarse en un teléfono pequeño o en un iPad ancho.
- **Tipos de contenido:** los emojis y los caracteres anchos como la "m" y la "w" ocupan más espacio que la "i" o la "t", y las palabras más largas como "interacción" pueden tener un salto de línea más brusco que las palabras más cortas.

{% endtab %}
{% endtabs %}

## Configuración de las notificaciones enriquecidas de iOS

### Paso 1: Crear una campaña push

Sigue los [pasos de la campaña]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message) para redactar una notificación push para iOS. Utilizarás el mismo compositor que usas para configurar las notificaciones push que no contienen contenido enriquecido.

### Paso 2: Añadir medios

Añade tu archivo de imagen, GIF, audio o video en el campo **Medios de notificación enriquecida** del redactor del mensaje. Consulta los [requisitos](#requirements) sobre cómo añadir tus archivos de contenido.

\![Ejemplo de texto resumido para una notificación push.]({% image_buster /assets/img_archive/rich_notification_add_image.png %}){: style="max-width:70%;" }

También puedes limitar este mensaje para que sólo se envíe a usuarios que tengan un dispositivo que funcione con iOS 10. Para los usuarios que no hayan actualizado a iOS 10, aparecerán como notificaciones de sólo texto sin el contenido enriquecido si dejas sin marcar la opción **Sólo enviar a dispositivos compatibles con notificaciones enriquecidas**.

La sección Ampliada de la imagen de notificación, donde puedes añadir una imagen o introducir una URL de imagen.]({% image_buster /assets/img_archive/rich_notification_ios10_select.png %}){: style="max-width:70%;" }

### Paso 3: Sigue creando tu campaña

Una vez cargado el contenido de tu notificación enriquecida en el panel, puedes seguir [programando tu campaña]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign).

Cuando un usuario recibe la notificación push, puede pulsar con fuerza sobre el mensaje push para ampliar la imagen.

\![Un usuario recibe una notificación push y pulsa con fuerza el mensaje para mostrar una imagen expandida que dice "¡Hola!".]({% image_buster /assets/img_archive/rich_notification_ios.gif %}){: style="max-width:50%;" }

