---
nav_title: よくある質問
article_title: クラウドデータ取り込みに関する FAQ
page_order: 100
page_type: FAQ
description: "このページには、クラウドデータ取り込みに関してよくある質問と、その回答を記載しています。"
toc_headers: h2
---

# よくある質問

> このページでは、クラウドデータ取り込みに関してよくある質問と、その回答を記載しています。

## 「Row errors in your CDI sync」(CDI 同期の行エラー) というメールが届いた理由は何ですか?

この種のメールは通常、CDIの設定に問題があることを意味する。ここでは、よくある問題とその解決方法を紹介する：

### CDI がお客様の認証情報を使用してデータウェアハウスやテーブルにアクセスできない

CDI の認証情報が正しくないか、データウェアハウスの設定が正しくない可能性があります。詳細については、[データウェアハウスの連携]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/)を参照してください。

### テーブルが見つからない

正しいデータベース構成を使用して連携を更新するか、データウェアハウスに `database/table` などの一致するリソースを作成してください。

### カタログが見つからない

統合で設定されたカタログは、Braze カタログには存在しません。カタログは、連携の設定後に削除できます。この問題を解決するには、別のカタログを使用するように統合を更新するか、統合のカタログ名と一致する新しいカタログを作成する。

## 「Row errors in your CDI sync」(CDI 同期の行エラー) というメールが届いた理由は何ですか?

この種のメールは、同期中にデータの一部が処理できなかったことを意味する。具体的なエラーを調べるために、Braze の [**CDI**] > [**同期ログ**] でログを確認できます。

## テスト接続とサポート・メールのエラーを修正するには？

{% tabs %}
{% tab Snowflake %}
### テスト接続が遅い

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことでスピードが向上する可能性があります。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。

### Snowflakeインスタンスへの接続エラー：IP を含む着信リクエストが Snowflake へのアクセスを許可されていない

IP許可リストにBrazeの公式IPを追加してみる。詳細については、[Data Warehouse Integrations]({{site.baseurl}}/user_guide/data/cloud_ingestion/integrations/)を参照するか、関連するIP を許可してください。

{% multi_lang_include data_centers.md datacenters='ips' %}

### 顧客設定による SQL 実行エラー: 002003 (42S02):SQLコンパイルエラー：存在しないか、認証されていない

テーブルが存在しない場合は、テーブルを作成します。テーブルが存在する場合は、ユーザとロールにテーブルからの読み取り権限があることを確認する。

### スキーマを使用できなかった

このエラーが発生した場合は、指定されたユーザーまたはロールにそのスキーマへのアクセスを許可する。

### ロールを使用できなかった

このエラーが表示された場合は、そのユーザーに指定されたロールの使用を許可する。

### ユーザーアクセスを無効にする

このエラーが表示された場合は、そのユーザーにSnowflakeアカウントへのアクセスを許可する。

### 現在のキーと古いキーでSnowflakeインスタンスに接続する際のエラー

このエラーが発生した場合は、ユーザがBraze ダッシュボードに表示されている現在の公開キーを使用していることを確認します。
{% endtab %}

{% tab Redshift %}
### テスト接続が遅い

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことでスピードが向上する可能性があります。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。

### 関係 {table_name} の権限が拒否された

このエラーが表示された場合

  - そのユーザのスキーマに`usage` 権限を与える。
  - そのユーザーに、そのテーブルの `select` 権限を付与します。

### 接続作成エラー

このエラーが表示された場合は、Redshift のエンドポイントとポートが正しいことを確認します。

### SSHトンネル作成エラー

このエラーが表示された場合

  - brazeダッシュボードの公開鍵が、SSHトンネリングに使用するec2ホスト上にあることを確認する。
  - ユーザー名が正しいことを確認する。
  - SSHトンネルが正しいことを確認する。
{% endtab %}

{% tab BigQuery %}
### テスト接続が遅い

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことでスピードが向上する可能性があります。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。

### ユーザーにテーブルを照会する権限がない

このエラーが発生した場合は、ユーザー権限を追加してテーブルを照会します。

### 使用量がカスタムクォータを超えた

このエラーが表示された場合、クォータを更新する必要があるため、現在のレートで同期を続けることができる。

### テーブルが場所 {region} の場所に見つからなかった

このエラーが表示された場合は、テーブルが正しいプロジェクトとデータセットにあることを確認してほしい。

### 無効なJWT署名

