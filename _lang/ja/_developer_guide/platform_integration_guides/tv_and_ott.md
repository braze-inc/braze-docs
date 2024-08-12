---
nav_title: テレビとOTTの統合
article_title: テレビとOTTの統合
page_order: 15

description: "この記事では、Braze TVとOTTの機能、統合、利用可能なプラットフォーム、その他の機能について詳しく説明します。"
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
  
---

# テレビとOTTの統合

> テクノロジーが新しいプラットフォームやデバイスに進化するにつれて、Brazeでのメッセージングも進化します。<br><br>Brazeは、さまざまなTVオペレーティングシステムと「OTT」セットトップボックス向けに、さまざまなエンゲージメントチャネルを提供しています。

## プラットフォームと機能

以下に、現在サポートされている機能とメッセージング チャネルを示します。

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
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV対応</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire(キンドルファイア)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Androidのテレビ</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LGテレビ(webOS)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">該当なし</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>サムスンTizenテレビ</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">該当なし</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">該当なし</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Apple TVのOS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>  
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
        </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = サポート対象
- <i class="fa-solid fa-minus"></i> = 部分的なサポート
- <i class="fas fa-times text-warning"></i> = Brazeではサポートされていません
- N/A = OTTプラットフォームではサポートされていません

{% alert note %}
現在、OTT ではサポートされていません。
\- すぐに使えるアプリ内メッセージのスライドアップ
カスタム HTML
{% endalert %}

## 統合ガイド

### Amazon Fire TV対応 {#fire-tv}

Braze Fire OS SDKを使用して、Amazon Fire TVデバイスと統合します。

機能は次のとおりです。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- プッシュ通知 (["Heads Up Notifications"][7] と呼ばれる)
  - これらを表示するには、優先度を「HIGH」に設定する必要があります。すべての通知は、Fire TVの設定メニューに表示されます。
- コンテンツカード
- アプリ内メッセージ
  - テレビなどの非タッチ環境で HTML メッセージを表示するには、 `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` ( `false` [Android SDK v23.1.0][android-tv-html] から使用可能)

詳細については、[Fire OS統合ガイド][2]を参照してください。

### Kindle Fire(キンドルファイア) {#kindle-fire}

Braze Fire OS SDK を使用して、Amazon Kindle Fire デバイスと統合します。

機能は次のとおりです。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- プッシュ通知
- コンテンツカード
- アプリ内メッセージ

詳細については、[Fire OS統合ガイド][2]を参照してください。

### Androidのテレビ {#android-tv}

Braze Android SDKを使用して、Android TVデバイスと統合します。

機能は次のとおりです。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- コンテンツカード
- アプリ内メッセージ 
  - テレビなどの非タッチ環境で HTML メッセージを表示するには、 `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` ( `false` [Android SDK v23.1.0][android-tv-html] から使用可能)
- \*プッシュ通知(手動統合が必要)

詳細については、[Android SDK統合ガイド][2]を参照してください。

プッシュ通知は、Android TV ではネイティブにサポートされていません。その理由については、Googleの[デザインガイドライン][5]を参照してください。ただし、 **これを実現するには、プッシュ通知 UI を手動で統合**できます。この設定方法については、 [ドキュメント][6] を参照してください。

{% alert note %}
Android OTT統合用のダッシュボードで新しいAndroidアプリを作成してください。
{% endalert %}

### LGウェブOS {#lg-webos}

Braze Web SDKを使用して、 [LG webOS TV](https://webostv.developer.lge.com/discover)と統合します。

機能は次のとおりです。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- コンテンツ カード ( [ヘッドレス UI](#custom-ui) 経由)
- アプリ内メッセージ( [ヘッドレスUI](#custom-ui)経由)

詳細については、[Web Smart TV integration guide][8]をご覧ください。

### サムスンTizen {#tizen}

Braze Web SDK を使用して、 [Samsung Tizen TV](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html) と統合します。

機能は次のとおりです。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- コンテンツ カード ( [ヘッドレス UI](#custom-ui) 経由)
- アプリ内メッセージ( [ヘッドレスUI](#custom-ui)経由)

詳細については、[Web Smart TV integration guide][8]をご覧ください。

### Roku {#roku}

Braze Roku SDKを使用して[Roku TV](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md)と統合する

機能は次のとおりです。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- アプリ内メッセージ( [ヘッドレスUI](#custom-ui)経由)
  - Webview は Roku プラットフォームではサポートされていないため、HTML アプリ内メッセージはサポートされていません。

詳細については、[Roku統合ガイド][3]をご覧ください。

### Apple TVのOS {#tvos}

Braze Swift SDKを使用してtvOSに統合する

詳細については、[iOS Swift SDK統合ガイド][4]を参照してください。

機能は次のとおりです。

- クロスチャネルエンゲージメントのためのデータと分析の収集
- コンテンツ カード ( [ヘッドレス UI](#custom-ui) 経由)
- アプリ内メッセージ( [ヘッドレスUI](#custom-ui)経由)
  - Webview は tvOS プラットフォームではサポートされていないため、HTML アプリ内メッセージはサポートされていません。
  - tvOS でカスタマイズされたメッセージングにヘッドレス UI を使用する方法の詳細については、[サンプル アプリ][9] を参照してください。
- サイレントプッシュ通知と更新バッジ

**Note**:テレビユーザーにモバイルアプリ内メッセージが表示されないようにするには、 [アプリターゲティング](#app-targeting) を設定するか、キーと値のペアを使用してメッセージを除外してください。たとえば、tvOS メッセージに特別な `tv = true` キーと値のペアが含まれている場合にのみ表示します。

## アプリのターゲティング {#app-targeting}

OTTアプリをメッセージングのターゲットに設定するには、OTTアプリ専用のセグメントを作成することをおすすめします。

![Android OTTアプリを使用して作成されたセグメント。[1]

## ヘッドレス UI {#custom-ui}

ヘッドレスUIを介してアプリ内メッセージやコンテンツカードをサポートするプラットフォームの場合、Brazeは、アプリが制御するUI内でアプリが読み取って使用できるJSONなどのデータモデルを提供します。これらのプラットフォームには、既定の UI やビューは含まれていません。

このデータには、ダッシュボードで構成されたフィールド (タイトル、本文、ボタン テキスト、色など) が含まれ、アプリはそれに応じて読み取って表示できます。

カスタム処理メッセージングの詳細については、以下を参照してください。

**アンドロイドSDK**
- [アプリ内メッセージのカスタマイズ](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/)
- [コンテンツカードのカスタマイズ](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/)

**スウィフトSDK**
- [アプリ内メッセージのカスタマイズ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
\- [ヘッドレスUIサンプルアプリ][9]
- [コンテンツカードのカスタマイズ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [アプリ内メッセージのカスタマイズ](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/in-app_messaging/customization/key_value_pairs)
- [コンテンツカードのカスタマイズ](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/)
 

[1]: {% image_buster /assets/img/android_ott.png %}
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[3]: {{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/
[4]: https://github.com/braze-inc/braze-swift-sdk
[5]: https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html
[6]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/android_tv_push/
[7]: https://developer.amazon.com/docs/fire-tv/notifications.html#headsup
[8]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/smart_tvs/
[android-tv-html]:https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310
[9]: https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui
