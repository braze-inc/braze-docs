---
nav_title: Shopify概要
article_title: "Shopify概要"
description: "このリファレンス記事では、Braze と Shopify のパートナーシップについて説明します。Shopify はグローバルなコマース企業であり、Shopify ストアを Brazeとシームレスに接続して、選択した Shopify Webhook を Braze に渡すことができます。Braze クロスチャネル戦略とキャンバスを活用して、顧客が購入を完了するように促し、購入履歴に基づいてユーザーをリターゲティングできます。"
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Shopify概要

> [Shopify](https://www.shopify.com/) は、規模を問わずビジネスの開始、成長、売買、管理のための信頼できるツールを提供する世界的なコマースのリーディングカンパニーです。Shopifyは、信頼性の高いプラットフォームとサービスを提供し、世界中の消費者により良いショッピング体験を提供することで、すべての人にとって商取引をより良くします。

ShopifyとのBrazeインテグレーションは、自社のカスタマーエンゲージメントを高め、パーソナライズされた マーケティング活動を推進しようとするイーコマース事業者にとって、強力なソリューションを提供する。このインテグレーションシームレスには、Shopifyの堅牢なeコマース機能を高度なカスタマーエンゲージメント プラットフォームに接続し、リアルタイムの買い物行動やアクションデータに基づいて、ターゲットを絞った、関連性のある、タイムリーなメッセージをユーザーに配信することを可能にします。

## 要件

| 要件 | 説明 |
| --- | --- |
| Shopify ストア | Shopify ストアをアクティブにしていること。 |
| Shopify ストアオーナーまたはスタッフの権限 | {::nomarkdown}<ul><li>すべての一般設定とオンラインストア設定にアクセスできること。</li><li> 追加の管理者権限</li><ul><li>注文数:ビュー</li><li>顧客: ReadWrite</li><li>顧客イベントの表示 (Web ピクセル)</li><li>設定の管理</li><li>スタッフ/協力者の開発によるアプリの表示</li><li>アプリとチャネルの管理/インストール</li><li>カスタムピクセルの管理/追加</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合方法 

Braze は、Shopify 加盟店向けに、e コマースビジネスの多様なニーズを満たすように設計された 2 つの統合オプションである**標準的な統合**と**カスタム統合**を提供しています。

{% multi_lang_include shopify.md section='Integration Tabs' %}

## 連携の仕組み

構成設定で履歴バックフィルをすでに設定し、オンにしている場合は、最初のデータ同期がすぐに開始されます。Braze は、Shopify への接続前の過去 90日間のすべての顧客と注文イベントをインポートします。Braze が Shopify の顧客をインポートする際、設定で選択された `external_id` タイプが割り当てられます。

カスタム外部 ID ([標準統合]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users)または[カスタム統合の]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)いずれか) との統合を計画している場合、既存のすべての Shopify 顧客プロファイルに Shopify 顧客メタフィールドとしてカスタム外部 ID を追加し、[履歴バックフィル]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill)を実行する必要があります。 

最初のデータ同期後、Braze は Shopifyと Braze SDK から直接、新しいデータと更新を継続的に追跡します。

{% alert note %}
既存の Braze 顧客で、アクティブなキャンペーンやキャンバスをご利用の場合は、[Shopify の履歴バックフィル]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill)を確認して、重要な情報を入手してください。具体的にどのような顧客データがバックフィルされているかは、[Shopify の機能]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/)で確認してください。
{% endalert %}

### ユーザーとデータの同期

統合が開始された後、Braze は Shopify との統合を通じて、2 つの主要なソースからユーザーデータを収集します。
- **Shopify Web Pixel APIとアプリ埋め込み:**これにより、Braze Web SDK とJavascript SDK の機能が強化され、オンサイトトラッキング、ID 管理、e コマース行動データ、アプリ内メッセージなどのメッセージングチャネルがサポートされます。
- **Shopify の Webhook:** e コマースの行動データ、商品同期、サブスクライバー収集

統合オンボーディングの際に、Braze SDK が初期化され、Shopify サイトを読み込むタイミングを選択する必要があります。 
- サイト訪問時 (セッション開始時など)
    - **実行内容:**ゲスト買い物客などの匿名ユーザーを追跡し、詳細にパーソナライズするためのデータにアクセスします。 
- アカウントログインなどのアカウントの登録時 
    - **実行内容:**より保守的なプライバシー指向の方法で匿名ユーザーの追跡を防止します。そのため、ユーザーのアクティビティはアカウントにサインイン*の後に*追跡されます

