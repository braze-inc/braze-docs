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

# Android プッシュ通知の統合

> このリファレンス記事では、Unityプラットフォーム用のAndroidプッシュ通知統合について説明する。

これらの手順は、[Firebase Cloud Messaging (FCM)](https://firebase.google.com/docs/cloud-messaging/) とプッシュを統合するためのものである。

ADM 統合の手順については、[[Unity ADM]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/adm_push_notifications/)] ドキュメントを 参照してください。

## ステップ 1:Firebaseを有効にする

開始するには、[Firebase Unity の設定ドキュメント](https://firebase.google.com/docs/unity/setup)に従ってください。

{% alert note %}
Firebase Unity SDK を統合すると、`AndroidManifest.xml` がオーバーライドされる場合があります。その場合は、必ず元に戻すこと。
{% endalert %}

## ステップ2:Firebaseの認証情報を設定する

Firebase サーバーキーと送信者 ID を Braze ダッシュボードに入力する必要があります。これを行うには、[Firebase Developers Console](https://console.firebase.google.com/)にログインし、Firebase プロジェクトを選択します。次に、[**設定**] で「**クラウドメッセージング**」を選択し、サーバーキーと送信者 ID をコピーします。<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

Braze の**アプリ設定**ページの [**設定の管理**] で Android アプリを選択します。次に、[**Firebase Cloud Messaging サーバーキー**] フィールドに「Firebase サーバーキー」を入力し、「**Firebase Cloud メッセージング送信者**」ID フィールドに「Firebase 送信者 ID」を入力します。

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")

## ステップ 3: 自動プッシュ統合を導入する

Braze SDK は、Firebase Cloud メッセージングサーバーへのプッシュ登録を自動的に処理して、デバイスがプッシュ通知を受信できるようにすることができます。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、「Unity Android 統合を自動化する」、「プッシュ通知 Firebase プッシュ」、「プッシュ構成によりプッシュディープリンクを自動的に処理する」、「プッシュ構成プッシュ通知 HTML レンダリング有効化」、「プッシュDeleted/Opened/Received リスナーを設定」が設定されています。「Firebase 送信者 ID」、「描画可能なアイコン (小/大)」、「デフォルト通知アクセントカラー」というフィールドも用意されています。]({% image_buster /assets/img/unity/android/unity_android_push_settings_config.png %}「Android プッシュ設定」)

- **Firebase Cloud メッセージングの自動登録が有効に**<br> デバイスの FCM プッシュトークンを自動的に取得して送信するように Braze SDK に指示します。 
- **Firebase クラウドメッセージング送信者 ID**<br> Firebase コンソールの送信者 ID。
- **プッシュディープリンクを自動的に処理する**<br> プッシュ通知がクリックされたときに、ディープリンクを開くかアプリを開くかを SDK で処理するかどうか。
- **描画可能な小さな通知アイコン**<br>Drawable は、プッシュ通知を受け取るたびに小さなアイコンとして表示されなければなりません。アイコンが提供されていない場合、通知はアプリケーションアイコンをスモールアイコンとして使用する。

## ステップ 4:プッシュリスナーを設定する

プッシュ通知のペイロードをUnityに渡したり、ユーザーがプッシュ通知を受信したときに追加の処理を行いたい場合、Brazeはプッシュ通知リスナーを設定するオプションを提供する。

Braze の**アプリ設定**ページの [**設定の管理**] で Android アプリを選択します。次に、Firebase サーバーキーを [**プッシュ通知設定**] フィールドに、Firebase 送信者 ID を [**プッシュ通知設定**] ID フィールドに入力します。

#### プッシュ受信リスナー

プッシュ受信リスナーは、ユーザーがプッシュ通知を受信したときに起動される。Unity にプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、[**プッシュ受信リスナーの設定**] の下にある受信リスナーのコールバックメソッドをプッシュします。

#### プッシュ開封済みリスナー

ユーザーがプッシュ通知をクリックしてアプリを起動すると、プッシュ開封済みリスナーが起動します。Unity にプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、[**プッシュ開封済みリスナーを設定する**] の下にある開封済みリスナーのコールバックメソッドをプッシュします。

#### プッシュ削除リスナー (Android のみ)

プッシュ削除リスナーは、ユーザーがプッシュ通知をスワイプして削除したり、無視したときに起動されます。Unity にプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、[**プッシュ削除済みリスナーを設定する**] の下にある削除済みリスナーのコールバックメソッドをプッシュします。

#### プッシュ・リスナーの実装例

次の例では、コールバックメソッド名 `PushNotificationReceivedCallback`、`PushNotificationOpenedCallback`、および `PushNotificationDeletedCallback` をそれぞれ使用して、`BrazeCallback` ゲームオブジェクトを実装します。

![この実装例の図は、前のセクションで述べた Braze の構成オプションと、C# のコードスニペットを示しています。]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %}「Android フルリスナーの例」)

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

[Braze Unity SDK](https://github.com/Appboy/appboy-unity-sdk/tree/master/unity-samples)リポジトリのサンプルプロジェクトには、FCMを含む完全な動作サンプルアプリが含まれている。

## アプリ内リソースへのディープリンク

Braze はデフォルトで標準的なディープリンク (Web サイトのURL、Android の URI など) を処理できますが、カスタムディープリンクを作成するには、追加のマニフェスト設定が必要です。

設定ガイダンスについては、[[アプリ内リソースへのディープリンク](https://developer.android.com/training/app-links/deep-linking)] を参照してください。

## Braze プッシュ通知アイコンの追加

プロジェクトにプッシュアイコンを追加するには、アイコンイメージファイルを含むAndroid アーカイブ(AAR) プラグインまたはAndroid ライブラリを作成します。手順と情報については、Unity のドキュメントを参照してください。[AndroidライブラリプロジェクトとAndroidアーカイブプラグイン](https://docs.unity3d.com/Manual/AndroidAARPlugins.html)。