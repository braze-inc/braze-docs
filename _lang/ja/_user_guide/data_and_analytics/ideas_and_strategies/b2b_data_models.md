---
nav_title: B2B データモデル
article_title: B2Bデータモデルの作成
page_order: 0
page_type: reference
description: "ろう付けデータツールを使用してB2B モデルを作成する方法について説明します。"
---

# B2B データモデルの作成

> このユースケースは、Braze データツールを使用して、効果的で効率的なB2B データモデルを作成する方法を示しています。B2B データモデルは、メッセージのターゲット設定、トリガ、パーソナライズ、およびビジネスユーザーへの送信に役立ちます。 

{% alert note %}
これらの推奨事項は、Braze がB2B 機能を構築するにつれて、時間の経過とともに変化する可能性があります。
{% endalert %}

B2B データモデルの設定方法を説明する前に、いくつかの概念と用語について説明します。

B2B キャンペーンを実行するために必要な主要なB2B オブジェクトは4 つあります。

| オブジェクト | 説明 |
| --- | --- |
| リード | 製品やサービスに興味を示したが、まだ機会として認定されていない潜在的な顧客の記録。 |
| 連絡先 | 通常、資格を取得し、リードから取引先責任者に転換して販売機会を追求する個人です。 |
| 機会 | 潜在的な売却または進行中の取引の詳細を追跡するレコード
| アカウント | 適格潜在顧客、既存顧客、パートナー、または類似の重要性を持つ競合他社である組織の記録。 |
{: .reset-td-br-1 .reset-td-br-2 }

Braze 内では、これら4 つのオブジェクトが結合され、ユーザプロファイルとビジネスオブジェクトの2 つのオブジェクトに縮小されます。

| ろう付けB2Bオブジェクト | 説明 | 元のB2Bオブジェクト  |
| --- | --- | --- |
| ユーザープロフィール | これらのマップは、販売CRM システムのリードおよび取引先責任者に直接対応します。リードはBraze によってキャプチャされるため、販売CRM システムでリードとして自動的に作成されます。コンタクトに変換されると、コンタクトID と詳細はBraze に同期されます。 |リード<br> 連絡先 |
| ビジネスオブジェクト | これらは、営業用CRMシステム内のすべての非ユーザオブジェクトにマップされます。これには、取引先オブジェクトや商談オブジェクトなど、営業固有のオブジェクトが含まれます。 | アカウント<br> 機会 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ステップ1:Braze でビジネスオブジェクトを作成する

ビジネス・オブジェクトは、ユーザ中心でない任意のデータ・セットです。B2B コンテキストでは、これらには、アカウントと商談データ、および会社が追跡するその他の関連するユーザ中心でないデータセットが含まれます。

Braze でビジネスオブジェクトを作成および管理するには、カタログと接続されたソースの2 つの方法があります。 

| 方法 | 説明 |
| --- | --- |
| [カタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) | これらは、ブレーズのプライマリユーザプロファイル上の独立したデータオブジェクト(補足データオブジェクト) です。B2B コンテキストでは、取引先と商談のカタログがある可能性があります。 |
| [接続されたソース]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources/) | これにより、Braze はデータウェアハウスに直接クエリを実行できます。リード、取引先責任者、商談、取引先オブジェクトを定期的にデータウェアハウスに同期している可能性があるため、Braze セグメンテーションをそのウェアハウスに直接ポイントし、ゼロコピー環境で有効化することができます。 |
{: .reset-td-br-1 .reset-td-br-2 }

### オプション 1: 取引先および商談のカタログの使用

カタログは、Braze でホストおよび管理されるデータテーブルです。取引先および商談データは、選択した販売CRMシステムから作成されますが、これらをBraze で複製して、取引先ベースのセグメンテーション、取引先ベースのマーケティング、リード管理などのマーケティング目的で使用することができます。

このオプションでは、アカウントと商談のカタログを1 つ作成し、[catalogs API]({{site.baseurl}}/api/endpoints/catalogs/) または[catalogs Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/sync_catalogs_data/) を通じてBraze の更新を送信することで、頻繁に更新することをお勧めします。これらのカタログを作成するときは、カタログの`id`(最初の列)が販売用CRMシステムの`id`と一致していることを確認してください。

#### CRM フィールドにマップする

以下の表に、CRM の取引先オブジェクトおよび商談オブジェクトからマップすることができる項目の例をいくつか示します。

{% tabs %}
{% tab アカウントカタログ %}

この使用例では、Salesforce がCRM システムの例です。CRM のオブジェクトに含まれる任意のフィールドにマップできます。

<table border="1">
  <tr>
    <th><b>ろう付けオブジェクト</b></th>
    <th><b>ろう付けフィールド</b></th>
    <th><b>CRM オブジェクト(Salesforce)</b></th>
    <th><b>CRM 項目(Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">カタログ> アカウントカタログ</td>
    <td><code>id</code></td>
    <td><code>account</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>AccountName</code></td>
    <td><code>account</code></td>
    <td><code>Account Name</code></td>
  </tr>
  <tr>
    <td><code>Type</code></td>
    <td><code>account</code></td>
    <td><code>Type</code></td>
  </tr>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>account</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
</table>

##### マップされた取引先フィールドのテーブルの例

![請求先住所やアカウント所有者など、それぞれの情報を含むSalesforce 取引先のテーブル。]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endtab %}
{% tab 商談カタログ %}

この使用例では、Salesforce がCRM システムの例です。CRM のオブジェクトに含まれる任意のフィールドにマップできます。

