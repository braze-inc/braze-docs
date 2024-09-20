---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "この参考記事では、モバイル、ウェブ、代替データを他のサードパーティ・ソースに接続できるユニバーサル・データ・ハブであるBrazeとTealiumのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium[AudienceStreamは](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/)、オムニチャネルの顧客セグメンテーションとリアルタイムアクションエンジンである。AudienceStreamは、EventStreamに流れ込むデータを取り込み、顧客のブランドに対するエンゲージメントの最も重要な属性を表す訪問者プロファイルを作成する。 

BrazeとTealiumの統合は、AudienceStreamの訪問者プロファイルを活用している。共有された行動は、オーディエンスと呼ばれる共通の特徴を持つ訪問者のセットを作成するために、これらのプロファイルをセグメント化する。これらのオーディエンスは、コネクターを通じてリアルタイムでマーケティング・テクノロジー・スタックに燃料を供給することができる。 

{% alert important %}
TealiumのAudienceStreamsとEventStreamsは、バッチと非バッチの両方のコネクターアクションを提供する。非バッチコネクターは、リアルタイムリクエストがユースケースにとって重要で、BrazeのAPIレート制限仕様にヒットする懸念がない場合に使用すべきである。ご質問がある場合は、Braze[サポート]({{site.baseurl}}/braze_support/)またはカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件

