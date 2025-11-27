## アップルのプライバシー・マニフェスト {#privacy-manifest}

### トラッキングデータとは何か？

アップルは「トラッキングデータ」を、エンドユーザーやデバイスについてあなたのアプリで収集され、第三者のデータ（ターゲット広告など）やデータブローカーにリンクされたデータと定義している。完全な定義と例については、[アップルを参照のこと：トラッキング](https://developer.apple.com/app-store/app-privacy-details/#user-tracking)を参照してください。

デフォルトでは、Braze SDKはトラッキングデータを収集しない。ただし、Braze SDKの設定によっては、アプリのプライバシーマニフェストにBraze固有のデータを記載する必要がある場合がある。

### プライバシー・マニフェストとは何か？

プライバシーマニフェストは、アプリとサードパーティの SDK がデータを収集する理由と、そのデータ収集方法を説明する Xcode プロジェクト内のファイルです。データを追跡するサードパーティの SDK には、それぞれ独自のプライバシーマニフェストが必要です。[アプリのプライバシーレポートを作成](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187)すると、これらのプライバシーマニフェストファイルは自動的に1つのレポートに集約される。

### APIトラッキング・データ・ドメイン

iOS 17.2 以降、Apple はエンドユーザーが [Ad Tracking Transparency (ATT) のプロンプト](https://support.apple.com/en-us/HT212025)を受け入れるまで、宣言されたすべてのトラッキングエンドポイントをブロックします。Brazeは、トラッキングデータをルーティングするためのトラッキングエンドポイントを提供し、同時にトラッキング以外のファーストパーティデータを元のエンドポイントにルーティングすることもできる。 

## Brazeのトラッキングデータを宣言する

{% alert tip %}
詳細な説明については、[プライバシートラッキングデータのチュートリアル](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/)を参照してください。
{% endalert %}

### 前提条件

この機能を実装するには、以下のBraze SDKバージョンが必要である：

{% sdk_min_versions swift:9.0.0 %}

### ステップ1:現在の方針を見直す

貴社のBraze SDKの現在のデータ収集ポリシーを法務チームと検討し、貴社のアプリが[Appleの定義に従って](#what-is-tracking-data)トラッキングデータを収集しているかどうかを判断する。トラッキングデータを収集していない場合は、現時点でBraze SDKのプライバシーマニフェストをカスタマイズする必要はない。Braze SDK のデータ収集ポリシーの詳細については、[SDK データ収集]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/)を参照してください。

{% alert important %}
Braze以外のSDKがトラッキングデータを収集する場合は、それらのポリシーを別途確認する必要がある。
{% endalert %}

### ステップ2:プライバシー・マニフェストを作成する

まず、Xcodeプロジェクトで`PrivacyInfo.xcprivacy` ファイルを検索して、プライバシー・マニフェストがすでにあるかどうかを確認する。すでにこのファイルを持っている場合は、次のステップに進むことができる。それ以外の場合は、[Apple:プライバシー・マニフェストを作成する](sdk-tracking.iad-01.braze.com).

### ステップ3:エンドポイントをプライバシー・マニフェストに追加する

Xcode プロジェクトでアプリの `PrivacyInfo.xcprivacy` ファイルを開き、表を右クリックして、**Raw Keys and Values** を確認します。

{% alert note %}

{% endalert %}

![コンテキストメニューが開き、「Raw Keys and Values」が強調表示された Xcode プロジェクト。]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})()

[**App Privacy Configuration**] で [**NSPrivacyTracking**] を選択し、値を [**YES**] に設定します。

![[NSPrivacyTracking] が [YES] に設定されて開かれている「PrivacyInfo.xcprivacy」ファイル。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})()

**App Privacy Configuration**」で**「NSPrivacyTrackingDomains**」を選択する。ドメイン配列で新しい要素を追加し、その値を、`sdk-tracking` 接頭辞を付けて [`AppDelegate` に以前に追加した]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate)エンドポイントに設定します。

![「NSPrivacyTrackingDomains」の下に Braze トラッキングエンドポイントがリストされて開かれている「PrivacyInfo.xcprivacy」ファイル。]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})()

