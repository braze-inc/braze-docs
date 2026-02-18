---
nav_title: Snowflakeデータ共有
hidden: true
---

# Snowflake データシェアリング統合

> Snowflake Data Shareが統合方法として使用される場合、Brazeが顧客に代わってSnowflakeインスタンスに共有をプロビジョニングする。この共有には、すべてのメッセージのエンゲージメントとユーザー行動のイベントが自動的に含まれる。

顧客が Snowflake データシェア資格を購入した後、シェアは顧客ごとにプロビジョニングされます。顧客がデータ共有を要求すると、Brazeは顧客のワークスペースに共有を追加し、顧客はセルフサービスUIを使って関連するパートナーのSnowflakeアカウントデータを追加できる。

![]({% image_buster /assets/img/snowflake.png %})

共有がプロビジョニングされると、すべてのデータは受信データ共有としてSnowflakeインスタンス内からすぐにアクセスできるようになる。

![]({% image_buster /assets/img/snowflake2.png %})

Snowflakeインスタンス内では、リージョンごとに1つのシェアが表示される。各テーブルには `app_group_id` という列があり、これは実質的な Braze のテナントキーです。新しい顧客が同じリージョン内のシェアに追加されると、この顧客は既存のテーブル内では異なる `app_group_ids` として表示されます。

{% alert important %}
Braze は現在、すべてのユーザーレベルのデータを Snowflake AWS US East-1 および EU-Centra (フランクフルト) リージョンでホストしています。Braze はクロスリージョンで共有できますが、`US-EAST-1` および/または `EU-CENTRAL-1` と共有すると、これは顧客にとって最もコスト効率が高くなります。
{% endalert %}

{% alert tip %}
[未加工のテーブル・スキーマは]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt?ffbc5f5ca7092bc9ae26268aa0e711df)こちらからダウンロードするか、スノーフレーク・マーケットプレイスで入手可能な[サンプル・イベント・データ](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XY0/braze-braze-user-event-demo-dataset)・セットを使用して、共有されるイベントに慣れることができる。
{% endalert %}

## 重複イベントを処理する

重複は予想されるが、すべてのイベントはIDカラムという一意の識別子を持っている。`select distinct(id)` を実行すると重複を解消できます。

## 破壊的な変更と非破壊的な変更

### 非破壊的な変更

非破壊的な変更はいつでも発生する可能性があり、一般的に追加の機能を提供します。非破壊的な変更の例には次のものがあります。
- 新しいテーブルまたはビューを追加する
- 既存のテーブルやビューにカラムを追加する

{% alert important %}
新しい列の追加は非破壊的な変更と見なされるため、Braze では `SELECT *` クエリを使用する代わりに、各クエリで関心のある列を明示的に列挙することを強くお勧めします。または、列に明示的に名前を付けるビューを作成してから、テーブルではなくそれらのビューを直接クエリすることもできます。
{% endalert %}

### 破壊的な変更

可能な場合には、破壊的な変更の前に通知を行い、移行期間を設けます。破壊的な変更の例には次のものがあります。
- テーブルまたはビューを削除する
- 既存のテーブルやビューからカラムを削除する
- 既存のカラムのタイプまたはヌル可能性を変更する

## SNAPSHOTS およびCHANGELOGS 表が更新 d の場合

SNAPSHOTSテーブルとCHANGELOGSテーブルは、キャンペーンとキャンバスの変更を追跡します。これらのテーブルが更新であるかどうかを理解することは、最新のメッセージバリエーションやキャンバス設定を照会する際に大切です。

### CHANGELOGS_CAMPAIGN_SHARED

以下の場合、`CHANGELOGS_CAMPAIGN_SHARED` に行が追加されます。
- キャンペーンが起動されます
- 次のスナップショットテーブルフィールドのいずれかが変更されます。
  - 名前
  - アクション(メッセージ内容の変更を含む)
  - 変換動作

{% alert important %}
起動後の下書きを保存または更新しても、更新は自動的にトリガーされません。更新がトリガーされるのは、キャンペーンを起動した場合、または起動後のキャンペーンへの変更をアプリした場合のみです。起動後の下書きは変更されます。
{% endalert %}

### SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED

`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` は`CHANGELOGS_CAMPAIGN_SHARED` から派生したものです。このテーブルは、`CHANGELOGS_CAMPAIGN_SHARED` からアクションs 列を抽出し、個々のメッセージバリエーションレコードに統合します。`CHANGELOGS_CAMPAIGN_SHARED`が更新dのときは、それに応じて更新dとなる。

### CHANGELOGS_CANVAS_SHARED

以下の場合、`CHANGELOGS_CANVAS_SHARED` に行が追加されます。
- キャンバスが起動するか、または
- 次のスナップショットテーブルフィールドのいずれかが変更されます。
  - 名前
  - 変換動作
  - バリエーション(パーセンテージe、最初のステップ代入、バリエーションの名前)

{% alert important %}
起動後の下書きを保存または更新しても、更新は自動的にトリガーされません。更新は、キャンバスを起動したときにのみトリガーされます。または、起動後の下書きがアクティブキャンバスに変更されるのをアプリします。
{% endalert %}

### SNAPSHOTS_CANVAS_VARIATION_SHARED

`SNAPSHOTS_CANVAS_VARIATION_SHARED` は`CHANGELOGS_CANVAS_SHARED` から派生したものです。このテーブルは、`SNAPSHOTS_CAMPAIGN_MESSAGE_VARIATION_SHARED` と同じエクストアクションパターンを使用し、`CHANGELOGS_CANVAS_SHARED` が更新 d の場合は更新 d になります。

### SNAPSHOTS_CANVAS_STEP_SHARED

以下の場合、`SNAPSHOTS_CANVAS_STEP_SHARED` に行が追加されます。
- キャンバスが起動するか、または
- アクティブキャンバスが更新d (起動後の下書き アプリが嘘)、または
- 次のスナップショットテーブルフィールドのいずれかが変更されます。
  - 名前
  - アクション(メッセージバリエーション内でのメッセージ内容の変更を含む)

{% alert important %}
起動後の下書きを保存しても、更新は自動的にトリガーされません。更新は、キャンバスを起動したときにのみトリガーされます。または、起動後の下書きがアクティブキャンバスに変更されるのをアプリします。
{% endalert %}

### SNAPSHOTS_CANVAS_FLOW_STEP_SHARED

以下の場合、`SNAPSHOTS_CANVAS_FLOW_STEP_SHARED` に行が追加されます。
- キャンバスが起動するか、または
- アクティブキャンバスが更新d (起動後の下書き アプリが嘘)、または
- 次のスナップショットテーブルフィールドのいずれかが変更されます。
  - 名前

{% alert important %}
起動後の下書きを保存しても、更新は自動的にトリガーされません。更新は、キャンバスを起動したときにのみトリガーされます。または、起動後の下書きがアクティブキャンバスに変更されるのをアプリします。
{% endalert %}

## 一般データ保護規則 (GDPR) への準拠

{% include partners/snowflake_pii_gdpr.md %}