---
nav_title: キャンバスの作成
article_title: キャンバスの作成
page_order: 0
page_type: reference
description: "この記事では、キャンバスの作成、維持、およびテストに必要な手順について説明します。"
tool: Canvas
search_rank: 1
---

# キャンバスの作成

> この記事では、キャンバスの作成、維持、およびテストに必要な手順について説明します。このガイドに従うか、[キャンバスの Braze ラーニングコース](https://learning.braze.com/quick-overview-canvas-setup)をご覧ください。

{% details Original Canvas editor %}
元のキャンバスエクスペリエンスを使用して、キャンバスを作成または複製することはできなくなりました。Brazeでは、[Currentsを]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)最新のエディタに[複製する]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)ことを推奨している。
{% enddetails %}

## キャンバスの作成

### ステップ 1: 新しいキャンバスを設定する 

まず、**メッセージング**> **キャンバス**に移動し、次に**キャンバスの作成**を選択します。

キャンバスビルダーは、命名からコンバージョンイベントを設定して適切なユーザーをカスタマージャーニーに導くまでのキャンバスの設定プロセスを、ステップごとに順を追って案内します。以下の各タブをクリックして、ビルダーの各ステップで調整できる設定を確認してください。

{% tabs local %}
  {% tab Basics %}
    ここでは、キャンバスの基本情報を設定します。
    \- キャンバスに名前を付ける
    \- チームを追加する
    \- タグを追加する
    \- コンバージョンイベントを割り当て、イベントタイプと期限を選択する

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab Entry Schedule %}
    ここで、ユーザーがキャンバスに入る方法とタイミングを決める：
    \- スケジュール: これは時間ベースのキャンバスエントリです。
    \- アクションベース: ユーザーは定義されたアクションを実行した後、キャンバスに入ります。
    \- API トリガー: API リクエストを使用してキャンバスにユーザーを入れます。

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab Target Audience %}
    ここでは、ターゲットオーディエンスを選択します。
    \- セグメントとフィルターを追加してオーディエンスを作成する
    \- キャンバスの再エントリとエントリ制限を微調整する
    \- ターゲットオーディエンスの要約を見る

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab Send Settings %}
    ここでは、キャンバスの送信設定を選択します。
    \- サブスクリプションの設定を選択する
    \- キャンバスメッセージの送信レート制限を設定する
    \- サイレント時間の有効化と設定を行う

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab Build Canvas %}
    ここでは、キャンバスを作成します。

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab Summary %}
    ここでは、キャンバスの詳細のまとめが表示されます。[キャンバスの承認ワークフロー]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/)をオンにしている場合は、一覧されたキャンバスの詳細を承認してからキャンバスを開始することができます。

  {% endtab %}
{% endtabs %}

#### ステップ1.1：キャンバスの基本情報から始める

ここでは、キャンバスに名前を付け、[チーム]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams)を割り当て、[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags)を作成または追加します。キャンバスのコンバージョンイベントを割り当てることもできます。

{% alert tip %}
キャンバスにタグを付けることで、検索とレポートの作成が簡単に行えるようになります。例えば、[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)を使用する場合、特定のタグでフィルタリングできます。
{% endalert %}

![キャンバスの詳細ページ。キャンバス名、説明、場所、タグのフィールドがある。]({% image_buster /assets/img/canvas_details.png %}){: style="max-width:70%;"}

##### コンバージョンイベントを選択する

コンバージョンイベントのタイプを選択し、記録するコンバージョンを選択します。これらの[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)によって、キャンバスの効果を測定します。 

![「購入」のイベントタイプを持つ 1 次コンバージョンイベント A。3 日間のコンバージョン期限内に何かを購入したユーザーとの会話を記録します。]({% image_buster /assets/img/add_canvas_conversions.png %})

キャンバスに複数のバリアントやコントロールグループがある場合、Braze はこのコンバージョンイベントを使用して、このコンバージョン目標を達成するための最適なバリアントを決定します。同じロジックを使用して、複数のコンバージョンイベントを作成できます。

#### ステップ1.2：キャンバスのエントリスケジュールを決める

ユーザーがキャンバスに入ることのできる 3 つの方法のいずれかを選択できます。 

##### エントリスケジュールのタイプ

