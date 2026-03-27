---
nav_title: Shopify概要
article_title: "Shopify概要"
description: "このリファレンス記事では、Braze と Shopify のパートナーシップについて説明します。Shopify はグローバルなコマース企業であり、Shopify ストアを Braze とシームレスに接続して、選択した Shopify webhook を Braze に渡すことができます。Braze のクロスチャネル戦略とキャンバスを活用して、顧客が購入を完了するように促し、購入履歴に基づいてユーザーをリターゲティングできます。"
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Shopify概要

> [Shopify](https://www.shopify.com/) は、規模を問わずビジネスの開始、成長、マーケティング、管理のための信頼できるツールを提供する世界的なコマースのリーディングカンパニーです。Shopify は、信頼性の高いプラットフォームとサービスを提供し、世界中の消費者により良いショッピング体験を提供することで、すべての人にとって商取引をより良くします。

Shopify との Braze 統合は、カスタマーエンゲージメントを高め、パーソナライズされたマーケティング活動を推進しようとする e コマース事業者にとって、強力なソリューションを提供します。この統合は、Shopify の堅牢な e コマース機能を高度なカスタマーエンゲージメントプラットフォームにシームレスに接続し、リアルタイムの買い物行動やトランザクションデータに基づいて、ターゲットを絞った、関連性のある、タイムリーなメッセージをユーザーに配信することを可能にします。

## 要件

| 要件 | 説明 |
| --- | --- |
| Shopify ストア | アクティブな Shopify ストアがあること。 |
| Shopify ストアオーナーまたはスタッフメンバーの権限 | {::nomarkdown}<ul><li>すべての一般設定とオンラインストア設定にアクセスできること。</li><li> 追加の管理者権限:</li><ul><li>注文: 表示</li><li>顧客: ReadWrite</li><li>顧客イベントの表示 (Web ピクセル)</li><li>設定の管理</li><li>スタッフ/協力者が開発したアプリの表示</li><li>アプリとチャネルの管理/インストール</li><li>カスタムピクセルの管理/追加</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合方法 

Braze は、Shopify 加盟店向けに、e コマースビジネスの多様なニーズを満たすように設計された 2 つの統合オプションである**標準統合**と**カスタム統合**を提供しています。

{% multi_lang_include shopify.md section='Integration Tabs' %}

## 統合の仕組み

設定で履歴バックフィルをすでに設定してオンにしている場合は、最初のデータ同期がすぐに開始されます。Braze は、Shopify 統合接続前の過去 90 日間のすべての顧客と注文イベントをインポートします。Braze が Shopify の顧客をインポートする際、設定で選択した `external_id` タイプが割り当てられます。

カスタム external ID との統合を計画している場合 ([標準統合]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users)または[カスタム統合]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)のいずれか)、既存のすべての Shopify 顧客プロファイルに Shopify 顧客メタフィールドとしてカスタム external ID を追加し、[履歴バックフィル]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill)を実行する必要があります。 

最初のデータ同期後、Braze は Shopify と Braze SDK から直接、新しいデータと更新を継続的に追跡します。

{% alert note %}
既存の Braze ユーザーで、アクティブなキャンペーンやキャンバスをご利用の場合は、[Shopify の履歴バックフィル]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill)で重要な情報を確認してください。具体的にどのような顧客データがバックフィルされているかについては、[Shopify の機能]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/)を参照してください。
{% endalert %}

### ユーザーとデータの同期

統合が開始された後、Braze は Shopify 統合を通じて、2 つの主要なソースからユーザーデータを収集します。
- **Shopify Web Pixel API とアプリ埋め込み:** これにより、Braze Web SDK と Javascript SDK の機能が強化され、オンサイトトラッキング、ID 管理、e コマース行動データ、アプリ内メッセージなどのメッセージングチャネルがサポートされます。
- **Shopify webhook:** e コマースの行動データ、商品同期、サブスクライバー収集

統合のオンボーディングの際に、Braze SDK が初期化され、Shopify サイトを読み込むタイミングを選択する必要があります。 
- サイト訪問時 (セッション開始時など)
    - **実行内容:** ゲスト買い物客などの匿名ユーザーを追跡し、より詳細なパーソナライゼーションのためのデータにアクセスします。 
- アカウント登録時 (アカウントログインなど) 
    - **実行内容:** より保守的なプライバシー指向のアプローチで匿名ユーザーの追跡を防止します。そのため、ユーザーのアクティビティはアカウントにサインインした*後に*追跡されます。

