## Android SDKを統合する

### ステップ 1: `build.gradle` を更新する

あなたの`build.gradle` 、リポジトリのリストに [`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html)をリポジトリのリストに追加する。

```kotlin
repositories {
  mavenCentral()
}
```

次に、Brazeを依存関係に追加する。

{% tabs local %}
{% tab base only %}
Braze UIコンポーネントを使用する予定がない場合は、以下のコードを`build.gradle` に追加する。`SDK_VERSION` をお使いのAndroid Braze SDKの現在のバージョンに置き換える。全バージョンのリストは[Changelogsを]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android)参照のこと。

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}

{% tab with ui components %}
Braze UIコンポーネントを後で使用する予定がある場合は、次のコードを`build.gradle` に追加する。 `SDK_VERSION` をお使いのAndroid Braze SDKの現在のバージョンに置き換える。全バージョンのリストは[Changelogsを]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android)参照のこと。

```kotlin
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components. 
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endtab %}
{% endtabs %}

### ステップ 2: を設定する。 `braze.xml`

{% alert note %}
2019 年 12 月をもって、カスタムエンドポイントは提供されなくなりました。既存のカスタムエンドポイントがある場合は、それを引き続き使用できます。詳細については、<a href="{{site.baseurl}}/api/basics/#endpoints">利用可能なエンドポイントのリスト</a>を参照してください。
{% endalert %}

プロジェクトの`res/values` フォルダーに`braze.xml` ファイルを作成する。特定のデータクラスターを使用している場合、または既存のカスタムエンドポイントがある場合は、`braze.xml` ファイルでもエンドポイントを指定する必要があります。 

ファイルの内容は、次のコードスニペットのようになります。Braze ダッシュボードの [**設定の管理**] ページにある識別子で `YOUR_APP_IDENTIFIER_API_KEY` を置き換えてください。[dashboard.braze.com](https://dashboard.braze.com)にログインして、[クラスターアドレス]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)を見つけてください。 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### ステップ 3: 権限を追加する `AndroidManifest.xml`

次に、`AndroidManifest.xml` に以下の権限を追加する：

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Android M のリリースにより、Android はインストール時権限モデルから実行時権限モデルに切り替わりました。ただし、これらの権限はどちらも通常の権限であり、アプリのマニフェストにリストされている場合は自動的に付与されます。詳細については、Android の[権限に関するドキュメント](https://developer.android.com/training/permissions/index.html)を参照してください。
{% endalert %}

### ステップ 4: 遅延初期化をイネーブルメントする（オプション）

遅延初期化を使用するには、Braze SDKの最小バージョンが必要である：

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
遅延初期化がイネーブルメントになっている間は、すべてのネットワーク接続がキャンセルされ、SDKがBrazeサーバーにデータを送信できなくなる。
{% endalert %}

#### ステップ4.1：`braze.xml` を更新する

遅延初期化はデフォルトで無効になっている。イネーブルメントを有効にするには、以下のいずれかのオプションを使用する：

{% tabs %}
{% tab Braze XML file %}
プロジェクトの`braze.xml` ファイルで、`com_braze_enable_delayed_initialization` を`true` に設定する。

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab At runtime %}
実行時に遅延初期化をイネーブルメントするには、以下のメソッドを使用する。

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### ステップ4.2：プッシュ分析を設定する（オプション）

遅延初期化をイネーブルメントにすると、プッシュ分析はデフォルトでキューに入れられる。しかし、その代わりにプッシュ分析を[明示的にキューに入れたり](#explicitly-queue-push-analytics)、[ドロップ](#drop-push-analytics)したりすることもできる。

##### 明示的にキューに入れる {#explicitly-queue-push-analytics}

プッシュ分析を明示的にキューに入れるには、以下のオプションのいずれかを選択する：

{% tabs %}
{% tab Braze XML file %}
`braze.xml` ファイルで、`com_braze_delayed_initialization_analytics_behavior` を`QUEUE` に設定する：

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
`QUEUE` を追加する。 [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html)メソッドを追加する：

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.QUEUE)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

##### ドロップ {#drop-push-analytics}

プッシュ分析を中止するには、以下のオプションのいずれかを選択する：

{% tabs %}
{% tab Braze XML file %}
`braze.xml` ファイルで、`com_braze_delayed_initialization_analytics_behavior` を`DROP` に設定する： 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
`DROP` を追加する。 [`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html)メソッドに追加する：

{% subtabs %}
{% subtab JAVA %}

```java
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP);
```

{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
Braze.enableDelayedInitialization(context, DelayedInitializationAnalyticsBehavior.DROP)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### ステップ4.3：SDKを手動で初期化する。

選択した遅延時間が経過したら [`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html)メソッドを使用して、SDKを手動で初期化する。

