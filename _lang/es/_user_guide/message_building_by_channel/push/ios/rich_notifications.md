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

> Las notificaciones enriquecidas permiten una mayor personalización de las notificaciones push añadiendo contenido adicional al texto. Desde hace algún tiempo, las notificaciones de Android incluyen imágenes en las notificaciones push, enviadas como "Imagen de notificación ampliada". A partir de iOS 10, tus clientes podrán recibir notificaciones push de iOS que incluyan GIF, imágenes, vídeos o audio.

## Requisitos previos

Antes de crear una notificación push enriquecidas para iOS, ten en cuenta los siguientes detalles:

- Para asegurarte de que tu aplicación puede enviar notificaciones enriquecidas, sigue las instrucciones de [integración push de iOS][1], ya que tu desarrollador tendrá que añadir una extensión de servicio a tu aplicación.
- Los tipos de archivo que actualmente admitimos para la carga directa en nuestro panel de control son JPEG, PNG o GIF. Estos archivos también pueden introducirse en el campo de URL planificable junto con estos tipos de archivo adicionales: AIF, M4A, MP3, MP4 o WAV.
- Consulta [la documentación de Apple][2] para conocer las limitaciones y especificaciones de los soportes.
- Las notificaciones enriquecidas de iOS no están disponibles al crear una campaña push rápida.
- iOS escalará las imágenes para que quepan en la pantalla y escalará las imágenes enriquecidas para la vista activa o bloqueada.

{% alert note %}
A partir de enero de 2020, las notificaciones push enriquecidas de iOS pueden gestionar imágenes de 1038x1038 que no superen los 10 MB, pero recomendamos utilizar un tamaño de archivo lo más pequeño posible. En la práctica, el envío de archivos de gran tamaño puede causar un estrés innecesario en la red y hacer que los tiempos de espera de descarga sean más frecuentes.
{% endalert %}

### Recuento de caracteres

Aunque no podemos ofrecer una regla rígida y rápida sobre el número exacto de caracteres que se deben incluir en un mensaje push, [ofrecemos algunas directrices]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/message_format/) que se deben tener en cuenta al diseñar mensajes para iOS. Puede haber alguna variación en función de la presencia de una imagen, el estado de la notificación y la configuración de visualización del dispositivo del usuario, y el tamaño del dispositivo. En caso de duda, sé conciso y amable.

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
    <td width="33%">Este es el escenario más común.<br><br><b>Título,</b> 1 línea de texto<br><b>Cuerpo:</b> 4 líneas de texto<br><b>Imagen:</b> miniatura cuadrada</td>
    <td width="33%">Cuando un usuario mantiene pulsado un mensaje.<br><br><b>Título,</b> 1 línea de texto<br><b>Cuerpo:</b> 7 líneas de texto<br><b>Imagen:</b> Relación de aspecto 2:1 (recomendada, véase la nota siguiente)</td>
    <td width="33%">Cuando un usuario recibe un push mientras su teléfono está desbloqueado y activo.<br><br><b>Título,</b> 1 línea de texto<br><b>Cuerpo:</b> 2 líneas de texto</td>
  </tr>
</tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 }

![Ejemplo de notificaciones push para push mostradas en la pantalla de bloqueo, cuando se expanden y cuando el dispositivo está activo.]({% image_buster /assets/img_archive/push_ios_notification_states.png %})

{% alert note %}
Aunque recomendamos una relación de aspecto de 2:1 para las notificaciones push ampliadas, se admite casi cualquier relación de aspecto. Las imágenes siempre ocuparán toda la anchura de la notificación, y la altura se ajustará en consecuencia.
{% endalert %}

#### Variables en el truncamiento de texto

Al crear contenidos, tenga en cuenta los siguientes escenarios que pueden afectar a la cantidad de texto que se muestra.

{% tabs %}
{% tab Temporización %}

En función del momento en que un usuario se conecta a una notificación push, la marca de tiempo puede acortar el texto del título.

![Ejemplo de notificación push con una marca de tiempo de "ahora" y un título de 35 caracteres.]({% image_buster/assets/img_archive/push_ios_timing_35.png %})
<br>Número de caracteres del título: **35**

