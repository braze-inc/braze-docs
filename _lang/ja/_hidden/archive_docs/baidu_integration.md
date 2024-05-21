---
nav_title: Baiduの統合
article_title: Baidu プッシュ通知統合 for Android
platform: Android
permalink: /baidu_integration/
description: "この記事では、バイドゥの Android 統合を設定する方法について説明します。"
hidden: true
---
# Baiduの統合
{% multi_lang_include archive/baidu_deprecation.md %}

Brazeは、[Baidu Cloud Push][14]を使用してAndroidデバイスにプッシュ通知を送信できます。Baidu Cloud Push を使用する場合 **、** Baidu App Store 経由でアプリを配布する必要はありません。

## ステップ 3:バイドゥのアカウントを作成する

バイドゥアカウントを作成するには、 [バイドゥポータル][7] にアクセスし、[ **登录** \](ログイン)をクリックして、ログインまたは新しいアカウントを作成するためのダイアログを表示します。

![][33]

新しいアカウントを作成するには、ログインダイアログの下部にある[ **立即注册** \](新しいアカウント)をクリックします。

![][38]{: style="max-width:70%;"}

ユーザー名、電話番号、パスワードをアカウント作成ページに入力します。次に、確認コードの受信ボタンをクリックします。これで、確認コードが記載された SMS メッセージが Baidu から届きます。最後に、使用許諾契約に同意し、「 **アカウント** の作成」をクリックして登録します。これらの設定手順が失敗した場合は、この [ログイン記事](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/)の説明に従って、Baidu Cloud ログインを使用して登録してみてください。

![Baiduサインアップページ][17]{: style="max-width:80%;"}

## ステップ 3:バイドゥの開発者として登録する

次に、バイドゥの開発者として登録する必要があります。まず、[Baidu開発者ポータル][36]にアクセスし、 **注册** (新しい開発者アカウントの作成)を選択して登録を開始します。

![][37]

登録ページで、アカウントの種類 (個人の場合は个人、ビジネスの場合は公司) と開発者の種類 (ほとんどの場合、開発者が事前に選択されており、正しい) を選択します。名前、自己紹介、電話番号を括弧で囲んで国番号を入力します(例:(1)xxxxxxxxxx)。**[发送验证码**]をクリックし、次の行に確認コードを入力します。次の 2 つのフィールド (開発者 Web サイトと開発者ロゴ) は省略可能です。使用許諾契約に同意し、「 **提交** 」(submit)をクリックして送信します。これで、バイドゥの開発者アカウントが作成されました。

![][13]

## ステップ 3:アプリケーションを Baidu に登録する

アプリケーションを Baidu に登録するには、[Baidu プロジェクト ポータル][11] にアクセスし、[ **プロジェクト** の作成] をクリックします。

![][10]

次のページで、アプリケーション名を入力します。次の 2 つのチェックボックスは、追加のバイドゥ サービスをアクティブ化するためのものです。ほとんどの場合、これらは空白のままにする必要があります。

![][26]

アプリケーションをセットアップすると、APIキーなど、アプリに関する情報を表示するコンソールが表示されます。次に、サイドバーの **云推送** (クラウドプッシュ)に移動します。次のページで、[ **推送设置** ] をクリックします。

![][14]

![][29]

次のページで、アプリのパッケージ名 ( `com.braze.sample`など) を入力し、メッセージをキャッシュするかどうか、キャッシュする場合はその期間 (時間単位) を指定します。これは、オフライン ユーザーへのメッセージ送信の試行を継続する期間を Baidu に示します。**保存设置**(save settings)をクリックして保存します。

![][39]

## ステップ 4: アプリケーションに Baidu を追加する

[Baidu Push SDK portal][40] にアクセスし、最新の Baidu Cloud Push Android SDK をダウンロードします。

![][41]

SDK 内には、プッシュ サービス jar とプラットフォーム固有のネイティブ ライブラリがあります。これらをプロジェクトに統合します。アプリが Baidu で現在サポートされている最新の SDK バージョンをターゲットとしていることを確認します。このドキュメントは、Baidu Cloud プッシュ Android SDK バージョン `4.6.2.38`用の最新のものです。

次の必要な Baidu アクセス許可をアプリケーションの `AndroidManifest.xml`.

