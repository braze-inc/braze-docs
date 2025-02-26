---
nav_title: HTML 푸시 알림
article_title: Android용 HTML 푸시 알림
platform: Android
page_order: 6
description: "이 참조 문서에서는 Android 애플리케이션에서 HTML 푸시 알림을 구현하는 방법을 다룹니다."
channel:
  - push

---

# HTML 푸시 알림

> 이 참조 문서에서는 Android 애플리케이션에서 HTML 푸시 알림을 구현하는 방법을 다룹니다.

Braze SDK 버전 3.1.1에서 HTML을 기기로 보내 푸시 알림에서 승수 텍스트를 렌더링할 수 있습니다.

![글자가 서로 다른 색상으로 이탤릭체로 표시되고 배경색이 지정된 Android 푸시 메시지 '멀티컬러 푸시 테스트 메시지'입니다.]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

이 예제는 다음 HTML로 렌더링됩니다:

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>
```

```html
<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Android OS는 푸시 알림에서 유효한 HTML 요소/태그를 제한합니다. 예를 들어, `marquee`는 허용되지 않습니다.

{% alert important %}
다중 색상 텍스트 렌더링은 기기마다 다르며 Android 기기 또는 버전에 따라 표시되지 않을 수도 있습니다.
{% endalert %}

## 구현

푸시 알림에서 여러 색상의 텍스트를 렌더링하려면 다음 중 하나를 수행합니다.

다음 항목을 `braze.xml`에 추가하십시오:

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```

**OR** 

에 다음을 추가합니다. [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

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

