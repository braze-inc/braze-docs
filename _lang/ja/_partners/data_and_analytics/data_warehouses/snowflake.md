---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "この記事では、Braze と Snowflake のパートナーシップについて説明します。データ共有（Braze から Snowflake）とクラウドデータ取り込み（Snowflake から Braze）の両方を取り上げます。"
page_type: partner
search_tag: Partner

---

# Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) は、Software-as-a-Service (SaaS) として提供される専用 SQL クラウドデータウェアハウスです。Snowflake のデータウェアハウスは、従来のデータウェアハウス製品よりも高速で使いやすく、極めて高い柔軟性を備えています。Snowflake 独自の特許取得済みアーキテクチャにより、すべてのデータを集約し、迅速な分析を可能にし、すべてのユーザーにデータドリブン型のインサイトを提供することが容易になります。

Braze は Snowflake との2つの統合を提供しています。これらを組み合わせることで、Braze と Snowflake 環境間の完全な双方向データパイプラインを実現します。

## 統合の選択

### データ共有（Braze から Snowflake）

Snowflake の [Secure Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/) により、Braze のエンゲージメントおよびキャンペーンデータに Snowflake インスタンスから直接、安全かつリアルタイムにアクセスできます。アカウント間でデータのコピーや転送は行われません。すべての共有は Snowflake 独自のサービスレイヤーとメタデータストアを介して行われます。

**データ共有は次のような場合に使用します。**
- Snowflake SQL を使用して Braze のイベントおよびキャンペーンデータをクエリする
- 複雑なレポートを作成し、アトリビューションモデリングを実行する
- Braze データを Snowflake ウェアハウス内の他のデータと結合する
- チャネル、業界、デバイスプラットフォーム全体でエンゲージメントデータをベンチマークする

設定手順については、[Snowflake データ共有]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/data_sharing/)を参照してください。

### クラウドデータ取り込み（Snowflake から Braze）

[クラウドデータ取り込み（CDI）]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/)を使用すると、Snowflake インスタンスから Braze にデータを直接同期できます。これにより、Braze のユーザー属性、イベント、購入を、信頼できる唯一の情報源であるデータウェアハウスと常に最新の状態に保つことができます。

**クラウドデータ取り込みは次のような場合に使用します。**
- Snowflake から Braze のユーザープロファイルにユーザー属性を同期する
- Snowflake から Braze にイベントまたは購入データを送信する
- ウェアハウスで行われるデータ変換と Braze を同期させる
- Snowflake から Braze へのカスタム ETL パイプラインの構築と保守を回避する

Snowflake のデータ共有の詳細については、[Introduction to Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work) を参照してください。

## 前提条件

この機能を使用する前に、以下を完了しておく必要があります。

| 必要条件 | 説明 |
| ----------- | ----------- |
| Braze へのアクセス | Braze でこの機能を使用するには、Braze アカウントまたはカスタマーサクセスマネージャーに連絡する必要があります。 |
| Snowflake アカウント | `admin` の権限を持つ Snowflake アカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 安全なデータ共有の設定

Snowflake では、データ共有は[データプロバイダー](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)と[データ消費者](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)の間で行われます。このコンテキストでは、データシェアを作成して送信するため、Braze アカウントがデータプロバイダーとなります。一方、データシェアを使用してデータベースを作成するため、Snowflake アカウントがデータ消費者となります。詳細は、[Snowflake: Consuming Shared Data](https://docs.snowflake.com/en/user-guide/data-share-consumers) を参照してください。

### ステップ 1: Braze からデータシェアを送信する

1. Braze で、[**パートナー連携**] > [**データ共有**] に移動します。
2. Snowflake アカウントの詳細とロケーターを入力します。アカウントロケーターを取得するには、送信先アカウントで `SELECT CURRENT_ACCOUNT()` を実行します。
3. CRR 共有をご利用の場合は、クラウドプロバイダーとリージョンを指定してください。
4. 完了したら、[**データ共有を作成**] を選択します。これでデータシェアが Snowflake アカウントに送信されます。

### ステップ 2: Snowflake でデータベースを作成する

1. 数分後に、Snowflake アカウントでインバウンドデータシェアを受信します。
2. インバウンドデータシェアを使用して、テーブルを表示しクエリするためのデータベースを作成します。以下に例を示します。
    ```sql
    CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>
    ```
3. 新しいデータベースをクエリする権限を付与します。

{% alert warning %}
Braze ダッシュボードで共有を削除して再作成する場合は、以前に作成したデータベースを削除し、`CREATE DATABASE <name> FROM SHARE <provider_account>.<share_name>` を使用して再作成し、インバウンド共有にクエリを実行する必要があります。
複数のワークスペースが同じ Snowflake アカウントにデータを共有している場合は、マルチワークスペース設定の管理に関するガイダンスについて [Snowflake データ共有の FAQ]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/faqs/) を参照してください。
{% endalert %}

## 使用と視覚化

