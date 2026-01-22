{% multi_lang_include developer_guide/prerequisites/unity.md %}

## プッシュ通知の設定

### ステップ 1: プラットフォームを設定する

{% tabs %}
{% tab Android %}
#### ステップ1.1：Firebaseを有効にする

開始するには、[Firebase Unity の設定ドキュメント](https://firebase.google.com/docs/unity/setup)に従ってください。

{% alert note %}
Firebase Unity SDK を統合すると、`AndroidManifest.xml` がオーバーライドされる場合があります。その場合は、必ず元に戻すこと。
{% endalert %}

#### ステップ1.2：Firebaseの認証情報を設定する

Firebase サーバーキーと送信者 ID を Braze ダッシュボードに入力する必要があります。これを行うには、[Firebase Developers Console](https://console.firebase.google.com/)にログインし、Firebase プロジェクトを選択します。次に、[**設定**] で「**クラウドメッセージング**」を選択し、サーバーキーと送信者 ID をコピーします。<br>![]({% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey")

Braze の**アプリ設定**ページの [**設定の管理**] で Android アプリを選択します。次に、[**Firebase Cloud Messaging サーバーキー**] フィールドに「Firebase サーバーキー」を入力し、「**Firebase Cloud メッセージング送信者**」ID フィールドに「Firebase 送信者 ID」を入力します。

![]({% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey")
{% endtab %}

{% tab Swift %}
#### ステップ1.1：統合方法を検証する

Braze は、iOS プッシュ統合を自動化するための Unity ネイティブソリューションを提供します。代わりに手動で統合の設定と管理を行いたい場合は、[Swiftを参照のこと：プッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift).

それ以外の場合は、次の手順に進みます。

{% alert note %}
当社の自動プッシュ通知ソリューションは、iOS 12の暫定認証機能を利用しており、ネイティブのプッシュプロンプトポップアップでは使用できない。
{% endalert %}
{% endtab %}

{% tab Amazon Device Messaging %}
#### ステップ1.1：ADM を有効にする

1. [Amazon Apps& Games Developer Portalで](https://developer.amazon.com/public)まだアカウントを作成していない場合は、アカウントを作成する。
2. [OAuth 認証情報 (クライアント ID とクライアントシークレット) と ADM API キー](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)を取得します。
3. [Unity Braze 設定]ウィンドウで [**自動 ADM 登録が有効**] を有効にします。 
  - または、`res/values/braze.xml` ファイルに次の行を追加して、ADM 登録を有効にすることもできます。

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```
{% endtab %}
{% endtabs %}

### ステップ 2:プッシュ通知を構成する

{% tabs %}
{% tab Android %}
#### ステップ 2.1: プッシュ設定を行う

Braze SDK は、Firebase Cloud メッセージングサーバーへのプッシュ登録を自動的に処理して、デバイスがプッシュ通知を受信できるようにすることができます。Unityで、**Automate Unity Android Integrationを**有効にし、以下の**プッシュ通知の**設定を行う。

| セッティング                                | 説明                                                                                                                                              |
|----------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Firebase Cloud メッセージングの自動登録が有効に | デバイスの FCM プッシュトークンを自動的に取得して送信するように Braze SDK に指示します。                                                                |
| Firebase クラウドメッセージング送信者 ID     | Firebase コンソールの送信者 ID。                                                                                                                |
| プッシュディープリンクを自動的に処理する    | プッシュ通知がクリックされたときに、ディープリンクを開くかアプリを開くかを SDK で処理するかどうか。                                                  |
| 描画可能な小さな通知アイコン       | Drawable は、プッシュ通知を受け取るたびに小さなアイコンとして表示されなければなりません。アイコンが提供されていない場合、通知はアプリケーションアイコンをスモールアイコンとして使用する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}
{% endtab %}

{% tab Swift %}
#### ステップ 2.1: APN トークンをアップロードする

{% multi_lang_include developer_guide/swift/apns_token.md %}

#### ステップ 2.2:自動プッシュをイネーブルメントにする

Unity エディターで **[Braze] > [Braze 構成]** の順に移動して、[Braze 構成設定] を開きます。

[**プッシュと Braze を統合する**] をチェックして、プッシュ通知用に自動的にユーザーを登録し、プッシュトークンを Braze に渡し、プッシュ開封の分析を追跡し、デフォルトのプッシュ通知処理を利用します。

#### ステップ 2.3:バックグラウンドプッシュを有効にする（オプション）

プッシュ通知で `background mode` を有効にする場合は、[**バックグラウンドプッシュを有効にする**] をオンにします。これにより、プッシュ通知が到着したときにシステムがアプリケーションを `suspended` 状態から復帰させ、アプリケーションがプッシュ通知に応答してコンテンツをダウンロードできるようになります。アンインストールの追跡機能を使用するには、このオプションをオンにする必要があります。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、「Unity iOS 統合の自動化」、「プッシュと Braze の統合」、および「バックグラウンドプッシュの有効化」が有効になっています。]({% image_buster /assets/img/unity/ios/unity_ios_enable_background.png %})

#### ステップ 2.4:自動登録を無効にする（オプション）

まだプッシュ通知をオプトインしていないユーザーは、アプリケーションを開くと自動的にプッシュ通知が許可されます。この機能を無効にし、手動でユーザーをプッシュ登録するには、[**Disable Automatic Push Registration (自動プッシュ登録を無効にする)**] をチェックします。

- IOS 12 以降で [**暫定承認を無効にする**] がオンになっていない場合、ユーザーはサイレントプッシュを受信することを暫定的に (サイレントに) 承認されます。チェックした場合、ユーザーにネイティブのプッシュプロンプトが表示される。
- 実行時にプロンプトが表示されるタイミングを正確に設定する必要がある場合は、Braze 構成エディターから自動登録を無効にし、代わりに `AppboyBinding.PromptUserForPushPermissions()` を使用します。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、「Unity iOS 統合の自動化」、「プッシュと Braze の統合」、および「プッシュの自動登録の有効化」が有効になっています。]({% image_buster /assets/img/unity/ios/unity_ios_disable_auto_push.png %})
{% endtab %}

{% tab Amazon Device Messaging %}
#### ステップ 2.1: `AndroidManifest.xml` を更新する

アプリに`AndroidManifest.xml` がない場合は、以下をテンプレートとして使用できます。それ以外の場合、すでに`AndroidManifest.xml` がある場合は、次のいずれかの欠落セクションが既存の`AndroidManifest.xml` に追加されていることを確認します。

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
          package="REPLACE_WITH_YOUR_PACKAGE_NAME">

  <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
  <uses-permission android:name="android.permission.INTERNET" />
  <permission
    android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE"
    android:protectionLevel="signature" />
  <uses-permission android:name="REPLACE_WITH_YOUR_PACKAGE_NAME.permission.RECEIVE_ADM_MESSAGE" />
  <uses-permission android:name="com.amazon.device.messaging.permission.RECEIVE" />

  <application android:icon="@drawable/app_icon" 
               android:label="@string/app_name">

    <!-- Calls the necessary Braze methods to ensure that analytics are collected and that push notifications are properly forwarded to the Unity application. -->
    <activity android:name="com.braze.unity.BrazeUnityPlayerActivity" 
      android:label="@string/app_name" 
      android:configChanges="fontScale|keyboard|keyboardHidden|locale|mnc|mcc|navigation|orientation|screenLayout|screenSize|smallestScreenSize|uiMode|touchscreen" 
      android:screenOrientation="sensor">
      <meta-data android:name="android.app.lib_name" android:value="unity" />
      <meta-data android:name="unityplayer.ForwardNativeEventsToDalvik" android:value="true" />
      <intent-filter>
        <action android:name="android.intent.action.MAIN" />
        <category android:name="android.intent.category.LAUNCHER" />
      </intent-filter>
    </activity>

    <receiver android:name="com.braze.push.BrazeAmazonDeviceMessagingReceiver" android:permission="com.amazon.device.messaging.permission.SEND">
      <intent-filter>
          <action android:name="com.amazon.device.messaging.intent.RECEIVE" />
          <action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
          <category android:name="REPLACE_WITH_YOUR_PACKAGE_NAME" />
      </intent-filter>
    </receiver>
  </application>
</manifest>
```

#### ステップ 2.2:ADM API キーを保存する

まず、[アプリ用のADM API Keyを生成](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)し、そのキーを`api_key.txt` という名前のファイルに保存して、プロジェクトの [`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html)ディレクトリに追加する。

{% alert important %}
Amazon は、末尾の改行などの空白文字が `api_key.txt` に含まれている場合、キーを認識しません。
{% endalert %}

次に、`mainTemplate.gradle` ：

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

#### ステップ 2.3:ADMジャーを追加する

必要なADM Jar ファイルは、[Unity JAR ドキュメント](https://docs.unity3d.com/Manual/AndroidJARPlugins.html) に従ってプロジェクト内の任意の場所に配置できます。

#### ステップ 2.4:クライアントシークレットとクライアント ID を Braze ダッシュボードに追加する

最後に、[ステップ 1](#unity_step-1-enable-adm) で取得したクライアントシークレットとクライアント ID を Braze ダッシュボードの [**設定の管理**] ページに追加する必要があります。

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})
{% endtab %}
{% endtabs %}

### ステップ 3:プッシュリスナーを設定する

{% tabs %}
{% tab Android %}
#### ステップ 3.1:プッシュ受信リスナーをイネーブルメントする

プッシュ受信リスナーは、ユーザーがプッシュ通知を受信したときに起動される。Unity にプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、[**プッシュ受信リスナーの設定**] の下にある受信リスナーのコールバックメソッドをプッシュします。

#### ステップ 3.2:プッシュ開封リスナーをイネーブルメントする

ユーザーがプッシュ通知をクリックしてアプリを起動すると、プッシュ開封済みリスナーが起動します。Unity にプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、[**プッシュ開封済みリスナーを設定する**] の下にある開封済みリスナーのコールバックメソッドをプッシュします。

#### ステップ3.3：プッシュ削除リスナーをイネーブルメントする

プッシュ削除リスナーは、ユーザーがプッシュ通知をスワイプして削除したり、無視したときに起動されます。Unity にプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、[**プッシュ削除済みリスナーを設定する**] の下にある削除済みリスナーのコールバックメソッドをプッシュします。

#### プッシュ・リスナーの例

次の例では、コールバックメソッド名 `PushNotificationReceivedCallback`、`PushNotificationOpenedCallback`、および `PushNotificationDeletedCallback` をそれぞれ使用して、`BrazeCallback` ゲームオブジェクトを実装します。

![この実装例の図は、前のセクションで述べた Braze の構成オプションと、C# のコードスニペットを示しています。]({% image_buster /assets/img/unity/android/unity_android_full_push_listener.png %} "Android Full Listener Example")

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
{% endtab %}

{% tab Swift %}
#### ステップ 3.1:プッシュ受信リスナーをイネーブルメントする

プッシュ受信リスナーは、ユーザーがアプリケーションをアクティブに使用しているとき（アプリがフォアグラウンドになっているときなど）にプッシュ通知を受信すると起動する。Brazeコンフィギュレーションエディターでプッシュ受信リスナーを設定する。ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()` を使用し、`BrazeUnityMessageType.PUSH_RECEIVED` を指定します。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、「プッシュ受信リスナーの設定」オプションが展開され、「ゲームオブジェクト名」(AppBoyCallback) と「コールバックメソッド名」(PushNotificationReceivedCallback) が指定されます。]({% image_buster /assets/img/unity/ios/unity_ios_push_received.png %})

#### ステップ 3.2:プッシュ開封リスナーをイネーブルメントする

ユーザーがプッシュ通知をクリックしてアプリを起動すると、プッシュ開封済みリスナーが起動します。Unity にプッシュペイロードを送信するには、ゲームオブジェクトの名前を設定し、[**プッシュ開封済みリスナーを設定する**] オプションの下にある開封済みリスナーのコールバックメソッドをプッシュします。

![UnityエディターはBrazeの設定オプションを表示する。このエディターでは、「プッシュ受信リスナーの設定」オプションが展開され、「ゲームオブジェクト名」(AppBoyCallback) と「コールバックメソッド名」(PushNotificationOpenedCallback) が指定されます。]({% image_buster /assets/img/unity/ios/unity_ios_push_opened.png %})

ゲームオブジェクトのリスナーを実行時に設定する必要がある場合は、`AppboyBinding.ConfigureListener()` を使用し、`BrazeUnityMessageType.PUSH_OPENED` を指定します。

#### プッシュ・リスナーの例

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
{% endtab %}

{% tab Amazon Device Messaging %}
[前のステップで](#unity_step-21-update-androidmanifestxml) `AndroidManifest.xml` 、プッシュ・リスナーが自動的に設定された。だから、これ以上の設定は必要ない。

```xml
<action android:name="com.amazon.device.messaging.intent.RECEIVE" />
<action android:name="com.amazon.device.messaging.intent.REGISTRATION" />
```

{% alert note %}
ADMプッシュリスナーについて詳しくは、[アマゾンを参照のこと：Amazon Device Messaging](https://developer.amazon.com/docs/video-skills-fire-tv-apps/integrate-adm.html) を統合する。
{% endalert %}
{% endtab %}
{% endtabs %}

## オプション構成

{% tabs %}
{% tab Android %}
#### アプリ内リソースへのディープリンク

Braze はデフォルトで標準的なディープリンク (Web サイトのURL、Android の URI など) を処理できますが、カスタムディープリンクを作成するには、追加のマニフェスト設定が必要です。

設定ガイダンスについては、[[アプリ内リソースへのディープリンク](https://developer.android.com/training/app-links/deep-linking)] を参照してください。

#### Braze プッシュ通知アイコンの追加

プロジェクトにプッシュアイコンを追加するには、アイコンイメージファイルを含むAndroid アーカイブ(AAR) プラグインまたはAndroid ライブラリを作成します。手順と情報については、Unity のドキュメントを参照してください。[AndroidライブラリプロジェクトとAndroidアーカイブプラグイン](https://docs.unity3d.com/Manual/AndroidAARPlugins.html)。
{% endtab %}

{% tab Swift %}
#### プッシュトークンコールバック

OS から Braze デバイストークンのコピーを受け取るには、`AppboyBinding.SetPushTokenReceivedFromSystemDelegate()` を使用してデリゲートを設定します。
{% endtab %}

{% tab Amazon Device Messaging %}
現時点では、ADMのオプション設定はない。
{% endtab %}
{% endtabs %}
