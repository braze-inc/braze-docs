---
nav_title: 百度の統合
article_title: バイドゥ・プッシュ通知のAndroidへの統合
platform: Android
permalink: /baidu_integration/
description: "この記事では、百度アンドロイドとの統合をセットアップする方法を紹介する。"
hidden: true
---
# 百度の統合
{% multi_lang_include アーカイブ/baidu_deprecation.md %}

Brazeは、\[Baidu Cloud Push][14].なお、Baidu Cloud Pushを利用する**場合**、Baidu App Store経由でアプリを配布する必要は**ない**。

## ステップ 1:百度のアカウントを作成する

百度アカウントを作成するには、[百度ポータルに][7]アクセスし、**登录**（ログイン）をクリックすると、ログインまたは新しいアカウントを作成するためのダイアログが表示される。

![][33]

新しいアカウントを作成するには、ログインダイアログの一番下にある**立即注册**（新しいアカウント）をクリックする。

![][38]{: style="max-width:70%;"}

アカウント作成ページにユーザー名、電話番号、パスワードを入力する。次に、検証コードを受け取るボタンをクリックする。Baiduから認証コードを含むSMSメッセージが届く。最後に、使用許諾契約書に同意し、**注册**（アカウント作成**）を**クリックして登録する。これらのセットアップ手順に失敗した場合は、この[ログイン記事で](https://www.adchina.io/how-to-open-a-baidu-account-outside-china/)説明されているように、Baiduクラウドログイン経由で登録を試みる。

![百度サインアップページ][17]{: style="max-width:80%;"}

## ステップ2:百度の開発者として登録する

次に、百度の開発者として登録しなければならない。まず、\[Baidu developer portal][36] ] にアクセスし、**注册**(create new developer account) を選択して登録を開始する。

![][37]

登録ページで、アカウントの種類（個人用には个人、ビジネス用には公司）と開発者の種類を選択する（ほとんどの場合、開発者があらかじめ選択されており、正しい）。氏名、略歴、電話番号（カッコ内に国番号を含む）を入力する（例：(1)xxxxxxxxxx）。**发送**验证码（認証コードを送信）をクリックし、次の行に認証コードを入力する。次の2つのフィールド、開発者のウェブサイトと開発者のロゴは任意である。使用許諾契約に同意し、**提交**（submit）をクリックして送信する。これでBaiduの開発者アカウントを取得したことになる。

![][13]

## ステップ 3:百度にアプリケーションを登録する

百度にアプリケーションを登録するには、\[百度プロジェクトポータル][11] ]にアクセスし、**创建**工程（プロジェクトの作成）をクリックする。

![][10]

次のページで、アプリケーション名を入力する。次の2つのチェックボックスは、百度の追加サービスを有効にするためのものである。ほとんどの場合、これらは空白のままでよい。

![][26]

アプリケーションをセットアップすると、APIキーを含むアプリケーションに関する情報を表示するコンソールが表示される。次に、サイドバーの「**云**推送（クラウドプッシュ）」に移動する。次のページで、**推送设置**（プッシュを設定する）をクリックする。

![][14]

![][29]

次のページで、アプリのパッケージ名（例えば、`com.braze.sample` ）を入力し、メッセージをキャッシュするかどうか、キャッシュする場合はその期間（時間単位）を指定する。これは、バイドゥに対して、オフラインのユーザーへのメッセージ送信をいつまで継続するかを示すものである。**保存设置**（設定を保存する）をクリックして保存する。

![][39]

## ステップ 4:アプリケーションに百度を追加する

Baidu push SDK portal][40] ] にアクセスし、最新のBaidu Cloud Push Android SDKをダウンロードする。

![][41]

SDKの中には、プッシュ・サービスのjarとプラットフォーム固有のネイティブ・ライブラリがある。これらをプロジェクトに組み込む。あなたのアプリが、百度が現在サポートしているSDKの最高バージョンをターゲットにしていることを確認する。このドキュメントは、Baidu Cloud push Android SDK バージョン`4.6.2.38` のものである。

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

Baiduのライブラリには、受信したプッシュ・メッセージを処理するブロードキャスト・レシーバーが含まれている。アプリケーションの`AndroidManifest.xml` 、`<application>` 要素の中で内部百度レシーバーを宣言する。

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

また、プッシュ・メッセージや通知の着信をリッスンするブロードキャスト・レシーバーも作成する必要がある。アプリケーションの`AndroidManifest.xml` 、`<application>` 要素の中で受信機を宣言する。このレシーバーは、`com.baidu.android.pushservice.PushMessageReceiver` を拡張し、百度プッシュ・サービスからのイベント更新を受け取るメソッドを実装する必要がある。