データ共有のプロビジョニングが完了したら、受信するデータ共有からデータベースを作成する必要があります。これにより、共有されているすべてのテーブルが Snowflake インスタンスに表示され、インスタンスに保存されている他のデータと同様にクエリ可能になります。ただし、共有データは読み取り専用であり、クエリのみ可能で、変更や削除は一切できないことにご注意ください。

Currents と同様に、Snowflake Secure Data Sharing を使用して次のことができます。

- 複雑なレポートを作成する
- アトリビューションモデリングを実行する
- 自社内での安全な共有
- 生のイベントまたはユーザーデータを CRM（Salesforce など）にマッピングする
- その他多数

利用可能なテーブルと列の完全なリストについては、[SQL テーブルリファレンス]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/sql_segments_tables/)を参照してください。Snowflake データ共有には、そのリファレンスのすべてのテーブルに加え、スナップショット、キャンペーンおよびキャンバスの変更ログ、エージェントコンソールイベント、メッセージリトライイベント用の Snowflake 専用テーブルが含まれます。

[未加工のテーブルスキーマをダウンロード]({% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %})してテキストファイルとして確認することもできます。

### ユーザー ID スキーマ

Braze と Snowflake でのユーザー ID の命名規則の違いに注意してください。

| Braze スキーマ | Snowflake スキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Braze によって自動的に割り当てられるユニークな識別子です。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されたユーザープロファイルのユニークな識別子です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 重要な情報と制限

### 破壊的な変更と非破壊的な変更

#### 非破壊的な変更

非破壊的な変更はいつでも発生する可能性があり、一般的に追加の機能を提供します。非破壊的な変更の例には次のものがあります。
- 新しいテーブルまたはビューを追加する
- 既存のテーブルやビューにカラムを追加する

{% alert important %}
新しい列の追加は非破壊的な変更と見なされるため、Braze では `SELECT *` クエリを使用する代わりに、各クエリで関心のある列を明示的に列挙することを強くお勧めします。あるいは、列を明示的に名前付けするビューを作成し、テーブルを直接クエリする代わりにそれらのビューをクエリすることを検討してください。
{% endalert %}

#### 破壊的な変更

可能な場合には、破壊的な変更の前に通知を行い、移行期間を設けます。破壊的な変更の例には次のものがあります。
- テーブルまたはビューを削除する
- 既存のテーブルやビューからカラムを削除する
- 既存の列の型または null 許容性を変更する

### Snowflake のリージョン

Braze は現在、Snowflake AWS US East-1、EU-Central（フランクフルト）、AP-Southeast-2（シドニー）、AP-Southeast-3（ジャカルタ）リージョンですべてのユーザーレベルデータをホストしています。これらのリージョン外のユーザーの場合、Braze は、Snowflake インフラを AWS、Azure、または GCP の任意のリージョンでホストしている共同の顧客にデータ共有を提供できます。

### データリテンション

#### 保存方針

2年以上前のデータはすべてアーカイブされ、長期保存に移されます。アーカイブプロセスの一環として、すべてのイベントは匿名化され、個人を特定できる情報（PII）が含まれる機密フィールドはすべて削除されます（これには、`properties` のようなオプションの PII フィールドも含まれます）。アーカイブされたデータには依然として `user_id` フィールドが含まれており、すべてのイベントデータにわたるユーザーごとの分析が可能です。

対応する `USERS_*_SHARED` ビューで各イベントの直近2年間のデータをクエリできます。さらに、各イベントには `USERS_*_SHARED_ALL` ビューが用意されており、匿名化されたデータと非匿名化されたデータの両方を返すクエリを実行できます。

#### 履歴データ

Snowflake の履歴イベントデータのアーカイブは2019年4月まで遡ります。Braze が Snowflake にデータを保存し始めた最初の数ヶ月間に、製品の変更が行われ、そのデータの一部がわずかに異なって見えたり、いくつかのフィールドに null 値が含まれている可能性があります（この時点ではすべての利用可能なフィールドにデータを渡していなかったため）。2019年8月以前のデータを含む結果は、予期される結果と多少異なる可能性があると想定しておくことをお勧めします。

### 一般データ保護規則（GDPR）準拠

{% multi_lang_include partners/snowflake_pii_gdpr.md %}

### スピード、パフォーマンス、クエリのコスト

データに対して実行されるクエリの速度、パフォーマンス、およびコストは、データのクエリに使用するウェアハウスのサイズによって決まります。場合によっては、分析のためにアクセスしているデータ量に応じて、クエリを成功させるためにより大きなウェアハウスサイズを使用する必要があるかもしれません。Snowflake には、[ウェアハウスの概要](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html)や[ウェアハウスの考慮事項](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)など、どのサイズを使用するかを最適に判断する方法に関する優れたリソースが用意されています。

> Snowflake の設定時に参照できるサンプルクエリセットについては、[サンプルクエリ]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/)および [ETL イベントパイプライン設定]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/)の例をご確認ください。

設定手順については、[クラウドデータ取り込み: データウェアハウス統合]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/integrations/)を参照してください。