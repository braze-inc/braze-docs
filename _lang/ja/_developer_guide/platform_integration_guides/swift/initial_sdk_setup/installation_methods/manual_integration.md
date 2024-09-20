---
nav_title: 手動統合
article_title: iOSの手動統合
platform: Swift
page_order: 3
description: "このリファレンス記事では、手動インストールを使用してBraze SWIFT SDKを統合する方法を示します。"
toc_headers: "h2"
---

# 手動統合

> パッケージマネージャー（[SWIFTパッケージマネージャー]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/)や[CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/)など）にアクセスできない場合は、代わりに手動でSWIFT SDKを統合することができます。

## ステップ1:Braze SDKをダウンロード

[GitHubのBraze SDKリリースページ](https://github.com/braze-inc/braze-swift-sdk/releases)に移動し、`braze-swift-sdk-prebuilt.zip`をダウンロードします。

![「GitHubのBraze SDKリリースページ。」]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

## ステップ2:フレームワークを選択してください

BrazeのSWIFT SDKには、さまざまなスタンドアロンのXCFrameworkが含まれており、すべてを統合する必要はなく、必要な機能を自由に統合できます。次の表を参照して、XCFrameworksを選択してください:

| パッケージ                    | 必要？ | 説明                                                                                                                                                                                                                                                                                                              |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | はい       | メインSDKライブラリーは、分析とプッシュ通知をサポートします。                                                                                                                                                                                                                                             |
| `BrazeLocation`            | いいえ        | 位置情報ライブラリーは、位置情報分析とジオフェンス監視をサポートします。                                                                                                                                                                                                                                   |
| `BrazeUI`                  | いいえ        | アプリ内メッセージおよびコンテンツカード用のBraze提供のユーザーインターフェイスライブラリー。                                                                                                                                                                                                                                             |
| `BrazeNotificationService` | いいえ        | リッチプッシュ通知をサポートする通知サービス拡張ライブラリー。このライブラリーを直接メインアプリケーションターゲットに追加しないでください。代わりに[この`BrazeNotificationService`ライブラリーを別々に追加してください](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications)。     |
| `BrazePushStory`           | いいえ        | 通知コンテンツ拡張ライブラリーは、プッシュストーリーをサポートします。このライブラリーを直接メインアプリケーションターゲットに追加しないでください。代わりに[この`BrazePushStory`ライブラリーを別々に追加してください](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories)。                                     |
| `BrazeKitCompat`           | いいえ        | 互換性ライブラリーには、バージョン4.X.Xの`Appboy-iOS-SDK`で利用可能だったすべての`Appboy`および`ABK*`クラスとメソッドが含まれています。使用の詳細については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)の最小限の移行シナリオを参照してください。 |
| `BrazeUICompat`            | いいえ        | 互換性ライブラリーには、`ABK*`クラスとメソッドがすべて含まれており、`AppboyUI`ライブラリーのバージョン4.X.Xから利用可能です。使用の詳細については、[移行ガイド](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/)の最小限の移行シナリオを参照してください。 |
| `SDWebImage`               | いいえ        | 最小限の移行シナリオで`BrazeUICompat`のみに使用される依存関係。 |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2}

## ステップ3:ファイルを準備してください

静的なXCFrameworksを使用するかダイナミックなXCFrameworksを使用するかを決定し、ファイルを準備します。

{% tabs %}
{% tab ダイナミックな %}
1. 一時的なディレクトリを作成して、XCFrameworksを保存します。
2. `braze-swift-sdk-prebuilt`で、`dynamic`ディレクトリを開封し、`BrazeKit.xcframework`を自分のディレクトリに移動します。あなたのディレクトリは次のようになります:
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. 選択した各XCFrameworkを一時ディレクトリに移動します。あなたのディレクトリは次のようになります:
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

1. 一時的なディレクトリを作成して、XCFrameworksを保存します。
2. `braze-swift-sdk-prebuilt`で、`static`ディレクトリを開封し、`BrazeKit.xcframework`を自分のディレクトリに移動します。あなたのディレクトリは次のようになります:
   ```bash
   temp_frameworks_dir
   └── BrazeKit.xcframework
   ```
3. 選択した各XCFrameworkを一時ディレクトリに移動します。あなたのディレクトリは次のようになります:
   ```bash
   temp_frameworks_dir
   ├── BrazeKit.xcframework
   ├── BrazeKitCompat.xcframework
   ├── BrazeLocation.xcframework
   └── SDWebImage.xcframework
   ```

### ステップ 3.2:バンドルを準備する

1. 一時的なディレクトリを作成して、バンドル用に使用します。
2. 開封 the `bundles` directory and move `BrazeKit.bundle` into your directory.あなたのディレクトリは次のようになります:
   ```bash
   temp_bundles_dir
   └── BrazeKit.bundle
   ```
3. XCFrameworks `BrazeLocation`、`BrazeUI`、`BrazeUICompat`、`SDWebImage` を使用している場合は、それらに対応するバンドルを一時ディレクトリに移動します。あなたのディレクトリは次のようになります:
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

次に、**ダイナミックな**または**静的な**XCFrameworksを[以前に準備した](#step-3-prepare-your-files)ものと統合します。

{% tabs %}
{% tab ダイナミックな %}
Xcodeプロジェクトでビルドターゲットを選択し、次に**一般**を選択します。**フレームワーク、ライブラリ、および埋め込みコンテンツ**の下に、[以前に準備したファイル<6>}をドラッグ＆ドロップします。

![「各Brazeライブラリーが「埋め込みと署名」に設定されたXcodeプロジェクトの例」]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert tip %}
GIFサポートを有効にするには、`SDWebImage.xcframework`を追加し、`braze-swift-sdk-prebuilt/dynamic`に配置します。
{% endalert %}
{% endtab %}

{% tab 静的 %}
Xcodeプロジェクトでビルドターゲットを選択し、次に**一般**。**フレームワーク、ライブラリ、および埋め込みコンテンツ**の下に、[以前に準備したフレームワーク<5>}をドラッグ＆ドロップします。各フレームワークの横に、**埋め込まない**を選択します。 

![「各Brazeライブラリーが「埋め込まない」に設定されているXcodeプロジェクトの例。」]({% image_buster /assets/img/swift/sdk_integration/do-not-embed-and-sign.png %})

{% alert tip %}
GIFサポートを有効にするには、`SDWebImage.xcframework`を追加し、`braze-swift-sdk-prebuilt/static`に配置します。
{% endalert %}

ビルドターゲットにいる間に、**ビルドフェーズ**を選択します。**Copy Bundle Resources**の下に、以前に準備した[バンドル<3>}をドラッグ＆ドロップします。

![「'Copy Bundle Resources'の下にバンドルが追加されたXcodeプロジェクトの例。」]({% image_buster /assets/img/swift/sdk_integration/copy-bundle-resources.png %})
{% endtab %}
{% endtabs %}

## Objective-Cプロジェクトの一般的なエラー

XcodeプロジェクトにOBJECTIVE-Cファイルのみが含まれている場合、プロジェクトのビルドを試みると「シンボルが見つかりません」というエラーが発生することがあります。これらのエラーを修正するには、プロジェクトを開封し、ファイルツリーに空のSWIFTファイルを追加します。これにより、ビルドツールチェーンが[SWIFTランタイム](https://support.apple.com/kb/dl1998)を埋め込み、ビルド時に適切なフレームワークにリンクするようになります。

```bash
FILE_NAME.swift
```

任意のスペースのない文字列で`FILE_NAME`を置き換えます。あなたのファイルは次のようになります:

```bash
empty_swift_file.swift
```
