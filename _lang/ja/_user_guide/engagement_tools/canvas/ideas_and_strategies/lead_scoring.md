---
nav_title: リードスコアリング
article_title: リードスコアリングワークフローの作成
description: "Braze を使用してシンプルなリードスコアリング、外部リードスコアリング、リードハンドオフを実行する方法について説明します。"
---

# リードスコアリングワークフローの作成

> このユースケースでは、Braze を使用してリードスコアをリアルタイムで更新 ユーザーし、自動的に営業チームに引き継ぐ方法を示します。

Braze でリードスコアリングワークフローを作成するには、次の2 つの重要なステップがあります。

1. Braze でリードスコアキャンバスを作成するか、外部リードスコアツールを統合します。
- [単純なリードスコアリング](#simple-lead-scoring)
- [外部リードスコアリング](#external-lead-scoring)

2. 資格のあるリードをセールスチームに送信するWebhook キャンペーンを作成します。
- [リードハンドオフ:適格リード(MQL)の販売へのマーケティング](#lead-handoff)

## 単純なリードスコアリング

### ステップ 1:キャンバスを作成する

1. **Messaging**> **Canvas**に進み、**Create Canvas**を選択し、Canvasの基本を入力します。

2. キャンバスに「リードスコアリングキャンバス」などの関連する名前を付け、探しやすくするために、「リードマネジメント」などでタグします。<br><br>![「リードスコアリングキャンバス」という名前のキャンバスを作成し、「リードマネジメント」をタグする手順1。][1]{: style="max-width:80%;"}

### ステップ2:エントリ条件の設定

1. **エントリ スケジュール**ステップに進み、**Action-Based**エントリ スケジュールを選択します。特殊なアクションを実行すると、キャンバスにユーザーs が入力されます。

2. **アクション ベースのオプション** で、次の2 つのアクションs を追加します。
    - **カスタム属性値**をリードスコアリング属性の名前(`lead score`など)で変更します。リードスコアリング属性をまだ作成していない場合は、[カスタム属性s]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)のステップに従います。リードスコアが変更されるたびに、キャンバスにユーザーs が入力されます。
    - **電子メールアドレスの追加**

![カスタム属性の「リードスコア」を変更し、メールの住所を追加する「アクションベース」およびアクションベースの選択肢をエントリ スケジュールとしたキャンバスの作成手順2。][2]{: style="max-width:80%;"}

### ステップ 3:対象オーディエンスの特定

#### ステップ3a:Segment選択s

すべてのユーザー s はリードスコアリングの対象となる[Segment s]({{site.baseurl}}/user_guide/engagement_tools/segments/) を選択し、追加の[フィルター s]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/) をアプリすることで、誰をスコア化するかに関する会社固有の規則を追加できます。たとえば、従業員、すでに顧客s であるユーザーs などを除外できます。 

![Segments とフィルターs を選択してエントリ オーディエンスを絞り込むための選択肢を含むキャンバスを作成する手順3。][3]{: style="max-width:80%;"}

#### ステップ3b:キャンバスの再適格性の設定

ユーザーは、このキャンバスのライフサイクル全体を通して何度もこのキャンバスを通過するため、前回終了したときにすぐに再入力できることを確認します。これは、再適格設定sによって達成することができる。 

**エントリコントロール**で、以下を実行します。
- **ユーザー s がこのキャンバス** を再入力できるようにします。
- **指定ウィンドウ**を選択します。
- 再取得対象を"0"**秒**に設定します。

![「入力制御」セクションには、「ユーザーがこのキャンバスに再入力できるようにする」の選択肢があり、0 秒の「指定ウィンドウ」に表示されます。][4]{: style="max-width:80%;"}

#### ステップ3c:送信設定のアップデート

このキャンバスの運用上の性質と、これらのユーザーにはメッセージが送信されないことを考慮すると、サブスクリプション ステータスes に従う必要はありません。

**Subscription Settings**で、**これらのユーザーに送信s:**選択**配信停止を含むすべてのs s s**。 

![設定メール送信オプション用のキャンバスを作成する手順4。][5]{: style="max-width:80%;"}

### ステップ 4:キャンバスを作成する

#### ステップ4a:アクションパスの追加

バリアントでプラスアイコンを選択し、**アクションパス**を選択します。

![「アクションパス」がメニュー開封に表示されているキャンバスは、プラスアイコンで囲まれています。][6]{: style="max-width:60%;"}

#### ステップ4b:アクショングループの作成

それぞれのアクション群は、同じ点の増減につながるすべてのアクションs を表します。最大8 つのアクショングループを設定できます。この例では、4つのグループを設定します。

アクションパスに次のグループを追加します。

- **グループ1:**1 ポイントの増分でカウントするすべてのイベント。
- **グループ2:**5 ポイントの増分でカウントするすべてのイベント。
- **グループ 3:**1 ポイントのデクリメントでカウントするすべてのイベント。
- **その他の全員:**アクションパスを使用すると、待機ウィンドウを定義し、ユーザーがアクションを受け取るかどうかを確認してから、それらを「他のすべてのユーザー」グループにドロップできます。リードスコアリングの場合、これは「非アクティブ」のスコアを減らす機会です。

![1 ポイント、5 ポイン、および10 ポイントを追加するアクショングループ、1 ポイントと10 ポイントを減算するアクショングループ、および「Everyone Else」を含むアクションパス。][7]

#### ステップ4c:関連するイベントを含めるように各グループを設定する

それぞれのアクショングループで、**トリガー**を選択し、特定のアクショングループのポイント数を追加するイベントを選択します。リードスコアを1 つ増やすすべてのイベントを含めるには、トリガーs を追加します。たとえば、ユーザーは、任意のアプリでセッションを起動したり、カスタムイベント(ウェビナーの登録や参加など)を実行したりすると、得点を1つ増やすことができます。 

![「アプリでセッションを開始する」と「カスタムイベントを実行する」のトリガーでポイントを追加するアクショングループ。][8]{: style="max-width:80%;"}

#### ステップ4d:ユーザアップデートステップの追加

ユーザアップデートステップを、アクションパスの下に作成されたキャンバスパスに追加します。 

![キャンバスは、アクショングループごとに分岐したユーザアップデートパスs を持つアクションパスを表示します。][9]{: style="max-width:80%;"}

{: start=”2”}
ユーザアップデートステップの**Compose** タブで、それぞれのフィールドs に対して次の操作を行います。

| フィールド | アクション (Action) |
| --- | --- |
| **属性名** | ステップ 2 で選択したリードスコア属性を選択します(`lead score`)。|
| **アクション (Action)** | パスが得点を上げる場合は**増分**に、パスが得点を下げる場合は**減分**にアクションを変更します |
| **増分**または**減分** | リードスコアから増減するポイント数を入力します。|
{: .reset-td-br-1 .reset-td-br-2}

### ステップ 5: キャンバスを起動する

そうです!リードスコアリングキャンバスを起動する準備ができました。

## 外部リードスコアリング

当社の[テクノロジーパートナー s]({{site.baseurl}}/partners/home/)のいずれかを使用するか、独自の内部リードスコアリングモデル、マシンラーニング、または別のリードスコアリングツールを使用するかどうかに関わらず、当社には複数の選択肢があります。

### 外部パートナー

リードスコアリング機能を提供するB2Bパートナーについては、[Technology partners]({{site.baseurl}}/partners/home)を参照してください。そこにあなたの道具が見えませんか？[`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#track-users) API エンドポイントを呼び出すことで統合できます。 

### 内部リードスコアリングデータモデル

Brazeは、リードスコアリングモデルを含む内部データモデルとさまざまな方法で統合できます。顧客がBrazeとどのように統合されているかについては、以下を参照してください。

#### 統合クラウドデータウェアハウス

{% tabs %}
{% tab データソースとしてのBraze %}

マーケティングツールとして、Braze には、チームの内部リードスコアモデルを補完できる、非常に関連性の高いデータが含まれています。 

たとえば、メッセージング エンゲージメントデータ(メール 開封 s やクリック、ランディングページエンゲージメントなど) でリードのエンゲージメント順位を決定できます。このデータをクラウドデータウェアハウスに渡し、Brazeストリーミングエクスポートデータソリューションs を使用してリードスコアリングモデルの入力として使用できるようにすることができます。

- [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/)
- [Snowflake セキュアデータ共有]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/)

{% endtab %}
{% tab 送信先としてのBraze %}

内部チームがリードスコアリングモデルを作成して実行したら、そのデータをBraze にプルバックして、関連するメッセージングのリードをより適切にSegmentし、対象にすることができます。これは、[ Braze クラウドデータインジェスト]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/overview/) を使用して実行できます。 

クラウドデータ取り込みでは、内部チームは、ユーザー 識別子s、最新のリードスコア、スコアが更新dのときのタイムスタンプを含む新しいテーブルまたはビューを作成します。Braze はテーブルまたはビューを選択し、リードスコアをユーザープロファイルs に追加します。

{% endtab %}
{% endtabs %}

## リードハンドオフ:適格リード(MQL)の販売へのマーケティング {#lead-handoff}

リードハンドオフへのアプリのおすすめは、それぞれのユーザーに対応するリードまたはコンタクトをBrazeに取り付けることです。これらのリードは、リードステータスがMQL s タグe に変更されたときに営業チームのキューに入ります。この時点で、Salesforce はリードルーティングまたは割り当てワークフローを開始します。 

Braze のリードステータスを使用してSalesforce のリードレコードを更新するには、トリガーのWebhook テンプレートを使用することをお勧めします。

### ステップ 1:Webhook キャンペーンの作成

### ステップ2:Webhookの設定

#### ステップ 2a: Webhook作成

1. Webhook キャンペーンに「Salesforce > MQL へのリードの更新」などの名前を付けます。

2. Webhook URL を{% raw %}`https://YOUR_SALESFORCE_INSTANCE.my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} の形式で入力します。{% raw %}`{{$user_id}}}`{% endraw %} のBraze ユーザー IDは、Salesforce の連絡先ID に一致する必要があります。そうでない場合は、{% raw %}`{{$user_id}}}`{% endraw %} の代わりにエイリアスを使用します。

3. **HTTP Method** を**PATCH** に更新します。

4. リードのリードスコアが事前定義されたしきい値を超えた場合にのみ、Salesforce のリードレコードを更新するように有料読み込むを設定します。リードスコアが100 を超える場合は、以下のリクエストボディの例を参照してください。

{% raw %}
```liquid
{% assign threshold = 100%}
{% if custom_attribute.${lead score} > threshold %}
{
"lead_status": "MQL"
}
{% else %}{% abort_message('not at threshold')%}
{% endif %}
```
{% endraw %}

{: start="5"}
5. 次のヘッダーを含めます。

| ヘッダー | コンテンツ |
| --- | --- |
| 許可 | {% raw %}`Bearer {{result.access_token}}`{% endraw %}<br><br>トークンを取得するには、[OAuth 2.0 クライアント 認証情報 s フローの接続アプリ](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5) を設定し、Connected Content を使用してSalesforce からベアラを取得します。<br><br>{% raw %}<code>{% connected_content <mem_9233bdf7-6615-4c4d-beab-4b4392a219c5/>[instance].my.salesforce.com/services/oauth2/token <br>:method post <br> :body client_id=[client_id]_mem_amp_client_secret=[client_secret]_mem_amp_grant_type=client_credentials <br>:save result %}{% endraw %} <br> Bearer {% raw %}{{result.access_token}}</code>{% endraw %} |
| Content_Type | application/json |
{: .reset-td-br-1 reset-td-br-2}

![Salesforce Webhook URL、PATCH HTTP メソッド、未加工のテキストリクエストボディ、およびリクエストヘッダーs で構成されるWebhook。][10]{: style="max-width:80%;"}

#### ステップ 2b: Webhook送信を予約する

キャンペーンは、ユーザーのリードスコアが変更されるたびにトリガーする必要があります。このキャンペーンは、スコアが変更されたユーザーをトリガーしますが、現在MQLではなく、前のステップで設定したしきい値を超えたユーザーにのみ影響します。

**Schedule Delivery**ステップで、以下を選択します。
- **Action-Based**配信タイプ
- **Change Custom 属性 Value**のトリガー アクションで、リードスコアリング属性の名前と**新しい値**のアクションを指定します。

#### ステップ 2c: 対象オーディエンスの特定

**Target Audiences**ステップには、"`lead_status``is none of``MQL`"のように、リードステータスがすでにMQL以上にあるユーザーsを除外するフィルターを含めます。

![「lead_ステータス」のフィルターを持つWebフックターゲティングオプションは、「MQL」のいずれでもありません。][11]{: style="max-width:80%;"}

### ステップ 3:起動キャンペーン

**Launch** を選択し、顧客がMQL リードスコアしきい値を超えたときに、Salesforce でリードステータスの変更を監視します。

[1]: {% image_buster /assets/img/b2b/step_1_simple.png %}
[2]: {% image_buster /assets/img/b2b/step_2_simple.png %}
[3]: {% image_buster /assets/img/b2b/step_3_simple.png %}
[4]: {% image_buster /assets/img/b2b/entry_controls_simple.png %}
[5]: {% image_buster /assets/img/b2b/step_4_simple.png %}
[6]: {% image_buster /assets/img/b2b/action_paths_simple.png %}
[7]: {% image_buster /assets/img/b2b/action_paths_selected_simple.png %}
[8]: {% image_buster /assets/img/b2b/action_groups_simple.png %}
[9]: {% image_buster /assets/img/b2b/user_update_paths_simple.png %}
[10]: {% image_buster /assets/img/b2b/webhook.png %}
[11]: {% image_buster /assets/img/b2b/step_3_webhook.png %}