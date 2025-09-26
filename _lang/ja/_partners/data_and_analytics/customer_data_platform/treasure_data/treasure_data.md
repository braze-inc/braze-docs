---
nav_title: トレジャーデータ
article_title: トレジャーデータ
description: "このリファレンス記事では、Braze とトレジャーデータのパートナーシップについて説明します。トレジャーデータはエンタープライズ顧客データプラットフォームであり、Braze に直接ジョブの結果を書き込むことができます。"
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# トレジャーデータ

> [トレジャーデータ](https://www.treasuredata.com/)は、複数のソースから情報を収集し、マーケティングスタックの他のさまざまな場所に情報をルーティングする顧客データプラットフォーム (CDP) です。

Braze とトレジャーデータの統合により、トレジャーデータのジョブ結果を Braze に直接書き込むことができます。
* **external ID をマッピングする**:CRMシステムからBrazeユーザーアカウントにIDをマッピングします。 
* **オプトアウトを管理する**:エンドユーザーが参加しないことを選択して同意を更新する場合。
* **イベント、購入、またはカスタムプロファイル属性のトラッキングをアップロードする**。この情報は、正確な顧客セグメントの作成に役立ちます。正確な顧客セグメントにより、キャンペーンのユーザーエクスペリエンスが向上します。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| トレジャーデータのアカウント | このパートナーシップを活用するには、[トレジャーデータのアカウント](https://www.treasuredata.com/custom-demo/)が必要です。 |
| Braze REST API キー | `users.track`、`users.delete`、`users.alias.new`、`users.identify`の権限を持つBraze REST APIキー。<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは、[インスタンスの Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) によって異なります。| |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## ユースケース

ターゲットセグメントを編成するために、統合された顧客プロファイルをトレジャーデータから Braze に同期できます。トレジャーデータは、ファーストパーティの Cookie データ、モバイル ID、CRM などのサードパーティシステムなどをサポートしています。

## 統合

### ステップ1:新しい接続を作成する

トレジャーデータで、[**Catalog**] の下にある [**Integrations Hub**] に移動し、[**Braze**] を検索して選択します。 

**新しい認証**プロンプトが表示されたら、接続に名前を付け、Braze REST APIキーとRESTエンドポイントを提供します。完了したら**完了**を選択します。

![]({% image_buster /assets/img/treasure_data/braze_authentication.png %}){: style="max-width:80%;"}

### ステップ2: クエリを定義する

トレジャーデータで、**クエリ**の下にある**データワークベンチ**に移動し、データをエクスポートしたいクエリを選択します。このクエリを実行して結果セットを検証します。

{% alert note %}
HIVEを使用してクエリを作成するユーザーの場合、HIVEではアンダースコアで始まる列またはテーブルをバッククォートで囲む必要があります。たとえば `_merge_objects` です。
{% endalert %}

次に、**結果をエクスポート**を選択し、既存の統合認証を選択します。

![]({% image_buster /assets/img/treasure_data/query_2.png %}){: style="max-width:80%;"}

次の[カスタマイズセクション](#customization)に概説されているように、追加のエクスポート結果パラメータを定義します。エクスポート統合コンテンツで、統合パラメータを確認してください。

![「Export Results」ページ。このページには、「Mode」、「Traffic Record Type」、および「Pre-formatted Fields」フィールドがある。この例では、それぞれのフィールドに「User-Track」と「Custome Event」が設定されています。]{% image_buster /assets/img/treasure_data/braze_export_configuration.png %}{: style="max-width:80%;"}

最後に、**完了**を選択し、クエリを実行して、データがBrazeに移動したことを確認します。

### カスタマイズ

エクスポート結果のパラメータは次の表に含まれています：

| パラメータ                 | 値 | 説明 |
|---------------------------|---|---|
| `mode`                    | User - New Alias<br>ユーザー - 識別<br>ユーザー - トラック<br>ユーザー - 削除 | コネクターモード |
| `pre_formatted_fields`    | String | 配列またはJSON列に使用してフォーマットを保持します。 |
| `track_record_type`       | カスタムイベント<br>購入<br>ユーザープロファイル属性| **User - Track** モードのレコードタイプ |
| `skip_on_invalid_records` | ブール値 | 有効にした場合、続行してJSON列の無効なレコードを無視します。<br> それ以外の場合は、ジョブが停止します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
詳細については、[トレジャーデータ](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration)を訪問してください。事前にフォーマットされたフィールド、サンプルクエリ、パラメータの詳細、およびクエリエクスポートジョブのスケジューリングについて説明します。
{% endalert %}

## Webhook

トレジャーデータのユーザーは、パブリック REST API を介してデータを取り込むことができます。トレジャーデータを使用して、データにカスタム Webhook を作成できます。詳細については、[トレジャーデータ](https://docs.treasuredata.com/display/public/PD/Postback+API)を参照してください。