{% alert note %}
- Web サイトへの訪問 (セッション) は、月間アクティブユーザー数 (MAU) の割り当てにカウントされます。
- Braze Web SDK と JavaScript SDK のバージョンは自動的に v5.4.0 に設定されます。
{% endalert %}

Braze は、Shopify 統合を使用して、ユーザーがゲストとしてショッピングを体験してから識別済みのユーザーになるまでを追跡する複数の識別子をサポートしています。

| Braze 識別子 | 説明 |
| --- | --- |
| Braze `device_id` | Braze SDK を通じて匿名ユーザーのアクティビティを追跡するために、ブラウザーに保存されるランダムに生成される ID です。 |
| カートトークンユーザーエイリアス | Braze がカート更新イベントを追跡するために作成するエイリアスです。このトークンは、Shopify カートトークンを使用して作成されます。 |
| チェックアウトトークンユーザーエイリアス | ユーザーがチェックアウトプロセスを開始する際に Braze が作成するエイリアスです。このトークンは、Shopify のチェックアウトトークンを使用して作成されます。<br><br> 顧客が Shop Pay を高速チェックアウトオプションとして使用した場合、Shopify は特定の標準チェックアウトイベントをバイパスし、Braze がチェックアウトトークンエイリアスを追加するために必要なデータを受信できなくなる場合があります。 |
| Shopify 顧客 ID エイリアス | Shopify 顧客 ID は、アカウントログイン時または注文時に external ID が割り当てられる際にエイリアスとして割り当てられます。 |
| Braze `external_id` | デバイスやプラットフォームを横断して顧客を追跡するための一意の識別子です。ユーザーがデバイスを切り替えたり、アプリを再インストールしたりしても、複数のプロファイルが作成されることを防ぎ、一貫したユーザーエクスペリエンスを維持し、分析を向上させます。<br><br>Shopify 統合では、以下の `external_id` タイプがサポートされます。<br><br>{::nomarkdown}<ul><li>Shopify 顧客 ID (デフォルト)</li><li>カスタム external ID</li><li>ハッシュされたメール (SHA-256)</li><li>ハッシュされたメール (SHA-1)</li><li>ハッシュされたメール (MD5)</li><li>メール</li></ul>{:/}Braze は以下のタイミングで SDK 内の changeUser メソッドを呼び出すことで、ユーザーに `external_id` を割り当てます。<br><br>{::nomarkdown}<ul><li>ユーザーがログインするか、アカウントを作成する</li><li>注文が行われる</li></ul>{:/}<br> 匿名プロファイルに `external_id` を割り当てた場合の詳細については、[ユーザープロファイルのライフサイクル]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users)を参照してください。<br><br>Braze はまた、`external_id` を活用して、Shopify webhook からの下流の e コマース行動データを紐付けます。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

この統合では、Braze SDK と Shopify サービスが連携して、Shopify データをほぼリアルタイムで適切に追跡し、適切なユーザーに紐付ける必要があります。統合によって追跡されるデータの詳細については、[Shopify データ]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/)を参照してください。

{% alert note %}
- 統合をテストしている場合は、シークレットモードを使用するか、Cookie をクリアして Braze `device_id` をリセットし、匿名ユーザーの行動を模倣することをお勧めします。
- Shopify の顧客 ID は、Shopify のニュースレターフッターにメールが入力されたときや、注文前のチェックアウトプロセス中に生成されますが、その顧客 ID には Shopify Web Pixels からアクセスできません。このため、Braze はこの 2 つの状況では `changeUser` メソッドを使用できません。
{% endalert %}

### Shopify のメールと SMS マーケティングのオプトインを同期する

設定でサブスクライバー収集を有効にした場合は、Braze に接続する各ストアにサブスクリプショングループを割り当てる必要があります。これにより、顧客はストアのサブスクリプショングループで「購読中」または「配信停止」のいずれかに分類されます。

メールと SMS マーケティングの Shopify マーケティングオプトインステータスは、以下の方法で更新できます。
- **手動更新:** ユーザーのメールや SMS マーケティングのオプトインステータスは、Shopify 管理画面で手動で変更できます。
- **Shopify ニュースレターフッター:** ユーザーが Shopify デフォルトのニュースレターフッターにメールを入力すると、オプトインステータスが更新されます。
- **チェックアウトプロセス:** ユーザーがチェックアウト中にオプトインステータスを更新した場合。

{% alert note %}
Shopify からのメールマーケティングオプトインステータスによって、Braze のユーザーの[グローバルメールサブスクリプションステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)が変更されることはありません。ユーザープロファイルが作成されたときのデフォルトのサブスクリプションステータスは「購読中」です。キャンペーンまたはキャンバスのエントリ基準の一部として、サブスクリプショングループを必ず使用してください。
{% endalert %}

