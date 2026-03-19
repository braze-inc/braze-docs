## Android SDKの統合

### ステップ 1: Gradleのビルド設定を更新せよ

プロジェクトのリポジトリ設定（例:`settings.gradle` , `settings.gradle.kts`, または最上位の `build.gradle`）で、リポジトリ一覧に を[`mavenCentral()`](https://docs.gradle.org/current/kotlin-dsl/gradle/org.gradle.api.artifacts.dsl/-repository-handler/maven-central.html)追加する。この構文はGroovyとKotlinのDSLの両方で同じである。

```groovy
repositories {
  mavenCentral()
}
```

次に、依存関係にBrazeを追加する。以下の例では、を現在のAndroid Braze`SDK_VERSION` SDKのバージョンに置き換えること。全バージョンのリストについては、[変更履歴を]({{site.baseurl}}/developer_guide/changelogs/?sdktab=android)参照せよ。

{% alert note %}
- Kotlin DSL (`build.gradle.kts`) では、構文`implementation("...")`を使用する。
- Groovy (`build.gradle`) では、構文`implementation '...'`を使う。
- [バージョンカタログ](https://developer.android.com/build/migrate-to-catalogs)については、ファイル`gradle/libs.versions.toml`にエントリを追加し、生成されたアクセサを使用してそれらを参照する。
{% endalert %}

{% tabs local %}
{% tab base only %}
Braze UI コンポーネントを使用する予定がないなら、依存関係に以下を追加せよ。

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-base:SDK_VERSION' // (Required) Adds dependencies for the base Braze SDK.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-base:SDK_VERSION") // (Required) Adds dependencies for the base Braze SDK.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
君の`gradle/libs.versions.toml`ファイルには：

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-base = { group = "com.braze", name = "android-sdk-base", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

次に、\`.bashrc\` または`build.gradle.kts``.bash_profile`build.gradle`\` ファイルに、以下の依存関係を追加する。この構文はGroovyとKotlinのDSLの両方で同じである。

```groovy
dependencies {
    implementation(libs.braze.android.sdk.base) // (Required) Adds dependencies for the base Braze SDK.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab with ui components %}
Braze UIコンポーネントを使用する予定なら、依存関係に以下を追加せよ。

{% subtabs local %}
{% subtab Groovy %}
```groovy
dependencies {
    implementation 'com.braze:android-sdk-ui:SDK_VERSION' // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation 'com.braze:android-sdk-location:SDK_VERSION' // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Kotlin DSL %}
```kotlin
dependencies {
    implementation("com.braze:android-sdk-ui:SDK_VERSION") // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation("com.braze:android-sdk-location:SDK_VERSION") // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% subtab Version catalog %}
君の`gradle/libs.versions.toml`ファイルには：

```toml
[versions]
braze = "SDK_VERSION"

[libraries]
braze-android-sdk-ui = { group = "com.braze", name = "android-sdk-ui", version.ref = "braze" }
braze-android-sdk-location = { group = "com.braze", name = "android-sdk-location", version.ref = "braze" }
```

次に、\`.bashrc\` または`build.gradle.kts``.bash_profile`build.gradle`\` ファイルに、以下の依存関係を追加する。この構文はGroovyとKotlinのDSLの両方で同じである。

```groovy
dependencies {
    implementation(libs.braze.android.sdk.ui) // (Required) Adds dependencies for the Braze SDK and Braze UI components.
    implementation(libs.braze.android.sdk.location) // (Optional) Adds dependencies for Braze location services.
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ 2:設定する `braze.xml`

{% alert note %}
2019 年 12 月をもって、カスタムエンドポイントは提供されなくなりました。既存のカスタムエンドポイントがある場合は、それを引き続き使用できます。詳細については、<a href="{{site.baseurl}}/api/basics/#endpoints">利用可能なエンドポイントのリスト</a>を参照してください。
{% endalert %}

プロジェクト`res/values`のフォルダ内にファイル`braze.xml`を作成する。特定のデータクラスターを使用している場合、または既存のカスタムエンドポイントがある場合は、`braze.xml` ファイルでもエンドポイントを指定する必要があります。 

ファイルの内容は、次のコードスニペットのようになります。Braze ダッシュボードの [**設定の管理**] ページにある識別子で `YOUR_APP_IDENTIFIER_API_KEY` を置き換えてください。[dashboard.braze.com](https://dashboard.braze.com)にログインして、[クラスターアドレス]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints)を見つけてください。 

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
  <string translatable="false" name="com_braze_api_key">YOUR_APP_IDENTIFIER_API_KEY</string>
  <string translatable="false" name="com_braze_custom_endpoint">YOUR_CUSTOM_ENDPOINT_OR_CLUSTER</string>
</resources>
```

### ステップ 3:権限を追加する `AndroidManifest.xml`

次に、以下の権限をあなたのに追加`AndroidManifest.xml`する：

```xml
<uses-permission android:name="android.permission.INTERNET" />
<uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
```

{% alert note %}
Android M のリリースにより、Android はインストール時権限モデルから実行時権限モデルに切り替わりました。ただし、これらの権限はどちらも通常の権限であり、アプリのマニフェストにリストされている場合は自動的に付与されます。詳細については、Android の[権限に関するドキュメント](https://developer.android.com/training/permissions/index.html)を参照してください。
{% endalert %}

### ステップ 4: 遅延初期化のイネーブルメント（任意）

遅延初期化を使用するには、最低限のBraze SDKバージョンが必要だ。

{% sdk_min_versions android:38.0.0 %}

{% alert note %}
遅延初期化のイネーブルメントが有効な間は、すべてのネットワーク接続がキャンセルされる。これにより、SDKがBrazeサーバーにデータを送信できなくなる。
{% endalert %}

#### ステップ4.1：`braze.xml` を更新する

遅延初期化はデフォルトで無効になっている。イネーブルメントを行うには、次のいずれかの方法を使う：

{% tabs %}
{% tab Braze XML file %}
プロジェクトの`braze.xml`ファイルで、をに`com_braze_enable_delayed_initialization`設定する`true`。

```xml
<bool name="com_braze_enable_delayed_initialization">true</bool>
```
{% endtab %}

{% tab At runtime %}
実行時に遅延初期化のイネーブルメントを行うには、次の方法を使う。

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

{% alert note %}
遅延初期化がイネーブルメントされている場合、プッシュ通知にディープリンクアクションが含まれていても、そのディープリンクは解決されない。
{% endalert %}

#### ステップ4.2：プッシュ分析を設定する（任意）

遅延初期化のイネーブルメントが有効な場合、プッシュ分析はデフォルトでキューに格納される。ただし、代わりにプッシュ分析を[明示的にキューに入れる](#explicitly-queue-push-analytics)か[破棄](#drop-push-analytics)するかを選択できる。

##### 明示的にキューに入れる {#explicitly-queue-push-analytics}

明示的にキューにプッシュ分析を追加するには、次のいずれかのオプションを選択する：

{% tabs %}
{% tab Braze XML file %}
ファイル`braze.xml`内で、を`com_braze_delayed_initialization_analytics_behavior`に設定せよ`QUEUE`：

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">QUEUE</string>
```
{% endtab %}

{% tab At runtime %}
メソッド[`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html)に`QUEUE`追加せよ：

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

##### 落とす {#drop-push-analytics}

プッシュ通知の分析を停止するには、次のいずれかの方法を選ぶ：

{% tabs %}
{% tab Braze XML file %}
ファイル`braze.xml`内で、を`com_braze_delayed_initialization_analytics_behavior`に設定せよ`DROP`： 

```xml
<string name="com_braze_delayed_initialization_analytics_behavior">DROP</string>
```
{% endtab %}

{% tab At runtime %}
メソッド[`Braze.enableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/enable-delayed-initialization.html)に`DROP`追加する：

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

#### ステップ4.3：SDKを手動で初期化する

選択した遅延期間の後、SDKを手動で初期化するためにメソッド[`Braze.disableDelayedInitialization()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-delayed-initialization.html)を使用する。

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

### ステップ 5: ユーザーセッションのトラッキングを有効にする

ユーザーセッショントラッキングをイネーブルすると、\``openSession()```closeSession()`、[`ensureSubscribedToInAppMessageEvents()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.inappmessage/-braze-in-app-message-manager/ensure-subscribed-to-in-app-message-events.html)``、``、および`InAppMessageManager`\`\`の登録呼び出しは自動的に処理される。

アクティビティのライフサイクルコールバックを登録するには、\`Activity`Application``クラスの`onStart()`メソッド`onCreate()`に以下のコードを追加する。 

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

利用可能なパラメータの一覧については、を参照せよ[`BrazeActivityLifecycleCallbackListener`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-activity-lifecycle-callback-listener/index.html)。

{% endtab %}
{% endtabs %}

## セッショントラッキングをテストする

{% alert tip %}
SDKの問題を診断するには[、SDKデバッガー]({{site.baseurl}}/developer_guide/debugging)も利用できる。
{% endalert %}

テスト中に問題が発生した場合は、[詳細ログの](#android_enabling-logs)イネーブルメントを行い、logcatを使用してアクティビティ内で欠落している\`onStart`openSession`()`および`onStop(`closeSession`)\`呼び出しを検出する。

1. Brazeで、**概要**に移動し、アプリを選択する。次に「**データを表示する期間**」のドロップダウンから**「今日」**を選ぶ。
    ![Brazeの「概要」ページで、「表示対象」フィールドが「本日」に設定されている状態。]({% image_buster /assets/img_archive/android_sessions.png %})
2. アプリを開いて、次にBrazeのダッシュボードを更新しろ。指標が1増加したことを確認せよ。
3. アプリを操作し、Brazeに記録されたセッションが1つだけであることを確認する。
4. アプリをバックグラウンドに少なくとも10秒間送ってから、フォアグラウンドに戻す。新しいセッションが記録されたことを確認せよ。

## オプション設定

### ランタイム構成

Brazeのオプションを設定`braze.xml`ファイルではなくコード内で設定するには、[ランタイム構成](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)を使用する。両方の場所に値が存在する場合、代わりに実行時の値が使用される。必要な設定をすべて実行時に指定したら、その`braze.xml`ファイルを削除できる。

次の例では、[ビルダーオブジェクト](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)が作成され、その後.に渡される[`Braze.configure()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/configure.html)。利用可能な実行時オプションの一部のみが表示されていることに注意せよ。完全なリストについては[KDoc](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.configuration/-braze-config/-builder/index.html)を参照せよ。

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
別の例を探しているのか？当社のHello[ Brazeサンプルアプリ](https://github.com/braze-inc/braze-android-sdk/blob/master/samples/hello-braze/src/main/java/com/braze/helloworld/CustomApplication.java)をチェックしてみろ。
{% endalert %}

### Google 広告 ID

[Google広告ID（GAID）](https://support.google.com/googleplay/android-developer/answer/6048248/advertising-id?hl=en)は、Google Playサービスが提供する、広告向けの任意のユーザー固有の匿名で一意かつリセット可能なIDである。GAID によりユーザーは、自分の識別子をリセットし、Google Play アプリ内の興味・関心に基づく広告をオプトアウトできます。また、開発者は、アプリの収益化を継続するためのシンプルな標準システムを入手できます。

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

Brazeの位置情報収集のイネーブルメントを行うには、設定`braze.xml`ファイルで``true`\`を\`\`に`com_braze_enable_location_collection`設定する。

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDK バージョン3.6.0 以降、Braze の位置情報収集機能はデフォルトで無効になっています。
{% endalert %}

### ロギング

デフォルトでは、Braze Android SDK のログレベルは `INFO` に設定されています。[これらのログを抑制](#android_suppressing-logs)したり、[別のログレベルを設定](#android_enabling-logs) (`VERBOSE`、`DEBUG`、または `WARN` など) したりすることができます。

#### ログのイネーブルメント

アプリの問題をトラブルシューティングしたり、Brazeサポートの対応時間を短縮したりするには、SDKの詳細ログをイネーブルメントできる。Brazeサポートに冗長ログを送信する場合は、アプリケーションを起動したらすぐにログを開始し、問題が発生してからずっと後にログを終了するようにする。集中管理された概要については、[詳細ログ記録を]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging)参照せよ。ログ出力の解釈方法の学習については、[「詳細ログの読み方」]({{site.baseurl}}/developer_guide/sdk_integration/reading_verbose_logs)を参照せよ。

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

Braze Android SDKのログを全て抑制するには、アプリケーションの\`setLogLevel`onCreate()`()`メソッドで、他のメソッド_よりも先に_`BrazeLogger.SUPPRESS`ログレベルを\`0\`に設定する。

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

ビルド内の複数の API キーを簡単に切り替えられるように、関連する[ビルドバリアント](https://developer.android.com/studio/build/build-variants.html)ごとに個別の `braze.xml` ファイルを作成することをお勧めします。ビルドバリアントは、ビルドタイプと製品フレーバーの組み合わせです。デフォルトでは、新しいAndroidプロジェクトは  [と`release`  の`debug`ビルドタイプ](https://developer.android.com/reference/tools/gradle-api/8.3/null/com/android/build/api/dsl/BuildType)で構成され、プロダクトフレーバーは設定されていない。

関連する各ビルドバリアントについて、ディレクトリ`src/<build variant name>/res/values/`内に`braze.xml`新しいを作成する。ビルドバリアントがコンパイルされると、新しい API キーが使用されます。

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```

{% alert tip %}
コード内でAPI キーを設定する方法については、[ランタイム設定を]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android)参照せよ。
{% endalert %}

### アプリ内メッセージ「トークバック」

[Androidアクセシビリティガイドライン](https://developer.android.com/guide/topics/ui/accessibility)に準拠し、Braze Android SDKはデフォルトでAndroidのTalkbackを提供する。アプリ内のメッセージの内容のみを読み上げさせ、アプリタイトルバーやナビゲーションなどの他の画面要素を含めないようにするには、TalkBackの排他モードをイネーブルメントできる。

アプリ内メッセージの排他モードをイネーブルメントするには：

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

### R8とProGuard

[コード圧縮](https://developer.android.com/build/shrink-code)設定は、Braze 統合に自動的に含まれます。

Braze コードを難読化するクライアントアプリでは、Braze がスタックトレースを解釈するためのリリースマッピングファイルを保存する必要があります。すべての Braze コードを引き続き保持する場合は、ProGuard ファイルに以下を追加します。

```
-keep class bo.app.** { *; }
-keep class com.braze.** { *; }
```
