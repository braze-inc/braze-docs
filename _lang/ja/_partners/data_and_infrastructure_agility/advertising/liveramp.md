---
nav_title: ライブランプ
article_title: ライブランプ
description: "LiveRamp、Snowflake、Brazeの接続方法を学ぶことで、高度にパーソナライズされた関連性の高いマーケティングキャンペーンを作成できる。"
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# LiveRamp、Snowflake、Brazeを接続する

> LiveRamp、Snowflake、Brazeを接続する方法を学ぶことで、洞察までの時間を短縮し、データのサイロ化を解消し、顧客エンゲージメントを最適化することで、高度にパーソナライズされた関連性の高いマーケティングキャンペーンを作成できる。この統合は、実用的な個人ベースのインサイトを提供し、より良いオーディエンスのセグメンテーションとタイムリーなキャンペーンのために消費者とのタッチポイントを統合することにより、データ駆動型マーケティングを強化する。また、Snowflakeが提供するベンチマークを活用し、業界標準に照らし合わせてマーケティング戦略を洗練させることができる。

{% alert important %}
Snowflakeの[Secure Data Sharesは](https://docs.snowflake.com/en/user-guide/data-sharing-intro)、LiveRamp、Snowflake、Braze間でデータを転送しない。データはスノーフレークのサービスとメタデータストアを通じてのみ共有されるため、データはコピーされず、追加のストレージ料金も発生しない。共有データへのアクセスは、Snowflakeアカウントのアクセス制御を使用して制御・管理される。
{% endalert %}

## ユースケース

- **データの最小化：**LiveRampのActivationアプリは、SnowflakeのSecure Data Share機能を使って、インスタンスから直接テーブルを効率的に読み取る。Snowflakeから下流のパートナーにデータを提供するまで、データは移動しない。
- **安全な1st Party Activation：**上記のIdentity Resolutionアプリケーションを使用することで、LiveRampのActivationアプリケーションは、Snowflakeインスタンス内のRampIDベースのテーブルのみを使用するため、PIIが壁を離れることはない。
- **生きる時間を早める：**お客様の環境で直接RampIDにデータを解決することにより、LiveRampのより伝統的なファイルベースのアプローチを使用する場合の数日と比較して、エンドデスティネーションへの配信は数時間以内に行うことができる。これにより、キャンペーンのパフォーマンスをタイムリーに最適化する能力が大幅に向上する。
- **経営上の節約：**上記と同様に、スノーフレークのセキュアなデータ共有機能を使用することで、LiveRampや最終目的地への直接のファイル送信を調整する場合と比較して、顧客は時間とコストを節約することができる。

## 前提条件

| 前提条件       | 説明                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Snowflake アカウント | 管理者レベルの権限を持つSnowflakeアカウントが必要だ。                                                                                                                                      |
| ライブランプ・アカウント  | Snowflake内で必要なLiveRampアプリケーションについては、LiveRampアカウント・チームまたは[snowflake@liveramp.com](mailto:snowflake@liveramp.com)まで連絡を。                              |
{: .reset-td-br-1 .reset-td-br-2 }

## 統合をセットアップする

### ステップ 1:ブレイズにデータ共有を依頼する

まず、Brazeアカウントマネージャーまたはカスタマーサクセスマネージャーに連絡して、Brazeアカウント用のSnowflake Data Share Connectorを購入する。データ共有をリクエストすると、Brazeは、共有が購入されたワークスペースから共有をプロビジョニングする。共有がプロビジョニングされると、すべてのデータは受信データ共有の形でSnowflakeインスタンス内からすぐにアクセスできるようになる。共有がインスタンスに表示されたら、共有からデータベースを作成し、テーブルを見たり問い合わせたりできるようにする。

完全なウォークスルーは、[BrazeとのSnowflake統合ガイドを]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)参照のこと。

### ステップ2:SnowflakeでLiveRampアプリをセットアップする 

翻訳とID解決の機能は、LiveRamp Identity Resolution and Translationネイティブアプリを通してSnowflake内で利用できる。

ネイティブアプリをセットアップするには、LiveRampのドキュメントにある以下のステップに従う：[SnowflakeでLiveRampネイティブアプリをセットアップ](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html)する。終わったら、次のステップに進む。

### ステップ 3:データテーブルを作成する

{% alert warning %}
PIIベースのテーブルを準備する前に、ジョブ中に実行される[LiveRampのプライバシーフィルターを](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html)理解し、入力テーブルの属性カラム（非識別子）にユニークすぎる値が含まれていないことを確認する。これは、消費者のプライバシーを維持し、再識別を避けるために重要である。
{% endalert %}

次に、LiveRampネイティブアプリに対して呼び出される、[必要なフォーマットの](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html)データテーブルを作成する。以下のカテゴリーを参照し、どの識別子が解決の対象となるかを判断する：