{% alert note %}
- Web サイトへの訪問 (セッション) は、月間アクティブユーザー数 (MAU) の配分にカウントされます。
- Braze Web SDK と JavaScript SDK のバージョンは自動的に v5.4.0 に設定されます。
{% endalert %}

Braze は、Shopify の統合を使用して、ユーザーがゲストとしてショッピングを体験してから識別済みのユーザーになるまでを追跡する複数の識別子をサポートしています。

| Braze 識別子 | 説明 |
| --- | --- |
| Braze `device_id` | Braze SDK を通じて匿名ユーザーの活動をトラッキングするために、ブラウザーに保存されるランダムに生成される ID。 |
| カートクンユーザーエイリアス | Braze がカート更新イベントを追跡するために作成するエイリアス。このトークンは、Shopify カートトークンを使用して作成される。 |
| チェックアウトトークンユーザーエイリアス | ユーザーがチェックアウトプロセスを開始する際に Braze が作成するエイリアス。このトークンは、Shopify のチェックアウトトークンを使用して作成されます。 |
| Shopify 顧客 ID エイリアス | Shopify 顧客 ID は、アカウントログイン時または注文時に外部 ID が割り当てられる際にエイリアスとして割り当てられます。 |
| Braze `external_id` | デバイスやプラットフォームを横断して顧客を追跡できるようにする一意の識別子。これにより、ユーザーがデバイスを切り替えたり、アプリを再インストールしたりしても、ユーザープロファイルが複数存在しないため、一貫したユーザーエクスペリエンスが維持され、分析が向上します。<br><br>Shopify との統合では、以下の `external_id` タイプがサポートされます。<br><br>{::nomarkdown}<ul><li>Shopify 顧客 ID (デフォルト)</li><li>カスタム external ID</li><li>ハッシュされたメール (SHA-256)</li><li>ハッシュされたメール (SHA-1)</li><li>ハッシュされたメール (MD5)</li><li>メール</li></ul>{:/}Braze は以下のタイミングで SDK の changeUser メソッドを呼び出すことで、ユーザーに `external_id` を割り当てます。<br><br>{::nomarkdown}<ul><li>ユーザーがログインするか、アカウントを作成する。</li><li>発注が行われている</li></ul>{:/}<br> 匿名プロファイルに `external_id` を割り当てた場合の詳細については、[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users)を参照してください。<br><br>Braze はまた、`external_id` を活用して、Shopify のWebhook から下流の e コマース行動データの属性を設定します。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

この統合には、Braze SDK と Shopify サービスが連携し、Shopify データをほぼリアルタイムで適切に追跡し、適切なユーザーに属性付けする必要があります。統合によって追跡されるデータの詳細については、[Shopify データ]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/)を参照してください。

{% alert note %}
- 統合をテストしている場合は、シークレットモードを使用するか、Cookie をクリアして Braze `device_id` をリセットし、匿名ユーザーの行動を模倣することをお勧めします。
- Shopify の顧客 ID は、Shopify のニュースレターフッターにメールが入力されたときや、注文前のチェックアウトプロセス中に生成されるにもかかわらず、その顧客 ID に Shopify Web Pixels からはアクセスできません。このため、Braze はこの 2 つの状況では `changeUser` を使用できません。
{% endalert %}

### Shopify のメールと SMS マーケティングのオプトインを同期する

設定で購読者収集を有効にした場合は、Braze に接続する各ストアに購読グループを割り当てる必要があります。これにより、顧客はストアの購読グループで「サブスクライバー」または「配信停止」のどちらかに分類されることになります。

メールと SMSマーケティングの Shopify マーケティングオプトインステータスは、以下の方法で更新できます。
- **手動更新:**ユーザーのメールや SMS マーケティングのオプトインステータスは、Shopify の管理で手動で変更できます。
- **Shopify ニュースレターのフッター:**ユーザーが Shopify デフォルトのニュースレターフッターにメールを入力すると、オプトインステータスが更新されます。
- **チェックアウトのプロセス:**ユーザーがチェックアウト中にオプトインのステータスを更新した場合。

{% alert note %}
Shopify からのメールマーケティングオプトインステータスで、Braze のユーザーの [グローバルメールサブスクリプションステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)が変更されることはありません。ユーザープロファイルが作成されたときのデフォルトの購読ステータスは、「購読」になります。必ず、購読グループをキャンペーンまたはキャンバスのエントリ基準の一部として使用するようにしてください。
{% endalert %}

