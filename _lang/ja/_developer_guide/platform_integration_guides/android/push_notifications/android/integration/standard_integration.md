---
nav_title: 標準の統合
article_title: Android 向け標準プッシュ通知の統合
platform: Android
page_order: 0
description: "この記事では、Android アプリケーションにプッシュ通知を統合する方法について説明します。"
channel:
  - push
search_rank: 3
---

# Android の標準プッシュ統合

> Android アプリにプッシュ通知を統合する方法を学びます。

プッシュ通知を使用すると、アプリが閉じている場合でも、関連性が高くて時間的制約のあるコンテンツをデバイス画面に直接送信することで、アプリユーザーを再び引き付けることができます。アプリのプッシュの統合が完了したら、[プッシュのベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)をご確認ください。

{% alert important %}
Android プッシュ統合がすでに設定されており、Google の非推奨  Cloud Messaging API からの移行を検討している場合は、[Firebase Cloud Messaging API への移行]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/migrating_to_firebase_cloud_messaging)を参照してください。
{% endalert %}

## プッシュへの登録

このセクションでは、Google の Firebase Cloud Messaging (FCM) API を使用してプッシュに登録する方法について説明します。Braze Android SDK で FCM を使用したサンプルアプリをご覧になりたい場合は、[Braze:Firebase プッシュサンプルアプリ](https://github.com/braze-inc/braze-android-sdk/tree/master/samples/firebase-push)を参照してください。

### ステップ 1:Firebase をプロジェクトに追加する

まず、Android プロジェクトに Firebase を追加する必要があります。詳細な手順については、Google の [Firebase セットアップガイド][49] を参照してください。

### ステップ 2:Cloud Messaging を依存関係に追加する

次に、Cloud Messaging ライブラリをプロジェクトの依存関係に追加します。Android プロジェクトで `build.gradle` を開き、`dependencies` ブロックに次の行を追加します。

```gradle
implementation "com.braze:android-sdk-ui:+"
```

依存関係は次のようになります。

```gradle
dependencies {
  implementation project(':android-sdk-ui')
  implementation "com.braze:android-sdk-ui:+"
}
```

### ステップ 3:Firebase Cloud Messaging API を有効にする

Google Cloud で、Android アプリが使用しているプロジェクトを選択し、[Firebase Cloud Messaging API](https://console.cloud.google.com/apis/library/fcm.googleapis.com) を有効にします。

![Enabled Firebase Cloud Messaging API]({% image_buster /assets/img/android/push_integration/create_a_service_account/firebase-cloud-messaging-api-enabled.png %}){: style="max-width:80%;"}

### ステップ 4:サービスアカウントを作成する

次に、新しいサービスアカウントを作成し、FCM トークンの登録時に Braze が許可された API 呼び出しを行えるようにします。Google Cloud で、[**サービスアカウント**] に移動し、プロジェクトを選択します。[**サービスアカウント**] ページで [**サービスアカウントの作成**] を選択します。

![A project's service account home page with "Create Service Account" highlighted.]({% image_buster /assets/img/android/push_integration/create_a_service_account/select-create-service-account.png %})

サービスアカウント名、ID、説明を入力して、[**作成して続行**] を選択します。

![The form for "Service account details."]({% image_buster /assets/img/android/push_integration/create_a_service_account/enter-service-account-details.png %})

[**ロール**] フィールドで、ロールのリストから [**Firebase Cloud Messaging API 管理者**] を見つけて選択します。アクセスをより制限する場合は、`cloudmessaging.messages.create` 権限を持つ[カスタムロール](https://cloud.google.com/iam/docs/creating-custom-roles)を作成し、代わりにリストからそれを選択します。[**完了**] を選択します。

{% alert warning %}
[**Firebase Cloud Messaging 管理者**] ではなく、[**Firebase Cloud Messaging _API_ 管理者**] を選択してください。
{% endalert %}

![The form for "Grant this service account access to project" with "Firebase Cloud Messaging API Admin" selected as the role.]({% image_buster /assets/img/android/push_integration/create_a_service_account/add-fcm-api-admin.png %})

### ステップ 5:JSON 認証情報を生成する

次に、FCM サービスアカウントの JSON 認証情報を生成します。Google Cloud IAM & Admin で、[**サービスアカウント**] に移動し、プロジェクトを選択します。[先ほど作成した](#step-3-create-a-service-account) FCM サービスアカウントを見つけて、<i class="fa-solid fa-ellipsis-vertical"></i>[**アクション**] > [**キーの管理**] を選択します。

![The project's service account homepage with the "Actions" menu open.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-manage-keys.png %})

[**キーの追加**] > [**新しいキーを作成**] を選択します。

![The selected service account with the "Add Key" menu open.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create-new-key.png %})

[**JSON**] を選択し、[**作成**] を選択します。キーをどこにダウンロードしたかを覚えておいてください。次のステップで必要になります。

![The form for creating a private key with "JSON" selected.]({% image_buster /assets/img/android/push_integration/generate_json_credentials/select-create.png %}){: style="max-width:65%;"}

{% alert warning %}
秘密キーが漏洩した場合は、セキュリティリスクが生じる可能性があります。JSON の認証情報は安全な場所に保存してください。キーは Braze にアップロードした後で削除します。
{% endalert %}

### ステップ 6:JSON の認証情報を Braze にアップロードする

次に、JSON 認証情報を Braze ダッシュボードにアップロードします。Braze で、<i class="fa-solid fa-gear"></i>[**設定**] > [**アプリの設定**] を選択します。

![The "Settings" menu open in Braze with "App Settings" highlighted.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/select-app-settings.png %})

Android アプリの [**プッシュ通知設定**] で [**Firebase**] を選択し、[**JSON ファイルのアップロード**] を選択して、[先ほど生成した](#step-4-generate-json-credentials)認証情報をアップロードします。完了したら、[**保存**] を選択します。

![The form for "Push Notification Settings" with "Firebase" selected as the push provider.]({% image_buster /assets/img/android/push_integration/upload_json_credentials/upload-json-file.png %})

{% alert warning %}
秘密キーが漏洩した場合は、セキュリティリスクが生じる可能性があります。キーが Braze にアップロードされたので、[先に生成した](#step-4-generate-json-credentials)ファイルを削除します。
{% endalert %}

### ステップ 7:トークンの自動登録を設定する

ユーザーの 1 人がプッシュ通知をオプトインした場合、アプリはそのユーザーにプッシュ通知を送信する前に、ユーザーのデバイス上で FCM トークンを生成する必要があります。Braze SDK を使用すると、プロジェクトの Braze 構成ファイルで各ユーザーのデバイスで FCM トークンの自動登録を有効にすることができます。

まず Firebase Console に移動し、プロジェクトを開いて、<i class="fa-solid fa-gear"></i>[**設定**] > [**プロジェクト設定**] を選択します。

![The Firebase project with the "Settings" menu open.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/select-project-settings.png %})

[**Cloud Messaging**] を選択し、[**Firebase Cloud Messaging API (V1)**] で [**送信者 ID**] フィールドの数字をコピーします。

![The Firebase project's "Cloud Messaging" page with the "Sender ID" highlighted.]({% image_buster /assets/img/android/push_integration/set_up_automatic_token_registration/copy-sender-id.png %})

次に、Android Studio プロジェクトを開き、Firebase 送信者 ID を使用して、`braze.xml` または `BrazeConfig` 内で FCM トークンの自動登録を有効にします。

{% tabs local %}
{% tab braze.xml %}
FCM トークンの自動登録を設定するには、`braze.xml` ファイルに以下の行を追加します。

```xml
<bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">FIREBASE_SENDER_ID</string>
```

`FIREBASE_SENDER_ID` を Firebase プロジェクトの設定からコピーした値に置き換えます。`braze.xml` は次のようになります。

\`\`\`xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">12345ABC-6789-DEFG-0123-HIJK456789LM</string><bool translatable="false" name="com_braze_firebase_cloud_messaging_registration_enabled">true</bool>
<string translatable="false" name="com_braze_firebase_cloud_messaging_sender_id">603679405392</string>
</resources>
```
{% endtab %}
{% tab BrazeConfig %}
FCM トークンの自動登録を設定するには、`BrazeConfig` に以下の行を追加します。

{% subtabs global %}
{% subtab JAVA %}
```java
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
.setIsFirebaseCloudMessagingRegistrationEnabled(true)
.setFirebaseCloudMessagingSenderIdKey("FIREBASE_SENDER_ID")
```
{% endsubtab %}
{% endsubtabs %}

`FIREBASE_SENDER_ID` を Firebase プロジェクトの設定からコピーした値に置き換えます。`BrazeConfig` は次のようになります。

{% subtabs global %}
{% subtab JAVA %}
```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build();
Braze.configure(this, brazeConfig);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
val brazeConfig = BrazeConfig.Builder()
  .setApiKey("12345ABC-6789-DEFG-0123-HIJK456789LM")
  .setCustomEndpoint("sdk.iad-01.braze.com")
  .setSessionTimeout(60)
  .setHandlePushDeepLinksAutomatically(true)
  .setGreatNetworkDataFlushInterval(10)
  .setIsFirebaseCloudMessagingRegistrationEnabled(true)
  .setFirebaseCloudMessagingSenderIdKey("603679405392")
  .build()
Braze.configure(this, brazeConfig)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

{% alert tip %}
代わりに FCM トークンを手動で登録する場合は、アプリの [`onCreate()`](https://developer.android.com/reference/android/app/Application.html#onCreate()) メソッド内で [`Braze.setRegisteredPushToken()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/registered-push-token.html) を呼び出すことができます。
{% endalert %}

### ステップ 8:不要な権限を削除する

新しいプッシュ統合が設定されたら、プロジェクトの `braze.xml` ファイルで Braze に次の権限が必要なくなります。

  ```xml
  <uses-permission android:name="android.permission.GET_ACCOUNTS" />
  <uses-permission android:name="android.permission.WAKE_LOCK" />
  <uses-permission android:name="com.google.android.c2dm.permission.RECEIVE" />
  <permission android:name="YOUR-APPLICATION-PACKAGE-NAME.permission.C2D_MESSAGE" android:protectionLevel="signature"/>
  <uses-permission android:name="YOUR-APPLICATION-PACKAGE-NAME.permission.C2D_MESSAGE" />
  ```

### ステップ 9:アプリケーションクラスの自動リクエストを削除する

サイレントプッシュ通知を送信するたびに Braze が不要なネットワークリクエストをトリガーしないようにするには、`Application` クラスの `onCreate()` メソッドで設定されている自動ネットワークリクエストをすべて削除します。詳細については、[Android 開発者リファレンス:アプリケーション](https://developer.android.com/reference/android/app/Application)を参照してください。

## プッシュ {#displaying-push} の受信と表示

このセクションを完了すると、Braze から送信されたプッシュ通知を受信して表示できるようになります。

### ステップ 1:Braze Firebase メッセージングサービスを登録する

{% alert warning %}
Firebase メッセージングサービスがすでに登録されている場合は、この手順を実行しないでください。代わりに、[独自の Firebase メッセージングサービスの使用](#using-your-own-firebase-messaging-service)に進み、そこに記載されている手順を実行してください。
{% endalert %}

Braze には、プッシュ受信インテントと開封インテントを処理するサービスが含まれています。`BrazeFirebaseMessagingService` クラスは `AndroidManifest.xml` に登録する必要があります。

```xml
<service android:name="com.braze.push.BrazeFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

通知コードでは、`BrazeFirebaseMessagingService` を使用して、オープンアクションとクリックアクションのトラッキングも処理します。このサービスが正しく機能するには、`AndroidManifest.xml` に登録する必要があります。また、Braze はシステムからの通知に一意のキーをプレフィックスとして付けることにも注意してください。これにより、システムから送信された通知のみが表示されるようになります。他の FCM サービスから送信される通知を表示するために、追加のサービスを個別に登録することもできます。Firebase プッシュサンプルアプリの [\`AndroidManifest.xml\`][70] を参照してください。

{% alert important %}
Braze SDK 3.1.1 より前では、FCM プッシュを処理するために `AppboyFcmReceiver` が使用されていました。マニフェストから `AppboyFcmReceiver` クラスを削除し、前述の統合に置き換える必要があります。
{% endalert %}

#### フォールバック Firebase メッセージングサービスの使用

使用したい別の Firebase メッセージングサービスがある場合は、アプリケーションが Braze からではないプッシュを受信した場合に呼び出すフォールバック Firebase メッセージングサービスを指定することもできます。

`braze.xml` で次のように指定します。

```xml
<bool name="com_braze_fallback_firebase_cloud_messaging_service_enabled">true</bool>
<string name="com_braze_fallback_firebase_cloud_messaging_service_classpath">com.company.OurFirebaseMessagingService</string>
```

または、[ランタイム構成:][65] 経由で設定します。

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setFallbackFirebaseMessagingServiceEnabled(true)
        .setFallbackFirebaseMessagingServiceClasspath("com.company.OurFirebaseMessagingService")
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

#### 独自の Firebase メッセージングサービスの使用

Firebase メッセージングサービスがすでに登録されている場合は、[\`RemoteMessage\`][75] オブジェクトを [\`BrazeFirebaseMessagingService.handleBrazeRemoteMessage()\`][74] 経由で Braze に渡すことができます。このメソッドは [\`RemoteMessage\`][75] オブジェクトが Braze から発信された場合にのみ通知を表示し、そうでない場合は無視します。

{% tabs %}
{% tab JAVA %}

```java
public class MyFirebaseMessagingService extends FirebaseMessagingService {
  @Override
  public void onMessageReceived(RemoteMessage remoteMessage) {
    super.onMessageReceived(remoteMessage);
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyFirebaseMessagingService : FirebaseMessagingService() {
  override fun onMessageReceived(remoteMessage: RemoteMessage?) {
    super.onMessageReceived(remoteMessage)
    if (BrazeFirebaseMessagingService.handleBrazeRemoteMessage(this, remoteMessage)) {
      // This Remote Message originated from Braze and a push notification was displayed.
      // No further action is needed.
    } else {
      // This Remote Message did not originate from Braze.
      // No action was taken and you can safely pass this Remote Message to other handlers.
    }
  }
}
```

{% endtab %}
{% endtabs %}

### ステップ 2:小さなアイコンをデザインガイドラインに準拠させる

Android の通知アイコンに関する一般的な情報は、[通知の概要][37] をご覧ください。

Android N 以降、色を使った小さな通知アイコンアセットは更新または削除する必要があります。Android システム (Braze SDK ではない) は、アクションアイコンと小さな通知アイコンの非アルファチャネルと透明チャネルをすべて無視します。つまり、Android は小さな通知アイコンの透明領域を除くすべての部分をモノクロに変換します。

小さな通知アイコンアセットを正しく作成するには:
-画像から白以外のすべての色を削除します。
-アセットの白以外のすべての領域が透明でなければなりません。

{% alert note %}
不適切なアセットでよく見られる問題の 1 つは、小さな通知アイコンが単色の正方形としてレンダリングされることです。これは、Android システムが小さな通知アイコンアセットで透明領域を見つけられないことが原因です。
{% endalert %}

次の図の大小アイコンは、適切にデザインされたアイコンの例です。

!["Hey I'm my way to the bar but.."というメッセージの横の大きなアイコンの下隅に表示される小さなアイコン][38]

### ステップ 3:通知アイコンを設定する

#### braze.xml でのアイコンの指定

Braze では、`braze.xml` 内で描画可能なリソースを指定することで、通知アイコンを設定できます。

```xml
<drawable name="com_braze_push_small_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
<drawable name="com_braze_push_large_notification_icon">REPLACE_WITH_YOUR_ICON</drawable>
```

小さな通知アイコンの設定は必須です。**設定しない場合、Braze はデフォルトで小さな通知アイコンとしてアプリケーションアイコンを使用しますが、これは最適に表示されない可能性があります。**

大きな通知アイコンの設定は任意ですが、推奨されます。

#### アイコンのアクセントカラーの指定

通知アイコンのアクセントカラーは、`braze.xml` でオーバーライドできます。色を指定しない場合、デフォルトの色は Lollipop がシステム通知に使用するのと同じグレーになります。

```xml
<integer name="com_braze_default_notification_accent_color">0xFFf33e3e</integer>
```

オプションでカラーリファレンスを使用することもできます。

```xml
<color name="com_braze_default_notification_accent_color">@color/my_color_here</color>
```

### ステップ 4:ディープリンクを追加する

#### ディープリンクの自動オープンを有効にする

プッシュ通知がクリックされたときに Braze がアプリとディープリンクを自動的に開くようにするには、`braze.xml` で `com_braze_handle_push_deep_links_automatically` を `true` に設定します。

```xml
<bool name="com_braze_handle_push_deep_links_automatically">true</bool>
```

このフラグは [ランタイム設定][65] でも設定できます。

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setHandlePushDeepLinksAutomatically(true)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

ディープリンクをカスタムで処理する場合は、Braze からのプッシュ受信およびオープンインテントをリッスンするプッシュコールバックを作成する必要があります。詳しくは [プッシュの受信と開封のカスタム処理][52] に関する記事をご覧ください。

#### カスタムディープリンクの作成

アプリにディープリンクをまだ追加していない場合は、ディープリンクに関する [Android 開発者向けドキュメント][40] に記載されている手順に従ってください。ディープリンクの詳細については、[FAQ の記事][42] を参照してください。

#### ディープリンクの追加

Braze ダッシュボードは、通知がクリックされたときに開くプッシュ通知キャンペーンとキャンバスでのディープリンクまたは Web URL の設定をサポートしています。

![][41]

#### バックスタックの動作のカスタマイズ

Android SDK のデフォルトでは、プッシュのディープリンクを辿ると、ホストアプリのメインのランチャーアクティビティがバックスタックに配置されます。Braze では、メインのランチャーアクティビティの代わりにバックスタックで開くカスタムアクティビティを設定したり、バックスタックを完全に無効にしたりすることができます。

たとえば、[ランタイム構成][65] を使用して `YourMainActivity` というアクティビティをバックスタックアクティビティとして設定するには、次のように入力します。

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setPushDeepLinkBackStackActivityEnabled(true)
        .setPushDeepLinkBackStackActivityClass(YourMainActivity.class)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

`braze.xml` の同等の設定を参照してください。クラス名は `Class.forName()` で返されるものと同じでなければならないことに注意してください。

```xml
<bool name="com_braze_push_deep_link_back_stack_activity_enabled">true</bool>
<string name="com_braze_push_deep_link_back_stack_activity_class_name">your.package.name.YourMainActivity</string>
```

### ステップ 5:通知チャネルを定義する

Braze Android SDK は [Android 通知チャネル][62] をサポートしています。Braze の通知に通知チャネルの ID が含まれていない場合、または Braze の通知に無効なチャネル ID が含まれている場合、Braze は SDK で定義されているデフォルトの通知チャネルで通知を表示します。Braze のユーザーはプラットフォーム内で [Android 通知チャネル][61] を使用して通知をグループ化します。

デフォルトの Braze 通知チャネルのユーザー向けの名前を設定するには、[\`BrazeConfig.setDefaultNotificationChannelName()\`][72] を使用します。

デフォルトの Braze 通知チャネルのユーザー向けの説明を設定するには、[\`BrazeConfig.setDefaultNotificationChannelDescription()\`][73] を使用します。

[Android プッシュオブジェクト][63] パラメーターを持つ API キャンペーンは、`notification_channel` フィールドを含むように更新する必要があります。このフィールドが指定されていない場合、Braze は [ダッシュボードフォールバック][64] チャネル ID を使用して通知ペイロードを送信します。

デフォルトの通知チャネル以外、Braze はチャネルを作成しません。他のすべてのチャネルは、ホストアプリでプログラムで定義してから、Braze ダッシュボードに入力する必要があります。

デフォルトのチャネル名と説明も `braze.xml` で設定できます。

```xml
<string name="com_braze_default_notification_channel_name">Your channel name</string>
<string name="com_braze_default_notification_channel_description">Your channel description</string>
```

### ステップ 6:通知の表示と分析をテストする

#### 表示のテスト

この時点で、Braze から送信された通知を表示できるはずです。これをテストするには、Braze ダッシュボードの [**キャンペーン**] ページにアクセスし、**プッシュ通知**キャンペーンを作成します。[**Android プッシュ**] を選択し、メッセージをデザインします。次に、作成画面で目のアイコンをクリックしてテスト送信者を取得します。現在のユーザーのユーザー ID またはメールアドレスを入力し、[**テストを送信**] をクリックします。デバイスにプッシュが表示されます。

![][55]

プッシュの表示に関連する問題については、[トラブルシューティングガイド][57] を参照してください。

#### 分析のテスト

この時点で、プッシュ通知の開封に関する分析ログも届いているはずです。届いた通知をクリックすると、キャンペーン結果ページの [**直接開封数**] の値が 1 増えます。プッシュ分析の内訳については、[プッシュレポート]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_reporting/)の記事をご覧ください。

プッシュ分析に関連する問題については、[トラブルシューティングガイド][57] を参照してください。

#### コマンドラインからのテスト

コマンドラインインターフェイスからアプリ内通知とプッシュ通知をテストする場合は、cURL と [メッセージング API][22] を介してターミナルから単一の通知を送信できます。次のフィールドをテストケースの正しい値に置き換える必要があります。

- `YOUR_API_KEY` ([**設定**] > [**API キー**]に移動)
- `YOUR_EXTERNAL_USER_ID` ([**ユーザーを検索**] ページでプロファイルを検索)
- `YOUR_KEY1` (省略可能)
- `YOUR_VALUE1` (省略可能)

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、これらのページは別の場所にあります。<br>\- [**API キー**] は [**開発者コンソール**] > [**API 設定**] にあります。<br>\- [**ユーザー検索**]は、[**ユーザー**] > [**ユーザー検索**] にあります。
{% endalert %}

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer {YOUR_API_KEY}" -d '{
  "external_user_ids":["YOUR_EXTERNAL_USER_ID"],
  "messages": {
    "android_push": {
      "title":"Test push title",
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }  
  }
}' https://rest.iad-01.braze.com/messages/send
```

この例では、`US-01` インスタンスを使用しています。このインスタンスを使用していない場合は、`US-01` エンドポイントを [自分のエンドポイント][66] に置き換えてください。

## 通知の表示のカスタマイズ

### ステップ 1:カスタム通知ファクトリーを作成する

サーバー側では面倒な方法や利用できない方法でプッシュ通知をカスタマイズしたい場合があります。通知表示を完全に制御できるよう追加された機能により、独自の [`IBrazeNotificationFactory`][6] を定義して Braze で表示する通知オブジェクトを作成できるようになりました。

カスタムの `IBrazeNotificationFactory` が設定されている場合、ユーザーに通知が表示される前に、プッシュ受信時に Braze がファクトリーの `createNotification()` メソッドを呼び出します。Braze は、Braze プッシュデータを含む `Bundle` と、ダッシュボードまたはメッセージング API 経由で送信されたカスタムのキーと値のペアを含む別の `Bundle` を渡します。

Braze は Braze プッシュ通知のデータを含む [\`BrazeNotificationPayload\`][77] を渡します。

{% tabs %}
{% tab JAVA %}

\`\`\`java
// Factory method implemented in your custom IBrazeNotificationFactory
@Override
public Notification createNotification(BrazeNotificationPayload brazeNotificationPayload) {
// Example of getting notification title
String title = brazeNotificationPayload.getTitleText();

  // カスタムの KVP ("my\_key" -> "my\_value") の取得の例
  String customKvp = brazeNotificationPayload.getBrazeExtras().getString("my\_key");
}
\`\`\`

{% endtab %}
{% tab KOTLIN %}

\`\`\`kotlin
// Factory method implemented in your custom IBrazeNotificationFactory
override fun createNotification(brazeNotificationPayload: BrazeNotificationPayload): Notification {
// Example of getting notification title
val title = brazeNotificationPayload.getTitleText()

  // カスタムの KVP ("my\_key" -> "my\_value") の取得の例
  val customKvp = brazeNotificationPayload.getBrazeExtras().getString("my\_key")
}
\`\`\`

{% endtab %}
{% endtabs %}

カスタムの `createNotification()` メソッドから `null` を返して通知をまったく表示しないことも、`BrazeNotificationFactory.getInstance().createNotification()` を使用してそのデータのデフォルトの `notification` オブジェクトを取得し、表示前に変更することも、完全に別個の `notification` オブジェクトを生成して表示することもできます。

{% alert note %}
Braze のプッシュデータキーに関するドキュメントは、[Android SDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html) を参照してください。
{% endalert %}

### ステップ 2:カスタム通知ファクトリーを設定する

Braze にカスタム通知ファクトリーを使用するように指示するには、`setCustomBrazeNotificationFactory` メソッドを使用して [`IBrazeNotificationFactory`][6] を設定します。

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(IBrazeNotificationFactory brazeNotificationFactory);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(brazeNotificationFactory: IBrazeNotificationFactory)
```

{% endtab %}
{% endtabs %}

カスタム `IBrazeNotificationFactory` を設定する場所として推奨されるのは、`Application.onCreate()` アプリケーションのライフサイクルメソッド (アクティビティではない) です。これにより、アプリプロセスがアクティブなときはいつでも通知ファクトリーを正しく設定できるようになります。

{% alert important %}
ゼロから独自の通知を作成するのは高度なユースケースです。十分なテストを行い、Braze のプッシュ機能を深く理解した上で行うようにしてください。たとえば、通知がプッシュ通知の開封数を正しくログに記録することを確認する必要があります。
{% endalert %}

カスタム [ の設定を解除し、プッシュのデフォルトの Braze 処理に戻すには、`IBrazeNotificationFactory` をカスタム通知ファクトリー設定機能に渡します。

{% tabs %}
{% tab JAVA %}


```java
setCustomBrazeNotificationFactory(null);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
setCustomBrazeNotificationFactory(null)
```

{% endtab %}
{% endtabs %}

## プッシュプライマー

プッシュプライマーキャンペーンでは、アプリのデバイスでプッシュ通知を有効にするようにユーザーに促します。これは、[ノーコードプッシュプライマー]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)を使用して、SDK のカスタマイズなしで行うことができます。

[6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze-notification-factory/index.html
[8]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[16]: {% image_buster /assets/img_archive/fcm_api_insert.png %} "FCMKey"
[22]: {{site.baseurl}}/api/endpoints/messaging/
[28]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/
[37]: https://developer.android.com/guide/topics/ui/notifiers/notifications
[38]: {% image_buster /assets/img_archive/large_and_small_notification_icon.png %}"大小通知アイコン"
[40]: http://developer.android.com/training/app-indexing/deep-linking.html "Google Deep Linking Documentation"
[41]: {% image_buster /assets/img_archive/deep_link_click_action.png %}"ディープリンククリックアクション"
[42]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#what-is-deep-linking
[45]: https://firebase.google.com/docs/cloud-messaging/
[48]: https://developers.google.com/cloud-messaging/android/android-migrate-fcm
[49]: https://firebase.google.com/docs/android/setup
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/standard_integration/#android-push-listener-callback
[55]: {% image_buster /assets/img_archive/android_push_test.png %} "Android プッシュテスト"
[56]: {{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message
[57]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/troubleshooting/
[58]: https://console.firebase.google.com/
[59]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %}"FirebaseServerKey"
[61]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/
[62]: https://developer.android.com/preview/features/notification-channels.html
[63]: {{site.baseurl}}/api/objects_filters/messaging/android_object/
[64]: {{site.baseurl}}/user_guide/message_building_by_channel/push/android/notification_channels/#dashboard-fallback-channel
[65]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/
[66]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/
[67]: https://developer.android.com/reference/android/app/Application.html#onCreate()
[68]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration
[70]: https://github.com/braze-inc/braze-android-sdk/blob/master/samples/firebase-push/src/main/AndroidManifest.xml "AndroidManifest.xml"
[72]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-name.html
[73]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/set-default-notification-channel-description.html
[74]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-firebase-messaging-service/-companion/handle-braze-remote-message.html
[75]: https://firebase.google.com/docs/reference/android/com/google/firebase/messaging/RemoteMessage
[76]: https://developer.android.com/reference/android/app/Application
[77]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.push/-braze-notification-payload/index.html
[78]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-constants/index.html
[79]: {% image_buster /assets/img_archive/cloud_messaging_legacy_disabled.png %}"Firebase レガシー無効"
[80]: {% image_buster /assets/img_archive/cloud_messaging_legacy_enabled.png %} "Firebase サーバーキー"