| 名前 | 説明 |
| ---- | ----------- |
| Tealiumアカウント | サーバー側にアクセスできる[Tealiumアカウントが](https://my.tealiumiq.com/)必要である。このパートナーシップを活用するために、クライアント側のインテグレーションも利用することをお勧めする。 |
| REST APIキー | `users.track`,`users.delete`,`subscription.status.set` のパーミッションを持つBraze REST APIキー。<br><br>これは、**Brazeのダッシュボード > Developer Console > REST API Key > Create New API Keyで**作成できる。|
| \[Braze RESTエンドポイント][6] | RESTエンドポイントのURL。エンドポイントは、[インスタンスのBraze URLに]({{site.baseurl}}/api/basics/#endpoints)依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:属性とバッジを設定する

#### 属性を理解する

AudienceStreamを使う最初のステップは、属性を作成することだ。属性は、訪問者の習慣、好み、行動、ブランドとの関わりを表す重要な特徴を定義することができる。 

**属性を訪問する**：Visit属性は、ユーザーの現在の訪問（またはセッション）に関連する。これらの属性に保存されたデータは、訪問期間中持続する。訪問属性の例をいくつか挙げる：
- 訪問期間（人）
- 現在のブラウザ (文字列)
- 現在のデバイス (文字列)
- ページビュー数（数）

**ビジター属性**：ビジター属性は現在のユーザーに関連する。これらのアトリビュートに保存されたデータは、ユーザーの生涯にわたって持続する。ビジター属性の例としては、以下のようなものがある： 
- 生涯受注額（数字）
- 名 (文字列)
- 生年月日（日付）
- 買取ブランド（集計）

利用可能なデータタイプの全リストは[Tealiumを][1]参照のこと。

##### 属性の強化

必要な属性を特定したら、それを[エンリッチメント](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/)（属性の値をいつ、どのように更新するかを決定するビジネスルール）で構成することができる。それぞれのデータ型は、属性の値を操作するための独自のエンリッチメントの選択を提供する。これは "WHEN "設定と関連している。各訪問者および訪問者の属性に対して、以下のオプションが利用可能である：

- 新規訪問者：訪問者があなたのサイトに初めて来たときに発生する。
- 新規訪問：ビジターが新規に訪問した際に発生する。
- エニー・イベント：どのイベントでも発生する。
- Visit Ended：訪問が終了したときに発生する。

また、ルールと呼ばれるカスタム条件を作成し、エンリッチメントが発生するタイミングを決定することもできる。

#### バッジ

バッジは、貴重な行動パターンを表す特別なビジター属性である。バッジは、訪問者のエンリッチメントのロジックに基づいて割り当てられたり、外されたりする。このロジックは通常、訪問者セグメントを捕捉するために複数の条件を組み合わせたり、特定の値に達したときのしきい値を設定したりする。

#### 属性とバッジの例

{% tabs ローカル %}
{% tab 属性 %}

すべての完了した注文（購入イベント）に対して、顧客が費やした累積金額（`order_total` ）を計算するビジター属性 "Lifetime Order Value "を作成する。Tealiumアカウントでライフタイムオーダーバリューを設定するには、以下の指示に従う：

1. **AudienceStream > Visitor/Visit Attributesに**移動し、**Add Attributeを**クリックする。
2. スコープを**ビジターとして**選択し、**Continueを**クリックする。
3. データ型「**Number」を**選択し、「**Continue**」をクリックする。
4. 属性名 "Lifetime Order Value "を入力する。
5. **Add Enrichmentを**クリックし、**Increment NumberまたはDecrement Numberを**選択する。
6. インクリメントする値を含む属性を選択する（`order_total` ）。
7. WHEN "を "Any Event "に設定したまま、**"Create a New Rule**"をクリックする。
8. 購入イベントがいつ発生したかを識別するルールを作成する。
9. **Saveを**クリックし、**Finishを**クリックする。

これで、すべての顧客は生涯注文価値属性を持つことになる。

{% endtab %}
{% tab バッジ %}

バッジを作成することで、ユーザーが共有する特定の属性によってユーザーを分類し、ターゲットを絞ることができる。次の例では、"Lifetime Order Value "が$500以上のユーザーに対してVIPバッジを作成する。

1. **AudienceStream > Visitor/Visit Attributesに**移動し、**Add Attributeを**クリックする。
2. スコープを**ビジターとして**選択し、**Continueを**クリックする。
3. データ・タイプ**Badgeを**選択し、**Continueを**クリックする。
4. バッジの名前「VIP」を入力する。
5. **Add Enrichmentを**クリックし、**Assign Badgeを**選択する。
6. WHEN "は "Any Event "のままにしておく。
7. **Create Rule（ルールの作成）を**選択して、バッジ割り当てのルールを作成する。このルールにタイトルを割り当て、前回作成した属性を使用して、ルールを「...属性 "Lifetime Order Value greater than 500 "を持つ」と設定する。
8. **Saveを**クリックし、**Finishを**クリックする。

{% endtab %}
{% endtabs %}

### ステップ2:観客を作る

Tealiumのホームページから、サイドバーナビゲーションで**AudienceStreamの**下にある**Audiencesを**選択する。ここでは、共通の属性を持つユーザーのオーディエンスを作成することができる。このオーディエンスへのユーザの入室または退室は、次のステップで設定するコネクタアクションのトリガとなり、この情報をBrazeのユーザプロファイルに渡す。 

まず、オーディエンスに名前を付け、あなたが作ろうとしているオーディエンスのタイプにはどのような属性が当てはまるかを考える。例えば、VIPユーザーのオーディエンスを作成するには、**VIPバッジを持って**いる訪問者のオーディエンスを作成することができる。

終了したら、必ずオーディエンスを**保存／公開**すること。

### ステップ3:イベントコネクターを作成する

コネクターとは、Tealiumと他のベンダーの間でデータを伝送するために使用される統合のことである。これらのコネクターには、パートナーがサポートするAPIを表すアクションが含まれている。 

1. Tealiumのサイドバーの**Server-Sideから**、**AudienceStream > Audience Connectorsに**移動する。
2. 青い**＋Add Connector**ボタンを選択し、コネクタ市場を調べる。表示された新しいダイアログボックスで、スポットライト検索を使って**Braze**コネクタを探す。
3. このコネクタを追加するには、**Braze**コネクタタイルをクリックする。クリックすると、接続の概要と、必要な情報、サポートされているアクション、設定手順のリストが表示される。コンフィギュレーションは、ソース、コンフィギュレーション、アクションの3つのステップで構成される。

#### ソース

表示される**Source**ダイアログで、前のステップで作成したオーディエンスと、状況に適していると思われるトリガーを選択する。また、このアクションがトリガーされる頻度をコントロールするために、頻度キャップを切り替えることもできる。 

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### 構成

次に、**設定**ダイアログが表示される。ページ下部の**Add Connectorを**選択する。コネクタに名前を付け、Braze APIエンドポイントとBraze REST APIキーをここに入力する。

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

以前にコネクタを作成したことがある場合は、利用可能なコネクタリストから既存のコネクタを使用し、鉛筆アイコンでニーズに合うように修正するか、ゴミ箱アイコンで削除することもできる。 

このオーディエンスをリンクするコネクタを作成または選択したら、Doneをクリックして続行する。

#### アクション (Action)

次に、コネクターアクションに名前を付け、設定したマッピングに従ってデータを送信するアクションタイプを選択する。ここでは、Brazeの属性をTealiumの属性名にマッピングする。どのアクションタイプを選択するかによって、Tealiumが要求するフィールドはさまざまに選択される。以下は、これらのフィールドの例と説明である。

{% alert important %}
すべての項目が必須というわけではない。

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs ローカル %}
{% tab ユーザーを追跡する（バッチと非バッチ） %}

このアクションでは、ユーザー、イベント、購入の属性を1つのアクションですべて追跡できる。Track UserアクションはAudienceStreamとEventStreamの両方で同じだが、TealiumはAudienceStreamアクションでユーザー属性のマッピングを設定し、EventStreamアクションでイベントと購入のマッピングを設定することを推奨する。

| パラメーター | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、TealiumユーザーIDフィールドとBrazeユーザーIDフィールドを対応させる。1つ以上のユーザーID属性をマップする。複数のIDが指定された場合、以下の優先順位に基づいて、空白でない最初の値が選ばれる：外部ID、ブレイズID、エイリアス名、エイリアスラベル。<br><br>\- プッシュトークンをインポートする場合、外部IDとBraze IDを指定すべきではない。<br>\- ユーザーエイリアスを指定する場合は、エイリアス名とエイリアスラベルを設定する必要がある。<br><br>詳しくは、Braze[`/users/track` のエンド]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)ポイントをチェックしてほしい。 |
| ユーザー属性 | Brazeの既存のユーザープロファイルのフィールド名を使用して、Brazeダッシュボードのユーザープロファイル値を更新するか、独自のカスタム[ユーザー属性]({{site.baseurl}}/api/objects_filters/user_attributes_object/)データをユーザープロファイルに追加する。<br><br>\- デフォルトでは、ユーザーが存在しない場合、新しいユーザーが作成される。<br>-**Update Existing Onlyを** `true` に設定すると、既存のユーザーのみが更新され、新規ユーザーは作成されない。<br>\- Tealium属性が空の場合、NULLに変換され、Brazeユーザープロファイルから削除される。ユーザー属性を削除するためにBrazeにNULL値を送信すべきでない場合は、エンリッチメントを使用すべきである。 |
| ユーザー属性を変更する | このフィールドを使用して、特定のユーザー属性をインクリメントまたはデクリメントする。<br><br>\- 整数属性は、正の整数または負の整数でインクリメントすることができる。<br>\- 配列の属性は、既存の配列に値を追加したり削除したりすることで変更できる。 |
| イベント | イベントは、タイムスタンプにおける、特定のユーザーによるカスタムイベントの単一発生を表す。このフィールドを使用して、Braze[イベントオブジェクトに]({{site.baseurl}}/api/objects_filters/event_object/)あるようなイベント属性を追跡し、マッピングする。<br><br>\- イベント属性`Name` は、マッピングされたイベントごとに必要である。<br>\- イベント属性`Time` は、明示的にマッピングされない限り、自動的にnowに設定される。<br>\- デフォルトでは、イベントが存在しない場合、新しいイベントが作成される。`Update Existing Only` を`true` に設定すると、既存のイベントのみが更新され、新しいイベントは作成されない。<br>\- 配列タイプの属性をマップして、複数のイベントを追加する。配列型の属性は同じ長さでなければならない。<br>\- 単一値属性を使用し、各イベントに適用することができる。 |
| イベントテンプレート | ボディデータで参照されるイベントテンプレートを提供する。Brazeにデータを送る前に、テンプレートを使ってデータを変換することができる。詳しくはTealiumの[テンプレートガイドを](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)参照のこと。 |
| イベントテンプレート変数 | イベントテンプレート変数をデータ入力として提供する。詳しくはTealiumの[テンプレート変数ガイドを](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)参照のこと。 |
| 購入 | このフィールドを使用して、Brazeの[購買オブジェクトに]({{site.baseurl}}/api/objects_filters/purchase_object/)あるようなユーザーの購買属性を追跡し、マッピングする。<br><br>-`Product ID` 、`Currency` 、`Price` の購買属性は、マッピングされた購買ごとに必要である。<br>\- 購買属性`Time` は、明示的にマッピングされない限り、自動的にnowに設定される。<br>\- デフォルトでは、新規購入が存在しない場合、新規購入が作成される。`Update Existing Only` を`true` に設定すると、既存の購入のみが更新され、新しい購入は作成されない。<br>\- 複数の購入項目を追加するために、配列タイプの属性をマップする。配列型の属性は同じ長さでなければならない。<br>\- 単一値属性を使用することができ、各項目に適用される。|
| テンプレート購入 | テンプレートは、Brazeに送信する前にデータを変換するために使用できる。<br>\- ネストされたオブジェクトのサポートが必要な場合は、購入テンプレートを定義する。<br>\- 購入テンプレートが定義されると、アクションの購入セクションで設定されたコンフィギュレーションは無視される。<br>\- 詳しくはTealiumの[テンプレートガイドを](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)参照のこと。|
| 購入テンプレート変数 | 製品テンプレートの変数をデータ入力として提供する。詳しくはTealiumの[テンプレート変数ガイドを](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2}

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab ユーザーを削除する（非バッチ） %}

