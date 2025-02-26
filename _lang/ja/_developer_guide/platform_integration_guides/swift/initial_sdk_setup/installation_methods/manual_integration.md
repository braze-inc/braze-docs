---
nav_title: 手動統合
article_title: iOS 向け手動統合
platform: Swift
page_order: 3
description: "この参照記事では、手動統合を使用して Braze Swift SDK を統合する方法を説明します。"
toc_headers: "h2"
---

# 手動統合

> パッケージマネージャー（[SWIFTパッケージマネージャー]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/)や[CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/)など）にアクセスできない場合は、代わりに手動でSWIFT SDKを統合することができます。

## ステップ1:Braze SDKをダウンロード

[GitHubのBraze SDKリリースページ](https://github.com/braze-inc/braze-swift-sdk/releases)に移動し、`braze-swift-sdk-prebuilt.zip`をダウンロードします。

![「GitHub の Braze SDK リリースページ。」]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

## ステップ2:フレームワークを選択してください

Braze SWIFT SDK には、さまざまなスタンドアロンの XCFramework が含まれており、すべてを統合する必要はなく、必要な機能を自由に統合できます。次の表を参照して、XCFrameworksを選択してください:

| パッケージ                    | 必要か | 説明                                                                                                                                                                                                                                                                                                              |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | はい       | メインSDKライブラリーは、分析とプッシュ通知をサポートします。                                                                                                                                                                                                                                             |
| `BrazeLocation`            | いいえ        | 位置情報ライブラリーは、位置情報分析とジオフェンス監視をサポートします。                                                                                                                                                                                                                                   |
| `BrazeUI`                  | いいえ        | アプリ内メッセージおよびコンテンツカード用のBraze提供のユーザーインターフェイスライブラリー。                                                                                                                                                                                                                                             |
| `BrazeNotificationService` | いいえ        | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。このライブラリーを直接メインアプリケーションターゲットに追加しないでください。代わりに[この`BrazeNotificationService`ライブラリーを別々に追加してください](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)。     |
| `BrazePushStory`           | いいえ        | 通知コンテンツ拡張ライブラリーは、プッシュストーリーをサポートします。このライブラリーを直接メインアプリケーションターゲットに追加しないでください。代わりに[この`BrazePushStory`ライブラリーを別々に追加してください](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)。                                     |
| `BrazeKitCompat`           | いいえ        | `Appboy-iOS-SDK` バージョン 4.X.X で使用可能だったすべての `Appboy` および `ABK*` クラスとメソッドを含む互換性ライブラリ。使用の詳細については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)の最小限の移行シナリオを参照してください。 |
| `BrazeUICompat`            | いいえ        | `Appboy-iOS-SDK` バージョン4.X.Xの `AppboyUI`ライブラリで使用可能だったすべての`ABK*` クラスとメソッドを含む互換性ライブラリ。使用の詳細については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)の最小限の移行シナリオを参照してください。 |
| `SDWebImage`               | いいえ        | 最小限の移行シナリオで `BrazeUICompat` によってのみ使用される依存関係。 |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ステップ3:ファイルを準備してください

**静的** XCFrameworks または**動的** XCFrameworks のどちらを使用するかを決定してから、ファイルを準備します。

