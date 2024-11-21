---
nav_title: Google Advertising ID (Opcional)
article_title: ID de publicidad de Google opcional para Android
page_order: 9
platform: 
  - Android
description: "Este artículo de referencia cubre los ID de publicidad de Google y cómo pasar esta información publicitaria a Braze para tu aplicación de Android o FireOS."

---

# ID de publicidad de Google (solo Android)

> El [ID de publicidad de Google](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) es un ID opcional específico del usuario, anónimo, único y reajustable para publicidad, proporcionado por los servicios de Google Play. Este artículo de referencia cubre los ID de publicidad de Google y cómo pasar esta información publicitaria a Braze para tu aplicación de Android o FireOS.

GAID ofrece a los usuarios la posibilidad de restablecer su identificador, excluirse voluntariamente de los anuncios basados en intereses dentro de las aplicaciones de Google Play, y proporciona a los desarrolladores un sistema sencillo y estándar para seguir monetizando sus aplicaciones.

## Pasar el ID de publicidad de Google a Braze

El SDK de Braze no recopila automáticamente el ID de publicidad de Google, por lo que debe establecerse manualmente mediante el método [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html).

{% alert important %}
Google requiere que el ID de publicidad se recoja en un hilo no-UI.
{% endalert %}

{% tabs %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Thread(Runnable {
  try {
    val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext())
    Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.id, idInfo.isLimitAdTrackingEnabled)
  } catch (e: Exception) {
    e.printStackTrace()
  }
}).start()
```

{% endtab %}
{% endtabs %}


