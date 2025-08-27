---
nav_title: Tealium AudienceStream
article_title: Tealium AudienceStream
page_order: 2
alias: /partners/tealium_audience_stream/
description: "このリファレンス記事では、Braze と Tealium のパートナーシップについて説明します。Tealium は、モバイルデータ、Web データ、代替データを他のサードパーティソースに接続できるユニバーサルデータハブです。"
page_type: partner
search_tag: Partner

---

# Tealium AudienceStream

> Tealium [AudienceStream](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/introduction/) は、オムニチャネルの顧客セグメンテーションおよびリアルタイムアクションエンジンです。AudienceStream は EventStream に流入するデータを取得し、ブランドのカスタマーエンゲージメントの最も重要な属性を表す訪問者プロファイルを作成します。 

Brazeと Tealium の統合には、AudienceStream の訪問者プロファイルが利用されています。共有された行動は、オーディエンスと呼ばれる共通の特徴を持つ訪問者のセットを作成するために、これらのプロファイルをセグメント化する。これらのオーディエンスは、コネクターを介してリアルタイムでマーケティングテクノロジースタックにデータを提供できます。 

{% alert important %}
TealiumのAudienceStreamsとEventStreamsは、バッチと非バッチの両方のコネクターアクションを提供する。非バッチコネクターは、リアルタイムリクエストがユースケースにとって重要であり、Braze の API レート制限指定に達する懸念がない場合にのみ使用してください。ご質問がある場合は、Braze [サポート]({{site.baseurl}}/braze_support/)またはカスタマーサクセスマネージャーにお問い合わせください。
{% endalert %}

## 前提条件

