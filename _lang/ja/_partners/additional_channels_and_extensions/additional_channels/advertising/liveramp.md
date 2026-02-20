---
nav_title: LiveRamp
article_title: LiveRamp
description: "LiveRamp、Snowflake、および Braze を接続する方法について説明します。この方法を理解することで、高度にパーソナライズされた関連性のあるマーケティングキャンペーンを作成できます。"
alias: /partners/liveramp/
page_type: partner
search_tag: Partner
---

# LiveRamp、Snowflake、Brazeを接続する

> LiveRamp、Snowflake、Brazeを接続する方法を学ぶことで、洞察までの時間を短縮し、データのサイロ化を解消し、顧客エンゲージメントを最適化することで、高度にパーソナライズされた関連性の高いマーケティングキャンペーンを作成できる。この統合により、実用的な個人ベースのインサイトが提供され、消費者のタッチポイントが集約され、より適切なオーディエンスセグメンテーションとタイムリーなキャンペーンが可能になり、データドリブン型のマーケティングが強化されます。また、Snowflakeが提供するベンチマークを活用し、業界標準に照らし合わせてマーケティング戦略を洗練させることができる。

{% alert important %}
Snowflake の[セキュアデータシェアリング](https://docs.snowflake.com/en/user-guide/data-sharing-intro)では、LiveRamp、Snowflake、および Braze 間でデータが転送されません。データは、Snowflake のサービスおよびメタデータストアでのみ共有されます。つまり、データはコピーされず、追加のストレージ料金は発生しません。共有データへのアクセスは、Snowflake アカウントのアクセスコントロールを使用して制御および管理されます。
{% endalert %}

## ユースケース

- **データの最小化::**LiveRamp のアクティベーションアプリでは、Snowflake のセキュアデータシェア機能を使用して、インスタンスから直接テーブルを効率的に読み取ります。ダウンストリームパートナーに配信する時点までは、Snowflake からデータは移動されません。
- **安全なファーストパーティのアクティベーション:**前述の ID 解決アプリケーションを使用することで、LiveRamp のアクティベーションアプリケーションはSnowflake インスタンスの RampID ベースのテーブルのみを使用します。このため、PII が外部へ流出することがありません。
- **有効期間の促進:**お客様の環境でデータを直接 RampID に解決することで、最終宛先への配信が数時間内に行われます。これに対し、LiveRamp の従来のファイルベースの方法では、このような配信が行われるまでに数日間かかっていました。これにより、キャンペーンのパフォーマンスをタイムリーに最適化できる能力が大幅に向上します。
- **運用コストの節約:**上記と同様に、ファイルの LiveRamp への出力またはその他の最終宛先への直接出力を調整することに比べ、Snowflake のセキュアデータシェアリング機能を使用することでお客様の時間と費用を節約できます。

## 前提条件

| 前提条件       | 説明                                                                                                                                                                                     |
|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Snowflake アカウント | 管理者レベルの権限を持つSnowflakeアカウントが必要だ。                                                                                                                                      |
| LiveRamp アカウント  | Snowflake内で必要なLiveRampアプリケーションについては、LiveRampアカウントチームまたは[snowflake@liveramp.com](mailto:snowflake@liveramp.com)までお問い合わせください。                              |
{: .reset-td-br-1 .reset-td-br-2 }

## 統合をセットアップする

### ステップ1:Braze からのデータ共有を依頼する

まず、Brazeアカウントマネージャーまたはカスタマーサクセスマネージャーに連絡して、Brazeアカウント用のSnowflake Data Share Connectorを購入する。データ共有を依頼すると、Braze は共有が購入されたワークスペースから共有をプロビジョニングします。共有がプロビジョニングされると、すべてのデータは Snowflake インスタンス内から受信データ共有の形式ですぐにアクセス可能になります。共有がインスタンスに表示されたら、共有からデータベースを作成し、テーブルを見たり問い合わせたりできるようにする。

完全なウォークスルーについては、[Braze と Snowflake の統合ガイド]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/)を参照してください。

### ステップ2:SnowflakeでLiveRampアプリをセットアップする 

翻訳機能と ID 解決機能は、Snowflake 内で LiveRamp Identity Resolution and Translation ネイティブアプリを通じて利用可能です。このアプリにより、アカウントに共有が作成され、ご利用の Snowflake 環境から参照データセットをクエリするためのビューが開かれます。

