---
nav_title: Snowflake
article_title: Snowflake
alias: /partners/snowflake/
description: "このリファレンス記事では、Braze と Snowflake のパートナーシップについて説明します。Snowflake は専用 SQL クラウドデータウェアハウスであり、お客様のすべてのデータとユーザーに対応しています。"
page_type: partner
search_tag: Partner

---

# [![Brazeラーニングコース]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/snowflake-secure-data-sharing-via-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Snowflake

> [Snowflake](https://docs.snowflake.net/manuals/user-guide/intro-key-concepts.html) は、Software-as-a-Service (SaaS) として提供される専用 SQL クラウドデータウェアハウスです。Snowflake のデータウェアハウスは、従来のデータウェアハウス製品よりも高速で使いやすく、極めて高い柔軟性を備えています。Snowflake 独自の特許取得済みアーキテクチャにより、すべてのデータを集約し、迅速な分析を可能にし、すべてのユーザーにデータドリブンのインサイトを提供することが容易になります。

パーソナライズされたおよび関連性のあるマーケティングキャンペーンには、その瞬間のデータへのアクセスが必要です。だからこそBrazeはSnowflakeと提携してデータ共有を開始しました。この共同の取り組みにより、マーケターはこれまでになく迅速にカスタマーエンゲージメントとびキャンペーンデータの可能性を引き出すことができます。

[BrazeとSnowflakeの統合](https://www.braze.com/perspectives/article/snowflake-partner-announcement)は、Snowflakeのデータ交換を活用してプレゼンスを構築し、新しい顧客を見つけ、増え続けるSnowflakeの顧客基盤を通じてリーチを拡大します。

{% alert tip %}
**Snowflake アカウントがなくても Snowflake レベルのデータにアクセスできるとしたらどうでしょうか?**<br>「[Snowflake Reader アカウント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)」をご覧ください。Reader Accounts では、Braze がお客様のデータを作成してアカウントと共有し、またログインしてデータにアクセスするための認証情報を用意します。これにより、すべてのデータ共有と使用量請求は  Braze が完全に処理することになります。
{% endalert %}

## データ共有とは何ですか？

Snowflakeの[Secure Data Sharing](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html)機能により、BrazeはSnowflakeポータル上のデータへの安全なアクセスを提供し、通常のデータ提供者との関係に伴うワークフローの摩擦や遅延、失敗点、不必要なコストを心配することなく利用できます。データ共有は、次の統合または [Snowflake Reader アカウント]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/how_braze_uses_currents/#snowflake-reader-accounts)で設定できます。

- **洞察までの時間を短縮する**<br>ETLプロセスの構築に数週間かかることにさよならを言いましょう。Braze と Snowflake の独自のアーキテクチャにより、すべてのカスタマーエンゲージメントとキャンペーンデータは、データレイクに到着した時点からすぐにアクセスおよびクエリ可能になります。データのコピーと移動は行われないので、最も関連性が高い最新の情報のみに基づいて顧客体験を提供できます。
- **データのサイロ化を解消する**<br>チャネルやプラットフォーム全体で顧客の全体像を把握する。データ共有により、Braze のカスタマーエンゲージメントデータを他のすべての Snowflake データと結合することがこれまで以上に容易になり、唯一の信頼できる情報源全体でより豊富なインサイトが作成されます。
- **お客様のエンゲージメントの状況を確認する**<br>Brazeベンチマークを使用して、カスタマーエンゲージメント戦略を最適化します。このインタラクティブツールは、BrazeとSnowflakeによって提供されており、ブランドのエンゲージメントデータをチャネル、業界、デバイスプラットフォーム全体のベンチマークと比較することができます。

データ共有では、実際のデータはアカウント間でコピーまたは転送されません。すべての共有は Snowflake 独自のサービスレイヤーとメタデータストアを介して行われます。共有データは消費者アカウントのストレージを一切使用しないため、これは重要な意味を持ちます。したがって、消費者の毎月のデータストレージ料金には影響しません。消費者に請求されるのは、共有データをクエリするために使用されるコンピューティングリソース (仮想ウェアハウスなど) **のみ**です。

さらに、Snowflake の組み込みの役割と権限の機能を使用すると、Snowflake アカウントとアカウント内のデータに対してすでに適用されているアクセス制御を使用して、Braze から共有されるデータへのアクセスを制御および管理できます。アクセスは、あなた自身のデータと同じ方法で制限および監視できます。

[セキュアデータ共有の紹介](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#how-does-secure-data-sharing-work)をチェックして、Snowflakeのデータ共有の仕組みについて詳しく読んでください。

## 前提条件

この統合について興味をお持ちの場合は、Snowflake とのセキュアデータ共有に関して Brazeデータ戦略サービスと相談するため、Braze アカウントまたはカスタマーサクセスマネージャーにご連絡ください。これにより Braze 内での手続きが開始され、お客様のビューが速やかに準備されます。

| 要件 | 説明 |
| ----------- | ----------- |
| Snowflakeアカウント | このパートナーシップを利用するには、管理者レベルの権限を持つSnowflakeアカウントが必要です。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

Brazeアカウントでセキュアデータ共有を設定するには、次の手順に従ってください。

1. Brazeダッシュボードの**パートナー統合** > **データ共有**に移動します。
2. Snowflakeアカウントの詳細を入力してください。Snowflake アカウント ID を確認するには、宛先アカウントで `SELECT CURRENT_ACCOUNT()` を実行します。
3. CRR 共有をご利用の場合は、クラウドプロバイダーとリージョンを指定してください。
4. [**データ共有を作成**] を選択します。

数分以内に、データ共有がSnowflakeインスタンスに表示されるはずです。共有からデータベースを作成して、テーブルを表示およびクエリできるようにします。データ共有を見るには、アカウント管理者である必要があることに注意してください。

![インバウンドデータ共有]({% image_buster /assets/img/inbound-data-share.png %})

データ共有の文脈では、Brazeは[データプロバイダー](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#providers)です。つまり、共有を作成し、他のSnowflakeアカウントが消費できるようにするSnowflakeアカウントです。あなたは[データ消費者](https://docs.snowflake.net/manuals/user-guide/data-sharing-intro.html#consumers)です—データプロバイダーによって提供された共有からデータベースを作成することを選択するアカウントです。

## 使用と視覚化

データ共有のプロビジョニングが完了したら、受信するデータ共有からデータベースを作成する必要があります。これにより、共有されているすべてのテーブルが Snowflake インスタンスに表示され、インスタンスに保存されている他のデータと同様にクエリ可能になります。ただし共有データは読み取り専用であり、クエリのみ可能で、変更や削除は一切できないことにご注意ください。

Currents と同様に、Snowflake セキュアデータシェアリングを使用して次のことができます:。
- 複雑なレポートを作成する
- アトリビューション モデリングを実行する
- 自社内での安全な共有
- 生のイベントまたはユーザーデータをCRM（Salesforceなど）にマッピングする
- さらに

[生テーブルスキーマをここからダウンロードしてください。][schemas]

### ユーザー ID スキーマ

次に示す Braze と Snowflake でのユーザー ID の命名規則の違いに注意してください。

| Brazeスキーマ | スノーフレークスキーマ | 説明 |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Brazeによって自動的に割り当てられる一意の識別子。 |
| `external_id` | `"EXTERNAL_USER_ID"` | 顧客によって設定されたユーザーのプロファイルの一意の識別子。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 重要な情報と制限

### 破壊的な変更と非破壊的な変更

#### 非破壊的な変更
非破壊的な変更はいつでも発生する可能性があり、一般的に追加の機能を提供します。非破壊的な変更の例には次のものがあります。
- 新しいテーブルまたはビューを追加する
- 既存のテーブルやビューにカラムを追加する

{% alert important %}
新しい列の追加は非破壊的な変更と見なされるため、Braze では `SELECT *` クエリを使用する代わりに、各クエリで関心のある列を明示的に列挙することを強くお勧めします。あるいは、列を明示的に名前付けするビューを作成し、それらのビューを直接テーブルの代わりにクエリすることを検討するかもしれません。
{% endalert %}

#### 破壊的な変更
可能な場合には、破壊的な変更の前に通知を行い、移行期間を設けます。破壊的な変更の例には次のものがあります。
- テーブルまたはビューを削除する
- 既存のテーブルやビューからカラムを削除する
- 既存の列の型またはnull許容性を変更する

### Snowflake のリージョン
Braze は現在、すべてのユーザーレベルのデータを Snowflake AWS US East-1 および EU-Centra (フランクフルト) リージョンでホストしています。これらのリージョン外のユーザーの場合、Braze は、Snowflake インフラストラクチャを AWS、Azure、または GCP リージョンでホストしている共同の顧客にデータ共有を提供できます。

### データリテンション

#### リテンションポリシー
2年以上前のデータはすべてアーカイブされ、長期保存に移されます。アーカイブプロセスの一環として、すべてのイベントは匿名化され、個人を特定できる情報 (PII) が含まれる機密フィールドはすべて削除されます (これには、`properties` のようなオプションの PII フィールドも含まれます)。アーカイブされたデータには依然として`user_id`フィールドが含まれており、すべてのイベントデータにわたるユーザーごとの分析が可能です。

対応する`USERS_*_SHARED`ビューで各イベントの直近2年間のデータを照会できます。さらに、各イベントには、匿名化されたデータと非匿名化されたデータの両方を返すためにクエリを実行できる`USERS_*_SHARED_ALL`ビューが用意されています。

#### 歴史的なデータ
Snowflake では、2019年4月までの履歴イベントデータがアーカイブされています。BrazeがSnowflakeにデータを保存し始めた最初の数ヶ月間に、製品の変更が行われ、そのデータの一部がわずかに異なって見えたり、いくつかのフィールドにnull値が含まれている可能性があります（この時点ではすべての利用可能なフィールドにデータを渡していなかったため）。2019年8月以前のデータを含む結果は、予期される結果と多少異なる可能性があると想定しておくことが最適です。

### 一般データ保護規則（GDPR）準拠
Braze に保管されているほぼすべてのイベントレコードには、ユーザーの個人を特定できる情報 (PII) を表すいくつかのフィールドが含まれています。一部のイベントには、メールアドレス、電話番号、デバイスID、言語、性別、および位置情報が含まれる場合があります。ユーザーの削除依頼がBrazeに送信された場合、これらのユーザーに属するイベントのPIIフィールドを無効化します。この方法では、イベントの履歴レコードは削除されませんが、イベントが特定の個人に結び付けられることは一切ありません。

### スピード、パフォーマンス、クエリのコスト
データに対して実行されるクエリの速度、パフォーマンス、およびコストは、データのクエリに使用するウェアハウスのサイズによって決まります。場合によっては、分析のためにアクセスしているデータ量によって、クエリを成功させるためにより大きなウェアハウスサイズを使用する必要があるかもしれません。Snowflakeには、[ウェアハウスの概要](https://docs.snowflake.net/manuals/user-guide/warehouses-overview.html)や[ウェアハウスの考慮事項](https://docs.snowflake.net/manuals/user-guide/warehouses-considerations.html)など、どのサイズを使用するかを最適に判断する方法に関する優れたリソースが用意されています。

## Braze Benchmarks

Benchmarks は [Braze によって構築されたデータツール](https://www.braze.com/perspectives/benchmarks)であり、Braze の見込み客と顧客は Benchmarks を使用して自社の指標を Braze の業界ベンチマークと比較して、業界上位の企業との比較を確認できます。

初期設定の業界には以下のものがあります。
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
