{% multi_lang_include developer_guide/prerequisites/android.md %} También tendrás que [configurar las notificaciones push]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android).

## Diseño de notificación personalizado

Las notificaciones Braze se envían como [mensajes de datos](https://firebase.google.com/docs/cloud-messaging/concept-options), lo que significa que tu aplicación siempre tendrá la oportunidad de responder y realizar un comportamiento acorde, incluso en segundo plano (a diferencia de los mensajes de notificación, que pueden ser gestionados automáticamente por el sistema cuando tu aplicación está en segundo plano). Como tal, tu aplicación tendrá la oportunidad de personalizar la experiencia, por ejemplo, mostrando elementos de interfaz de usuario personalizados dentro de la notificación entregada en la bandeja de notificaciones. Aunque implementar el push de esta forma puede resultar desconocido para algunos, una de nuestras características más conocidas en Braze, [las historias push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), ¡son un excelente ejemplo del uso de componentes de vista personalizados para crear una experiencia atractiva!

{% alert important %}
Android impone algunas limitaciones a los componentes que pueden utilizarse para implementar vistas de notificación personalizadas. Los diseños de las vistas de notificación _sólo_ deben contener objetos Vista compatibles con el marco [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews).
{% endalert %}

## Notificaciones push personalizadas

Las notificaciones push pueden mostrar información específica del usuario dentro de una jerarquía de vistas personalizada. En el siguiente ejemplo, se utiliza un desencadenador API para enviar una notificación push personalizada a un usuario para que pueda comprobar su progreso actual tras completar una tarea específica en la aplicación.

![Ejemplo de panel push personalizado]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

Para configurar un push personalizado en el panel, registra la categoría específica que quieres que se muestre y, a continuación, establece los atributos de usuario relevantes que te gustaría mostrar utilizando Liquid.

![Ejemplo de panel push personalizado]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}
