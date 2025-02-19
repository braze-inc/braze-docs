---
nav_title: アクションパス 
article_title: アクションパス 
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "この記事では、行動に基づいてユーザーを並べ替えることができるコンポーネント、アクションパスの使い方を説明します。"
tool: Canvas
---

# アクションパス 

> キャンバスのアクションパスでは、ユーザーをそのアクションに基づいて並べ替えることができます。 

アクションパスを使用して、次のことを行えます。

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}

* ユーザーエンゲージメントイベントやカスタムイベントなど、特定のアクションに基づいてユーザーパスをカスタマイズする。
* 指定期間中、ユーザーを保持し、この評価期間中のユーザーのアクションに基づいて、ユーザーの次のパスに優先順位を付ける。

## アクションパスを作成する

アクションパスを作成するには、キャンバスにコンポーネントを追加します。サイドバーからコンポーネントをドラッグアンドドロップするか、ステップの下部にある<i class="fas fa-plus-circle"></i> プラスボタンを選択し、**Action Paths** を選択します。 

### アクション設定

**Action Settings**で、**Evaluation Window**を設定して、ユーザーがステップに保持される期間を決定します。デフォルトでは、ユーザーが 1 日以内に評価されますが、キャンバスに応じて、この時間枠を秒、分、時間、日、週単位で調整できます。アクションパスの大評価期間は31 日間です。

[**アクション設定**] で、[**ランクに基づいてユーザーを先に進める**] トグルをオンにすることで、コンポーネントのランク付けされた順序をオンにすることもできます。

![][4]

デフォルトでは、**ランク**がオフになっています。ユーザーがアクションパスに入り、いずれかのアクショングループに付属するトリガーイベントを実行すると、即座に関連するアクショングループに進みます。ユーザーがトリガーイベントを実行しなかった場合、評価期間の終了時にデフォルトの [**その他のユーザー**] グループに進むことになります。

[**ランクに基づいてユーザーを先に進める**] が有効になっている場合、**ランク**がオンになっています。そのため、評価時間枠が終了するまですべてのユーザーがここに留まります。評価期間が終了した時点で、ユーザーは、評価時間枠の終了時点で対象となる最も優先順位の高いアクショングループに進みます。評価時間枠の間にどのアクションも実行しなかったユーザーは、デフォルトの [**その他のユーザー**] グループのパスを進みます。

#### アプリ内メッセージ

アクショングループのトリガーがセッションの開始であり、次のステップがアプリ内メッセージである場合、アプリ内メッセージを受け取るために、ユーザーはセッションを 2 回開始する必要があることに注意してください。最初のセッションはアクションパス内のアクショングループにユーザーを割り当て、2 番目のセッションがアプリ内メッセージをトリガーします。

#### ランクステータスの例

ここでは評価期間が 1 日で、行動グループが 2 つあるアクションパスを想定し、これをグループ 1 とグループ 2 とします。グループ 1 には「セッションを開始」というトリガーイベントがあり、グループ 2 には「購入」というトリガーイベントがあります。**ランク**がオンになっている場合、アクションパスに含まれるすべてのユーザーは 1 日間「保持」されます。1 日の終わりに、ユーザーがセッションを開始し、購入した場合、最高ランクのパスに進みます。ここではユーザーがグループ 1 に進みます。 

前述の例では、**ランク**がオフの場合、ユーザーがトリガーイベント (「セッションを開始」または「購入」) のいずれかを実行すると、そのユーザーはトリガーアクションに基づいて、関連するアクショングループに進みます。

キャンバスエントリのプロパティは、イベントのプロパティとは異なることに注意してください。キャンバスエントリのプロパティは、キャンバスをトリガーしたイベントのプロパティです。これらのプロパティは、元のキャンバスワークフローを使用する場合にキャンバスの最初のフルステップでのみ使用できます。キャンバスフローを使用する場合、永続エントリプロパティが有効になり、キャンバス全体でエントリプロパティを再利用できるようになります。逆に、イベントプロパティは、ユーザーがワークフローを進行する中で発生するイベントやアクションに由来しています。

### アクショングループ

1 つまたは複数のトリガーを追加して、アクショングループを定義します。ここでは、次のユーザー行動などのさまざまなトリガーを選択できます。

- 購入する
- セッションの起動
- [カスタムイベント]][2]の実行
- コンバージョンイベントの実行
- メール宛先を追加する
- カスタム属性を変更する
- サブスクリプション ステータスまたはサブスクリプショングループ ステータスをアップデートする
- キャンペーンまたはコンテンツカードとのやり取り
- 場所を入力
- ジオフェンスのトリガー
- SMSまたはWhatsApp受信メールを送信する

![][3]

各アクショングループの設定の中で、[**このグループにキャンバスを終了させる**] チェックボックスを選択するオプションもあります。このグループのユーザーは、評価期間終了時にキャンバスから退出します。

### 再適格性を伴うキャンバス

ユーザーが 1 つのアクションパスに複数回入り、同時に複数のエントリがアクションパスにある場合、期待される動作は**ランク**のステータスによって異なります。 

| ランキングステータス | アクションパスの動作 |
|---|--------------|
| **オフ** | 関連するアクションが実行されると、Braze はエントリーを重複排除し、関連するアクショングループを介して最も早いエントリをただちに進めます。<br><br/> 関連するアクションが実行されない場合、すべてのエントリを関連する評価ウィンドウの終了時に進めます。重複排除は発生しません。 |
| **オン** | 関連する評価期間の終了時に、すべてのエントリを進めます。重複排除は発生しません。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

なお、ランクを[開始後に編集]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/)することはできません。


[1]: {% image_buster /assets/img/canvas_actionpath.png %}
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events
[3]: {% image_buster /assets/img/actionpath_group.png %}
[4]: {% image_buster /assets/img/actionpath_settings.png %} 
