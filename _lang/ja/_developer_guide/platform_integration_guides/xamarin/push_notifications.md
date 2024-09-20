---
nav_title: プッシュ通知
article_title: Xamarinのプッシュ通知
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 1
description: "この記事では、XamarinプラットフォームにおけるAndroid、FireOS、iOSのプッシュ通知統合について説明する。"
channel: push
toc_headers: h2
---

# プッシュ通知の統合

> XamarinでAndroid、FireOS、iOSのプッシュ通知を設定する方法を学ぶ。

## 前提条件

この機能を使用するには、[Xamarinプラットフォーム用のBraze SDKを統合する]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup/)必要がある。

## プッシュ通知の統合

{% tabs %}
{% tab アンドロイド %}
{% alert tip %}
JavaとC#で名前空間がどのように変わるかは、[GitHubのXampleサンプルアプリを](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp)チェックしてほしい。
{% endalert %}

Xamarinのプッシュ通知を統合するには、ネイティブのAndroidプッシュ通知の手順を完了する必要がある。以下の手順はあくまで概要である。完全なチュートリアルについては、[ネイティブ・プッシュ通知ガイドを]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/integration/standard_integration/)参照のこと。

### ステップ1:プロジェクトを更新する

1. AndroidプロジェクトにFirebaseを追加する。
2. Androidプロジェクトの`build.gradle` にCloud Messagingライブラリを追加する：
  ```gradle
  implementation "google.firebase:firebase-messaging:+"
  ```

### ステップ2:JSON認証情報を作成する

1. Google Cloudで、[Firebase Cloud Messaging APIを](https://console.cloud.google.com/apis/library/fcm.googleapis.com)有効にする。
2. **Service Accounts**> your project >**Create Service Accountを**選択し、サービスアカウント名、ID、説明を入力する。完了したら、**Createを選択して続ける**。
3. \[**ロール**] フィールドで、ロールのリストから \[**Firebase Cloud Messaging API 管理者**] を見つけて選択します。
4. **Service Accountsで**プロジェクトを選択し、<i class="fa-solid fa-ellipsis-vertical"></i> **Actions**>**Manage Keys**>**Add Key**>**Create new keyを**選択する。\[**JSON**] を選択し、\[**作成**] を選択します。

### ステップ3:JSON認証情報をアップロードする

1. Braze で、<i class="fa-solid fa-gear"></i>\[**設定**] > \[**アプリの設定**] を選択します。Androidアプリの**プッシュ通知設定で** **Firebaseを**選択し、**Upload JSON Fileを**選択して、先ほど生成した認証情報をアップロードする。完了したら、\[**保存**] を選択します。
2. Firebase Consoleにアクセスして、FCMトークンの自動登録を有効にする。プロジェクトを開き、<i class="fa-solid fa-gear"></i> **Settings**>**Project settingsを**選択する。\[**Cloud Messaging**] を選択し、\[**Firebase Cloud Messaging API (V1)**] で \[**送信者 ID**] フィールドの数字をコピーします。
3. Android Studioプロジェクトの`braze.xml` 。

  ```xml
  <bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
  <string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
  ```

{% alert important %}
サイレントプッシュ通知を送信するたびにBrazeが不要なネットワークリクエストをトリガーするのを防ぐには、`Application` クラスの`onCreate()` メソッドで設定されている自動ネットワークリクエストをすべて削除する。詳細については、[Android 開発者リファレンス:アプリケーション](https://developer.android.com/reference/android/app/Application)を参照してください。
{% endalert %}
{% endtab %}

{% tab アイオス %}
### ステップ1:初期設定を完了する

プッシュを使ったアプリケーションのセットアップや、認証情報をサーバーに保存する方法については、[スウィフトとの統合に関する説明を]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration)参照のこと。詳細は[iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp)サンプル・アプリケーションを参照のこと。

### ステップ2:プッシュ通知の許可をリクエストする

Xamarin SDKが自動プッシュ設定をサポートするようになった。Brazeインスタンス構成に以下のコードを追加して、プッシュ自動化とパーミッションを設定する：

```csharp
configuration.Push.Automation = new BRZConfigurationPushAutomation(true);
configuration.Push.Automation.RequestAuthorizationAtLaunch = false;
```

詳細は[iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/tree/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp)サンプル・アプリケーションを参照のこと。詳細については、[ Xamarin.iOS の Enhanced User Notifications](https://learn.microsoft.com/en-us/previous-versions/xamarin/ios/platform/user-notifications/enhanced-user-notifications?tabs=macos) の Xamarin ドキュメントを参照のこと。
{% endtab %}
{% endtabs %}
