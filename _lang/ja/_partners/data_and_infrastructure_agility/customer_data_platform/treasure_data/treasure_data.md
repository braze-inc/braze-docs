---
nav_title: Treasure Data
article_title:Treasure Data
description:
alias: /partners/treasure_data/
page_type: partner
search_tag:Partner

---

# Treasure Data

> \[Treasure Data][4] は顧客データプラットフォーム（CDP）であり、複数のソースから情報を収集し、マーケティングスタックの様々な場所にルーティングする。


* **外部IDをマップ**する：CRMシステムからBrazeユーザーアカウントにIDをマッピングする。 
* **オプトアウトを**マネージャーする：エンドツーエンドのユーザーが、参加しないことを選択して同意を更新した場合。
* **イベント、購入、カスタムプロファイル属性のトラッキングをアップロード**する。この情報は、キャンペーンのユーザーエクスペリエンスを向上させる正確なカスタマーセグメントの構築に役立つ。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
|  | このパートナーシップを利用するには、[トレジャーデータのアカウントが](https://www.treasuredata.com/custom-demo/)必要である。 |
| Braze REST API キー | `users.track`,`users.delete`,`users.alias.new`,`users.identify` の権限を持つREST APIキー。<br><br>これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは\[インスタンスのBraze URL][1]]に依存する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## ユースケース

トレジャーデータからBrazeに統合した顧客プロファイルを同期し、ターゲットセグメントを構築することができる。トレジャーデータは、ファーストパーティのCookieデータ、モバイルID、CRMのようなサードパーティシステム、その他多くのデータをサポートしている。

## 統合

### ステップ1:新しい接続を作成する

トレジャーデータで、**Integrations Hubの**下にある**カタログに**移動し、**Brazeを**検索して選択する。 

表示される**New Authentication**プロンプトで、接続に名前を付け、REST APIキーとRESTエンドポイントを入力する。終了したら**Doneを**選択する。

![][2]{: style="max-width:80%;"}

### ステップ2:クエリを定義する

トレジャーデータで、**データ・ワークベンチの**「**クエリ**」に移動し、データをエクスポートしたいクエリを選択する。このクエリーを実行して、結果セットを検証する。

{% alert note %}
HIVEを使用してクエリを構築するユーザーのために、HIVEはアンダースコアで始まるカラムまたはテーブルをバッククォートでラップすることを要求する。例えば、`_merge_objects` 。
{% endalert %}

次に、「**Export Results**」を選択し、既存の統合認証を選択する。

![][11]{: style="max-width:80%;"}

以下の[カスタマイズセクションで](#customization)説明されているように、追加のエクスポート結果パラメータを定義する。エクスポート統合コンテンツで、統合パラメータを確認する。

![結果のエクスポート」ページ。このページには、"モード"、"トラックレコード・タイプ"、"プリフォーマット・フィールド "のフィールドがある。この例では、"User-Track "と "Custom Events "がそれぞれこれらのフィールドに設定されている。][3]{: style="max-width:80%;"}

最後に、**Doneを**選択し、クエリを実行し、Brazeにデータが移動したことを確認する。

### カスタマイズ

エクスポート結果のパラメーターは以下の表に含まれている：

| パラメーター                 | 価値観 | 説明 |
|---------------------------|---|---|
| `mode`                    | ユーザー - 新しいエイリアス<br>ユーザー -識別子<br>ユーザー - 追跡<br>ユーザー - 削除 | コネクター・モード |
| `pre_formatted_fields`    | String | 配列やJSONカラムの書式を保持するために使用する。 |
| `track_record_type`       | カスタムイベント<br>購入<br>ユーザープロファイル属性| **ユーザー・トラック**・モードの記録タイプ |
| `skip_on_invalid_records` | ブール値 | イネーブルメントの場合、JSONカラムの無効なレコードは無視する。<br> そうでなければ、仕事は中断される。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
フォーマット済みフィールド、クエリ例、パラメータ詳細、クエリ・エクスポート・ジョブのスケジュールについては、[トレジャーデータを](https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration)参照のこと。
{% endalert %}

## Webhook

トレジャーデータユーザーは、パブリックREST APIを通じてデータを取り込むことができる。トレジャーデータを使用して、データにカスタムWebhookを作成することができる。詳しくは[トレジャーデータを][6]ご覧いただきたい。

[6]: https://docs.treasuredata.com/display/public/PD/Postback+API
[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: {% image_buster /assets/img/treasure_data/braze_authentication.png %}
[3]: {% image_buster /assets/img/treasure_data/braze_export_configuration.png %}
[4]: https://www.treasuredata.com/
[5]: https://docs.treasuredata.com/display/public/INT/Braze+Export+Integration
[10]: {% image_buster /assets/img/treasure_data/query_1.png %}
[11]: {% image_buster /assets/img/treasure_data/query_2.png %}
