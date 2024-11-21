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

アップルは「トラッキングデータ」を、エンドユーザーやデバイスについてあなたのアプリで収集され、第三者のデータ（ターゲット広告など）やデータブローカーにリンクされたデータと定義している。完全な定義と例については、[アップルを参照のこと：トラッキング](https://developer.apple.com/app-store/app-privacy-details/#user-tracking)を参照してください。

デフォルトでは、Braze SDKはトラッキングデータを収集しない。ただし、Braze SDKの設定によっては、アプリのプライバシーマニフェストにBraze固有のデータを記載する必要がある場合がある。

## プライバシー・マニフェストとは何か？

プライバシーマニフェストは、アプリとサードパーティの SDK がデータを収集する理由と、そのデータ収集方法を説明する Xcode プロジェクト内のファイルです。データを追跡するサードパーティの SDK には、それぞれ独自のプライバシーマニフェストが必要です。[アプリのプライバシーレポートを作成](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187)すると、これらのプライバシーマニフェストファイルは自動的に1つのレポートに集約される。

## APIトラッキング・データ・ドメイン

iOS 17.2 以降、Apple はエンドユーザーが [Ad Tracking Transparency (ATT) のプロンプト](https://support.apple.com/en-us/HT212025)を受け入れるまで、宣言されたすべてのトラッキングエンドポイントをブロックします。Brazeは、トラッキングデータをルーティングするためのトラッキングエンドポイントを提供し、同時にトラッキング以外のファーストパーティデータを元のエンドポイントにルーティングすることもできる。 

## Brazeのトラッキングデータを宣言する

{% alert tip %}
詳細な説明については、[プライバシートラッキングデータのチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/)を参照してください。
{% endalert %}

### ステップ1:現在の方針を見直す

貴社のBraze SDKの現在のデータ収集ポリシーを法務チームと検討し、貴社のアプリが[Appleの定義に従って](#what-is-tracking-data)トラッキングデータを収集しているかどうかを判断する。トラッキングデータを収集していない場合は、現時点でBraze SDKのプライバシーマニフェストをカスタマイズする必要はない。Braze SDK のデータ収集ポリシーの詳細については、[SDK データ収集]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)を参照してください。

{% alert important %}
Braze以外のSDKがトラッキングデータを収集する場合は、それらのポリシーを別途確認する必要がある。
{% endalert %}

### ステップ2:プライバシー・マニフェストを作成する

まず、Xcodeプロジェクトで`PrivacyInfo.xcprivacy` ファイルを検索して、プライバシー・マニフェストがすでにあるかどうかを確認する。すでにこのファイルを持っている場合は、次のステップに進むことができる。それ以外の場合は、[Apple:プライバシー・マニフェストを作成する](sdk-tracking.iad-01.braze.com).

### ステップ3:エンドポイントをプライバシー・マニフェストに追加する

Xcode プロジェクトでアプリの `PrivacyInfo.xcprivacy` ファイルを開き、表を右クリックして、**Raw Keys and Values** を確認します。

{% alert note %}

{% endalert %}

![コンテキストメニューが開き、「Raw Keys and Values」が強調表示された Xcode プロジェクト。]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

[**App Privacy Configuration**] で [**NSPrivacyTracking**] を選択し、値を [**YES**] に設定します。

![[NSPrivacyTracking] が [YES] に設定されて開かれている「PrivacyInfo.xcprivacy」ファイル。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

**App Privacy Configuration**」で**「NSPrivacyTrackingDomains**」を選択する。ドメイン配列で新しい要素を追加し、その値を、`sdk-tracking` 接頭辞を付けて [`AppDelegate` に以前に追加した]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate)エンドポイントに設定します。

![「NSPrivacyTrackingDomains」の下に Braze トラッキングエンドポイントがリストされて開かれている「PrivacyInfo.xcprivacy」ファイル。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### ステップ4: トラッキングデータを宣言する

次に `AppDelegate.swift` を開き、静的または動的トラッキングリストを作成して、宣言する各[トラッキングプロパティ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/)をリストします。Apple は、エンドユーザーが ATT プロンプトを受け入れるまでこれらのプロパティをブロックするため、あなたとあなたの法務チームがトラッキングを検討するプロパティのみをリストします。以下はその例です。

{% tabs %}
{% tab 静的な例 %}
以下の例では、`dateOfBirth`、`customEvent`、および `customAttribute` が静的リスト内でトラッキングデータとして宣言されています。 

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

SDKが無限再試行ループに入るのを防ぐため、`set(adTrackingEnabled: enableAdTracking)` メソッドを使用してATTパーミッションを処理する。メソッド内の `adTrackingEnabled` プロパティは、以下のように処理する必要があります。

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
