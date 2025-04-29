---
nav_title: iOS
article_title: Unity の SDK iOS 統合
platform: 
  - Unity
  - iOS
page_order: 1
description: "このリファレンス記事では、Unity プラットフォームのiOS SDKインテグレーションについて説明します。"
search_rank: .9
---

# SDK iOS 統合

> このリファレンス記事では、Unity プラットフォームのiOS SDKインテグレーションについて説明します。Braze を Unity アプリケーションで実行するには、以下の手順に従ってください。 

手動統合から移行する場合は、[自動統合](#transitioning-from-manual-to-automated-integration-ios)の手順をお読みください。

## ステップ1:Braze Unity パッケージの選択

Braze [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) は、Android プラットフォームと iOS プラットフォーム向けのネイティブバインディングを C# インターフェイスとともにバンドルします。

Braze Unity パッケージは、次の2種類の統合オプションを使用して、[Braze Unity リリースページ](https://github.com/Appboy/appboy-unity-sdk/releases)でダウンロードできます。

1. `Appboy.unitypackage` のみ
  - このパッケージは、Braze Android と iOS SDK を追加の依存関係なしでバンドルします。この統合方法では、Braze アプリ内メッセージングと、iOS 上のコンテンツカード機能が適切に機能しません。カスタムコードなしで完全なBraze機能を使用する場合は、代わりに以下のオプションを使用してください。
  - この統合オプションを使用する場合は、[Braze 構成] の下にある Unity UI で `Import SDWebImage dependency` の横にあるボックスに*チェックマークが入れられていない*ことを確認してください。
2. `SDWebImage` を含む `Appboy.unitypackage`
  - この統合オプションは、Braze Android および iOS SDK と、iOS SDK の [SDWebImage](https://github.com/SDWebImage/SDWebImage) 依存関係をバンドルします。これは、Braze アプリ内メッセージングと、iOS 上のコンテンツカード機能を適切に機能させるために必要です。`SDWebImage` フレームワークは、GIF を含む画像のダウンロードと表示に使用されます。完全なBraze機能を使用する場合は、このパッケージを読み込むしてインポートします。
  - `SDWebImage` を自動的にインポートするには、[Braze 構成] の下にある Unity UIで `Import SDWebImage dependency` の横にあるボックスに*チェックマークが入れられている*ことを確認してください。

**iOS**:iOS プロジェクトに [SDWebImage](https://github.com/SDWebImage/SDWebImage) の依存関係が必要かどうかを確認するには、[iOS アプリ内メッセージドキュメント]を参照してください。({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).] <br>
**Android**:Unity 2.6.0 以降、バンドルされた Braze Android SDK アーティファクトには [AndroidX](https://developer.android.com/jetpack/androidx) 依存関係が必要です。以前に`jetified unitypackage` を使用していた場合は、対応する`unitypackage` に安全に移行できます。

## ステップ2:パッケージをインポートする

Unity エディターで Unity プロジェクトにパッケージをインポートするには、**[アセット] > [パッケージをインポート] > [カスタムパッケージ]** の順に移動します。次に、**Import**をクリックします。

または、カスタム Unity パッケージのインポートに関して詳しくは、[Unity アセットパッケージのインポート](https://docs.unity3d.com/Manual/AssetPackages.html)の説明を参照してください。 

{% alert note %}
iOS またはAndroid プラグインのみをインポートする場合は、Braze`.unitypackage` をインポートするときに`Plugins/Android` または`Plugins/iOS` サブディレクトリの選択を解除します。
{% endalert %}

## ステップ3:API キーの設定

Braze は、Unity iOS 統合を自動化するためのネイティブ Unity ソリューションを提供しています。このソリューションは、Unity の [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) を使用してビルドされた Xcode プロジェクトを変更し、`IMPL_APP_CONTROLLER_SUBCLASS` マクロを使用して `UnityAppController` をサブクラス化します。

1. Unity エディターで **[Braze] > [Braze 構成]** の順に移動して、[Braze 構成設定] を開きます。
2. [**Unity iOS 統合の自動化**] ボックスにチェックマークを入れます。
3. **Braze API キー** フィールドで、**設定の管理** にあるアプリアプリケーションのAPI キーを入力します。

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

アプリですでに別の `UnityAppController` サブクラスが使用されている場合、サブクラスの実装を `AppboyAppDelegate.mm` とマージする必要があります。

## 基本的な SDK 統合の完了

これで、Braze はアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。プッシュ統合の詳細については、次の記事を参照してください。[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/)と[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/)、[アプリ内メッセージs]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/)、[コンテンツカード]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/)。

高度なSDKインテグレーションオプションについては、[高度なインプリメンテーション]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#ios-sdk-advanced)を参照してください。

