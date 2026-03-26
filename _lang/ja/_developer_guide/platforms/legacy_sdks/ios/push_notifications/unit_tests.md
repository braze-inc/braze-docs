---
nav_title: 単体テスト (オプション)
article_title: iOS のプッシュ通知単体テスト
platform: iOS
page_order: 29.5
description: "この参考記事では、iOS プッシュ実装のオプションの単体テストを実装する方法について説明します。"
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# 単体テスト {#unit-tests}

このオプションのガイドでは、アプリのデリゲートが[プッシュ統合手順]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration/)に記載されている手順に正しく従っているかどうかを検証するいくつかの単体テストを実装する方法について説明します。 

すべてのテストに合格した場合、通常、プッシュ設定のコードベースの部分が機能していることを意味します。テストが失敗した場合は、手順を誤って実行したか、有効なカスタマイズがデフォルトの手順と正確に一致していないことが原因である可能性があります。

いずれにせよ、これは統合手順に従っていることを確認し、リグレッションを監視するのに役立つアプローチです。

## ステップ1:単体テストターゲットの作成

Xcode のアプリプロジェクトにすでに単体テストバンドルが含まれている場合は、このステップをスキップしてください。

アプリプロジェクトで、メニューの **[ファイル] > [新規] > [ターゲット]** に移動し、新しい「単体テストバンドル」を追加します。このバンドルでは、Objective-C または Swift を使用でき、任意の名前を付けることができます。[テスト対象] をメインのアプリターゲットに設定します。

## ステップ2:Braze SDK を単体テストに追加する

最初に [Braze SDK をインストールする]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview/)ために使用したのと同じ方法を使用して、同じ SDK インストールが単体テストのターゲットでも使用できることを確認します。たとえば、CocoaPods を使用すると、次のようになります。

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## ステップ 3:OCMock を単体テストに追加する

CocoaPods、Carthage、またはその静的ライブラリを介して [OCMock](https://ocmock.org/) をテストターゲットに追加します。たとえば、CocoaPods を使用すると、次のようになります。

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## ステップ 4:追加したライブラリのインストールを完了する

Braze SDK と OCMock のインストールを完了します。たとえば、CocoaPods を使用して、ターミナル内の Xcode アプリプロジェクトのディレクトリに移動し、次のコマンドを実行します。

```
pod install
```

この時点で、CocoaPods によって作成された Xcode プロジェクトワークスペースを開くことができるはずです。

## ステップ5: プッシュテストの追加

単体テストのターゲットに新しい Objective-C ファイルを作成します。 

単体テストのターゲットが Swift にある場合、Xcode は「Objective-C ブリッジングヘッダーを構成しますか?」と尋ねる場合があります。ブリッジングヘッダーはオプションであるため、[**作成しない**] をクリックしてもこれらの単体テストを正常に実行できます。

HelloSwift サンプルアプリの [`AppboyPushUnitTests.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m) のコンテンツを新しいファイルに追加します。

## ステップ6: テストスイートを実行する

アプリの単体テストを実行します。これは1回限りの検証ステップにすることも、リグレッションを検出するためにこれをテストスイートに無期限に含めることもできます。