<table border="1">
  <tr>
    <th><b>ろう付けオブジェクト</b></th>
    <th><b>ろう付けフィールド</b></th>
    <th><b>CRM オブジェクト(Salesforce)</b></th>
    <th><b>CRM 項目(Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">カタログ> 商談カタログ</td>
    <td><code>id</code></td>
    <td><code>opportunity</code></td>
    <td><code>id</code></td>
  </tr>
  <tr>
    <td><code>OpportunityName</code></td>
    <td><code>opportunity</code></td>
    <td><code>Opportunity Name</code></td>
  </tr>
  <tr>
    <td><code>Territory</code></td>
    <td><code>opportunity</code></td>
    <td><code>Territory</code></td>
  <tr>
    <td><code>OTHER_FIELDS</code></td>
    <td><code>opportunity</code></td>
    <td><code>OTHER_FIELDS</code></td>
  </tr>
  </tr>
</table>

##### マッピングされた商談項目の例のテーブル

![請求先住所や取引先所有者など、それぞれの情報を含むSalesforce 商談のテーブル。]({% image_buster /assets/img/b2b/sf_opportunities.png %})

{% endtab %}
{% endtabs %}

### オプション 2: 取引先および商談の接続元を使用する

接続されたソースは、ユーザーが独自のデータウェアハウスでホストし、Braze [CDI セグメント]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) によって照会されるデータテーブルです。カタログとは異なり、Braze でビジネスオブジェクト(取引先および商談) を複製するのではなく、データウェアハウスに保存し、真理の源泉としてウェアハウスを使用します。

接続ソースを設定するには、[接続ソースの統合]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources#integrating-connected-sources)を参照してください。

## ステップ2:ビジネス・オブジェクトをユーザー・プロファイルに関連付ける

ユーザープロファイルは、Braze の主なオブジェクトです。Braze は、デモグラフィックのセグメンテーション、トリガー、パーソナライゼーションの大部分を処理します。ユーザープロファイルには、SDK によって収集された[デフォルトのユーザーデータ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/) と、[カスタムデータ]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/) が含まれます。これらのデータは、属性(人口統計データ)、イベント(行動データ)、購入(トランザクションデータ) のいずれかの形式になります。

### ステップ 2.1:販売CRM IDのろう付けへのマッピング

まず、ブレーズと選択したCRMに、データを共有するための共通の識別子があることを確認します。次の表を使用して、販売 CRM ID 項目を Braze ユーザーオブジェクトにマップすることをお勧めします。下の表には、CRM システムとしてSalesforce がありますが、これは任意のCRM で実行できます。

#### ろう付けオブジェクト:ユーザー

| ろう付けフィールド | CRM オブジェクト(Salesforce) | CRM 項目(Salesforce) | 追加情報 |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | 鉛 | `id` |  \- ユーザー別名ラベル: `salesforce_lead_id`<br>\- ユーザー別名: `lead_id`|
| `Aliases.salesforce_contact_id` | このページが引き続き表示される場合は、 | `id` | \- ユーザー別名ラベル: `salesforce_contact_id`<br>\- ユーザー別名: `contact_id` |
| `AccountId` | このページが引き続き表示される場合は、 | `AccountId` | 
| `OpportunityId` (オプション、スカラ) <br>または<br> `Opportunities` (オプション、配列) | 案件 | `id` | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% alert note %}
Salesforce リードおよび取引先責任者の識別子をBraze にマップするには、`external_id` ではなく[エイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) を使用することをお勧めします。これは、製品主導の成長スタイルのイニシアチブを特定して実行する際に必要なルックアップの量を減らすためです。
{% endalert %}

ID を同期したら、Braze ユーザープロファイルをビジネスオブジェクトに関連付ける必要があります。 

### ステップ 2.2:ユーザプロファイルとビジネスオブジェクト間の関係を作成する

#### オプション 1: ビジネス・オブジェクトのカタログを使用する場合

商談および取引先の詳細がBraze カタログとして会計処理されるようになったので、これらのカタログと、メッセージを送信するユーザプロファイルとの間に関係を作成する必要があります。現在、これには2つのステップが必要です。

1. アカウント(`account_id (string)` など)、商談ID (`opportunity_ids (array)` など)、またはその両方を属性としてユーザープロファイルに含めます。
2. イベントプロパティとしてアカウントID を含むイベント(`account_linked` など) をログに記録します。

```json
{
  "attributes" : [
    {
      "external_id" : "user1",
      "accountId" : "001J7000004K7AF",
      "opportunityIds" : [
"0064J000004EU59",
"0064J000004EU5G"
]
    }
  ],
  "events" : [
    {
      "external_id" : "user1",
      "name" : "account_linked",
      "time" : "2013-07-16T19:20:45+01:00",
      "properties": {
        "account_id": "001J7000004K7AF"
      }
    }
  ]
}
```

#### オプション 2: 接続したソースを使用する場合

接続されたソースのテーブルの1 つに、ユーザのBraze で設定された`user_id` と一致する`external_user_id` が含まれている必要があります。上記のユーザプロファイル設定ではリードを使用し、`contact_ids` を`external_id` として使用するため、リード/ 取引先責任者テーブルにこれらのID が含まれていることを確認する必要があります。

ID の一致を保証することに加えて、`account_id`、`opportunity_id` などの基本的なアカウントレベルのデータ、および`industry` などの一般的なファームグラフィック属性をユーザープロファイルに書き込んで、効率的なセグメンテーションとパーソナライズを行うことをお勧めします。