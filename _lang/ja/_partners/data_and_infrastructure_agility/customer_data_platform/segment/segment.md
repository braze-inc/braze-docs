---
nav_title: Segment
article_title:セグメント
page_order:1
alias: /partners/segment/
description:"この参考記事では、Brazeと、マーケティングスタック内のソース間の情報収集とルーティングを行う顧客データプラットフォームSegmentのパートナーシップについて概説している。"
page_type: partner
search_tag:Partner

---

# セグメント

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [セグメンテーションは][5]、顧客データの収集、クリーニング、活性化を支援する顧客データプラットフォームである。 

Brazeとセグメンテーションの統合により、ユーザーを追跡し、様々なユーザー分析プロバイダーにデータをルーティングすることができる。セグメンテーションでは以下のことができる：
- Brazeキャンペーンとキャンバスセグメンテーションで使用するために、[セグメントエンゲージを]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_engage/)Brazeに同期する。
- [2つのプラットフォーム間でデータをインポート](#integration-options)する。お客様のAndroid、iOS、Webアプリケーション用のサイドバイサイドSDKインテグレーションと、お客様のデータをBrazeのREST APIに同期させるためのサーバー間インテグレーションを提供。
- [Currentsを通じてデータをセグメンテーションに接続]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/)する。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| セグメンテーション・アカウント | このパートナーシップを利用するには、[セグメンテーション・アカウントが](https://app.segment.com/login)必要である。 |
| インストールされたソースとSegmentソース[ライブラリー](https://segment.com/docs/sources/) | モバイルアプリ、Webサイト、バックエンドサーバーなど、Segmentに送信されたデータのオリジン。<br><br>`Source > Destination` フローを設定する前に、アプリ、サイト、またはサーバーにライブラリをインストールする必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Brazeとセグメンテーションを統合するには、[選択した統合タイプ](#integration-options)（接続モード）に従って、[Brazeを](#connection-settings)送信先に設定する必要がある。Brazeの新規顧客であれば、[セグメンテーションリプレイを使って](#segment-replays)過去のデータをBrazeに中継することができる。次に、Brazeとセグメンテーション間のスムーズなデータフローを確保するために、[マッピングを](#methods)設定し、[統合をテスト](#step-4-test-your-integration)する必要がある。

### ステップ1:送信先を作成する {#connection-settings}

ソースの設定に成功したら、各ソース（iOS、Android、Webなど）の[送信](https://segment.com/docs/destinations/)先としてBrazeを設定する必要がある。接続設定を使用して、Brazeとセグメンテーション間のデータフローをカスタマイズする多くのオプションがある。

### ステップ2:送信先フレームワークと接続タイプを選ぶ {#integration-options}

セグメンテーションで、**送信先＞Braze＞Configure Braze＞ソースを選択＞Setupと**進む。

![ソースの設定ページ。このページでは、送信先フレームワークを「アクション」または「クラシック」のいずれかに設定し、接続モードを「クラウドモード」または「デバイスモード」のいずれかに設定する。][42]

Segmentのウェブソース（Analytics.js）とネイティブクライアントサイドライブラリーは、サイドバイサイド（デバイスモード）統合またはサーバー間（クラウドモード）統合のいずれかを使用して、Brazeと統合することができる。

接続モードの選択は、送信先が設定されているソースのタイプによって決定される。

| 統合 | 詳細 |
| ----------- | ------- |
| [サイド・バイ・サイド<br>(デバイスモード)](#side-by-side-sdk-integration) |セグメンテーション's SDK to translate events into Braze'のネイティブコールを使用し、サーバー間の統合よりも深い機能へのアクセスとBrazeのより包括的な利用を可能にする。<br><br>セグメンテーションは、すべてのBrazeメソッド（例えばコンテンツカード）をサポートしているわけではない。対応するマッピングを通してマッピングされていないBrazeメソッドを使用するには、コードベースにネイティブのBrazeコードを追加してメソッドを呼び出す必要がある。 |
| [サーバー間<br>(クラウドモード）](#server-to-server-integration) | SegmentからBraze REST APIエンドポイントにデータを転送する。<br><br>アプリ内メッセージング、コンテンツカード、プッシュ通知などのBraze UI機能には対応していない。また、デバイスレベルのフィールドのように、この方法では利用できない、自動的にキャプチャされたデータも存在する。<br><br>これらの機能を使いたい場合は、サイド・バイ・サイドの統合を検討しよう。|
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
2つの統合オプション（接続モード）について、それぞれの利点を含め、詳しくは[Segmentを](https://segment.com/docs/destinations/#connection-modes)ご覧いただきたい。
{% endalert %}

#### サイド・バイ・サイドSDKの統合

デバイスモードとも呼ばれるこの統合は、SegmentのSDKと[メソッドを](#methods)Braze SDKにマッピングし、プッシュ、アプリ内メッセージング、Brazeネイティブのその他のメソッドなど、当社のSDKが提供するすべての機能にアクセスできるようにする。 

{% alert note %}
セグメンテーションのデバイスモードを使用する場合、Braze SDKを直接統合する必要はない。Segmentのデバイスモード送信先としてBrazeを追加する場合、Segment SDKはBraze SDKを初期化し、関連するマッピングされたBrazeメソッドを呼び出す。
{% endalert %}

デバイスモード接続を使用する場合、Braze SDKをネイティブに統合するのと同様に、Braze SDKはすべてのユーザーに`device_id` とバックエンド識別子`braze_id` を割り当てる。これによりBrazeは、`userId` の代わりにこれらの識別子を照合することで、デバイスからの匿名アクティビティをキャプチャできる。 

{% tabs local %}
{% tab Android %}

{% alert important %}
Androidデバイスモード統合のソースコードはBrazeによって管理されており、新しいBraze SDKのリリースに合わせて定期的に更新される。

<br>
使用するBraze SDKは、使用するセグメンテーションSDKによって異なる：

| セグメンテーションSDK｜Braze SDK｜Braze SDK｜Braze SDK
| - | ----------- | --------- |
| 優先｜[分析-Kotlin](https://github.com/segmentio/analytics-kotlin)｜[セグメンテーションKotlin](https://github.com/braze-inc/braze-segment-kotlin)
| レガシー｜[分析-Android](https://github.com/segmentio/analytics-android)｜[Braze Segment Android](https://github.com/braze-inc/braze-segment-android)｜[セグメンテーション-Android](https://github.com/braze-inc/braze-segment-android)｜レガシー
{: .reset-td-br-1 .reset-td-br-2}


{% endalert %}

Androidソースのデバイスモード送信先としてBrazeを設定するには、デスティネーションフレームワークとして**Classicを**選択し、**Saveを**クリックする。 

![\]({% image_buster /assets/img/segment/android.png %})

サイドバイサイドの統合を完了するには、Segmentの[Android](https://segment.com/docs/connections/sources/catalog/libraries/mobile/kotlin-android/destination-plugins/braze-kotlin-android/)アプリにBrazeの送信先依存関係を追加するための詳細な手順を参照する。

[Androidデバイスモード](https://github.com/braze-inc/braze-segment-kotlin)統合のソースコードはBrazeによって管理されており、新しいBraze SDKのリリースに合わせて定期的に更新される。

{% endtab %}
{% tab iOS %}

{% alert important %}
iOSデバイスモード統合のソースコードはBrazeによって管理されており、新しいBraze SDKのリリースに合わせて定期的に更新される。

<br>
使用するBraze SDKは、使用するセグメンテーションSDKによって異なる：

| セグメンテーションSDK｜Braze SDK｜Braze SDK｜Braze SDK
| - | ----------- | --------- |
| Preferred |[Analytics-Swift](https://github.com/segmentio/analytics-swift)\|[セグメンテーションSwift](https://github.com/braze-inc/braze-segment-swift)\|
| レガシー｜[アナリティクスiOS](https://github.com/segmentio/analytics-ios)｜[セグメンテーションiOS](https://github.com/Appboy/appboy-segment-ios)
{: .reset-td-br-1 .reset-td-br-2}
{% endalert %}

iOSソースのデバイスモード送信先としてBrazeを設定するには、送信先フレームワークとして**Classicを**選択し、**Saveを**クリックする。 

![\]({% image_buster /assets/img/segment/ios.png %})

サイドバイサイドの統合を完了するには、[iOS](https://segment.com/docs/connections/sources/catalog/libraries/mobile/apple/destination-plugins/braze-swift/)アプリにセグメンテーションポッドを追加するためのSegmentの詳細な手順を参照する。

[iOSデバイスモード](https://github.com/braze-inc/braze-segment-swift)統合のソースコードはBrazeによって管理されており、新しいBraze SDKのリリースに合わせて定期的に更新される。

{% endtab %}
{% tab Web or JavaScript %}

BrazeをWebソースのデバイスモード送信先として設定するには、セグメンテーションの新しいBraze Web Mode（アクション）フレームワークが推奨される。 

セットアップUIで、送信先フレームワークとして**アクションを**選択し、接続モードとして**デバイス**モードを選択する。

![\]({% image_buster /assets/img/segment/website.png %})

{% endtab %}
{% tab React Native %}
[React Native Brazeプラグ](https://github.com/segmentio/analytics-react-native/tree/master/packages/plugins/plugin-braze)インのソースコードはセグメンテーションによって管理されており、新しいBraze SDKのリリースに合わせて定期的に更新されている。

React NativeセグメンテーションソースをBrazeに接続する場合、オペレーティングシステムごとにソースと送信先を設定する必要がある。例えば、iOSの送信先とAndroidの送信先を設定する。 

アプリのコードベース内で、各アプリに関連付けられたそれぞれのソース書き込みキーを使用して、デバイスタイプ別にセグメンテーションSDKを条件付きで初期化する。

デバイスからプッシュトークンが登録され、Brazeに送信されると、SDKの初期化時に使用されたアプリ識別子と関連付けられる。デバイスタイプの条件付き初期化は、Brazeに送信されるプッシュトークンが関連アプリに関連付けられていることを確認するのに役立つ。

{% alert important %}
React Nativeアプリがすべてのデバイスで同じBrazeアプリ識別子でBrazeを初期化する場合、すべてのReact NativeユーザーはBrazeでAndroidまたはiOSユーザーとみなされ、すべてのプッシュトークンはそのオペレーティングシステムに関連付けられる。
{% endalert %}

Brazeを各ソースのデバイスモード送信先として設定するには、送信先フレームワークとして**Classicを**選択し、**Saveを**クリックする。

{% endtab %}
{% endtabs %}

#### サーバー間の統合

クラウドモードとも呼ばれるこの統合は、SegmentからBraze's REST APIs. Use Segment'の新しい[Brazeクラウドモード（アクション）](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/)フレームワークにデータを転送し、任意のソースにクラウドモードの送信先を設定する。 

サイド・バイ・サイドの統合とは異なり、サーバー間統合では、アプリ内メッセージング、コンテンツカード、自動プッシュトークン登録といったBrazeのUI機能はサポートされない。また、クラウドモードでは利用できない[自動取得]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection)データ（匿名ユーザーやデバイスレベルのフィールドなど）も存在する。

このデータとこれらの機能を使用したい場合は、サイド・バイ・サイド（デバイスモード）SDK統合の使用を検討すること。

[Brazeクラウドモード（アクション）送信](https://github.com/segmentio/action-destinations/tree/main/packages/destination-actions/src/destinations/braze)先のソースコードは、セグメンテーションによって管理されている。

### ステップ3:設定

送信先の設定を定義する。すべての設定がすべての送信先タイプに適用されるわけではない。

{% tabs local %}
{% tab Mobile Device-Mode %}

| 設定 | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。Brazeダッシュボードの「**設定の管理**」で確認できる。 | 
| カスタムAPIエンドポイント<br>(SDKエンドポイント) | インスタンスに対応するBraze SDKエンドポイント (`sdk.iad-01.braze.com` など) | 
| エンドポイント領域 | Brazeインスタンス（US 01、US 02、EU 01など） | 
| アプリ内メッセージの自動登録をイネーブルメントにする | アプリ内メッセージを手動で登録したい場合は無効にする。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Web Device-Mode %}

| 設定 | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。Brazeダッシュボードの「**設定の管理**」で確認できる。 | 
| カスタムAPIエンドポイント<br>(SDKエンドポイント) | インスタンスに対応するBraze SDKエンドポイント (`sdk.iad-01.braze.com` など) | 
| SafariのWebサイト・プッシュID | Safariプッシュをサポートしている場合、Safariプッシュ証明書を作成する際にAppleに提供したWebサイトプッシュID（`web` で始まる、たとえば、`web.com.example.domain` ）をこのオプションに指定する必要がある。 |
| Braze Web SDKバージョン | 使用したいBraze Web SDKのバージョン |
| アプリ内メッセージを自動送信する | デフォルトでは、ユーザーが受信可能なアプリ内メッセージはすべて自動的にユーザーに配信される。アプリ内メッセージを手動で表示したい場合は、これを無効にする。 |
| 素晴らしいフォントを読み込まない | Brazeはアプリ内メッセージアイコンにFont Awesomeを使用している。デフォルトでは、Brazeは自動的にFontAwesome CDNからFontAwesomeを読み込む。この行動を無効にするには（例えば、あなたのサイトが FontAwesome のカスタマイズバージョンを使用しているため）、このオプションを`TRUE` に設定する。これを行う場合、FontAwesomeがあなたのサイトに読み込まれていることを確認する責任があることに注意すること - そうでない場合、アプリ内メッセージが正しくレンダリングされない可能性がある。 |
| HTMLアプリ内メッセージをイネーブルメントにする | このオプションをイネーブルメントにすると、BrazeダッシュボードユーザーがHTMLアプリ内メッセージを使用できるようになる。 | 
| アプリ内メッセージを新しいタブで開封する | デフォルトでは、アプリ内メッセージクリックからのリンクは、メッセージごとにダッシュボードで指定された現在のタブまたは新しいタブに読み込まれる。このオプションを`TRUE` に設定すると、アプリ内メッセージのクリックからのリンクはすべて新しいタブまたはウィンドウで開封される。 |
| アプリ内メッセージ z インデックス | Brazeのデフォルトのz-indexを上書きするには、このオプションに値を指定する。 | 
| アプリ内メッセージの明示的な解除を要求する。 | デフォルトでは、アプリ内メッセージが表示されている場合、エスケープボタンを押すか、ページのグレーアウトしたバックグラウンドをクリックすると、メッセージが解除される。このオプションをtrueに設定すると、この動作を防ぎ、メッセージングを解除するために明示的なボタンクリックを要求する。 |
| トリガーアクション間の最小間隔（秒 | デフォルトは30である。<br>デフォルトでは、トリガーアクションは、最後のトリガーアクションから少なくとも30秒が経過した場合にのみ発火する。このコンフィギュレーション・オプションに値を指定すると、デフォルトを独自の値で上書きすることができる。ユーザーへのスパム通知を避けるため、この値を10より小さくすることは推奨しない。|
| サービス従業員の所在地 | デフォルトでは、ユーザーをWebプッシュ通知に登録する際、BrazeはWebサーバーのルートディレクトリ`/service-worker.js` にある必要なサービスワーカーファイルを探す。サーバー上の別のパスでサービスワーカーをホストしたい場合、このオプションにファイルへの絶対パスを指定する。(例えば、`/mycustompath/my-worker.js`)。ここで値を設定すると、サイト上でのプッシュ通知の範囲が制限されることに注意。例えば、上記の例では、サービスワーカーファイルは`/mycustompath/` ディレクトリ内にあるため、`requestPushPermission` は`http://yoursite.com/mycustompath/` で始まる Web ページからのみ呼び出すことができる。 |
| プッシュトークンのメンテナンスを無効にする | デフォルトでは、Webプッシュ権限を付与済みのユーザーは、配信可能性を確保するため、新規セッション時にプッシュトークンをBrazeバックエンドと自動的に同期する。この動作を無効にするには、このオプションを`FALSE` に設定する。 |
| サービス・ワーカーを外部で管理する | 登録し、ライフサイクルをコントロールする独自のサービスワーカーがある場合、このオプションを`TRUE` に設定すると、Braze SDKはサービスワーカーを登録または登録解除しない。このオプションを`TRUE` に設定した場合、プッシュが正しく機能するためには、`requestPushPermission` を呼び出す前に自分でサービスワーカーを登録し、`self.importScripts('https://js.appboycdn.com/web-sdk-develop/4.1/service-worker.js');` を使うか、そのファイルの内容を直接インクルードして、Brazeのサービスワーカーコードが含まれていることを確認する必要がある。このオプションが`TRUE` の場合、`serviceWorkerLocation` オプションは無関係であり、無視される。 |
| コンテンツ・セキュリティ・ノンス | このオプションに値を指定すると、Braze SDKは、SDKによって作成された`<script>` および`<style>` 要素にnonceを追加する。これにより、Braze SDKがWebサイトのコンテンツセキュリティポリシーと連動できるようになる。このnonceの設定に加えて、FontAwesomeの読み込みを許可する必要があるかもしれない。これは、コンテンツセキュリティポリシーのallowlistに`use.fontawesome.com` を追加するか、`doNotLoadFontAwesome` オプションを使用して手動で読み込むことでできる。 |
| クローラーの活動を許可する | デフォルトでは、Braze Web SDKは、ユーザーエージェント文字列に基づいて、Googleなどの既知のスパイダーやWebクローラーからのアクティビティを無視する。これにより、データポイントが節約され、分析がより正確になり、ページランクが向上する可能性がある。ただし、Brazeにこれらのクローラーからの活動を記録させたい場合は、このオプションを`TRUE` に設定することができる。 |
| ロギングをイネーブルメントにする | デフォルトでロギングをイネーブルメントにするには、`TRUE` に設定する。これにより、BrazeはJavaScriptコンソールにログを記録し、すべてのユーザーに見えるようになる。ページを本番環境にリリースする前に、これを削除するか、代替のロガーを`setLogger` で提供すべきである。 |
| ニュースフィードのカードを新しいタブで開く（カードを新しいタブで開く） | デフォルトでは、カードオブジェクトからのリンクは現在のタブやウィンドウに読み込まれる。このオプションを`TRUE` に設定すると、カードからのリンクが新しいタブまたはウィンドウで開封されるようになる。<br><br>**Note:** ニュースフィードは廃止される。Braze は、ニュースフィードツールを使っている顧客には、コンテンツカードのメッセージングチャネルに移行することを勧めています。詳しくは[マイグレーションガイド]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/)をご覧ください。 |
| ユーザー提供のJavaScriptを許可する | デフォルトでは、Braze Web SDKは、ユーザーが提供するJavaScriptのクリックアクションを許可しない。これは、ダッシュボードユーザーがサイト上でJavaScriptを実行できるようにするためである。ダッシュボードユーザーが悪意のないJavaScriptクリックアクションを記述することを信頼することを示すには、このプロパティを`TRUE` に設定する。`enableHtmlInAppMessages` が`TRUE` の場合、このオプションも`TRUE` に設定される。 |
| アプリ版| このオプションに値を指定すると、Brazeに送信されたユーザーイベントは、指定されたバージョンに関連付けられ、ユーザーセグメンテーションに使用できる。 |
| セッションタイムアウト（秒 | デフォルトは30である。<br>デフォルトでは、セッションは30分間使用されないとタイムアウトする。このコンフィギュレーション・オプションに値を指定すると、デフォルトを独自の値で上書きすることができる。 | 
| デバイスプロパティ allowlist | デフォルトでは、Braze SDKは自動的にすべてのデバイスプロパティを検出し、`DeviceProperties` で収集する。この動作をオーバーライドするには、`DeviceProperties` の配列を指定する。いくつかのプロパティがないと一部の機能が正しく機能しないことがあるので注意してください。たとえば、ローカルタイムゾーンの配信はタイムゾーンなしでは機能しません。 |
| ローカライゼーション | デフォルトでは、SDKが生成したユーザー可視メッセージは、ユーザーのブラウザ言語で表示される。その動作をオーバーライドして特定の言語を強制するには、このオプションに値を指定する。このオプションの値はISO 639-1言語コードでなければならない。 |
| クッキーなし | デフォルトでは、Braze SDKは少量のデータ（ユーザーID、セッションID）をCookieに保存する。これは、Brazeがサイトの異なるサブドメイン間でユーザーとセッションを認識できるようにするためである。これが問題になる場合は、このオプションに`TRUE` を渡してCookieの保存を無効にし、HTML 5のlocalStorageに完全に依存してユーザーとセッションを識別する。 |
| すべてのページをトラッキングする | **クラシック送信先Webデバイスモード（保守）のみ**<br><br>セグメンテーションでは、[マッピングによって](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)この設定を[イネーブルメントに](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)できるWeb Actionsフレームワークの送信先への移行を推奨している。<br><br>これにより、すべての[ページ呼び出しが](https://segment.com/docs/spec/page/)"Loaded/Viewed a Page "イベントとしてBrazeに送られる。 |
| 指定されたページのみトラッキング, 追跡 | **クラシック送信先Webデバイスモード（保守）のみ**<br><br>セグメンテーションでは、[マッピングによって](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)この設定を[イネーブルメントに](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)できるWeb Actionsフレームワークの送信先への移行を推奨している。<br><br>これは、Brazeに、その名前に関連するページコールのみを送信する。 |
| 収益がある場合、購入を記録する | **クラシック送信先Webデバイスモード（保守）のみ**<br><br>セグメンテーションでは、[マッピングによって](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)この設定を[イネーブルメントに](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)できるWeb Actionsフレームワークの送信先への移行を推奨している。<br><br>このオプションをイネーブルメントにすると、収益プロパティを持つすべてのトラッキング・コールが購入イベントをトリガーする。 | 
| 既知のユーザーのみをトラッキング追跡する | **クラシック送信先Webデバイスモード（保守）のみ**<br><br>セグメンテーションでは、マッピングによってこの設定をイネーブルメントにできるWeb Actions Framework送信先への移行を推奨している。<br><br>イネーブルメントが有効な場合、この新しい設定は、有効な`userId` まで、`window.appboy.initialize` の呼び出しを遅らせる。 | 
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Cloud-Mode %}

| 設定 | 説明 |
| ------- | ----------- |
| アプリ識別子 | 特定のアプリを参照するためのアプリ識別子。Brazeダッシュボードの「**設定の管理**」で確認できる。 | 
| REST APIキー | これは、ダッシュボードの「**設定」**>「**APIキー**」で確認できる。 | 
| カスタムREST APIエンドポイント | インスタンスに対応するBraze RESTエンドポイント（rest.iad-01.braze.comなど）。 | 
| 既存ユーザーのみを更新する | **クラシック送信先 クラウドモード（メンテナンス）のみ**<br><br>セグメンテーションは、[マッピングによって](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)この設定を[有効に](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#braze-web-settings-mapping)できるCloud Actions Framework送信先への移行を推奨している。<br><br>既存のユーザーのみを更新するかどうかを決定する。 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

### ステップ 4:地図メソッド {#methods}

Brazeは、[Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page)、[Identify](https://segment.com/docs/spec/identify/)、[Track](https://segment.com/docs/spec/track/)Segmentメソッドをサポートしている。これらの方法で使用される識別子の種類は、データがサーバー間（クラウドモード）で送信されるのか、サイドバイサイド（デバイスモード）で送信されるのかによって異なる。Braze Web Mode ActionsとCloud Mode Actionsの送信先では、[セグメンテーションエイリアス通話の](https://segment.com/docs/connections/spec/alias/)マッピング設定を選択することもできる。 

{% alert note %}
ユーザーエイリアスは、Brazeクラウドモード（アクション）送信先の識別子としてサポートされているが、セグメンテーションのエイリアス呼び出しは、Brazeユーザーエイリアスとは直接関係ないことに注意すべきである。
{% endalert %}

| 識別子タイプ | 対応送信先 |
| --------------- | --------------------- |
| `userId` (`external_id`) | すべて |
| 匿名ユーザー | デバイスモードの送信先 |
| ユーザーエイリアス | クラウドモードの送信先 |
{: .reset-td-br-1 .reset-td-br-2}

クラウドモードのアクション送信先には、[エイリアスの作成アクションが](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#create-alias)あり、エイリアスのみのユーザーを作成したり、既存の`external_id` プロファイルにエイリアスを追加したりすることができる。[ユーザーの識別（Identify User）アクションは](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#identify-user)、エイリアスの作成（Create Alias）アクションと一緒に使用することができ、エイリアスのみのユーザーが`external_id` 、そのユーザーに使用できるようになった後にマージすることができる。 

回避策を開発し、`braze_id` 、クラウドモードで匿名のユーザーデータを送信することも可能だ。そのため、すべてのSegment APIコールにユーザーの`braze_id` を手動で含める必要がある。この回避策の設定方法については、[セグメンテーションのドキュメントを](https://segment.com/docs/connections/destinations/catalog/braze/#capture-the-braze_id-of-anonymous-users)参照されたい。

Brazeに送信される送信先データは、クラウドモードアクション内でバッチ処理できる。バッチサイズのキャップは75イベントであり、これらのバッチはフラッシュされる前に30秒間蓄積される。リクエストのバッチ処理はアクションごとに行われる。例えば、識別子コール（アトリビューション）はリクエストにバッ チされ、トラッキングコール（カスタムイベント）は2番目のリクエストにバッ チされる。セグメンテーションからBrazeに送信されるリクエストの数を減らすことができるため、Brazeはこの機能をイネーブルメントにすることを推奨している。その結果、送信先がBrazeのレート制限にかかり、リクエストを再試行するリスクを減らすことができる。 

Braze Destination >**Mappingsに**移動して、アクションのバッチ処理をオンにすることができる。そこから、マッピングの右側にある3つの点のアイコンをクリックし、**マッピングの編集を**選択する。**Select mappings**セクションの一番下までスクロールし、**Batch Data to Brazeが** **Yesに**設定されていることを確認する。


{% tabs local %}
{% tab Identify %}
#### 識別子

[Identify](https://segment.com/docs/spec/identify/)コールは、ユーザーをそのアクションに結びつけ、そのユーザーに関する属性を記録することができる。 

特定のSegmentの特殊特性は、Brazeの標準属性プロファイル項目にマッピングされている：

| セグメンテーションの特徴 | アトリビューション標準属性項目 |
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

`email_subscribe` 、`push_subscribe` などのその他の予約Brazeプロファイルフィールドは、Brazeのこれらのフィールドの命名規則を使用し、識別子呼び出し内で形質として渡すことで送信できる。

##### ユーザーをサブスクリプショングループに追加する

traits パラメータの以下のフィールドを使用して、指定されたサブスクリプショングループからユーザーをサブスクライブまたはサブスクライブ停止することもできる。

`braze_subscription_groups` という予約Brazeプロファイルフィールドを使用し、オブジェクトの配列と関連付けることができる。配列の各オブジェクトは、2つの予約キーを持たなければならない：

1. `subscription_group_state`:ユーザーが特定のサブスクリプショングループに対して`"subscribed"` または`"unsubscribed"` のどちらであるかを示す。
2. `subscription_group_id`:サブスクリプショングループの一意な ID を表す。このIDは、Brazeダッシュボードの**サブスクリプショングループ管理で**確認できる。

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

| セグメンテーション方式 | Braze法 | 例 |
|---|---|---|
| ユーザーIDによる識別子 | 外部IDを設定する | Segment:  `analytics.identify("dawei");`<br>Braze: `Braze.changeUser("dawei")` |
| 予約特性を識別子とする | ユーザー属性を設定する | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `Braze.getUser().setEmail("dawei@braze.com");`
| カスタムの特徴を識別する | カスタム属性を設定する | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Braze: `Braze.getUser().setCustomAttribute("fav_cartoon": "Naruto")`;
| ユーザーIDと特徴を識別する | Segment: 外部IDと属性を設定する | 先の方法を組み合わせる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

[Web Mode Actionsと](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#update-user-profile) [Cloud Mode Actionsの](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#update-user-profile)送信先では、Update User Profile Actionを使用して上記のマッピングを設定できる。

{% alert important %}
ユーザー属性データを渡す際には、前回の更新以降に変更された属性の値のみを渡すようにする。こうすることで、データ割り当てに不必要にデータポイントを消費することがなくなる。クライアント側のソースについては、Segmentのオープンソースの[ミドルウェアツールを](https://github.com/segmentio/segment-braze-mobile-middleware)使用して、統合を最適化し、Segmentからの重複した`identify()` 呼び出しをデバウンスすることによって、データポイントの使用量を制限する。 

{% endalert %}
{% endtab %}

{% tab Track %}
#### トラッキング、 追跡

あなたがイベントをトラッキングするとき、私たちはそのイベントを、提供された名前を使用して[カスタムイベントとして]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)記録する。 

トラックコールのプロパティオブジェクト内で送信されたメタデータは、関連イベントのカスタムイベントプロパティとしてBrazeに記録される。すべての[カスタムイベントプロパティのデータ型が](https://www.braze.com/docs/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)サポートされている。

[Web Mode Actionsと](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-event) [Cloud Mode Actionsの](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-event)送信先では、Track Event Actionを使って上記のマッピングを設定できる。

| セグメンテーション方式 | Braze法 | 例 |
|---|---|---|
| [トラッキング、 追跡](https://segment.com/docs/spec/track/) | [カスタムイベントとして]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)記録される。 | Segment: `analytics.track("played_game");`<br>Braze: `Braze.logCustomEvent("played_game");`|
| [プロパティでトラッキング、追跡](https://segment.com/docs/spec/track/) | [イベントプロパティとして]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties)記録される。 | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});`<br>Braze: `Braze.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [トラッキング、製品追跡](https://segment.com/docs/spec/track/) | [購入イベントとして]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)記録される。 | Segment: `analytics.track("Order Completed", {products: [product_id: "ab12", price: 19]});`<br>Braze: `Braze.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

##### 注文完了 {#order-completed}

Segmentの[eコマースAPIに](https://segment.com/docs/spec/ecommerce/v2/)記載されているフォーマットを使用して、`Order Completed` という名前でイベントをトラッキング追跡すると、あなたが[購入として]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data)リストアップした商品が記録される。

[Web Mode Actionsと](https://segment.com/docs/connections/destinations/catalog/braze-web-device-mode-actions/#track-purchase) [Cloud Mode Actionsの](https://segment.com/docs/connections/destinations/catalog/braze-cloud-mode-actions/#track-purchase)送信先では、Track Purchase Actionでデフォルトマッピングをカスタマイズできる。

{% endtab %}

{% tab Page %}
#### ページ {#page}

[Page](https://segment.com/docs/spec/page/)コールは、ユーザーがWebサイトのページを見たときに、ページに関する任意のプロパティとともに記録することができる。

このイベントタイプは、Web Mode ActionsとCloud Actionsの送信先でトリガーとして使用し、カスタムイベントをBrazeに記録することができる。
{% endtab %}

{% endtabs %}

### ステップ 5: 連携のテスト

サイドバイサイド（デバイスモード）統合を使用する場合、[概要][27]メトリクス（ライフタイムセッション、MAU、DAU、スティッキネス、デイリーセッション、MAUあたりのデイリーセッション）を使用して、BrazeがSegmentからデータを受信していることを確認することができる。

[カスタムイベントや][22] [収益][28]ページ、または[セグメンテーションを作成][23]することで顧客データを見ることができる。ダッシュボードの**カスタムイベントページでは**、カスタムイベントのカウントを時系列で見ることができる。サーバー間（クラウドモード）統合を使用している場合、MAUとDAU統計を含む[計算式を][24]使用することはできないことに注意。

購入データをBrazeに送信している場合（[ステップ](#methods)3の**Track**タブで完了した注文を参照）、[収益][28]ページで特定の期間の収益や購入に関するデータ、またはアプリの総収益を確認できる。

[セグメントを作成すること][26]で、カスタムイベントと属性データに基づいてユーザーをフィルターすることができる。

{% alert important %}
サーバー間統合（クラウドモード）を使用している場合、自動的に収集されたセッションデータ（「最初に使用したアプリ」や「最後に使用したアプリ」など）に関連するフィルターは機能しない。セグメンテーションとBrazeの統合でこれらを使用したい場合は、サイドバイサイド統合（デバイスモード）を使用する。
{% endalert %}

## ユーザーの削除と抑制 

ユーザーを削除または抑制する必要がある場合、[Segmentのユーザー削除](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **機能は**、Braze[`/users/delete` エンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)マッピングされていることに注意。これらの削除の検証には最大30日かかる可能性があることに注意してほしい。

Brazeとセグメンテーションで共通のユーザー識別子を選択する必要がある（`external_id` のように）。Segmentで削除リクエストを開始すると、Segmentダッシュボードの削除リクエストタブでステータスを確認できる。

## セグメンテーション・リプレイ

セグメンテーションはクライアントに、すべての過去データを新しいテクノロジーパートナーに「再生」するサービスを提供している。関連するすべての履歴データをインポートしたい新規Braze顧客は、セグメンテーションを通じてインポートできる。興味があれば、セグメンテーション担当者に相談してほしい。

Segmentが当社の[`/users/track` エンドポイントに]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)接続し、ユーザーに代わってユーザーデータをBrazeにインポートする。

{% alert important %}
クラウドモード・アクションの送信先でサポートされているすべての識別子は、セグメンテーション・リプレイの一部としてサポートされている。
{% endalert %}

## ベストプラクティス

{% details Review use cases to avoid data overages. %}

**セグメンテーションは**、クライアントが送信するデータエレメントの数を制限しない。セグメンテーションにより、Brazeに送信するイベントをすべて送信するか決定することができる。すべてのイベントをセグメンテーションを使って送信するのではなく、マーケティングチームや編集チームとユースケースを検討し、データ超過料金を避けるためにどのイベントをBrazeに送信するかを決定することをお勧めする。

{% enddetails %}

{% details Understand the difference between the custom API endpoint and the custom REST API endpoint in the Mobile Device Mode destination settings. %}

| ブレイズ用語 | セグメンテーション相当額 |
| ----------------- | ------------------ |
| Braze SDKエンドポイント | カスタムAPIエンドポイント |
| Braze RESTエンドポイント | カスタムREST APIエンドポイント |
{: .reset-td-br-1 .reset-td-br-2}

あなたのBraze APIエンドポイント(Segmentでは「カスタムAPIエンドポイント」と呼ばれる)は、BrazeがあなたのSDKのために設定するSDKエンドポイントである(例えば、`sdk.iad-03.braze.com`)。あなたのBraze REST APIエンドポイント(セグメンテーションでは「カスタムREST APIエンドポイント」と呼ばれる)は、REST APIエンドポイント(例えば、`https://rest.iad-03.braze.com`)である。
{% enddetails %}

{% details Ensure your custom API endpoint is correctly input into the mobile device mode destination settings. %}

| ブレイズ用語 | セグメンテーション相当額 |
| ----------------- | ------------------ |
| Braze SDKエンドポイント | カスタムAPIエンドポイント |
| Braze RESTエンドポイント | カスタムREST APIエンドポイント |
{: .reset-td-br-1 .reset-td-br-2}

Braze SDKエンドポイントを正しく入力するために、適切なフォーマットに従う必要がある。あなたのBraze SDKエンドポイントは、`https://` (例えば、`sdk.iad-03.braze.com`)を含んではならない。さもないと、Braze統合は壊れる。これは、Segmentが自動的にエンドポイントの先頭に`https://` を付けるためで、その結果、Brazeは無効なエンドポイント`https://https://sdk.iad-03.braze.com` で初期化される。

{% enddetails %}

{% details Data mapping nuances. %}

データが期待通りに通過しないシナリオ：

1. 階層化カスタム属性
  - [階層化されたカスタム属性は]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/)、技術的にはセグメンテーションを通じてBrazeに送信できるが、**ペイロード全体が**毎回送信される。これにより、ペイロードが送信されるたびに、ネストされたオブジェクトに渡されたキーごとに[データポイントが]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#data-points)発生する。<br><br> ペイロードの送信時にデータポイントのサブセットのみを使用するには、セグメンテーションが所有するカスタム[送信先関数の](https://segment.com/docs/connections/functions/destination-functions/)機能を使用することができる。セグメンテーションプラットフォームのこの機能により、下流の送信先へのデータ送信方法をカスタマイズすることができる。

  {% alert note %}
  カスタム送信先機能はセグメンテーション内でコントロールされ、外部で設定された機能に対するBrazeのインサイトは限られている。
  {% endalert %}

{: start="2"}
2\.匿名データをサーバー間で受け渡す。
  - 顧客は、Segmentのサーバー間ライブラリを使用して、匿名データを他のシステムに流すことができる。サーバー間(クラウドモード)統合で、`external_id` のないユーザーをBrazeに送る方法については、マップ方法のセクションを参照のこと。

{% enddetails %}

{% details Customization of Braze initialization. %}

Brazeのカスタマイズには、プッシュ、アプリ内メッセージ、コンテンツカード、初期化などいくつかの方法がある。サイドバイサイドの統合でも、Brazeとの直接統合と同様に、プッシュ、アプリ内メッセージ、コンテンツカードをカスタマイズできる。

しかし、Braze SDKを統合する際のカスタマイズや初期化設定の指定は困難であり、場合によっては不可能なこともある。これは、Segmentの初期化時にBraze SDKが初期化されるためである。

{% enddetails %}

{% details Sending deltas to Braze. %}

ユーザー属性データを渡す際には、前回の更新以降に変更された属性の値のみを渡すようにする。こうすることで、データ割り当てに不必要にデータポイントを消費することがなくなる。クライアント側のソースについては、セグメンテーションのオープンソースの[ミドルウェアツールを](https://github.com/segmentio/segment-braze-mobile-middleware)使用して、統合を最適化し、セグメンテーションからの重複した`identify()` 呼び出しをデバウンスすることで、データポイントの使用量を制限する。 

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
