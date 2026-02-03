---
nav_title: CDIでユーザーを削除する
article_title: クラウドデータ取り込みによるユーザーの削除
page_order: 30
page_type: reference
description: "このページでは、Cloud Data Ingestionでユーザーを削除するプロセスの概要を説明する。"

---

# クラウドデータ取り込みによるユーザーの削除

> このページでは、Cloud Data Ingestion を使用してユーザーを削除するプロセスについて説明します。

ユーザー削除の同期は、利用可能なすべてのクラウドデータ取り込みデータソースでサポートされています。 

## 統合の設定 

標準のプロセスに従って、接続するデータウェアハウスの Braze ダッシュボードで[新規の連携を作成]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)します。削除テーブルにアクセスできるロールが含まれていることを確認します。**Create import sync** ページで、**Data Type** を**Delete Users** に設定し、統合実行中に適切なアクションを実行してユーザーを削除します。

![]({% image_buster /assets/img/cloud_ingestion/deletion_1.png %})

## ソースデータの設定

ユーザー削除のソーステーブルには、1 つ以上のユーザー識別子タイプと、`UPDATED_AT` タイムスタンプを 1 つ含める必要があります。ペイロード列は、ユーザー削除データではサポートされていません。

### `UPDATED_AT`

ソーステーブルに `UPDATED_AT` タイムスタンプを追加します。このタイムスタンプは、この行が更新されたか、テーブルに追加された時点を示します。Braze は、最後の同期以降に追加または更新が行われた行のみを同期します。

### ユーザー識別子列

テーブルには、ユーザー識別子列が 1 列以上含まれている場合があります。各行は、識別子 (`external_id` 単独か、`alias_name` と `alias_label` または `braze_id` の組み合わせ) を 1 つのみ含まなければなりません。ソーステーブルには、1 つ、2 つ、または 3 つすべての識別子タイプの列が含まれる場合があります。
- `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致しなければなりません。 
- `ALIAS_NAME` および `ALIAS_LABEL` \- この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` は一意の識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` を 1 つしか持つことができません。
- `BRAZE_ID` - Braze のユーザー識別子。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定します。 

{% alert important %}
ユーザーを削除する目的で、テーブルに `PAYLOAD` 列を含めないでください。ユーザーの偶発的、永久的な削除を防ぐため、ソーステーブルに PAYLOAD 列がある場合、同期は失敗します。その他すべての列は許可されますが、Braze では無視されます。
{% endalert %}

{% tabs %}
{% tab Snowflake %}
```json
CREATE OR REPLACE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
     UPDATED_AT TIMESTAMP_NTZ(9) NOT NULL DEFAULT SYSDATE(),
     --at least one of external_id, alias_name and alias_label, or braze_id is required  
     EXTERNAL_ID VARCHAR(16777216),
     --if using user alias, both alias_name and alias_label are required
     ALIAS_LABEL VARCHAR(16777216),
     ALIAS_NAME VARCHAR(16777216),
     --braze_id can only be used to update existing users created through the Braze SDK
     BRAZE_ID VARCHAR(16777216)
);
```
{% endtab %}
{% tab Redshift %}
```json
CREATE TABLE BRAZE_CLOUD_PRODUCTION.INGESTION.USERS_DELETES (
   updated_at timestamptz default sysdate,
   --at least one of external_id, alias_name and alias_label, or braze_id is required
   external_id varchar,
   --if using user alias, both alias_name and alias_label are required
   alias_label varchar,
   alias_name varchar,
   --braze_id can only be used to update existing users created through the Braze SDK
   braze_id varchar
);
```
{% endtab %}

{% tab BigQuery %}
次のフィールドを持つテーブルを作成します。

| フィールド名 | タイプ | モード |
|---|---|---|
| `UPDATED_AT`| タイムスタンプ | 必須 |
| `EXTERNAL_ID`| 文字列 | NULL 許容 |
| `ALIAS_NAME`| 文字列 | NULL 許容 |
| `ALIAS_LABEL`| 文字列 | NULL 許容 |
| `BRAZE_ID`| 文字列 | NULL 許容 |
{% endtab %}

{% tab Databricks %}
次のフィールドを持つテーブルを作成します。

| フィールド名 | タイプ | モード |
|---|---|---|
| `UPDATED_AT`| タイムスタンプ | 必須 |
| `EXTERNAL_ID`| 文字列 | NULL 許容 |
| `ALIAS_NAME`| 文字列 | NULL 許容 |
| `ALIAS_LABEL`| 文字列 | NULL 許容 |
| `BRAZE_ID`| 文字列 | NULL 許容 |
{% endtab %}
{% tab Microsoft Fabric %}
```json
CREATE OR ALTER TABLE [warehouse].[schema].[users_deletes] 
(
  UPDATED_AT DATETIME2(6) NOT NULL,
  PAYLOAD VARCHAR NOT NULL,
  --at least one of external_id, alias_name and alias_label, or braze_id is required  
  EXTERNAL_ID VARCHAR,
  --if using user alias, both alias_name and alias_label are required
  ALIAS_NAME VARCHAR,
  ALIAS_LABEL VARCHAR,
  --braze_id can only be used to update existing users created through the Braze SDK
  BRAZE_ID VARCHAR,
)
GO
```
{% endtab %}

{% endtabs %}

### CDI の仕組み

Braze のクラウドデータ取り込みでは、データウェアハウスインスタンスと Braze ワークスペースとの連携を設定して、定期的にデータを同期します。この同期は設定したスケジュールで実行され、連携ごとに異なるスケジュールを設定できます。同期は最大頻度で 15 分ごと、最小頻度で月に 1 回実行できます。15 分より短い間隔で頻繁に同期を実行する必要がある場合は、カスタマーサクセスマネージャーに相談するか、REST API 呼び出しを使用するリアルタイムのデータ取り込みを検討してください。

同期が実行されると、Braze はデータウェアハウスインスタンスに直接接続し、指定されたテーブルからすべての新しいデータを取得して、Braze ダッシュボードで対応するユーザープロファイルを削除します。 

{% alert warning %}
ユーザープロファイルの削除は元に戻せません。ユーザーを完全に削除するため、データの矛盾が発生する可能性があります。詳細については、[ユーザープロファイルの削除]({{site.baseurl}}/help/help_articles/api/delete_user/)を参照してください。
{% endalert %}

<br><br>