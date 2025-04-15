---
nav_title: HTML プッシュ通知
article_title: Android 向け HTML プッシュ通知
platform: Android
page_order: 6
description: "このリファレンス記事では、Android アプリケーションで HTML プッシュ通知を実装する方法について説明します。"
channel:
  - push

---

# HTML プッシュ通知

> このリファレンス記事では、Android アプリケーションで HTML プッシュ通知を実装する方法について説明します。

Braze SDK バージョン3.1.1 では、HTML をデバイスに送信し、プッシュ通知でマルチプライヤーテキストをレンダリングできます。

![Android のプッシュメッセージ「マルチカラー・プッシュ・テスト・メッセージ」。文字の色が異なり、イタリック体で、バックグラウンドカラーが与えられている。]({% image_buster /assets/img/multicolor_android_push.png %}){: style="max-width:40%;"}

この例は、以下の HTML でレンダリングされます。

```html
<p><span style="color: #99cc00;">M</span>u<span style="color: #008080;">lti</span>Colo<span style="color: #ff6600;">r</span> <span style="color: #000080;">P</span><span style="color: #00ccff;">u</span><span style="color: #ff0000;">s</span><span style="color: #808080;">h</span></p>
```

```html
<p><em>test</em> <span style="text-decoration: underline; background-color: #ff6600;"><strong>message</strong></span></p>
```

Android OS では、プッシュ通知で有効な HTML 要素 / タグが制限されています。たとえば、`marquee` は使用できません。

{% alert important %}
マルチカラーテキストのレンダリングはデバイス固有であり、Android デバイスまたはバージョンによってはて表示されない場合があることに注意してください。
{% endalert %}

## 実装

プッシュ通知でマルチカラーテキストをレンダリングするには、次のいずれかを行います。

`braze.xml` に以下を追加します。

```xml
<bool translatable="false" name="com_braze_push_notification_html_rendering_enabled">true</bool>
```

**または** 

[`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration) に以下を追加します。

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

