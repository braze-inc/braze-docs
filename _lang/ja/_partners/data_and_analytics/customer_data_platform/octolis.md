---
nav_title: Octolis
article_title: Octolis
description: "このリファレンス記事では、Braze と Octolis のパートナーシップについて説明します。Octolisはデータアクティベーションプラットフォームであり、データを Braze に統合できます。"
alias: /partners/octolis/
page_type: partner
search_tag: Octolis

---

# Octolis

> [Octolis](http://octolis.com)は、強力なデータアクティベーションプラットフォーム(またはヘッドレスCDP)です。Octolisは、自分が所有するデータベースの上に座って、ビジネスツールでデータを統合、準備、スコア化、同期するための簡単な方法です。

_この統合は Octolis によって管理されます。_

## 統合について

Braze と Octolis の統合は、生データソースと Braze 間のミドルウェアとして機能します。これにより、オンラインとオフラインのさまざまなソースからデータを取得して統合できます。
1. エスホップ、CRM、POSシステムなどの情報源からのデータを統一し、統合する。
2. 正規化とスコア化
3. 計算されたフィールドsと事象のBrazeへのリアルタイム同期

![]({% image_buster /assets/img/Octolis/Braze_scheme.png %})

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Octolisアカウント | このパートナーシップを活用するには、Octolis アカウントが必要です。 |
| Braze REST API キー | [**users.track**]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) 権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。エンドポイントは、インスタンスのBraze URLに依存する。 |
| Brazeアプリキー | アプリ識別子キー。これは、**Braze ダッシュボード > [設定の管理] > [API キー]** で確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

統合を開始する前に、接続、ソース、オーディエンス、および同期に関する以下のセクションを参照してください。

詳細については、Octolis [Getting started](https://help.octolis.com/)セクションを参照してください。

### ステップ1:Octolisをデータソースに接続する

Braze にデータを送信するには、少なくとも1つの[オーディエンス](https://help.octolis.com/audiences/create-a-no-code-audience)を作成しておく必要があります。オーディエンスは、いくつかのデータソースsを結合し、それらを調製ステップsにアプリし、計算されたフィールドsを加算します。

これらのオーディエンスは、さまざまなデータソースに基づいて作成する必要があります。ソースとして次のいずれかを使用できます。
- Salesforce オブジェクト(取引先責任者、取引先など)
- Zendesk オブジェクト(チケット)
- SFTP 内のファイル(一部の連絡先を含むCSVファイル、イベントを含むJSON ファイルなど)
- データベースのテーブル/ビュー。
- いずれかのシステムから、Webhook や API 呼び出しを通じてレコードが送信されます。

### ステップ2:Braze を宛先として追加する

次に、Braze を新しい宛先として設定するには、メイン画面の現在の宛先の上にある [**\+ Add more**] を選択し、利用可能なビジネスツールから [**Braze**] を選択します。

![]({% image_buster /assets/img/Octolis/Braze_screen2.png %})

選択したら、以下を入力します。

- Braze API キー:これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。
- 時間ウィンドウ:Octolis は特定の期間にわたってレート制限を適用します。
- Request volume:この期間内に実行できるリクエストの数。
- カスタム属性s:ここで、Braze に送信する新しいフィールドs、その形式(文字列、整数、浮動小数点数)、および**sync に必要な**を指定します(いずれかを同期に必須にする場合)。

![]({% image_buster /assets/img/Octolis/Braze_screen3.png %})

設定が完了すると、ホーム画面で新しい宛先として Braze が表示されます。

### ステップ3:新しい同期の作成

メニューから**Syncs**をクリックし、右上の**Add sync**を選択します。以前に作成したオーディエンスから、使用するオーディエンスを選択します。
次に、宛先として [**Braze**] を選択し、データ宛先エンティティを選択します。

![]({% image_buster /assets/img/Octolis/Braze_screen4.png %})

### ステップ 4: 出力設定を行う

デフォルトでは、送信するすべての属性が Braze により作成されますが、同期するフィールドのリストを文書に記録しておく必要があります。

![]({% image_buster /assets/img/Octolis/Braze_screen5.png %}){: style="max-width:75%;"}

設定フィールドの具体的な定義を次に示します。

| フィールド | 説明 |
| --- | --- |
| オーディエンスの同期先は? | レコードを作成または更新する Braze エンティティ。 |
| レコードを識別するために使用されるフィールドは? | フィールドは、レコードがすでにBrazeに存在する場合、Octolis を使用してレコードを識別します。 |
| How often do you want to send each record? | デフォルトでは、すべての統合 (API、データベース、FTP) で同期は増分同期になります。つまり、最後の更新以降の新しい値のみが更新d になります。必要に応じて、定期的にテーブル全体を送信することもできます。開始時に、Octolisは完全なテーブルを送信します。 |
| 同期するフィールドはどれですか? | Octolis と Braze のフィールドのマッピングです。利用可能なすべてのフィールドのリストがドロップダウンメニューに表示される。計算フィールドをBrazeに送信するには、まず、Brazeエンティティ内に対応する列を作成したことを確認する必要があります。 |
| オーディエンスをいつ同期しますか? | Braze へのデータの送信方法: 手動、リアルタイム、またはプログラムによる送信のいずれかです。  |
| Sync when record is... | 作成:オプトインの場合、Braze テーブルがマスターのままであることが重要です。フィールドの更新時に Octolis が同期をトリガーしないようにします。<br><br>更新:一方で、たとえば名前フィールドの場合、顧客が新しいエントリを入力するたびに Braze テーブルのフィールドを更新できるようにすることがあります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 複数キーの重複排除

重複排除は、複数のソース、特にオンラインおよびオフラインのソースのデータを照合する場合に大きな課題となります。Octolis の高度なノーコードモジュールにより、[重複排除](https://help.octolis.com/resources/faq/what-is-deduplication-and-how-does-it-work)に複数のキーを使用できます。このモジュールは各マスターテーブルで使用できます。つまり、各エンティティにロジックを適合させることができます。