Brazeダッシュボードからユーザーを削除する。

| パラメーター | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、TealiumユーザーIDフィールドとBrazeユーザーIDフィールドを対応させる。<br><br>\- 1つ以上のユーザーID属性をマップする。複数のIDが指定された場合、以下の優先順位に基づいて、空白でない最初の値が選ばれる：外部ID、ブレイズID、エイリアス名、エイリアスラベル。<br>\- ユーザーエイリアスを指定する場合、エイリアス名とエイリアスラベルの両方を設定する必要がある。<br><br>詳細については、Braze[`/users/delete` のエンド]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)ポイントを参照のこと。 |
{: .reset-td-br-1 .reset-td-br-2}

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab ユーザーサブスクリプショングループのステータスを更新する（非バッチ） %}
この操作により、Braze SMSまたはEメール購読グループからユーザーを追加または削除することができる。

| パラメーター | 説明 |
| ---------- | ----------- |
| グループ・タイプ | このフィールドを使用して、SMS購読グループかEメール購読グループかを示す。 |
| 更新タイプ | このアクションを購読解除または購読イベントにマッピングする 
| 属性 | \- サブスクリプション・グループID（必須）：前のフィールドでマップされたグループタイプに関連するサブスクリプショングループのID。<br>\- 外部ID：ユーザーの外部ID。<br><br>電子メール・グループ特有のものである：<br>\- EメールユーザーのEメールアドレス。<br>**外部IDが定義されていない場合は、Eメールが必要となる。**<br><br>SMSグループ固有である：<br>\- 電話だ：E.164 。例えば、+14155552671である。<br>**外部IDが定義されていない場合、電話が必要となる。** |
{: .reset-td-br-1 .reset-td-br-2}

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

