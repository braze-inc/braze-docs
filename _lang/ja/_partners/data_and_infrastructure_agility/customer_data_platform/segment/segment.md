---
nav_title: セグメント
article_title: セグメント
page_order: 1
alias: /partners/segment/
description: "この参考記事では、BrazeとSegmentのパートナーシップについて概説している。Segmentは、マーケティング・スタックのソース間で情報を収集し、ルーティングする顧客データ・プラットフォームである。"
page_type: partner
search_tag: Partner

---

# セグメント

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment][5] は、顧客データの収集、クリーンアップ、およびアクティブ化を支援する顧客データプラットフォームです。 

Braze と Segment の統合により、ユーザーを追跡し、さまざまなユーザー分析プロバイダーにデータを転送できます。Segment では次の操作を行うことができます。

- Braze キャンペーンとキャンバスセグメンテーションで使用するために、[Segment Engage]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_engage/)を Braze に同期する。
- [2つのプラットフォームの間でデータをインポートする](#integration-options)。Android、iOS、および Web アプリケーション用のサイドバイサイド SDK 統合と、Braze の REST API にデータを同期するサーバー間統合を提供しています。
- [カレントを介してデータをセグメントに接続する]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/)。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Segment アカウント | このパートナーシップを活用するには、[Segment アカウント](https://app.segment.com/login)が必要です。 |
| インストールされたソースと Segment ソースの[ライブラリ](https://segment.com/docs/sources/) | モバイルアプリ、Web サイト、バックエンドサーバーなど、Segment に送信されるデータの提供元。<br><br>適切な `Source > Destination` フローを設定できるようにするには、ライブラリをアプリ、サイト、サーバーにインストールしておく必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

BrazeとSegmentを統合するには、[選択した統合タイプ](#integration-options)（接続モード）に従って、[Brazeを接続先に](#connection-settings)設定する必要がある。Brazeの新規顧客であれば、[セグメントリプレイを使って](#segment-replays)過去のデータをBrazeにリレーすることができる。次に、Braze と Segment 間のスムーズなデータフローを確保するために、[マッピング](#methods)を設定し、[統合をテスト](#step-4-test-your-integration)する必要があります。

### ステップ1:Braze 宛先を作成する {#connection-settings}

ソースの設定が完了したら、各ソース (iOS、Android、Web など) の[宛先](https://segment.com/docs/destinations/)として Braze を設定する必要があります。接続設定を使用して、BrazeとSegment間のデータフローをカスタマイズする多くのオプションがある。

### ステップ2:宛先フレームワークと接続タイプを選択する {#integration-options}

Segment で、[**送信先**] > [**Braze**] > [**Braze 設定**] > [**ソースを選択**] > [**設定**] と移動します。

![ソースの設定ページ。このページでは、宛先フレームワークを [Actions] または [Classic] のいずれかに設定し、接続モードを [Cloud mode] または [Device mode] のいずれかに設定します。][42]

Segment のWeb ソース (Analytics.js) およびネイティブクライアントサイドライブラリは、サイドバイサイド (デバイスモード) 統合またはサーバー間 (クラウドモード) 統合のいずれかを使用して、Braze と統合できます。

選択する接続モードは、宛先が設定されているソースのタイプによって決まります。

| 統合 | 詳細 |
| ----------- | ------- |
| [サイドバイサイド<br>(デバイスモード)](#side-by-side-sdk-integration) |Segment の SDK を使用して、イベントを Braze のネイティブ呼び出しに変換します。これにより、サーバー間統合よりも高度な機能を利用できるため、Braze をより包括的に使用できるようになります。<br><br>Segmentは、すべてのBrazeメソッド（例えば、Content Cards）をサポートしているわけではない。対応するマッピングを通してマッピングされていないBrazeメソッドを使用するには、コードベースにネイティブのBrazeコードを追加してメソッドを呼び出す必要がある。 |
| [サーバー間<br>(クラウドモード)](#server-to-server-integration) | SegmentからBraze REST APIエンドポイントにデータを転送する。<br><br>アプリ内メッセージ、コンテンツカード、プッシュ通知などのBraze UI機能には対応していない。また、この方法では利用できないデバイスレベルのフィールドなど、自動的に取得されるデータも存在します。<br><br>これらの機能を使いたい場合は、サイド・バイ・サイドの統合を検討しよう。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
2つの統合オプション（接続モード）について、それぞれの利点を含め、詳しくは[セグメントを](https://segment.com/docs/destinations/#connection-modes)ご覧いただきたい。
{% endalert %}

#### サイドバイサイドの SDK 統合

デバイスモードとも呼ばれるこの統合では、Segment の SDK と[メソッド](#methods)が Braze SDK にマッピングされます。これにより、Braze の SDK が提供するすべての機能 (プッシュ、アプリ内メッセージング、その他の Braze ネイティブのメソッドなど) にアクセスできるようになります。 

{% alert note %}
Segment のデバイスモードを使用する場合、Braze SDK を直接統合する必要はありません。Segment のデバイスモードの宛先として Braze を追加する場合、Segment SDK は Braze SDK を初期化し、関連するマッピングされた Braze メソッドを呼び出します。
{% endalert %}

デバイスモード接続を使用する場合、Braze SDK をネイティブに統合する場合と同様に、Braze SDK はすべてのユーザーに `device_id` とバックエンド識別子 `braze_id` を割り当てます。これにより Braze は、`userId` の代わりにこれらの識別子を照合することで、デバイスからの匿名アクティビティを取得できます。 

{% tabs ローカル %}
{% tab Android %}

{% alert important %}
Androidデバイスモード統合のソースコードは、Brazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新される。

<br>
使用する Braze SDKは、使用する Segment SDK によって異なります。

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| 優先 | [Analytics-Kotlin](https://github.com/segmentio/analytics-kotlin) | [Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin) |
| レガシー｜[Analytics-Android](https://github.com/segmentio/analytics-android)｜[Braze Segment Android](https://github.com/braze-inc/braze-segment-android)｜
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


{% endalert %}

Braze を Android ソースのデバイスモード送信先として設定するには、**送信先フレームワーク**として [**アクション**] を選択してから、[**保存**] を選択します。 

サイドバイサイドの統合を完了するには、[Android](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/)アプリにBrazeのデスティネーション依存性を追加するためのSegmentの詳細な手順を参照する。

[Androidデバイスモード](https://github.com/braze-inc/braze-segment-kotlin)統合のソースコードは、Brazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新される。

{% endtab %}
{% tab iOS %}

{% alert important %}
iOSデバイスモード統合のソースコードは、Brazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新される。

<br>
使用する Braze SDKは、使用する Segment SDK によって異なります。

| | Segment SDK | Braze SDK |
| - | ----------- | --------- |
| 優先 | [Analytics-Swift](https://github.com/segmentio/analytics-swift) | [Braze Segment Swift](https://github.com/braze-inc/braze-segment-swift) |
| レガシー｜[Analytics-iOS](https://github.com/segmentio/analytics-ios)｜[Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios)｜
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
{% endalert %}

Braze を iOS ソースのデバイスモード送信先として設定するには、**送信先フレームワーク**として [**アクション**] を選択してから、[**保存**] を選択します。 

サイドバイサイドの統合を完了するには、[iOS](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/)アプリにBraze Segmentポッドを追加するためのSegmentの詳細な手順を参照する。

[iOSデバイスモード](https://github.com/braze-inc/braze-segment-swift)統合のソースコードは、Brazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新される。

{% endtab %}
{% tab ウェブまたはJavaScript %}

Web ソースのデバイスモード送信先として Braze を設定する場合は、Segment の Braze Web モード (アクション) フレームワークが推奨されます。 

Segment で、送信先フレームワークとして [**アクション**] を選択し、接続モードとして [**デバイスモード**] を選択します。

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
[React Native Braze プラグイン](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze)のソースコードは Segment によって管理されており、新しい Braze SDK リリースを反映するために定期的に更新されます。

React Native Segment ソースを Braze に接続する場合は、オペレーティングシステムごとにソースと宛先を設定する必要があります。たとえば、iOS の宛先と Android の宛先を設定します。 

アプリのコードベース内で、各アプリに関連付けられたそれぞれのソース書き込みキーを使用して、デバイスタイプ別にSegment SDKを条件付きで初期化する。

デバイスからプッシュトークンが登録され、Brazeに送信されると、SDKの初期化時に使用されたアプリ識別子に関連付けられる。デバイスタイプの条件付き初期化は、Brazeに送信されるプッシュトークンが関連アプリに関連付けられていることを確認するのに役立つ。

{% alert important %}
React Native アプリがすべてのデバイスで同じ Braze アプリ識別子を使用して Braze を初期化する場合、すべての React Native ユーザーは Braze で Android ユーザーまたは iOS ユーザーとみなされ、すべてのプッシュトークンはそのオペレーティングシステムに関連付けられます。
{% endalert %}

Braze を各ソースのデバイスモード送信先として設定するには、**送信先フレームワーク**として [**アクション**] を選択してから、[**保存**] を選択します。

{% endtab %}
{% endtabs %}

#### サーバー間統合

クラウドモードとも呼ばれるこの統合は、Segment から Braze の REST API にデータを転送します。Segment の [Braze クラウドモード (アクション)](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/) フレームワークを使用して、任意のソースにクラウドモードの送信先を設定します。 

サイドバイサイドの統合とは異なり、サーバー間の統合では、アプリ内メッセージング、コンテンツカード、自動プッシュトークン登録などの Braze UI 機能はサポートされません。また、クラウドモードでは利用できない[自動取得]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection)データ（匿名ユーザーやデバイスレベルのフィールドなど）も存在する。

このデータとこれらの機能を使用したい場合は、サイド・バイ・サイド（デバイスモード）SDK統合の使用を検討すること。

[Braze Cloud Mode (Actions) destination](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze) のソースコードは Segment によって管理されています。

### ステップ3:設定

宛先の設定を定義します。すべての設定がすべての宛先タイプに適用されるわけではありません。

{% tabs ローカル %}
{% tab Mobile Device-Mode %}

| セッティング | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。これは、Braze ダッシュボードの [**設定の管理**] で確認できます。 | 
| カスタムAPIエンドポイント<br>(SDKエンドポイント） | インスタンスに対応するBraze SDKエンドポイント（`sdk.iad-01.braze.com` など） | 
| Endpoint region | あなたのBrazeインスタンス（US 01、US 02、EU 01など） | 
| Enable automatic in-app message registration | アプリ内メッセージを手動で登録したい場合は、これを無効にする。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Web Device-Mode %}

| セッティング | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。これは、Braze ダッシュボードの [**設定の管理**] で確認できます。 | 
| カスタムAPIエンドポイント<br>(SDKエンドポイント） | インスタンスに対応するBraze SDKエンドポイント（`sdk.iad-01.braze.com` など） | 
| Safari website push ID | Safariプッシュをサポートしている場合、Safariプッシュ証明書を作成する際にAppleに提供したWebサイトプッシュID（`web` で始まる、たとえば、`web.com.example.domain` ）をこのオプションに指定する必要がある。 |
| Braze Web SDKバージョン | 使用したいBraze Web SDKのバージョン |
| アプリ内メッセージを自動送信する | デフォルトでは、ユーザーが受信できるすべてのアプリ内メッセージは、自動的にユーザーに配信されます。アプリ内メッセージを手動で表示したい場合は、これを無効にする。 |
| Do not load font awesome | Brazeはアプリ内のメッセージアイコンにFont Awesomeを使用している。デフォルトでは、Brazeは自動的にFontAwesome CDNからFontAwesomeを読み込む。この動作を無効にするには（例えば、あなたのサイトが FontAwesome のカスタマイズ版を使用しているため）、このオプションを`TRUE` に設定する。これを行う場合、FontAwesomeがあなたのサイトにロードされていることを確認する責任があることに注意すること - そうでない場合、アプリ内メッセージが正しくレンダリングされない可能性がある。 |
| HTMLアプリ内メッセージを有効にする | このオプションを有効にすると、Braze ダッシュボードのユーザーが HTML アプリ内メッセージを使用できるようになります。 | 
| アプリ内のメッセージを新しいタブで開く | デフォルトでは、アプリ内メッセージでクリックしたリンクは、現在のタブまたは新しいタブに読み込まれます。どちらのタブになるかは、ダッシュボードでメッセージごとに指定されています。このオプションを`TRUE` に設定すると、アプリ内メッセージのクリックによるすべてのリンクが新しいタブまたはウィンドウで強制的に開かれる。 |
| アプリ内メッセージzインデックス | このオプションに値を指定して Braze のデフォルトの z-index をオーバーライドします。 | 
| Require explicit in-app message dismissal | デフォルトでは、アプリ内メッセージが表示されている場合、エスケープボタンを押すか、ページのグレーアウトした背景をクリックすると、メッセージが表示されなくなる。このオプションをtrueに設定すると、この動作を防ぎ、メッセージを解除するために明示的なボタンクリックを要求する。 |
| トリガーアクションの最小間隔（秒 | デフォルトは30です。<br>デフォルトでは、トリガーアクションは、前回のトリガーアクションから30秒以上が経過した場合にのみ実行されます。デフォルトを各自の値でオーバーライドするには、この設定オプションに値を指定します。ユーザーへのスパム通知を避けるため、この値を10より小さくすることは推奨しない。|
| サービス従業員の所在地 | デフォルトでは、Webプッシュ通知のためにユーザーを登録するとき、Brazeは、Webサーバーのルートディレクトリの`/service-worker.js` にある必要なサービスワーカーファイルを探す。サーバー上の別のパスでサービスワーカーをホストする場合は、このオプションにファイルの絶対パスを指定します (例: `/mycustompath/my-worker.js`)。ここで値を設定すると、サイトでのプッシュ通知の範囲が制限されることに注意してください。たとえば上記の例では、サービスワーカーファイルは `/mycustompath/` ディレクトリ内にあるため、`requestPushPermission` は`http://yoursite.com/mycustompath/` で始まる Web ページからのみ呼び出すことができます。 |
| プッシュトークンのメンテナンスを無効にする | デフォルトでは、確実に配信されるようにするため、すでに Web プッシュ通知の権限が付与されているユーザーが、新しいセッションでプッシュトークンを Braze バックグラウンドと自動的に同期します。この動作を無効にするには、このオプションを`FALSE` に設定する。 |
| Manage service worker externally | 登録し、ライフサイクルを制御する独自のサービスワーカーがある場合、このオプションを`TRUE` に設定すると、Braze SDKはサービスワーカーを登録または登録解除しない。このオプションを `TRUE` に設定した場合にプッシュを正しく機能させるには、`requestPushPermission` を呼び出す前にサービスワーカーを自身で登録し、`self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` を使うか、そのファイルの内容を直接含めることで、Braze サービスワーカーのコードが確実に含まれるようにする必要があります。このオプションが`TRUE` の場合、`serviceWorkerLocation` オプションは無関係であり、無視される。 |
| Content security nonce | このオプションに値を指定すると、Braze SDK によって作成されたすべての `<script>` 要素と`<style>` 要素に nonce が追加されます。これにより Braze SDK は、Web サイトのコンテンツセキュリティポリシーを処理できるようになります。この nonce の設定に加えて、FontAwesome の読み込みを許可する必要があります。このためには、コンテンツセキュリティポリシー許可リストに `use.fontawesome.com` を追加するか、または `doNotLoadFontAwesome` オプションを使用して手動で読み込みます。 |
| クローラーの活動を許可する | デフォルトでは、Braze Web SDK はエージェント文字列に基づいて、Google などの既知のスパイダーや Web クローラーからのアクティビティを無視します。これによりデータポイントを節約でき、分析がより正確になり、またページランクが向上する可能性があります。ただし、Braze にこれらのクローラーからのアクティビティを記録させる場合には、このオプションを `TRUE` に設定します。 |
| ロギングを有効にする | デフォルトでロギングを有効にするには、`TRUE` に設定します。これにより Braze は、すべてのユーザーに対して表示される JavaScript コンソールにログを記録することに注意してください。ページを本番環境にリリースする前にこれを削除するか、`setLogger` で代替ロガーを指定する必要があります。 |
| ニュースフィードのカードを新しいタブで開く（新しいタブでカードを開く） | デフォルトでは、カード・オブジェクトからのリンクは現在のタブまたはウィンドウに読み込まれる。カードからのリンクを新しいタブまたはウィンドウで開くようにするには、このオプションを`TRUE` に設定する。<br><br>**注:**ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。 |
| ユーザー提供のJavaScriptを許可する | デフォルトでは、Braze Web SDK は、ユーザー提供の JavaScript クリックアクションを許可しません。これは、このアクションにより、Braze ダッシュボードのユーザーがサイトで JavaScript を実行できるようになるためです。Brazeダッシュボードのユーザーが悪意のないJavaScriptクリックアクションを記述することを信頼することを示すには、このプロパティを`TRUE` に設定する。`enableHtmlInAppMessages` が`TRUE` の場合、このオプションも`TRUE` に設定されます。 |
| App version| このオプションに値を指定すると、Brazeに送信されたユーザーイベントは、指定したバージョンに関連付けられ、ユーザーセグメンテーションに使用できる。 |
| セッションタイムアウト（秒 | デフォルトは30です。<br>デフォルトでは、セッションは30分間操作がないとタイムアウトする。デフォルトを各自の値でオーバーライドするには、この設定オプションに値を指定します。 | 
| Device property allowlist | デフォルトでは、Braze SDK は `DeviceProperties` のすべてのデバイスプロパティを自動的に検出して収集します。この動作をオーバーライドするには、`DeviceProperties` の配列を指定する。いくつかのプロパティがないと一部の機能が正しく機能しないことがあるので注意してください。たとえば、ローカルタイムゾーンの配信はタイムゾーンなしでは機能しません。 |
| ローカライゼーション | デフォルトでは、SDK により生成されたユーザーに対して表示されるメッセージはすべて、ユーザーのブラウザーで設定されている言語で表示されます。その動作をオーバーライドして特定の言語を強制するには、このオプションに値を指定する。このオプションの値は ISO 639-1言語コードでなければなりません。 |
| クッキーなし | デフォルトでは、Braze SDKは少量のデータ（ユーザーID、セッションID）をクッキーに保存する。これは、Brazeがサイトの異なるサブドメイン間でユーザーとセッションを認識できるようにするためである。これで問題が発生する場合は、このオプションに `TRUE` を渡して Cookie の保存を無効にし、HTML 5 localStorage のみを使用してユーザーとセッションを識別します。 |
| すべてのページを追跡する | **Classic Destination Web Device-Mode (メンテナンス) のみ**<br><br>Segment は、この設定を Web Actions フレームワーク宛先に移行することを推奨しています。Web Actions フレームワーク宛先では、この設定を[マッピングによって有効にできます](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)。<br><br>これにより、すべての[ページ呼び出し](https://segment.com/docs/spec/page/)が "Loaded/Viewed a Page "イベントとして Braze に送信されます。 |
| 指定されたページのみを追跡する | **Classic Destination Web Device-Mode (メンテナンス) のみ**<br><br>Segment は、この設定を Web Actions フレームワーク宛先に移行することを推奨しています。Web Actions フレームワーク宛先では、この設定を[マッピングによって有効にできます](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)。<br><br>これにより、ページ呼び出しとそれに関連付けられている名前のみが Braze に送信されます。 |
| Log purchase when revenue is present | **Classic Destination Web Device-Mode (メンテナンス) のみ**<br><br>Segment は、この設定を Web Actions フレームワーク宛先に移行することを推奨しています。Web Actions フレームワーク宛先では、この設定を[マッピングによって有効にできます](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)。<br><br>このオプションを有効にすると、収益プロパティを持つすべてのTrackコールが購入イベントをトリガーする。 | 
| 既知のユーザーのみを追跡する | **Classic Destination Web Device-Mode (メンテナンス) のみ**<br><br>Segment は、この設定を Web Actions フレームワーク宛先に移行することを推奨しています。Web Actions フレームワーク宛先では、この設定をマッピングによって有効にできます。<br><br>有効にすると、この新しい設定により、有効な`userId` が存在するまで `window.appboy.initialize` の呼び出しが遅延します。 | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Cloud-Mode %}

| セッティング | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。これは、Braze ダッシュボードの [**設定の管理**] で確認できます。 | 
| REST APIキー | これは、Brazeダッシュボードの**「設定」**>「**APIキー**」で確認できる。 | 
| カスタムREST APIエンドポイント | インスタンスに対応するBraze RESTエンドポイント（rest.iad-01.braze.com など）。 | 
| 既存ユーザーのみを更新する | **Classic Destination Cloud-Mode (メンテナンス) のみ**<br><br>Segment は、この設定を Cloud Actions フレームワーク宛先に移行することを推奨しています。Cloud Actions フレームワーク宛先では、この設定を[マッピングによって有効にできます](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)。<br><br>既存のユーザーのみを更新するかどうかを決定する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

### ステップ4:メソッドをマッピングする {#methods}

Brazeは、[Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page)メソッド、[Identify](https://segment.com/docs/spec/identify/)メソッド、[Track](https://segment.com/docs/spec/track/)Segmentメソッドをサポートしている。これらのメソッドで使用される識別子の種類は、データがサーバー間統合 (cloud-mode) で送信されるのか、サイドバイサイド (device-mode) で送信されるのかによって異なります。Braze Web Mode Actions 宛先と Cloud Mode Actions 宛先では、[Segment エイリアス呼び出し](https://segment.com/docs/connections/spec/alias/)のマッピングを設定することもできます。 

{% alert note %}
ユーザーエイリアスは、Braze Cloud Mode (Actions) 宛先の識別子としてサポートされていますが、Segment のエイリアス呼び出しは、Braze ユーザーエイリアスとは直接関係ないことに注意してください。
{% endalert %}

| 識別子タイプ | サポートされている宛先 |
| --------------- | --------------------- |
| `userId` (`external_id`) | すべて |
| 匿名ユーザー | Device mode の宛先 |
| ユーザーエイリアス | Cloud mode の宛先 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Cloud Mode (Actions) 宛先にある [Create Alias アクション](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias)を使用して、エイリアスのみのユーザーを作成したり、既存の `external_id` プロファイルにエイリアスを追加したりできます。[ユーザーの識別（Identify User）アクションは](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user)、エイリアスの作成（Create Alias）アクションと並行して使用することができ、そのユーザーが使用可能になった後、エイリアスのみのユーザーを`external_id` 。 

回避策を考案し`braze_id` を使用して cloud-mode で匿名ユーザーのデータを送信することもできます。そのため、すべてのSegment APIコールにユーザーの`braze_id` を手動で含める必要がある。この回避策の設定方法については、[Segmentのドキュメントを](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users)参照されたい。

Braze に送信される宛先データは、Cloud Mode Actions 内でバッチ処理できます。バッチサイズの上限は75イベントであり、これらのバッチはフラッシュされる前に30秒間蓄積される。リクエストのバッチ処理はアクションごとに実行されます。たとえば、Identify Calls (属性) が1つのリクエストでバッチ処理され、Track Calls (カスタムイベント) が2番目のリクエストでバッチ処理されます。SegmentからBrazeに送信されるリクエストの数を減らすことができるため、Brazeはこの機能を有効にすることを推奨している。その結果、宛先が Braze のレート制限に達してリクエストを再試行するリスクが減少します。 

[Braze Destination] > [**Mappings**] に移動して、アクションのバッチ処理をオンにできます。そこから、マッピングの右側にある3つのドットのアイコンをクリックし、[**Edit Mapping**] を選択します。**Select mappings**セクションの一番下までスクロールし、**Batch Data to Brazeが** **Yesに**設定されていることを確認する。


{% tabs ローカル %}
{% tab Identify %}
#### 特定する

[Identify](https://segment.com/docs/spec/identify/)コールは、ユーザーをその行動に結びつけ、そのユーザーに関する属性を記録することができる。 

特定のセグメント特殊特性は、Brazeの標準的な属性プロファイルフィールドにマッピングされる：

| Segment の特別な特性 | Braze の標準属性項目 |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

`email_subscribe` や `push_subscribe` などのその他の予約済み Braze プロファイルフィールドを送信するには、これらのフィールドに Braze 命名規則を使用して、identify 呼び出しでこれらを特性として渡します。

##### サブスクリプショングループにユーザーを追加する

traits パラメータの以下のフィールドを使用して、指定されたサブスクリプショングループからユーザーをサブスクライブまたはアンサブスクライブすることもできる。

`braze_subscription_groups` という予約済みの Braze プロファイルフィールドを使用します。このフィールドは、オブジェクト配列に関連付けることができます。配列の各オブジェクトに2つの予約キーが含まれている必要があります。

1. `subscription_group_state`:特定のサブスクリプショングループに対してユーザーが `"subscribed"` または`"unsubscribed"` のいずれであるかを示します。
2. `subscription_group_id`:サブスクリプショングループの一意の ID を表す。この ID は、Braze ダッシュボードの [**サブスクリプショングループ管理**] で確認できます。

{% subtabs %}
{% subtab Swift %}
```swift
analytics.identify(
  userId: "{your-user}",
  traits: [
    "braze_subscription_groups": [
      [
        "subscription_group_id": "{your-group-id}",
        "subscription_group_state": "subscribed"
      ],
      [
        "subscription_group_id", "{your-group-id}",
        "subscription_group_state": "unsubscribed"
      ]
    ]
  ]
)
```
{% endsubtab %}
{% subtab Kotlin %}
```kotlin
analytics.identify(
  "{your-user}",
  buildJsonObject {
    put("braze_subscription_groups", buildJsonArray {
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "subscribed")
          }
        )
        add(
          buildJsonObject {
            put("subscription_group_id", "{your-group-id}")
            put("subscription_group_state", "unsubscribed")
          }
        )
      }
    )
  }
)
```
{% endsubtab %}
{% subtab TypeScript %}
```typescript
analytics.identify(
  "{your-user}",
  {
    braze_subscription_groups: [
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "subscribed"
      },
      {
        subscription_group_id: "{your-group-id}",
        subscription_group_state: "unsubscribed"
      }
    ]
  }
)
```
{% endsubtab %}
{% endsubtabs %}

##### カスタム属性

その他の特徴はすべて[カスタム属性として]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)記録される。

| Segment での方法 | Braze での方法 | 例 |
|---|---|---|
| ユーザーIDで識別する | 外部IDを設定する | Segment:  `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| 予約済み特性で識別する | ユーザー属性を設定する | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| カスタム特性で識別する | カスタム属性を設定する | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| ユーザー ID と特性で識別する | Segment:external ID と属性を設定する | 先の方法を組み合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) 宛先と [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile) 宛先では、Update User Profile Action を使用して前述のマッピングを設定できます。

{% alert important %}
ユーザー属性データを渡すときは、前回の更新以降に変更された属性の値のみを渡すようにする。こうすることで、データポイントを不必要に消費することがなくなります。クライアントサイドのソースについては、Segment のオープンソース [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) ツール使用して統合を最適化し、Segment からの重複した `identify()` 呼び出しをデバウンスすることで、データポイント使用量を制限します。 

{% endalert %}
{% endtab %}

{% tab Track %}
#### Track

あなたがイベントを追跡するとき、私たちは提供された名前を使用して[カスタムイベントとして]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)そのイベントを記録する。 

トラックコールのプロパティオブジェクト内で送信されたメタデータは、関連イベントのカスタムイベントプロパティとしてBrazeに記録される。すべての[カスタムイベントプロパティデータタイプが]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)サポートされている。

[Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) 宛先と [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event) 宛先では、Track Event Action を使用して前述のマッピングを設定できます。

| Segment での方法 | Braze での方法 | 例 |
|---|---|---|
| [追跡](https://segment.com/docs/spec/track/) | [カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)として記録される | Segment: `analytics.track("played_game");`<br>Braze: `Braze.logCustomEvent("played_game");`|
| [プロパティを使用した追跡](https://segment.com/docs/spec/track/) | [イベントプロパティ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)として記録される | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});`<br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [製品を使用した追跡](https://segment.com/docs/spec/track/) | [購入イベント]({{site.baseurl}}/developer_guide/analytics/logging_purchases/?tab=web)として記録される。 | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});`<br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

##### 注文完了 {#order-completed}

Segment の [eCommerce API ](https://segment.com/docs/spec/ecommerce/v2/)で記述されているフォーマットを使用して、`Order Completed` という名前のイベントを追跡すると、[購入]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data)としてリストアップされた商品が記録されます。

[Web Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) 宛先と [Cloud Mode Actions](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase) 宛先では、Track Purchase Action でデフォルトのマッピングをカスタマイズできます。

{% endtab %}

{% tab ページ %}
#### ページ {#page}

[Page](https://segment.com/docs/spec/page/)コールは、ユーザーがあなたのウェブサイトのページを見るたびに、ページに関するオプションのプロパティとともに記録することができる。

このイベントタイプを、Web Mode Actions 宛先と Cloud Actions 宛先でトリガーとして使用して、カスタムイベントを Braze に記録することができます。
{% endtab %}

{% endtabs %}

### ステップ 5: 連携のテスト

サイドバイサイド（デバイスモード）統合を使用する場合、[概要][27]メトリクス（ライフタイムセッション、MAU、DAU、スティッキネス、デイリーセッション、MAUあたりのデイリーセッション）を使用して、BrazeがSegmentからデータを受信していることを確認できる。

[カスタムイベント][22]ページまたは[収益][28]ページでデータを確認するか、または[セグメントを作成する][23]ことでデータを確認できます。ダッシュボードの**カスタム・イベント**・ページでは、カスタム・イベントのカウントを時系列で見ることができる。サーバー間（クラウドモード）統合を使用している場合、MAUとDAU統計を含む[計算式を][24]使用することはできないことに注意。

Braze に購入データを送信する場合 ([ステップ3](#methods) の「**Track**」タブの「Ｏｒｄｅｒ Completed」を参照)、[収益][28]ページで特定の期間の収益や購入に関するデータ、またはアプリの総収益を確認できます。

[セグメントを作成すること][26]で、カスタムイベントと属性データに基づいてユーザーをフィルタリングすることができる。

{% alert important %}
サーバー間統合 (cloud-mode) を使用する場合、自動的に収集されたセッションデータに関連するフィルター (「最初に使用したアプリ」や「最後に使用したアプリ」など) は機能しません。Segment とBraze の統合でこれらを使用する場合は、サイドバイサイド統合 (デバイスモード) を使用してください。
{% endalert %}

## ユーザーの削除と抑制 

ユーザーを削除または抑制する必要がある場合は、[Segment のユーザー削除機能](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to)**が** Braze [`/users/delete` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)にマッピングされていることに注意してください。これらの削除の検証には最大30日かかる可能性があることに注意してほしい。

(`external_id` と同様に) Braze と Segment の間で共通のユーザー識別子を選択する必要があります。Segment で削除リクエストを開始した後は、Segment ダッシュボードの削除リクエストのタブでステータスを確認できます。

## Segment のリプレイ機能

Segment は、新しいテクノロジーパートナーに対してすべての履歴データを「再生」するサービスをクライアントに提供しています。関連するすべての履歴データをインポートすることを望む Braze の新しいお客様は、Segment を介してインポートできます。この機能に興味がある場合は Segment の担当者にお問い合わせください。

Segmentが当社の[`/users/track` エンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)接続し、ユーザーに代わってBrazeにユーザーデータをインポートする。

{% alert important %}
Cloud Mode Actions 宛先でサポートされているすべての識別子は、Segment のリプレイの一部としてサポートされています。
{% endalert %}

## ベストプラクティス

{% details データ超過を避けるために使用例を見直す。 %}

Segment では、クライアントが送信できるデータエレメントの数は制限**されていません**。セグメントを使えば、すべてのイベントをBrazeに送ることも、どのイベントを送るかを決めることもできる。Segmentを使ってすべてのイベントを送信するのではなく、マーケティングチームや編集チームとユースケースを検討し、データオーバーを避けるためにBrazeに送信するイベントを決定することをお勧めする。

{% enddetails %}

{% details モバイルデバイスモード宛先設定のカスタムAPIエンドポイントとカスタムREST APIエンドポイントの違いを理解する。 %}

| ブレイズ用語 | Segment で対応する用語 |
| ----------------- | ------------------ |
| Braze SDKエンドポイント | カスタムAPIエンドポイント |
| Braze RESTエンドポイント | カスタムREST APIエンドポイント |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze API エンドポイント (Segment では「Custom API Ednpoint」と呼ばれます) は、SDK のために Braze により設定される SDK エンドポイントです (例: `sdk.iad-03.braze.com`)。Braze REST API エンドポイント (Segment では「Custom REST API Endpoint」と呼ばれます) は、REST API エンドポイントです (例: `https://rest.iad-03.braze.com`)。
{% enddetails %}

{% details カスタムAPIエンドポイントがモバイルデバイスモードの宛先設定に正しく入力されていることを確認する。 %}

| ブレイズ用語 | Segment で対応する用語 |
| ----------------- | ------------------ |
| Braze SDKエンドポイント | カスタムAPIエンドポイント |
| Braze RESTエンドポイント | カスタムREST APIエンドポイント |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze SDK のエンドポイントを正しく入力するには、適切な形式に従う必要があります。Braze SDK エンドポイントには `https://` を含めないでください (例: `sdk.iad-03.braze.com`)。このようにしないと、Braze 統合が機能しなくなります。これは、Segment によりエンドポイントの先頭に `https://` が自動的に付加され、その結果、Braze は無効なエンドポイント `https://https://sdk.iad-03.braze.com` で初期化されことになるためです。

{% enddetails %}

{% details データマッピングのニュアンス %}

データが期待通りに通過しないシナリオ：

1. 階層化カスタム属性
  - [ネストされたカスタム属性は]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/nested_custom_attribute_support/)、技術的にはSegmentを通してBrazeに送信できるが、**ペイロード全体が**毎回送信される。これにより、ペイロードが送信されるたびに、ネストされたオブジェクトに渡されたキーごとに[データポイントが]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points)発生する。<br><br> ペイロードの送信時にデータポイントのサブセットのみを使用するには、Segment のカスタム[宛先関数](https://segment.com/docs/connections/functions/destination-functions/)機能を使用できます。Segment プラットフォームのこの機能により、ダウンストリームの宛先へのデータの送信方法をカスタマイズできます。

  {% alert note %}
  カスタム宛先関数は Segment 内で管理されるため、Braze では外部で設定されているこの関数に関する情報は限られています。
  {% endalert %}

{: start="2"}
2\.サーバー間で匿名データを受け渡す。
  - 顧客は、Segment のサーバー間ライブラリを使用して、匿名データを他のシステムに渡すことができます。サーバー間 (cloud-mode) 統合を介して `external_id` を持たないユーザーを Braze に送信する方法については、「メソッドをマッピングする」セクションを参照してください。

{% enddetails %}

{% details Brazeの初期化をカスタマイズする。 %}

Brazeのカスタマイズには、プッシュ、アプリ内メッセージ、コンテンツカード、初期化など、いくつかの方法がある。サイドバイサイド統合では、Braze の直接統合と同様に、プッシュ、アプリ内メッセージ、コンテンツカードをカスタマイズできます。

ただし Braze SDK の統合時にカスタマイズを行うこと、または初期化設定を指定することは難しく、場合によっては不可能なことがあります。これは、Segment の初期化時に Segment により Braze SDK が初期化されるためです。

{% enddetails %}

{% details Braze に差分を送信する。 %}

ユーザー属性データを渡すときは、前回の更新以降に変更された属性の値のみを渡すようにする。こうすることで、データポイントを不必要に消費することがなくなります。クライアントサイドのソースについては、Segment のオープンソース [Middleware](https://github.com/segmentio/segment-braze-mobile-middleware) ツール使用して統合を最適化し、Segment からの重複した `identify()` 呼び出しをデバウンスすることで、データポイント使用量を制限します。 

{% enddetails %}


[5]: https://segment.com
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events
[14]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[18]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[19]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[22]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data
[23]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[24]: {{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula
[25]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection
[26]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[27]: {{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/
[28]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[36]: https://segment.com/docs/sources/#server
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[39]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[40]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[41]: https://segment.com/docs/spec/identify/#user-id
[42]: {% image_buster /assets/img/segment/setup.png %}
[43]: {% image_buster /assets/img/segment/website.png %}
[44]: {% image_buster /assets/img/segment/ios.png %}
[45]: {% image_buster /assets/img/segment/android.png %}
