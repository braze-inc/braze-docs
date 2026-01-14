---
nav_title: マニュアル
article_title: iOS の手動統合オプション
platform: iOS
page_order: 4
description: "この参考記事では、iOS 用 Braze SDK を手動で統合する方法を説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 手動統合

{% alert tip %}
[Swift パッケージマネージャー](../swift_package_manager/)、[CocoaPods](../cocoapods/)、[Carthage](../carthage_integration/) などのパッケージマネージャーを使用して SDK を実装することを強くお勧めします。これにより、時間を大幅に節約し、プロセスの多くを自動化できます。ただし、それができない場合は、手順に従って手動で統合を完了することができます。
{% endalert %}

## ステップ1:Braze SDK のダウンロード

### オプション1:ダイナミック XCFramework

1. [リリースページ](https://github.com/appboy/appboy-ios-sdk/releases)から `Appboy_iOS_SDK.xcframework.zip`をダウンロードし、ファイルを抽出します。
2. Xcode では、この `.xcframework` をプロジェクトにドラッグアンドドロップします。
3. プロジェクトの**General** タブの下で、`Appboy_iOS_SDK.xcframework` に**Embed & Sign** を選択します。

### オプション 2: 静的統合用の静的 XCFramework

1. [リリースページ](https://github.com/appboy/appboy-ios-sdk/releases)から `Appboy_iOS_SDK.zip` をダウンロードしてください。<br><br>
2. Xcode のプロジェクトナビゲーターから、Braze の宛先プロジェクトまたはグループを選択します。<br><br>
3. **File > Add Files > Project_Name** に移動します。<br><br>
4. `AppboyKit` と `AppboyUI` フォルダをグループとしてプロジェクトに追加します。
	- 初めて統合する場合は、[**宛先グループのフォルダに項目をコピー**] オプションが選択されていることを確認してください。ファイルピッカーの [**オプション**] を展開して、[**必要に応じてアイテムをコピー**] と [**グループを作成**] を選択します。
	- `AppboyKit/include` と `AppboyUI/include` のディレクトリを削除します。<br><br>
5. (オプション) 次のいずれかに該当する場合:
  - SDK のコア分析機能のみが必要で、UI 機能 (アプリ内メッセージやコンテンツカードなど) は使用しないでください。
  - Braze UI 機能のカスタム UI があり、画像のダウンロードは自分で処理できます。<br><br>SDK のコアバージョンは、`ABKSDWebImageProxy.m` および `Appboy.bundle` のファイルを削除することで使用できます。これにより、`SDWebImage` フレームワークの依存関係と UI 関連のすべてのリソース (Nib ファイル、画像、ローカリゼーションファイルなど) が SDK から削除されます。

{% alert warning %}
Braze UI 機能なしでコアバージョンの SDK を使用しようとしても、アプリ内メッセージは表示されません。コアバージョンで Braze コンテンツカードの UI を表示しようとすると、予期しない動作が発生します。
{% endalert %}

## ステップ2:必要な iOS ライブラリの追加

1. プロジェクトのターゲットをクリックし (左側のナビゲーションを使用)、[**ビルドフェーズ**] タブを選択します。<br><br>
2. [**バイナリをライブラリにリンク**] の下の<i class="fas fa-plus"></i>ボタンをクリックします。<br><br>
3. メニューで、`SystemConfiguration.framework` を選択します。<br><br>
4. `SystemConfiguration.framework` の横にあるプルダウンメニューを使用して、このライブラリを必須としてマークします。<br><br>
5. これを繰り返して、次の各必須フレームワークをプロジェクトに追加し、それぞれを「必須」としてマークします。
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. 次のフレームワークを追加し、オプションとしてマークします。
	- `CoreTelephony.framework`<br><br>
7. [**ビルド設定**] タブを選択します。[**リンク**] セクションで、「**その他のリンカーフラグ**」設定を探し、`-ObjC` フラグを追加します。<br><br>
8. コンテンツカードとアプリ内メッセージングが正しく機能するには、`SDWebImage` フレームワークが必要です。`SDWebImage` は GIF を含む画像のダウンロードと表示に使用されます。コンテンツカードまたはアプリ内メッセージを使用する場合は、SDWebImage の統合手順に従ってください。

### SDWebImage 統合

`SDWebImage` をインストールするには、[手順](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework)に従い、出来上がった `XCFramework` をプロジェクトにドラッグアンドドロップしてください。

### オプションの位置情報の追跡

1. `CoreLocation.framework` を追加して位置情報の追跡を有効にします。
2. アプリで `CLLocationManager` を使用するユーザーの位置情報を認証する必要があります。

## ステップ3:Objective-C ブリッジヘッダー

{% alert note %}
プロジェクトで Objective-C のみを使用する場合は、このステップをスキップしてください。
{% endalert %}

プロジェクトで Swift を使用している場合は、ブリッジヘッダーファイルが必要になります。

ブリッジヘッダーファイルがない場合は、**[ファイル] > [新規] > [ファイル] > (iOS または OS X) > [ソース] > [ヘッダーファイル]** を選択して作成し、`your-product-module-name-Bridging-Header.h` という名前を付けます。次に、ブリッジヘッダーファイルの先頭に次のコード行を追加します。
```
#import "AppboyKit.h"
```

プロジェクトの**ビルド設定**で、ヘッダーファイルの相対パスを `Swift Compiler - Code Generation` の下の `Objective-C Bridging Header` ビルド設定に追加します。

## 次のステップ

手順に従って[統合を完了]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/)してください。
