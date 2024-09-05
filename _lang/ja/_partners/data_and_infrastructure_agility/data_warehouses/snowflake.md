---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "このリファレンス記事は、Braze と Snowflake のパートナーシップについて概説しています。Snowflake は、すべてのデータとユーザーのために特別に構築された SQL クラウド データウェアハウスです。"
page_type: partner
search_tag: Partner

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) は、Software-as-a-Service (SaaS) として提供される目的別 SQL クラウド データウェアハウスです。Snowflakeは、従来のデータウェアハウス製品よりも高速で使いやすく、はるかに柔軟なデータウェアハウスを提供します。Snowflakeのユニークで特許取得済みのアーキテクチャにより、すべてのデータを集約し、迅速な分析を可能にし、すべてのユーザーにデータドリブン型のインサイトを提供することが容易になります。

パーソナライズされたおよび関連性のあるマーケティングキャンペーンには、その瞬間のデータへのアクセスが必要です。だからこそBrazeはSnowflakeと提携してデータ共有を開始しました。この共同提供により、マーケターはこれまでになく迅速にカスタマーエンゲージメントおよびキャンペーンデータの可能性を引き出すことができます。

[BrazeとSnowflakeの統合](https://www.braze.com/perspectives/article/snowflake-partner-announcement)は、Snowflakeのデータ交換を活用してプレゼンスを構築し、新しい顧客を見つけ、増え続けるSnowflakeの顧客基盤を通じてリーチを拡大します。

{% alert tip %}
**SnowflakeアカウントがなくてもSnowflakeレベルのデータにアクセスできることに興味がありますか？**<br>[Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)をチェックしてください。Reader Accounts では、Braze がお客様のデータを作成してアカウントと共有し、またログインしてデータにアクセスするための認証情報を用意します。これにより、すべてのデータ共有と使用量請求は  Braze が完全に処理することになります。
{% endalert %}

## データ共有とは何ですか？

Snowflakeの[Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html)機能により、BrazeはSnowflakeポータル上のデータへの安全なアクセスを提供し、通常のデータ提供者との関係に伴うワークフローの摩擦や遅延、失敗点、不必要なコストを心配することなく利用できます。データ共有は、次の統合を通じて、または[Snowflake Reader Accounts]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)を通じて設定できます。

- **洞察までの時間を短縮する**<br>ETLプロセスの構築に数週間かかることにさよならを言いましょう。BrazeとSnowflakeのユニークなアーキテクチャにより、すべてのカスタマーエンゲージメントおよびキャンペーンデータは、データレイクに到着した瞬間から即座にアクセス可能でクエリ可能になります。データはコピーまたは移動されないため、最も関連性が高く最新の情報に基づいて顧客体験を提供できます。
- **データサイロ化を解消する**<br>チャネルやプラットフォーム全体で顧客の全体像を把握する。データ共有により、Brazeのカスタマーエンゲージメントデータを他のすべてのSnowflakeデータと結合することがこれまでになく簡単になり、単一の信頼できる情報源全体でより豊かな洞察を生み出します。
- **あなたのエンゲージメントがどのように積み重なるかを確認してください**<br>Brazeベンチマークを使用して、カスタマーエンゲージメント戦略を最適化します。このインタラクティブツールは、BrazeとSnowflakeによって提供されており、ブランドのエンゲージメントデータをチャネル、業界、デバイスプラットフォーム全体のベンチマークと比較することができます。

データ共有では、実際のデータはアカウント間でコピーまたは転送されません。すべての共有は、Snowflakeのユニークなサービス層とメタデータストアを通じて行われます。これは重要な概念です。なぜなら、共有データは消費者アカウントにストレージを占有せず、したがって消費者の月間データストレージ料金に寄与しないからです。消費者への唯一の請求は、共有データをクエリするために使用されるコンピューティングリソース（仮想ウェアハウスなど）に対してです。

さらに、Snowflake の組み込みロールと権限機能を使用して、Braze から共有されたデータへのアクセスを、Snowflake アカウントおよびその中のデータに既に設定されているアクセス制御を使用して制御および管理できます。アクセスは、あなた自身のデータと同じ方法で制限および監視できます。

[セキュアデータ共有の紹介](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)をチェックして、Snowflakeのデータ共有の仕組みについて詳しく読んでください。

## 前提条件

この統合に興味がある場合は、Brazeアカウントまたは顧客成功マネージャーに連絡し、Snowflakeとのセキュアデータ共有に関するBrazeデータ戦略サービスに相談するよう依頼してください。これによりBrazeの内部で歯車が回り始め、すぐにビューが設定されます！

| 要件 | 説明 |
| ----------- | ----------- |
| Snowflakeアカウント | このパートナーシップを利用するには、管理者レベルの権限を持つSnowflakeアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

Brazeアカウントでセキュアデータ共有を設定するには、次の手順に従ってください。

1. Brazeダッシュボードの**パートナー統合** > **データ共有**に移動します。
2. Snowflakeアカウントの詳細を入力してください。送信先アカウントで`SELECT CURRENT_ACCOUNT()`を実行することにより、SnowflakeアカウントIDを見つけることができます。
3. クラウドプロバイダーとリージョンを指定してください。
4. **「データ共有の作成」を選択**。

数分以内に、データ共有がSnowflakeインスタンスに表示されるはずです。共有からデータベースを作成して、テーブルを表示およびクエリできるようにします。データ共有を見るには、アカウント管理者である必要があることに注意してください。

![インバウンドデータ共有]({% image_buster /assets/img/inbound-data-share.png %})

データ共有の文脈では、Brazeは[データプロバイダー](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)です。つまり、共有を作成し、他のSnowflakeアカウントが消費できるようにするSnowflakeアカウントです。あなたは[データ消費者](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)です—データプロバイダーによって提供された共有からデータベースを作成することを選択するアカウントです。

