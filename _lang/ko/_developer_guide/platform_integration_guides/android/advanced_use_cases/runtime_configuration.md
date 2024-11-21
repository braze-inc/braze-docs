---
nav_title: 런타임 구성
article_title: Android 및 FireOS용 런타임 구성
platform: 
  - Android
  - FireOS
page_order: 4
description: "이 참조 문서에서는 Android 또는 FireOS 애플리케이션의 런타임 구성을 설정하는 방법을 다룹니다."

---

# 런타임 구성

>[런타임 구성](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)은 `braze.xml` 대신 런타임에 앱을 구성하는 선택적 방법입니다. 이 참조 문서에서는 런타임 구성을 설정하는 방법에 대해 설명합니다.

런타임 구성과 `braze.xml` 구성을 모두 사용할 수 있습니다. 런타임에 구성된 값은 항상 `braze.xml`의 동일한 값보다 우선합니다. Braze SDK가 런타임 구성에서 모든 값을 찾을 수 있으면 `braze.xml`은 더 이상 필요하지 않으므로 제거할 수 있습니다. 

## 사용 예

구성은 [빌더 오브젝트](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)를 사용하며, 이후 빌드되어 [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)로 전달됩니다. 다음 예제에서는 사용 가능한 런타임 구성 옵션의 하위 집합을 사용합니다. 전체 옵션 목록은 [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)를 참조하세요.

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

또 다른 예는 [Hello Braze 샘플 앱에서](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java) 확인할 수 있습니다.

