---
nav_title: Google Advertising ID (Optional)
article_title: Optional Google Advertising ID for Android
page_order: 9
platform: 
  - Android
description: "This article covers Google advertising IDs and how to pass this advertising information to Braze."

---

# Optional Google Advertising ID (Android only)

The [Google Advertising ID][2] is a user-specific, anonymous, unique, and resettable ID for advertising, provided by Google Play services. GAID gives users the power to reset their identifier, opt-out of interest-based ads within Google Play apps, and provides developers with a simple, standard system to continue to monetize their apps.

## Passing the Google Advertising ID to Braze

The Google Advertising ID is not automatically collected by the Braze SDK and must be set manually via the [`Appboy.setGoogleAdvertisingId()`][1] method.

{% alert important %}
Google requires the Advertising ID to be collected on a non-UI thread.
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


[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/set-google-advertising-id.html
[2]: https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en
