---
nav_title: Runtime Configuration
article_title: Runtime Configuration for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 4
description: "This reference article covers how to set up runtime configuration for your Android or FireOS application."

---

# Runtime configuration

[Runtime configuration][1] is an optional way to configure your app at runtime in place of a `braze.xml`. The use of both runtime configuration and `braze.xml` configuration is still possible. Runtime configured values will always take precedence over the same value in the `braze.xml`. If the Braze SDK can find all values in the runtime configuration, then the `braze.xml` is no longer needed and can be removed.

## Example usage

The configuration uses a [builder object][2] that is then built and passed to [`Braze.configure()`][1]. The following example uses a subset of the runtime configuration options available, see our [KDoc][1] for a complete list of options.

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

Another example can be found in our [Hello Braze sample app][3].

[1]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.appboy/-appboy/configure.html
[2]: https://appboy.github.io/appboy-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html
[3]: https://github.com/Appboy/appboy-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java
