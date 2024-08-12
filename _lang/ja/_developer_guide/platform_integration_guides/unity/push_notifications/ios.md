---
nav_title: iOS
article_title: Unity のプッシュ通知
platform:
  - Unity
  - iOS
channel: push
ex_push_payload: archive/apple/push_payload.json
page_order: 1
description: "この参考記事では、Unity プラットフォームの iOS プッシュ通知統合について説明します。"

---

# iOS プッシュ通知の統合

> この参考記事では、Unity プラットフォームの iOS プッシュ通知統合について説明します。

## ステップ 1:自動または手動のプッシュ統合を選択

Braze は iOS プッシュ統合を自動化するためのネイティブ Unity ソリューションを提供しています。

- ビルドした Xcode プロジェクトを変更して手動で統合を完了したい場合は、[ネイティブの iOS プッシュ手順に従ってください][8]。
- 手動インテグレーションから自動インテグレーションに移行する場合は、「[自動インテグレーションへの移行][2]」の指示に従ってください。
- 当社の自動プッシュ通知ソリューションはiOS 12の仮承認機能を利用しているため、ネイティブのプッシュプロンプトポップアップでは使用できません。

## ステップ 2: 自動プッシュ統合の実装

### プッシュ通知を構成する

[iOS プッシュ通知設定ドキュメントに従い][8]、`.p8`ファイルを使用して Braze を設定します。

### 自動プッシュ統合を有効にする

Unity エディターで Braze **> Braze 設定に移動して Braze** 設定を開きます。

「**Integrate Push With Braze**」をオンにすると、プッシュ通知へのユーザーの登録、Braze へのプッシュトークンの受け渡し、プッシュオープンの分析の追跡、およびデフォルトのプッシュ通知処理を利用することができます。

### バックグラウンドプッシュを有効にする (オプション)

**プッシュ通知を有効にする場合は、「バックグラウンドプッシュを有効にする**`background mode`」にチェックを入れます。これにより、`suspended`システムはプッシュ通知が到着したときの状態からアプリケーションを復帰させ、アプリケーションがプッシュ通知に応答してコンテンツをダウンロードできるようになります。アンインストール追跡機能を使用するには、このオプションをチェックする必要があります。

![Unity エディターには Braze の設定オプションが表示されます。このエディターでは、「Unity iOS 統合の自動化」、「プッシュと braze の統合」、「バックグラウンドプッシュを有効にする」が有効になっています。] [29]

### 自動登録を無効にする (オプション)

プッシュ通知をまだ選択していないユーザーは、アプリケーションを開くと自動的にプッシュが承認されます。この機能を無効にしてユーザーをプッシュ対象に手動で登録するには、「**自動プッシュ登録を無効にする**」にチェックを入れてください。

- iOS 12 以降で「**仮認証を無効にする**」にチェックが入っていない場合、ユーザーは暫定的に（サイレントに）クワイエットプッシュを受信する権限を与えられます。オンにすると、ユーザーにはネイティブプッシュプロンプトが表示されます。
- 実行時にプロンプトが表示されるタイミングを正確に設定する必要がある場合は、Braze `AppboyBinding.PromptUserForPushPermissions()` 設定エディターからの自動登録を無効にして代わりに使用してください。

![Unity エディターには Braze の設定オプションが表示されます。このエディターでは、「Unity iOS 統合の自動化」、「プッシュと braze の統合」、「自動プッシュ登録の無効化」が有効になっています。] [28]

## ステップ 3: プッシュリスナーを設定する

プッシュ通知ペイロードを Unity に渡したり、ユーザーがプッシュ通知を受け取ったときに追加の手順を実行したりする場合、Braze にはプッシュ通知リスナーを設定するオプションが用意されています。

### プッシュ受信リスナー

プッシュ受信リスナーは、ユーザーがアプリケーションをアクティブに使用している間（アプリがフォアグラウンド状態になったときなど）にプッシュ通知を受け取ったときに起動されます。Braze 設定エディターでプッシュ受信リスナーを設定します。実行時にゲームオブジェクトリスナーを設定する必要がある場合は`AppboyBinding.ConfigureListener()`、を使用して指定してください`BrazeUnityMessageType.PUSH_RECEIVED`。

![Unity エディターには Braze の設定オプションが表示されます。このエディターでは、「プッシュ受信リスナーの設定」オプションが拡張され、「ゲームオブジェクト名」(AppBoyCallback) と「コールバックメソッド名」(PushNotificationReceivedCallback) が提供されています。] [30]

### プッシュオープンリスナー

プッシュオープンリスナーは、ユーザーがプッシュ通知をクリックしてアプリを起動したときに起動されます。プッシュペイロードを Unity に送信するには、ゲームオブジェクトの名前を設定し、Set Push Opened Listener **オプションでオープンされたリスナーのコールバックメソッドをプッシュします**。

![Unity エディターには Braze の設定オプションが表示されます。このエディターでは、「プッシュ受信リスナーの設定」オプションが拡張され、「ゲームオブジェクト名」(AppBoyCallback) と「コールバックメソッド名」(PushNotificationOpenedCallback) が提供されています。] [31]

実行時にゲームオブジェクトリスナーを設定する必要がある場合は`AppboyBinding.ConfigureListener()`、を使用して指定してください`BrazeUnityMessageType.PUSH_OPENED`。

### プッシュリスナーの実装例

次の例では`PushNotificationOpenedCallback`、`AppboyCallback``PushNotificationReceivedCallback`それぞれとというコールバックメソッド名を使用してゲームオブジェクトを実装しています。

![この実装例の図は、前のセクションで説明した Braze 設定オプションと C# コードスニペットを示しています。] [32]

\`\`\`csharp
パブリッククラスのメインメニュー:MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
\#if ユニティ\_アンドロイド
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
\#elif UNITY\_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
\`endif\`  
  ()

  void PushNotificationOpenedCallback(string message) {
\#if ユニティ\_アンドロイド
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
\#elif UNITY\_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
\`endif\`  
  ()
}
\`\`\`

## 高度な機能

### プッシュトークンのコールバック

OS から Braze デバイストークンのコピーを受け取るには、を使用してデリゲートを設定します。`AppboyBinding.SetPushTokenReceivedFromSystemDelegate()`

### その他の機能

ディープリンク、バッジカウント、カスタムサウンドなどの高度な機能を実装するには、[iOSのネイティブプッシュ手順をご覧ください][8]。

[1]: #manual-push-integration
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[9]: https://developer.apple.com/ios/manage/overview/index.action "iOS プロビジョニングポータル"
[10]: {% image_buster /assets/img_archive/ios_provisioning.png %} 「pushNotification2.png」
[11]: {% image_buster /assets/img_archive/AppleProvisioningOptions.png %} 「AppleProvisioningOptions.png」
[12]: {% image_buster /assets/img_archive/push_cert_gen.png %} 「pushNotification3.png」
[15]: https://github.com/Appboy/appboy-unity-sdk/blob/master/unity-samples/iOS/Roll-A-Ball-Ios/Classes/UnityAppController.mm "sample AppController.mm"
[24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %}
[27]: {% image_buster /assets/img/unity/ios/unity_ios_api_key.png %}
[28]: {% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %}
[29]: {% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %}
[30]: {% image_buster /assets/img/unity/ios/unity_ios_push_received.png %}
[31]: {% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %}
[32]: {% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %}
