---
nav_title: トレジャーデータ
article_title: トレジャーデータ
description: "この記事では、Brazeとトレジャーデータのパートナーシップについて説明します。トレジャーデータは、企業向けの顧客データプラットフォームで、ジョブの結果を直接Brazeに書き込むことができます。"
alias: /partners/treasure_data/
page_type: partner
search_tag: Partner

---

# トレジャーデータ

> \[トレジャーデータ][4]は、複数のソースから情報を収集し、マーケティングスタック内のさまざまな場所にルーティングする顧客データプラットフォーム（CDP）です。

Brazeとトレジャーデータの統合により、トレジャーデータからBrazeに直接ジョブ結果を書き込むことができ、次のことが可能になります:
* **外部IDをマップする**:CRMシステムからBrazeユーザーアカウントにIDをマッピングします。 
* **オプトアウトを管理する**:エンドユーザーが参加しないことを選択して同意を更新する場合。
* **あなたのイベント、購入、またはカスタムプロファイル属性のトラッキングをアップロード**。この情報は、キャンペーンのユーザーエクスペリエンスを向上させる正確な顧客セグメントの構築に役立ちます。

## 前提条件

| 要件 | 説明 |
| --- | --- |
| トレジャーデータアカウント | このパートナーシップを利用するには、[トレジャーデータアカウント](https://www.treasuredata.com/custom-demo/)が必要です。 |
| Braze REST API キー | `users.track`、`users.delete`、`users.alias.new`、`users.identify`の権限を持つBraze REST APIキー。<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント  | あなたのRESTエンドポイントURL。エンドポイントは、インスタンスのBraze URL][1]に依存します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## ユースケース

トレジャーデータから統合された顧客プロファイルをBrazeに同期して、ターゲットセグメントを構築できます。トレジャーデータは、ファーストパーティCookieデータ、モバイルID、CRMのようなサードパーティシステムなど、多くのものをサポートしています。

## 統合

### ステップ1:新しい接続を作成する

トレジャーデータで、**カタログ**の**インテグレーションハブ**に移動し、**Braze**を検索して選択します。 

**新しい認証**プロンプトが表示されたら、接続に名前を付け、Braze REST APIキーとRESTエンドポイントを提供します。完了したら**完了**を選択します。

![][2]{: style="max-width:80%;"}

### ステップ2:クエリを定義する

トレジャーデータで、**クエリ**の下にある**データワークベンチ**に移動し、データをエクスポートしたいクエリを選択します。このクエリを実行して結果セットを検証します。

{% alert note %}
HIVEを使用してクエリを作成するユーザーの場合、HIVEではアンダースコアで始まる列またはテーブルをバッククォートで囲む必要があります。例えば、`_merge_objects`。
{% endalert %}

次に、**結果をエクスポート**を選択し、既存の統合認証を選択します。

![][11]{: style="max-width:80%;"}

次の[カスタマイズセクション](#customization)に概説されているように、追加のエクスポート結果パラメータを定義します。エクスポート統合コンテンツで、統合パラメータを確認してください。

![「結果のエクスポート」ページ。このページには、「モード」、「トラックレコードタイプ」、および「事前フォーマットされたフィールド」のフィールドがあります。この例では、「ユーザー-トラック」と「カスタムイベント」がそれぞれこれらのフィールドに設定されています。][3]{: style="max-width:80%;"}

最後に、**完了**を選択し、クエリを実行して、データがBrazeに移動したことを確認します。

### カスタマイズ

エクスポート結果のパラメータは次の表に含まれています：

| パラメータ                 | 値 | 説明 |
|---------------------------|---|---|
| `mode`                    | ユーザー - New Alias<br>ユーザー - 識別<br>ユーザー - トラック<br>ユーザー - 削除 | コネクターモード |
| `pre_formatted_fields`    | String | 配列またはJSON列に使用してフォーマットを保持します。 |
| `track_record_type`       | カスタムイベント<br>購入<br>ユーザープロファイル属性| **ユーザー - トラック**モードのレコードタイプ |
| `skip_on_invalid_records` | ブール値 | 有効にした場合、続行してJSON列の無効なレコードを無視します。<br> さもなければ、仕事は止まります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
詳細については、[トレジャーデータ](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration)を訪問してください。事前にフォーマットされたフィールド、サンプルクエリ、パラメータの詳細、およびクエリエクスポートジョブのスケジューリングについて説明します。
{% endalert %}

## Webhook

トレジャーデータのユーザーは、パブリックREST APIを通じてデータを取り込むことができます。トレジャーデータを使用して、データにカスタムwebhookを作成できます。詳細については、[トレジャーデータ][6]をご覧ください。

[6]: https://docs.treasuredata.com/display/public/PD/Postback+API
[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: {% image_buster /assets/img/treasure_data/braze_authentication.png %}
[3]: {% image_buster /assets/img/treasure_data/braze_export_configuration.png %}
[4]: https://www.treasuredata.com/
[5]: https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration
[10]: {% image_buster /assets/img/treasure_data/query_1.png %}
[11]: {% image_buster /assets/img/treasure_data/query_2.png %}
