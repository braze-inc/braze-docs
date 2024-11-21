---
nav_title: 機能採用
article_title: 機能採用
page_order: 3
page_type: reference
description: "この記事では、Braze Canvas テンプレートを使用して、適時にカスタマイズされたメッセージを配信し、利点と使用上のヒントを強調する方法について説明します。"
tool: Canvas
---

# 機能の採用

> このテンプレートは、新しい機能、既存の製品、追加のオファリング、またはお客様が体験したい他の領域の使用を促進するように設計されています。パーソナライズされたコミュニケーションと構造化された一連のメッセージを活用することで、ユーザーに新しい機能をシームレスに導入し、ユーザーから貴重なフィードバックを得ることができます。 

この記事では、**Feature Adoption**テンプレートのユースケースについて説明します。これは、ユーザライフサイクルの保持とロイヤルティステージを対象としています。この記事の後、ユーザーに新しい機能の使用を促し、ユーザーセンチメントを収集するユーザージャーニーをカスタマイズします。

## 前提条件

このテンプレートを正常に使用するには、ユーザーがこの機能を使用したときに参照する[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events) が必要です。

## 必要に応じてテンプレートをカスタマイズする

食品配送アプリのカロリー・ロケットで働いているとしよう。カロリー・ロケットは、最近クルーズ・コントロールをローンチした。クルーズ・コントロールは食料配送を繰り返しスケジュールする機能で、より多くのユーザーにこの新機能を採用するよう促したいと思っている。この例では、カスタムイベント`scheduled_delivery` を使用して、ユーザーがいつクルーズコントロール機能を試行したかを追跡します。

バックインストックテンプレートにアクセスするには、新しいキャンバスを作成するときに、**キャンバステンプレートを使用**> **ブレーズテンプレート**を選択します。次に、**Feature Adoption**の横にある**Apply Template**を選択します。これで、テンプレートを使用してニーズに合わせることができます。

### ステップ 1: 詳細を設定する

キャンバスの詳細を調整して、目標を反映しましょう。

1. テンプレート名の横にある**編集**を選択します。

![Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/select_edit_details.png %})の現在のタイトルと説明{: style="max-width:60%;"}

{:start="2"}
2\.キャンバス名を更新して、ユーザフィードバックを収集するターゲットユーザにキャンバスがあることを指定します。
3\.説明を更新して、ユーザがフィードバックを送信し、新しいクルーズコントロール機能のユーザセンチメントを追跡するようにキャンバスを指定します。
4. タグ**Feature approduction** を追加して、Canvas ホームページでフィルタリングできるようにします。

![キャンバスの新しい名前と説明。新しい説明では、次のように記述されます。'クルーズコントロールの採用とユーザーセンチメントを追跡するための機能採用キャンバス、繰り返しの食品配送をスケジュールする機能']({% image_buster /assets/img/canvas_templates/feature_adoption/enter_new_canvas_name.png %}){: style="max-width:60%;"}

### ステップ 2: 変換イベントの割り当て

次に、Canvas の変換イベントを追加して、フィーチャーの採用を通知します。これにより、後でユーザーの旅行でExperiment Path を調整することができます。

1. **Assign Conversion Events**の下で、**Add Conversion Event**を選択します。
2. **Primary Conversion Event - A** の下で、**Custom Event** を**Conversion event type** として選択します。
3. カスタムイベント`scheduled_delivery` を選択します。
4. 変換期限は3日間とします。

![Canvas.]({% image_buster /assets/img/canvas_templates/feature_adoption/assign_conversion_event_cruise_control.png %})の変換イベントウィンドウ{: style="max-width:90%;"}

### ステップ 3:入力スケジュールを調整する

私たちの目標は、ユーザーにクルーズコントロールを採用するよう促すことですが、私たちのメッセージをあまり頻繁にすることは望ましくありません。そのため、このキャンバスをスケジュールされた配信として保存し、**Time-Based Options** セクションに対して次の調整を行います。

