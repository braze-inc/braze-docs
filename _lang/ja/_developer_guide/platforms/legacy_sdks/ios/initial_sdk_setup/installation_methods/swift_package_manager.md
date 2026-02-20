---
nav_title: Swiftパッケージマネージャー
article_title: iOS 向け Swift Package Manager の統合
platform: iOS
page_order: 3
description: "このチュートリアルでは、iOS 用 Swift Package Manager を使用した Braze SDK のインストールについて説明します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Swift Package Manager の統合

[Swift Package Manager](https://swift.org/package-manager/) (SPM) 経由で iOS SDK をインストールすると、インストールプロセスの大部分が自動化されます。このプロセスを開始する前に、Xcode 12 以降を使用していることを確認してください。

{% alert note %}
tvOS は現在、Swift Package Manager 経由では利用できません。
{% endalert %}

## ステップ1:依存関係をプロジェクトに追加する

### SDK バージョンのインポート

プロジェクトを開き、プロジェクトの設定に移動します。[**Swift パッケージ**] タブを選択し、パッケージリストの下にある <i class="fas fa-plus"></i>[追加] ボタンをクリックします。

![]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

SDK バージョン `3.33.1` 以降をインポートする場合、iOS SDK リポジトリの URL (`https://github.com/braze-inc/braze-ios-sdk`) をテキストフィールドに入力し、[**次へ**] をクリックします。 

バージョン `3.29.0` から `3.32.0` の場合、URL `https://github.com/Appboy/Appboy-ios-sdk` を使用してください。

![]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

次の画面で、SDK バージョンを選択し、[**次へ**] をクリックします。バージョン `3.29.0` 以降は Swift Package Manager と互換性があります。

![]({% image_buster /assets/img/ios/spm/select_version.png %})

### パッケージの選択

ニーズに最も適したパッケージを選択し、[**完了**] をクリックします。必ず `AppboyKit` または `AppboyUI` のどちらかを選択してください。両方のパッケージを含めると、望ましくない動作が発生する可能性があります。

- `AppboyUI`
  - Braze が提供するUIコンポーネントを使用する場合に最適です。
  - `AppboyKit` が自動的に含まれます。
- `AppboyKit`
  - Braze が提供する UI コンポーネント (コンテンツカード、アプリ内メッセージなど) を使用する必要がない場合に最適です。
- `AppboyPushStory`
  - アプリにプッシュストーリーを統合している場合は、このパッケージを含めます。これは現在のバージョン `3.31.0` 以降でサポートされています。
  - `Add to Target` のドロップダウンで 、メインアプリのターゲットの代わりに `ContentExtension` ターゲットを選択してください。 

![]({% image_buster /assets/img/ios/spm/add_package.png %})

## ステップ 2:プロジェクトの構成

次に、プロジェクトの**ビルド設定**に移動し、`-ObjC` フラグを [**その他のリンカーフラグ**] 設定に追加します。SDK をさらに統合するには、このフラグを追加し、[エラー](https://developer.apple.com/library/archive/qa/qa1490/_index.html)を解決する必要があります。

![]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
`-ObjC` フラグを追加しない場合は、API の一部が欠落し、動作が未定義になる可能性があります。「認識されないセレクターがクラスに送信されました」などの予期しないエラー、アプリケーションのクラッシュ、その他の問題が発生する可能性があります。
{% endalert %}

## ステップ3: ターゲットのスキームの編集
{% alert important %}
Xcode 12.5 以降を使用している場合は、この手順をスキップしてください。
{% endalert %}

Xcode 12.4 以前を使用している場合は、Appboy パッケージを含むターゲットのスキームを編集します (**[製品] > [スキーム] > [スキームの編集]** メニュー項目)。
1. [**ビルド**] メニューを展開し、[**ポストアクション**] を選択します。プラス (+) ボタンを押して、[**新しいスクリプト実行アクション**] を選択します。
2. [**ビルド設定の提供元**] ドロップダウンで、アプリのターゲットを選択します。
3.  このスクリプトを開封フィールドにコピーしてください:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## 次のステップ

手順に従って[統合を完了]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/)してください。

