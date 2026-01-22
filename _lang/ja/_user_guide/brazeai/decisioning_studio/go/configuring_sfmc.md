---
nav_title: Salesforce Marketing Cloud を使用した設定
article_title: BrazeAI デシジョンスタジオGo 用のSalesforce Marketing Cloud を使用した設定
page_order: 5
description: "BrazeAI Decisioning Studio<sup>TM</sup> Go で使用するために、Salesforce Marketing Cloud でデータクエリオートメーションとジャーニーを設定する方法について説明します。"
toc_headers: h2
---

# BrazeAI Decisioning Studio™Go 用のSalesforce Marketing Cloud を使用した設定

> Salesforce Marketing Cloud (SFMC) でジャーニーを設定し、BrazeAI Decisioning Studio™Go を介して送信のトリガーを開始します。

## データクエリオートメーションの設定

### ステップ 1: 新しいオートメーションの作成

1. Salesforce Marketing Cloud ホームから、**Journey Builder** に移動し、**Automation Studio** を選択します。

![Journey BuilderナビゲーションのAutomation Studioオプション。]({% image_buster /assets/img/decisioning_studio_go/query13.png %})

{: start="2"}
2\.**新規自動化**を選択します。
3\.**Schedule** ノードを**Starting Source** としてドラッグアンドドロップします。

!["Schedule"ジャーニーの開始元として使用します。]({% image_buster /assets/img/decisioning_studio_go/query14.png %})

{: start="4"}
4. **Schedule** ノードで、**Configure** を選択します。
5. スケジュールに以下を設定します。
    - **開始日:**明日の暦日
    - **時間:****午前12:00**
    - **タイムゾーン:****(GMT-05:00) Eastern (米国& カナダ)**
6. **Repeat**では、**Daily**を選択します。
7. このスケジュールを終了しないように設定します。
8. **Done**を選択してスケジュールを保存します。

![毎日繰り返すために、2024年1月25日午前12時に定義されたサンプルスケジュール。]({% image_buster /assets/img/decisioning_studio_go/query12.png %})

### ステップ 2:SQL クエリを作成する

次に、サブスクライバー s クエリとエンゲージメント クエリの2 つのSQL クエリを作成します。これらのクエリーを使用すると、BrazeAI Decisioning Studio™Go でオーディエンスにデータを取り込み、エンゲージメントのイベントを取り込むことができます。

{% tabs %}
{% tab Subscribers query %}
1. **SQLクエリ**をキャンバスにドラッグアンドドロップします。
2. ****を選択します。
3. **Create New Query Activity**を選択します。
4. クエリに名前と外部キーを指定します。BrazeAI Decisioning Studio™Goポータルで提供されているサブスクライバークエリーに推奨される名前と外部キーを使用することをお勧めします。 

![例"OFE_Subscribers_query_Test5" と外部キー。]({% image_buster /assets/img/decisioning_studio_go/query11.png %})

{: start="5"}
5. [**次へ**] を選択します。
6. BrazeAI Decisioning Studio™Go ポータルで、**Subscriber Query Resources** でシステムデータSQL クエリを見つけます。
7. クエリをコピーしてテキストボックスに貼り付け、**Next**を選択します。

![SQL Query セクションのクエリの例。]({% image_buster /assets/img/decisioning_studio_go/query10.png %})

{: start="8"}
8. BrazeAI Decisioning Studio™Go ポータルで、**Resources で** セクションを使用して、ターゲットデータ拡張の外部キーを見つけます。次に、検索バーに貼り付けて検索します。

![検索バーに貼り付けられた外部キー]({% image_buster /assets/img/decisioning_studio_go/query9.png %})

{: start="9"}
9\.検索した外部キーに一致するデータ拡張子を選択します。ターゲットデータ拡張名は、BrazeAI Decisioning Studio™Goポータルでも相互参照できます。サブスクライバークエリーの**Data Extension**は、`BASE_AUDIENCE_DATA`サフィックスで終わる必要があります。

