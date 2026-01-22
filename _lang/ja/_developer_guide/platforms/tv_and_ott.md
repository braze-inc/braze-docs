---
nav_title: テレビとOTT
article_title: Braze 用 TV と OTT の統合
page_order: 15

description: "この記事では、Braze TVおよびOTTの機能、統合、利用可能なプラットフォーム、その他の機能について詳しく説明します。"
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# TVとOTTの統合

> テクノロジーが新しいプラットフォームやデバイスに進化するにつれて、Brazeを使用したメッセージングも進化します！Braze は、さまざまなTV オペレーティングシステムおよび Over-the-Top (OTT) コンテンツ配信方法に対応した、さまざまなエンゲージメントチャネルを提供しています。

## プラットフォームと機能

以下は、今日サポートされている機能とメッセージングチャネルのリストです。

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center !important;
    vertical-align: center;
}

</style>
<table id="tv-feature-table">
    <thead>
        <tr>
            <th>デバイスのタイプ</th>
            <th>データと分析</th>
            <th>アプリ内メッセージ</th>
            <th>コンテンツカード</th>
            <th>プッシュ通知</th>
            <th>キャンバス</th>
            <th>フィーチャーフラグ</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LGテレビ（webOS）</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">該当なし</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">該当なし</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">該当なし</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
             <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>  
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
       <tr>
          <td>Apple Vision Pro</td>
          <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
           <td for="iam"><i class="fas fa-check text-success"></i></td>
          <td for="content-cards"><i class="fas fa-check text-success"></i></td>
          <td for="push"><i class="fa-solid fa-minus"></i></td>  
          <td for="canvas"><i class="fas fa-check text-success"></i></td>
          <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
      </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = サポートされている
- <i class="fa-solid fa-minus"></i> = 部分的なサポート
- <i class="fas fa-times text-warning"></i> = Brazeではサポートされていません
- N/A = OTTプラットフォームではサポートされていません

## 統合ガイド

### Amazon Fire TV {#fire-tv}

Amazon Fire TVデバイスと統合するには、Braze Fire OS SDKを使用します。

以下の機能があります。

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- プッシュ通知 ([[「ヘッドアップ通知」](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup)] とも呼ばれる)
  - これらが表示されるためには、優先度を「高」に設定する必要があります。すべての通知はFire TVの設定メニューに表示されます。
- コンテンツカード
- フィーチャーフラグ
- アプリ内メッセージ
  - TV などの非タッチ環境でHTML メッセージを表示するには、`com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` を`false` に設定します([Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310) から利用可能)。

詳細については、[Fire OS統合ガイド]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)を参照してください。

### Kindle Fire {#kindle-fire}

Amazon Kindle Fireデバイスと統合するには、Braze Fire OS SDKを使用します。

以下の機能があります。

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- プッシュ通知
- コンテンツカード
- フィーチャーフラグ
- アプリ内メッセージ

詳細については、[Fire OS統合ガイド]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)を参照してください。

### Android TV {#android-tv}

Braze Android SDK を使用して、Android TV デバイスと統合します。

以下の機能があります。

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- コンテンツカード
- フィーチャーフラグ
- アプリ内メッセージ 
  - TV などの非タッチ環境でHTML メッセージを表示するには、`com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` を`false` に設定します([Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310) から利用可能)。
- \* プッシュ通知 (手動での統合が必要)
  - プッシュ通知はAndroid TVでネイティブにサポートされていません。理由については、Googleの[デザインガイドライン](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html)を参照してください。ただし、これを実現するには、**プッシュ通知UIの手動統合を行うことができます**。この設定方法については、[documentation]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=android%20tv)を参照してください。

詳細については、[Android SDK 統合ガイド]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android)をご覧ください。

{% alert note %}
Android OTT 統合用に、ダッシュボードで新しい Android アプリを作成してください。
{% endalert %}

### LG webOS {#lg-webos}

