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

> [Segmentは][5]、顧客データの収集、クリーニング、活性化を支援する顧客データ・プラットフォームである。 

BrazeとSegmentの統合により、ユーザーを追跡し、様々なユーザー分析プロバイダーにデータをルーティングすることができる。セグメントを使えば、次のことができる：
- BrazeキャンペーンとCanvasセグメンテーションで使用するために、[Segment Engageを]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_engage/)Brazeに同期する。
- [2つのプラットフォーム間でデータをインポートする](#integration-options)。お客様のAndroid、iOS、およびWebアプリケーション用のサイドバイサイドSDKインテグレーションと、BrazeのREST APIにデータを同期するためのサーバー間インテグレーションを提供する。
- [カレントを介してデータをセグメントに接続する]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/)。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| セグメント・アカウント | このパートナーシップを利用するには、[セグメントアカウントが](https://app.segment.com/login)必要である。 |
| インストールされたソースとセグメント・ソース・[ライブラリ](https://segment.com/docs/sources/) | モバイルアプリ、ウェブサイト、バックエンドサーバーなど、Segmentに送信されるあらゆるデータの送信元。<br><br>ライブラリをアプリ、サイト、サーバーにインストールしてからでないと、`Source > Destination` 。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

BrazeとSegmentを統合するには、[選択した統合タイプ](#integration-options)（接続モード）に従って、[Brazeを接続先に](#connection-settings)設定する必要がある。Brazeの新規顧客であれば、[セグメントリプレイを使って](#segment-replays)過去のデータをBrazeにリレーすることができる。次に、BrazeとSegment間のスムーズなデータフローを確保するために、[マッピングを](#methods)設定し、[統合をテスト](#step-4-test-your-integration)しなければならない。

### ステップ1:ブレイズの目的地を作る {#connection-settings}

ソースの設定に成功したら、各ソース（iOS、Android、ウェブなど）の[デスティネーションとして](https://segment.com/docs/destinations/)Brazeを設定する必要がある。接続設定を使用して、BrazeとSegment間のデータフローをカスタマイズする多くのオプションがある。

### ステップ2:接続先フレームワークと接続タイプを選択する {#integration-options}

Segmentで、**Destinations > Braze > Configure Braze > Select your Source > Setupと**進む。

![ソースの設定ページ。このページでは、デスティネーション・フレームワークを「アクション」または「クラシック」のいずれかに設定し、接続モードを「クラウドモード」または「デバイスモード」のいずれかに設定する。][42]

Segmentのウェブソース（Analytics.js ）およびネイティブクライアントサイドライブラリは、サイドバイサイド（デバイスモード）統合またはサーバー間（クラウドモード）統合のいずれかを使用して、Brazeと統合できる。

接続モードの選択は、宛先が設定されているソースのタイプによって決定される。

| 統合 | 詳細 |
| ----------- | ------- |
| [サイド・バイ・サイド<br>(デバイスモード)](#side-by-side-sdk-integration) |SegmentのSDKを使用して、イベントをBrazeのネイティブコールに変換し、サーバー間の統合よりも深い機能とBrazeのより包括的な使い方にアクセスできるようにする。<br><br>Segmentは、すべてのBrazeメソッド（例えば、Content Cards）をサポートしているわけではない。対応するマッピングを通してマッピングされていないBrazeメソッドを使用するには、コードベースにネイティブのBrazeコードを追加してメソッドを呼び出す必要がある。 |
| [サーバー間<br>(クラウドモード）](#server-to-server-integration) | SegmentからBraze REST APIエンドポイントにデータを転送する。<br><br>アプリ内メッセージ、コンテンツカード、プッシュ通知などのBraze UI機能には対応していない。また、この方法では利用できない、デバイスレベルのフィールドのような、自動的に取り込まれるデータも存在する。<br><br>これらの機能を使いたい場合は、サイド・バイ・サイドの統合を検討しよう。|
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
2つの統合オプション（接続モード）について、それぞれの利点を含め、詳しくは[セグメントを](https://segment.com/docs/destinations/#connection-modes)ご覧いただきたい。
{% endalert %}

#### サイド・バイ・サイドのSDK統合

デバイスモードとも呼ばれるこの統合は、SegmentのSDKと[メソッドを](#methods)Braze SDKにマッピングし、プッシュ、アプリ内メッセージング、その他のBrazeネイティブのメソッドなど、当社のSDKが提供するすべての機能へのアクセスを可能にする。 

{% alert note %}
Segmentのデバイスモードを使用する場合、Braze SDKを直接統合する必要はない。Segmentのデバイスモード先としてBrazeを追加する場合、Segment SDKはBraze SDKを初期化し、関連するマッピングされたBrazeメソッドを呼び出す。
{% endalert %}

デバイスモード接続を使用する場合、Braze SDKをネイティブに統合するのと同様に、Braze SDKは、すべてのユーザーに`device_id` とバックエンド識別子、`braze_id` を割り当てる。これによりBrazeは、`userId` の代わりにこれらの識別子を照合することで、デバイスからの匿名アクティビティをキャプチャすることができる。 

{% tabs ローカル %}
{% tab アンドロイド %}

{% alert important %}
Androidデバイスモード統合のソースコードは、Brazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新される。

<br>
使用するBraze SDKは、使用するSegment SDKによって異なる：

| セグメントSDK｜ブレイズSDK
| - | ----------- | --------- |
\|[Analytics-Kotlin｜Braze Segment Kotlin](https://github.com/braze-inc/braze-segment-kotlin)｜優先｜[分析-Kotlin](https://github.com/segmentio/analytics-kotlin)｜[ブレイズ・セグメント・コトリン](https://github.com/braze-inc/braze-segment-kotlin)
| レガシー｜[アナリティクス-アンドロイド](https://github.com/segmentio/analytics-android)｜[Braze Segment Android](https://github.com/braze-inc/braze-segment-android)｜[ブレイズ・セグメント・アンドロイド](https://github.com/braze-inc/braze-segment-android)
{: .reset-td-br-1 .reset-td-br-2}


{% endalert %}

AndroidソースのデバイスモードデスティネーションとしてBrazeを設定するには、デスティネーションフレームワークとして**Classicを**選択し、**Saveを**クリックする。 

![]({% image_buster /assets/img/segment/android.png %})

サイドバイサイドの統合を完了するには、[Android](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/)アプリにBrazeのデスティネーション依存性を追加するためのSegmentの詳細な手順を参照する。

[Androidデバイスモード](https://github.com/braze-inc/braze-segment-kotlin)統合のソースコードは、Brazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新される。

{% endtab %}
{% tab iOS %}

{% alert important %}
iOSデバイスモード統合のソースコードは、Brazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新される。

<br>
使用するBraze SDKは、使用するSegment SDKによって異なる：

| セグメントSDK｜ブレイズSDK
| - | ----------- | --------- |
| プリファード｜[アナリティクス・スイフト](https://github.com/segmentio/analytics-swift)｜[ブレイズ・セグメント・スイフト](https://github.com/braze-inc/braze-segment-swift)
| レガシー｜[アナリティクスiOS](https://github.com/segmentio/analytics-ios)｜[Braze Segment iOS](https://github.com/Appboy/appboy-segment-ios)｜[ブレイズ・セグメントiOS](https://github.com/Appboy/appboy-segment-ios)
{: .reset-td-br-1 .reset-td-br-2}
{% endalert %}

BrazeをiOSソースのデバイスモードデスティネーションとして設定するには、デスティネーションフレームワークとして**Classicを**選択し、**Saveを**クリックする。 

![]({% image_buster /assets/img/segment/ios.png %})

サイドバイサイドの統合を完了するには、[iOS](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/)アプリにBraze Segmentポッドを追加するためのSegmentの詳細な手順を参照する。

[iOSデバイスモード](https://github.com/braze-inc/braze-segment-swift)統合のソースコードは、Brazeによって保守されており、新しいBraze SDKのリリースを反映して定期的に更新される。

{% endtab %}
{% tab ウェブまたはJavaScript %}

Segmentの新しいBraze Web Mode (Actions)フレームワークは、BrazeをWebソースのデバイスモードデスティネーションとして設定するのに推奨される。 

セットアップUIで、接続先フレームワークとして**Actionsを**、接続モードとして**Device Modeを**選択する。

![]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab リアクト・ネイティブ %}
[React Native Brazeプラグインの](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze)ソースコードはSegmentによって管理されており、新しいBraze SDKのリリースを反映するために定期的に更新される。

React NativeセグメントソースをBrazeに接続する場合、オペレーティングシステムごとにソースとデスティネーションを設定する必要がある。例えば、iOSのデスティネーションとAndroidのデスティネーションを設定する。 

アプリのコードベース内で、各アプリに関連付けられたそれぞれのソース書き込みキーを使用して、デバイスタイプ別にSegment SDKを条件付きで初期化する。

デバイスからプッシュトークンが登録され、Brazeに送信されると、SDKの初期化時に使用されたアプリ識別子に関連付けられる。デバイスタイプの条件付き初期化は、Brazeに送信されるプッシュトークンが関連アプリに関連付けられていることを確認するのに役立つ。

{% alert important %}
React Nativeアプリがすべてのデバイスで同じBrazeアプリ識別子でBrazeを初期化する場合、すべてのReact NativeユーザーはBrazeでAndroidまたはiOSユーザーとみなされ、すべてのプッシュトークンはそのオペレーティングシステムに関連付けられる。
{% endalert %}

Brazeを各ソースのデバイスモードデスティネーションとして設定するには、デスティネーションフレームワークとして**Classicを**選択し、**Saveを**クリックする。

{% endtab %}
{% endtabs %}

#### サーバー間の統合

クラウドモードとも呼ばれるこの統合は、SegmentからBrazeのREST APIにデータを転送する。Segmentの新しい[Brazeクラウドモード（Actions）](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/)フレームワークを使って、どのソースにもクラウドモードのデスティネーションを設定する。 

サイド・バイ・サイドの統合とは異なり、サーバー間統合は、アプリ内メッセージング、コンテンツカード、自動プッシュトークン登録といったBrazeのUI機能をサポートしていない。また、クラウドモードでは利用できない[自動取得]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection)データ（匿名ユーザーやデバイスレベルのフィールドなど）も存在する。

このデータとこれらの機能を使用したい場合は、サイド・バイ・サイド（デバイスモード）SDK統合の使用を検討すること。

[Braze Cloud Mode（Actions）デスティネーションの](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze)ソースコードはSegmentによって管理されている。

### ステップ3:設定

目的地の設定を定義する。すべての設定がすべてのデスティネーションタイプに適用されるわけではない。

{% tabs ローカル %}
{% tab モバイル・デバイス・モード %}

| セッティング | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。これは、Brazeダッシュボードの「**Manage Settings**」で確認できる。 | 
| カスタムAPIエンドポイント<br>(SDKエンドポイント） | インスタンスに対応するBraze SDKエンドポイント（`sdk.iad-01.braze.com` など） | 
| 終点領域 | あなたのBrazeインスタンス（US 01、US 02、EU 01など） | 
| アプリ内の自動メッセージ登録を有効にする | アプリ内メッセージを手動で登録したい場合は、これを無効にする。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab ウェブ・デバイス・モード %}

| セッティング | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。これは、Brazeダッシュボードの「**Manage Settings**」で確認できる。 | 
| カスタムAPIエンドポイント<br>(SDKエンドポイント） | インスタンスに対応するBraze SDKエンドポイント（`sdk.iad-01.braze.com` など） | 
| サファリウェブサイトのプッシュID | Safariプッシュをサポートしている場合、Safariプッシュ証明書を作成する際にAppleに提供したWebサイトプッシュID（`web` で始まる、たとえば、`web.com.example.domain` ）をこのオプションに指定する必要がある。 |
| Braze Web SDKバージョン | 使用したいBraze Web SDKのバージョン |
| アプリ内メッセージを自動送信する | デフォルトでは、ユーザーが受信可能なアプリ内メッセージはすべて、自動的にユーザーに配信される。アプリ内メッセージを手動で表示したい場合は、これを無効にする。 |
| 素晴らしいフォントを読み込まない | Brazeはアプリ内のメッセージアイコンにFont Awesomeを使用している。デフォルトでは、Brazeは自動的にFontAwesome CDNからFontAwesomeを読み込む。この動作を無効にするには（例えば、あなたのサイトが FontAwesome のカスタマイズ版を使用しているため）、このオプションを`TRUE` に設定する。これを行う場合、FontAwesomeがあなたのサイトにロードされていることを確認する責任があることに注意すること - そうでない場合、アプリ内メッセージが正しくレンダリングされない可能性がある。 |
| HTMLアプリ内メッセージを有効にする | このオプションを有効にすると、BrazeダッシュボードユーザーがHTMLアプリ内メッセージを使用できるようになる。 | 
| アプリ内のメッセージを新しいタブで開く | デフォルトでは、アプリ内のメッセージクリックからのリンクは、メッセージごとにダッシュボードで指定された現在のタブまたは新しいタブに読み込まれる。このオプションを`TRUE` に設定すると、アプリ内メッセージのクリックによるすべてのリンクが新しいタブまたはウィンドウで強制的に開かれる。 |
| アプリ内メッセージzインデックス | Brazeのデフォルトのz-indexを上書きするには、このオプションに値を指定する。 | 
| 明示的なアプリ内メッセージの解除を要求する | デフォルトでは、アプリ内メッセージが表示されている場合、エスケープボタンを押すか、ページのグレーアウトした背景をクリックすると、メッセージが表示されなくなる。このオプションをtrueに設定すると、この動作を防ぎ、メッセージを解除するために明示的なボタンクリックを要求する。 |
| トリガーアクションの最小間隔（秒 | デフォルトは30である。<br>デフォルトでは、トリガーアクションは、最後のトリガーアクションから少なくとも30秒が経過した場合にのみ発火する。このコンフィギュレーション・オプションに値を指定すると、デフォルトを独自の値で上書きすることができる。ユーザーへのスパム通知を避けるため、この値を10より小さくすることは推奨しない。|
| サービス従業員の所在地 | デフォルトでは、Webプッシュ通知のためにユーザーを登録するとき、Brazeは、Webサーバーのルートディレクトリの`/service-worker.js` にある必要なサービスワーカーファイルを探す。サーバー上の別のパスでサービスワーカーをホストしたい場合、このオプションにファイルへの絶対パスを指定する。(例えば、`/mycustompath/my-worker.js`)。ここで値を設定すると、サイト上でのプッシュ通知の範囲が制限されることに注意。例えば、上記の例では、サービスワーカーファイルは`/mycustompath/` ディレクトリ内にあるため、`requestPushPermission` は`http://yoursite.com/mycustompath/` で始まるウェブページからのみ呼び出すことができる。 |
| プッシュトークンのメンテナンスを無効にする | デフォルトでは、すでにウェブプッシュ許可を与えているユーザーは、配信可能性を確保するために、新しいセッションで自動的にBrazeバックエンドとプッシュトークンを同期する。この動作を無効にするには、このオプションを`FALSE` に設定する。 |
| サービス・ワーカーを外部で管理する | 登録し、ライフサイクルを制御する独自のサービスワーカーがある場合、このオプションを`TRUE` に設定すると、Braze SDKはサービスワーカーを登録または登録解除しない。このオプションを`TRUE` に設定した場合、プッシュが正しく機能するためには、`requestPushPermission` を呼び出す前に自分でサービスワーカーを登録し、`self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` を使うか、そのファイルの内容を直接含めるかして、Brazeのサービスワーカーコードが含まれていることを確認する必要がある。このオプションが`TRUE` の場合、`serviceWorkerLocation` オプションは無関係であり、無視される。 |
| コンテンツ・セキュリティ・ノンス | このオプションに値を指定すると、Braze SDKは、SDKによって作成されたすべての`<script>` および`<style>` 要素にnonceを追加する。これにより、Braze SDKは、あなたのウェブサイトのコンテンツセキュリティポリシーと連動することができる。このnonceの設定に加えて、FontAwesomeの読み込みを許可する必要があるかもしれない。これは、コンテンツセキュリティポリシーのallowlistに`use.fontawesome.com` を追加するか、`doNotLoadFontAwesome` オプションを使用して手動で読み込むことでできる。 |
| クローラーの活動を許可する | デフォルトでは、Braze Web SDKは、ユーザーエージェント文字列に基づいて、Googleなどの既知のスパイダーやウェブクローラーからのアクティビティを無視する。これはデータポイントを節約し、分析をより正確にし、ページランクを向上させる可能性がある。ただし、Brazeにこれらのクローラーからの活動を記録させたい場合は、このオプションを`TRUE` 。 |
| ロギングを有効にする | デフォルトでロギングを有効にするには、`TRUE` に設定する。この場合、BrazeはJavaScriptコンソールにログを記録する。ページを本番環境にリリースする前に、これを削除するか、`setLogger` で代替のロガーを提供すべきである。 |
| ニュースフィードのカードを新しいタブで開く（新しいタブでカードを開く） | デフォルトでは、カード・オブジェクトからのリンクは現在のタブまたはウィンドウに読み込まれる。カードからのリンクを新しいタブまたはウィンドウで開くようにするには、このオプションを`TRUE` に設定する。<br><br>**注:**ニュースフィードは非推奨になります。Braze では、News Feed ツールを使用するお客様は、コンテンツカードメッセージングチャネルに移動することを推奨しています。これは、より柔軟でカスタマイズ可能で、信頼性が高いチャネルです。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。 |
| ユーザー提供のJavaScriptを許可する | デフォルトでは、Braze Web SDKは、Brazeダッシュボードユーザーがサイト上でJavaScriptを実行できるように、ユーザーが提供するJavaScriptクリックアクションを許可しない。Brazeダッシュボードのユーザーが悪意のないJavaScriptクリックアクションを記述することを信頼することを示すには、このプロパティを`TRUE` に設定する。`enableHtmlInAppMessages` が`TRUE` の場合、このオプションも`TRUE` に設定される。 |
| アプリ版| このオプションに値を指定すると、Brazeに送信されたユーザーイベントは、指定したバージョンに関連付けられ、ユーザーセグメンテーションに使用できる。 |
| セッションタイムアウト（秒 | デフォルトは30である。<br>デフォルトでは、セッションは30分間操作がないとタイムアウトする。このコンフィギュレーション・オプションに値を指定すると、デフォルトを独自の値で上書きすることができる。 | 
| デバイス・プロパティ allowlist | デフォルトでは、Braze SDKは自動的にすべてのデバイスプロパティを検出し、`DeviceProperties` で収集する。この動作をオーバーライドするには、`DeviceProperties` の配列を指定する。いくつかのプロパティがないと一部の機能が正しく機能しないことがあるので注意してください。たとえば、ローカルタイムゾーンの配信はタイムゾーンなしでは機能しません。 |
| ローカライゼーション | デフォルトでは、SDKが生成したユーザー可視メッセージはすべて、ユーザーのブラウザ言語で表示される。その動作をオーバーライドして特定の言語を強制するには、このオプションに値を指定する。このオプションの値はISO 639-1言語コードでなければならない。 |
| クッキーなし | デフォルトでは、Braze SDKは少量のデータ（ユーザーID、セッションID）をクッキーに保存する。これは、Brazeがサイトの異なるサブドメイン間でユーザーとセッションを認識できるようにするためである。これが問題になる場合は、このオプションに`TRUE` 。クッキーの保存を無効にし、ユーザーとセッションの識別をHTML 5のlocalStorageに完全に依存する。 |
| すべてのページを追跡する | **クラシック・デスティネーション・ウェブ・デバイス・モード（メンテナンス）のみ**<br><br>Segmentでは、この設定を[マッピングで有効に](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)できるWeb Actionsフレームワークへの移行を推奨している。<br><br>これにより、すべての[ページ呼び出しが](https://segment.com/docs/spec/page/)"Loaded/Viewed a Page "イベントとしてBrazeに送られる。 |
| 指定されたページのみを追跡する | **クラシック・デスティネーション・ウェブ・デバイス・モード（メンテナンス）のみ**<br><br>Segmentでは、この設定を[マッピングで有効に](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)できるWeb Actionsフレームワークへの移行を推奨している。<br><br>これでBrazeには、名前に関連づけられたページ・コールだけが送られる。 |
| 収益がある場合、購入を記録する | **クラシック・デスティネーション・ウェブ・デバイス・モード（メンテナンス）のみ**<br><br>Segmentでは、この設定を[マッピングで有効に](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)できるWeb Actionsフレームワークへの移行を推奨している。<br><br>このオプションを有効にすると、収益プロパティを持つすべてのTrackコールが購入イベントをトリガーする。 | 
| 既知のユーザーのみを追跡する | **クラシック・デスティネーション・ウェブ・デバイス・モード（メンテナンス）のみ**<br><br>Segmentでは、マッピングによってこの設定を有効にできるWeb Actions Frameworkへの移行を推奨している。<br><br>この新しい設定を有効にすると、有効な`userId` まで、`window.appboy.initialize` の呼び出しを遅らせる。 | 
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab クラウドモード %}

| セッティング | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。これは、Brazeダッシュボードの「**Manage Settings**」で確認できる。 | 
| REST APIキー | これは、Brazeダッシュボードの**「設定」**>「**APIキー**」で確認できる。 | 
| カスタムREST APIエンドポイント | インスタンスに対応するBraze RESTエンドポイント（rest.iad-01.braze.com など）。 | 
| 既存ユーザーのみを更新する | **クラシック・デスティネーション クラウドモード（メンテナンス）のみ**<br><br>セグメントでは、[マッピングによって](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)この設定を[有効に](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)できるCloud Actions Frameworkデスティネーションへの移行を推奨している。<br><br>既存のユーザーのみを更新するかどうかを決定する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

### ステップ4:地図メソッド {#methods}

Brazeは、[Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page)メソッド、[Identify](https://segment.com/docs/spec/identify/)メソッド、[Track](https://segment.com/docs/spec/track/)Segmentメソッドをサポートしている。これらの方法で使用される識別子の種類は、データがサーバー間（クラウドモード）で送信されるのか、サイドバイサイド（デバイスモード）で送信されるのかによって異なる。Braze Web Mode ActionsとCloud Mode Actionsの宛先では、[セグメントエイリアス通話の](https://segment.com/docs/connections/spec/alias/)マッピングを設定することもできる。 

{% alert note %}
ユーザーエイリアスは、Brazeクラウドモード（Actions）デスティネーションの識別子としてサポートされているが、Segmentのエイリアス呼び出しは、Brazeユーザーエイリアスとは直接関係ないことに注意すべきである。
{% endalert %}

| 識別子タイプ | サポート先 |
| --------------- | --------------------- |
| `userId` (`external_id`) | すべて |
| 匿名ユーザー | デバイス・モードの目的地 |
| ユーザーエイリアス | クラウドモードの目的地 |
{: .reset-td-br-1 .reset-td-br-2}

クラウドモード（Actions）デスティネーションには、[エイリアスの作成（Create Alias）アクションが](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#create-alias)あり、エイリアスのみのユーザーを作成したり、既存の`external_id` プロファイルにエイリアスを追加したりするのに使用できる。[ユーザーの識別（Identify User）アクションは](https://segment.com/docs/connections/destinations/catalog/actions-braze-cloud/#identify-user)、エイリアスの作成（Create Alias）アクションと並行して使用することができ、そのユーザーが使用可能になった後、エイリアスのみのユーザーを`external_id` 。 

回避策を考え、`braze_id` 、クラウドモードで匿名のユーザーデータを送信することも可能だ。そのため、すべてのSegment APIコールにユーザーの`braze_id` を手動で含める必要がある。この回避策の設定方法については、[Segmentのドキュメントを](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users)参照されたい。

Brazeに送信される宛先データは、クラウドモードアクション内でバッチ処理できる。バッチサイズの上限は75イベントであり、これらのバッチはフラッシュされる前に30秒間蓄積される。リクエストのバッチ処理はアクションごとに行われる。例えば、Identify Calls（属性）はリクエストにバッチされ、Track Calls（カスタムイベント）は2番目のリクエストにバッチされる。SegmentからBrazeに送信されるリクエストの数を減らすことができるため、Brazeはこの機能を有効にすることを推奨している。その結果、デスティネーションがBrazeのレート制限にヒットし、リクエストをリトライするリスクを減らすことができる。 

Braze Destination >**Mappingsに**移動して、アクションのバッチ処理をオンにできる。そこから、マッピングの右側にある3つの点のアイコンをクリックし、**マッピングの編集を**選択する。**Select mappings**セクションの一番下までスクロールし、**Batch Data to Brazeが** **Yesに**設定されていることを確認する。


{% tabs ローカル %}
{% tab 特定する %}
#### 特定する

[Identify](https://segment.com/docs/spec/identify/)コールは、ユーザーをその行動に結びつけ、そのユーザーに関する属性を記録することができる。 

特定のセグメント特殊特性は、Brazeの標準的な属性プロファイルフィールドにマッピングされる：

| 特別セグメントの特徴 | ブレージング標準属性 |
| ------------- | ----------- |
| `userId` | `external_id` |
| `firstName` | `first_name` |
| `lastName` | `last_name` |
| `email` | `email` |
| `birthday` | `dob` |
| `address.country` | `country` |
| `address.city` | `home_city` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2}

`email_subscribe` 、`push_subscribe` などの予約済みBrazeプロファイルフィールドは、Brazeのこれらのフィールドの命名規則を使用し、identifyコール内でtraitとして渡すことで送信できる。

##### 購読グループにユーザーを追加する

traits パラメータの以下のフィールドを使用して、指定されたサブスクリプショングループからユーザーをサブスクライブまたはアンサブスクライブすることもできる。

`braze_subscription_groups` という予約済みのBrazeプロファイル・フィールドを使用し、オブジェクトの配列と関連付けることができる。配列の各オブジェクトは、2つの予約キーを持っていなければならない：

1. `subscription_group_state`:ユーザーが特定のサブスクリプショングループに`"subscribed"` 、または`"unsubscribed"` 。
2. `subscription_group_id`:サブスクリプショングループの一意の ID を表す。このIDは、Brazeダッシュボードの「**Subscription Group Management**」で確認できる。

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

その他の特徴はすべて[カスタム属性として]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)記録される。

| セグメント方式 | ろう付け法 | 例 |
|---|---|---|
| ユーザーIDで識別する | 外部IDを設定する | セグメントだ：  `analytics.identify("dawei");`<br>ブレイズだ： `Braze.changeUser("dawei")` |
| 控えめな特徴を識別する | ユーザー属性を設定する | セグメントだ： `analytics.identify({email: "dawei@braze.com"});`<br> ブレイズだ： `Braze.getUser().setEmail("dawei@braze.com");`
| カスタム特性で識別する | カスタム属性を設定する | セグメントだ： `analytics.identify({fav_cartoon: "Naruto"});`<br>ブレイズ：`Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")` ；
| ユーザーIDと特徴を識別する | セグメントだ：外部IDと属性を設定する | 先の方法を組み合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[Web Mode Actionsと](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) [Cloud Mode Actionsの](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile)宛先では、Update User Profile Actionを使って上記のマッピングを設定できる。

{% alert important %}
ユーザー属性データを渡すときは、前回の更新以降に変更された属性の値のみを渡すようにする。こうすることで、不必要にデータポイントを消費することがなくなる。クライアント側のソースについては、Segmentのオープンソースの[ミドルウェアツールを](https://github.com/segmentio/segment-braze-mobile-middleware)使用して、統合を最適化し、Segmentからの重複した`identify()` 呼び出しをデバウンスすることで、データポイントの使用量を制限する。 

{% endalert %}
{% endtab %}

{% tab トラック %}
#### トラック

あなたがイベントを追跡するとき、私たちは提供された名前を使用して[カスタムイベントとして]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)そのイベントを記録する。 

トラックコールのプロパティオブジェクト内で送信されたメタデータは、関連イベントのカスタムイベントプロパティとしてBrazeに記録される。すべての[カスタムイベントプロパティデータタイプが](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)サポートされている。

[Web Mode Actionsと](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) [Cloud Mode Actionsの](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event)デスティネーションでは、Track Event Actionを使って上記のマッピングを設定できる。

| セグメント方式 | ろう付け法 | 例 |
|---|---|---|
| [トラック](https://segment.com/docs/spec/track/) | [カスタムイベントとして]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)記録される。 | セグメントだ： `analytics.track("played_game");`<br>ブレイズだ： `Braze.logCustomEvent("played_game");`|
| [物件を追跡する](https://segment.com/docs/spec/track/) | [イベントプロパティとして]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)記録される。 | セグメントだ： `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});`<br>ブレイズだ： `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [製品で追跡する](https://segment.com/docs/spec/track/) | [購入イベントとして]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)記録される。 | セグメントだ： `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});`<br>ブレイズだ： `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

##### 注文完了 {#order-completed}

Segmentの[EコマースAPIに](https://segment.com/docs/spec/ecommerce/v2/)記載されているフォーマットを使用して、`Order Completed` という名前でイベントをトラッキングすると、あなたが[購入として]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data)リストアップした商品が記録される。

[Web Mode Actionsと](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) [Cloud Mode Actionsの](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase)宛先では、Track Purchase Actionでデフォルトのマッピングをカスタマイズできる。

{% endtab %}

{% tab ページ %}
#### ページ {#page}

[Page](https://segment.com/docs/spec/page/)コールは、ユーザーがあなたのウェブサイトのページを見るたびに、ページに関するオプションのプロパティとともに記録することができる。

このイベントタイプは、Web Mode ActionsとCloud Actionsのデスティネーションでトリガーとして使用し、カスタムイベントをBrazeに記録することができる。
{% endtab %}

{% endtabs %}

### ステップ 5: 連携のテスト

サイドバイサイド（デバイスモード）統合を使用する場合、[概要][27]メトリクス（ライフタイムセッション、MAU、DAU、スティッキネス、デイリーセッション、MAUあたりのデイリーセッション）を使用して、BrazeがSegmentからデータを受信していることを確認できる。

[カスタムイベントや][22] [収益][28]ページ、または[セグメントを作成する][23]ことでデータを見ることができる。ダッシュボードの**カスタム・イベント**・ページでは、カスタム・イベントのカウントを時系列で見ることができる。サーバー間（クラウドモード）統合を使用している場合、MAUとDAU統計を含む[計算式を][24]使用することはできないことに注意。

Brazeに購入データを送信している場合（[ステップ](#methods)3の**Track**タブで注文完了を参照）、[収益][28]ページで特定の期間の収益や購入に関するデータ、またはアプリの総収益を確認できる。

[セグメントを作成すること][26]で、カスタムイベントと属性データに基づいてユーザーをフィルタリングすることができる。

{% alert important %}
サーバー間統合（クラウドモード）を使用している場合、自動的に収集されたセッションデータ（「最初に使用したアプリ」や「最後に使用したアプリ」など）に関連するフィルターは機能しない。SegmentとBrazeの統合でこれらを使用したい場合は、サイドバイサイド統合（デバイスモード）を使用する。
{% endalert %}

## ユーザーの削除と抑制 

ユーザーを削除または抑制する必要がある場合は、[Segmentのユーザー削除](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **機能が**Braze[`/users/delete` エンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)マッピングされて**いる**ことに注意。これらの削除の検証には最大30日かかる可能性があることに注意してほしい。

BrazeとSegmentの間で共通のユーザー識別子を選択する必要がある（`external_id` のように）。Segmentで削除リクエストを開始すると、Segmentダッシュボードの削除リクエストタブでステータスを確認できる。

## セグメント・リプレイ

セグメントは顧客に対して、すべての履歴データを新しいテクノロジー・パートナーに「再生」するサービスを提供している。関連するすべての履歴データをインポートしたいBrazeの新規顧客は、Segmentを通じてインポートできる。もし興味があれば、セグメント担当者に相談してほしい。

Segmentが当社の[`/users/track` エンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)接続し、ユーザーに代わってBrazeにユーザーデータをインポートする。

{% alert important %}
クラウドモード・アクションの宛先でサポートされているすべての識別子は、セグメント・リプレイの一部としてサポートされている。
{% endalert %}

## ベストプラクティス

{% details データ超過を避けるために使用例を見直す。 %}

セグメントは**、**クライアントが送信するデータエレメントの数を制限**しない**。セグメントを使えば、すべてのイベントをBrazeに送ることも、どのイベントを送るかを決めることもできる。Segmentを使ってすべてのイベントを送信するのではなく、マーケティングチームや編集チームとユースケースを検討し、データオーバーを避けるためにBrazeに送信するイベントを決定することをお勧めする。

{% enddetails %}

{% details モバイルデバイスモード宛先設定のカスタムAPIエンドポイントとカスタムREST APIエンドポイントの違いを理解する。 %}

| ブレイズ用語 | セグメントに相当する |
| ----------------- | ------------------ |
| Braze SDKエンドポイント | カスタムAPIエンドポイント |
| Braze RESTエンドポイント | カスタムREST APIエンドポイント |
{: .reset-td-br-1 .reset-td-br-2}

あなたのBraze APIエンドポイント（Segmentでは「カスタムAPIエンドポイント」と呼ばれる）は、BrazeがあなたのSDKのために設定するSDKエンドポイントである（例えば、`sdk.iad-03.braze.com` ）。あなたのBraze REST APIエンドポイント（Segmentでは「カスタムREST APIエンドポイント」と呼ばれる）は、REST APIエンドポイント（例えば、`https://rest.iad-03.braze.com` ）である。
{% enddetails %}

{% details カスタムAPIエンドポイントがモバイルデバイスモードの宛先設定に正しく入力されていることを確認する。 %}

| ブレイズ用語 | セグメントに相当する |
| ----------------- | ------------------ |
| Braze SDKエンドポイント | カスタムAPIエンドポイント |
| Braze RESTエンドポイント | カスタムREST APIエンドポイント |
{: .reset-td-br-1 .reset-td-br-2}

Braze SDKのエンドポイントを正しく入力するために、適切なフォーマットに従わなければならない。あなたのBraze SDKエンドポイントは、`https://` (例えば、`sdk.iad-03.braze.com`)を含んではならない。そうでなければ、Braze統合は壊れる。これは、Segmentが自動的にエンドポイントの先頭に`https://` を付けるためで、その結果、Brazeは無効なエンドポイント`https://https://sdk.iad-03.braze.com` で初期化される。

{% enddetails %}

{% details データマッピングのニュアンス %}

データが期待通りに通過しないシナリオ：

1. 階層化カスタム属性
  - [ネストされたカスタム属性は]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/)、技術的にはSegmentを通してBrazeに送信できるが、**ペイロード全体が**毎回送信される。これにより、ペイロードが送信されるたびに、ネストされたオブジェクトに渡されたキーごとに[データポイントが]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points)発生する。<br><br> ペイロードの送信時にデータポイントのサブセットのみを使用するには、Segmentが持つカスタム[宛先関数](https://segment.com/docs/connections/functions/destination-functions/)機能を使用することができる。Segmentプラットフォームのこの機能により、下流へのデータ送信方法をカスタマイズすることができる。

  {% alert note %}
  カスタムデスティネーション機能はセグメント内で制御され、外部で設定された機能に対するBrazeの洞察力は限られている。
  {% endalert %}

{: start="2"}
2\.匿名データをサーバー間で受け渡す。
  - 顧客は、Segmentのサーバー間ライブラリを使用して、匿名データを他のシステムに流すことができる。サーバー間（クラウドモード）統合で、`external_id` のないユーザーをBrazeに送る方法については、マップ方法のセクションを参照のこと。

{% enddetails %}

{% details Brazeの初期化をカスタマイズする。 %}

Brazeのカスタマイズには、プッシュ、アプリ内メッセージ、コンテンツカード、初期化など、いくつかの方法がある。サイドバイサイドの統合でも、Brazeとの直接統合と同様に、プッシュ、アプリ内メッセージ、コンテンツカードをカスタマイズできる。

しかし、Braze SDKを統合する際のカスタマイズや初期化設定の指定は困難であり、場合によっては不可能なこともある。これは、Segmentの初期化時にBraze SDKが初期化されるためである。

{% enddetails %}

{% details ブレーズにデルタを送る。 %}

ユーザー属性データを渡すときは、前回の更新以降に変更された属性の値のみを渡すようにする。こうすることで、不必要にデータポイントを消費することがなくなる。クライアント側のソースについては、Segmentのオープンソースの[ミドルウェアツールを](https://github.com/segmentio/segment-braze-mobile-middleware)使用して、統合を最適化し、Segmentからの重複した`identify()` 呼び出しをデバウンスすることで、データポイントの使用量を制限する。 

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