このエラーが表示された場合は、アカウントでBigQuery APIサービスが有効になっていることを確認する。
{% endtab %}

{% tab Databricks %}
### テスト接続が遅い

テスト接続はデータウェアハウス上で実行されるため、ウェアハウスの容量を増やすことでスピードが向上する可能性があります。Databricks の場合、Braze が Classic および Pro の SQL インスタンスに接続するときにウォームアップ時間が 2 〜 5 分かかることがあるため、接続の設定中やテスト中、およびスケジュールされた同期の開始時に遅延が発生します。サーバーレス SQL インスタンスを使用すると、ウォームアップ時間が最小限に抑えられ、クエリのスループットが向上しますが、連携コストが若干高くなる場合があります。

### ウェアハウスが停止していためコマンドが失敗した

このエラーが表示された場合は、Databricks ウェアハウスが実行されていることを確認します。

### サービス: Amazon S3; ステータスコード：403; エラーコード403禁

このエラーが発生した場合は、[Databricks を参照のこと：S3データへのアクセス中に禁則エラー](https://kb.databricks.com/security/forbidden-access-to-s3-data).
{% endtab %}
{% endtabs %}

## CDI統合のメールアラート設定を更新するには？

各インテグレーションには、それぞれ独自の通知設定がある。CDIページに移動し、更新したい統合名を選択する。**通知設定**セクションで、選択した統合に関するアラートの受信方法を更新できる。

## 将来のUPDATED_ATが統合と同期された場合はどうなるのか？

CDI は `UPDATED_AT` を使用して、新しいデータを特定します。未来の `UPDATED_AT` を同期すると、それ日時以前のデータは処理されません。これを修正するには、次の操作を行います。:

1. `UPDATED_AT` を修正します。
2. Brazeと同期済みの古いデータを削除する。
3. そのテーブルを再び処理するために、新しい統合を作成する。

## なぜ「同期された行数」がウェアハウスの数値と一致しないのですか?

CDI は `UPDATED_AT` を使用して、同期中に取得するレコードを決定します。どのように機能するかは、[このイラストを]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/#what-gets-synced)ご覧いただきたい。同期実行の冒頭で、CDI はウェアハウスにクエリし、前回処理した値より後の `UPDATED_AT` を持つレコードをすべて取得します。クエリー実行時にピックアップされたレコードはすべてBrazeに同期される。以下は、レコードが同期されない可能性のある一般的なケースである：

- すでに処理済みの `UPDATED_AT` 値を持つレコードをテーブルに追加している。
- 同期によってレコードを処理した後に、それらのレコードの値を更新しているが、`UPDATED_AT` を変更していない。 
- 同期の進行中にレコードの追加または更新を実行している。CDIクエリの実行タイミングによっては、レコードがピックアップされないレースコンディションが発生する可能性がある。

{% alert tip %}
今後、このような動作を回避するために、単調増加する `UPDATED_AT` 値を使用し、スケジュールされた同期実行中にはテーブルを更新しないことをお勧めします。
{% endalert %}

## 同期中、複数のレコードが同じIDを共有する場合、順序は保持されるか？

処理順序は100％予測できるものではない。例えば、同期中にテーブル内に同じ`EXTERNAL_ID` を持つ複数の行がある場合、最終的にどの値がプロファイルに入るかは保証できない。同じ`EXTERNAL_ID` をペイロード列の異なる属性で更新している場合、同期が完了するとすべての変更が反映されます。

## CDIのセキュリティ対策はどうなっているのか？

### 当社の取り組み

Braze では CDI に関して以下の対策を講じています。:

- すべての認証情報はデータベース内で暗号化され、特定の社員のみが認証されたアクセス権を持つ。
- 当社では、暗号化された接続を使用して、お客様のウェアハウスにデータを送信しています。
- Braze APIエンドポイントへのリクエストは、当社がお客様に使用を推奨しているのと同じAPIキーとTLS接続を使用して行う。
- 定期的にライブラリを更新し、すべてのセキュリティパッチを取得しています。

### お客様の対策

お客様と社内チームで、御社側に以下のセキュリティ対策を講じることをお勧めします。 

- 認証情報へのアクセスを、CDI の運用に必要な最小限に制限します。これは、特定のテーブルとビューに対してセレクト（とカウント）を実行できるようにする必要があるからだ。
- テーブルにアクセスできる IP を、正式に公開された[Braze IP]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/.#step-1-set-up-tables-or-views) に制限します。
