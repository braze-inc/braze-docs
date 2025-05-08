---
nav_title: Google Advertising ID (Optional)
article_title: Optionale Google Advertising ID für Android
page_order: 9
platform: 
  - Android
description: "Dieser referenzierte Artikel behandelt die Google IDs für Werbung und wie Sie diese Werbeinformationen an Braze für Ihre Android- oder FireOS-Anwendung weitergeben."

---

# Google Advertising ID (nur Android)

> Die [Google Advertising ID](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en) ist eine optionale benutzerspezifische, anonyme, eindeutige und zurücksetzbare ID für Werbung, die von Google Play Diensten bereitgestellt wird. Dieser referenzierte Artikel behandelt die Google IDs für Werbung und wie Sie diese Werbeinformationen an Braze für Ihre Android- oder FireOS-Anwendung weitergeben.

GAID gibt Nutzern:innen die Möglichkeit, ihren Bezeichner zurückzusetzen, interessenbezogene Werbung in Google Play Apps abzulehnen und bietet Entwicklern:innen ein einfaches, standardisiertes System, um ihre Apps weiterhin zu monetarisieren.

## Übergabe der Google Advertising ID an Braze

Die Google Advertising ID wird nicht automatisch vom Braze SDK erfasst und muss manuell über die Methode [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) festgelegt werden.

{% alert important %}
Google verlangt, dass die Advertising ID auf einem Nicht-UI-Thread erfasst wird.
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


