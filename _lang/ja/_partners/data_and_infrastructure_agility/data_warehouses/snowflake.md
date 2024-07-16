---
nav_title: Snowflake
article_title:Snowflake
alias: /partners/snowflake/
description:"この参考記事では、BrazeとSnowflakeのパートナーシップについて概説している。"Snowflakeは、すべてのデータとユーザーのための専用SQLクラウドデータウェアハウスである。
page_type: partner
search_tag:Partner

---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake

> [Snowflakeは](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html)、SaaS（Software-as-a-Service）として提供される専用のSQLクラウドデータウェアハウスである。Snowflakeは、従来のデータウェアハウスよりも高速で、使いやすく、はるかに柔軟なデータウェアハウスを提供する。Snowflake's unique and patented architecture, it'を使用すると、すべてのデータを簡単に収集し、迅速な分析を可能にし、すべてのユーザーに対してデータドリブン型のインサイトを導き出すことができる。

パーソナライズされた適切なマーケティングキャンペーンを行うには、データに瞬時にアクセスする必要がある。そこでBrazeはSnowflakeと提携し、データ共有を開始した。この共同提供により、マーケターは顧客エンゲージメントとキャンペーンデータの潜在能力をこれまで以上に迅速に引き出すことができる。

[BrazeとSnowflakeの統合は](https://www.braze.com/perspectives/article/snowflake-partner-announcement)、Snowflakeのデータ交換を活用し、プレゼンスを構築し、新規顧客を見つけ、成長し続けるSnowflake顧客ベースを通じてリーチを拡大する。

{% alert tip %}
**SnowflakeアカウントなしでSnowflakeレベルのデータにアクセスすることに興味があるか？**<br>[Snowflakeの読者アカウントを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)チェックしよう。Reader Accounts では、Braze がお客様のデータを作成してアカウントと共有し、またログインしてデータにアクセスするための認証情報を用意します。これにより、すべてのデータ共有と使用量請求は  Braze が完全に処理することになります。
{% endalert %}

## データ共有とは何か？

Snowflakeの[セキュアデータ共有](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html)機能により、Brazeは、一般的なデータプロバイダーとの関係で発生するワークフローの摩擦や減速、障害ポイント、不必要なコストを心配することなく、Snowflakeポータル上のデータに安全にアクセスすることができる。データ共有は、以下の統合または[Snowflake Reader Accountsを通じて]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)設定できる。

- **インサイトまでの時間を短縮する**<br>構築に何週間もかかるETLプロセスに別れを告げよう。BrazeとSnowflakeのユニークなアーキテクチャにより、すべてのカスタマーエンゲージメントデータとキャンペーンデータは、データレイクに到着した瞬間から即座にアクセスでき、クエリ可能になる。データのコピーや移動がないため、最も関連性の高い最新情報のみに基づいてカスタマーエクスペリエンスを提供できる。
- **データのサイロ化を解消する**<br>チャネルやプラットフォームを横断して、顧客の全体像を把握する。データ共有により、Brazeカスタマーエンゲージメントデータと他のすべてのSnowflakeデータとの結合がこれまで以上に簡単になり、信頼できる単一のデータソースでより豊かなインサイトを作成できる。
- **エンゲージメントを確認する**<br>カスタマーエンゲージメント戦略をBraze Benchmarksで最適化しよう。BrazeとSnowflakeが提供するこのインタラクティブなツールでは、チャネル、業界、デバイスプラットフォームを横断して、ブランドのエンゲージメントデータをベンチマークと比較することができる。

データ共有では、アカウント間で実際のデータがコピーされたり転送されたりすることはない。すべての共有は、Snowflake's unique services layer and metadata store. This is an important concept because shared data does not take up any storage in a consumer account and, therefore, does not contribute to the consumer'の月額データ保存料を通じて行われる。消費者に請求されるのは、共有データへのクエリに使用されるコンピューター・リソース（仮想ウェアハウスなど）の**料金のみ**である。

さらに、Snowflakeに組み込まれた役割と権限機能を使用して、Brazeから共有されるデータへのアクセスは、Snowflakeアカウントとその中のデータに対してすでに設定されているアクセスコントロールを使用してコントロールおよび管理することができる。自分のデータと同じようにアクセスを制限し、監視することができる。

Snowflakeのデータ共有の仕組みについては、「[安全なデータ共有入門](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)」を参照されたい。

## 前提条件

この統合に興味がある場合は、Brazeアカウントマネージャーまたはカスタマーサクセスマネージャーに連絡し、Snowflakeとのセキュアなデータ共有に関するBrazeデータ戦略サービスを相談するよう依頼する。これでBraze内部の歯車が動き出し、すぐにビューの設定ができるだろう！

| 必要条件 | 説明 |
| ----------- | ----------- |
| Snowflakeアカウント | このパートナーシップを利用するには、管理者レベルの権限を持つSnowflakeアカウントが必要である。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Brazeアカウントで安全なデータ共有を設定するには、以下のステップに従う。 

1. ダッシュボードの**Partner Integrations**>**Data Sharingに**移動する。
2. Snowflakeアカウントの詳細を入力する。SnowflakeのアカウントIDは、送信先アカウントで`SELECT CURRENT_ACCOUNT()` 。
3. CRR共有を使っている場合は、クラウド・プロバイダーと地域を指定する。
4. **データシェアの作成**」を選択する。