| 識別子の種類 | 説明  |
|-----------------|--------------|
| 完全なPII        | 個人を特定できる情報（PII）には、ユーザーの氏名、住所、電子メール、電話番号などが含まれる。**注:**すべての識別子がすべての記録に必要なわけではない。 |
| Eメールのみ      | `alex-lee@email.com` のようなユーザーのメールアドレス。 |
| デバイス          | これには、サードパーティのクッキー、モバイル広告ID（MAID）、コネクテッドTV ID（CTV ID）、およびRampID（Household RampIDに解決される）が含まれる。 |
| CIDについて            | これらは、プラットフォーム・パートナーからの識別子、またはLiveRampと同期したIDであり、社内の顧客IDなどである。 |
{: .reset-td-br-1 .reset-td-br-2}

#### ブレイズ識別子

Brazeのイベントログには、LiveRampネイティブアプリ内で使用できる識別子が含まれている。各イベントタイプで使用可能な識別子の全リストは、[Braze Event Schemas and Identifiersを](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt)ダウンロードする。

| 識別子の種類 | 説明  |
|-----------------|--------------|
| `AD_ID` | `ios_idfa`,`google_ad_id`,`roku_ad_id` のような広告IDは、特定のイベントタイプ内でキャプチャされ、LiveRampのDevice Resolutionサービスと組み合わせて使用することができる。デフォルトでは、Advertising IDは収集されないが、[Brazeのドキュメントに従って](https://www.braze.com/docs/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default)トラッキングを有効にすることができる。 |
| `EMAIL_ADDRESS`   | LiveRampのEメールのみによる解決サービスと併用できるEメールアドレス |
| `TO_PHONE_NUMBER` | 電話番号は、LiveRampのPII Resolutionサービスと組み合わせて使用することができる。 |
| `EXTERNAL_USER_ID` | ユーザーに関連付けられた外部IDで、LiveRampのDevice Resolutionサービス（CID）と組み合わせて使用できる。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
LiveRampのアプリケーション内でクライアントまたはブランド固有のカスタム識別子を使用するには、[LiveRampとのID同期が](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html)必要である。
{% endalert %}

### ステップ 4:変数を設定する

次に、アプリで提供される実行ステップのワークシートで、ジョブの変数を設定する。これには、ターゲット・データベース、関連テーブル（入力データ、メトリクス、ロギング）、出力テーブル名の定義などの詳細が含まれる。完全なウォークスルーは、[LiveRampを参照のこと：](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727) 変数を指定する。

### ステップ 5: PII解決のためのメタデータテーブルを作成する

変数が設定できたので、PII解決のためのメタデータテーブルを作成する。これは、関係する識別子のカテゴリーに基づいて実行される特定のジョブタイプの詳細を示す。完全なウォークスルーは、[LiveRampを参照のこと：メタデータ・テーブルの作成](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43).

### ステップ 6: ID解決操作を実行する

最後に、ID解決操作を実行する。完全なウォークスルーは、[LiveRampを参照のこと：アイデンティティ解決操作を実行する](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation).

{% tabs ローカル %}
{% tab 入力例 %}
```sql
call lr_resolution_and_transcoding(
$customer_input_table_name,
$customer_meta_table_name,
$output_table_name,
$customer_logging_table_name,
$customer_metrics_table_name
);
```
{% endtab %}

{% tab 出力例 %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### 次のステップ

データがRampIDの専用エンコーディングに仮名化されたことで、RampIDベースのテーブルをライブランプのマネージド・アクティベーション・アプリケーションと共有することができ、主要な広告プラットフォーム・パートナーへの合理的なフルフィルメントが可能になる。アクティベーション・アプリケーションには、セグメンテーションを追加したり、下流のデスティネーション・パートナーを選択／設定するための、ビジネス・ユーザー・フレンドリーなインターフェイスが含まれている。アプリケーションの詳細については、LiveRampのアカウントチームまたは[snowflake@liveramp.com](mailto:snowflake@liveramp.com) までお問い合わせいただきたい。

## トラブルシューティング

{% alert note %}
より具体的な問題や質問がある場合は、[martech@liveramp.com](mailto:martech@liveramp.com) まで連絡を。
{% endalert %}

### 雪片地域

現在、このアプリケーションは、米国を拠点とする以下の地域でのみ利用できる：

  - aws-us-east-1：POA18931
  - aws-us-west-2：FAA28932
  - azure-east-us-2：BL60425

### プライバシーとコラムの価値

このプロセスでは、一意な値があるかどうか、行ごとにすべての列値の組み合わせを評価する。特定のカラム値の組み合わせが3回以下しか出現しない場合、それらのカラム値を含む行はマッチせず、出力テーブルには返されない。同様に、プライバシーを確保するために、LiveRampサービスはカラム値の組み合わせの一意性を評価し、ファイルの行の5％以上がまれな組み合わせのためにマッチ不可能になった場合、ジョブは失敗する。

### 過去のデータ

Snowflakeの過去データは2019年4月まで遡るが、2019年8月以前のデータには製品変更により若干の差異が生じる可能性がある。

### スピード、パフォーマンス、コスト

クエリーのスピードとコストは、使用する倉庫のサイズに依存する。ウェアハウスのサイズを選択する際には、データアクセスのニーズを考慮すること。

### Braze Benchmarks

ベンチマークでは、Snowflake Data Exchangeで直接利用できる業界標準と自社の指標を比較することができる。

### ブレーク対ブレークブレークしない変更

統合に影響を及ぼす可能性のある変化に注意すること。画期的な変更には、アナウンスと移行期間が設けられる。
