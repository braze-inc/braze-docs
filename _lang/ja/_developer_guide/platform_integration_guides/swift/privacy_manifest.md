---
nav_title: プライバシーマニフェスト
article_title: プライバシーマニフェスト
page_order: 7
platform: Swift
description: "アプリのプライバシーマニフェストでBrazeトラッキングデータを宣言する方法を学びます。"
---

# プライバシーマニフェスト

> Braze SDKがトラッキングデータを収集する場合、Appleはトラッキングデータを収集する理由と方法を説明するプライバシーマニフェストを追加することを要求します。

## トラッキングデータとは

Appleは、「トラッキングデータ」を、サードパーティのデータ(ターゲット広告など)にリンクされているエンドユーザーまたはデバイス、またはデータブローカーについてアプリで収集されるデータと定義しています。例を含む完全な定義については、Appleを参照してください [。追跡

デフォルトでは、Braze SDK はトラッキングデータを収集しません。ただし、Braze SDKの設定によっては、アプリのプライバシーマニフェストにBraze固有のデータを記載する必要がある場合があります。

## プライバシーマニフェストとは?

プライバシーマニフェストは、アプリとサードパーティの SDK がデータを収集する理由と、データ収集方法を記述した Xcode プロジェクト内のファイルです。データを追跡するサードパーティの SDK には、それぞれ独自のプライバシー マニフェストが必要です。[アプリのプライバシー レポートを作成する](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187)と、これらのプライバシー マニフェスト ファイルが自動的に 1 つのレポートに集約されます。

## API トラッキング・データ・ドメイン

iOS 17.2 以降、Apple は、エンドユーザーが [広告トラッキング透過性(ATT)プロンプト](https://support.apple.com/en-us/HT212025)を受け入れるまで、アプリで宣言されたすべてのトラッキング エンドポイントをブロックします。Brazeは、このデータを専用の `-tracking` エンドポイントに自動的に再ルーティングし、残りの非トラッキングのファーストパーティデータを元のエンドポイントに送信します。以下に例を示します。

- **元のエンドポイント:** `sdk.iad-01.braze.com`
- **追跡エンドポイント:** `sdk-tracking.iad-01.braze.com`

## Brazeトラッキングデータの宣言

{% alert tip %}
完全なチュートリアルについては、 [プライバシー追跡データのチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/)を参照してください。
{% endalert %}

### ステップ 1:現在のポリシーを確認する

Braze SDKの現在のデータ収集ポリシーを法務チームと確認し、アプリが [Appleの定義に従って](#what-is-tracking-data)トラッキングデータを収集しているかどうかを判断します。トラッキングデータを収集していない場合は、現時点ではBraze SDKのプライバシーマニフェストをカスタマイズする必要はありません。

Braze SDKのデータ収集ポリシーの詳細については、「 [SDKデータ収集]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)」を参照してください。

{% alert important %}
Braze SDK以外のSDKのいずれかがトラッキングデータを収集する場合は、それらのポリシーを個別に確認する必要があります。
{% endalert %}

### ステップ 2: トラッキングデータを申告する

Xcode プロジェクトで、静的または動的な追跡リストを作成して、宣言する各[追跡プロパティ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/)を開き`AppDelegate.swift`、一覧表示します。Appleは、エンドユーザーがATTプロンプトを受け入れるまでこれらのプロパティをブロックするため、あなたとあなたの法務チームが追跡を検討しているプロパティのみをリストアップすることに注意してください。

{% tabs %}
{% tab static example %}
次の例では、`dateOfBirth`、 `customEvent``customAttribute` 

\`\`\`swift
import UIKit
import BrazeKit

@main
class AppDelegate:UIResponder, UIApplicationDelegate {

  static var braze:Braze? = nil

  func application(
    _ application:UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey:Any]?
  ) -> Bool {
let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
// Declare which types of data you wish to collect for user tracking.
configuration.api.trackingPropertyAllowList = [
.dateOfBirth,
.customEvent(["event-1"]),
.customAttribute(["attribute-1", "attribute-2"])
]
let braze = Braze(configuration: configuration)
AppDelegate.braze = braze
return true
}
    ()
    \`\`\`
    {% endtab %}

{% tab dynamic example %}
次の例では、エンドユーザーがATTプロンプトを受け入れると、追跡リストが自動的に更新されます。

\`\`\`swift
func applicationDidBecomeActive(_ application:UIApplication,
  // Request and check your user's tracking authorization status.
ATTrackingManager.requestTrackingAuthorization { status in
// Let Braze know whether user data is allowed to be collected for tracking.
  let enableAdTracking = status == .authorized
    AppDelegate.braze?です。set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  ()
}
\`\`\`
{% endtab %}
{% endtabs %}

### ステップ 3: 無限の再試行ループを防ぐ

SDK が無限の再試行ループに入らないようにするには、メソッドを使用して `set(adTrackingEnabled: enableAdTracking)` ATT アクセス許可を処理します。メソッドのプロパティは `adTrackingEnabled` 、次のように処理する必要があります。

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```