Braze Web SDK を使用して [LG webOS テレビ](https://webostv.developer.lge.com/discover) と統合します。

以下の機能があります。

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- コンテンツカード ([ヘッドレス UI](#custom-ui) を使用)
- フィーチャーフラグ
- アプリ内メッセージ（[Headless UI](#custom-ui)経由）

詳細については、[Web Smart TV 統合ガイド]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/)をご覧ください。

### Samsung Tizen {#tizen}

Braze Web SDKを使用して[Samsung Tizen TV](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html)と統合します。

以下の機能があります。

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- コンテンツカード ([ヘッドレス UI](#custom-ui) を使用)
- フィーチャーフラグ
- アプリ内メッセージ（[Headless UI](#custom-ui)経由）

詳細については、[Web Smart TV 統合ガイド]({{site.baseurl}}/developer_guide/platforms/web/smart_tvs/)をご覧ください。

### Roku {#roku}

Braze Roku SDKを使用して、[Rokuテレビ](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md)と統合します。

以下の機能があります。

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- アプリ内メッセージ（[Headless UI](#custom-ui)経由）
  - RokuプラットフォームではWebviewがサポートされていないため、アプリ内メッセージのHTMLはサポートされていません。
- フィーチャーフラグ

詳細については、[[Roku 統合ガイド]({{site.baseurl}}/developer_guide/in_app_messages/?sdktab=roku)] をご覧ください。

### Apple TV OS {#tvos}

tvOSと統合するにはBraze SWIFT SDKを使用します。Swift SDK には tvOS のデフォルト UI やビューは含まれていないため、独自に実装する必要があります。

以下の機能があります。

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- コンテンツカード ([ヘッドレス UI](#custom-ui) を使用)
- フィーチャーフラグ
- アプリ内メッセージ（[Headless UI](#custom-ui)経由）
  - tvOS プラットフォームでは Web ビューはサポートされていないため、HTML アプリ内メッセージもサポートされていません。
  - tvOS でカスタマイズされたメッセージングにヘッドレスUI を使用する方法の詳細については、[sample app](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) を参照してください。
- サイレントプッシュ通知と更新バッジ

詳細については、[iOS Swift SDK 統合ガイド](https://github.com/braze-inc/braze-swift-sdk)をご覧ください。

{% alert note %}
TVユーザーにモバイルのアプリ内メッセージを表示しないようにするには、[アプリターゲティング](#app-targeting)を設定するか、キーと値のペアを使用してメッセージをフィルターしてください。例えば、特別な`tv = true`キーと値のペアが含まれている場合にのみtvOSメッセージを表示する。
{% endalert %}

### Apple Vision Pro {#vision-pro}

Braze SWIFT SDKを使用してvisionOSと統合します。iOSで利用可能なほとんどの機能は、visionOSでも利用可能です。これには次のものが含まれます:

- 分析（セッション、カスタムイベント、購入など）
- アプリ内メッセージング（データモデルとUI）
- コンテンツカード（データモデルとUI）
- プッシュ通知（ユーザーが見えるアクションボタン付きの通知とサイレント通知）
- フィーチャーフラグ
- ロケーション分析

詳細については、[iOS Swift SDK 統合ガイド](https://github.com/braze-inc/braze-swift-sdk)をご覧ください。

{% alert important %}
一部のiOS機能は部分的にサポートされているか、サポートされていません。完全なリストについては、[visionOSサポート](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/visionos)を参照してください。
{% endalert %}

## アプリのターゲット指定 {#app-targeting}

メッセージングに OTT アプリをターゲット指定する場合、その OTT アプリに固有のセグメントを作成することをお勧めします。

![Android OTTアプリを使用して作成されたセグメント。]({% image_buster /assets/img/android_ott.png %})

## ヘッドレス UI {#custom-ui}

{% alert important %}
ヘッドレス UI を介してアプリ内メッセージまたはコンテンツカードをサポートしているプラットフォームは、デフォルトの UI やビューは含まれて**いない**ため、独自のカスタム UI を実装してください。
{% endalert %}

ヘッドレス UI を使用して、Braze は、アプリが制御する UI 内でアプリが読み取り、使用できる JSON などのデータモデルを提供します。このデータには、ダッシュボードで設定されたフィールド (タイトル、本文、ボタンテキスト、色など) が含まれており、アプリはその設定に従ってそれらを読み取り、表示できます。メッセージングのカスタム処理の詳細については、以下を参照してください。

**Android SDK**
- [アプリ内メッセージ カスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android#android_setting-custom-manager-listeners)
- [コンテンツカードのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

**SWIFT SDK**
- [アプリ内メッセージ カスタマイズ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [ヘッドレス UI サンプルアプリ](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [コンテンツカードのカスタマイズ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [アプリ内メッセージ カスタマイズ]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web)
- [コンテンツカードのカスタマイズ]({{site.baseurl}}/developer_guide/content_cards/customizing_cards/style/)

