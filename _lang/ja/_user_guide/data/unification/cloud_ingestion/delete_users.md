---
nav_title: CDIによるユーザーの削除
article_title: クラウドデータ取り込みによるユーザーの削除
page_order: 30
page_type: reference
description: "このページでは、Cloud Data Ingestion を使用したユーザーの削除手順の概要を説明します。"

---

# クラウドデータ取り込みによるユーザーの削除

> このページでは、Cloud Data Ingestion を使用してユーザーを削除するプロセスについて説明します。

ユーザー削除の同期は、利用可能なすべてのクラウドデータ取り込みデータソースでサポートされています。 

## 統合の設定 

標準のプロセスに従って、接続するデータウェアハウスの Braze ダッシュボードで[新しい統合を作成]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/#step-1-set-up-tables-or-views)します。削除テーブルにアクセスできるロールが含まれていることを確認してください。**Create import sync** ページで、**データタイプ**を **Delete Users** に設定し、統合実行中にユーザーを削除するための適切なアクションが実行されるようにします。

![]({% image_buster /assets/img/cloud_ingestion/deletion_1.png %})

## ソースデータの設定

ユーザー削除のソーステーブルには、1 つ以上のユーザー識別子タイプと `UPDATED_AT` タイムスタンプを含める必要があります。ペイロード列は、ユーザー削除データではサポートされていません。

### `UPDATED_AT`

ソーステーブルに `UPDATED_AT` タイムスタンプを追加します。このタイムスタンプは、この行が更新されたか、テーブルに追加された時点を示します。Braze は、`UPDATED_AT` が最後に同期された値より後の行を同期します。同じタイムスタンプを持つ新しい行がある場合、境界のタイムスタンプにある行は再同期される可能性があります。

### ユーザー識別子列

テーブルには、ユーザー識別子列を 1 列以上含めることができます。各行には、識別子（`external_id` 単独か、`alias_name` と `alias_label` の組み合わせ、または `braze_id`）を 1 つのみ含める必要があります。ソーステーブルには、1 つ、2 つ、または 3 つすべての識別子タイプの列を含めることができます。
- `EXTERNAL_ID` - 更新対象のユーザーを特定します。これは Braze で使用されている `external_id` 値と一致する必要があります。 
- `ALIAS_NAME` および `ALIAS_LABEL` - この 2 列はユーザーエイリアスオブジェクトを作成します。`alias_name` はユニークな識別子である必要があり、`alias_label` はエイリアスのタイプを指定します。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は 1 つしか持てません。
- `BRAZE_ID` - Braze のユーザー識別子です。これは Braze SDK によって生成されます。クラウドデータ取り込み経由で Braze ID を使用して新規ユーザーを作成することはできません。新規ユーザーを作成するには、外部ユーザー ID またはユーザーエイリアスを指定してください。 

{% alert important %}
ユーザーを削除する目的で、テーブルに `PAYLOAD` 列を含めないでください。ユーザーの偶発的かつ永久的な削除を防ぐため、ソーステーブルにペイロード列がある場合、同期は失敗します。その他の列は許可されますが、Braze では無視されます。
{% endalert %}

{% tabs %}
{% tab Snowflake %}
```sql
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
```sql
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
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
{% endtab %}

{% tab Databricks %}
次のフィールドを持つテーブルを作成します。

| フィールド名 | タイプ | モード |
|---|---|---|
| `UPDATED_AT`| TIMESTAMP | REQUIRED |
| `EXTERNAL_ID`| STRING | NULLABLE |
| `ALIAS_NAME`| STRING | NULLABLE |
| `ALIAS_LABEL`| STRING | NULLABLE |
| `BRAZE_ID`| STRING | NULLABLE |
{% endtab %}
{% tab Microsoft Fabric %}
```sql
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

### 仕組み

Braze のクラウドデータ取り込みでは、データウェアハウスインスタンスと Braze ワークスペースの間の統合を設定して、定期的にデータを同期します。この同期は設定したスケジュールで実行され、統合ごとに異なるスケジュールを設定できます。同期は最短で 15 分ごと、最長で月に 1 回の頻度で実行できます。15 分より短い間隔で同期を実行する必要がある場合は、カスタマーサクセスマネージャーにご相談いただくか、リアルタイムのデータ取り込みに REST API 呼び出しの使用をご検討ください。

同期が実行されると、Braze はデータウェアハウスインスタンスに直接接続し、指定されたテーブルからすべての新しいデータを取得して、Braze ダッシュボード上の対応するユーザープロファイルを削除します。 

{% alert warning %}
ユーザープロファイルの削除は元に戻せません。ユーザーが完全に削除されるため、データの不整合が発生する可能性があります。詳細については、[ユーザープロファイルの削除]({{site.baseurl}}/help/help_articles/api/delete_user/)を参照してください。
{% endalert %}

<br><br>