![Ejemplo de notificación push con una marca de tiempo de "hace 3 horas" y un título de 33 caracteres.]({% image_buster/assets/img_archive/push_ios_timing_33.png %})
<br>Número de caracteres del título: **33**

![Ejemplo de notificación push con una fecha y hora de "Ayer, 8:37 AM" y un título de 22 caracteres.]({% image_buster/assets/img_archive/push_ios_timing_22.png %})
<br>Número de caracteres del título: **22**

{% endtab %}
{% tab Imágenes %}

El cuerpo del texto se acorta unos 10 caracteres por línea cuando hay una imagen.

![Ejemplo de notificación push sin imagen y con un cuerpo de 179 caracteres.]({% image_buster/assets/img_archive/push_ios_images_179.png %})
<br>Número de caracteres del cuerpo: **179**

![Ejemplo de notificación push con una imagen y un cuerpo de 154 caracteres.]({% image_buster/assets/img_archive/push_ios_images_154.png %})
<br>Número de caracteres del cuerpo: **154**

{% endtab %}
{% tab Nivel de interrupción %}

Para iOS 15, las denotaciones Sensible al tiempo y Crítico empujan el título a una nueva línea sin la marca de tiempo, dándole un poco más de espacio.

![Ejemplo de notificación push sin indicación de tiempo sensible o crítico y con un título de 35 caracteres.]({% image_buster/assets/img_archive/push_ios_interruption_level_35.png %})
<br>Número de caracteres del título: **35**

![Ejemplo de notificación push con una denotación Time Sensitive y un título de 39 caracteres.]({% image_buster/assets/img_archive/push_ios_interruption_level_39.png %})
<br>Número de caracteres del título: **39**

{% endtab %}
{% tab Más %}

Los siguientes detalles también pueden influir en el truncamiento del texto:

- **Ajustes de visualización del teléfono:** un usuario puede aumentar o reducir el tamaño de la fuente de la interfaz de usuario global en su teléfono, normalmente por razones de accesibilidad.
- **Anchura del dispositivo:** el mensaje podría mostrarse en un teléfono pequeño o en un iPad ancho.
- **Tipos de contenido:** los emojis y los caracteres anchos como la "m" y la "w" ocupan más espacio que la "i" o la "t", y las palabras largas como "compromiso" pueden tener un salto de línea más abrupto que las palabras cortas.

{% endtab %}
{% endtabs %}

## Configuración de las notificaciones enriquecidas de iOS

### Paso 1: Crear una campaña push

Sigue los [pasos de la campaña][3] para redactar una notificación push para iOS. Utilizará el mismo compositor que utiliza para configurar las notificaciones push que no contienen contenido enriquecido.

### Paso 2: Añadir medios

Añada su archivo de imagen, GIF, audio o vídeo en el campo **Rich Notification Media** del redactor del mensaje. Consulte los [requisitos](#requirements) sobre cómo añadir sus archivos de contenido.

![Un ejemplo de texto resumido para una notificación push.][4]{: style="max-width:70%;" }

También puedes limitar este mensaje para que solo se envíe a usuarios que tengan un dispositivo con iOS 10. Para los usuarios que no hayan actualizado a iOS 10, aparecerá como notificaciones de solo texto sin el contenido enriquecido si dejas desmarcada la opción **Solo enviar a dispositivos compatibles con notificaciones enriquecidas**.

![La sección Imagen de notificación ampliada, donde puedes añadir una imagen o introducir una URL de imagen.][5]{: style="max-width:70%;" }

### Paso 3: Sigue creando tu campaña

Una vez cargado el contenido de tu notificación enriquecida en el panel, puedes continuar [programando tu campaña][6].

Cuando un usuario recibe la notificación push, puede pulsar con fuerza sobre el mensaje push para ampliar la imagen.

![Un usuario recibe una notificación push y pulsa con fuerza el mensaje para mostrar una imagen expandida que dice "¡Hola!".][8]{: style="max-width:50%;" }

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#ios-10-rich-notifications
[2]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
[3]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[4]: {% image_buster /assets/img_archive/rich_notification_add_image.png %}
[5]: {% image_buster /assets/img_archive/rich_notification_ios10_select.png %}
[6]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#schedule-push-campaign
[8]: {% image_buster /assets/img_archive/rich_notification_ios.gif %}
