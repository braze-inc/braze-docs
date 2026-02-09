{% multi_lang_include developer_guide/prerequisites/flutter.md %}

## プッシュ通知の設定

### ステップ 1: 初期設定を完了する

{% tabs %}
{% tab Android %}
#### ステップ1.1：プッシュ登録

Google の Firebase Cloud Messaging (FCM) API を使用してプッシュに登録します。詳しい手順については、「[ネイティブ Android プッシュ通知統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/)」で以下の手順を参照してください。

1. [Firebase をプロジェクトに追加します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-1-add-firebase-to-your-project)。
2. [Cloud Messaging を依存関係に追加します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-2-add-cloud-messaging-to-your-dependencies)。
3. [サービスアカウントを作成します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-3-create-a-service-account)。
4. [JSON 認証情報を生成します]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-4-generate-json-credentials)。
5. [JSON認証情報をBrazeにアップロードする]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#step-5-upload-your-json-credentials-to-braze)。

#### ステップ1.2：Google Sender IDを取得する

まず Firebase Console に移動し、プロジェクトを開いて、<i class="fa-solid fa-gear"></i>[**設定**] > [**プロジェクト設定**] を選択します。

![設定」メニューが開封されたFirebaseプロジェクト。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

[**Cloud Messaging**] 選択し、[**Firebase Cloud Messaging API (V1)**] の下にある [**送信者 ID**] をクリップボードにコピーします。

![Firebaseプロジェクトの "Cloud Messaging "ページで、"Sender ID "がハイライトされている。]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

#### ステップ1.3：`braze.xml` を更新する

`braze.xml` ファイルに以下を追加する。`FIREBASE_SENDER_ID` を、以前にコピーした送信者 ID に置き前ます。

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

{% endtab %}

{% tab iOS %}
#### ステップ1.1：APN証明書をアップロードする

Appleプッシュ通知サービス（APNs）証明書を生成し、Brazeダッシュボードにアップロードする。詳細な手順については、[APN 証明書のアップロード]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-upload-your-apns-certificate)を参照してください。

#### ステップ1.2：アプリにプッシュ通知サポートを追加する

[ネイティブ iOS 統合ガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/?tab=objective-c#automatic-push-integration)の手順に従います。

{% endtab %}
{% endtabs %}

### ステップ2:プッシュ通知イベントをリッスンする（オプション）

Braze が検出して処理したプッシュ通知イベントをリッスンするには、`subscribeToPushNotificationEvents()` を呼び出し、実行する引数を渡します。

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

##### プッシュ通知イベントフィールド

{% alert note %}
iOS のプラットフォーム制限のため、Braze SDK はアプリがフォアグラウンドにあるときにのみプッシュペイロードを処理できます。リスナーは、ユーザーがプッシュを操作した後、iOSで `push_opened` イベントタイプに対してのみトリガーされます。
{% endalert %}

プッシュ通知フィールドの完全なリストについては、以下の表を参照してください。

| フィールド名         | タイプ      | 説明 |
| ------------------ | --------- | ----------- |
| `payloadType`     | 文字列    | 通知ペイロードのタイプを指定します。Braze Flutter SDK から送信される2つの値は、`push_opened` と `push_received` です。 iOS では、`push_opened` イベントのみがサポートされています。 |
| `url`              | 文字列    | 通知によって開かれたURLを指定する。 |
| `useWebview`      | ブール値   | `true` の場合、URLはアプリ内のモーダルウェブビューで開かれる。`false` の場合、URLは端末のブラウザーで開かれる。 |
| `title`            | 文字列    | 通知のタイトルを表す。 |
| `body`             | 文字列    | 通知の本文または内容テキストを表す。 |
| `summaryText`     | 文字列    | 通知の要約テキストを表す。これは iOS で `subtitle` からマップされます。 |
| `badgeCount`      | 数値   | 通知のバッジカウントを表す。 |
| `timestamp`        | 数値 | ペイロードがアプリケーションによって受信された時刻を表す。 |
| `isSilent`        | ブール値   | `true` の場合、ペイロードはサイレントに受信されます。Android のサイレントプッシュ通知の送信の詳細については、[Android でのサイレントプッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)を参照してください。iOS のサイレントプッシュ通知の送信の詳細については、[iOS のサイレントプッシュ通知を参照してください]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)。 |
| `isBrazeInternal`| ブール値   | ジオフェンス同期、機能フラグ同期、またはアンインストールトラッキングなどの内部 SDK 機能に対して通知ペイロードが送信された場合、これは `true` になります。ペイロードはユーザーに対してサイレントに受信されます。 |
| `imageUrl`        | 文字列    | 通知画像に関連するURLを指定する。 |
| `brazeProperties` | オブジェクト    | キャンペーンに関連するBrazeのプロパティ（キーと値のペア）を表す。 |
| `ios`              | オブジェクト    | iOS固有のフィールドを表す。 |
| `android`          | オブジェクト    | Android固有のフィールドを表す。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### ステップ3:プッシュ通知の表示をテストする

ネイティブレイヤーでプッシュ通知を設定した後、統合をテストするには：

1. Flutter アプリケーションでアクティブユーザーを設定します。これを行うには、`braze.changeUser('your-user-id')` を呼び出してプラグインを初期化します。
2. [**キャンペーン**] に移動し、新しいプッシュ通知キャンペーンを作成します。テストしたいプラットフォームを選択します。
3. テスト通知を作成し、[**テスト**] タブに移動します。テストユーザーと同じ `user-id` を追加し、[**テストを送信**] をクリックします。
4. まもなくデバイスに通知が届くはずです。通知が表示されない場合は、通知センターで確認するか、設定を更新する必要が生じる場合があります。

{% alert tip %}
Xcode 14から、iOSシミュレーター上でリモート・プッシュ通知をテストできるようになった。
{% endalert %}