![外部キーの例と一致するデータ拡張名。]({% image_buster /assets/img/decisioning_studio_go/query8.png %})

{: start="10"}
10\.**Overwrite**を選択し、**Next**を選択します。
{% endtab %}
{% tab Engagement query %}
1. **SQLクエリ**をキャンバスにドラッグアンドドロップします。

!["SQL Query"ジャーニーのアクティビティとして追加されました。]({% image_buster /assets/img/decisioning_studio_go/query7.png %})

{: start="2"}
2\.****を選択します。
3\.**Create New Query Activity**を選択します。
4. クエリに名前と外部キーを指定します。BrazeAI Decisioning Studio™Goポータルで提供されているエンゲージメントクエリーに推奨される名前と外部キーを使用することをお勧めします。 

![例"OFE_Engagement_query" と外部キー。]({% image_buster /assets/img/decisioning_studio_go/query6.png %})

{: start="5"}
5. [**次へ**] を選択します。
6. BrazeAI Decisioning Studio™Go ポータルで、**Engagement Query Resources** でシステムデータSQL クエリを見つけます。
7. クエリをコピーしてテキストボックスに貼り付け、**Next**を選択します。

![SQL Query セクションのクエリの例。]({% image_buster /assets/img/decisioning_studio_go/query5.png %})

{: start="8"}
8. BrazeAI Decisioning Studio™Goポータルで指定されているEngagement Queryの対象となるData Extensionを見つけて選択します。 

{% alert tip %}
ターゲットデータ拡張名は、BrazeAI Decisioning Studio™Goポータルでも相互参照できます。 Engagement Query のターゲットData Extension を確認してください。エンゲージメントクエリーの**Data Extension**は、ENGAGEMENT_DATAサフィックスで終わる必要があります。
{% endalert %}

{: start="9"}
9\.**Overwrite**を選択し、**Next**を選択します。

![外部キーの例と一致するデータ拡張名。]({% image_buster /assets/img/decisioning_studio_go/query4.png %})

{% endtab %}
{% endtabs %}

### ステップ 3:オートメーションの実行

1. オートメーションに名前を付け、**Save**を選択します。

