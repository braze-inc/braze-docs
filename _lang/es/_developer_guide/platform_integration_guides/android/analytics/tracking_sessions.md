---
nav_title: Seguimiento de sesiones
article_title: Sesiones de seguimiento para Android y FireOS
platform: 
  - Android
  - FireOS
page_order: 0
description: "Este artículo de referencia muestra cómo suscribirte a las actualizaciones de sesión para tu aplicación Android o FireOS."

---

# Seguimiento de sesiones

> El SDK de Braze informa de los datos de sesión utilizados por el panel de Braze para calcular la participación de los usuarios y otros análisis esenciales para comprender a tus usuarios. Nuestro SDK genera puntos de datos de "inicio de sesión" y "cierre de sesión" que tienen en cuenta la duración de la sesión y los recuentos de sesiones visibles dentro del panel Braze, basándose en la siguiente semántica de sesión. Este artículo de referencia muestra cómo suscribirte a las actualizaciones de sesión para tu aplicación Android o FireOS.

## Ciclo de vida de la sesión

Si has integrado Braze utilizando nuestra [integración de devolución de llamada del ciclo de vida de la actividad recomendada]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-4-tracking-user-sessions-in-android), `openSession()` y `closeSession()` se llamarán automáticamente para cada actividad de tu aplicación. Por predeterminado, las sesiones en Android se abren con la primera llamada a `openSession()` y se cierran después de que una aplicación haya estado fuera del primer plano durante más de 10 segundos. Nota que llamar a `closeSession()` no cierra la sesión inmediatamente. Más bien, cierra una sesión en 10 segundos si el usuario no llama a `openSession()` (por ejemplo, navegando a otra actividad) en ese plazo.

Una sesión de Android se agota tras 10 segundos sin ninguna comunicación de la aplicación anfitriona. Esto significa que si un usuario sale de la aplicación y vuelve 9 segundos después, continuará la misma sesión. Ten en cuenta que si se cierra una sesión mientras el usuario tiene la aplicación en segundo plano, es posible que esos datos no se vuelquen al servidor hasta que se vuelva a abrir la aplicación.

{% alert note %}
Si necesitas forzar una nueva sesión, puedes hacerlo cambiando de usuario.
{% endalert %}

## Personalizar el tiempo de espera de la sesión
Para personalizar el tiempo de espera de la sesión, añade `com_braze_session_timeout` a tu archivo [`braze.xml`]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/#step-2-configure-the-braze-sdk-in-brazexml). El valor mínimo de `NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT` es 1 segundo.

```xml
<!-- The length of time before a session times out in seconds. The session manager will "re-open" otherwise closed sessions if the call to StartSession comes within this interval. (default is 10) -->
<integer name="com_braze_session_timeout">NUMBER_OF_SECONDS_UNTIL_SESSION_TIMEOUT</integer>
```

## Probar el seguimiento de la sesión

Para detectar sesiones a través de tu usuario, busca a tu usuario en el panel y navega hasta **Uso de la aplicación** en el perfil de usuario. Puedes confirmar que el seguimiento de la sesión funciona comprobando que la métrica de la sesión aumenta cuando esperas que lo haga.

![Un componente de perfil de usuario que muestra cuántas sesiones se han producido, cuándo se utilizó la aplicación por primera vez y cuándo se utilizó por última vez.]({% image_buster /assets/img_archive/test_session.png %})

## Suscribirse a las actualizaciones de la sesión

El SDK de Braze proporciona un [`subscribeToSessionUpdates`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/subscribe-to-session-updates.html) suscriptor para escuchar las actualizaciones de sesión:

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(this).subscribeToSessionUpdates(new IEventSubscriber<SessionStateChangedEvent>() {
  @Override
  public void trigger(SessionStateChangedEvent message) {
    if (message.getEventType() == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
      // A session has just been started
    }
  }
});
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(this).subscribeToSessionUpdates { message ->
  if (message.eventType == SessionStateChangedEvent.ChangeType.SESSION_STARTED) {
    // A session has just been started
  }
}
```

{% endtab %}
{% endtabs %}

