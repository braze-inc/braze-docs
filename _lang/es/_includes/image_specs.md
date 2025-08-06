{% if include.variable_name == "image behavior" %}


| Diseño | Comportamiento |
| --- | --- |
| Imagen y texto | Las imágenes altas o estrechas se reducirán y se centrarán horizontalmente. Las imágenes anchas se recortarán por los bordes izquierdo y derecho. |
| Solo imagen | El mensaje cambiará de tamaño para adaptarse a imágenes de la mayoría de las relaciones de aspecto. |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "payload size" %}

Recomendamos los siguientes tamaños de carga útil:

| Sistema de mensajería | Carga útil recomendada |
| --- | --- |
| iOS (pre-iOS 8) | 0,256 KB |
| iOS (post-iOS 8) | 2 KB |
| Android (FCM) | 4 KB |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "in-app messages" %}

Los mensajes modales dentro de la aplicación están diseñados para ajustarse al dispositivo en las proporciones mejores y más llenas posibles, al tiempo que se mantienen fieles al tamaño y las proporciones de la imagen o el texto que elijas para tu mensaje.

Aunque no hay límites en cuanto al número de caracteres de texto que puedes incluir en un mensaje dentro de la aplicación (así como en los botones, el titular, el cuerpo principal y otros), moderamos el número de caracteres de texto que utilizas. Demasiado texto obligará a los usuarios a ampliar y desplazar el mensaje.

Todos los mensajes dentro de la aplicación tienen un tamaño de imagen recomendado de 500 KB, un tamaño de imagen máximo de 5 MB y admiten los tipos de archivo PNG, JPEG y GIF.

{% tabs %}
{% tab Retrato %}

| Tipo | Relación de aspecto | Calidad de imagen | Notas |
| --- | --- | --- | --- |
| Retrato a pantalla completa con texto | 6:5 | Alta resolución 1200 x 1000 px <br>Resolución mínima 600 x 500 px | Se puede recortar por todos los lados, pero la imagen siempre ocupará el 50% superior de la ventana. |
| Retrato a pantalla completa (sólo imagen, con o sin botones) | 3:5 | Alta resolución 1200 x 2000 px <br> Resolución mínima 600 x 1000 px | El recorte puede producirse en los bordes izquierdo y derecho en los dispositivos más altos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Horizontal %}

| Tipo | Relación de aspecto | Calidad de imagen | Notas |
| --- | --- | --- | --- |
| Pantalla completa apaisada con texto | 10:3 | Alta resolución 2000 x 600 px <br>Resolución mínima 1000 x 300 px | Se puede recortar por todos los lados, pero la imagen siempre ocupará el 50% superior de la ventana. |
| Pantalla completa apaisada (sólo imagen, con o sin botones) | 5:3 | Alta resolución 2000 x 600 px <br> Resolución mínima 1000 x 600 px | El recorte puede producirse en los bordes izquierdo y derecho en los dispositivos más altos. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Deslizamiento hacia arriba %}

| Tipo | Relación de aspecto | Calidad de imagen | Notas |
| --- | --- | --- | --- |
| deslizamiento hacia arriba | 1:1 | Alta resolución 150 x 150 px <br> Resolución mínima 50 x 50 px | Las imágenes de distintas relaciones de aspecto cabrán en un contenedor de imágenes cuadrado, sin recortar. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% tab Modal %}

| Tipo | Relación de aspecto | Calidad de imagen | Notas |
| --- | --- | --- | --- |
| Modal (sólo imagen) | 1:1 | Alta resolución 1200 x 2000 px <br> Resolución mínima 600 x 600 px | El mensaje cambiará de tamaño para adaptarse a imágenes de la mayoría de las relaciones de aspecto. |
| Modal con texto | 29:10 | Alta resolución 1450 x 500 px <br> Resolución mínima 600 x 205 px | Las imágenes altas se reducirán y se centrarán horizontalmente. Las imágenes anchas se recortarán por los bordes izquierdo y derecho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% endtab %}
{% endtabs %}

{% endif %}

{% if include.variable_name == "push notifications" %}

