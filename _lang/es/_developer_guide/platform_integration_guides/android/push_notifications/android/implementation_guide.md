---
nav_title: Guía de Implementación Avanzada (Opcional)
article_title: Implementación avanzada de notificaciones push para Android (Opcional)
platform: Android
page_order: 29
description: "Esta guía de implementación avanzada explica cómo personalizar el diseño de las notificaciones push para mostrar información específica del usuario en tus mensajes. También se incluye un ejemplo de caso de uso construido por nuestro equipo, fragmentos de código que lo acompañan y orientación sobre el análisis de registros."
channel:
  - push
---

<br>
{% alert important %}
¿Buscas la guía básica de integración para desarrolladores de notificaciones push? Encuéntralo [aquí]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/).
{% endalert %}

# Guía de implementación avanzada

> Esta guía de implementación opcional y avanzada cubre formas de aprovechar una subclase personalizada de FirebaseMessagingService para sacar el máximo partido a tus mensajes push. Se incluye un caso de uso personalizado creado por nuestro equipo, fragmentos de código que lo acompañan y orientaciones sobre el registro de análisis. ¡Visita nuestro repositorio de demostraciones Braze [aquí](https://github.com/braze-inc/braze-growth-shares-android-demo-app)! Ten en cuenta que esta guía de implementación se centra en una implementación de Kotlin, pero se proporcionan fragmentos de código Java para los interesados.

## Diseño de notificación personalizado

Las notificaciones Braze se envían como [mensajes de datos](https://firebase.google.com/docs/cloud-messaging/concept-options), lo que significa que tu aplicación siempre tendrá la oportunidad de responder y realizar un comportamiento acorde, incluso en segundo plano (esto contrasta con los mensajes de notificación, que pueden ser gestionados automáticamente por el sistema cuando tu aplicación está en segundo plano). Como tal, tu aplicación tendrá la oportunidad de personalizar la experiencia, por ejemplo, mostrando elementos de interfaz de usuario personalizados dentro de la notificación entregada en la bandeja de notificaciones. Aunque implementar el push de esta forma puede resultar desconocido para algunos, una de nuestras características más conocidas en Braze, [las historias push]({{site.baseurl}}/user_guide/message_building_by_channel/push/advanced_push_options/push_stories/), ¡son un excelente ejemplo del uso de componentes de vista personalizados para crear una experiencia atractiva!

#### Requisitos

Android impone algunas limitaciones a los componentes que pueden utilizarse para implementar vistas de notificación personalizadas. Los diseños de las vistas de notificación _sólo_ deben contener objetos Vista compatibles con el marco [RemoteViews](https://developer.android.com/reference/android/widget/RemoteViews).

### Notificaciones push personalizadas

Las notificaciones push pueden mostrar información específica del usuario dentro de una jerarquía de vistas personalizada. El siguiente ejemplo muestra una notificación push después de que un usuario haya completado una tarea específica (curso de Braze Learning) y ahora se le anima a ampliar esta notificación para comprobar su progreso. La información que se proporciona aquí es específica del usuario y puede dispararse cuando se completa una sesión o se realiza una acción específica del usuario aprovechando un desencadenante de la API. 

![Ejemplo de panel push personalizado]({% image_buster /assets/img/push_implementation_guide/android_push_custom_layout.png %}){: style="max-width:65%;border:0"}

#### Configuración del panel de control

Para configurar un push personalizado en el panel, debes registrar la categoría específica que quieres que se muestre. Establece los atributos de usuario adecuados que quieres que muestre el mensaje dentro de los pares clave-valor utilizando Liquid estándar. Estas vistas pueden personalizarse en función de atributos específicos de usuario de un perfil de usuario concreto.

![Ejemplo de panel push personalizado]({% image_buster /assets/img/push_implementation_guide/push5.png %}){: style="max-width:60%;"}

##### ¿Listo para el análisis de registros?
Visita la [sección siguiente](#logging-analytics) para comprender mejor cómo debe ser el flujo de datos.

## Análisis de registros

### Registro con la API de Braze (recomendado)

El análisis de los registros solo puede hacerse en tiempo real con la ayuda del servidor del cliente que accede a nuestro [punto final`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Para registrar los análisis, envía el valor `braze_id` en el campo de los pares clave-valor (como se ve en la siguiente captura de pantalla) para identificar qué perfil de usuario hay que actualizar.

![Ejemplo de panel push personalizado]({% image_buster /assets/img/push_implementation_guide/android_braze_id_configuration.png %}){: style="max-width:80%;"}

### Registrar manualmente 

El registro manual se puede conseguir registrando los elementos que desees desde tu implementación de `FirebaseMessagingService.onMessageReceived` o desde tu actividad de inicio, en función de los extras presentes en la carga útil. Sin embargo, una advertencia importante que debes recordar es que tu subclase `FirebaseMessagingService` _debe_ finalizar la ejecución en los 10 segundos siguientes a la invocación para evitar que el sistema Android [la marque o la finalice](https://firebase.google.com/docs/cloud-messaging/android/receive). 


