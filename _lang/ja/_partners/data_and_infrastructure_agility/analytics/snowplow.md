---
nav_title: Snowplow
article_title: Snowplow
description: "このリファレンス記事では、BrazeとSnowplowのパートナーシップについて説明します。Snowplowはオープンソースのデータ収集プラットフォームであり、Google Tag Managerのサーバーサイドタグ付けを通じてSnowplowイベントをBrazeに転送することができます。"
alias: /partners/snowplow/
page_type: partner
search_tag: Partner

---

# Snowplow

> [Snowplow][1] は、豊富で高品質、低レイテンシーのデータ収集のためのスケーラブルなオープンソースプラットフォームです。エンタープライズビジネスのための高品質で完全な行動データを収集するように設計されています。

_この統合は Snowplow によって管理されます。_

## 統合について

Braze と Snowplow の統合により、ユーザーは Google Tag Manager のサーバーサイドタグ設定を使用して Snowplow のイベントを Braze に転送できます。Snowplow Braze タグを使用すると、イベントを Braze に送信しながら、以下によって柔軟性とコントロール性を高めることができます。
- データ上のすべての変換を完全に可視化する
- 時間の経過とともに洗練度を高める
- すべてのデータを転送するまでプライベートクラウドに残す
- 豊富なタグライブラリと使い慣れたGoogle Tag Manager UIによるセットアップの容易さ

Snowplowの豊富な行動データを活用して、Brazeで強力な顧客中心のインタラクションを促進し、リアルタイムでパーソナライズされたメッセージを配信します。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Snowplow パイプライン | Snowplowパイプラインが稼働している必要があります。 |
| Google Tag Managerサーバーサイド | GTM-SSをデプロイし、[GTM-SS用のSnowplowクライアント][2]をセットアップする必要があります。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][3]。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

### パーソナライズされた、アクションベースの配信
Snowplow がデフォルトで収集する多数のリッチなイベントのいずれかを使用するか、カスタムイベントを定義して、ビジネスに適したより細かなカスタマージャーニーを形成します。Snowplowの豊富な行動データを活用して顧客ファネルを設計し、マーケティングおよび製品チームの価値を引き出し、Brazeを通じてコンバージョンと製品使用を最大化するのに役立てます。

### ダイナミックなセグメンテーション
Snowplowの高品質な行動データに基づいてBrazeでダイナミックなオーディエンスを作成する:ユーザーが製品、アプリ、またはWebサイトでアクションを実行すると、Snowplowが収集するリアルタイムの行動データを活用して、Brazeの関連セグメントにユーザーを自動的に追加または削除できます。

## 統合

### ステップ1:テンプレートインストール

#### 手動インストール

1. [`template.tpl`][7] テンプレートファイルをダウンロードしてください。
2. Google Tag Manager サーバーコンテナの **テンプレート** セクションに新しいタグを作成します。
3. 右上隅の**その他の操作**メニューをクリックし、**インポート**を選択します。
4. ダウンロードしたテンプレートファイルをインポートして保存します。

#### タグ マネージャー ギャラリー

近日公開予定です。このタグを GTM ギャラリーに追加するための承認が保留中です。

### ステップ2:Braze タグの設定

テンプレートをインストールしたら、BrazeタグをGTM-SSコンテナに追加します。

1. **タグ** タブから **新規** を選択し、タグ構成として **Braze タグ** を選択します。
2. 転送したいイベントのトリガーを選択してBrazeに送信します。
3. 必要なパラメータを入力し、タグを構成します（詳細は次のカスタマイズセクションにあります）。
4. [**保存**] をクリックします。

## カスタマイズ

### 必須タグパラメーター

次の表は、Brazeタグのセットアップに含める必要があるタグパラメータを一覧にしたものです。

| パラメータ | 説明 |
| --------- | ----------- |
| Braze REST API エンドポイント | これを Braze REST [エンドポイント][3] の URL に設定します。 |
| Braze API キー | これを各リクエストに含まれるBraze [API キー][4]に設定します。 |
| Braze `external_id` | このキーをクライアントイベントプロパティに設定し、ユーザーの`external_id`に対応させ、[Brazeユーザー識別子][5]として使用します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### イベントマッピング

次の表は、[Snowplowクライアント][2]が主張するSnowplowイベントに関するイベントマッピングオプションを一覧にしたものです。

