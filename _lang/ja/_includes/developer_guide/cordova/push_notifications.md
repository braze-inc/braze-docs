{% multi_lang_include developer_guide/prerequisites/cordova.md %} SDKを統合すると、基本的なプッシュ通知機能はデフォルトでイネーブルメントされる。[リッチプッシュ]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova)通知と[プッシュストーリー]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova)を使用するには、それぞれ個別に設定する必要がある。iOSのプッシュ通知を利用するには、有効なプッシュ証明書もアップロードする必要がある。

{% alert warning %}
Cordovaのプラグインを追加、削除、更新するたびに、Cordovaは iOS アプリの Xcode プロジェクト内の Podfile を上書きする。これは、Cordovaのプラグインを変更するたびに、これらの機能を再度設定する必要があることを意味する。
{% endalert %}

## プッシュディープリンクのイネーブルメント

デフォルトでは、Braze Cordova SDK はプッシュ通知からのディープリンクを自動的に処理しない。プッシュディープリンクのイネーブルメントを行うには、[ディープリンク]({{site.baseurl}}/developer_guide/cordova/deep_linking/)の設定ステップに従うこと。
これらの設定やその他のプッシュ設定オプションの詳細については、[「オプションの設定」]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional)を参照のこと。

## 基本プッシュ通知を無効にする（iOSのみ）

iOS 用の Braze Cordova SDK を統合すると、基本的なプッシュ通知機能がデフォルトでイネーブルメントされる。iOSアプリでこの機能を無効にするには、設定`config.xml`ファイルに以下を追加する。詳細については、[オプション設定を]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional)参照せよ。

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
