---
nav_title: HTML Push-Benachrichtigungen
article_title: HTML Push-Benachrichtigungen für Android
platform: Android
page_order: 6
description: "Dieser Referenzartikel beschreibt, wie Sie HTML Push-Benachrichtigungen in Ihrer Android-Anwendung implementieren."
channel:
  - push

---

# HTML Push-Benachrichtigungen

> Dieser Referenzartikel beschreibt, wie Sie HTML Push-Benachrichtigungen in Ihrer Android-Anwendung implementieren.

In Braze SDK Version 3.1.1 kann HTML an ein Gerät gesendet werden, um Multiplikatortext in Push-Benachrichtigungen zu rendern.

![Die Android-Push-Nachricht "Multicolor Push Test Nachricht", bei der die Buchstaben verschiedene Farben haben, kursiv geschrieben sind und eine Hintergrundfarbe haben.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

Dieses Beispiel wird mit dem folgenden HTML-Code wiedergegeben:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>
```

```html
<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Android schränkt ein, welche HTML-Elemente und -Tags in Push-Benachrichtigungen zulässig sind. Zum Beispiel ist `marquee` nicht zulässig.

{% alert important %}
Beachten Sie, dass die Wiedergabe von mehrfarbigem Text gerätespezifisch ist und je nach Android-Gerät oder -Version möglicherweise nicht angezeigt wird.
{% endalert %}

## Implementierung

Um mehrfarbigen Text in Push-Benachrichtigungen darzustellen, können Sie entweder:

Fügen Sie Folgendes in Ihrem `braze.xml` hinzu:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```

**ODER** 

Fügen Sie Folgendes in Ihrem [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setPushHtmlRenderingEnabled(true)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setPushHtmlRenderingEnabled(true)
    .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

