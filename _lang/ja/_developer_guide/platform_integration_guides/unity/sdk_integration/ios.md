---
nav_title: iOS
article_title: SDK iOS Integration for Unity
platform: 
  - Unity
  - iOS
page_order: 1
description: "このリファレンス記事では、Unity プラットフォームのiOS SDKインテグレーションについて説明します。"
search_rank: .9
---

# SDKのiOSインテグレーション

> このリファレンス記事では、Unity プラットフォームのiOS SDKインテグレーションについて説明します。Unity アプリのライセンスでBrazeを実行するには、次の手順に従ってください。 

手動統合から移行する場合は、[自動統合][5]の手順をお読みください。

## ステップ1:Braze Unityの選択

Braze[`.unitypackage`][41] は、Android およびiOS プラットフォームs のネイティブバインディングをC# インターフェイスとともにバンドルします。

Braze Unity パッケージは、[ Braze Unityで、ページ][42] を2 つのインテグレーションオプションを使用して読み込むできます。

1. `Appboy.unitypackage` のみ
  - このパッケージは、Braze Android とiOS SDKを追加の依存関係なしでバンドルします。この統合方式では、iOS上のBrazeインアプリ メッセージング、およびコンテンツカード機能の適切な機能はありません。カスタムコードなしで完全なBraze機能を使用する場合は、代わりに以下のオプションを使用してください。
  - この統合オプションを使用するには、" Braze Configuration" のUnity UI で、`Import SDWebImage dependency` の横のボックスが*unchecked* であることを確認します。
2. `Appboy.unitypackage` 有 `SDWebImage`
  - この統合オプションでは、Braze Android およびiOS SDKs と[SDWebImage][unity-1] 依存関係をiOS SDKにバンドルします。これは、iOS のBraze in-アプリ メッセージング、およびコンテンツカード機能の適切な機能に必要です。`SDWebImage` フレームワークは、GIF を含む"画像の表示と下位読み込むに使用されます。完全なBraze機能を使用する場合は、このパッケージを読み込むしてインポートします。
  - `SDWebImage` を自動的にインポートするには、" Braze Configuration" のUnity UI の`Import SDWebImage dependency` の横にあるボックスを*チェックしてください。

**iOS**:iOS プロジェクトに[SDWebImage][unity-1] の依存関係が必要かどうかを確認するには、\[iOS アプリ内メッセージ ドキュメント]\[unity-4]] を参照してください。<br>
**Android**:Unity 2.6.0 以降、バンドルされたBraze Android SDK アーティファクトには[AndroidX][unity-3] 依存関係が必要です。以前に`jetified unitypackage` を使用していた場合は、対応する`unitypackage` に安全に移行できます。

## ステップ2:パッケージをインポートする

Unityエディタで、**Assets > Import Package > Custom Package** に移動して、パッケージをUnity プロジェクトにインポートします。次に、**Import**をクリックします。

または、[ Unity アセットパッケージインポート][41] の手順に従って、カスタムUnityパッケージのインポートに関する詳細を確認してください。 

{% alert note %}
iOS またはAndroid プラグインのみをインポートする場合は、Braze`.unitypackage` をインポートするときに`Plugins/Android` または`Plugins/iOS` サブディレクトリの選択を解除します。
{% endalert %}

## ステップ3:API キーの設定

Braze は、Unity iOS インテグレーションを自動化するためのネイティブUnity ソリューションを提供します。このソリューションは、Unity の[`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) を使用してビルドされたXコード プロジェクトを変更し、`UnityAppController` マクロを使用して`UnityAppController` をサブクラス化します。

1. Unityエディタで、** Braze > Braze Configuration** に移動して、Braze 設定を開封します。
2. **Unity iOS 統合の自動化**を確認してください。
3. **Braze API キー** フィールドで、**設定の管理** にあるアプリアプリケーションのAPI キーを入力します。

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

アプリのライセンスで別の`UnityAppController` サブクラスがすでに使用されている場合は、サブクラスのインプリメンテーションを`AppboyAppDelegate.mm` にマージする必要があります。

## 基本SDK一体化完了

これで、Braze はアプリケーションからデータを収集しており、基本的な統合は完了しているはずです。プッシュの統合の詳細については、次の記事を参照してください。[Android][53]と[iOS][50]、[アプリ内メッセージs][34]、[コンテンツカード][40]。

高度なSDKインテグレーションオプションについては、[高度なインプリメンテーション][54]を参照してください。

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
\[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/