{% tabs local %}
  {% tab Scheduled Delivery %}
    スケジュールされた配信では、ユーザーのエントリが時間のスケジュールに従って決まります。これは、キャンペーンをスケジュールする方法と似ています。キャンバスを開始してすぐにユーザーを登録し、将来のある時点でジャーニーにエントリさせたり、定期的に (毎日、毎週、毎月など) エントリさせたりできます。 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2025 until December 31, 2025.

    ![The "Entry Schedule" page with the type set to "Scheduled". Due to the selection, time-based options are shown, including frequency, start time, recurrence, days, and more.]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab Action-Based Delivery %}
    アクションベースの配信では、ユーザーはキャンバスに入り、アプリを開いたり、購入したり、カスタムイベントをトリガーしたりといった特定のアクションを行った後、メッセージを受け取り始めます。

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2025.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API-Triggered Delivery %}
    API トリガー配信では、ユーザーがキャンバスに入り、API 経由で [`/canvas/trigger/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)を使用してメッセージが追加されると、メッセージを受け取り始めます。ダッシュボードには、これを行い、[キャンバスエントリのプロパティオブジェクト]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)を使用してオプションの [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) も割り当てる、cURL リクエストの例があります。 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

配信方法を選択したら、ユースケースに合わせて設定を調整し、続いてターゲットオーディエンスを設定します。

{% details Deduplicate behavior for Canvases using the original editor %}
再適格性の期間がキャンバスの最大継続時間よりも短い場合、ユーザーに再エントリが許可され、複数のコンポーネントメッセージを受信することが可能です。ユーザーの再エントリが前のエントリと同じコンポーネントに到達したエッジケースでは、Braze がそのコンポーネントのメッセージの重複を除外します。 

キャンバスに再エントリし、前回のエントリと同じコンポーネントに到達したユーザーに、エントリごとにアプリ内メッセージを受け取る資格がある場合、セッションを 2 回再開封すれば、ユーザーは (アプリ内メッセージの優先度に応じて) メッセージを 2 回受け取る可能性があります。
{% enddetails %}

#### ステップ1.3：エントリのターゲットオーディエンスを設定する

つまり、Brazeは、ユーザーが**キャンバスジャーニーに**入る**前に、**まずターゲットオーディエンスの適格性を評価する。例えば、新規ユーザーをターゲットにしたい場合、初めてアプリを使用したのが1週間以内のユーザーをセグメントとして選択することができる。

**エントリコントロールでは**、キャンバスがスケジュールされるたびにユーザー数を制限することができる。APIトリガーベースおよびアクションベースのキャンバスでは、この制限はUTC時間ごとに発生する。 

{% alert important %}
オーディエンスフィルターと同じトリガー (属性の変更やカスタムイベントの実行など) でアクションベースのキャンペーンやキャンバスを設定しないでください。[競合条件が]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions)発生すると、ユーザーがトリガーイベントを実行した時点でオーディエンスにおらず、キャンペーンを受け取れなかったり、キャンバスに入れなかったりする。
{% endalert %}

##### オーディエンスのテスト

ターゲットオーディエンスにセグメントとフィルターを追加した後、[ユーザーを検索]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)してオーディエンス基準に一致しているかを確認することで、オーディエンスが期待どおりに設定されているかどうかをテストできます。

![外部ユーザーIDまたはBraze IDで検索できる「ユーザー検索」フィールド。]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:100%;"}{: style="max-width:80%;"}

##### エントリコントロールの選択

エントリコントロールは、ユーザーがキャンバスに再エントリできるかどうかを決定します。また、選択したケイデンス(毎日、キャンバスの寿命、またはキャンバスがスケジュールされるたびに)によってこのキャンバスに入る可能性のある人の数を制限することもできます。 

たとえば、**Limit entrance volume**を選択し、**Maximum entries**フィールドを、制限ケイデンスとして**Daily**を持つユーザー5000人に設定した場合、キャンバスは1日に5000人のユーザーにのみ送信します。

![[エントリーコントロール] ページに [ユーザーがこのキャンバスに再エントリできるようにする] および [エントリ数の制限] のチェックボックスが表示されます。後者では、エントリーの上限を設定し、毎日、キャンバスの有効期間中、またはキャンバスがスケジュールされるたびに制限するかどうかを設定できる。]({% image_buster /assets/img_archive/entry_controls.png %})

{% alert tip %}
Braze では、IP ウォームアップの目的で [**キャンバスがスケジュールされるごと**] 機能を使用することを推奨していません。これにより、送信量が増加する可能性があるためです。
{% endalert %}

##### 終了条件を設定する

[終了条件]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria)を設定すると、キャンバスを退出するユーザーが決まります。ユーザーが例外イベントを実行するか、セグメントとフィルターに一致した場合、それ以降のメッセージを受け取らなくなります。

##### ターゲット層の計算

[**ターゲット層**] セクションでは、選択したセグメントや追加フィルターなどのオーディエンスの概要や、メッセージングチャネルごとにリーチ可能なユーザー数の内訳を確認できます。デフォルトの推定値ではなく、ターゲットオーディエンスのリーチ可能なユーザーの正確な数を計算するには、［[正確な統計値を計算する]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment#calculating-exact-statistics)] を選択します。

注意事項:

- 正確な統計の計算には数分かかる。この関数は、フィルターやフィルターグループレベルではなく、セグメントレベルでの正確な統計を計算するだけである。
- 大きなセグメントでは、正確な統計を計算しても、通常はわずかな変動が見られます。この機能の精度は、99.999% 以上であることが期待されます。

ターゲットユーザーの平均生涯収益などの追加統計を表示するには、「**追加統計を表示**」を選択する。

![正確な統計を計算するオプションを使用したターゲット人口の内訳。]({% image_buster /assets/img_archive/canvas_exact_stats.png %})

##### ターゲットオーディエンスの数が到達可能なユーザーの数と異なる理由

{% multi_lang_include segments.md section='Differing audience size' %}

#### ステップ1.4:送信設定を選択する

[**送信設定**] を選択し、サブスクリプション設定を編集し、レート制限をオンにして、サイレント時間を有効にします。[レート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components)または[フリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping)をオンにすることで、ユーザーにかかるマーケティングの圧力を軽減し、過剰なメッセージングを避けることができます。

メールチャネルとプッシュ通知チャネルをターゲットにしたキャンバスの場合、明示的にオプトインしているユーザーのみがメッセージを受け取るようにキャンバスを制限できます (配信登録済みユーザーまたは配信停止済みユーザーを除く)。例えば、オプトインステータスの異なる 3 人のユーザーがいるとします。

- **ユーザー A** はメールを購読しており、プッシュ通知が有効です。このユーザーはメールを受信しませんが、プッシュ通知は受信します。
- **ユーザー B** はメールにオプトインしていますが、プッシュ通知を有効にしていません。このユーザーはメールを受信しますが、プッシュ通知は受信しません。
- **ユーザー C** はメールにオプトインしており、プッシュ通知が有効です。このユーザーはメールとプッシュ通知の両方を受け取ります。

これを行うには、このキャンバスを「オプトインユーザーのみ」に送信するように、[**サブスクリプション設定**] を設定します。このオプションを選択すると、オプトインしたユーザーのみがメールを受信し、Braze は、デフォルトでプッシュ通知が有効になっているユーザーにのみプッシュ通知を送ります。 

これらのサブスクリプション設定はステップごとに適用されるため、エントリオーディエンスへの影響はありません。したがって、この設定は、ユーザーがキャンバスの各ステップを受け取るための適格性を評価するために使用されます。

{% alert important %}
この設定では、**ターゲットオーディエンス**ステップに、オーディエンスを 1 つのチャネルに制限するフィルターを含めないでください (`Foreground Push Enabled = True` や `Email Subscription = Opted-In` など)。
{% endalert %}

必要に応じて、キャンバスにサイレント時間 (メッセージを送信しない時間帯) を指定します。[**送信設定**] で [**サイレント時間を有効にする**] をオンにします。次に、ユーザーの現地時間でサイレント時間を選択し、そのサイレント時間内にメッセージがトリガーされた場合の後続のアクションを選択します。

![[サイレント時間] サイレント時間を有効にするチェックボックスを表示するページ。有効にすると、開始時刻、終了時刻、およびフォールバックの動作を設定できます。]({% image_buster /assets/img/quiet_hours.png %})

### ステップ 2:キャンバスを作成する

{% alert tip %}
[Braze キャンバステンプレート]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/#available-braze-templates)を使用することで、キャンバスの作成にかかるに時間を短縮し、効率化できます。事前に作成されたテンプレートのライブラリーから、あなたのユースケースに合ったテンプレートを見つけ、特定のニーズに合わせてカスタマイズしよう。
{% endalert %}

#### ステップ 2.1:バリアントを追加する

![バリアントを追加」ボタンを選択すると、「バリアントを追加」オプションのあるコンテキストメニューが表示される。]({% image_buster /assets/img_archive/canvas_add_variant.gif %}){: style="float:right;max-width:40%;margin-left:15px;"}

[**バリアントを追加**] を選択し、キャンバスに新しいバリアントを追加します。バリアントはユーザーがたどるジャーニーを表し、複数のステップや分岐を含めることができます。

<i class="fas fa-plus-circle"></i> プラスボタンを選択して、さらにバリアントを追加できます。新しいバリアントを追加すると、ユーザーの配分方法を調整できるため、さまざまなエンゲージメント戦略の効果を相互比較して分析できます。

![Braze キャンバスの2つのバリアントの例。]({% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %})

{% alert tip %}
デフォルトでは、ユーザーがキャンバスに入るときにキャンバスバリアントの割り当てがロックされます。つまり、ユーザーが最初にバリアントに入った場合、キャンバスに再エントリするたびにそのバリアントが使用されます。ただし、この動作を回避する方法があります。<br><br>これを行うには、Liquid を使用して乱数ジェネレーターを作成します。これを各ユーザーのキャンバスエントリの先頭で実行し、値をカスタム属性として保存してから、その属性を使用してユーザーをランダムに分けることができます。

{% details Expand for steps %}

1. 乱数を保存するカスタム属性を作成します。"lottery_number" 、"random_assignment". のように、わかりやすい名前をつける。アトリビューションは、[ダッシュボードで]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data/)作成するか、[`/users/track` エンドポイントへの]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)APIコールで作成することができる。<br><br>
2. キャンバスの始めに Webhook キャンペーンを作成します。このキャンペーンは、そこに乱数を作成し、カスタム属性として保存する媒体となります。詳細は、「[Webhook の作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook)」を参照してください。URL を `/users/track` エンドポイントに設定します。<br><br>
3. 乱数ジェネレーターを作成します。これは、[ここに概説されているコード](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486)を使用して行うことができます。このコードは、各ユーザの一意の入力時間を利用して乱数を作成します。Webhook キャンペーン内で、結果の数値を Liquid 変数として設定します。<br><br>
4. Webhook キャンペーンの `/users/track` 呼び出しをフォーマットして、ステップ 1 で作成したカスタム属性を、現在のユーザーのプロファイルで生成した乱数に設定します。このステップを実行すると、ユーザーがキャンペーンに入るたびに変化する乱数を作成することができます。<br><br>
5. キャンバスの分岐を調整して、ランダムに選んだバリアントで分けるのではなく、オーディエンスルールに基づいて分けるように設定します。各分岐のオーディエンスルールで、カスタム属性に応じてオーディエンスフィルターを設定します。<br><br>例えば、あるBranchでは"lottery_number 、オーディエンスフィルターとして3 "未満とし、別のBranchでは"lottery_number 、オーディエンスフィルターとして3以上6 "未満とする。

{% enddetails %}
{% endalert %}

#### ステップ 2.2:キャンバスステップの追加

キャンバスワークフローにさらにステップを追加するには、[**コンポーネント**] サイドバーからコンポーネントをドラッグ＆ドロップします。または、<i class="fas fa-plus-circle"></i>プラスボタンを選択して、ポップアップメニューからコンポーネントを追加します。

{% alert tip %}
ステップを追加し始めると、ズームレベルを切り替えて、詳細にフォーカスしたり、ユーザージャーニー全体を表示したりできます。<kbd>Shift</kbd> + <kbd>+</kbd> でズームイン、<kbd>Shift</kbd> + <kbd>-</kbd> でズームアウトします。
{% endalert %}

![Brazeキャンバスに遅延ステップを追加するコンポーネント検索ウィンドウ。]({% image_buster /assets/img_archive/add_components_flow.png %}){: style="max-width:80%;"}

{% alert important %}
キャンバスには200ステップまで追加できる。キャンバスが200ステップを超えると、読み込む際に問題が発生する可能性がある。
{% endalert %}

##### 最大期間

キャンバスジャーニーのステップが増えるにつれて、最大所要時間はユーザーがこのキャンバスを完成させるために費やせる最長時間となります。これは、最長パスのバリアントごとの各ステップの延期期間とトリガー期間を加算して計算されます。例えば、キャンバスに延期期間が 3 日の延期期間ステップと、メッセージステップが 1 つずつある場合、キャンバスの最大期間は 3 日になります。

##### ステップを編集する

ユーザージャーニーのステップを編集したいことがあります。キャンバスのワークフローに応じた方法を以下で確認してください。

キャンバスワークフローのどのステップも、コンポーネントを選択して編集することができる。例えば、ワークフローの最初のステップである[遅延]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/)コンポーネントを特定の日に変更したいとします。ステップを選択して設定を表示し、3月1日までの遅延を調整する。すると、ユーザーは 3 月 1 日にキャンバスの次のステップに移行します。

![遅延を「特定の日まで」に設定した「遅延」ステップの例。]({% image_buster /assets/img_archive/edit_delay_flow.png %})

または、[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)ステップの [**アクション設定**] の編集および調整を迅速に行って、ユーザーを一定の期間留めておくこともできます。これは、この評価期間中のアクションに基づいて、次のパスに優先順位を付けます。

![キャンバスの第2ステップ「アクション設定」で、評価ウィンドウを1日に設定した。]({% image_buster /assets/img_archive/action_paths_flow.png %})

キャンバスの軽量コンポーネントによってシンプルな編集が可能になり、キャンバスの細かい調整を簡単に行うことができます。 

##### キャンバスのメッセージ

キャンバスコンポーネント内のメッセージを編集して、特定のステップで送信されるメッセージを制御します。キャンバスはメール、モバイル、Web プッシュメッセージを送信でき、他のシステムと統合するための Webhook も送信できます。キャンペーンと同様に、特定の [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) テンプレートを使用してメッセージをパーソナライズできます。

{% alert tip %}
メッセージやリンクテンプレートにキャンバスコンポーネント名を含めることができるようになりました。<br>
キャンバスで `campaign.${name}` Liquid タグを使用すると、現在のキャンバスコンポーネント名が表示されます。
{% endalert %}

メッセージコンポーネントは、ユーザーに送信されるメッセージを管理します。[**メッセージングチャネル**] を選択し、[**配信設定**] を調整してキャンバスメッセージングを最適化できます。このコンポーネントの詳細については、「[メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)」を参照してください。

![メッセージングチャネル」を選択した「メッセージングの設定」ステップでは、アンドロイドプッシュ、コンテンツカード、メールなど、利用可能なメッセージングチャネルのリストが表示される。]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

キャンバスコンポーネントの設定が完了したら、[**完了**] をクリックします。

{% tabs local %}
{% tab Canvas Entry Properties %}

`canvas_entry_properties` はキャンバスの作成のエントリスケジュールステップで設定され、キャンバスにユーザーを入れるトリガーを指定します。これらのプロパティは、API トリガーキャンバスのエントリペイロードのプロパティにもアクセスできます。`canvas_entry_properties` オブジェクトは最大50KB まで可能であることに注意してください。 

これらのエントリプロパティを参照する場合は、{% raw %} ``canvas_entry_properties.${property_name}`` {% endraw %} という Liquid を使用します。このように使用するには、イベントがカスタムイベントまたは購入イベントでなければならないことに注意してください。

{% raw %}
例えば、`\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` というリクエストを考えてみます。``{{canvas_entry_properties.${product_name}}}`` という Liquid でメッセージに「shoes」という単語を追加できます。
{% endraw %}

{% endtab %}

{% tab Event Properties %}
イベントプロパティは、カスタムイベントや購入イベントの発生時に設定できるプロパティです。これらの `event_properties` は、アクションベースの配信を伴うキャンペーンおよびキャンバスで使用できます。 

キャンバスでは、カスタムイベントと購入イベントプロパティは、アクションパスステップに続くメッセージステップでLiquidで使用できる。これらの `event_properties` を参照する場合は、{% raw %} ``{{event_properties.${property_name}}}``{% endraw %} という Liquid を使用します。メッセージコンポーネントでこのように使用するには、これらのイベントがカスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されるイベントに関連する `event_properties` を使用できます。このアクションパスステップとメッセージステップの間に、他のステップ (別のアクションパスやメッセージステップではない) があってもかまいません。なお、`event_properties` にアクセスできるのは、メッセージステップが、アクションパスステップの「その他のユーザー」以外のパスに遡ることができる場合のみです。

{% endtab %}
{% endtabs %}

#### ステップ 2.3:接続の編集

ステップ間で接続を移動するには、2 つのコンポーネントを接続する矢印を選択し、別のコンポーネントを選択します。接続を削除するには、キャンバスのコンポーザーのフッターで、矢印の後に続く「**接続をキャンセル**」を選択する。

### ステップ 3:コントロールグループの追加

キャンバスにコントロールグループを追加するには、<i class="fas fa-plus-circle"></i> プラスボタンを選択して、新しいバリアントを追加する。 

Braze は、コントロールグループに含まれるユーザーのコンバージョンを追跡します。ただし、これらのユーザーにはメッセージは届きません。正確なテストを行うため、コンバージョンイベント選択画面に示されているのと同じ長さの期間、バリアントとコントロールグループのコンバージョン数が追跡されます。 

[**バリアント名**] のヘッダーをダブルクリックするとメッセージの分配を調整できます。

この例では、キャンバスを 2 つのバリアントに分割しています。1 つ目のバリアントには、ユーザーの 70% が含まれています。2 つ目のバリアントは、残りの 30% のユーザーが含まれるコントロールグループです。

![Braze Canvas のバリアントの例。70% は"Variant 1" に移動します。これは、最初のステップで1 日間遅延し、2 番目のステップでメッセージを送信します。残りの30％は、フォローアップステップのない「コントロール」に回る。]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

#### キャンバスのインテリジェントセレクション

インテリジェントセレクション機能が多変量キャンバス内で使用できるようになりました。多変量キャンペーンの[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)機能と同様に、キャンバスのインテリジェントセレクション機能は、各キャンバスバリアントのパフォーマンスを分析し、各バリアントを経由して目標達成プロセスをたどるユーザーの割合を調整します。この分布は、各バリアントのパフォーマンスメトリクスに基づいて、予想される変換の総数を最大化します。

多変量キャンバスを使用すると、コピーだけでなく、タイミングやチャネルもテストできることに留意してください。インテリジェントセレクションにより、キャンバスをより効率的にテストでき、ユーザーを可能な限り最適なキャンバスジャーニーに送ることができるようになります。

![[バリアント分布を編集] ページで [インテリジェントセレクション] オプションが有効になります。キャンバスを分析して最適化すると、ページ全体に横向きのバーが表示されます。このバーは複数のセクションに分割され、それぞれ色とサイズが異なります。これはあくまで視覚的な表現であり、特定の分析に関連するものではない。]({% image_buster /assets/img_archive/canvas_intelligent_selection.png %})

キャンバスのインテリジェントセレクションは、並べ替えで各バリアントに分けられるユーザーの分布を段階的にリアルタイムで調整することで、キャンバスの結果を最適化します。統計アルゴリズムがバリアントの中で決定的な勝者を決定すると、パフォーマンスの低いバリアントを除外し、キャンバスのすべての将来の適格な受信者を勝者バリアントに割り当てます。 

このため、新規ユーザーが頻繁に入るキャンバスではインテリジェントセレクションが最適です。

### ステップ 4: 保存して開始

キャンバスの作成が完了したら、「**キャンバスを起動**」を選択してキャンバスを保存し、起動する。キャンバスを開始した後、[**キャンバスの詳細**] ページで、ジャーニーの分析結果をリアルタイムで確認できるようになります。 

後で見直す必要がある場合は、キャンバスを下書きとして保存することもできます。

![Braze のキャンバスの例。]({% image_buster /assets/img_archive/Canvas_Analytics.png %})

{% alert tip %}
キャンバスを開始した後で変更したい場合もあります。その場合には編集が可能です。詳細は、「[開始後にキャンバスを編集する]({{site.baseurl}}/post-launch_edits/)」を参照してください。
{% endalert %}

