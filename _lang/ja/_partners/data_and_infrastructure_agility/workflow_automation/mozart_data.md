---
nav_title: Mozart Data
article_title:モーツァルトデータ
description:「この参考記事では、オールインワンの最新データプラットフォームであるBrazeとMozart Dataとのパートナーシップの概要を説明しています。これにより、Fivetran を使用してSnowflakeへのデータのインポート、変換の作成、データの結合などが可能になります。「
alias: /partners/mozartdata/
page_type: partner
search_tag:Partner

---

# モーツァルトデータ

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Dataは](https://mozartdata.com/)、Fivetran、Portable、Snowflakeを搭載したオールインワンのモダンデータプラットフォームです。

Braze と Mozart のデータ統合により、次のことが可能になります。
- Fivetran を使用して Braze データをSnowflake にインポートします
- Braze データを他のアプリケーションデータと組み合わせてトランスフォームを作成し、ユーザー行動を効果的に分析します
- SnowflakeからBrazeにデータをインポートして、新しいカスタマーエンゲージメント機会を創出します
- Brazeのデータを他のアプリケーションデータと組み合わせて、ユーザー行動をより包括的に理解しましょう
- ビジネスインテリジェンスツールと統合して、Snowflakeに保存されているデータをさらに詳しく調べる

## 前提条件

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| 必要条件 | 説明 |
| ----------- | ----------- |
| モーツァルトデータアカウント | このパートナーシップを利用するには、Mozart Dataアカウントが必要です。[こちらからサインアップしてください。](https://app.mozartdata.com/signup)|
| Snowflake アカウント<br>オプション 1: 新規口座 | Mozart DataのMozart **Dataアカウント作成プロセス中に \[新しいSnowflakeアカウントを作成**] を選択して、新しいSnowflakeアカウントをプロビジョニングしてください。 |
| Snowflake アカウント<br>オプション 2: 既存のアカウント | 組織にすでにSnowflakeアカウントがある場合は、Mozart データ接続オプションを使用できます。<br><br>既存のSnowflakeアカウントを接続するには**、「すでにSnowflakeアカウントを持っています**」オプションを選択してください。このオプションを利用するには、アカウントレベルの権限を持つユーザー[次の手順に従う必要があります](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount)。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

この統合は、BrazeからMozart [[Dataへのデータ同期とMozartデータからBrazeへのデータの同期の両方でサポートされています](#syncing-data-from-mozart-data-to-braze)](#syncing-data-from-braze-to-mozart-data)。

### Braze からモーツァルトデータへのデータの同期

#### ステップ1:Braze コネクタのセットアップ

1. Mozart Data で、\[コネクター] に移動し、\[****コネクターを追加****] をクリックします。
2. 「Braze」を検索し、コネクタカードを選択します。
3. Braze から同期されたすべてのデータが保存される送信先スキーマ名を入力します。デフォルトのスキーマ名を使用することをお勧めします`braze`。
4. \[**コネクタを追加**] をクリックします。

#### ステップ2:Fivetran コネクターフォームに必要事項を記入してください

Fivetran コネクタのページにリダイレクトされます。このページで、指定のフィールドに入力します。次に、\[**続行**] > \[**保存してテスト**] をクリックして Fivetran コネクタを完成させます。

Fivetran、BrazeアカウントからSnowflakeデータウェアハウスへのデータの同期を開始します。コネクタの同期が終了すると、Mozart Data からクエリデータにアクセスできます。 

### モーツァルトデータから Braze へのデータの同期

#### ステップ1:Snowflakeデータウェアハウススをセットアップする

[クラウドデータ取り込みの手順に従って]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake)、Snowflakeインターフェイスからテーブル、ユーザー、権限を設定します。このステップには管理者レベルのSnowflakeアクセスが必要であることに注意してください。

#### ステップ2:Braze でSnowflake インテグレーションをセットアップする

**Snowflakeウェアハウスを設定したら、Mozart **Dataでインテグレーションページに移動し**、Brazeを選択します。**ここには、Braze の提供に必要な認証情報が記載されています。

![] ({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

次に、Braze にサインインした状態で、\[**統合] > \[テクノロジーパートナー] > \[Snowflake]** に移動して統合プロセスを開始します。Mozart Data から認証情報をコピーして、Snowflake データインポートページに追加します。\[**同期の詳細を設定**] をクリックし、Snowflakeアカウントとソーステーブル情報を入力します。 

![] ({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

次に、同期の名前を選択し、連絡先メールアドレスを入力し、データタイプと同期頻度を選択します。 

![] ({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### ステップ3:Braze ユーザーへの公開キーの追加
この時点で、Snowflakeに戻ってセットアップを完了する必要があります。Brazeダッシュボードに表示されている公開キーを、BrazeがSnowflakeに接続するために作成したユーザーに追加します。

その方法の詳細については、[Snowflake のドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。任意の時点でキーをローテーションしたい場合、Mozart Data は新しいキーペアを生成し、新しい公開キーを提供します。

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### ステップ 4:テスト接続

ユーザー公開キーで更新されたら、Braze ダッシュボードに戻り、\[**接続をテスト**] をクリックします。成功すると、データのプレビューが表示されます。何らかの理由で接続に失敗した場合、問題のトラブルシューティングに役立つエラーが表示されます。

![] ({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
連携を下書き状態からアクティブ状態に移行するには、連携のテストに成功する必要があります。作成ページを閉じる必要がある場合は、連携が保存されるので、詳細ページに再度アクセスして変更やテストを行うことができます。  
{% endalert %}

## このインテグレーションを使用する

### モーツァルトデータユーザーとしてBrazeデータにアクセスする方法
Mozart Dataアカウントが正常に作成されると、モーツァルトデータからSnowflakeデータウェアハウスに同期されたBrazeデータにアクセスできます。

#### トランスフォーム
Mozart Data には、ユーザーがビューやテーブルを作成できる SQL 変換レイヤーが用意されています。ユーザーレベルのディメンションテーブル（たとえば`dim_users`）を作成して、各ユーザーの製品使用データ、取引履歴、エンゲージメントアクティビティをBrazeメッセージで要約できます。 

#### 分析
Brazeから同期されたトランスフォームモデルまたは生データを使用して、' engagement with Braze messages. Additionally, you can combine the Braze data with other application data and analyze how the insights you gained from users'ユーザーに関する他のデータに関連するBrazeメッセージに対するユーザーのやり取りを分析できます。たとえば、人口統計情報、ショッピング履歴、製品使用状況、顧客サービスエンゲージメントなどです。 

これにより、エンゲージメント戦略についてより多くの情報に基づいた意思決定を行い、ユーザーリテンションを向上させることができます。これはすべて Mozart Data のインターフェイス内でクエリツールを使用して実行できます。クエリツールでは、結果を Google Sheets または CSV にエクスポートしてプレゼンテーションの準備を行うことができます。

#### ビジネスインテリジェンス (BI)
インサイトを視覚化して他のチームメンバーと共有する準備はできていますか？Mozart データはほとんどすべての BI ツールと統合されています。BIツールをまだお持ちでない場合は、Mozart Dataに連絡して無料のMetabaseアカウントを設定してください。 