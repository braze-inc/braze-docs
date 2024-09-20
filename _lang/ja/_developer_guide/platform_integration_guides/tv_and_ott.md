---
nav_title: TVとOTTの統合
article_title: TVとOTTの統合
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

> テクノロジーが新しいプラットフォームやデバイスに進化するにつれて、Brazeを使用したメッセージングも進化します！Brazeは、さまざまなTVオペレーティングシステムおよび「OTT」セットトップボックス向けに異なるエンゲージメントチャネルを提供しています。

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
            <th>デバイスタイプ</th>
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
            <td>アマゾンファイヤーTV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>キンドルファイア</td>
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
            <td>サムスンタイゼンテレビ</td>
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
          <td>アップルビジョンプロ</td>
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

特徴には以下が含まれます:

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- プッシュ通知（「ヘッズアップ通知」として知られる][7]）
  - これらが表示されるためには、優先度を「高」に設定する必要があります。すべての通知はFire TVの設定メニューに表示されます。
- コンテンツカード
- フィーチャーフラグ
- アプリ内メッセージ
  - タッチ非対応の環境（テレビなど）でHTMLメッセージを表示するには、`com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages`を`false`に設定します（\[Android SDK v23.1.0]\[android-tv-html]から利用可能）

詳細については、\[Fire OS 統合ガイド][2]をご覧ください。

### Kindle Fire {#kindle-fire}

Amazon Kindle Fireデバイスと統合するには、Braze Fire OS SDKを使用します。

特徴には以下が含まれます:

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- プッシュ通知
- コンテンツカード
- フィーチャーフラグ
- アプリ内メッセージ

詳細については、\[Fire OS 統合ガイド][2]をご覧ください。

### Android TV {#android-tv}

Braze Android SDK を使用して Android TV デバイスと統合します。

特徴には以下が含まれます:

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- コンテンツカード
- フィーチャーフラグ
- アプリ内メッセージ 
  - タッチ非対応の環境（テレビなど）でHTMLメッセージを表示するには、`com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages`を`false`に設定します（\[Android SDK v23.1.0]\[android-tv-html]から利用可能）
- プッシュ通知（手動統合が必要）
  - プッシュ通知はAndroid TVでネイティブにサポートされていません。理由を知るには、Googleの\[デザインガイドライン][5]をご覧ください。ただし、これを実現するには、**プッシュ通知UIの手動統合を行うことができます**。ドキュメント][6]の設定方法については、こちらをご覧ください。

詳細については、\[Android SDK 統合ガイド][2]をご覧ください。

{% alert note %}
ダッシュボードで新しいAndroidアプリを作成して、Android OTT統合を行ってください。
{% endalert %}

### LG webOS {#lg-webos}

Braze Web SDK を使用して [LG webOS テレビ](https://webostv.developer.lge.com/discover) と統合します。

特徴には以下が含まれます:

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- コンテンツカード（[Headless UI](#custom-ui)経由）
- フィーチャーフラグ
- アプリ内メッセージ（[Headless UI](#custom-ui)経由）

詳細については、\[Web Smart TV 統合ガイド][8]をご覧ください。

### サムスンタイゼン {#tizen}

Braze Web SDKを使用して[Samsung Tizen TV](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html)と統合します。

特徴には以下が含まれます:

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- コンテンツカード（[Headless UI](#custom-ui)経由）
- フィーチャーフラグ
- アプリ内メッセージ（[Headless UI](#custom-ui)経由）

詳細については、\[Web Smart TV 統合ガイド][8]をご覧ください。

### Roku {#roku}

Braze Roku SDKを使用して、[Rokuテレビ](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md)と統合します。

特徴には以下が含まれます:

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- アプリ内メッセージ（[Headless UI](#custom-ui)経由）
  - RokuプラットフォームではWebviewがサポートされていないため、アプリ内メッセージのHTMLはサポートされていません。
- フィーチャーフラグ

詳細については、\[Roku 統合ガイド][3]をご覧ください。

### Apple TV OS {#tvos}

tvOSと統合するにはBraze SWIFT SDKを使用します。覚えておいてください、SWIFT SDKにはtvOS用のデフォルトのUIやビューが含まれていないため、自分で実装する必要があります。

特徴には以下が含まれます:

- クロスチャネルのエンゲージメントのためのデータと分析の収集
- コンテンツカード（[Headless UI](#custom-ui)経由）
- フィーチャーフラグ
- アプリ内メッセージ（[Headless UI](#custom-ui)経由）
  - tvOSプラットフォームではWebviewがサポートされていないため、HTMLのアプリ内メッセージはサポートされていません。
  - tvOS でカスタマイズされたメッセージングのためのヘッドレス UI の使用方法について詳しく知るには、\[サンプルアプリ][9]をご覧ください。
- サイレントプッシュ通知と更新バッジ

詳細については、\[iOS SWIFT SDK 統合ガイド][4]をご覧ください。

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

詳細については、\[iOS SWIFT SDK 統合ガイド][4]をご覧ください。

{% alert important %}
一部のiOS機能は部分的にサポートされているか、サポートされていません。完全なリストについては、[visionOSサポート](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/visionos)を参照してください。
{% endalert %}

## アプリのターゲティング{#app-targeting}

メッセージングのためにOTTアプリをターゲットにするには、OTTアプリに特化したSegmentを作成することをお勧めします。

![Android OTTアプリを使用して作成されたセグメント。][1]

## ヘッドレスUI {#custom-ui}

{% alert important %}
アプリ内メッセージやコンテンツカードをヘッドレスUI経由でサポートするプラットフォームには、デフォルトのUIやビューが含まれていないため、独自のカスタムUIを実装してください。
{% endalert %}

ヘッドレスUIを使用すると、Brazeはアプリが読み取ってUI内で使用できるデータモデル（JSONなど）を提供します。このデータには、アプリが読み取って表示できるダッシュボード（タイトル、本文、ボタンテキスト、色など）に設定されたフィールドが含まれます。詳細な情報については、カスタム処理メッセージングをご覧ください。

**Android SDK**
- [アプリ内メッセージ カスタマイズ](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/)
- [コンテンツカードのカスタマイズ](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/)

**SWIFT SDK**
- [アプリ内メッセージ カスタマイズ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- ヘッドレスUIサンプルアプリ][9]
- [コンテンツカードのカスタマイズ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [アプリ内メッセージ カスタマイズ](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/in-app_messaging/customization/key_value_pairs)
- [コンテンツカードのカスタマイズ](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/)

[1]: {% image_buster /assets/img/android_ott.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/
[4]: https://github.com/braze-inc/braze-swift-sdk
[5]: https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/android_tv_push/
[7]: https://developer.amazon.com/docs/fire-tv/notifications.html#headsup
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/smart_tvs/
\[Android-tv-HTML]: https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310
[9]: https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui
