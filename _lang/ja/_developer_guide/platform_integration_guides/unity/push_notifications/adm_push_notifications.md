---
nav_title: アマゾン・デバイス・メッセージング
article_title: Unity用Amazonデバイス・メッセージング・プッシュ通知
platform: 
  - Unity
  - Android
page_order: 2
description: "このリファレンス記事では、Unityプラットフォーム用のAmazon Androidプッシュ通知統合について説明する。"
channel: push

---

# アマゾン・デバイス・メッセージング

> このリファレンス記事では、Unityプラットフォーム用のAmazon Androidプッシュ通知統合について説明する。

プッシュ通知は、重要なアップデートが発生したときにユーザーの画面に表示されるアプリ外のアラートです。プッシュ通知は、時間的制約があって関連性の高いコンテンツをユーザーに提供したり、ユーザーをアプリに再エンゲージしたりするための効果的な方法です。

ADM (Amazon Device Messaging) は、Amazon 以外のデバイスではサポートされていません。Kindle プッシュをテストするには、[FireOS デバイス](https://developer.amazon.com/appsandservices/apis/engage/device-messaging/tech-docs/04-integrating-your-app-with-adm)が必要です。その他のベストプラクティスについては、[ヘルプセクションを]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/troubleshooting/)チェックしてほしい。

Braze は、[Amazon Device Messaging (ADM)](https://developer.amazon.com/public/apis/engage/device-messaging) を使用して Amazon デバイスにプッシュ通知を送信します。

## ステップ 1:ADM を有効にする

1. まだ作成していない場合は、[Amazon Apps & Games Developer Portal](https://developer.amazon.com/public) を使用してアカウントを作成します。
2. [OAuth 認証情報 (クライアント ID とクライアントシークレット) と ADM API キー](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)を取得します。
3. [Unity Braze 設定]ウィンドウで [**自動 ADM 登録が有効**] を有効にします。 
  - または、`res/values/braze.xml` ファイルに次の行を追加して、ADM 登録を有効にすることもできます。

  ```xml
  <bool name="com_braze_push_adm_messaging_registration_enabled">true</bool>
  ```

## ステップ2:Unity AndroidManifest.xml の更新

アプリに `AndroidManifest.xml` がない場合、以下をテンプレートとして使用できます。そうでない場合は、すでに`AndroidManifest.xml` をお持ちの場合、以下の欠落しているセクションのいずれかが、既存の`AndroidManifest.xml` に追加されていることを確認すること。

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

## ステップ3:ADM API キーを保存する

まず、[アプリの ADM API キーを取得](https://developer.amazon.com/public/apis/engage/device-messaging/tech-docs/02-obtaining-adm-credentials)します。 次に、ADM API キーを`api_key.txt` という名前のファイルに保存し、プロジェクトの[`Assets/`](https://docs.unity3d.com/Manual/AndroidAARPlugins.html) フォルダに保存します。

Amazon は、末尾の改行などの空白文字が `api_key.txt` に含まれている場合、キーを認識しません。

`mainTemplate.gradle` ファイルに以下を追加する：

```gradle
task copyAmazon(type: Copy) {
    def unityProjectPath = $/file:///**DIR_UNITYPROJECT**/$.replace("\\", "/")
    from unityProjectPath + '/Assets/api_key.txt'
    into new File(projectDir, 'src/main/assets')
}

preBuild.dependsOn(copyAmazon)
```

## ステップ4: ADMジャーを追加する

必要なADM Jar ファイルは、[Unity JAR ドキュメント](https://docs.unity3d.com/Manual/AndroidJARPlugins.html) に従ってプロジェクト内の任意の場所に配置できます。

## ステップ 5:クライアントシークレットとクライアント ID を Braze ダッシュボードに追加する

最後に、[ステップ 1](#step-1-enable-adm) で取得したクライアントシークレットとクライアント ID を Braze ダッシュボードの [**設定の管理**] ページに追加する必要があります。

![]({% image_buster /assets/img_archive/fire_os_dashboard.png %})