```xml
      <receiver android:name=".MyPushMessageReceiver">
        <intent-filter>
          <action android:name="com.baidu.android.pushservice.action.MESSAGE"/>
          <action android:name="com.baidu.android.pushservice.action.RECEIVE"/>
          <action android:name="com.baidu.android.pushservice.action.notification.CLICK"/>
        </intent-filter>
      </receiver>
```

メイン・アクティビティの`onCreate()` ・メソッドに、以下の行を追加し、アプリケーションを百度に登録し、受信プッシュ・メッセージのリッスンを開始する。Your-API-Key "をプロジェクトのBaidu API Keyに置き換えてほしい。

```
PushManager.startWork(getApplicationContext(), PushConstants.LOGIN_TYPE_API_KEY, "Your-API-Key");
```

最後に、ユーザーをBrazeに登録する必要がある。このステップで作成した百度放送受信機の`onBind()` メソッドで、`Braze.registerAppboyPushMessages(channelId)` を使って`channelId` をBrazeに送信する。

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

## ステップ 5: プッシュオープンを登録する

Baiduは、JSON形式のプッシュ・メッセージで余分なキー・バリュー・ペアの送信をサポートしている。ブロードキャスト・レシーバーの`public void onNotificationClicked(Context context, String title, String description, String customContentString)` メソッドは、ユーザーが受信プッシュ・メッセージをクリックするたびに呼び出される。パラメータ`customContentString` には、JSON形式のエクストラが含まれる。Brazeからのすべてのメッセージには、以下の2つのキーと値のペアが含まれる：

  ```json
  {
    "source": "Appboy",
    "cid": "your-campaign-Id"
  }
  ```

`onNotificationClicked` があなたの Baidu レシーバーに呼び出されるたびに、レシーバーは`customContentString` を含む \[Intent][44] ] をあなたのアプリケーションに送信する必要がある。あなたのアプリケーションは、`customContentString` を使用してBrazeにクリックを記録する。

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

Brazeが使用する予約キー以外に、`customContentString` パラメーターには、ユーザー定義のカスタムキーと値のペアがすべて含まれる。キーと値のペアを取り出すには、`customContentString` をJSONObjectでラップし、エキストラを取り出す：

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

## ステップ 7:百度キーを設定する

BrazeダッシュボードにBaidu API KeyとBaidu Secret Keyを入力する必要がある。どちらのキーも百度のアプリケーション・コンソールから利用できる。

**Manage Settings**ページで、Android Chinaアプリを選択し、プッシュ通知セクションにBaidu API KeyとBaidu Secret Keyを入力する。

![][19]{: style="max-width:80%;"}

## その他のリソース

- [百度ポータル][7]
- \[百度開発者ポータル][36]
- \[百度プロジェクトポータル][11]
- \[百度プッシュSDKポータル][40]
- \[バイドゥ統合ドキュメント][43]

[7]: https://www.baidu.com/
[10]: {% image_buster /assets/img_archive/baidu_project.png %}
[11]: http://developer.baidu.com/console#app/project
[13]: {% image_buster /assets/img_archive/baidu_dev_reg.png %}
[14]: {% image_buster /assets/img_archive/baidu_app_console.png %}
[17]: {% image_buster /assets/img_archive/baidu_signup.png %}
[19]: {% image_buster /assets/img_archive/baidu_api_key.png %} 「APIKey」である。
[26]: {% image_buster /assets/img_archive/baidu_app_name.png %}
[29]: {% image_buster /assets/img_archive/baidu_continue.png %}
[33]: {% image_buster /assets/img_archive/baidu_portal.png %}
[34]: {% image_buster /assets/img_archive/baidu_email.png %}
[35]: {% image_buster /assets/img_archive/baidu_text.png %}
[36]: http://developer.baidu.com/
[37]: {% image_buster /assets/img_archive/baidu_dev_portal.png %}
[38]: {% image_buster /assets/img_archive/baidu_login_dialog.png %}
[39]: {% image_buster /assets/img_archive/baidu_configure_cloud.png %}
[40]: http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/sdk/clientsdk
[41]: {% image_buster /assets/img_archive/baidu_sdk.png %}
[43]: http://developer.baidu.com/wiki/index.php?title=docs/frontia/guide-android/overview
[44]: http://developer.android.com/reference/android/content/Intent.html