| Tipo de mensaje | Longitud máxima del mensaje | Longitud máxima del título |
| --- | --- | --- |
| Pantalla de bloqueo de iOS | 175 caracteres | 43 caracteres |
| Notificación iOS | 175 caracteres | 43 caracteres |
| Alerta de banner en iOS | 85 caracteres | 43 caracteres |
| Pantalla de bloqueo de Android | 49 caracteres | 43 caracteres |
| Cajón de notificaciones de Android | 597 caracteres | 43 caracteres |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

El tamaño recomendado para todas las imágenes push es de 500 KB.

<style>
table td {
    word-break: break-word;
}
</style>

<table>
  <thead>
    <tr>
      <th>Tipo de imagen</th>
      <th>Relación de aspecto</th>
      <th>Píxeles máximos</th>
      <th>Tamaño máximo de la imagen</th>
      <th>Tipos de archivo</th>
      <th>Notas</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>iOS</td>
      <td>2:1 (recomendado)</td>
      <td>1038 x 1038</td>
      <td>5 MB</td>
      <td>PNG, JPEG, GIF</td>
      <td>A partir de enero de 2020, las notificaciones push enriquecidas de iOS pueden manejar imágenes de 1038 x 1038 px siempre que no superen los 10 MB, pero recomendamos utilizar un tamaño de archivo lo más pequeño posible. En la práctica, enviar archivos de gran tamaño puede causar una tensión innecesaria en la red y hacer que los tiempos de espera de descarga sean más frecuentes.<br><br>Para más información, consulta <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/">Notificaciones enriquecidas de iOS</a>.</td>
    </tr>
    <tr>
      <td>Icono push de Android</td>
      <td>1:1</td>
      <td>N/A</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td></td>
    </tr>
    <tr>
      <td>Imagen de notificación ampliada de Android</td>
      <td>2:1</td>
      <td><b>Pequeña:</b><br>512 x 256<br><br><b>Medio:</b><br>1024 x 512<br><br><b>Grande:</b><br>2048 x 1024</td>
      <td>500 KB</td>
      <td>PNG, JPEG</td>
      <td>Se utiliza en las <a href="{{site.baseurl}}/user_guide/message_building_by_channel/push/android/rich_notifications/">notificaciones enriquecidas de Android</a>.</td>
    </tr>
    <tr>
      <td>Imagen inclinada Android</td>
      <td>3:2</td>
      <td>N/A</td>
      <td>N/A</td>
      <td>PNG, JPEG</td>
      <td>Para más detalles, consulta <a href="{{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/inline_image_push/">Push de imágenes en línea de Android</a>.</td>
    </tr>
  </tbody>
</table>
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4  .reset-td-br-5 .reset-td-br-6 role="presentation"}

{% endif %}

{% if include.variable_name == "email" %}

| Tipo de correo electrónico | Propiedades máximas recomendadas |
| --- | --- | 
| Sólo texto | 25 KB |
| Texto con imágenes | 60 KB |
| Anchura del correo electrónico | 600 px |
{: .reset-td-br-1 .reset-td-br-2}

| Especificaciones de imagen | Propiedades máximas recomendadas |
| --- | --- | 
| Tamaño | 5 MB |
| Ancho | Cabecera: 600 px<br>Cuerpo: 480 px |
| Tipos de archivo | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2}

| Especificaciones del texto | Propiedades máximas recomendadas |
| --- | --- | 
| Longitud de la línea del asunto | 35 caracteres<br>De 6 a 10 palabras |
| `"From: Name"` longitud | 25 caracteres |
| Longitud del preencabezado | 85 caracteres |
{: .reset-td-br-1 .reset-td-br-2}

{% endif %}

{% if include.variable_name == "content cards" %}

| Tipo de tarjeta | Relación de aspecto     | Calidad de imagen       |
| --------- | ---------------- | ------------------- |
| Clásica   | Relación de aspecto 1:1 | 60 x 60 px        |
| Subtitulado | Relación de aspecto 4:3 | 600 px de anchura mínima |
| Banner    | Cualquier relación de aspecto | 600 px de anchura mínima |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Para más información, consulta los [Detalles creativos de la tarjeta de contenido]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/creative_details/).

{% endif %}