このネイティブアプリを設定するには、LiveRamp のドキュメント[Snowflake での LiveRamp ネイティブアプリの設定](https://docs.liveramp.com/identity/en/set-up-the-liveramp-native-app-in-snowflake.html)に記載されている手順に従います。終わったら、次のステップに進む。

### ステップ3:データテーブルを作成する

{% alert warning %}
PII ベースのテーブルを準備する前に、ジョブで実行される [LiveRamp のプライバシーフィルター](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html)を理解し、入力テーブルの属性列 (識別子以外) に非常に独特な値が含まれていないことを確認してください。これは、消費者のプライバシーを維持し、再識別を避けるために重要である。
{% endalert %}

次に、LiveRamp ネイティブアプリに対して呼び出されるデータテーブルを[必要な形式t](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html)で作成します。以下のカテゴリーを参照し、どの識別子が解決の対象となるかを判断する：

| 識別子の種類 | 説明  |
|-----------------|--------------|
| 完全な PII        | 個人を特定できる情報（PII）には、ユーザーの氏名、住所、電子メール、電話番号などが含まれる。**注:**すべての識別子がすべての記録に必要なわけではない。 |
| Eメールのみ      | ユーザーのメールアドレス (`alex-lee@email.com` など)。 |
| デバイス          | これには、サードパーティのクッキー、モバイル広告ID（MAID）、コネクテッドTV ID（CTV ID）、およびRampID（Household RampIDに解決される）が含まれる。 |
| CID            | これらは、プラットフォームパートナーまたは LiveRamp との ID 同期からの識別子です (内部顧客 ID など)。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### ブレイズ識別子

Brazeのイベントログには、LiveRampネイティブアプリ内で使用できる識別子が含まれている。各イベントタイプで使用可能な識別子の完全なリストについては、[Braze イベントのスキーマと識別子]({{site.baseurl}}/assets/download_file/data-sharing-raw-table-schemas.txt)をダウンロードしてください。

| 識別子の種類 | 説明  |
|-----------------|--------------|
| `AD_ID` | `ios_idfa`、`google_ad_id`、`roku_ad_id` などの広告 ID は、特定のイベントタイプ内でキャプチャされ、LiveRamp のデバイス解決サービスと組み合わせて使用できます。デフォルトでは広告 ID は収集されませんが、[Braze のドキュメント]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/#data-not-collected-by-default)に従って追跡を有効にできます。 |
| `EMAIL_ADDRESS`   | LiveRamp のメール専用解決サービスと併用できるメールアドレス |
| `TO_PHONE_NUMBER` | LiveRamp の ＰＩＩ 解決サービスと併用できる電話番号 |
| `EXTERNAL_USER_ID` | ユーザーに関連付けられた external ID。この ID は LiveRamp の Device Resolution サービスと併用できます (CID)。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
LiveRamp のアプリケーション内でクライアントまたはブランド固有のカスタム識別子を使用するには、[LiveRamp との ID 同期](https://docs.liveramp.com/identity/en/getting-started-with-liveramp-identity.html)が必要です。
{% endalert %}

### ステップ4:変数を設定する

次に、アプリに用意されている Execution Step ワークシートでジョブの変数を設定します。これには、ターゲット・データベース、関連テーブル（入力データ、メトリクス、ロギング）、出力テーブル名の定義などの詳細が含まれる。完全なウォークスルーは、[LiveRampを参照のこと：変数 ](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#specify-the-variables-43-150727) を指定します。

### ステップ 5: PII解決のためのメタデータテーブルを作成する

変数が設定できたので、PII解決のためのメタデータテーブルを作成する。これは、関係する識別子のカテゴリーに基づいて実行される特定のジョブタイプの詳細を示す。完全なウォークスルーは、[LiveRampを参照のこと：メタデータテーブル ](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#create-the-metadata-table-43) を作成します。

### ステップ 6: ID解決操作を実行する

最後に、ID解決操作を実行する。完全なウォークスルーは、[LiveRampを参照のこと：ID 解決操作を実行します](https://docs.liveramp.com/identity/en/perform-identity-resolution-in-snowflake.html#perform-the-identity-resolution-operation)。

{% tabs local %}
{% tab example input %}
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

{% tab example output %}
```sql
call check_for_output(
$output_table_name
);
```
{% endtab %}
{% endtabs %}

### 次のステップ

データが RampID の専用エンコードに仮名化されたので、RampID ベースのテーブルを LiveRamp のマネージドアクティベーションアプリケーションと共有して、主要な広告プラットフォームパートナーに対して効率的なフルフィルメントを実現することができます。アクティベーションアプリケーションには、追加のセグメンテーションと、ダウンストリーム宛先パートナーを選択/設定するための、ビジネスユーザーにとって使いやすいインターフェイスが含まれています。アプリケーションの詳細については、LiveRampのアカウントチームまたは[Snowflake@liveramp.com](mailto:snowflake@liveramp.com) に問い合わせること。

## トラブルシューティング

{% alert note %}
より具体的な問題や質問がある場合は、[マーテク@liveramp.com](mailto:martech@liveramp.com) まで連絡を。
{% endalert %}

### Snowflake のリージョン

現在、このアプリケーションは次の米国のリージョンでのみ使用できます。

  - aws-us-east-1：POA18931
  - aws-us-west-2：FAA28932
  - azure-east-us-2：BL60425

### プライバシー& 列の値

このプロセスでは、一意な値があるかどうか、行ごとにすべての列値の組み合わせを評価する。特定のカラム値の組み合わせが3回以下しか出現しない場合、それらのカラム値を含む行はマッチせず、出力テーブルには返されない。同様に、プライバシーを確保するために、LiveRamp サービスは列値の組み合わせの一意性を評価します。これにより、稀な組み合わせが原因でファイルの行の5 % 以上が照合不可能になった場合にはジョブが失敗するようになります。

### 過去のデータ

Snowflakeの過去データは2019年4月まで遡るが、2019年8月以前のデータには製品変更により若干の差異が生じる可能性がある。

### スピード、パフォーマンス、コスト

クエリの速度とコストは、使用するウェアハウスのサイズによって異なります。ウェアハウスのサイズを選択するときには、データアクセスの必要性を考慮してください。

### Braze Benchmarks

ベンチマークでは、Snowflake Data Exchangeで直接利用できる業界標準と自社の指標を比較することができる。

### 破壊的変更と非破壊的変更

統合に影響を及ぼす可能性のある変化に注意すること。破壊的な変更の前に発表と移行期間を設けます。
