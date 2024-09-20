---
nav_title: プッシュ通知
article_title: Flutter のプッシュ通知
platform: Flutter
page_order: 2
description: "この記事では、Flutter でのプッシュ通知の実装とテストについて説明します。"
channel: push

---

# プッシュ通知の統合

> この参考記事では、Flutterにプッシュ通知を設定する方法を説明する。プッシュ通知を統合するには、各ネイティブプラットフォームを個別に設定する必要があります。リストされているそれぞれのガイドに従って、インストールを完了します。

## ステップ1:初期設定を完了する

{% tabs %}
{% tab アンドロイド %}
### ステップ1.1：プッシュ登録

GoogleのFirebase Cloud Messaging (FCM) APIを使ってプッシュに登録する。完全なチュートリアルについては、[ネイティブAndroidプッシュ統合ガイドの]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/)以下のステップを参照のこと：

1. [Firebaseをプロジェクトに追加する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project)。
2. [Cloud Messagingを依存関係に追加する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies)。
3. [サービスアカウントを作成する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account)。
4. [JSON認証情報を生成する]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials)。
5. [JSON認証情報をBrazeにアップロードする]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze)。

### ステップ1.2：Google Sender IDを取得する

まず Firebase Console に移動し、プロジェクトを開いて、<i class="fa-solid fa-gear"></i>\[**設定**] > \[**プロジェクト設定**] を選択します。

![設定」メニューを開いたFirebaseプロジェクト]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

**Cloud Messagingを**選択し、**Firebase Cloud Messaging API (V1)の**下にある**Sender IDを**クリップボードにコピーする。

![Firebaseプロジェクトの "Cloud Messaging "ページ。"Sender ID "がハイライトされている。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

### ステップ1.3：更新する `braze.xml`

`braze.xml` ファイルに以下を追加する。`FIREBASE_SENDER_ID` 、前回コピーした送信者IDに置き換える。

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
### ステップ1.1：APN証明書をアップロードする

Appleプッシュ通知サービス（APNs）証明書を生成し、Brazeダッシュボードにアップロードする。完全なチュートリアルについては、[APNs証明書をアップロードするを]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate)参照のこと。

### ステップ1.2：アプリにプッシュ通知を追加する

[iOSのネイティブ・インテグレーション・ガイドに]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)従う。

{% endtab %}
{% endtabs %}

## ステップ2:プッシュ通知イベントをリッスンする（オプション）

Brazeが検知して処理したプッシュ通知イベントをリッスンするには、`subscribeToPushNotificationEvents()` を呼び出し、実行する引数を渡す。

{% alert note %}
Braze プッシュ通知イベントは、Android と iOS の両方で利用できます。プラットフォームが異なるため、iOS はユーザーが通知を操作した場合にのみ Braze プッシュイベントを検出します。
{% endalert %}

```dart
// Create stream subscription
StreamSubscription pushEventsStreamSubscription;

pushEventsStreamSubscription = braze.subscribeToPushNotificationEvents((BrazePushEvent pushEvent) {
  print("Push Notification event of type ${pushEvent.payloadType} seen. Title ${pushEvent.title}\n and deeplink ${pushEvent.url}");
  // Handle push notification events
});

// Cancel stream subscription
pushEventsStreamSubscription.cancel();
```

#### プッシュ通知イベントフィールド

{% alert note %}
iOS のプラットフォーム制限のため、Braze SDK はアプリがフォアグラウンドにあるときにのみプッシュペイロードを処理できます。リスナーは、ユーザーがプッシュを操作した後、iOSで `push_opened` イベントタイプに対してのみトリガーされます。
{% endalert %}

プッシュ通知フィールドの完全なリストについては、以下の表を参照してください。

| フィールド名         | タイプ      | 説明 |
| ------------------ | --------- | ----------- |
| `payloadType`     | string    | 通知ペイロード・タイプを指定する。Braze Flutter SDKから送信される2つの値は`push_opened` と`push_received` 。 iOSでは、`push_opened` イベントのみがサポートされている。 |
| `url`              | string    | 通知によって開かれたURLを指定する。 |
| `useWebview`      | ブール値   | `true` の場合、URLはアプリ内のモーダルウェブビューで開かれる。`false` の場合、URLは端末のブラウザーで開かれる。 |
| `title`            | string    | 通知のタイトルを表す。 |
| `body`             | string    | 通知の本文または内容テキストを表す。 |
| `summaryText`     | string    | 通知の要約テキストを表す。これはiOSの`subtitle` 。 |
| `badgeCount`      | 数値   | 通知のバッジカウントを表す。 |
| `timestamp`        | 数値 | ペイロードがアプリケーションによって受信された時刻を表す。 |
| `isSilent`        | ブール値   | `true` の場合、ペイロードは静かに受信される。Android のサイレントプッシュ通知の送信の詳細については、[Android でのサイレントプッシュ通知]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/silent_push_notifications)を参照してください。iOSのサイレント・プッシュ通知の送信については、[iOSのサイレント・プッシュ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/silent_push_notifications/)通知を参照のこと。 |
| `isBrazeInternal`| ブール値   | ジオフェンス同期、Feature Flag同期、アンインストール追跡など、SDK内部機能のために通知ペイロードが送信された場合、これは`true` 。ペイロードは、ユーザーのために静かに受信される。 |
| `imageUrl`        | string    | 通知画像に関連するURLを指定する。 |
| `brazeProperties` | オブジェクト    | キャンペーンに関連するBrazeのプロパティ（キーと値のペア）を表す。 |
| `ios`              | オブジェクト    | iOS固有のフィールドを表す。 |
| `android`          | オブジェクト    | Android固有のフィールドを表す。 |
{: .reset-td-br-1 .reset-td-br-2}

## ステップ3:プッシュ通知の表示をテストする

ネイティブ・レイヤーでプッシュ通知を設定した後、統合をテストする：

1. Flutter アプリケーションでアクティブユーザーを設定します。これを行うには、`braze.changeUser('your-user-id')` を呼び出してプラグインを初期化します。
2. \[**キャンペーン**] に移動し、新しいプッシュ通知キャンペーンを作成します。テストしたいプラットフォームを選択します。
3. テスト通知を作成し、\[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。
4. まもなくデバイスに通知が届くはずです。通知が表示されない場合は、通知センターで確認するか、設定を更新する必要が生じる場合があります。

{% alert tip %}
Xcode 14から、iOSシミュレーター上でリモート・プッシュ通知をテストできるようになった。
{% endalert %}
