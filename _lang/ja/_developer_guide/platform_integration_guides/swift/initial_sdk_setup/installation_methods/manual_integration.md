---
nav_title: 手動統合
article_title: iOS の手動統合
platform: Swift
page_order: 3
description: "このリファレンス記事では、手動インストールを使用してBraze Swift SDK を統合する方法を示します。"
toc_headers: "h2"
---

# 手動統合

> パッケージマネージャへのアクセス権がない場合([Swift Package Manager]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) や[CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/) など)、代わりにSwift SDK を手動で統合できます。

## ステップ 1:Braze SDK をダウンロードする

GitHub の[Braze SDK リリースページに移動し、`braze-swift-sdk-prebuilt.zip` をダウンロードします。

!["The Braze SDK release page on GitHub."]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

## ステップ 2: フレームワークの選択

Braze Swift SDK にはさまざまなスタンドアローンXCFrameworks が含まれています。これにより、必要な機能を統合する自由が得られます。すべてを統合する必要はありません。次の表を参照して、XCF ワークを選択します。

| パッケージ| 必須? | 説明|
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit` | Yes | 分析およびプッシュ通知のサポートを提供するメインSDK ライブラリ。|
| `BrazeLocation` | No | 位置分析とジオフェンスモニタリングをサポートするロケーションライブラリ。|
| `BrazeUI` | No | アプリ内メッセージおよびコンテンツカード用の Braze 提供ユーザーインタフェースライブラリ。|
| `BrazeNotificationService` | No | リッチプッシュ通知をサポートする通知サービス拡張ライブラリ。このライブラリをメインアプリケーションターゲットに直接追加するのではなく、[`BrazeNotificationService` ライブラリを別途追加](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).|
| `BrazePushStory` | No | プッシュストーリーをサポートする通知コンテンツ拡張ライブラリ。このライブラリをメインアプリケーションターゲットに直接追加するのではなく、[`BrazePushStory` ライブラリを個別に](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)追加します。|
| `BrazeKitCompat` | No | Compatibility library `Appboy` と`ABK*` のすべてのクラスとメソッドを含む互換性ライブラリ。`Appboy-iOS-SDK` バージョン4.X.X で使用できます。使用方法の詳細については、[マイグレーションガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)の最小マイグレーションシナリオを参照してください。|
| `BrazeUICompat` | No | Compatibility library `ABK*` のすべてのクラスと`AppboyUI` ライブラリで`Appboy-iOS-SDK` バージョン4.X.X から利用可能なメソッドを含む。使用方法の詳細については、[マイグレーションガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)の最小マイグレーションシナリオを参照してください。|
| `SDWebImage` | 最小移行シナリオで`BrazeUICompat` のみが使用する依存関係|

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2}

## ステップ 3: ファイルの準備

**Static** または**Dynamic** XCFrameworks を使用するかどうかを決定し、ファイルを準備します。

{% tabs %}
{% tab dynamic %}
1. XCF ワーク用の一時ディレクトリーを作成します。
2. `braze-swift-sdk-prebuilt`で、`dynamic`ディレクトリを開き、`BrazeKit.xcframework`をディレクトリに移動します。ディレクトリは次のようになります。
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. [ chosen XCFrameworks](#step-2-choose-your-frameworks) をそれぞれ一時ディレクトリに移動します。ディレクトリは次のようになります。
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```
{% endtab %}

{% tab static %}
### ステップ 3.1:フレームワークの準備

1. XCF ワーク用の一時ディレクトリーを作成します。
2. `braze-swift-sdk-prebuilt` で`static` ディレクトリを開き、`BrazeKit.xcframework` をディレクトリに移動します。ディレクトリは次のようになります。
   ```bash
   temp_frameworks_dir
   └── BrazeKit.xcframework
   ```
3. [ chosen XCFrameworks](#step-2-choose-your-frameworks) をそれぞれ一時ディレクトリに移動します。ディレクトリは次のようになります。
   ```bash
   temp_frameworks_dir
   ├── BrazeKit.xcframework
   ├── BrazeKitCompat.xcframework
   ├── BrazeLocation.xcframework
   └── SDWebImage.xcframework
   ```

### ステップ 3.2:バンドルの準備

1. バンドルの一時ディレクトリを作成します。
2. `bundles` ディレクトリを開き、`BrazeKit.bundle` をディレクトリに移動します。ディレクトリは次のようになります。
   ```bash
   temp_bundles_dir
   └── BrazeKit.bundle
   ```
3. `BrazeLocation`、`BrazeUI`、`BrazeUICompat`、または`SDWebImage` XCFrameworks を使用している場合は、対応するバンドルを一時ディレクトリに移動します。ディレクトリは次のようになります。
   ```bash
   temp_bundles_dir
   ├── BrazeLocation.bundle
   ├── BrazeUI.bundle
   ├── BrazeUICompat.bundle
   └── SDWebImage.bundle
   ```
{% alert note %}
[準備したフレームワーク](#step-31-prepare-your-frameworks)のバンドルの上のみ移動します。
{% endalert %}
{% endtab %}
{% endtabs %}

## ステップ 4: フレームワークの統合

次に、**Dynamic** または**Static** XCFrameworks you [prepared before](#step-3-prepare-your-files) を統合します。

{% tabs %}
{% tab dynamic %}
Xcode プロジェクトで、ビルドターゲットを選択し、**General** を選択します。**Frameworks, Libraries, and Embedded Content**の下で、前に準備した[ファイルをドラッグ&ドロップします。

!["An example Xcode project with each Braze library set to 'Embed & Sign.'"]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert tip %}
GIF サポートを有効にするには、`braze-swift-sdk-prebuilt/dynamic` にある`SDWebImage.xcframework` を追加します。
{% endalert %}
{% endtab %}

{% tab static %}
Xcode プロジェクトで、ビルドターゲットを選択し、**General** を選択します。**Frameworks, Libraries, and Embedded Content**の下で、前に準備した[フレームワークをドラッグ&ドロップします。各フレームワークの横にある**埋め込まない**を選択します。 

!["An example Xcode project with each Braze library set to 'Do Not Embed.'"]({% image_buster /assets/img/swift/sdk_integration/do-not-embed-and-sign.png %})

{% alert tip %}
GIF サポートを有効にするには、`braze-swift-sdk-prebuilt/static` にある`SDWebImage.xcframework` を追加します。
{% endalert %}

ビルドターゲットで、**ビルドフェーズ** を選択します。**Copy Bundle Resources**の下で、前に準備した[バンドルをドラッグ&ドロップします。

!["An example Xcode project with bundles added under 'Copy Bundle Resources.'"]({% image_buster /assets/img/swift/sdk_integration/copy-bundle-resources.png %})
{% endtab %}
{% endtabs %}

## Objective-C プロジェクトの一般的なエラー

Xcode プロジェクトにObjective-C ファイルのみが含まれている場合は、" missing symbol" errors with your build your project.これらのエラーを修正するには、プロジェクトを開き、空のSwift ファイルをファイルツリーに追加します。これにより、ビルドツールチェーンは[Swift Runtime](https://support.apple.com/kb/dl1998) を埋め込み、ビルド時に適切なフレームワークにリンクします。

```bash
FILE_NAME.swift
```

`FILE_NAME` を空白以外の文字列に置き換えます。ファイルは次のようになります。

```bash
empty_swift_file.swift
```
