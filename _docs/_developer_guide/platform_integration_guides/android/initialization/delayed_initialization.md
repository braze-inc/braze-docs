---
nav_title: Delayed Initialization
article_title: Delayed Initialization for Android and FireOS
platform: 
  - Android
  - FireOS
page_order: 0
description: "This article covers how to implement delayed initialization on the Android SDK and optionally preserve push notification analytics when delayed initialization is enabled."

---

# Delayed initialization for the Braze Android SDK

> Learn how to enable delayed initialization and opt in to preserve push notification analytics when it is enabled. This can be useful when you need to set up other services before initializing the SDK, such as fetching configuration data from a server or waiting for user consent.

{% alert note %}
While delayed initialization is enabled, all network connections will be canceled, and the Braze SDK will not pass any data to Braze servers.
{% endalert %}

## Prerequisites

To use this feature, you'll need to Braze Android SDK version XXXX or later.

## Enabling Delayed Initialization

Delayed initialization is disabled by default. To enable, use one of the following options:

{% tabs %}
{% tab Braze XML file %}
In your project's `braze.xml` file, set `com_braze_enable_delayed_initialization` to `true`.

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab At runtime %}
To enable delayed initialization at runtime, use the following method.

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Configuring push analytics

When delayed initialization is enabled, push analytics are queued by default. However, you can choose to explicitly queue or drop push analytics instead.

### Explicitly queue

To explicitly queue push analytics, choose one of the following options:

{% tabs %}
{% tab Braze XML file %}
In your `braze.xml` file, set `com_braze_delayed_initialization_analytics_behavior` to `QUEUE`:

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
Add `QUEUE` to your [`Braze.enableDelayedInitialization()`](LINK) method:

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### Drop

To drop push analytics, choose one of the following options:

{% tabs %}
{% tab Braze XML file %}
In your `braze.xml` file, set `com_braze_delayed_initialization_analytics_behavior` to `DROP`: 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
Add `DROP` to [`Braze.enableDelayedInitialization()`](LINK) method:

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Initializing After Delay

To initialize the SDK after your chosen delay period, use the [`Braze.disableDelayedInitialization()`](LINK) method:

{% tabs local %}
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