この表は、Shopify マーケティングのオプトインのステータスと購読グループ内のステータスとの関連を示しています。 

| Shopify マーケティングのオプトインステータス | 購読グループのステータス |
| --- | --- |
| メール購読済み | 配信登録済み |
| メールの配信停止 | 配信停止済み |
| メール確認中 | 配信停止済み |
| メールが無効です | 配信停止済み |
| SMS 購読済み | 配信登録済み |
| SMS 配信停止済み | 配信停止済み |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### 登録フォーム

#### Shopifyニュースレターのフッター: 

Shopify のニュースレターフッターにメールアドレスを入力したユーザーは、次のいずれかのワークフローが適用されます。

##### アカウントにログインしていないユーザー

1. 顧客が作成または更新されるたびに、Braze は Shopify のWebhook を受信します。
2. Braze は、そのユーザーに関連付けられているメールアドレスと Shopify 顧客 ID エイリアスを含むユーザープロファイルを作成します。
3. Braze SDK は、メールアドレスで匿名プロファイルを更新します。

{% alert note %}
その結果、アカウントの作成、アカウントにログインしたり、注文を行うなどしてユーザーがユーザー自身を識別可能にするまで、プロファイルに重複が生じることがあります。Braze は、重複プロファイルの照合を自動化するための一括マージツールを提供しています。詳細は[重複ユーザー]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/)を参照してください。
{% endalert %}

##### アカウントにログイン済みのユーザー

Braze は、そのユーザーに関連付けられているメールアドレスと Shopify 顧客 ID エイリアスを含むユーザープロファイルを作成します。Brazeは、ログインユーザーのメールアドレスを更新しない。なぜなら、Shopifyがすでにこの情報を提供していると想定しているからだ。

#### Braze 登録フォーム

Braze は 2 種類の登録フォームテンプレートを提供しています。
- **[メール登録フォーム]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/email_capture/): **ドラッグ＆ドロップエディターを使ってこれらを作成します。
- **[従来のエディターのメールキャプチャフォーム]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/): **メールアドレスを取得するための、よりわかりやすいフォーム。

これらの登録フォームテンプレートを使用すると、Braze は自動的にユーザープロファイルのグローバルメール購読ステータスを更新します。グローバルメール購読のステータスの処理方法についての詳細 (メールの検証に関する情報を含む) については、各フォームテンプレートタイプのドキュメントを参照してください。

{% alert note %}
- キャンペーンまたはキャンバスに、グローバルメール購読ステータスと、Shopify ストアに接続されている購読グループの両方を含む入力基準を必ず含めてください。これにより、適切なオーディエンスをターゲットにしていることを確認できます。 
- Braze は、ブラウザー内メッセージを通じて、メールアドレスや電話番号などの訪問者情報を収集します。この情報はShopify ビジターAPI に送信されますが、Shopify では顧客 プロファイルは作成されません。詳細については、[Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api) を参照してください。
{% endalert %}

#### サードパーティの登録フォーム 

サードパーティのプラットフォームや Shopify のプラグインをサインアップフォームに使用している場合は、フォーム送信からメールアドレスとグローバルメール購読ステータスを取得するために、開発者と協力して Braze SDK コードを統合する必要があります。詳細については、[Shopify 標準統合セットアップと]({{site.baseurl}}/shopify_standard_integration/) [Shopify カスタム統合セットアップ]({{site.baseurl}}/shopify_custom_integration/)を確認します。

### 製品の同期 

Braze は、Shopify ストアの商品を Braze カタログに同期する機能をサポートしています。詳細は、[Shopify product syncs]({{site.baseurl}}/shopify_catalogs/) を参照してください。

## データ主体に関するリクエスト

Braze プラットフォームの Shopify 統合の一環として、Braze は自動的に [Shopify のコンプライアンス webhook](https://shopify.dev/docs/apps/build/privacy-law-compliance/)を受信します。ただし、顧客はそのエンドユーザーデータのデータ管理当事者であるため、顧客は、Braze のエンドユーザーデータ (Shopify 統合を通じて受信したエンドユーザーデータを含む) に関して受領したデー主体リクエストへの対応に必要なアクションを実行する必要があります。詳細は、[データ保護技術支援]({{site.baseurl}}/dp-technical-assistance)ドキュメントを参照してください。
