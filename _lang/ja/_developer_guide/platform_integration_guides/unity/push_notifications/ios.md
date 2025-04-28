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

Braze は、iOS プッシュ統合を自動化するための Unity ネイティブソリューションを提供します。

- ビルドしたXcodeプロジェクトを修正して手動で統合を完了したい場合は、[ネイティブのiOSプッシュ]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)手順に従ってほしい。
- 手動統合から自動統合に移行する場合は、[自動統合への移行]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/ios/#transitioning-from-manual-to-automated-integration-ios)の指示に従ってください。
- 当社の自動プッシュ通知ソリューションは、iOS 12の暫定認証機能を利用しており、ネイティブのプッシュプロンプトポップアップでは使用できない。

## ステップ2:自動プッシュ統合を導入する

### プッシュ通知を構成する

[iOSプッシュ通知設定ドキュメントに従って]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)、`.p8` ファイルを使用してBrazeを設定する。

### 自動プッシュ統合を有効にする

Unity エディターで **[Braze] > [Braze 構成]** の順に移動して、[Braze 構成設定] を開きます。

[**プッシュと Braze を統合する**] をチェックして、プッシュ通知用に自動的にユーザーを登録し、プッシュトークンを Braze に渡し、プッシュ開封の分析を追跡し、デフォルトのプッシュ通知処理を利用します。

### バックグラウンドプッシュを有効にする（オプション）

プッシュ通知で `background mode` を有効にする場合は、[**バックグラウンドプッシュを有効にする**] をオンにします。これにより、プッシュ通知が到着したときにシステムがアプリケーションを `suspended` 状態から復帰させ、アプリケーションがプッシュ通知に応答してコンテンツをダウンロードできるようになります。アンインストールの追跡機能を使用するには、このオプションをオンにする必要があります。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、「Unity iOS 統合の自動化」、「プッシュと Braze の統合」、および「バックグラウンドプッシュの有効化」が有効になっています。]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

### 自動登録を無効にする（オプション）

まだプッシュ通知をオプトインしていないユーザーは、アプリケーションを開くと自動的にプッシュ通知が許可されます。この機能を無効にし、手動でユーザーをプッシュ登録するには、[**Disable Automatic Push Registration (自動プッシュ登録を無効にする)**] をチェックします。

- IOS 12 以降で [**暫定承認を無効にする**] がオンになっていない場合、ユーザーはサイレントプッシュを受信することを暫定的に (サイレントに) 承認されます。チェックした場合、ユーザーにネイティブのプッシュプロンプトが表示される。
- 実行時にプロンプトが表示されるタイミングを正確に設定する必要がある場合は、Braze 構成エディターから自動登録を無効にし、代わりに `AppboyBinding.PromptUserForPushPermissions()` を使用します。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、「Unity iOS 統合の自動化」、「プッシュと Braze の統合」、および「プッシュの自動登録の無効化」が有効になっています。]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})

## ステップ3: プッシュリスナーを設定する

プッシュ通知のペイロードをUnityに渡したり、ユーザーがプッシュ通知を受信したときに追加の処理を行いたい場合、Brazeはプッシュ通知リスナーを設定するオプションを提供する。

### プッシュ受信リスナー

プッシュ受信リスナーは、ユーザーがアプリケーションをアクティブに使用しているとき（アプリがフォアグラウンドになっているときなど）にプッシュ通知を受信すると起動する。Brazeコンフィギュレーションエディターでプッシュ受信リスナーを設定する。ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()` を使用し、`BrazeUnityMessageType.PUSH_RECEIVED` を指定します。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、「プッシュ受信リスナーの設定」オプションが展開され、「ゲームオブジェクト名」(AppBoyCallback) と「コールバックメソッド名」(PushNotificationReceivedCallback) が指定されます。]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

### プッシュ開封済みリスナー

ユーザーがプッシュ通知をクリックしてアプリを起動すると、プッシュ開封済みリスナーが起動します。Unity にプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、[**プッシュ開封済みリスナーを設定する**] オプションの下にある開封済みリスナーのコールバックメソッドをプッシュします。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、「プッシュ受信リスナーの設定」オプションが展開され、「ゲームオブジェクト名」(AppBoyCallback) と「コールバックメソッド名」(PushNotificationOpenedCallback) が指定されます。]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()` を使用し、`BrazeUnityMessageType.PUSH_OPENED` を指定します。

### プッシュ・リスナーの実装例

次の例では、コールバックメソッド名 `PushNotificationReceivedCallback`、および `PushNotificationOpenedCallback` をそれぞれ使用して、`AppboyCallback` ゲームオブジェクトを実装します。

![この実装例の図は、前のセクションで述べた Braze の構成オプションと、C# のコードスニペットを示しています。]({% image_buster /assets/img/unity/ios/unity_ios_appboy_callback.png %})

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

OS から Braze デバイストークンのコピーを受け取るには、`AppboyBinding.SetPushTokenReceivedFromSystemDelegate()` を使用してデリゲートを設定します。

### その他の特徴

ディープリンク、バッジカウント、カスタムサウンドなどの高度な機能を実装するには、[iOS ネイティブプッシュの説明]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/)をご覧ください。