1. **入力頻度**を**Weekly**に更新します。
2. 再発はそのままにしておきなさい。
3. **Mon**を選択すると、週の初めにユーザーをターゲットにします。
4. キャンバスの開始時間を選択します。
5. **終了パラメータ**を更新して、1年の最後の日にキャンバスを終了します。

ユーザーがローカルタイムゾーンでキャンバスに入ることを許可するオプションを保持します。

### ステップ4:対象者を選択

次に、テンプレートで以下の詳細を更新して、ターゲットオーディエンスを設定します。

1. **All Users**セグメントを選択します。
2. テンプレートの追加フィルタを削除します。 
3. カスタムイベント`Has scheduled_delivery for exactly 0 times` を使用してこのフィルタを作成します。これにより、この機能をすでに使用しているユーザーをキャンバスに入ることができなくなります。

![Cruise Control.]({% image_buster /assets/img/canvas_templates/feature_adoption/cruise_control_segment.png %})を使用していないすべてのユーザーのセグメント{: style="max-width:90%;"}

{: start="4"}
4. Calorie Rocket では、数人のユーザーが新しい機能の Cruise Control をベータテストできるようになっています。ここでは、これらのユーザーが Canvas に入らないように出口条件を更新します。

### ステップ 5: 送信設定を選択する

デフォルトのサブスクリプション設定を維持するため、メッセージまたは通知の受信をサブスクライブまたはオプトインしたユーザーにのみ送信し、その他の設定(頻度の上限、静かな時間、シードグループ)はスキップします。

### ステップ 6:キャンバスをカスタマイズする

#### アクションパスの構築

次に、最初のアクションパスステップを作成してみましょう。これは、ユーザーが新しい機能に関心を持っているかどうかを示すためのものです。テンプレートに以下の調整を行います。

1. クルーズコントロール機能は、注文がカートに追加された後でのみ使用可能であるため、最初のアクショングループに名前を付け**カート**に追加し、カスタムイベントに`added_to_cart`を選択します。

![&quot に設定されたアクショングループ名;cart&quot に追加;および"Perform Custom Event" set to "add_to_cart".]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_added_to_cart.png %}){: style="max-width:60%;"}

{: start="2"}
2\.2 番目のアクショングループ**Taken Tour** はそのままにしておきます。ユーザーがアプリをツアーしたかどうかを評価し、アプリがあれば2 番目のパスに進みます。
3\.後続のアクションパス**Asses Usage**については、**Used Feature >3x**を**Viewed Cruise Control settings**に置き換えます。
4. **Perform Custom Event** ドロップダウンを選択し、カスタムイベントの`scheduled_delivery` を選択します。

![アクショングループ名は「Used Feature >3x」に設定され、「Perform Custom Event」は「scheduled_delivery」に設定されます。]({% image_buster /assets/img/canvas_templates/feature_adoption/action_path_assess_usage.png %}){: style="max-width:60%;"}

#### フィードバック調査の設定

次に、**Feedback Survey**という名前のMessageステップに進み、初めてCruise Controlを使用した後にユーザーが記入するためのフィードバック調査を含めます。私たちのアンケート回答の選択肢は次のとおりです。

- **大好きでした!**
- **私のためではありません。**

1. 2 つのサーベイの選択肢については、カスタム属性として**Experience Feedback** を選択し、クルーズコントロールのフィードバックをキャプチャして追跡します。このカスタム属性には、調査回答を表す2 つの値があります(`good` および`bad`)。
2. 調査オプションに一致するように属性値を更新します。これにより、ユーザーの応答を追跡できます。

### ステップ 7:キャンバスをテストして起動する

キャンバスをテストして確認し、正常に動作することを確認したら、**Launch Canvas** を選択してキャンバスを起動します。これで、パーソナライズされたユーザジャーニーを持つユーザをターゲットにして、新しい機能のクルーズコントロールを採用するように促すことができます。

{% alert tip %}
キャンバスを起動する前と後に考慮すべき事柄については、[起動前と起動後のチェックリスト]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch)を参照してください。
{% endalert %}
