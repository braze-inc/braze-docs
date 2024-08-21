---
nav_title: モーツァルト・データ
article_title: モーツァルト・データ
description: "この参考記事では、Brazeとオールインワンのモダン・データ・プラットフォームであるMozart Dataの提携について概説しており、Fivetranを使用してSnowflakeへのデータのインポート、トランスフォームの作成、データの結合などを行うことができる。"
alias: /partners/mozartdata/
page_type: partner
search_tag: Partner

---

# モーツァルト・データ

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> [Mozart Dataは](https://mozartdata.com/)、Fivetran、Portable、Snowflakeを搭載したオールインワンの最新データ・プラットフォームである。

BrazeとMozart Dataの統合により、以下のことが可能になる：
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
| モーツァルト・データ・アカウント | このパートナーシップを利用するには、モーツァルト・データのアカウントが必要である。[登録はこちらから。](https://app.mozartdata.com/signup)|
| Snowflake アカウント<br>オプション 1: 新規アカウント | Mozart Dataのアカウント作成プロセスで**Create a New Snowflake Accountを**選択すると、Mozart Dataがお客様のために新しいSnowflakeアカウントをプロビジョニングする。 |
| Snowflake アカウント<br>オプション 2: 既存口座 | 組織がすでにSnowflakeアカウントを持っている場合は、Mozart Data Connectedオプションを使うことができる。<br><br>既存の**Snowflake**アカウントに接続するには、**Already Have a Snowflake Account**オプションを選択する。このオプションを実行するには、アカウントレベルの権限を持つユーザーが[以下のステップに従わなければ](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount)ならない。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

この統合は、[BrazeからMozart Dataへの](#syncing-data-from-braze-to-mozart-data)データ同期と、[Mozart DataからBrazeへの](#syncing-data-from-mozart-data-to-braze)データ同期の両方でサポートされている。

### BrazeからMozart Dataにデータを同期する

#### ステップ1:ブレイズコネクターをセットアップする

1. Mozart Dataで、**Connectorsに**進み、**Add Connectorを**クリックする。
2. Braze」を検索し、コネクターカードを選択する。
3. Brazeから同期されたすべてのデータが保存される保存先スキーマ名を入力する。デフォルトのスキーマ名`braze` を使用することを推奨する。
4. **Add Connectorを**クリックする。

#### ステップ2:Fivetranコネクタフォームに記入する

Fivetranコネクタのページにリダイレクトされる。このページで、所定の欄に記入する。次に、**Continue**>**Save & Testを**クリックし、Fivetranコネクタを完成させる。

Fivetranは、BrazeアカウントからSnowflakeデータウェアハウスへのデータの同期を開始する。コネクタの同期が完了した後、Mozart Dataからクエリデータにアクセスできる。 

### Mozart DataからBrazeにデータを同期する

#### ステップ1:Snowflakeデータウェアハウスをセットアップする

[Cloud Data Ingestionの]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake)手順に従って、Snowflakeインターフェースからテーブル、ユーザー、権限を設定する。このステップには、管理者レベルのSnowflakeアクセスが必要であることに注意。

#### ステップ2:BrazeでSnowflakeとの統合をセットアップする

Snowflake warehouseを設定した後、Mozart Dataで**Integration**ページに行き、**Brazeを**選択する。ここで、Brazeに提供するために必要なクレデンシャルを見つける。

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

次に、Brazeにサインインした状態で、**Integrations > Technology Partners > Snowflakeと**進み、統合プロセスを開始する。Mozart Dataから認証情報をコピーし、Snowflake Dataのインポートページに追加する。**Set up sync detailsを**クリックし、Snowflakeアカウントとソーステーブル情報を入力する。 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

次に、同期の名前を選択し、連絡先のEメールを入力し、データの種類と同期頻度を選択する。 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### ステップ 3:Braze ユーザーへの公開キーの追加
この時点で、Snowflakeに戻ってセットアップを完了する必要がある。Brazeのダッシュボードに表示される公開鍵を、BrazeがSnowflakeに接続するために作成したユーザーに追加する。

その方法の詳細については、[Snowflake のドキュメント](https://docs.snowflake.com/en/user-guide/key-pair-auth.html)を参照してください。鍵のローテーションを行いたい場合は、Mozart Dataが新しい鍵ペアを生成し、新しい公開鍵を提供する。

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### ステップ 4:テスト接続

ユーザーが公開鍵で更新されたら、Brazeダッシュボードに戻り、**Test connectionを**クリックする。成功すると、データのプレビューが表示されます。何らかの理由で接続に失敗した場合、トラブルシューティングに役立つエラーメッセージが表示される。

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
連携を下書き状態からアクティブ状態に移行するには、連携のテストに成功する必要があります。作成ページを閉じる必要がある場合は、連携が保存されるので、詳細ページに再度アクセスして変更やテストを行うことができます。  
{% endalert %}

## この統合を使う

### Mozart DataのユーザーとしてBrazeのデータにアクセスする方法
Mozart Dataアカウントの作成に成功すると、Mozart DataからSnowflakeデータウェアハウスに同期されたBrazeデータにアクセスできるようになる。

#### トランスフォーム
Mozart Dataは、ユーザーがビューやテーブルを作成するためのSQL変換レイヤーを提供している。ユーザーレベルのディメンションテーブル（たとえば、`dim_users` ）を作成し、各ユーザーの製品使用データ、取引履歴、Brazeメッセージとのエンゲージメント活動を要約することができる。 

#### 分析
Brazeから同期された変換モデルまたは生データを使用して、Brazeメッセージに対するユーザーのエンゲージメントを分析できる。さらに、Brazeのデータを他のアプリケーションのデータと組み合わせて、ユーザーとBrazeのメッセージとのやり取りから得た洞察が、ユーザーについて持っている他のデータとどのように関連しているかを分析することもできる。例えば、デモグラフィック情報、ショッピング履歴、製品の使用状況、カスタマーサービスへの関与などである。 

これは、ユーザーのリテンションを向上させるためのエンゲージメント戦略について、より多くの情報に基づいた決定を下すのに役立つ。これはすべて、クエリーツールを使ってMozart Dataのインターフェイス内で行うことができ、結果をGoogleシートやCSVにエクスポートしてプレゼンテーションに備えることができる。

#### ビジネスインテリジェンス（BI）
自分の洞察を可視化し、他のチームメンバーと共有する準備はできているか？Mozart Dataは、ほとんどすべてのBIツールと統合できる。BIツールをまだ持っていない場合は、Mozart Dataに連絡して無料のMetabaseアカウントをセットアップしてほしい。 