---
nav_title: 統合
article_title: FireOS のプッシュ統合
platform: FireOS
page_order: 0
page_type: solution
description: "このリファレンス記事では、FireOS アプリケーションで Braze プッシュ通知を統合する方法について説明します。"
channel: push
search_rank: 0.9
---

# FireOS プッシュ統合

> このリファレンス記事では、FireOS アプリケーションで Braze プッシュ通知を統合する方法について説明します。

プッシュ通知は、重要なアップデートが発生したときにユーザーの画面に表示されるアプリ外のアラートです。プッシュ通知は、時間的制約があって関連性の高いコンテンツをユーザーに提供したり、ユーザーをアプリに再エンゲージしたりするための効果的な方法です。

ADM (Amazon Device Messaging) は、Amazon 以外のデバイスではサポートされていません。Kindle プッシュをテストするには、[FireOS デバイス](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm)が必要です。その他のベストプラクティスについては、[ヘルプの生地]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/)を参照してください。

Braze は、[Amazon Device Messaging (ADM)](https://developer.amazon.com/public/apis/engage/device-messaging) を使用して Amazon デバイスにプッシュ通知を送信します。

## ステップ 1:ADM を有効にする

1. まだ作成していない場合は、[Amazon Apps & Games Developer Portal](https://developer.amazon.com/public) を使用してアカウントを作成します。
2. [OAuth 認証情報 (クライアント ID とクライアントシークレット) と ADM API キー](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)を取得します。
3. [Unity Braze 設定]ウィンドウで [**自動 ADM 登録が有効**] を有効にします。 
  - または、`res/values/braze.xml` ファイルに次の行を追加して、ADM 登録を有効にすることもできます。

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## ステップ2:AndroidManifest.xml を更新する

アプリのAndroidManifest.xml 、Amazonの名前空間を`<>manifest</>` タグに追加する：

```xml
  xmlns:amazon="http://schemas.amazon.com/apk/res/android"
```

次に、`<>permission</>` および`<>uses-permission</>` 要素を `<>manifest</> element` の後に追加して、ADM をサポートするために必要な権限を宣言します。

  ```xml
  <manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:amazon="http://schemas.amazon.com/apk/res/android"
    package="[YOUR PACKAGE NAME]"
    android:versionCode="1"
    android:versionName="1.0">

  <!-- This permission verifies that no other application can intercept your ADM messages. -->
  <permission
    android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="[YOUR PACKAGE NAME].permission.RECEIVE_ADM_MESSAGE" />

   <!-- This permission allows your app access to receive push notifications from ADM. -->
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <!-- ADM uses WAKE_LOCK to keep the processor from sleeping when a message is received. -->
  <uses-permission android:name="android.permission.WAKE_LOCK" />
    ...
  </manifest>
```

次に、`amazon:enable-feature` 要素をマニフェストのアプリケーション要素に追加することで、アプリがデバイスの ADM 機能を使用すること、およびデバイスに ADM が存在しない状態でアプリが機能を維持するように設計されていること (`android:required="false"`) を宣言します。`android:required` を`"false"` として設定しても安全です。これは、ADM がデバイスに存在しない場合、Braze ADM コードはグレースフルデグラデーションを行うためです。

  ```xml
  ...
  <application
    android:icon="@drawable/ic_launcher"
    android:label="@string/app_name"
    android:theme="@style/AppTheme">

    <amazon:enable-feature android:name="com.amazon.device.messaging" android:required="false"/>
  ...
  ```

最後に、Braze `AndroidManifest.xml` ファイル内の ADM から `REGISTRATION` および `RECEIVE` インテントを処理するインテントフィルターを追加します。`amazon:enable-feature` の直後に、以下の要素を追加します。

```xml
    <receiver
      android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver"
      android:exported="true"
      android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
        <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
        <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />

        <category android:name="${applicationId}" />
      </intent-filter>
    </receiver>
```

## ステップ 3:ADM API キーを保存する

まず、ADM API キーを `api_key.txt` という名前のファイルに保存し、ファイルをプロジェクトの [`Assets/Plugins/Android/assets`][54] フォルダーに保存します。次に、[アプリの ADM API キーを取得します](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)。

Amazon は、末尾の改行などの空白文字が `api_key.txt` に含まれている場合、キーを認識しません。

## ステップ 4:ディープリンクを追加する

#### ディープリンクの自動オープンを有効にする

プッシュ通知がクリックされたときに Braze がアプリとディープリンクを自動的に開くようにするには、`braze.xml` で `com_braze_handle_push_deep_links_automatically` を `true` に設定します。

```
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

ディープリンクをカスタムで処理する場合は、Braze からのプッシュ受信およびオープンインテントをリッスンするプッシュコールバックを作成する必要があります。詳細については、Android のプッシュに関するドキュメントの [[カスタム処理のプッシュ受信およびオープン]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback)] を参照してください。

## ステップ5: Braze ダッシュボードにクライアントシークレットとクライアントID を追加する

最後に、[ステップ 1](#step-1-enable-adm) で取得したクライアントシークレットとクライアント ID を Braze ダッシュボードの [**設定の管理**] ページに追加する必要があります。

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

## 手動プッシュ登録

Brazeは手動登録の使用を推奨していないが、ADM登録を自分で処理する必要がある場合は、以下のように [braze.xml](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/03-setting-up-adm):

```xml
<!-- This will disable automatic registration for ADM via the Braze SDK-->
<bool name="com_braze_push_adm_messaging_registration_enabled">false</bool>
```
次に [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html)を使って、ユーザーのADM`registration_id` をBrazeに渡す：

{% tabs local %}
{% tab Java %}

```java
Braze.getInstance(context).setRegisteredPushToken(registration_id);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).registeredPushToken = registration_id
```

{% endtab %}
{% endtabs %}

## ADM の extra

ユーザーは、[ディープリンク]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/deep_linking/)、URL トラッキングなどのための `extras` として、Kindle プッシュメッセージでカスタムのキーと値のペアを送信できます。Android プッシュとは異なり、Kindle プッシュのユーザーは、`extra` キーと値のペアを定義するときに、Braze の予約キーをキーとして使用しないことがあります。

予約キーには以下が含まれます。

- `_ab`
- `a`
- `cid`
- `p`
- `s`
- `t`
- `ttl`
- `uri`

Kindle 予約キーが検出されると、Braze は `Status Code 400: Kindle Push Reserved Key Used` を返します。

