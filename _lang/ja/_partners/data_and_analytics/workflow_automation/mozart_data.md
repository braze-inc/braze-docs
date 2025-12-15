---
nav_title: Mozart Data
article_title: Mozart Data
description: "このリファレンス記事では、Braze と Mozart Data のパートナーシップについて説明します。Mozart Data はオールインワンの最新のデータプラットプラットフォームであり、Fivetran を使用して Snowflake へのデータのインポート、トランスフォームの作成、データの結合などを行うことができます。"
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Data](https://mozartdata.com/) は、Fivetran、Portable、Snowflake を利用するオールインワンの最新データプラットフォームです。

Braze と Mozart Data の統合により、以下のことが可能になります。
- Fivetranを使ってBrazeのデータをSnowflakeにインポートする
- Brazeのデータと他のアプリケーションのデータを組み合わせてトランスフォームを作成し、ユーザーの行動を効果的に分析する。
- SnowflakeからBrazeにデータをインポートし、新たな顧客エンゲージメントの機会を創出する。
- Brazeのデータを他のアプリケーションのデータと組み合わせ、ユーザーの行動をより総合的に理解する。
- ビジネスインテリジェンスツールと統合し、Snowflakeに保存されているデータをさらに詳しく調査する。

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
| Mozart Data アカウント | このパートナーシップを活用するには、Mozart Data アカウントが必要です。[こちらからご登録ください。](https://app.mozartdata.com/signup)|
| Snowflake アカウント<br>オプション 1: 新規アカウント | Mozart Data のアカウント作成プロセスで [**Create a New Snowflake Account**] を選択すると、Mozart Data により新しい Snowflake アカウントがプロビジョニングされます。 |
| Snowflake アカウント<br>オプション 2: 既存口座 | 組織がすでに Snowflake アカウントを所有している場合は、Mozart Data Connected オプションを使用できます。<br><br>既存のSnowflakeアカウントに接続するには、**Already Have a Snowflake Account**オプションを選択する。このオプションを使用する場合は、アカウントレベルの権限を持つユーザーが[以下の手順に従って操作する](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount)必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

この統合は、[Braze から Mozart Data への](#syncing-data-from-braze-to-mozart-data)データ同期と [Mozart Data から Braze への](#syncing-data-from-mozart-data-to-braze)データ同期の両方でサポートされています。

### BrazeからMozart Dataにデータを同期する

#### ステップ1:Braze コネクターを設定する

1. Mozart Data で [**Connectors**] に移動し、[**Add Connector**] をクリックします。
2. 「Braze」を検索し、コネクターカードを選択します。
3. Brazeから同期されたすべてのデータが保存される保存先スキーマ名を入力する。デフォルトのスキーマ名`braze` を使用することを推奨する。
4. [**Add Connector**] をクリックします。

#### ステップ2:Fivetran コネクターフォームに情報を入力します。

Fivetran コネクターページにリダイレクトされます。このページで所定のフィールドに入力します。次に、**Continue**> **Save & Test** をクリックしてFivetran コネクターを完成させます。

Fivetran が、Braze アカウントから Snowflake データウェアハウスへのデータの同期を開始します。コネクターの同期が完了したら、Mozart Data からクエリデータにアクセスできます。 

### Mozart DataからBrazeにデータを同期する

#### ステップ1:Snowflakeデータウェアハウスをセットアップする

「[クラウドデータ取り込み]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake)」の手順に従って、Snowflake インターフェイスからテーブル、ユーザー、権限を設定します。このステップには、管理者レベルのSnowflakeアクセスが必要であることに注意。

#### ステップ2:BrazeでSnowflakeとの統合をセットアップする

Snowflake ウェアハウスの設定後に、Mozart Data の [**Integration**] ページで [**Braze**] を選択します。ここで、Braze に提供する必要がある認証情報を確認します。

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

次に、Braze にサインインした状態で **[統合] > [テクノロジーパートナー] > [Snowflake]** に移動し、統合プロセスを開始します。Mozart Data から認証情報をコピーし、Snowflake Data のインポートページに追加します。[**同期の詳細を設定**] をクリックし、Snowflake アカウントとソーステーブルの情報を入力します。 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

次に、同期の名前を選択し、連絡先のEメールを入力し、データの種類と同期頻度を選択する。 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### ステップ 3:Braze ユーザーへの公開キーの追加
この時点で、Snowflake に戻って設定を完了する必要があります。Brazeのダッシュボードに表示される公開鍵を、BrazeがSnowflakeに接続するために作成したユーザーに追加する。

その方法の詳細については、[Snowflake のドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。任意の時点でのキーのローテーションを行う場合、Mozart Data は新規のキーペアを生成して、新規の公開キーを提供できます。

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### ステップ4:テスト接続

ユーザーが公開キーで更新されたら、Braze ダッシュボードに戻って、[**テスト接続**] をクリックします。成功すると、データのプレビューが表示されます。何らかの理由で接続に失敗した場合、トラブルシューティングに役立つエラーメッセージが表示される。

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
連携を下書き状態からアクティブ状態に移行するには、連携のテストに成功する必要があります。作成ページを閉じる必要がある場合は、連携が保存されるので、詳細ページに再度アクセスして変更やテストを行うことができます。  
{% endalert %}

## この統合を使用する

### Mozart Data のユーザーとして Braze のデータにアクセスする方法
Mozart Data アカウントが作成されたら、Mozart Data から Snowflake データウェアハウスに同期された Braze データにアクセスできます。

#### トランスフォーム
Mozart Dataは、ユーザーがビューやテーブルを作成するためのSQL変換レイヤーを提供している。各ユーザーの製品使用データ、取引履歴、エンゲージメントアクティビティを Braze メッセージとともに要約するユーザーレベルのディメンションテーブル (`dim_users` など) を作成できます。 

#### 分析
Brazeから同期された変換モデルまたは生データを使用して、Brazeメッセージに対するユーザーのエンゲージメントを分析できる。さらに、Braze データを他のアプリケーションのデータと組み合わせて、Braze メッセージに対するユーザーのインタラクションから得たインサイトが、ユーザーに関して所有している他のデータとどのように関連しているかを分析できます。たとえば、顧客のデモグラフィック情報、ショッピング履歴、製品の使用状況、カスタマーサービスエンゲージメントなどです。 

これは、ユーザーのリテンションを向上させるためのエンゲージメント戦略について、より多くの情報に基づいた決定を下すのに役立つ。これはすべて、クエリーツールを使ってMozart Dataのインターフェイス内で行うことができ、結果をGoogleシートやCSVにエクスポートしてプレゼンテーションに備えることができる。

#### ビジネスインテリジェンス（BI）
自分の洞察を可視化し、他のチームメンバーと共有する準備はできているか？Mozart Data は、ほぼすべての BI ツールと統合されています。BI ツールをまだお持ちでない場合は、Mozart Data に連絡して無料のMetabase アカウントをセットアップしてください。