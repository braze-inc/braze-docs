---
nav_title: iOS
article_title: ユニティ用 SDK iOS インテグレーション
platform: 
  - Unity
  - iOS
page_order: 1
description: "この参考記事では、Unity プラットフォームの iOS SDK 統合について説明します。"
search_rank: .9
---

# SDK iOS インテグレーション

> この参考記事では、Unity プラットフォームの iOS SDK 統合について説明します。こちらのガイドに従って、お使いの Unity アプリケーションで Braze を実行してください。 

手動統合から移行する場合は、「[自動統合への移行][5]」の手順をお読みください。

## ステップ 1:Braze ユニティパッケージをお選びください

Brazeには、[`.unitypackage`][41]AndroidおよびiOSプラットフォーム用のネイティブバインディングとC＃インターフェイスがバンドルされています。

Braze Unity パッケージは、次の 2 つの統合オプションを含む [Braze Unity リリースページからダウンロードできます][42]。

1. `Appboy.unitypackage` のみ
  - このパッケージには Braze Android と iOS の SDK がバンドルされており、追加の依存関係はありません。この統合方法では、Brazeのアプリ内メッセージ機能やiOSのコンテンツカード機能が正しく機能しなくなります。カスタムコードなしで Braze の全機能を活用したい場合は、代わりに以下のオプションを使用してください。
  - この統合オプションを使用するには、Unity UIの「Braze Configuration」*の横のボックスがオフになっていることを確認してください*。`Import SDWebImage dependency`
2. `Appboy.unitypackage` と `SDWebImage`
  - この統合オプションには、Braze AndroidおよびiOS SDKと、[Brazeアプリ内メッセージングの適切な機能およびiOSのコンテンツカード機能の適切な機能に必要な、iOS SDK用のSDWebImage依存関係がバンドルされています][unity-1]。`SDWebImage`このフレームワークは、GIF を含む画像のダウンロードと表示に使用されます。Braze の全機能を利用したい場合は、このパッケージをダウンロードしてインポートしてください。
  - 自動的にインポートするには`SDWebImage`、Unity UI の「Braze 設定」*`Import SDWebImage dependency`の下の横にあるチェックボックスを必ずチェックしてください*。

**iOS**:iOS プロジェクトに [SDWebImage][unity-1] 依存関係が必要かどうかを確認するには、[iOS アプリ内メッセージドキュメント] [unity-4] を参照してください。<br>
**Android**:[Unity 2.6.0 以降、バンドルされている Braze Android SDK アーティファクトには AndroidX の依存関係が必要です。][unity-3]以前にを使用していた場合は`jetified unitypackage`、対応するバージョンに安全に移行できます`unitypackage`。

## ステップ 2: パッケージをインポートする

Unity エディターで、「**アセット」>「パッケージのインポート」>「カスタムパッケージ」に移動して、パッケージを Unity プロジェクトにインポートします**。次に、[**インポート**] をクリックします。

または、[Unity アセットパッケージのインポート手順に従って][41]、カスタム Unity パッケージのインポートに関する詳細なガイドを参照してください。 

{% alert note %}
iOS または Android プラグインのみをインポートする場合は、Braze `Plugins/Android` `Plugins/iOS` をインポートするときにまたはサブディレクトリの選択を解除してください。`.unitypackage`
{% endalert %}

## ステップ 3: API キーを設定する

Braze は Unity iOS 統合を自動化するためのネイティブ Unity ソリューションを提供しています。このソリューションは、[`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html)Unityを使用してビルドされたXcodeプロジェクトを変更し、`UnityAppController`マクロを使用してサブクラス化します。`IMPL_APP_CONTROLLER_SUBCLASS`

1. Unity エディターで、Braze **> Braze 設定に移動して Braze** 設定を開きます。
2. 「**Unity iOS インテグレーションの自動化**」ボックスをチェックします。
3. **Braze API キーフィールドに**、**設定管理にあるアプリケーションの** API キーを入力します。

![\]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

`UnityAppController`アプリケーションがすでに別のサブクラスを使用している場合は、サブクラスの実装をにマージする必要があります。`AppboyAppDelegate.mm`

## \## 基本的な SDK 統合の完了

これで、Braze はアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。Push の統合について詳しくは、以下の記事をご覧ください。[Android][53] と [iOS][50]、[アプリ内メッセージ][34]、[コンテンツカード][40]

高度な SDK 統合オプションについては、「[高度な実装][54]」をご覧ください。

[5]: #transitioning-from-manual-to-automated-integration-ios
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/news_feed/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[42]: https://github.com/Appboy/appboy-unity-sdk/releases
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/
[54]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#ios-sdk-advanced
[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-2]: https://firebase.google.com/docs/unity/setup
[unity-3]: https://developer.android.com/jetpack/androidx
[[unity-4]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/