| マッピングオプション | 説明 |
| --------- | ----------- |
| 自己記述イベントを含める | デフォルトでオンになっています。Snowplowの自己記述イベントデータがBrazeに送信されるイベントのプロパティオブジェクトに含まれるかどうかを示します。 |
| Snowplow イベントコンテキストルール | BrazeタグがSnowplowイベントに関連付けられたコンテキストエンティティをどのように使用するかについて説明します。 |
| 配列からエンティティを抽出する場合、単一の要素 | 複数の同一エンティティを1つのイベントにアタッチできるため、Snowplow エンティティは常に配列に格納されます。このオプションは、配列に単一の要素しか含まれていない場合、その単一の要素を選択します。 |
| イベントオブジェクトにすべてのエンティティを含める | デフォルトでオンになっています。Brazeイベントのプロパティオブジェクト内のイベントに含まれるすべてのエンティティを含みます。このオプションを無効にして、個々のエンティティを選択して含めます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 高度なイベントマッピング

#### イベントプロパティルール

クライアントイベントから他のプロパティを含め、それらをBrazeイベントにマッピングしたい場合は、次の表のルールを参照してください。 

| イベントプロパティルール | 説明 |
| --------- | ----------- |
| 共通イベントプロパティを含める | デフォルトで有効になっているこのオプションは、Brazeイベントのプロパティに[共通イベント定義][6]のイベントプロパティを自動的に含めるかどうかを設定します。 |
| 追加のユーザー プロパティおよびイベント プロパティ マッピング ルール | クライアントイベントからプロパティキーと、マッピングしたいプロパティオブジェクトのキーを指定します（または、マッピングされたキーを空白のままにして同じ名前を保持します）。ここではキーパス表記を使用できます (たとえば Snowplow イベントプラットフォームの場合は `x-sp-tp2.p`、Snowplow イベントページビュー ID (配列インデックス 0) の場合は `x-sp-contexts.com_snowplowanalytics_snowplow_web_page_1.0.id`、代替クライアントを使用する場合は Snowplow 以外のプロパティを選択します)。<br><br>イベントプロパティマッピングルールはBrazeイベントプロパティオブジェクトに入力されます。|
| 一般的なユーザーのプロパティを含める| デフォルトで有効になっているこのオプションは、Brazeユーザー属性オブジェクトに共通イベント定義からの`user_data`プロパティを含めるかどうかを設定します。|
| イベント時間プロパティ | このオプションを使用すると、イベント時間（ISO-8601形式）を入力するためのクライアントイベントプロパティを指定するか、空のままにして現在の時間（デフォルトの動作）を使用できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### エンティティマッピング

Snowplowエンティティマッピングテーブルを使用すると、エンティティをBrazeで異なる名前に再マッピングし、イベントプロパティやユーザー属性オブジェクトに含めることができます。 

エンティティは2つの異なる形式で指定できます:
- メジャーバージョン一致: `x-sp-contexts_com_snowplowanalytics_snowplow_web_page_1`。ここで、`com_snowplowanalytics_snowplow` はイベントベンダー、`web_page` はスキーマ名、`1` はメジャーバージョン番号です。`x-sp-` は必要に応じて省略できます。
- 完全なスキーマ一致: `iglu:com.snowplowanalytics.snowplow/webPage/jsonschema/1-0-0`
<br><br>

| エンティティマッピングオプション | 説明 |
| --------- | ----------- |
| イベントにマッピングされていないエンティティを含める | いくつかのエンティティをユーザー属性にリマップまたは移動する際に、前述のカスタマイズを使用すると、このオプションにより、すべてのマッピングされていないエンティティ（[イベントプロパティルール](#event-property-rules)に見つからないエンティティなど）がBrazeイベントのプロパティオブジェクトに含まれるようにすることができます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


[1]: https://snowplowanalytics.com
[2]: https://docs.snowplowanalytics.com/docs/forwarding-events-to-destinations/forwarding-events/google-tag-manager-server-side/snowplow-client-for-gtm-ss/
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[5]: {{site.baseurl}}/developer_guide/rest_api/basics/#external-user-id-explanation
[6]: https://developers.google.com/tag-platform/tag-manager/server-side/common-event-data
[7]: https://github.com/snowplow/snowplow-gtm-server-side-braze-tag/blob/main/template.tpl
