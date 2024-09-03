---
nav_title: プライバシー・マニフェスト
article_title: プライバシー・マニフェスト
page_order: 7
platform: Swift
description: "アプリのプライバシーマニフェストでBrazeトラッキングデータを宣言する方法を学ぶ。"
---

# プライバシー・マニフェスト

> あなたのBraze SDKがトラッキングデータを収集する場合、Appleは、トラッキングデータを収集する理由と方法を説明するプライバシーマニフェストを追加することを要求する。

## トラッキングデータとは何か？

アップルは「トラッキングデータ」を、エンドユーザーやデバイスについてあなたのアプリで収集され、第三者のデータ（ターゲット広告など）やデータブローカーにリンクされたデータと定義している。完全な定義と例については、[アップルを参照のこと：トラッキング](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

デフォルトでは、Braze SDKはトラッキングデータを収集しない。ただし、Braze SDKの設定によっては、アプリのプライバシーマニフェストにBraze固有のデータを記載する必要がある場合がある。

## プライバシー・マニフェストとは何か？

プライバシー・マニフェストは、Xcodeプロジェクト内のファイルで、あなたのアプリとサードパーティSDKがデータを収集する理由と、そのデータ収集方法を記述している。データを追跡するサードパーティSDKは、それぞれ独自のプライバシー・マニフェストを必要とする。[アプリのプライバシーレポートを作成](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187)すると、これらのプライバシーマニフェストファイルは自動的に1つのレポートに集約される。

## APIトラッキング・データ・ドメイン

iOS 17.2から、Appleはエンドユーザーが[Ad Tracking Transparency (ATT)プロンプトを](https://support.apple.com/en-us/HT212025)受け入れるまで、あなたのアプリで宣言されたすべてのトラッキングエンドポイントをブロックする。Brazeは、トラッキングデータをルーティングするためのトラッキングエンドポイントを提供し、同時にトラッキング以外のファーストパーティデータを元のエンドポイントにルーティングすることもできる。 

## Brazeのトラッキングデータを宣言する

{% alert tip %}
完全なチュートリアルについては、[プライバシー・トラッキング・データのチュートリアルを](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/)参照のこと。
{% endalert %}

### ステップ1:現在の方針を見直す

貴社のBraze SDKの現在のデータ収集ポリシーを法務チームと検討し、貴社のアプリが[Appleの定義に従って](#what-is-tracking-data)トラッキングデータを収集しているかどうかを判断する。トラッキングデータを収集していない場合は、現時点でBraze SDKのプライバシーマニフェストをカスタマイズする必要はない。Braze SDKのデータ収集ポリシーの詳細については、[SDKデータ収集を]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)参照のこと。

{% alert important %}
Braze以外のSDKがトラッキングデータを収集する場合は、それらのポリシーを別途確認する必要がある。
{% endalert %}

### ステップ2:プライバシー・マニフェストを作成する

まず、Xcodeプロジェクトで`PrivacyInfo.xcprivacy` ファイルを検索して、プライバシー・マニフェストがすでにあるかどうかを確認する。すでにこのファイルを持っている場合は、次のステップに進むことができる。それ以外の場合は、[アップルを参照のこと：プライバシー・マニフェストを作成する](sdk-tracking.iad-01.braze.com).

### ステップ3:エンドポイントをプライバシー・マニフェストに追加する

Xcodeプロジェクトで、アプリの`PrivacyInfo.xcprivacy` ファイルを開き、テーブルを右クリックして**Raw Keys and Valuesを**チェックする。

{% alert note %}

{% endalert %}

![コンテキストメニューを開き、"Raw Keys and Values "をハイライトしたXcodeプロジェクト。]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

**App Privacy Configuration**」で**「NSPrivacyTracking」を**選択し、その値を「**YES**」に設定する。

![PrivacyInfo.xcprivacy' ファイルを "NSPrivacyTracking" を "YES" に設定して開く。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

**App Privacy Configuration**」で**「NSPrivacyTrackingDomains**」を選択する。domains配列に新しい要素を追加し、その値を[、`AppDelegate` の]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate)先頭に`sdk-tracking` を付けて[追加]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate)したエンドポイントに設定する。

![PrivacyInfo.xcprivacy' ファイルは、"NSPrivacyTrackingDomains" の下に記載されているBrazeトラッキングエンドポイントで開く。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### ステップ4: トラッキング・データを宣言する

次に、`AppDelegate.swift` を開き、静的または動的トラッキング・リストを作成することによって、宣言したい[各トラッキング・プロパティを](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/)リストアップする。アップルは、エンドユーザーがATTプロンプトを受け入れるまで、これらのプロパティをブロックすることに留意してほしい。以下はその例です。

{% tabs %}
{% tab 静的な例 %}
以下の例では、`dateOfBirth` 、`customEvent` 、`customAttribute` がスタティック・リスト内のトラッキング・データとして宣言されている。 

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
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
}
```
{% endtab %}

{% tab ダイナミックな例 %}
以下の例では、エンドユーザーがATTプロンプトを受け入れた後、トラッキングリストは自動的に更新される。

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### ステップ5:無限リトライ・ループを防ぐ

SDKが無限再試行ループに入るのを防ぐため、`set(adTrackingEnabled: enableAdTracking)` メソッドを使用してATTパーミッションを処理する。メソッド内の`adTrackingEnabled` プロパティは、以下のように処理する：

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