![オートメーション "OFE_Experimenter_Test5_Automation".]({% image_buster /assets/img/decisioning_studio_go/query3.png %} の例

{: start="2"}
2\.次に、**Run Once**を選択して、すべてが期待どおりに動作していることを確認します。
3\.両方のクエリを選択し、**Run** を選択します。

![実行する選択したSQL クエリアクティビティの一覧を含むオートメーション"OFE_Experimenter_Test5_Automation"。]({% image_buster /assets/img/decisioning_studio_go/query2.png %})

{: start="4"}
4. **今すぐ実行**を選択します。

![選択したSQL クエリアクティビティ。]({% image_buster /assets/img/decisioning_studio_go/query1.png %})

これで、オートメーションが正常に実行されていることを確認できます。オートメーションが期待どおりに動作しない場合は、Brazeサポートに連絡して、サポートを受けてください。

## SFMC ジャーニーの作成

### ステップ 1: ジャーニーのセットアップ

1. Salesforce Marketing Cloud で、**Journey Builder** > **Journey Builder** に移動します。
2. **Create New Journey**を選択します。
3. ジャーニータイプには、**Multi-Step Journey**を選択し、**Create**を選択します。

![ディシジョンスプリットノードと複数の電子メールノードに接続されたAPI イベントエントリソース。]({% image_buster /assets/img/decisioning_studio_go/journey1.png %})

### ステップ 2:ジャーニーの構築

#### ステップ 2.1: エントリ源の作成

1. エントリ元の場合、**API Event** をジャーニービルダーにドラッグします。

!["API Event"エントリ元として選択されます。]({% image_buster /assets/img/decisioning_studio_go/journey2.png %})

2. **API Event**で、**Create an event**を選択します。

![" は、API イベントでevent" オプションを作成します。]({% image_buster /assets/img/decisioning_studio_go/journey3.png %})

{: start="3"}
3\.**Select Data Extension**を選択します。BrazeAI Decisioning Studio™Goが推奨事項を書き込むデータエクステンションを見つけて選択します。
4. **Summary**を選択して変更を保存します。
5. API イベントを保存するには、**Done** を選択します。

![API イベントの概要。]({% image_buster /assets/img/decisioning_studio_go/journey4.png %}){: style="max-width:80%;"}

#### ステップ 2.2:条件分岐を追加

1. **Decision Split**を**API Entry Event**の後にドラッグ&ドロップします。 
2. **Decision Split**の内容で、最初のパスで**Edit**を選択します。

![Decision "Edit"ボタンで詳細を分割します。]({% image_buster /assets/img/decisioning_studio_go/journey5.png %})

{: start="3"}
3\.**Decision Split**を更新して、レコメンドデータ拡張によって渡されたテンプレート IDを使用します。**Journey Data**でアプリの適切なフィールドを見つけます。

![Decision SplitのPath 1のJourney Dataセクション。]({% image_buster /assets/img/decisioning_studio_go/journey6.png %})

{: start="4"}
4. エントリを選択し、目的のテンプレート ID フィールドを見つけてワークスペースにドラッグします。

![含めるメール テンプレート ID。]({% image_buster /assets/img/decisioning_studio_go/journey7.png %})

{: start="5"}
5. 最初のメール テンプレートのテンプレート ID を入力し、**Done** を選択します。
6. このパスを保存するには、**Summary**を選択します。
7. メール テンプレートs ごとにパスを追加し、上記のステップ4 ～6 を繰り返して、テンプレート ID がそれぞれのテンプレートのID と一致するようにフィルター基準を設定します。
8. **Done**を選択して**Decision Split**ノードを保存します。

![デシジョン分割でメール テンプレート ID ごとに2 つのパスを分割します。]({% image_buster /assets/img/decisioning_studio_go/journey10.png %}){: style="max-width:65%;"}

#### ステップ 2.3:デシジョン分割ごとにメールを追加する

1. **Email**ノードを**Decision Split**のそれぞれのパスにドラッグします。
2. **Email**を選択し、各パスに配置するアプリの適切なテンプレートを選択します(つまり、ID 値を持つテンプレートは、デシジョンスプリットのロジックと一致する必要があります)。

![ジャーニーに追加された電子メールノード。]({% image_buster /assets/img/decisioning_studio_go/journey9.png %})

### ステップ 3:ジャーニーの有効化

ジャーニーを設定したら、ジャーニーを有効化し、BrazeAI Decisioning Studio™Go チームと以下の情報を共有します。 

* ジャーニーID
* ジャーニー名
* APIイベント定義キー
* 推奨データ拡張外部キー

{% alert note %}
BrazeAI Decisioning Studio™Go ポータルには、サブスクライバー s およびエンゲージメント を1 日1 回エクスポートするためにプロビジョニングされたSFMC オートメーションが表示されます。SFMC でこのオートメーションを開封する場合は、必ずオーズを解除し、ライブに戻してください。
{% endalert %}

1. BrazeAI Decisioning Studio™Goポータルで、**ジャーニー名**をコピーします。
2. 次に、Salesforce Marketing Cloud Journey Builder で、検索バーにジャーニー名を貼り付けます。
3. ジャーニー名を選択します。ジャーニーは現在ドラフトステータスにあります。
4. **Validate**を選択します。

![有効化する完了したジャーニー。]({% image_buster /assets/img/decisioning_studio_go/activate3.png %})

{: start="5"}
5. 次に、検証結果を確認し、**Activate** を選択します。

![「検証ルール」セクションにリストされている推奨事項。]({% image_buster /assets/img/decisioning_studio_go/activate1.png %}){: style="max-width:60%;"}

{: start="6"}
6. **Activate Journey** summary で、**Activate** を再度選択します。

![ジャーニーの概要。]({% image_buster /assets/img/decisioning_studio_go/activate2.png %}){: style="max-width:85%;"}

すべて完了しました。これで、BrazeAI Decisioning Studio™Go を介した送信のトリガーを開始できます。
