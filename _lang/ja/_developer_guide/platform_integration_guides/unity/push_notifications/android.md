---
nav_title: Android
article_title: Unity用Androidプッシュ通知
platform: 
  - Unity
  - Android
channel: push
page_order: 1
description: "このリファレンス記事では、Unityプラットフォーム用のAndroidプッシュ通知統合について説明する。"

---

# アンドロイド・プッシュ通知の統合

> このリファレンス記事では、Unityプラットフォーム用のAndroidプッシュ通知統合について説明する。

これらの手順は、[Firebase Cloud Messaging (FCM)][9] とプッシュを統合するためのものである。

ADM統合の手順については、\[Unity ADM][64] ドキュメント]を参照のこと。

## ステップ 1:Firebaseを有効にする

始めるには、[Firebase Unityのセットアップ・ドキュメントに][11]従う。

{% alert note %}
Firebase Unity SDK を統合すると、`AndroidManifest.xml` がオーバーライドされることがある。その場合は、必ず元に戻すこと。
{% endalert %}

## ステップ2:Firebaseの認証情報を設定する

Firebaseサーバーキーと送信者IDをBrazeダッシュボードに入力する必要がある。これを行うには、\[Firebase Developers Console][58] ] にログインし、Firebase プロジェクトを選択する。次に、**「設定**」で**クラウド・メッセージングを**選択し、サーバー・キーと送信者IDをコピーする：<br>![][59]

Brazeの**アプリ設定**ページで、**設定の管理から**Androidアプリを選択する。次に、Firebase**Cloud Messaging Server Key**フィールドに Firebase Server Key を、**Firebase Cloud Messaging Sender**ID フィールドに Firebase Sender ID を入力する。

![][15]

## ステップ 3:自動プッシュ統合を導入する

Braze SDKは、Firebase Cloud Messaging Serversへのプッシュ登録を自動的に処理し、デバイスがプッシュ通知を受け取れるようにすることができる。

![UnityエディターはBrazeの設定オプションを表示する。このエディタでは、"Automate Unity Android Integration"、"Push Notification Firebase Push"、"Push Configuration Handle Push Deeplinks Automatically"、"Push Configuration Push Notification HTML Rendering Enabled"、"Set PushDeleted/Opened/Received Listeners "を設定する。Firebase Sender ID"、"Small/Large Icon Drawable"、"Default Notification Accent Color "フィールドも用意されている。][62]

- **Firebaseクラウドメッセージングの自動登録を有効にする**<br> デバイスのFCMプッシュトークンを自動的に取得して送信するようBraze SDKに指示する。 
- **Firebaseクラウドメッセージング送信者ID**<br> Firebaseコンソールからの送信者ID。
- **ディープリンクを自動的にプッシュする**<br> プッシュ通知がクリックされたときに、SDKがディープリンクを開くかアプリを開くかを処理するかどうか。
- **小さな通知アイコン**<br>Drawableは、プッシュ通知を受け取るたびに小さなアイコンとして表示されなければならない。アイコンが提供されていない場合、通知はアプリケーションアイコンをスモールアイコンとして使用する。

## ステップ 4:プッシュリスナーを設定する

プッシュ通知のペイロードをUnityに渡したり、ユーザーがプッシュ通知を受信したときに追加の処理を行いたい場合、Brazeはプッシュ通知リスナーを設定するオプションを提供する。

Brazeの**アプリ設定**ページで、**設定の管理から**Androidアプリを選択する。次に、Firebase Server Keyを**Push Notification Settings**フィールドに、Firebase Sender IDを**Push Notification Settings**IDフィールドに入力する。

#### プッシュ受信リスナー

プッシュ受信リスナーは、ユーザーがプッシュ通知を受信したときに起動される。Unityにプッシュ・ペイロードを送信するには、ゲーム・オブジェクトの名前を設定し、**Set Push Received Listenerの**下にあるreceived listenerコールバック・メソッドをプッシュする。

#### プッシュオープンリスナー

ユーザーがプッシュ通知をクリックしてアプリを起動すると、プッシュ・オープン・リスナーが起動する。Unityにプッシュペイロードを送信するには、ゲームオブジェクトの名前とプッシュオープンリスナーのコールバックメソッドを**Set Push Opened Listenerで**設定する。

#### プッシュ削除リスナー（Androidのみ）

削除されたプッシュ・リスナーは、ユーザーがプッシュ通知をスワイプしたり、削除したりしたときに発行される。Unityにプッシュペイロードを送信するには、ゲームオブジェクトの名前とプッシュ削除リスナーのコールバックメソッドを**Set Push Deleted Listenerで**設定する。

#### プッシュ・リスナーの実装例

以下の例では、`PushNotificationReceivedCallback` 、`PushNotificationOpenedCallback` 、`PushNotificationDeletedCallback` のコールバック・メソッド名を使って、`BrazeCallback` ゲーム・オブジェクトを実装している。

![この実装例の図は、前のセクションで述べたBrazeのコンフィギュレーションオプションと、C#のコードスニペットを示している。][63]

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

  void PushNotificationDeletedCallback(string message) {
#if UNITY_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message);
    Debug.Log("Push Notification dismissed: " + pushNotification);  
#endif
  }
}
```

### 実施例

[Braze Unity SDK][13]リポジトリのサンプルプロジェクトには、FCMを含む完全な動作サンプルアプリが含まれている。

## アプリ内リソースへのディープリンク

Brazeはデフォルトで標準的なディープリンク（ウェブサイトのURL、AndroidのURIなど）を扱うことができるが、カスタムディープリンクを作成するには、追加のマニフェスト設定が必要である。

設定ガイダンスについては、\[アプリ内リソースへのディープリンク][26] を参照のこと。

[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/troubleshooting/
[9]: https://firebase.google.com/docs/cloud-messaging/
[11]: https://firebase.google.com/docs/unity/setup
[12]: https://firebase.google.com/docs/android/setup
[13]: https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples
[15]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey"
[26]: https://developer.android.com/training/app-links/deep-linking
[58]: https://console.firebase.google.com/
[59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey"
[61]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases
[62]: {% image_buster /assets/img/unity/android/unity_android_push_settings_config.png %} 「アンドロイド・プッシュ設定
[63]: {% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} 「アンドロイド・フルリスナーの例
[64]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/