**仕上げを**選択する。

#### まとめ

作成したコネクタの概要を表示する。選択したオプションを変更したい場合は、「**Back**」を選択して編集するか、「**Finish」を**選択して完了する。

コネクタがTealiumホームページのコネクタ一覧に表示される。

終了したら、必ずコネクタを保存するかパブリッシュすること。設定したアクションは、トリガーの接続が満たされたときに実行される。 

### ステップ4:Tealiumコネクタをテストする

コネクターが稼動したら、正常に動作しているかテストする必要がある。これをテストする最も簡単な方法は、Tealium**Trace Toolを**使うことである。Traceを使い始めるには、Tealium Toolsブラウザ拡張機能を追加していることを確認する。

1. 新しいトレースを開始するには、サイドバーの**サーバーサイドオプションから** **トレースを**選択する。**Startを**クリックし、トレースIDをキャプチャする。
2. ブラウザ拡張機能を開き、AudienceStream TraceにトレースIDを入力する。
3. リアルタイムのログを調べる。
4. **Actions Triggered（トリガーされたアクション）」の**エントリーをクリックして展開し、検証したいアクションをチェックする。
5. 検証したいアクションを探し、ログのステータスを見る。 

TealiumのTraceツールの実装方法については、Tealiumの\[Trace documentation][21] ]を参照すること。

