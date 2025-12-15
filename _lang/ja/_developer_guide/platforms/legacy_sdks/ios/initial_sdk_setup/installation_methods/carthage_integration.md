---
nav_title: Carthage
article_title: iOS 用 Carthage 統合
platform: iOS
page_order: 1
description: "この参照記事では、iOS 用 Carthage を使用して Braze SDK を統合する方法を示します。"

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Carthage 統合

## SDK をインポートする

バージョン `4.4.0` から、Braze SDK は Carthage 経由での統合時に XCFrameworks をサポートするようになりました。SDK 全体をインポートするには、次の行を `Cartfile` に含めます。
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

SDK のインポートの詳細については、[Carthage クイックスタートガイド](https://github.com/Carthage/Carthage#quick-start)を参照してください。

`4.4.0` 以前のバージョンから移行する場合は、[XCFrameworks 用 Carthage 移行ガイド](https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks)を参照してください。

{% alert note %}
`Cartfile` の構文やバージョンピン留めなどの機能の詳細については、[Carthage ドキュメント](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile)を参照してください。
Carthage のプラットフォーム固有の使用方法については、それぞれの[ユーザーガイド](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos)を参照してください。
{% endalert %}

### 以前のバージョン

`3.24.0` から `4.3.4` のバージョンの場合は、次の内容を `Cartfile` に含めてください。
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

`3.24.0` 以前のバージョンをインポートするには、`Cartfile` に以下を含めます。
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

`<BRAZE_IOS_SDK_VERSION>` は「x.y.z」形式の[適切なバージョン](https://github.com/Appboy/appboy-ios-sdk/releases)の Braze iOS SDK に置き換えてください。

## 次のステップ:

指示に従って[統合を完了]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration/)します。

## コアのみの統合

UIコンポーネントや依存関係なしで Core SDK を使用する場合は、以下の行を `Cartfile` に含めて Braze Carthage フレームワークのコアバージョンをインストールします。

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

