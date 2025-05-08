---
nav_title: Google 광고 ID(선택 사항)
article_title: Android용 Google 광고 ID(선택 사항)
page_order: 9
platform: 
  - Android
description: "이 참조 문서에서는 Google 광고 ID와 Android 또는 FireOS 애플리케이션에서 Braze로 이 광고 정보를 전달하는 방법을 다룹니다."

---

# Google 광고 ID(Android 전용)

> [Google 광고 ID](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en)는 Google Play 서비스에서 제공하는 광고에 대한 사용자별 익명의 고유 ID(선택적 기능)로, 재설정이 가능합니다. 이 참조 문서에서는 Google 광고 ID와 Android 또는 FireOS 애플리케이션에서 Braze로 이 광고 정보를 전달하는 방법을 다룹니다.

GAID를 통해 사용자는 자신의 식별자를 재설정하고 Google Play 앱 내에서 관심 기반 광고를 옵트아웃할 수 있으며, 개발자는 간단한 표준 시스템으로 앱에서 지속적으로 수익을 창출할 수 있습니다.

## Braze에 Google 광고 ID 전달하기

Google 광고 ID는 Braze SDK에서 자동으로 수집되지 않으며, [`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) 메서드를 통해 수동으로 설정해야 합니다.

{% alert important %}
Google은 비 UI 스레드에서 광고 ID를 수집하도록 요구합니다.
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