{% tabs local %}
{% tab JAVA %}

```java
Braze.disableDelayedInitialization(context);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.disableDelayedInitialization(context)
```

{% endtab %}
{% endtabs %}

### ステップ 5: ユーザーセッションのトラッキングをイネーブルにする

ユーザーセッション追跡をイネーブルメントにすると、`openSession()` 、`closeSession()` 、[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)および`InAppMessageManager` 登録の呼び出しを自動的に処理することができる。

アクティビティのライフサイクル・コールバックを登録するには、`Application` クラスの`onCreate()` メソッドに以下のコードを追加する。 

{% tabs local %}
{% tab JAVA %}

```java
public class MyApplication extends Application {
  @Override
  public void onCreate() {
    super.onCreate();
    registerActivityLifecycleCallbacks(new BrazeActivityLifecycleCallbackListener());
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
class MyApplication : Application() {
  override fun onCreate() {
    super.onCreate()
    registerActivityLifecycleCallbacks(BrazeActivityLifecycleCallbackListener())
  }
}
```

使用可能なパラメータのリストについては [`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html).

{% endtab %}
{% endtabs %}

## セッショントラッキングをテストする

{% alert tip %}
[SDKデバッガーを使って]({{site.baseurl}}/developer_guide/debugging)SDKの問題を診断することもできる。
{% endalert %}

テスト中に問題が発生した場合は、[冗長ロギングをイネーブルメントに](#android_enabling-logs)し、logcatを使用してアクティビティ内の`openSession` 、`closeSession` 。

1. Brazeの「**Overview**」でアプリを選択し、**「Display Data For**」のドロップダウンで「**Today**」を選択する。
    ![Brazeの "Overview "ページ。"Display Data For "フィールドが "Today "に設定されている。]({% image_buster /assets/img_archive/android_sessions.png %})
2. アプリを開封し、Brazeダッシュボードを更新する。メトリクスが1増加したことを確認する。
3. アプリをナビゲートし、Brazeにログインしたセッションが1つだけであることを確認する。
4. アプリを少なくとも10秒間バックグラウンドにし、その後フォアグラウンドにする。新しいセッションが記録されたことを確認する。

## オプション構成

### ランタイム構成

Brazeのオプションを`braze.xml` ファイルではなくコードで設定するには、[ランタイム設定を](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)使う。両方の場所に値が存在する場合は、ランタイムの値が代わりに使われる。必要な設定がすべて実行時に提供された後、`braze.xml` ファイルを削除することができる。

以下の例では、[ビルダー・オブジェクトが](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)作成され、次のように渡される。 [`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html).利用可能なランタイムオプションの一部しか表示されていないことに注意してほしい。

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build();
Braze.configure(this, brazeConfig);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
        .setApiKey("api-key-here")
        .setCustomEndpoint("YOUR_CUSTOM_ENDPOINT_OR_CLUSTER")
        .setSessionTimeout(60)
        .setHandlePushDeepLinksAutomatically(true)
        .setGreatNetworkDataFlushInterval(10)
        .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

{% alert tip %}
他の例をお探しだろうか？[Hello Brazeのサンプルアプリを](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java)チェックしよう。
{% endalert %}

### Google 広告 ID

[Google Advertising ID (GAID)](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en)は、Google Play サービスにより提供される、ユーザー固有の、匿名かつ一意の、再設定可能な広告用オプション ID である。GAID によりユーザーは、自分の識別子をリセットし、Google Play アプリ内の興味・関心に基づく広告をオプトアウトできます。また、開発者は、アプリの収益化を継続するためのシンプルな標準システムを入手できます。

