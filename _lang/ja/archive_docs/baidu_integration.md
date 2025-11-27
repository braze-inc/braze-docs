---
nav_title: Baidu の統合
article_title: バイドゥ・プッシュ通知のAndroidへの統合
platform: Android
permalink: /baidu_integration/
description: "この記事では、Baidu Android 統合の設定方法について説明します。"
hidden: true
---
# Baidu の統合
{% multi_lang_include archive/baidu_deprecation.md %}

Braze は、[Baidu Cloud Push]({% image_buster /assets/img_archive/baidu_app_console.png %}) を使用して Android デバイスにプッシュ通知を送信できます。Baidu Cloud Push を使用すると、Baidu アプリストアを介してアプリを配布する必要が**ありません**。

## ステップ1:Baidu のアカウントを作成する

Baidu アカウントを作成するには、[[Baidu ポータル](https://www.baidu.com/)] にアクセスし、[**登录**] (ログイン) をクリックすると、ログインまたは新しいアカウントを作成するためのダイアログが表示されます。

![]({% image_buster /assets/img_archive/baidu_portal.png %})

新しいアカウントを作成するには、ログインダイアログの一番下にある**立即注册**（新しいアカウント）をクリックする。

![]({% image_buster /assets/img_archive/baidu_login_dialog.png %}){: style="max-width:70%;"}

アカウント作成ページにユーザー名、電話番号、パスワードを入力する。次に、[確認コードを受信] ボタンをクリックします。Baiduから認証コードを含むSMSメッセージが届く。最後に、使用許諾契約書に同意し、[**注册**] (アカウントの作成) をクリックして登録します。これらの設定手順に失敗した場合は、この[ログイン記事](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/)で説明されているように、Baidu Cloud ログイン経由での登録を試します。

![百度サインアップページ]({% image_buster /assets/img_archive/baidu_signup.png %}){: style="max-width:80%;"}

## ステップ2:Baidu の開発者として登録する

次に、Baidu の開発者として登録する必要があります。まず、[Baidu developer portal[](http://developer.baidu.com/) ] にアクセスし、**注册**(create new developer account) を選択して登録を開始する。

![]({% image_buster /assets/img_archive/baidu_dev_portal.png %})

登録ページで、アカウントの種類 (個人用には「个人」、ビジネス用には「公司」) と開発者の種類を選択する (開発者があらかじめ選択されており、ほとんどの場合正しい)。氏名、略歴、電話番号（カッコ内に国番号を含む）を入力する（例：(1)xxxxxxxxxx）。[**发送验证码**] (確認コードを送信) をクリックし、次の行に確認コードを入力します。次の2つのフィールド、開発者のウェブサイトと開発者のロゴは任意である。使用許諾契約に同意し、**提交**（submit）をクリックして送信する。これでBaiduの開発者アカウントを取得したことになる。

![]({% image_buster /assets/img_archive/baidu_dev_reg.png %})

## ステップ 3: Baidu にアプリケーションを登録する

Baidu にアプリケーションを登録するには、[Baidu プロジェクトポータル[](http://developer.baidu.com/console#app/project) にアクセスし、[**创建工程**] (プロジェクトの作成) をクリックします。

![]({% image_buster /assets/img_archive/baidu_project.png %})

次のページで、アプリケーション名を入力します。次の2つのチェックボックスは、Baidu の追加サービスを有効にするためのものです。ほとんどの場合、これらは空白のままでよい。

![]({% image_buster /assets/img_archive/baidu_app_name.png %})

アプリケーションをセットアップすると、APIキーを含むアプリケーションに関する情報を表示するコンソールが表示される。次に、サイドバーの [**云推送**] (クラウドプッシュ)」に移動します。次のページで、**推送设置**（プッシュを設定する）をクリックする。

![]({% image_buster /assets/img_archive/baidu_app_console.png %})

![]({% image_buster /assets/img_archive/baidu_continue.png %})

次のページで、アプリのパッケージ名（例えば、`com.braze.sample` ）を入力し、メッセージをキャッシュするかどうか、キャッシュする場合はその期間（時間単位）を指定する。これは、Baidu に対して、オフラインユーザーにメッセージの送信を試行し続ける時間を示します。**保存设置**（設定を保存する）をクリックして保存する。

![]({% image_buster /assets/img_archive/baidu_configure_cloud.png %})

## ステップ 4: アプリケーションに Baidu を追加する

[Baidu プッシュ SDK ポータル[](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk) にアクセスし、最新の Baidu Cloud Push Android SDK をダウンロードします。

![]({% image_buster /assets/img_archive/baidu_sdk.png %})

SDK の中には、プッシュサービスの jar とプラットフォーム固有のネイティブライブラリがあります。これらをプロジェクトに組み込む。ご使用のアプリが現在 Baidu でサポートされている最新の SDK バージョンを対象にしていることを確認します。このドキュメントは、Baidu Cloud push Android SDK バージョン`4.6.2.38` を対象としています。

以下の必要なBaiduパーミッションをアプリケーションの`AndroidManifest.xml` に追加する。

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

Baiduのライブラリには、受信したプッシュ・メッセージを処理するブロードキャスト・レシーバーが含まれている。アプリケーションの `AndroidManifest.xml` 内の `<application>` 要素内で内部 Baidu レシーバーを宣言します。

```xml
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
```

また、プッシュメッセージや通知の着信をリッスンするブロードキャストレシーバーも作成する必要があります。アプリケーションの `AndroidManifest.xml`、`<application>` 要素の中でレシーバーを宣言します。このレシーバーは、`com.baidu.android.pushservice.PushMessageReceiver` を拡張し、Baidu プッシュサービスからイベント更新を受け取るメソッドを実装する必要があります。

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

メインアクティビティの `onCreate()` メソッドに次の行を追加します。これにより、アプリケーションが Baidu に登録され、着信プッシュメッセージのリッスンが開始されます。「Your-API-Key」をプロジェクトの Baidu API キーに置き換えてください。

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

最後に、ユーザーをBrazeに登録する必要がある。このステップで作成した Baidu ブロードキャストレシーバーの `onBind()` メソッドで、`Braze.registerAppboyPushMessages(channelId)` を使用して `channelId` を Braze に送信します。

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

## ステップ 5: プッシュ開封を登録する

Baiduは、JSON形式のプッシュ・メッセージで余分なキー・バリュー・ペアの送信をサポートしている。ブロードキャストレシーバーの `public void onNotificationClicked(Context context, String title, String description, String customContentString)` メソッドは、ユーザーが着信プッシュメッセージをクリックするたびに呼び出されます。パラメータ`customContentString` には、JSON形式のエクストラが含まれる。Brazeからのすべてのメッセージには、以下の2つのキーと値のペアが含まれる：

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

`onNotificationClicked` が Baidu レシーバーと呼ばれるたびに、レシーバーは `customContentString` を含むアプリケーションに [Intent[](http://developer.android.com/reference/android/content/Intent.html) を送信する必要があります。あなたのアプリケーションは、`customContentString` を使用してBrazeにクリックを記録する。

次のサンプルコードは、`customContentString` をBrazeに渡し、クリックのログを取る：

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

## ステップ 6: エクストラ

Braze が使用する予約キー以外に、`customContentString` パラメーターには、ユーザー定義のカスタムのキーと値のペアがすべて含まれています。キーと値のペアを抽出するには、JSONObject で `customContentString` をラップし、エキストラを取得します。

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

## ステップ 7:Baidu キーを設定する

Braze ダッシュボードに Baidu API キーとBaidu シークレットキーを入力する必要があります。どちらのキーも Baidu のアプリケーションコンソールから利用できます。

**Manage Settings**ページで、Android Chinaアプリを選択し、プッシュ通知セクションにBaidu API KeyとBaidu Secret Keyを入力する。

![]({% image_buster /assets/img_archive/baidu_api_key.png %} "APIKey"){: style="max-width:80%;"}

## その他のリソース

- [Baidu ポータル](https://www.baidu.com/)
- [百度開発者ポータル[](http://developer.baidu.com/)
- [百度プロジェクトポータル[](http://developer.baidu.com/console#app/project)
- [百度プッシュSDKポータル[](http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk)
- [Baidu 統合ドキュメント[](http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview)

