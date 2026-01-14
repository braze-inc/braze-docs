{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## プッシュ通知の設定

{% tabs %}
{% tab android %}
{% alert tip %}
Java と C# で名前空間がどのように変わるかは、[GitHub のXample サンプルアプリ](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp)をチェックしてください。
{% endalert %}

.NET MAUI（旧Xamarin）のプッシュ通知を統合するには、Androidネイティブのプッシュ通知のステップを完了する必要がある。以下の手順はあくまで概要である。完全なチュートリアルについては、[ネイティブ・プッシュ通知ガイドを]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/?tab=android/)参照のこと。

### ステップ1:プロジェクトを更新する

1. AndroidプロジェクトにFirebaseを追加する。
2. Android プロジェクトの `build.gradle` に Cloud Messaging ライブラリを追加します。
  ```gradle
  implementation "google.firebase:firebase-messaging:+"
  ```

### ステップ2:JSON認証情報を作成する

1. Google Cloud で、[Firebase Cloud Messaging API](https://console.cloud.google.com/apis/library/fcm.googleapis.com) を有効にします。
2. [**サービスアカウント**] > [プロジェクト] > [**サービスアカウントの作成**] の順に選択し、サービスアカウント名、ID、説明を入力します。完了したら、**Createを選択して続ける**。
3. [**ロール**] フィールドで、ロールのリストから [**Firebase Cloud Messaging API 管理者**] を見つけて選択します。
4. [**サービスアカウント**] でプロジェクトを選択し、<i class="fa-solid fa-ellipsis-vertical"></i>[**アクション**] > [**キーの管理**] > [**キーの追加**] > [**新しいキーの作成**] の順に選択します。[**JSON**] を選択し、[**作成**] を選択します。

### ステップ3:JSON認証情報をアップロードする

1. Braze で、<i class="fa-solid fa-gear"></i>[**設定**] > [**アプリの設定**] を選択します。Android アプリの [**プッシュ通知設定**] で [**Firebase**] を選択し、[**JSON ファイルのアップロード**] を選択して、先ほど生成した認証情報をアップロードします。完了したら、[**保存**] を選択します。
2. Firebase Consoleにアクセスして、FCMトークンの自動登録を有効にする。プロジェクトを開き、<i class="fa-solid fa-gear"></i>[**設定**] > [**プロジェクト設定**] の順に選択します。[**Cloud Messaging**] を選択し、[**Firebase Cloud Messaging API (V1)**] で [**送信者 ID**] フィールドの数字をコピーします。
3. Android Studio プロジェクトで、以下を `braze.xml` に追加します。

  ```xml
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
  ```

{% alert important %}
サイレントプッシュ通知を送信するたびにBrazeが不要なネットワークリクエストをトリガーするのを防ぐには、`Application` クラスの`onCreate()` メソッドで設定されている自動ネットワークリクエストをすべて削除する。詳細については、[Android 開発者リファレンス:アプリケーション](https://developer.android.com/reference/android/app/Application)を参照してください。
{% endalert %}
{% endtab %}

{% tab ios %}
### ステップ 1: 初期設定を完了する

プッシュを使ったアプリケーションの設定や、認証情報をサーバーに保存する方法については、[SWIFT の統合に関する説明]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift)を参照してください。詳細は[iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp)サンプル・アプリケーションを参照のこと。

### ステップ2:プッシュ通知の許可をリクエストする

当社の.NET MAUI SDKが自動プッシュ設定をサポートするようになった。Brazeインスタンス構成に以下のコードを追加して、プッシュ自動化とパーミッションを設定する：

```csharp
configuration.Push.Automation = new BRZConfigurationPushAutomation(true);
configuration.Push.Automation.RequestAuthorizationAtLaunch = false;
```

詳細は[iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp)サンプル・アプリケーションを参照のこと。詳細については、[Xamarin.iOS の拡張ユーザー通知](https://learn.microsoft.com/en-us/previous-versions/xamarin/ios/platform/user-notifications/enhanced-user-notifications?tabs=macos)に関する Xamarin ドキュメントを参照してください。
{% endtab %}
{% endtabs %}