Google 広告 ID は Braze SDK によって自動的に収集されないため、[`Braze.setGoogleAdvertisingId()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/set-google-advertising-id.html) メソッドを使用して手動で設定する必要があります。

{% tabs local %}
{% tab JAVA %}

```java
new Thread(new Runnable() {
  @Override
  public void run() {
    try {
      AdvertisingIdClient.Info idInfo = AdvertisingIdClient.getAdvertisingIdInfo(getApplicationContext());
      Braze.getInstance(getApplicationContext()).setGoogleAdvertisingId(idInfo.getId(), idInfo.isLimitAdTrackingEnabled());
    } catch (Exception e) {
      e.printStackTrace();
    }
  }
}).start();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
suspend fun fetchAndSetAdvertisingId(
  context: Context,
  scope: CoroutineScope = GlobalScope
) {
  scope.launch(Dispatchers.IO) {
    try {
      val idInfo = AdvertisingIdClient.getAdvertisingIdInfo(context)
      Braze.getInstance(context).setGoogleAdvertisingId(
        idInfo.id,
        idInfo.isLimitAdTrackingEnabled
      )
    } catch (e: Exception) {
      e.printStackTrace()
    }
  }
}
```

{% endtab %}
{% endtabs %}

{% alert important %}
Google では、非 UI スレッドで広告 ID を収集する必要があります。
{% endalert %}


### 位置情報の追跡

Brazeロケーションコレクションをイネーブルメントにするには、`braze.xml` ファイルで`com_braze_enable_location_collection` を`true` に設定する：

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDK バージョン3.6.0 以降、Braze の位置情報収集機能はデフォルトで無効になっています。
{% endalert %}

### ロギング

デフォルトでは、Braze Android SDK のログレベルは `INFO` に設定されています。[これらのログを抑制](#android_suppressing-logs)したり、[別のログレベルを設定](#android_enabling-logs) (`VERBOSE`、`DEBUG`、または `WARN` など) したりすることができます。

#### ログの有効化 

アプリの問題のトラブルシューティングや、Braze サポートでの所要時間の短縮に役立つように、SDK の詳細ログを有効にします。Brazeサポートに冗長ログを送信する場合は、アプリケーションを起動したらすぐにログを開始し、問題が発生してからずっと後にログを終了するようにする。

詳細なログは開発環境のみを対象としているため、アプリをリリースする前に無効にする必要があります。

{% alert important %}
`Application.onCreate()` で他の呼び出しを行う前に詳細ログを有効にして、ログが可能な限り完全になるようにします。
{% endalert %}

{% tabs local %}
{% tab Application %}
アプリで直接ログを有効にするには、他のメソッドの前に、以下をアプリケーションの `onCreate()` メソッドに追加します。

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.MIN_LOG_LEVEL);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.MIN_LOG_LEVEL
```
{% endsubtab %}
{% endsubtabs %}

`MIN_LOG_LEVEL` を、最小ログレベルとして設定するログレベルの**定数**に置き換えます。設定した`MIN_LOG_LEVEL` のレベル`>=` のログはすべて、Androidのデフォルトの [`Log`](https://developer.android.com/reference/android/util/Log)メソッドに転送される。設定した `MIN_LOG_LEVEL` 未満の (`<`) すべてのログは破棄されます。

| コンスタント    | 値          | 説明                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | デバッグや開発のために最も詳細なメッセージをログに記録する。            |
| `DEBUG`     | 3              | デバッグや開発のために、説明的なメッセージをログに記録する。                  |
| `INFO`      | 4              | 一般的なハイライトのための情報メッセージを記録する。                       |
| `WARN`      | 5              | 潜在的に有害な状況を特定するための警告メッセージをログに記録する。     |
| `ERROR`     | 6              | アプリケーションの失敗や深刻な問題を示すエラーメッセージを記録する。 |
| `ASSERT`    | 7              | 開発中に条件が偽の場合にアサーションメッセージをログに記録する。     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

たとえば、以下のコードはログレベル`2`、`3`、`4`、`5`、`6`、`7`を `Log` メソッドに転送します。

{% subtabs local %}
{% subtab JAVA %}
```java
BrazeLogger.setLogLevel(Log.VERBOSE);
```
{% endsubtab %}

{% subtab KOTLIN %}
```kotlin
BrazeLogger.logLevel = Log.VERBOSE
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab xml %}
`braze.xml` でログを有効にするには、ファイルに以下を追加する：

```xml
<integer name="com_braze_logger_initial_log_level">MIN_LOG_LEVEL</integer>
```

`MIN_LOG_LEVEL` を、最小ログレベルとして設定するログレベルの**値**に置き換えます。設定した`MIN_LOG_LEVEL` のレベル`>=` のログはすべて、Androidのデフォルトの [`Log`](https://developer.android.com/reference/android/util/Log)メソッドに転送される。設定した `MIN_LOG_LEVEL` 未満の (`<`) すべてのログは破棄されます。

| コンスタント    | 値          | 説明                                                               |
|-------------|----------------|---------------------------------------------------------------------------|
| `VERBOSE`   | 2              | デバッグや開発のために最も詳細なメッセージをログに記録する。            |
| `DEBUG`     | 3              | デバッグや開発のために、説明的なメッセージをログに記録する。                  |
| `INFO`      | 4              | 一般的なハイライトのための情報メッセージを記録する。                       |
| `WARN`      | 5              | 潜在的に有害な状況を特定するための警告メッセージをログに記録する。     |
| `ERROR`     | 6              | アプリケーションの失敗や深刻な問題を示すエラーメッセージを記録する。 |
| `ASSERT`    | 7              | 開発中に条件が偽の場合にアサーションメッセージをログに記録する。     |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

たとえば、以下のコードはログレベル`2`、`3`、`4`、`5`、`6`、`7`を `Log` メソッドに転送します。

```xml
<integer name="com_braze_logger_initial_log_level">2</integer>
```
{% endtab %}
{% endtabs %}

#### 冗長ログを検証する

ログが `VERBOSE` に設定されていることを確認するには、`V/Braze` がログのどこかで発生するかどうかを確認します。もしそうなら、冗長ログは正常に有効になっている。以下に例を示します。

```
2077-11-19 16:22:49.591 ? V/Braze v9.0.01 .bo.app.d3: Request started
```

#### ログの抑制

Braze Android SDKのすべてのログを抑制するには、アプリケーションの`onCreate()` メソッドで、他のメソッドの_前に_ログレベルを`BrazeLogger.SUPPRESS` に設定する。

{% tabs local %}
{% tab JAVA %}
```java
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS);
```
{% endtab %}

{% tab KOTLIN %}
```kotlin
BrazeLogger.setLogLevel(BrazeLogger.SUPPRESS)
```
{% endtab %}
{% endtabs %}

### 複数の API キー

複数の API キーの最も一般的なユースケースは、デバッグおよびリリースビルドバリアントの API キーを分離することです。

ビルド内の複数の API キーを簡単に切り替えられるように、関連する[ビルドバリアント](https://developer.android.com/studio/build/build-variants.html)ごとに個別の `braze.xml` ファイルを作成することをお勧めします。ビルドバリアントは、ビルドタイプと製品フレーバーの組み合わせです。デフォルトでは、新しいAndroidプロジェクトは[`debug` と`release` ビルドタイプで](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType)構成され、プロダクトフレーバーはない。

関連するバリアントごとに、`src/<build variant name>/res/values/` ディレクトリに新しい`braze.xml` を作成する。ビルドバリアントがコンパイルされると、新しい API キーが使用されます。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
コード内でAPIキーを設定する方法については、[ランタイム設定を]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)参照のこと。
{% endalert %}

### アプリ内限定メッセージ TalkBack

[Androidアクセシビリティガイドラインに従い](https://developer.android.com/guide/topics/ui/accessibility)、Braze Android SDKはデフォルトでAndroid Talkbackを提供する。アプリ内メッセージの内容だけを、アプリのタイトルバーやナビゲーションなど他の画面要素を含めずに読み上げるようにするには、TalkBackの排他モードを有効にする。

アプリ内メッセージの排他モードをイネーブルメントにする：

{% tabs local %}
{% tab Braze XML %}
```xml
<bool name="com_braze_device_in_app_message_accessibility_exclusive_mode_enabled">true</bool>
```
{% endtab %}

{% tab Kotlin %}
```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true)
Braze.configure(this, brazeConfigBuilder.build())
```
{% endtab %}

{% tab Java %}
```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
brazeConfigBuilder.setIsInAppMessageAccessibilityExclusiveModeEnabled(true);
Braze.configure(this, brazeConfigBuilder.build());
```
{% endtab %}
{% endtabs %}

### R8とプロガード

[コード圧縮](https://developer.android.com/build/shrink-code)設定は、Braze 統合に自動的に含まれます。

Braze コードを難読化するクライアントアプリでは、Braze がスタックトレースを解釈するためのリリースマッピングファイルを保存する必要があります。すべての Braze コードを引き続き保持する場合は、ProGuard ファイルに以下を追加します。

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
