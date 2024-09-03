---
nav_title: iOS
article_title: Unityのプッシュ通知
platform:
  - Unity
  - iOS
channel: push
ex_push_payload: archive/apple/push_payload.json
page_order: 1
description: "この参考記事では、UnityプラットフォームにおけるiOSプッシュ通知の統合について説明する。"

---

# iOSプッシュ通知の統合

> この参考記事では、UnityプラットフォームにおけるiOSプッシュ通知の統合について説明する。

## ステップ1:自動または手動プッシュ統合を選択する

Brazeは、iOSプッシュ統合を自動化するためのUnityネイティブソリューションを提供する。

- ビルドしたXcodeプロジェクトを修正して手動で統合を完了したい場合は、[ネイティブのiOSプッシュ][8]手順に従ってほしい。
- 手動統合から自動統合に移行する場合は、[自動統合への移行の][2]指示に従う。
- 当社の自動プッシュ通知ソリューションは、iOS 12の暫定認証機能を利用しており、ネイティブのプッシュプロンプトポップアップでは使用できない。

## ステップ2:自動プッシュ統合を導入する

### プッシュ通知を構成する

[iOSプッシュ通知設定ドキュメントに従って][8]、`.p8` ファイルを使用してBrazeを設定する。

### 自動プッシュ統合を有効にする

Unity EditorでBraze**> Braze Configurationに**移動して、Braze Configuration Settingsを開く。

**Integrate Push With Brazeを**チェックすると、自動的にプッシュ通知用にユーザーを登録し、プッシュトークンをBrazeに渡し、プッシュ開封のアナリティクスを追跡し、デフォルトのプッシュ通知処理を利用できる。

### バックグラウンドプッシュを有効にする（オプション）

プッシュ通知で`background mode` 、**Enable Background Pushに**チェックを入れる。これにより、プッシュ通知が届くと、システムがアプリケーションを`suspended` の状態から目覚めさせ、アプリケーションがプッシュ通知に応じてコンテンツをダウンロードできるようになる。このオプションをチェックすることは、アンインストール追跡機能に必要である。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、"Automate Unity iOS integration"、"Integrate push with braze"、"Enable background push "が有効になっている。][29]

### 自動登録を無効にする（オプション）

まだプッシュ通知をオプトインしていないユーザーは、アプリケーションを開くと自動的にプッシュ通知が許可される。この機能を無効にし、手動でユーザーをプッシュ登録するには、**Disable Automatic Push Registration**（**自動プッシュ登録を無効にする**）をチェックする。

- iOS12以降で**Disable Provisional Authorizationが**チェックされていない場合、ユーザーはクワイエットプッシュの受信を暫定的に（無言で）許可される。チェックした場合、ユーザーにネイティブのプッシュプロンプトが表示される。
- 実行時にプロンプトが表示されるタイミングを正確に設定する必要がある場合は、Brazeコンフィギュレーションエディタからの自動登録を無効にし、代わりに`AppboyBinding.PromptUserForPushPermissions()` 。

![UnityエディターはBrazeの設定オプションを表示する。このエディタでは、"Automate Unity iOS integration"、"integrate push with braze"、"disable automatic push registration "が有効になっている。][28]

## ステップ3:プッシュリスナーを設定する

プッシュ通知のペイロードをUnityに渡したり、ユーザーがプッシュ通知を受信したときに追加の処理を行いたい場合、Brazeはプッシュ通知リスナーを設定するオプションを提供する。

### プッシュ受信リスナー

プッシュ受信リスナーは、ユーザーがアプリケーションをアクティブに使用しているとき（アプリがフォアグラウンドになっているときなど）にプッシュ通知を受信すると起動する。Brazeコンフィギュレーションエディターでプッシュ受信リスナーを設定する。ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()` を使い、`BrazeUnityMessageType.PUSH_RECEIVED` を指定する。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、"Set Push Received Listener "オプションを展開し、"Game Object Name"（AppBoyCallback）と "Callback Method Name"（PushNotificationReceivedCallback）を指定する。][30]

### プッシュオープンリスナー

ユーザーがプッシュ通知をクリックしてアプリを起動すると、プッシュ・オープン・リスナーが起動する。Unityにプッシュペイロードを送信するには、**Set Push Opened Listener**オプションでゲームオブジェクトの名前とプッシュオープンリスナーのコールバックメソッドを設定する：

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、"Set Push Received Listener "オプションを展開し、"Game Object Name"（AppBoyCallback）と "Callback Method Name"（PushNotificationOpenedCallback）を指定する。][31]

ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()` を使い、`BrazeUnityMessageType.PUSH_OPENED` を指定する。

### プッシュ・リスナーの実装例

以下の例では、`PushNotificationReceivedCallback` と`PushNotificationOpenedCallback` のコールバック・メソッド名を使って、`AppboyCallback` ゲーム・オブジェクトを実装している。

![この実装例の図は、前のセクションで述べたBrazeのコンフィギュレーションオプションと、C#のコードスニペットを示している。][32]

```csharp
public class MainMenu : MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification received: " + pushNotification);   
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push received Notification event: " + pushNotification);   
#endif  
  }

  void PushNotificationOpenedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification opened: " + pushNotification);  
#elif UNITY_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message);
    Debug.Log("Push opened Notification event: " + pushNotification);   
#endif  
  }
}
```

## 高度な機能

### プッシュトークンコールバック

OSからBrazeデバイストークンのコピーを受け取るには、`AppboyBinding.SetPushTokenReceivedFromSystemDelegate()` を使ってデリゲートを設定する。

### その他の特徴

ディープリンク、バッジカウント、カスタムサウンドなどの高度な機能を実装するには、[iOSネイティブプッシュの説明を][8]ご覧いただきたい。

[1]: #manual-push-integration
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[9]: https://developer.apple.com/ios/manage/overview/index.action "iOSプロビジョニング・ポータル"
[10]: {% image_buster /assets/img_archive/ios_provisioning.png %} "pushNotification2.png"
[11]: {% image_buster /assets/img_archive/AppleProvisioningOptions.png %} "AppleProvisioningOptions.png"
[12]: {% image_buster /assets/img_archive/push_cert_gen.png %} "pushNotification3.png"
[15]: https://github.com/Appboy/appboy-unity-sdk/blob/master/unity-samples/iOS/Roll-A-Ball-Ios/Classes/UnityAppController.mm "sampleAppController.mm"
[24]: {% image_buster /assets/img_archive/Enable_push_capabilities.png %}
[27]: {% image_buster /assets/img/unity/ios/unity_ios_api_key.png %}
[28]: {% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %}
[29]: {% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %}
[30]: {% image_buster /assets/img/unity/ios/unity_ios_push_received.png %}
[31]: {% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %}
[32]: {% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %}
