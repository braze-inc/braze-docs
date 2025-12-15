---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "このリファレンス記事では、Braze と Airbridge のパートナーシップについて説明します。Airbridge は、デバイス、ID、プラットフォームにわたり真のマーケティング効果を測定するためのピープルベースドアトリビューションとインクリメンタル測定を提供します。"
page_type: partner
search_tag: Partner

---

# Airbridge

> [Airbridge](https://www.airbridge.io/)は、モバイルアトリビューション、インクリメンタル計測、マーケティングミックスモデリングによる生育源を発見するための統一されたモバイル計測プラットフォームです。

_この統合は Airbridge によって管理されます。_

## 統合について

BrazeとAirbridgeの統合により、パーソナライズされたマーケティングキャンペーンを構築するために、AirbridgeからBrazeにオーガニックインストール以外のアトリビューションデータを渡すことができる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Airbridge アカウント | このパートナーシップを活用するには、Airbridge アカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合では、iOS アプリと Android アプリがサポートされています。プラットフォームによっては、アプリケーションにコード・スニペットが必要になるかもしれない。 |
| Airbridge SDK | 必要なBraze SDKに加えて、Airbridge[Android](https://help.airbridge.io/en/developers/android-sdk)または[iOS](https://help.airbridge.io/en/developers/ios-sdk)SDKをインストールする必要がある。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:デバイス ID をマッピングする

サーバー間統合を有効にするには、アプリに次のコードスニペットを組み込みます。

#### Android

Androidアプリをお持ちの場合は、一意のBrazeデバイスIDをAirbridgeに渡す必要がある。

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
// MainApplciation.java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize Airbridge SDK
    AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build();
    Airbridge.init(this, config);
    
    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
    // Explicitly start tracking
    Airbridge.startTracking();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// MainApplication.kt
override fun onCreate() {
    super.onCreate()
    // Initialize Airbridge SDK
    val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build()
    Airbridge.init(this, config)

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
    // Explicitly start tracking
    Airbridge.startTracking()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### iOS

iOSアプリの場合、useUUIDAsDeviceIdフィールドをfalseに設定することで、IDFVを収集することができる。設定されていない場合、iOSのアトリビューションはAirbridgeからBrazeに正確にマッピングされない可能性が高い。詳細については、「IDFV の収集」を参照してください。

{% tabs %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

```swift
// AppDelegate.swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
    AirBridge.setAutoStartTrackingEnabled(false)
    AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

    AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
    AirBridge.startTracking()
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// AppDelegate.m
-           (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  AirBridge.autoStartTrackingEnabled = NO;
  [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
    [AirBridge startTracking];
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### React Native

{% tabs %}
{% tab TypeScript %}

```typescript
Braze.getInstallTrackingId(function (error, brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
    Airbirdge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Cordova

{% tabs %}
{% tab TypeScript %}

```typescript
AppboyPlugin.getDeviceId(function (brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Flutter

{% tabs %}
{% tab TypeScript %}

```typescript
BrazePlugin.getInstallTrackingId().then((brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Unity

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### ステップ2:Brazeデータインポートキーを取得する

Brazeで [**パートナー連携**] >[**テクノロジーパートナー**] に移動し、[**Airbridge**] を選択します。

ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。Airbridge のダッシュボードでポストバックを設定する場合、次のステップでデータインポートキーと REST エンドポイントが使用されます。

![]({% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %})

### ステップ 3:Airbridge のダッシュボードで Braze を設定する

1. Airbridgeで、左サイドバーの **[Integrations] > [Third-party Integrations]** に移動し、[**Braze**] を選択します。
2. Braze ダッシュボードで見つけたデータインポートキーと RESTエンドポイントを入力します。
3. イベントタイプ(Install Event またはInstall & Deeplink Open Event)を選択し、保存します。

{% alert note %}
ディープリンクオープンイベントにつながったキャンペーンのアトリビューションデータは、デバイスレベルで更新される。例えば、2人のユーザーが1つのデバイスを使用し、1人のユーザーがディープリンクを開くイベントを行った場合、このイベントのアトリビューションデータはもう1人のユーザーのデータにも反映される。
{% endalert %}

詳細な手順については、[Airbridge](https://help.airbridge.io/en/guides/braze)を参照してください。

### ステップ4:統合を確認する

Braze が Airbridge からアトリビューションデータを受信すると、Braze の Airbridge テクノロジーパートナーページのステータス接続インジケーターが [接続されていません] から [接続済み] に変わります。最後に成功したリクエストのタイムスタンプも含まれる。

これは、紐づけられるインストールに関するデータを受け取るまでは発生しないことに注意してください。Airbridge のポストバックから除外する必要があるオーガニックインストールは、Braze の API では無視され、接続の確立が成功したかどうかを判断する際に考慮されません。

## 利用可能なデータフィールド

Airbridge は、次のデータフィールドチャートにリストされている4種類のアトリビューションデータを Braze に送信できます。このデータは Airbridge ダッシュボードで確認でき、ユーザーのインストールアトリビューションおよびフィルタリングに使用されます。

提案されたとおりに統合を設定すると、Brazeはインストールデータをセグメントフィルターにマッピングする。

| Airbridge のデータフィールド | Braze セグメントフィルター | 説明 |
| -------------------- | ---------------------| ---- |
| `Channel` | 帰属ソースをインストールする | インストールまたはディープリンクオープンが紐づけられるチャネル |
| `Campaign` | アトリビューション・キャンペーンをインストールする | インストールまたはディープリンクのオープンが帰属するキャンペーン |
| `Ad Group` | アトリビューション広告グループをインストールする | インストールまたはディープリンクのオープンが帰属する広告グループ |
| `Ad Creative` | アトリビューション広告をインストールする | インストールまたはディープリンクが開かれた広告クリエイティブは、以下のものに起因する。 |

ユーザー群は、Braze ダッシュボードで インストールアトリビューションのフィルターを使用して、アトリビューションデータによってセグメント化できます。

![]({% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %})

## Meta Business アトリビューションデータ

Meta Businessキャンペーンのアトリビューションデータは、当社のパートナーから入手することはできません。このメディアソースは、パートナーにアトリビューションデータを第三者と共有することを許可していないため、パートナーはそのデータを Braze に送信できません。

## Braze での Airbridge クリックトラッキング URL (オプション)

Braze キャンペーン s でクリック"トラッキングを使用すると、どのキャンペーンがアプリをインストールして再エンゲージメントするかが表示されます。この結果を用いてマーケティング パフォーマンスを測定し、より強力なROIのためにどこに資源を投入するかを決定する。

Airbridge のクリックトラッキングリンクの使用を開始するには、[Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link) にアクセスします。セットアップが完了したら、エアブリッジのクリックトラッキングリンクをBrazeのキャンペーンに直接挿入することができる。その後、Airbridge は[確率的アトリビューション手法](https://help.airbridge.io/en/guides/identity-matching)を使用して、リンクをクリックしたユーザーを紐づけます。Brazeキャンペーンからのアトリビューションの精度を高めるために、Airbridgeトラッキングリンクにデバイス識別子を付加することをお勧めする。これにより、リンクをクリックしたユーザーを決定論的に属性付けします。

{% tabs %}
{% tab Android %}
Androidの場合、Brazeを使用すると、顧客は[Google広告IDコレクション（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)にオプトインできます。GAID はまた、Airbridge SDK統合によってネイティブに収集されます。以下のリキッドロジックを利用することで、エアブリッジのクリックトラッキングリンクにGAIDを含めることができる：
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAirbridgeの両方が、SDKの統合を通じてネイティブにIDFVを自動的に収集する。これはデバイス識別子として使用できる。以下のリキッドロジックを利用することで、エアブリッジのクリックトラッキングリンクにIDFVを含めることができる：

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**この推奨事項の適用は完全に任意です。**<br>
現在、クリックトラッキングリンクで IDFV やGAID などのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Airbridge は確率的モデリングによってこれらのクリックを紐づけることができます。
{% endalert %}


