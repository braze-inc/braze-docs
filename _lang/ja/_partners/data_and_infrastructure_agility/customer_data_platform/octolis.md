---
nav_title: オクトリス
article_title: オクトリス
description: "このリファレンス記事では、Braze と、データをBraze に統合できるデータアクティベーションプラットフォームであるOctolis の連携について説明します。"
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# オクトリス

> [Octolis][0]は、強力なデータアクティベーションプラットフォーム(またはヘッドレスCDP)です。Octolisは、自分が所有するデータベースの上に座って、ビジネスツールでデータを統合、準備、スコア化、同期するための簡単な方法です。

Braze とOctolis の統合は、未加工のデータソースとBraze間のミドルウェアとして機能し、オンラインとオフラインのさまざまなソースからデータを取得して統合することができます。
1. エスホップ、CRM、POSシステムなどの情報源からのデータを統一し、統合する。
2. 正規化とスコア化
3. 計算されたフィールドsと事象のBrazeへのリアルタイム同期

![][7]

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| Octolisアカウント | この提携の前進タグeをとるには、オクトーリスの勘定が必要である。 |
| Braze REST API キー | [**users.track**][1] 権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
| Braze REST エンドポイント | [Your REST エンドポイント URL][2].エンドポイントは、インスタンスのBraze URL によって異なります。 |
| Braze アプリボタン | アプリ 識別子ボタン。これは、** Braze Dashboard > Manage Settings > API Key** にあります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

インテグレーションを開始する前に、コネクション、ソース、オーディエンスs、シンクに関する以下の節を参照してください。

詳細については、Octolis [Getting started][4]セクションを参照してください。

### ステップ1:Octolisをデータソースに接続する

Braze に送信するには、少なくとも1 つの[オーディエンス][5] が作成されていることを確認する必要があります。オーディエンスは、いくつかのデータソースsを結合し、それらを調製ステップsにアプリし、計算されたフィールドsを加算します。

これらのオーディエンスsは、いくつかのデータソースsに基づいて構築する必要があります。ソースには、次のいずれかを指定できます。
- Salesforce オブジェクト(取引先責任者、取引先など)
- Zendesk オブジェクト(チケット)
- SFTP 内のファイル(一部の連絡先を含むCSVファイル、イベントを含むJSON ファイルなど)
- データベースのテーブル/ビュー。
- システムの1 つが、webhookまたはAPI 呼び出しを介してレコードを送信します。

### ステップ2:Brazeを送信先として追加する

次に、Braze を新しい送信先として設定するには、メインスクリーン内のカレント送信先の上部で**\+ Add more** を選択し、利用可能なビジネスツールから**Braze** を選択します。

![][9]

選択したら、以下を入力します。

- Braze API キー:これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。
- 時間ウィンドウ:オクトリスは与えられた時期にレート制限をアプリします。
- リクエストボリューム:この期間内に実行できるリクエストの数。
- カスタム属性s:ここで、Braze に送信する新しいフィールドs、その形式(文字列、整数、浮動小数点数)、およびsync に必要な** を指定します(いずれかを同期に必須にする場合)。

![][10]

設定が完了すると、Braze は新しい送信先としてイヤーをホームスクリーンにアプリします。

### ステップ3:新しい同期の作成

メニューから**Syncs**をクリックし、右上の**Add sync**を選択します。以前に作成したオーディエンスから選択するオーディエンスを選択します。
次に、送信先として**Braze**を選択し、データを送信するエンティティを選択します。

![][11]

### ステップ4:出力設定設定s

デフォルトでは、Braze は送信するすべての属性s を作成しますが、同期するフィールドs の一覧を文書化する必要があります。

![][12]{: style="max-width:75%;"}

設定 s フィールド s の具体的な定義を次に示します。

| フィールド | 説明 |
| --- | --- |
| オーディエンスの同期先はどこですか? | レコードを作成または更新するBrazeのエンティティ。 |
| レコードを識別するために使用されるフィールドは? | フィールドは、レコードがすでにBrazeに存在する場合、Octolis を使用してレコードを識別します。 |
| どのくらいの頻度で各レコードを送信しますか? | デフォルトでは、シンクはすべての統合(API、データベース、FTP)に対してインクリメンタルになります。つまり、最後の更新以降の新しい値のみが更新d になります。必要に応じて、定期的にテーブル全体を送信することもできます。開始時に、Octolisは完全なテーブルを送信します。 |
| 同期するフィールドはどれですか? | オクトリスはs m アプリ ing をBraze フィールドする。使用可能なすべてのフィールドの一覧が、ドロップダウンメニューの耳にアプリします。計算フィールドをBrazeに送信するには、まず、Brazeエンティティ内に対応する列を作成したことを確認する必要があります。 |
| オーディエンスをいつ同期しますか? | Brazeへの送信方法:手動、リアルタイム、またはプログラム  |
| レコードが…のときに同期 | 作成:オプトインの場合、Brazeテーブルがマスタのままであることが大切です。フィールドが更新dのときに同期をトリガーしないようにします。<br><br>更新:一方、名 フィールドの場合は、顧客が新しいエントリを提供するたびに、Brazeテーブルのフィールドに更新できるようにする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## マルチキー重複排除

重複排除は、複数のソース、特にオンラインおよびオフラインからのデータを調整する場合の重要な課題です。Octolisの高度なno-コードモジュールを使用すると、[deduplication][3]に複数のキーを使用できます。このモジュールは各マスターテーブルで使用できます。つまり、各エンティティにロジックを適合させることができます。

[0]: http://octolis.com
[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work
[4]: https://help.octolis.com/
[5]: https://help.octolis.com/audiences/create-a-no-code-audience
[6]: {{site.baseurl}}/api/api_limits/
[7]: {% image_buster /assets/img/Octolis/Braze_scheme.png %}
[8]: {% image_buster /assets/img/Octolis/Braze_screen1.png %}
[9]: {% image_buster /assets/img/Octolis/Braze_screen2.png %}
[10]: {% image_buster /assets/img/Octolis/Braze_screen3.png %}
[11]: {% image_buster /assets/img/Octolis/Braze_screen4.png %}
[12]: {% image_buster /assets/img/Octolis/Braze_screen5.png %}
