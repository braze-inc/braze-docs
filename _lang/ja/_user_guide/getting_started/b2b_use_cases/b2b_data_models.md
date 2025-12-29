---
nav_title: データモデル
article_title: B2Bデータモデルの作成
page_order: 0
page_type: reference
description: "Braze データツールを使用して B2B モデルを作成する方法について説明します。"
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
| 連絡先 | 通常、連絡先として適格であり、セールス案件を探求するためにリードから連絡先に変換された個人。 |
| 機会 | 潜在的な売却または進行中の取引の詳細を追跡するレコード
| アカウント | 適格な見込み顧客、既存の顧客、パートナー、または類似する重要な関係性を持つ競合他社である組織のレコード。 |
{: .reset-td-br-1 .reset-td-br-2 }

Braze 内では、この4つのオブジェクトが結合され、ユーザープロファイルとビジネスオブジェクトという2つのオブジェクトになります。

| Braze B2B オブジェクト | 説明 | 元のB2Bオブジェクト  |
| --- | --- | --- |
| ユーザープロフィール | ユーザープロファイルは、営業用 CRM システムのリードおよび連絡先に直接マップされています。リードは Braze によってキャプチャされるため、営業用 CRM システムでは自動的にリードとして作成されます。連絡先に変換されると、連絡先 ID と詳細が Braze に同期されます。 |リード<br> 連絡先 |
| ビジネスオブジェクト | これらは、営業用CRMシステム内のすべての非ユーザオブジェクトにマップされます。これには、アカウントオブジェクトや案件オブジェクトなど、営業固有のオブジェクトが含まれます。 | アカウント<br> 機会 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ステップ1:Braze でビジネスオブジェクトを作成する

ビジネス・オブジェクトは、ユーザ中心でない任意のデータ・セットです。B2B コンテキストでは、これらには、アカウントと商談データ、および会社が追跡するその他の関連するユーザ中心でないデータセットが含まれます。

Braze でビジネスオブジェクトを作成および管理するには、カタログと接続されたソースの2つの方法があります。 

| 方法 | 説明 |
| --- | --- |
| [カタログ]({{site.baseurl}}/user_guide/data/activation/catalogs) | これらは、Braze のプライマリユーザプロファイルの独立したデータオブジェクト (補足データオブジェクト) です。B2B のコンテキストでは、アカウントと案件のカタログがある可能性があります。 |
| [接続されたソース]({{site.baseurl}}/user_guide/data/cloud_ingestion/connected_sources/) | これにより、Braze はデータウェアハウスに直接クエリを実行できます。すでにリード、連絡先、案件、アカウントの各オブジェクトをデータウェアハウスと定期的に同期している可能性があるため、Braze セグメンテーションをそのウェアハウスに直接ポイントし、ゼロコピー環境で有効化することができます。 |
{: .reset-td-br-1 .reset-td-br-2 }

{% tabs %}
{% tab Catalogs %}

### オプション 1: アカウントと案件のカタログを使用する

カタログは、Braze でホストおよび管理されるデータテーブルです。アカウントデータと案件データは、使用している営業用 CRM システムから作成されますが、Braze でこれらのデータを複製して、マーケティング目的 (アカウントベースのセグメント化、アカウントベースのマーケティング、リード管理など) で使用できます。

このオプションでは、アカウントと商談のカタログを1 つ作成し、[catalogs API]({{site.baseurl}}/api/endpoints/catalogs/) または[catalogs Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data/cloud_ingestion/sync_catalogs_data/) を通じてBraze の更新を送信することで、頻繁に更新することをお勧めします。これらのカタログを作成するときは、カタログの`id`(最初の列)が販売用CRMシステムの`id`と一致していることを確認してください。

#### CRM フィールドにマップする

以下の表に、CRM のアカウントオブジェクトと案件オブジェクトからマップできるフィールドの例をいくつか示します。

{% subtabs %}
{% subtab Account catalog %}

この使用例では、Salesforce がCRM システムの例です。CRM のオブジェクトに含まれる任意のフィールドにマップできます。

<table border="1">
  <tr>
    <th><b>Braze オブジェクト</b></th>
    <th><b>Braze フィールド</b></th>
    <th><b>CRM オブジェクト(Salesforce)</b></th>
    <th><b>CRM フィールド (Salesforce)</b></th>
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

![請求先住所や取引先所有者など、それぞれの情報を含むSalesforce 取引先のテーブル。]({% image_buster /assets/img/b2b/sf_accounts.png %})

{% endsubtab %}
{% subtab Opportunity catalog %}

この使用例では、Salesforce がCRM システムの例です。CRM のオブジェクトに含まれる任意のフィールドにマップできます。

