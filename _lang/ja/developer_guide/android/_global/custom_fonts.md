{% multi_lang_include developer_guide/prerequisites/android.md %}

## カスタムフォントの使用

### ステップ 1: フォントファミリの作成

以下は、[フォントファミリガイド](https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html#font-family)を使用したカスタムフォントファミリ定義の例です。この例では、[Bungee Shade フォント](https://fonts.google.com/specimen/Bungee+Shade)を使用します。

```html
<?xml version="1.0" encoding="utf-8"?>
<font-family xmlns:android="http://schemas.android.com/apk/res/android"
             xmlns:app="http://schemas.android.com/apk/res-auto">

  <!--Note: You must declare both sets of attributes
      so that your fonts load on devices running Android 8.0 (API level 26) or lower.
      See https://developer.android.com/guide/topics/ui/look-and-feel/fonts-in-xml.html -->

  <font android:fontStyle="normal"
        android:fontWeight="400"
        android:font="@font/bungeeshade"

        app:fontStyle="normal"
        app:fontWeight="400"
        app:font="@font/bungeeshade"/>
</font-family>
```

フォントファミリの定義を`/res/font/bungee_font_family.xml`に保存したら、XML でそれを`@font/bungee_font_family`として参照できます。

### ステップ 2: フォントファミリを参照する

フォントファミリが作成されたので、`styles.xml`の Braze スタイルのデフォルトをオーバーライドして、フォントファミリへの参照を含めることができます。

例えば、次のスタイルのオーバーライドでは、すべての Braze アプリ内メッセージに`bungee`フォントファミリが使用されます。

```html
<style name="Braze.InAppMessage">
  <item name="android:fontFamily">@font/bungee_font_family</item>
  <item name="fontFamily">@font/bungee_font_family</item>
</style>

<style name="Braze.Cards">
  <item name="android:fontFamily">@font/another_custom_font_family</item>
  <item name="fontFamily">@font/another_custom_font_family</item>
</style>
```

{% alert warning %}
すべての SDK バージョン間で互換性を維持するには、`android:fontFamily`と`fontFamily`両方のスタイル属性を設定する必要があります。
{% endalert %}
