---
nav_title: Delayed Initialization
article_title: Delayed Initialization for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 10
description: "This article covers how to implement delayed initialization on the Android SDK and optionally preserve push notification analytics when delayed initialization is enabled."

---

# Delayed initialization for the Braze Android SDK

> Learn how to enable delayed initialization and opt in to preserve push notification analytics when it is enabled. This can be useful when you need to set up other services before initializing the SDK, such as fetching configuration data from a server, or waiting for user consent.

While delayed initialization is enabled, all network connections to be canceled, and the Braze SDK will not pass any data to Braze servers.

{% alert important %}
Delayed initialization is available starting in Android SDK version xxxx.
{% endalert %}

## Enabling Delayed Initialization

Delayed initialization is disabled by default. In order to delay initialization, update your `braze.xml` file to include `com_braze_enable_delayed_initialization` and confirm its value is set to `true`:

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```

This can additionally be done at runtime via:

{% tabs %}
{% tab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

## Initializing After Delay

To initialize the SDK once the delay period is over, use the [`Braze.disableDelayedInitialization()`](set link after release) method:

{% tabs %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

## Setting Delayed Initialization Push Analytics Behavior

When delayed initialization is enabled, you have to option to queue or drop push analytics. If push analytics are queued, these events will be logged once delayed initialization is disabled. 

By default, push analytics are queued when delayed initialization is enabled. In order to drop push analytics, update your `braze.xml` file to include `com_braze_delayed_initialization_analytics_behavior` as follows: 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```

To explicitly queue push analytics, update your `braze.xml` file to include `com_braze_delayed_initialization_analytics_behavior` as follows:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```

Additionaly, the push analytics behavior can be set during runtime in the [`Braze.enableDelayedInitialization()`](set link after release) method by using one of the following code snippets:

{% tabs %}
{% tab JAVA %}

```java
// Drop all push analytics
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);

// Queue push analytics
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
// Drop all push analytics
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)

// Queue push analytics
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endtab %}
{% endtabs %}