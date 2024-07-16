---
nav_title: Airbridge
article_title:Airbridge
alias: /partners/airbridge/
description:
page_type: partner
search_tag:Partner

---

# Airbridge

> [Airbridgeは](https://www.airbridge.io/)、モバイルアトリビューション、インクリメンタリスト測定、マーケティングミックスモデリングを通じて、真の成長源を発見できる統合モバイル測定プラットフォームである。

BrazeとAirbridgeの統合により、オーガニック以外のインストールアトリビューションデータをAirbridgeからBrazeに渡し、パーソナライズされたマーケティングキャンペーンを構築することができる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Airbridgeアカウント | このパートナーシップを利用するには、Airbridgeアカウントが必要である。 |
| iOSまたはAndroidアプリ | この統合はiOSとAndroidアプリをサポートしている。プラットフォームによっては、アプリケーションにコード・スニペットが必要な場合がある。 |
| エアブリッジSDK | 必要なBraze SDKに加えて、Airbridge[Android](https://help.airbridge.io/en/developers/android-sdk)または[iOS](https://help.airbridge.io/en/developers/ios-sdk)SDKをインストールする必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:マップ・デバイスID

サーバー間の統合は、以下のコード・スニペットをアプリに含めることでイネーブルメントにすることができる。

#### Android

Androidアプリをお持ちの場合は、固有のBrazeデバイスIDをAirbridgeに渡す必要がある。

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

iOSアプリの場合、useUUIDAsDeviceIdフィールドをfalseに設定することで、IDFVを収集することができる。設定されていない場合、iOSのアトリビューションはAirbridgeからBrazeに正確にマッピングされない可能性が高い。詳しくは「IDFVの収集」を参照のこと。

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

### ステップ2:Brazeデータインポートキーを取得する。

Brazeで、**Partner Integrations**>**Technology Partnersに**移動し、**Airbridgeを**選択する。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合**」の下に**テクノロジーパートナーが**ある。
{% endalert %}

ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。鍵の生成後、新しい鍵を作成したり、既存の鍵を無効にしたりすることができる。データインポートキーとRESTエンドポイントは、Airbridgeのダッシュボードでポストバックを設定する際に、次のステップで使用される。

![][1]

### ステップ3:AirbridgeのダッシュボードでBrazeを設定する。

1. Airbridgeで、左サイドバーの**Integrations > Third-party Integrationsに**移動し、**Brazeを**選択する。
2. Brazeのダッシュボードで見つけたデータインポートキーとRESTエンドポイントを入力する。
3. イベントの種類（Install EventまたはInstall & Deeplink Open Event）を選択し、保存する。

{% alert note %}
ディープリンク開封イベントにつながったキャンペーンのアトリビューションデータは、デバイスレベルで更新される。例えば、2人のユーザーが1台のデバイスを使用し、1人のユーザーがディープリンク開封イベントを行った場合、このイベントのアトリビューションデータはもう1人のユーザーのデータにも反映される。
{% endalert %}

より詳細な手順については、[Airbridgeを](https://help.airbridge.io/en/guides/braze)参照のこと。

### ステップ 4:統合を確認する

BrazeがAirbridgeからアトリビューションデータを受信すると、BrazeのAirbridgeテクノロジーパートナーページのステータス接続インジケータが「未接続」から「接続済み」に変わる。最後に成功したリクエストのタイムスタンプも含まれる。

これは、インストールアトリビューションに関するデータを受け取るまでは起こらないことに注意してほしい。Airbridgeのポストバックから除外されるべきオーガニックインストールは、APIによって無視され、接続が成功したかどうかを判断する際にカウントされない。

## 利用可能なデータフィールド

Airbridgeは、以下のデータフィールド表に記載されている4種類のアトリビューションデータをBrazeに送信することができる。このデータはAirbridgeのダッシュボードで見ることができ、ユーザーのインストールアトリビューションとフィルターに使用される。

提案されたとおりに統合を設定すると、Brazeはインストールデータをセグメンテーションフィルターにマッピングする。

| Airbridgeデータフィールド | セグメンテーションフィルター | 説明 |
| -------------------- | ---------------------| ---- |
| `Channel` | インストールアトリビューションソース | インストールまたはディープリンク開封の属性は、チャネルである。 |
| `Campaign` | インストールアトリビューションキャンペーン | インストールまたはディープリンク開封の属性は以下のキャンペーンである。 |
| `Ad Group` | アトリビューション広告グループをインストールする | インストールまたはディープリンクの開封がアトリビューションされた広告グループ |
| `Ad Creative` | インストールアトリビューション広告 | インストールまたはディープリンク開封の広告クリエイティブは、以下の属性に帰属する。 |

Brazeダッシュボードのインストールアトリビューションフィルターを使って、ユーザー群をアトリビューションデータでセグメンテーションすることができる。

![][2]

## メタビジネス属性データ

Meta Businessキャンペーンのアトリビューションデータは、パートナーを通じて入手することはできない。このメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーはそのデータをBrazeに送信することができない。

## BrazeのAirbridgeクリックトラッキングURL（オプション）

Brazeキャンペーンでクリックトラッキングリンクを使用すると、どのキャンペーンがアプリのインストールやリエンゲージメントを促進しているかを簡単に確認できる。その結果、マーケティング活動をより効果的に測定できるようになり、ROIを最大化するためにどこにリソースを投資すべきか、データドリブン型の意思決定ができるようになる。

Airbridgeのクリック追跡リンクを利用するには、[Airbridgeを](https://help.airbridge.io/en/guides/creating-a-new-tracking-link)ご覧いただきたい。設定完了後、Airbridgeクリック追跡リンクをキャンペーンに直接挿入することができる。Airbridgeは、[確率的アトリビューション手法を](https://help.airbridge.io/en/guides/identity-matching)使用して、リンクをクリックしたユーザーの属性を決定する。これにより、リンクをクリックしたユーザーの属性が決定的になる。

{% tabs %}
{% tab Android %}
Androidの場合、Brazeは顧客が[Google Advertising ID収集（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)）にオプトインできるようにしている。GAIDは、Airbridge SDKとの統合によってネイティブに収集される。以下のLiquidロジックを利用することで、Airbridgeクリック追跡リンクにGAIDを含めることができる：
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAirbridgeの両方が、SDK統合を通じてネイティブにIDFVを自動的に収集する。これはデバイス識別子として使用できる。以下のLiquidロジックを利用することで、Airbridgeクリック追跡リンクにIDFVを含めることができる：

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
**この推奨は純粋にオプションである。**<br>
現在、クリック追跡リンクに IDFV や GAID などのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Airbridge は確率的モデリングによってこれらのクリックを属性化することができます。
{% endalert %}

[1]: {% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %}
[2]: {% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %}
