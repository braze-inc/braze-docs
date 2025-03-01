---
nav_title: Laufzeit-Konfiguration
article_title: Laufzeitkonfiguration für Android und FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "Dieser referenzierte Artikel beschreibt, wie Sie die Laufzeitkonfiguration für Ihre Android- oder FireOS-Anwendung einrichten."

---

# Laufzeitkonfiguration

>Die [Laufzeitkonfiguration](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) ist eine optionale Möglichkeit, Ihre App zur Laufzeit zu konfigurieren, anstatt die `braze.xml`. Dieser Referenzartikel beschreibt, wie Sie die Laufzeitkonfiguration einrichten.

Die Verwendung sowohl der Laufzeitkonfiguration als auch der `braze.xml` Konfiguration ist weiterhin möglich. Die zur Laufzeit konfigurierten Werte haben immer Vorrang vor dem gleichen Wert in `braze.xml`. Wenn das Braze SDK alle Werte in der Laufzeitkonfiguration finden kann, wird die `braze.xml` nicht mehr benötigt und kann entfernt werden. 

## Verwendungsbeispiel

Die Konfiguration verwendet ein [Builder-Objekt](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html), das dann erstellt und an [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html) weitergeleitet wird. Das folgende Beispiel verwendet eine Teilmenge der verfügbaren Laufzeitkonfigurationsoptionen. Eine vollständige Liste der Optionen finden Sie in unserer [KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html).

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

Ein weiteres Beispiel finden Sie in unserer [Hello Braze Beispiel App](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java).