しばらくすると、データ共有がSnowflakeインスタンスに表示されるはずだ。共有からデータベースを作成し、テーブルを見たり問い合わせたりできるようにする。なお、データ共有を見るにはアカウント管理者である必要がある。

![Inbound data share]({% image_buster /assets/img/inbound-data-share.png %})

データ共有の文脈では、Brazeは[データプロバイダーであり、](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)共有を作成し、他のSnowflakeアカウントが利用できるようにするSnowflakeアカウントである。あなたは[データ消費者であり、](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)データプロバイダーが提供する共有データからデータベースを作成することを選択するアカウントである。

## 使用法と視覚化

データ共有のプロビジョニングが完了したら、受信したデータ共有からデータベースを作成し、共有されたすべてのテーブルをSnowflakeインスタンスに表示させ、インスタンスに保存している他のデータと同様にクエリ可能にする必要がある。ただし、共有データは読み取り専用であり、照会はできるが、変更や削除は一切できないことに留意してほしい。

Currentsと同様に、Snowflakeセキュアデータシェアリングを使用することができる：
- 複雑なレポートを作成する
- アトリビューション・モデリングを行う。
- 社内での安全な共有
- 生のイベントまたはユーザーデータをCRM（Salesforceなど）にマッピングする。
- そしてさらに

\[生のテーブル・スキーマはこちらからダウンロードできる。

### ユーザーIDスキーマ

ユーザーIDに関するBrazeとSnowflakeの命名規則の以下の違いに注意。

| Brazeスキーマ | Snowflakeスキーマ | 説明 | 
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Brazeが自動的に割り当てる一意の識別子。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されるユーザープロファイルの一意の識別子。 |
{: .reset-td-br-1 .reset-td-br-2}

## 重要な情報と制限

### 壊れる変更と壊れない変更

#### 非破壊的な変更
壊れることのない変更はいつでも可能であり、一般的に追加機能を提供する。ブレークしない変更の例：
- 新しいテーブルまたはビューを追加する
- 既存のテーブルやビューにカラムを追加する

{% alert important %}
新しいカラムは非改行カラムとみなされるため、Brazeは、`SELECT *` クエリを使用する代わりに、各クエリで目的のカラムを明示的にリストすることを強く推奨する。あるいは、カラム名を明示的に指定したビューを作成し、テーブルに直接問い合わせるのではなく、それらのビューに問い合わせることもできる。
{% endalert %}

#### 破壊的な変更
可能な限り、速報性のある変更にはアナウンスと移行期間を設ける。変更点の例としては、以下のようなものがある：
- テーブルまたはビューを削除する
- 既存のテーブルやビューからカラムを削除する
- 既存のカラムのタイプまたはヌル可能性を変更する

### 雪片地方
Brazeは現在、Snowflake AWSのUS East-1リージョンとEU-Central（フランクフルト）リージョンですべてのユーザーレベルのデータをホストしている。これらのリージョン以外のユーザーに対しては、Brazeは、AWS、Azure、GCPのいずれかのリージョンでSnowflakeインフラをホスティングしている共同顧客にデータ共有を提供することができる。

### 過去のデータ
Braze's historical event data in Snowflake goes back to April 2019. In the first few months of Braze storing data there, product changes were made that may have resulted in some of that data looking slightly different or having some null values (as we weren'、この時点で利用可能なすべてのフィールドにデータを渡す）。2019年8月以前のデータを含む結果は、予想と若干異なる可能性があると考えた方が良いだろう。

### 一般データ保護規則（GDPR）への対応
Brazeが保存するほぼすべてのイベント記録には、ユーザーを表すいくつかのフィールドが含まれている。' personally identifiable information (PII). Some events may include email address, phone number, device ID, language, gender, and location information. If a user'、Brazeに忘れ去られたいというリクエストが提出された場合、それらのユーザーに属するイベントについては、それらのPIIフィールドを無効化する。こうすることで、その出来事の歴史的記録を削除することはないが、その出来事が特定の個人に結びつくことはなくなる。

### クエリのスピード、パフォーマンス、コスト
データ上で実行されるクエリのスピード、パフォーマンス、コストは、データのクエリに使用するデータウェアハウスのサイズによって決まる。分析のためにアクセスするデータ量によっては、クエリを成功させるために、より大きなウェアハウスサイズを使用する必要があることがわかるケースもある。Snowflakeは、[倉庫の概要や](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html) [倉庫の考慮事項](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)など、どのサイズを使用するかを決定するための優れたリソースを提供している。

## Braze Benchmarks

Benchmarksは、[Brazeが構築したデータツールで](https://www.braze.com/perspectives/benchmarks)、Brazeの見込み客や顧客は、Brazeの業界ベンチマークと指標を比較することで、業界のトッププレーヤーとの比較を確認することができる。

初期産業には以下が含まれる： 
- 配送サービス
- e コマース
- 教育
- エンターテイメント
- ファイナンス
- ゲーミング
- 健康
- ライフスタイル
- レストラン
- 小売
- テクノロジー
- 交通
- 旅行

当社のベンチマークデータは、[Snowflake Data Exchangeで](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XXR)直接入手することもできる。

> Snowflakeを設定する際に参照するクエリ例については、[サンプルクエリと][SQ] [ETLイベントパイプラインの設定][ETL]例を参照のこと。

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
\[スキーマ]である： {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}
