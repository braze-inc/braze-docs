{% multi_lang_include developer_guide/prerequisites/cordova.md %} SDKを統合すると、基本的なプッシュ通知機能がデフォルトで有効になる。[リッチプッシュ通知と]({{site.baseurl}}/developer_guide/push_notifications/rich/?sdktab=cordova) [プッシュストーリーを]({{site.baseurl}}/developer_guide/push_notifications/push_stories/?sdktab=cordova)使うには、個別に設定する必要がある。

{% alert warning %}
Cordovaプラグインを追加、削除、更新するたびに、CordovaはiOSアプリのXcodeプロジェクトのPodfileを上書きする。つまり、Cordovaプラグインを変更するたびに、これらの機能を再度設定する必要があるということだ。
{% endalert %}

## 基本的なプッシュ通知を無効にする（iOSのみ）

Braze Cordova SDK for iOSを統合すると、基本的なプッシュ通知機能がデフォルトでイネーブルになる。iOSアプリでこの機能を無効にするには、`config.xml` 。詳細については、[オプション構成を]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=cordova#optional)参照のこと。

```xml
<platform name="ios">
    <preference name="com.braze.ios_disable_automatic_push_registration" value="NO" />
    <preference name="com.braze.ios_disable_automatic_push_handling" value="NO" />
</platform>
```
