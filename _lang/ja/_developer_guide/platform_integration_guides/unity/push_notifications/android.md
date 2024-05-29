---
nav_title: Android
article_title: Unity用Androidプッシュ通知
platform: 
  - Unity
  - Android
channel: push
page_order: 1
description: "このリファレンス記事では、Unityプラットフォーム用のAndroidプッシュ通知の統合について説明します。"

---

# アンドロイド・プッシュ通知の統合

> このリファレンス記事では、Unityプラットフォーム用のAndroidプッシュ通知の統合について説明します。

これらの手順は、[Firebase Cloud Messaging (FCM][9]) とプッシュを統合するためのものです。

ADMの統合手順については、[Unity ADM][64]のドキュメントを参照してください。

## ステップ 1:Firebaseを有効にする

開始するには、[Firebase Unity セットアップドキュメントに従って][11]ください。

{% alert note %}
Firebase Unity SDK を統合すると、`AndroidManifest.xml` がオーバーライドされる場合があります。その場合は、必ず元に戻してください。
{% endalert %}

## ステップ 2: Firebaseの認証情報を設定する

Firebaseサーバーキーと送信者IDをBrazeダッシュボードに入力する必要があります。Firebase Developers Console][58] にログインし、Firebase プロジェクトを選択します。次に、**Settingsの** **Cloud Messagingを**選択し、Server KeyとSender IDをコピーします：<br>![][59]

Brazeの**アプリ設定**ページの「**設定の管理**」でAndroidアプリを選択します。次に、Firebase**Cloud Messaging Server Key**フィールドに Firebase Server Key を、Firebase**Cloud Messaging Sender**ID フィールドに Firebase Sender ID を入力します。

![][15]

## ステップ 3: 自動プッシュ統合の実装

Braze SDKは、Firebaseクラウドメッセージングサーバーへのプッシュ登録を自動的に処理し、デバイスにプッシュ通知を受信させることができます。

UnityエディターはBrazeの設定オプションを表示します。このエディタでは、"Automate Unity Android Integration"、"Push Notification Firebase Push"、"Push Configuration Handle Push Deeplinks Automatically"、"Push Configuration Push Notification HTML Rendering Enabled"、および "Set Push Deleted "を設定します。/Opened/Received Listeners" are set. The fields "Firebase Sender ID", "Small/Large Icon Drawable", "Default Notification Accent Color" are also provided.][62]

- **Firebase Cloud Messagingの自動登録が有効になりました。**<br> デバイスのFCMプッシュトークンを自動的に取得して送信するようにBraze SDKに指示します。 
- **Firebase Cloud Messaging の送信者 ID**<br> Firebase コンソールからの送信者 ID。
- **ディープリンクを自動的にプッシュする**<br> プッシュ通知がクリックされたときに、SDKがディープリンクを開くか、アプリを開くかを処理するかどうか。
- **小さな通知アイコン**<br>Drawableは、プッシュ通知を受信するたびに小さなアイコンとして表示される必要があります。アイコンが提供されていない場合、通知はアプリケーションアイコンをスモールアイコンとして使用します。

## ステップ 4: プッシュリスナーを設定する

プッシュ通知のペイロードをUnityに渡したり、ユーザーがプッシュ通知を受信したときに追加の処理を行いたい場合、Brazeにはプッシュ通知リスナーを設定するオプションがあります。

Brazeの**アプリ設定**ページの「**設定の管理**」でAndroidアプリを選択します。次に、Firebase Server Keyを**Push Notification Settings**フィールドに、Firebase Sender IDを**Push Notification Settings**IDフィールドに入力します。

#### プッシュ受信リスナー

プッシュ受信リスナーは、ユーザーがプッシュ通知を受信したときに起動されます。Unityにプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、**Set Push Received Listenerの**下に受信リスナーコールバックメソッドをプッシュします。

#### プッシュオープンリスナー

ユーザーがプッシュ通知をクリックしてアプリを起動すると、プッシュ・オープン・リスナーが起動します。Unityにプッシュペイロードを送信するには、**Set Push Opened Listenerで**ゲームオブジェクトの名前とプッシュオープンリスナーのコールバックメソッドを設定します。

#### プッシュ削除リスナー（Androidのみ）

削除されたプッシュ・リスナーは、ユーザーがプッシュ通知をスワイプしたり、削除したりしたときに発行されます。Unityにプッシュペイロードを送信するには、**Set Push Deleted Listenerで**ゲームオブジェクトの名前とプッシュ削除リスナーのコールバックメソッドを設定します。

#### プッシュ・リスナーの実装例

次の例では、`PushNotificationReceivedCallback` 、`PushNotificationOpenedCallback` 、`PushNotificationDeletedCallback` のコールバック・メソッド名を使って、`BrazeCallback` ゲーム・オブジェクトを実装している。

この実装例の図は、前のセクションで述べたBrazeの設定オプションと、C#のコードスニペットを示しています][63]。

\`\`\`csharp
public class MainMenu ：MonoBehaviour {
  void PushNotificationReceivedCallback(string message) {
\#if UNITY\_ANDROID
    Debug.Log("PushNotificationReceivedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message)；
    Debug.Log("Push Notification received: " + pushNotification)；   
\#elif UNITY\_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message)；
    Debug.Log("Push received Notification event: " + pushNotification)；   
\`endif\`  
  ()

  void PushNotificationOpenedCallback(string message) {
\#if UNITY\_ANDROID
    Debug.Log("PushNotificationOpenedCallback message: " + message)；
    PushNotification pushNotification = new PushNotification(message)；
    Debug.Log("Push Notification opened: " + pushNotification)；  
\#elif UNITY\_IOS
    ApplePushNotification pushNotification = new ApplePushNotification(message)；
    Debug.Log("Push opened Notification event: " + pushNotification)；   
\`endif\`  
  ()

  void PushNotificationDeletedCallback(string message) {
\#if UNITY\_ANDROID
    Debug.Log("PushNotificationDeletedCallback message: " + message);
    PushNotification pushNotification = new PushNotification(message)；
    Debug.Log("Push Notification dismissed: " + pushNotification)；  
\`endif\`
  ()
}
\`\`\`

### 実施例

[Braze Unity SDK][13]リポジトリのサンプルプロジェクトには、FCMを含む完全な動作サンプルアプリが含まれています。

## アプリ内リソースへのディープリンク

Brazeは標準的なディープリンク（ウェブサイトのURLやAndroidのURIなど）をデフォルトで扱うことができますが、カスタムディープリンクを作成するには、追加のマニフェスト設定が必要です。

設定ガイダンスについては、[アプリ内リソースへのディープリンク][26]を参照してください。

[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/troubleshooting/
[9]: https://firebase.google.com/docs/cloud-messaging/
[11]: https://firebase.google.com/docs/unity/setup
[12]: https://firebase.google.com/docs/android/setup
[13]: https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples
[15]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey"
[26]: https://developer.android.com/training/app-links/deep-linking
[58]: https://console.firebase.google.com/
[59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %}"FirebaseServerKey"
[61]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/advanced_use_cases
[62]: {% image_buster /assets/img/unity/android/unity_android_push_settings_config.png %} 「アンドロイド・プッシュ設定
[63]: {% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} 「アンドロイド・フルリスナーの例
[64]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/