この表は、Shopify マーケティングのオプトインステータスと Braze サブスクリプショングループ内のステータスとの対応関係を示しています。 

| Shopify マーケティングのオプトインステータス | Braze サブスクリプショングループのステータス |
| --- | --- |
| メール購読済み | 購読中 |
| メール配信停止 | 配信停止済み |
| メール確認待ち | 配信停止済み |
| メールが無効 | 配信停止済み |
| SMS 購読済み | 購読中 |
| SMS 配信停止済み | 配信停止済み |
{: .reset-td-br-1 .reset-td-br_2 role="presentation"}

### 登録フォーム

#### Shopify ニュースレターフッター

Shopify のニュースレターフッターにメールアドレスを入力したユーザーには、次のいずれかのワークフローが適用されます。

##### アカウントにログインしていないユーザー

1. 顧客が作成または更新されるたびに、Braze は Shopify の webhook を受信します。
2. Braze は、そのユーザーに関連付けられたメールアドレスと Shopify 顧客 ID エイリアスを含むユーザープロファイルを作成します。
3. Braze SDK は、メールアドレスで匿名プロファイルを更新します。

{% alert note %}
その結果、ユーザーがアカウントの作成、アカウントへのログイン、または注文を行うことで自身を識別するまで、プロファイルの重複が生じる場合があります。Braze は、重複プロファイルの照合を自動化するための一括マージツールを提供しています。詳細は[重複ユーザー]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/)を参照してください。
{% endalert %}

##### アカウントにログイン済みのユーザー

Braze は、そのユーザーに関連付けられたメールアドレスと Shopify 顧客 ID エイリアスを含むユーザープロファイルを作成します。Shopify がすでにこの情報を提供していると想定されるため、Braze はログイン済みユーザーのメールアドレスを更新しません。

#### Braze 登録フォーム

Braze は 2 種類の登録フォームテンプレートを提供しています。
- **[メール登録フォーム]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/email_capture/):** ドラッグ＆ドロップエディターを使用して作成します。
- **[従来のエディターのメールキャプチャフォーム]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/):** メールアドレスを取得するための、よりシンプルなフォームです。

これらの登録フォームテンプレートを使用すると、Braze は自動的にユーザープロファイルのグローバルメールサブスクリプションステータスを更新します。グローバルメールサブスクリプションステータスの処理方法についての詳細 (メールの検証に関する情報を含む) については、各フォームテンプレートタイプのドキュメントを参照してください。

{% alert note %}
- キャンペーンまたはキャンバスに、グローバルメールサブスクリプションステータスと、Shopify ストアに接続されているサブスクリプショングループの両方を含むエントリ基準を必ず含めてください。これにより、適切なオーディエンスをターゲットにしていることを確認できます。 
- Braze は、ブラウザー内メッセージを通じて、メールアドレスや電話番号などの訪問者情報を収集します。この情報は Shopify Visitor API に送信されますが、Shopify では顧客プロファイルは作成されません。詳細については、[Visitor API](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api) を参照してください。
{% endalert %}

#### サードパーティの登録フォーム 

サードパーティのプラットフォームや Shopify プラグインを登録フォームに使用している場合は、フォーム送信からメールアドレスとグローバルメールサブスクリプションステータスを取得するために、開発者と協力して Braze SDK コードを統合する必要があります。詳細については、[Shopify 標準統合セットアップ]({{site.baseurl}}/shopify_standard_integration/)と [Shopify カスタム統合セットアップ]({{site.baseurl}}/shopify_custom_integration/)を確認してください。

### 商品の同期 

Braze は、Shopify ストアの商品を Braze カタログに同期する機能をサポートしています。詳細は、[Shopify 商品同期]({{site.baseurl}}/shopify_catalogs/)を参照してください。

## データ主体リクエスト

Braze プラットフォームの Shopify 統合の一環として、Braze は自動的に [Shopify のコンプライアンス webhook](https://shopify.dev/docs/apps/build/privacy-law-compliance/) を受信します。ただし、顧客はそのエンドユーザーデータのデータ管理者であるため、Braze のエンドユーザーデータ (Shopify 統合を通じて受信したエンドユーザーデータを含む) に関して受領したデータ主体リクエストへの対応に必要なアクションを実行する必要があります。詳細は、[データ保護技術支援]({{site.baseurl}}/dp-technical-assistance)ドキュメントを参照してください。