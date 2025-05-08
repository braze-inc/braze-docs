---
nav_title: カスタムスタイリング
article_title: Android と FireOS のアプリ内メッセージカスタムスタイリング
platform: 
  - Android
  - FireOS
page_order: 2
description: "このリファレンス記事では、Android または FireOS アプリケーションのアプリ内メッセージングのカスタムスタイリングについて説明します。"
channel:
  - in-app messages

---

# カスタムスタイリング

> Braze の UI 要素は、Android 標準の UI ガイドラインにマッチしたデフォルトのルックアンドフィールで提供され、シームレスな体験を提供します。このリファレンス記事では、Android または FireOS アプリケーションのアプリ内メッセージングのカスタムスタイリングについて説明します。

デフォルトのスタイルは、Braze SDK の[`styles.xml`](https://github.com/braze-inc/braze-android-sdk/blob/master/android-sdk-ui/src/main/res/values/styles.xml)ファイルで確認できます。

```xml
  <style name="Braze"/>
  <style name="Braze.InAppMessage"/>
  <style name="Braze.InAppMessage.Header">
    <item name="android:layout_height">wrap_content</item>
    <item name="android:layout_width">match_parent</item>
    <item name="android:padding">0.0dp</item>
    <item name="android:background">@android:color/transparent</item>
    <item name="android:textColor">@color/com_braze_inappmessage_header_text</item>
    <item name="android:textSize">20.0sp</item>
    <item name="android:lineSpacingMultiplier">1.3</item>
    <item name="android:gravity">center</item>
    <item name="android:textStyle">bold</item>
    <item name="android:layout_centerHorizontal">true</item>
  </style>
```

必要に応じて、これらのスタイルをオーバーライドし、アプリにより適したルックアンドフィールを作成することができます。

スタイルを上書きするには、スタイル全体をプロジェクトの`styles.xml`ファイルにコピーし、変更を加えます。すべての属性が正しく設定されるようにするには、スタイル全体をローカルの`styles.xml`にコピーする必要があります。これらのカスタムスタイルは、個々の UI 要素を変更するためのものであり、レイアウトを全面的に変更するものではないことに注意してください。レイアウトレベルの変更はカスタムビューで処理する必要があります。

{% alert note %}
XMLを修正することなく、Brazeキャンペーンでいくつかの色を直接カスタマイズできる。Brazeダッシュボードで設定した色は、他の場所で設定した色よりも優先されることを覚えておいてほしい。
{% endalert %}

## カスタムフォント

Braze では、[フォントファミリガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/font_customization/#font-customization)を使用してカスタムフォントを設定することができます。使用するには、メッセージテキスト、ヘッダー、ボタンテキストのスタイルをオーバーライドし、`fontFamily`属性を使用して、Braze にカスタムフォントファミリを使用するように指示します。

例えば、アプリ内メッセージボタンテキストのフォントを更新するには、`Braze.InAppMessage.Button`スタイルをオーバーライドし、カスタムフォントファミリを参照します。属性値は、`res/font`ディレクトリのフォントファミリを指す必要があります。

以下は、最後の行でカスタムフォントファミリ `my_custom_font_family` が参照されている部分的なコード例です。

```xml
  <style name="Braze.InAppMessage.Button">
    <item name="android:layout_height">wrap_content</item>
    ...
    <item name="android:paddingBottom">15.0dp</item>
    <item name="android:fontFamily">@font/my_custom_font_family</item>
    <item name="fontFamily">@font/my_custom_font_family</item>
  </style>
```

ボタンテキストの`Braze.InAppMessage.Button`スタイルは別として、メッセージテキストのスタイルは`Braze.InAppMessage.Message`、メッセージヘッダーのスタイルは`Braze.InAppMessage.Header`です。アプリ内メッセージの全テキストにカスタムフォントファミリを使用する場合は、`Braze.InAppMessage`スタイルにフォントファミリを設定することができます。このスタイルは、すべてのアプリ内メッセージの親スタイルとなります。

{% alert important %}
他のカスタムスタイルと同様に、すべての属性が正しく設定されるようにするには、スタイル全体をローカルの`styles.xml`にコピーする必要があります。
{% endalert %}

## 方向を固定する

アプリ内メッセージに固定方向を設定するには、最初に[カスタムのアプリ内メッセージマネージャーリスナーを設定]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/)します。次に、`beforeInAppMessageDisplayed()`デリゲートメソッドで`IInAppMessage`オブジェクトに対して`setOrientation()`を呼び出します。

{% tabs %}
{% tab JAVA %}
```java
public InAppMessageOperation beforeInAppMessageDisplayed(IInAppMessage inAppMessage) {
  // Set the orientation to portrait
  inAppMessage.setOrientation(Orientation.PORTRAIT);
  return InAppMessageOperation.DISPLAY_NOW;
}
```
{% endtab %}
{% tab KOTLIN %}
```kotlin
override fun beforeInAppMessageDisplayed(inAppMessage: IInAppMessage): InAppMessageOperation {
  // Set the orientation to portrait
  inAppMessage.orientation = Orientation.PORTRAIT
  return InAppMessageOperation.DISPLAY_NOW
}
```
{% endtab %}
{% endtabs %}

タブレット端末の場合、アプリ内メッセージは、実際の画面の向きに関係なく、ユーザーが希望する向きのスタイルで表示されます。