| 名前 | 説明 |
| ---- | ----------- |
| Tealiumアカウント | サーバー側にアクセスできる[Tealiumアカウントが](https://my.tealiumiq.com/)必要である。このパートナーシップを活用するために、クライアント側のインテグレーションも利用することをお勧めする。 |
| REST APIキー | `users.track`,`users.delete`,および `subscription.status.set` の権限を持つ Braze REST API キー。<br><br>これは **Brazeダッシュボード > [開発者コンソール] > [REST API キー] > [新しい API キーを作成]** で作成できます|
| [Braze RESTエンドポイント]({{site.baseurl}}/api/basics/#endpoints) | RESTエンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/api/basics/#endpoints) に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:属性とバッジを設定する

#### 属性を理解する

AudienceStreamを使う最初のステップは、属性を作成することだ。属性を使用して、訪問者の習慣、好み、アクション、ブランドへのエンゲージメントを表す重要な特性を定義できます。 

**訪問属性**:Visit属性は、ユーザーの現在の訪問（またはセッション）に関連する。これらの属性に保存されたデータは、訪問期間中持続する。訪問属性の例をいくつか挙げる：
- Visit Duration (数値)
- 現在のブラウザ (文字列)
- Current Device (文字列)
- ページビュー数（数）

**訪問者属性**:ビジター属性は現在のユーザーに関連する。これらの属性に保存されるデータは、ユーザーの存続期間全体にわたって持続します。訪問者属性の例としては、以下のものがあります。 
- Lifetime Order Value (数値)
- First Name (文字列)
- 生年月日（日付）
- Purchases Brands (集計)

利用可能なデータタイプの全リストは[Tealiumを](https://docs.tealium.com/server-side/attributes/about/)参照のこと。

##### 属性エンリッチメント

必要な属性を特定したら、それを[エンリッチメント](https://docs.tealium.com/server-side/getting-started/audiencestream-cdp/attributes-enrichments/)（属性の値をいつ、どのように更新するかを決定するビジネスルール）で構成することができる。それぞれのデータ型は、属性の値を操作するための独自のエンリッチメントの選択を提供する。これは "WHEN "設定と関連している。各訪問属性および訪問者属性で利用可能なオプションを以下に示します。

- 新規訪問者：訪問者があなたのサイトに初めて来たときに発生する。
- 新規訪問：ビジターが新規に訪問した際に発生する。
- Any Event: 任意のイベントで発生します。
- Visit Ended: 訪問が終了したときに発生します。

また、エンリッチメントが発生するタイミングを決定するカスタム条件 (ルール) を作成することもできます。

#### バッジ

バッジは、価値の高い行動パターンを表す特別な訪問者属性です。バッジは、訪問者のエンリッチメントのロジックに基づいて割り当てられたり、外されたりする。このロジックは通常、訪問者セグメントを捕捉するために複数の条件を組み合わせたり、特定の値に達したときのしきい値を設定したりする。

#### 属性とバッジの例

{% tabs ローカル %}
{% tab 属性 %}

すべての完了した注文 (購入イベント) での顧客の累積支出額 (`order_total`) を計算する訪問者属性「Lifetime Order Value」を作成します。Tealium アカウントで生涯注文額を設定するには、次の手順に従います。

1. **[AudienceStream] > [Visitor/Visit Attributes]** に移動して [**Add Attribute**] をクリックします。
2. スコープとして [**Visitor**] を選択して [**Continue**] をクリックします。
3. データ型として [**Number**] を選択して [**Continue**] をクリックします。
4. 属性名として「Lifetime Order Value」を入力します。
5. [**Add Enrichmentを**] をクリックし、[**Increment or Decrement Number**] を選択します。
6. インクリメントする値を含む属性を選択する（`order_total` ）。
7. [WHEN] は [Any Event] のままにしておき、[**Create a New Rule**] をクリックします。
8. 購入イベントがいつ発生したかを識別するルールを作成する。
9. [**Save**] をクリックし、[**Finish**] をクリッします。

これで、すべての顧客に生涯注文額属性が関連付けられます。

{% endtab %}
{% tab バッジ %}

バッジを作成することで、ユーザーが共有する特定の属性によってユーザーを分類し、ターゲットを絞ることができる。次の例では、「Lifetime Order Value」が$500を超えるユーザーに対して VIP バッジを作成します。

1. **[AudienceStream] > [Visitor/Visit Attributes]** に移動して [**Add Attribute**] をクリックします。
2. スコープとして [**Visitor**] を選択して [**Continue**] をクリックします。
3. データ型として [**Badge**] を選択して [**Continue**] をクリックします。
4. バッジの名前「VIP」を入力する。
5. [**Add Enrichment**] をクリックし、[**Assign Badge**] を選択します。
6. WHEN "は "Any Event "のままにしておく。
7. [**Create Rule**] を選択して、バッジ割り当てのルールを作成します。このルールにタイトルを割り当て、前回作成した属性を使用して、ルールを「...属性 "Lifetime Order Value greater than 500 "を持つ」と設定する。
8. [**Save**] をクリックし、[**Finish**] をクリックします。

{% endtab %}
{% endtabs %}

### ステップ2:オーディエンスを作成する

Tealium のホームページから、サイドバーナビゲーションの [**AudienceStream**] の [**Audiences**] を選択します。ここでは、共通の属性を持つユーザーのオーディエンスを作成できます。このオーディエンスへのユーザーの出入りが、次のステップで設定する Connector Action のトリガーとなり、この情報が Braze のユーザープロファイルに渡されます。 

まず、オーディエンスに名前を付けてから、作成するオーディエンスのタイプに適用する属性を検討します。たとえば VIP ユーザーのオーディエンスを作成するには、**VIP バッジ**を持つ訪問者のオーディエンスを作成することができます。

終了したら、オーディエンスを必ず**保存 / 公開**してください。

### ステップ3:イベントコネクターを作成する

コネクターとは、Tealium と他のベンダーの間でデータを伝送するために使用される統合です。これらのコネクターには、パートナーがサポートするAPIを表すアクションが含まれている。 

1. Tealium のサイドバーの [**Server-Side**] から **[AudienceStream] > [Audience Connectors]** に移動します。
2. 青色の [**＋Add Connector**] ボタンを選択して、コネクターマーケットプレースを参照します。アプリが耳にする新しいダイアログボックスで、スポットライト検索を使用して**Braze** コネクターを見つけます。
3. このコネクターを追加するには、**Braze**コネクタータイルを選択します。クリックすると、接続の概要と、必要な情報、サポートされているアクション、設定手順のリストが表示される。この設定は、ソース、設定、アクションの3つのステップで構成されています。

#### ソース

表示される**Source**ダイアログで、前のステップで作成したオーディエンスと、状況に適していると思われるトリガーを選択する。また、このアクションのトリガーの頻度を制御するためにフリークエンシーキャップをオンに切り替えることもできます。 

![]({% image_buster /assets/img/tealium/create_source.png %}){: style="max-width:90%;"}

#### 構成

次に、**設定**ダイアログが表示される。ページ下部の [**Add Connector**] を選択します。コネクタに名前を付け、Braze APIエンドポイントとBraze REST APIキーをここに入力する。

![]({% image_buster /assets/img/tealium/create_configuration.png %}){: style="max-width:70%;"}

以前にコネクターを作成したことがある場合は、利用可能なコネクターのリストにある既存のコネクターを使用し、鉛筆アイコンでニーズに合わせて変更するか、ゴミ箱アイコンでコネクターを削除することができます。 

このオーディエンスをリンクするコネクターを作成または選択したら、[Done] をクリックして続行します。

#### アクション (Action)

次に、コネクターアクションに名前を付け、設定したマッピングに従ってデータを送信するアクションタイプを選択する。ここでは、Brazeの属性をTealiumの属性名にマッピングする。選択するアクションタイプに応じて、Tealium で必要となるフィールドは異なります。以下は、これらのフィールドの例と説明である。

{% alert important %}
提供されるすべてのフィールドが必要なわけではありません。

![]({% image_buster /assets/img/tealium/minimize.gif %}){: style="max-width:90%"}
{% endalert %}

{% tabs local %}
{% tab ユーザーの追跡 (バッチと非バッチ) %}

このアクションを使用すると、ユーザー、イベント、購入属性をすべて1回のアクションで追跡できます。Track User アクションは AudienceStream と EventStream の両方で同じですが、Tealium はAudienceStream アクションでユーザー属性のマッピングを設定し、EventStream アクションでイベントと購入のマッピングを設定することを推奨しています。

| パラメーター | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、Tealium のユーザー ID フィールドを Braze の対応するフィールドにマッピングします。1 つ以上のユーザー ID 属性をマップします。複数のID が指定されている場合、最初の非ブランク値は、次の優先順位に基づいて選択されます。External ID、Braze ID、エイリアス名、エイリアスラベル。<br><br>\- プッシュトークンs をインポートする場合は、外部ID とBraze ID を指定しないでください。<br>\- ユーザーエイリアスを指定する場合、エイリアス名とエイリアスラベルの両方を設定する必要があります。<br><br>詳細については、Braze[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) を参照してください。 |
| ユーザ属性 | 既存の Braze のユーザープロファイルのフィールド名を使用して、Braze ダッシュボードのユーザープロファイル値を更新するか、独自のカスタム[ユーザー属性]({{site.baseurl}}/api/objects_filters/user_attributes_object/)データをユーザープロファイルに追加します。<br><br>\- デフォルトでは、新規ユーザーが存在しない場合は作成されます。<br>\- 設定では、** 更新 Existing Only** to `true` で、存在するユーザーs のみが更新d になり、新しいユーザーは作成されません。<br>\- Tealium 属性が空の場合、その属性は NULL に変換され、Braze ユーザープロファイルから削除されます。ユーザー属性を削除する目的で Braze に NULL 値を送信すべきでない場合は、エンリッチメントを使用してください。 |
| Modify user attributes | このフィールドを使用して、特定のユーザー 属性を増減します<br><br>\- 整数属性は、正の整数または負の整数でインクリメントできます。<br>\- 配列属性s は、既存の配列に数値を追加または削除することで修正できます。 |
| イベント | イベントは、タイムスタンプの時点で特定のユーザーによりカスタムイベントが1回発生したことを表します。このフィールドは、Braze [イベントオブジェクト]({{site.baseurl}}/api/objects_filters/event_object/)の属性と同様にイベント属性を追跡、マッピングする場合に使用します。<br><br>\- イベント属性 `Name` は、マッピングされたすべてのイベントで必要です。<br>\- イベント属性 `Time` は、明示的にマッピングされていない限り、自動的に現時点の時刻に設定されます。<br>\- デフォルトでは、新しいイベントは存在しない場合に作成されます。`Update Existing Only` を`true` に設定すると、既存のイベントのみが更新され、新規のイベントは作成されません。<br>\- 配列型属性s をマップして、複数のイベントを追加します。配列型の属性s は等しい長さでなければなりません。<br>\- 単一値属性を使用できます。単一値属性は各イベントに適用できます。 |
| Event template | ボディデータで参照するイベントテンプレートを指定します。テンプレートを使用してデータを変換してから、Brazeに送信できます。詳細については、Tealiumの[テンプレートガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)を参照してください。 |
| Event template variable | イベントテンプレート変数をデータ入力として指定します。詳細については、Tealiumの[テンプレート変数ガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)を参照してください。 |
| 購入 | このフィールドは、Braze [購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)の属性と同様に購入属性を追跡、マッピングする場合に使用します。<br><br>\- 購入属性 `Product ID`、`Currency`、`Price` は、マッピングされたすべての購入に必要です。<br>\- 購入属性 `Time` は、明示的にマッピングされていない限り、自動的に現時点の時刻に設定されます。<br>\- デフォルトでは、新規購入が存在しない場合は作成されます。`Update Existing Only` を`true` に設定すると、既存の購入のみが更新され、新規購入は作成されません。<br>\- 配列型属性s をマップして、複数の購入アイテムを追加します。配列型の属性s は等しい長さでなければなりません。<br>\- 単一値属性を使用できます。単一値属性は各アイテムに適用されます。|
| 購買テンプレート | テンプレートを使用して、Brazeに送信する前にデータを変換できます。<br>\- ネストされたオブジェクトサポートが必要な場合は、購入テンプレートを定義します。<br>\- 購入テンプレートを定義すると、アクションの購入セクションで設定された設定は無視されます。<br>\- 詳細については、Tealiumの[テンプレートガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/trimou-templating-engine/)を参照してください。|
| 購買テンプレート変数 | 商品テンプレートの項目を入力します。詳細については、Tealiumの[テンプレート変数ガイド](https://docs.tealium.com/server-side/connectors/webhook-connectors/template-variables/)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_example2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab ユーザーの削除 - 非バッチ %}

このアクションでは、Braze ダッシュボードからユーザーを削除できます。

| パラメータ | 説明 |
| ---------- | ----------- |
| ユーザー ID | このフィールドを使用して、TealiumユーザーIDフィールドとBrazeユーザーIDフィールドを対応させる。<br><br>\- 1つ以上のユーザーID属性をマップする。複数のID が指定されている場合、最初の非ブランク値は、次の優先順位に基づいて選択されます。External ID、Braze ID、エイリアス名、エイリアスラベル。<br>\- ユーザーエイリアスを指定する場合、エイリアス名とエイリアスラベルの両方を設定する必要があります。<br><br>詳細については、Braze[`/users/delete` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/track_user_delete2.png %}){: style="max-width:90%"}

{% endtab %}
{% tab ユーザーサブスクリプショングループステータスの更新 - 非バッチ %}
この操作により、Braze SMSまたはEメール購読グループからユーザーを追加または削除することができる。

| パラメーター | 説明 |
| ---------- | ----------- |
| Group type | このフィールドを使用して、SMS購読グループかEメール購読グループかを示す。 |
| 更新タイプ | このアクションを購読解除または購読イベントにマッピングする 
| 属性 | \- Subscription group ID (required):前のフィールドでマップされたグループタイプに関連するサブスクリプショングループのID。<br>\- 外部ID：ユーザーの外部ID。<br><br>メールグループ固有:<br>\- Email:ユーザーのEメールアドレス。<br>**external ID が定義されていない場合はメールが必須です。**<br><br>SMS グループ固有:<br>\- Phone:E.164 形式の電話番号。 +14155552671 などです。<br>**external ID が定義されていない場合は電話番号が必須です。** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![]({% image_buster /assets/img/tealium/update_subscription.png %}){: style="max-width:90%"}

{% endtab %}
{% endtabs %}

[**Finish**] を選択します。

#### まとめ

作成したコネクタの概要を表示する。選択したオプションを変更する場合は、[**Back**] を選択して編集するか、[**Finish**] を選択して完了します。

コネクターが Tealium ホームページのコネクターリストに表示されます。

終了したら、必ずコネクタを保存するかパブリッシュすること。設定したアクションは、トリガー接続が満たされたときに実行されます。 

### ステップ4:Tealium コネクターをテストする

コネクターが稼動したら、正常に動作していることを確認するため、コネクターをテストする必要があります。最も簡単なテスト方法は、Tealium **Trace ツール**を使用する方法です。Traceを使い始めるには、Tealium Toolsブラウザ拡張機能を追加していることを確認する。

1. 新しいトレースを開始するには、サイドバーの [**Server-Side**] のオプションから [**Trace**] を選択します。[**Start**] をクリックし、トレース ID をキャプチャします。
2. ブラウザー拡張機能を開き、AudienceStream Trace にトレース ID を入力します。
3. リアルタイムログを調べます。
4. 展開する **Actions Triggered** エントリをクリックして、検証するアクションを確認します。
5. 検証するアクションを探して、ログステータスを表示します。 

Tealium の [Trace ツールの詳しい実装手順については、Tealium の [Trace ドキュメント](https://docs.tealium.com/server-side/connectors/trace/about/)を参照してください。

## 統合デモ

<div class="video-container">
  <iframe width="560" height="315" src="https://drive.google.com/file/d/1m2JI4vdFt3fDePBdVvVcQWEjbC82ApGA/preview" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</div>

## 潜在データポイント 超過料金s

Tealium から Braze を統合するときに、誤ってデータ超過料金が生じる主な状況が3つあります。

#### 重複したデータを送信する - 属性のBraze差分のみを送信する
Tealiumはユーザー属性のBrazeデルタを送信しない。例えば、ユーザーのファーストネーム、Eメール、携帯電話番号を追跡するEventStreamアクションがある場合、Tealiumはアクションがトリガーされるたびに、3つの属性すべてをBrazeに送信する。Tealium は、変更された内容や更新された内容を探してその情報のみを送信することはありません。<br><br> 
**解決策**:<br>バックエンドを確認して、属性が変更されているかどうかを評価し、変更されている場合は、Tealium の関連メソッドを呼び出してユーザープロファイルを更新できます。**これは、Braze を直接統合するユーザーが通常行う作業です。**<br>**または**<br> 自分自身のユーザープロファイルをバックエンドに保存しておらず、属性が変更されたかどうかを判断できない場合は、AudienceStream を使用して[リッチメントを作成し](https://docs.tealium.com/server-side/attributes/manage-enrichments/add-enrichment/)、値が変更された場合にのみユーザー属性を送信するようにできます。 

#### 無関係なデータを送信したり、不必要にデータを上書きしたりする。
同じイベントフィードをターゲットとする複数の EventStream がある場合、1つのアクションがトリガーされるたびに、**そのコネクターで有効になっているすべてのアクション**が自動的に起動します。**その結果、Braze でデータが上書きされる可能性があります。**<br><br>
**解決策**:<br>それぞれのアクションを追跡するために、個別のイベント指定またはフィードを設定します。<br>**または**<br> Tealium ダッシュボードのトグルを使用して、起動しないアクション (またはコネクター) を無効にします。

#### Brazeの初期化が早すぎる
Braze Web SDK タグを使用して Tealium と統合するユーザーの場合、MAU が大幅に増加する可能性があります。**Braze がページ読み込むで初期化されている場合、Web ユーザーが初めてWeb サイトに移動するたびに、Braze によって匿名プロファイルが作成されます。**ユーザーが"Signed In"または"Watched Video"など、いくつかのアクションを完了したときにのみ、MAU数を減らすためにユーザーの挙動を追跡することを望む人もいるかもしれません。<br><br>
**解決策**:<br>[ 読み込む規則](https://docs.tealium.com/iq-tag-management/load-rules/about/) を設定して、タグ 読み込むがいつどこにあるかを正確に判断します。

