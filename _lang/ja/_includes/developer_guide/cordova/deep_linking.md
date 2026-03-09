{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## プッシュディープリンクのイネーブルメント

デフォルトでは、Braze Cordova SDK は通知からのプッシュディープリンクを自動的に処理しない。プッシュディープリンクのイネーブルメントを行うには、プロジェクトの`config.xml``AndroidManifest.xml` ファイル内の `<ANDROIDMANIFEST`platform`>\` 要素に以下の設定を追加する。

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.ios_forward_universal_links" value="YES" />
</platform>
```
{% endtab %}

{% tab android %}
```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
</platform>
```

ディープリンクが追跡された際のバックスタック動作をカスタマイズするには、以下のオプション設定を追加することもできる：

```xml
<platform name="android">
    <preference name="com.braze.android_handle_push_deep_links_automatically" value="true" />
    <preference name="com.braze.is_push_deep_link_back_stack_activity_enabled" value="true" />
    <preference name="com.braze.push_deep_link_back_stack_activity_class_name" value="YOUR_ACTIVITY_CLASS_NAME" />
</platform>
```
{% endtab %}
{% endtabs %}

利用可能なプッシュ設定オプションの完全な一覧については、[「オプション設定」]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional)を参照せよ。