<table border="1">
  <tr>
    <th><b>Braze オブジェクト</b></th>
    <th><b>Braze フィールド</b></th>
    <th><b>CRM オブジェクト(Salesforce)</b></th>
    <th><b>CRM フィールド (Salesforce)</b></th>
  </tr>
  <tr>
    <td rowspan="4">カタログ > 案件カタログ</td>
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

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Connected sources %}

### オプション 2: アカウントと案件に接続されたソースを使用する

接続されたソースは、独自のデータウェアハウスでホストされ、Braze [CDI Segment Extensions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments/) によってクエリされるデータテーブルです。カタログとは異なり、Braze でビジネスオブジェクト (アカウントと案件) を複製する代わりに、データウェアハウスにこれらのオブジェクトを維持し、ウェアハウスを信頼できる情報源として使用します。

接続されたソースを設定するには、「[接続されたソースの統合]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources#integrating-connected-sources)」を参照してください。

{% endtab %}
{% endtabs %}

## ステップ 2:ビジネス・オブジェクトをユーザー・プロファイルに関連付ける

ユーザープロファイルは、Braze の主要なオブジェクトです。ユーザー層のセグメンテーション、トリガー、パーソナライゼーションの大部分の処理に使用されます。ユーザープロファイルには、SDK によって収集された[デフォルトのユーザーデータ]({{site.baseurl}}/user_guide/data/user_data_collection/) と、[カスタムデータ]({{site.baseurl}}/user_guide/data/custom_data/) が含まれます。これらのデータは、属性(人口統計データ)、イベント(行動データ)、購入(トランザクションデータ) のいずれかの形式になります。

### ステップ 2.1:営業用 CRM の ID を Braze にマッピングする

まず、Braze とご利用の CRM に、データを共有するための共通の識別子があることを確認します。次の表を使用して、営業用 CRM の ID フィールドを Braze ユーザーオブジェクトにマップすることをお勧めします。以下の表では CRM システムとしてSalesforce が使用されていますが、これはあらゆる CRM に適用できます。

#### Braze オブジェクト:ユーザー

| Braze フィールド | CRM オブジェクト(Salesforce) | CRM フィールド (Salesforce) | 追加情報 |
| --- | --- | --- | --- |
| `Aliases.salesforce_lead_id` | リード | `id` |  \- ユーザー別名ラベル: `salesforce_lead_id`<br>\- ユーザー別名: `lead_id`|
| `Aliases.salesforce_contact_id` | このページが引き続き表示される場合は、 | `id` | \- ユーザー別名ラベル: `salesforce_contact_id`<br>\- ユーザー別名: `contact_id` |
| `AccountId` | このページが引き続き表示される場合は、 | `AccountId` | 
| `OpportunityId` (オプション、スカラ) <br>または<br> `Opportunities` (オプション、配列) | 案件 | `id` | 
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

{% alert note %}
Salesforce のリードと取引先責任者の識別子を Braze にマップするには、`external_id` ではなく[エイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) を使用することをお勧めします。これは、製品主導の成長スタイルのイニシアチブを特定して実行する際に必要なルックアップの量を減らすためです。
{% endalert %}

ID を同期したら、Braze ユーザープロファイルをビジネスオブジェクトに関連付ける必要があります。 

### ステップ 2.2:ユーザプロファイルとビジネスオブジェクト間の関係を作成する

{% tabs %}
{% tab Catalogs %}

#### オプション 1: カタログsを使用する場合

商談および取引先の詳細がBraze カタログとして会計処理されるようになったので、これらのカタログと、メッセージを送信するユーザプロファイルとの間に関係を作成する必要があります。現在、これには2つのステップが必要です。

1. アカウント (`account_id (string)` など) または案件 ID (`opportunity_ids (array)` など)、あるいはこの両方を、属性としてユーザープロファイルに含めます。
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

{% endtab %}
{% tab Connected sources %}

#### オプション 2: 接続したソースを使用する場合

接続されたソースのテーブルの1つに、Braze でユーザーに対して設定された `external_user_id` に一致する `user_id` が含まれている必要があります。前述のユーザープロファイル設定では、リードと `contact_ids` が `external_id` として使用されています。このため、リード/連絡先のテーブルにこれらの ID が含まれていることを確認する必要があります。

ID の一致を確認することに加え、効率的なセグメンテーションとパーソナライゼーションのために、基本的なアカウントレベルデータ (`account_id`、`opportunity_id` など) と一般的な企業統計属性 (`industry` など) をユーザープロファイルに書き込むことをお勧めします。

{% endtab %}
{% endtabs %}