```xml
    <uses-permission android:name="android.permission.READ_PHONE_STATE" />
    <uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
    <uses-permission android:name="android.permission.WRITE_SETTINGS" />
    <uses-permission android:name="android.permission.VIBRATE" />
    <uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE" />
    <uses-permission android:name="android.permission.DISABLE_KEYGUARD" />
    <uses-permission android:name="android.permission.ACCESS_WIFI_STATE" />
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

Baidu のライブラリには、受信プッシュメッセージを処理するブロードキャストレシーバーが含まれています。内部 Baidu レシーバーをアプリケーションの `AndroidManifest.xml` 要素内で `<application>` 宣言します。

'''xml
  <!-- 用于接收系统消息以保证 PushService 正常运行 -->
      <receiver
        android:name="com.baidu.android.pushservice.PushServiceReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="android.intent.action.BOOT_COMPLETED"/>
          <action android:name="android.net.conn.CONNECTIVITY_CHANGE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.SHOW"/>
          <action android:name="com.baidu.android.pushservice.action.media.CLICK"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务接收客户端发送的各种请求-->
      <!-- 注意:RegistrationReceiver 在 2.1.1 及之前版本有拼写失误,为 RegistratonReceiver ,用 新版本 SDK 时请更改为如下代码-->
      <receiver
        android:name="com.baidu.android.pushservice.RegistrationReceiver"
        android:process=":bdservice_v1">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.METHOD"/>
          <action android:name="com.baidu.android.pushservice.action.BIND_SYNC"/>
        </intent-filter>
        <intent-filter>
          <action android:name="android.intent.action.PACKAGE_REMOVED"/>
          <data android:scheme="package"/>
        </intent-filter>
      </receiver>
      <!-- Push 服务 -->
      <!-- 注意:在 4.0 (包含)之后的版本需加上如下所示的 intent-filter action -->
      <service
        android:name="com.baidu.android.pushservice.PushService"
        android:exported="true"
        android:process=":bdservice_v1">
        <intent-filter >
          <action android:name="com.baidu.android.pushservice.action.PUSH_SERVICE"/>
        </intent-filter>
      </service>


また、受信プッシュメッセージと通知をリッスンするブロードキャストレシーバーも作成する必要があります。アプリケーションの `AndroidManifest.xml` 要素内でレシーバーを宣言します `<application>` 。この受信者は、Baidu プッシュ サービスからイベントの更新を受信するメソッドを拡張し `com.baidu.android.pushservice.PushMessageReceiver` て実装する必要があります。

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

メインアクティビティの `onCreate()` メソッドに次の行を追加して、アプリケーションを Baidu に登録し、受信プッシュメッセージのリッスンを開始します。「Your-API-Key」をプロジェクトの Baidu API キーに置き換えてください。

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

最後に、Brazeにユーザーを登録する必要があります。`onBind()`この手順で作成したBaiduブロードキャストレシーバーの方法で、を使用してBraze`Braze.registerAppboyPushMessages(channelId)`に送信します`channelId`。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).setRegisteredPushToken(channelId);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).setRegisteredPushToken(channelId)
```

{% endtab %}
{% endtabs %}

## ステップ 5: プッシュオープンの登録

バイドゥは、JSON 形式のプッシュメッセージで追加のキーと値のペアの送信をサポートしています。ブロードキャスト受信者の `public void onNotificationClicked(Context context, String title, String description, String customContentString)` メソッドは、ユーザーが受信プッシュメッセージをクリックするたびに呼び出されます。パラメーター `customContentString` には、JSON 形式のエクストラが含まれています。Brazeからのすべてのメッセージには、次の2つのキーと値のペアが含まれます。

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

が Baidu レシーバーと呼ばれるたびに `onNotificationClicked` 、受信者は を含む [Intent][44] をアプリケーション `customContentString`に送信する必要があります。アプリケーションは、 を使用してクリックを Braze `customContentString`に記録します。

次のサンプルコードはBrazeに渡され `customContentString` 、クリックを記録します。

{% tabs %}
{% tab JAVA %}

  ```java
  String customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY);
  BrazeNotificationUtils.logBaiduNotificationClick(mApplicationContext, customContentString);
  ```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val customContentString = intent.getStringExtra(ChinaPushMessageReceiver.NOTIFICATION_CLICKED_KEY)
BrazeNotificationUtils.logBaiduNotificationClick(context, customContentString)
```

{% endtab %}
{% endtabs %}

## ステップ 3:エキストラ

Brazeが使用する予約済みキーの他に、このパラメータ `customContentString` にはユーザー定義のカスタムキーと値のペアもすべて含まれます。キーと値のペアを抽出するには、JSONObject でラップ `customContentString` し、エクストラを取得します。

{% tabs %}
{% tab JAVA %}

```java
try {
  JSONObject myExtras = new JSONObject(customContentString);
  String myValue = myExtras.optString("my_key", null);
} catch (Exception e) {
  Log.e(TAG, "Caught an exception processing customContentString");
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
try {
  val myExtras = JSONObject(customContentString)
  val myValue = myExtras.optString("my_key", null)
} catch (e: Exception) {
  Log.e(TAG, "Caught an exception processing customContentString", e)
}
```

{% endtab %}
{% endtabs %}

## ステップ 3:バイドゥのキーを設定する

Baidu API キーと Baidu シークレット キーを Braze ダッシュボードに入力する必要があります。どちらのキーも、Baidu アプリケーション コンソールから使用できます。

[ **設定の管理** ] ページで、Android China アプリを選択し、プッシュ通知セクションに Baidu API キーと Baidu シークレット キーを入力します。

![][19]{: style="max-width:80%;"}

## 参考資料

- [Baiduポータル][7]
- [バイドゥ開発者ポータル][36]
- [百度プロジェクトポータル][11]
- [Baidu プッシュ SDK ポータル][40]
- [Baidu統合ドキュメント][43]

[7]: https://www.baidu.com/
[10]: {% image_buster /assets/img_archive/baidu_project.png %}
[11]:のHTTP://developer.baidu.com/console#app/project
[13]: {% image_buster /assets/img_archive/baidu_dev_reg.png %}
[14]: {% image_buster /assets/img_archive/baidu_app_console.png %}
[17]: {% image_buster /assets/img_archive/baidu_signup.png %}
[19]: {% image_buster /assets/img_archive/baidu_api_key.png %}「APIKey」
[26]: {% image_buster /assets/img_archive/baidu_app_name.png %}
[29]: {% image_buster /assets/img_archive/baidu_continue.png %}
[33]: {% image_buster /assets/img_archive/baidu_portal.png %}
[34]: {% image_buster /assets/img_archive/baidu_email.png %}
[35]: {% image_buster /assets/img_archive/baidu_text.png %}
[36]:のHTTP://developer.baidu.com/
[37]: {% image_buster /assets/img_archive/baidu_dev_portal.png %}
[38]: {% image_buster /assets/img_archive/baidu_login_dialog.png %}
[39]: {% image_buster /assets/img_archive/baidu_configure_cloud.png %}
[40]:のHTTP://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk
[41]: {% image_buster /assets/img_archive/baidu_sdk.png %}
[43]:のHTTP://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview
[44]:のHTTP://developer.android.com/reference/android/content/Intent.html