## 使用と視覚化

データ共有がプロビジョニングされると、受信データ共有からデータベースを作成する必要があります。これにより、共有されたすべてのテーブルがSnowflakeインスタンスに表示され、インスタンスに保存されている他のデータと同様にクエリ可能になります。ただし、共有データは読み取り専用であり、照会のみ可能で、変更や削除は一切できません。

Currentsと同様に、Snowflake Secure Data Sharingを使用して次のことができます:
- 複雑なレポートを作成する
- アトリビューション モデリングを実行する
- 自社内での安全な共有
- 生のイベントまたはユーザーデータをCRM（Salesforceなど）にマッピングする
- さらに

[生のテーブルスキーマをここからダウンロードしてください。][schemas]

### ユーザー ID スキーマ

ユーザーIDの命名規則に関するBrazeとSnowflakeの違いに注意してください。

| Brazeスキーマ | スノーフレークスキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Brazeによって自動的に割り当てられる一意の識別子。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されたユーザーのプロファイルの一意の識別子。 |
{: .reset-td-br-1 .reset-td-br-2}

## 重要な情報と制限

### 非互換変更と互換変更

#### 非破壊的な変更
非破壊的な変更はいつでも発生する可能性があり、一般的に追加の機能を提供します。非破壊的変更の例：
- 新しいテーブルまたはビューの追加
- 既存のテーブルまたはビューに列を追加する

{% alert important %}
新しい列は非破壊と見なされるため、Braze は `SELECT *` クエリを使用する代わりに、各クエリで関心のある列を明示的に列挙することを強くお勧めします。あるいは、列を明示的に名前付けするビューを作成し、それらのビューを直接テーブルの代わりにクエリすることを検討するかもしれません。
{% endalert %}

#### 破壊的な変更
可能な場合、破壊的変更は発表と移行期間を伴います。破壊的変更の例には次のようなものがあります:
- テーブルまたはビューの削除
- 既存のテーブルまたはビューから列を削除する
- 既存の列の型またはnull許容性を変更する

### Snowflakeリージョン
Brazeは現在、すべてのユーザーレベルのデータをSnowflake AWS US East-1およびEU-Central（フランクフルト）リージョンにホストしています。これらの地域外のユーザーに対して、Braze は、Snowflake インフラストラクチャを任意の AWS、Azure、または GCP リージョンにホストしている共同顧客へのデータ共有を提供できます。

### データリテンション

#### リテンションポリシー
2年以上前のデータはすべてアーカイブされ、長期保存に移されます。アーカイブプロセスの一環として、すべてのイベントは匿名化され、個人を特定できる情報 (PII) の機密フィールドはすべて削除されます（これには、`properties` のようなオプションの PII フィールドも含まれます）。アーカイブされたデータには依然として`user_id`フィールドが含まれており、すべてのイベントデータにわたるユーザーごとの分析が可能です。

対応する`USERS_*_SHARED`ビューで各イベントの直近2年間のデータを照会できます。さらに、各イベントには、匿名化されたデータと非匿名化されたデータの両方を返すためにクエリを実行できる`USERS_*_SHARED_ALL`ビューが用意されています。

#### 歴史的なデータ
Snowflake における歴史的イベントデータのアーカイブは、2019年4月に遡ります。BrazeがSnowflakeにデータを保存し始めた最初の数ヶ月間に、製品の変更が行われ、そのデータの一部がわずかに異なって見えたり、いくつかのフィールドにnull値が含まれている可能性があります（この時点ではすべての利用可能なフィールドにデータを渡していなかったため）。2019年8月以前のデータを含む結果は、予想と少し異なる可能性があると考えるのが最善です。

### 一般データ保護規則（GDPR）準拠
ほぼすべてのイベントレコードBrazeには、ユーザーの個人を特定できる情報（PII）を表すいくつかのフィールドが含まれています。一部のイベントには、メールアドレス、電話番号、デバイスID、言語、性別、および位置情報が含まれる場合があります。ユーザーの削除依頼がBrazeに送信された場合、これらのユーザーに属するイベントのPIIフィールドを無効化します。この方法では、イベントの歴史的記録を削除することはありませんが、今ではイベントが特定の個人に結びつけられることは決してありません。

### スピード、パフォーマンス、クエリのコスト
クエリを実行するために使用するウェアハウスのサイズによって、データ上で実行されるクエリの速度、パフォーマンス、およびコストが決まります。場合によっては、分析のためにアクセスしているデータ量によって、クエリを成功させるためにより大きなウェアハウスサイズを使用する必要があるかもしれません。Snowflakeには、[ウェアハウスの概要](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html)や[ウェアハウスの考慮事項](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)など、どのサイズを使用するかを最適に判断する方法に関する優れたリソースが用意されています。

## Braze Benchmarks

ベンチマーク、[Brazeによって構築されたデータツール](https://www.braze.com/perspectives/benchmarks)は、Brazeの見込み客と顧客が自社の指標をBrazeの業界ベンチマークと比較することで、業界のトッププレーヤーとどのように比較されるかを確認できるようにします。

初期産業には以下が含まれます：
- 配達サービス
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

ベンチマークデータは、[Snowflake Data Exchange](https://app.snowflake.com/marketplace/listing/GZT0Z5I4XXR)で直接入手できます。

> Snowflakeの設定時に参照するためのサンプルクエリセットについては、[サンプルクエリ][SQ]および[ETLイベントパイプライン設定][ETL]の例を確認してください。

[SQ]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/sample_queries/
[ETL]: {{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/etl_pipline_setup/
[schemas]: {% image_buster /assets/download_file/data-sharing-raw-table-schemas.txt %}