{% tabs %}
{% tab 動的 %}
1. XCFrameworks 用の一時ディレクトリーを作成します。
2. `braze-swift-sdk-prebuilt` で、`dynamic` ディレクトリを開き、`BrazeKit.xcframework` を自分のディレクトリに移動します。あなたのディレクトリは次のようになります:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. [選択した各 XCFramework](#step-2-choose-your-frameworks) を一時ディレクトリに移動します。あなたのディレクトリは次のようになります:
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```
{% endtab %}

{% tab 静的 %}
### ステップ 3.1:フレームワークを準備する

1. XCFrameworks 用の一時ディレクトリーを作成します。
2. `braze-swift-sdk-prebuilt` で、`static` ディレクトリを開き、`BrazeKit.xcframework` を自分のディレクトリに移動します。あなたのディレクトリは次のようになります:
   ```bash
   temp_frameworks_dir
   └── BrazeKit.xcframework
   ```
3. [選択した各 XCFramework](#step-2-choose-your-frameworks) を一時ディレクトリに移動します。あなたのディレクトリは次のようになります:
   ```bash
   temp_frameworks_dir
   ├── BrazeKit.xcframework
   ├── BrazeKitCompat.xcframework
   ├── BrazeLocation.xcframework
   └── SDWebImage.xcframework
   ```

### ステップ 3.2:バンドルを準備する

1. バンドル用の一時ディレクトリーを作成します。
2. `bundles` ディレクトリを開き、`BrazeKit.bundle` を自分のディレクトリに移動します。あなたのディレクトリは次のようになります:
   ```bash
   temp_bundles_dir
   └── BrazeKit.bundle
   ```
3. `BrazeLocation`、`BrazeUI`、`BrazeUICompat`、または `SDWebImage` XCFrameworksを使用している場合は、対応するバンドルを一時ディレクトリに移動します。あなたのディレクトリは次のようになります:
   ```bash
   temp_bundles_dir
   ├── BrazeLocation.bundle
   ├── BrazeUI.bundle
   ├── BrazeUICompat.bundle
   └── SDWebImage.bundle
   ```
{% alert note %}
バンドルを移動するのは、[準備したフレームワーク](#step-31-prepare-your-frameworks)だけにしてください。
{% endalert %}
{% endtab %}
{% endtabs %}

## ステップ4: フレームワークを統合する

次に、[以前に準備した](#step-3-prepare-your-files)**動的な** XCFrameworks または**静的な** XCFrameworks を統合します。

{% tabs %}
{% tab 動的 %}
Xcodeプロジェクトでビルドターゲットを選択し、次に**一般**を選択します。**フレームワーク、ライブラリ、および埋め込みコンテンツ**の下に、[以前に準備したファイル](#step-3-prepare-your-files)をドラッグ＆ドロップします。

![「各Brazeライブラリーが「埋め込みと署名」に設定されたXcodeプロジェクトの例」]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert tip %}
GIF サポートを有効にするには、`braze-swift-sdk-prebuilt/dynamic` にある `SDWebImage.xcframework` を追加します。
{% endalert %}
{% endtab %}

{% tab 静的 %}
Xcodeプロジェクトでビルドターゲットを選択し、次に**一般**を選択します。**フレームワーク、ライブラリ、および埋め込みコンテンツ**の下に、[以前に準備したフレームワーク](#step-31-prepare-your-frameworks)をドラッグ＆ドロップします。各フレームワークの横に、**埋め込まない**を選択します。 

![「各Brazeライブラリーが「埋め込まない」に設定されているXcodeプロジェクトの例。」]({% image_buster /assets/img/swift/sdk_integration/do-not-embed-and-sign.png %})

{% alert tip %}
GIF サポートを有効にするには、`braze-swift-sdk-prebuilt/static` にある `SDWebImage.xcframework` を追加します。
{% endalert %}

ビルドターゲットにいる間に、[**ビルドフェーズ**] を選択します。**Copy Bundle Resources**の下に、以前に準備した[バンドル<3>}をドラッグ＆ドロップします](#step-32-prepare-your-bundles)。

![「バンドルリソースをコピーする」の下にバンドルが追加された Xcode プロジェクトの例。」]({% image_buster /assets/img/swift/sdk_integration/copy-bundle-resources.png %})
{% endtab %}
{% endtabs %}

## Objective-Cプロジェクトの一般的なエラー

XcodeプロジェクトにOBJECTIVE-Cファイルのみが含まれている場合、プロジェクトのビルドを試みると「シンボルが見つかりません」というエラーが発生することがあります。これらのエラーを修正するには、プロジェクトを開封し、ファイルツリーに空のSWIFTファイルを追加します。これにより、ビルドツールチェーンが[SWIFTランタイム](https://support.apple.com/kb/dl1998)を埋め込み、ビルド時に適切なフレームワークにリンクするようになります。

```bash
FILE_NAME.swift
```

任意のスペースのない文字列で`FILE_NAME`を置き換えます。ファイルは次のようになります。

```bash
empty_swift_file.swift
```