### ステップ 4: トラッキングデータを宣言する

次に `AppDelegate.swift` を開き、静的または動的トラッキングリストを作成して、宣言する各[トラッキングプロパティ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/)をリストします。Apple は、エンドユーザーが ATT プロンプトを受け入れるまでこれらのプロパティをブロックするため、あなたとあなたの法務チームがトラッキングを検討するプロパティのみをリストします。以下に例を示します。

{% tabs %}
{% tab static example %}
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

{% tab dynamic example %}
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

## トラッキングを無効にする

Swift SDKのデータ追跡アクティビティを無効にするには、Brazeインスタンスの [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled)プロパティを`false` 。`enabled` が `false` に設定されると、Braze SDK でパブリック API への呼び出しがすべて無視されます。SDKはまた、ネットワークリクエストやイベント処理など、飛行中のすべてのアクションをキャンセルする。 

## 過去に保存したデータを消去する

この [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata())メソッドを使用すると、ユーザーのデバイスにローカルに保存されたSDKデータを完全に消去できる。

Braze Swiftのバージョン7.0.0以降では、SDKと`wipeData()` メソッドが、デバイスIDのUUIDをランダムに生成する。しかし、あなたの`useUUIDAsDeviceId` が`false` に設定されて_いるか、_Swift SDK バージョン 5.7.0 以前を使用している場合、あなたはまた、ポストリクエストを行う必要がある。 [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)ベンダーの識別子(IDFV)が自動的にユーザーのデバイスIDとして使用されるからだ。

## データトラッキングを再開する

データ収集を再開するには、[`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) を `true` に設定します。これは、以前に消去したデータを復元するものではないことに留意してほしい。

## IDFVコレクション

Braze iOS SDK の以前のバージョンでは、IDFV (ベンダーの識別子) フィールドがユーザーのデバイス ID として自動的に収集されていました。Swift SDK`v5.7.0` 以降、IDFVフィールドはオプションで無効になり、代わりにBrazeはランダムなUUIDをデバイスIDとして設定するようになった。Swift SDK`v7.0.0` 以降、IDFV フィールドはデフォルトでは収集されず、代わりに UUID がデバイス ID として設定される。

`useUUIDAsDeviceId` 機能により、デバイス ID を UUID として設定するよう [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) が構成されます。従来、iOS SDK では Apple が生成した IDFV 値と同じデバイス ID が割り当てられていました。iOS アプリでこの機能がデフォルトで有効になっている場合、SDK を介して作成されたすべての新規ユーザーに、UUID と同じデバイス ID が割り当てられます。

それでもIDFVを別に集めたい場合は、次のようにすることができる。 [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

### 考慮事項

#### SDK バージョン

Swift SDK`v7.0.0+` において、`useUUIDAsDeviceId` がイネーブルメント（デフォルト）である場合、新規作成されたすべてのユーザーにはランダムなデバイス ID が割り当てられる。既存のユーザーは、すべて同じデバイス ID 値を保持します。これは、IDFV である場合もあります。

この機能が有効でない場合、デバイスには引き続き作成時に IDFV が割り当てられます。

#### ダウンストリーム 

**テクノロジーパートナー**: この機能を有効にすると、Braze デバイス ID から IDFV 値を取得するテクノロジーパートナーは、このデータにアクセスできなくなります。パートナー連携にデバイスから得られるIDFV値が必要な場合は、この機能を`false` に設定することを推奨する。

**Currents**: `useUUIDAsDeviceId` が true に設定されている場合、Currents で送信されたデバイス ID は IDFV 値と等しくなくなります。

### よくある質問

#### この変更は Braze の既存ユーザーに影響しますか?

いいえ。この機能を有効にしても、Braze のユーザーデータは上書きされません。新しいUUIDデバイスIDは、新しいデバイス、または`wipedata()` 。

#### この機能をオンにした後にオフにすることはできますか?

はい、この機能はオンとオフを自由に切り替えることができます。以前に保存されたデバイス ID は上書きされません。

#### Braze を介し、IDFV 値を別の場所で収集することはできますか?

はい、オプションで Swift SDK を使用して IDFV を収集することもできます (収集はデフォルトでは無効です)。 