## 統合デモ

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## データ・ポイント超過の可能性

Tealiumを通じてBrazeを統合する際に、誤ってデータ超過に見舞われる可能性のある主な方法は3つある：

#### 重複したデータを送信する - 属性のBraze差分のみを送信する
Tealiumはユーザー属性のBrazeデルタを送信しない。例えば、ユーザーのファーストネーム、Eメール、携帯電話番号を追跡するEventStreamアクションがある場合、Tealiumはアクションがトリガーされるたびに、3つの属性すべてをBrazeに送信する。Tealiumは、何が変更されたか、更新されたかを探し、その情報のみを送信することはない。<br><br> 
**解決策**だ：<br>バックエンドをチェックして属性が変更されたかどうかを評価し、変更された場合はTealiumの関連メソッドを呼び出してユーザープロファイルを更新することができる。**これは、Brazeを直接統合するユーザーが通常行うことである。**<br>**または**<br> バックエンドにユーザープロファイルの独自のバージョンを保存しておらず、属性が変更されたかどうかが分からない場合は、AudienceStreamを使用し、値が変更された場合にのみユーザー属性を送信する[エンリッチメントを作成](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/)することができる。 

#### 無関係なデータを送信したり、不必要にデータを上書きしたりする。
同じイベントフィードをターゲットとする複数のEventStreamがある場合、1つのアクションがトリガーされると、**そのコネクタで有効になっているすべてのアクションが**自動的に起動する**。**<br><br>
**解決策**だ：<br>各アクションを追跡するために、個別のイベント仕様またはフィードを設定する。<br>**または**<br> Tealiumダッシュボードのトグルを使って、起動したくないアクション（またはコネクタ）を無効にする。

#### Brazeの初期化が早すぎる
Braze Web SDKタグを使用してTealiumと統合するユーザーは、MAUが劇的に増加する可能性がある。**Brazeがページ読み込み時に初期化される場合、Brazeは、ウェブユーザーが初めてウェブサイトに移動するたびに匿名プロファイルを作成する。**MAUカウントを下げるために、ユーザーが「サインイン」や「ビデオ視聴」など、何らかのアクションを完了した時だけ、ユーザーの行動をトラッキングしたいと考える人もいるだろう。<br><br>
**解決策**だ：<br>[ロードルールを](https://docs.tealium.com/iq-tag-management/load-rules/about/)設定し、タグがサイト上でロードされるタイミングと場所を正確に決定する。

[1]: https://docs.tealium.com/server-side/attributes/about/
[15]: {% image_buster /assets/img/tealium/create_configuration.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[21]: https://docs.tealium.com/server-side/connectors/trace/about/
[17]: {% image_buster /assets/img/tealium/save_publish.png %}
