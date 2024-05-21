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

{% alert important %}
2023 年 2 月 28 日以降、従来のキャンバスエクスペリエンスを使用したキャンバスの作成や複製ができなくなりました。Braze では、元のキャンバスエクスペリエンスを使用しているお客様に、キャンバスフローへの移行をお勧めしています。これは、キャンバスの構築と管理をより良く行う目的で改良された編集エクスペリエンスです。「[キャンバスからキャンバスフローへの複製]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/)」を参照してください。
{% endalert %}

## ステップ 1: 新しいキャンバスを作成する 

[**メッセージング**] > [**キャンバス**] に移動し、[**キャンバスを作成**] をクリックします。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**エンゲージメント**] の [**キャンバス**] にあります。
{% endalert %}

## ステップ 2: キャンバスを設定する

キャンバスビルダーは、命名からコンバージョンイベントを設定して適切なユーザーをカスタマージャーニーに導くまでのキャンバスの設定プロセスを、ステップごとに順を追って案内します。以下の各タブをクリックして、ビルダーの各ステップで調整できる設定を確認してください。

{% tabs local %}
  {% tab 基本情報 %}
    ここでは、キャンバスの基本情報を設定します。
    \- キャンバスに名前を付ける
    \- チームを追加する
    \- タグを追加する
    \- コンバージョンイベントを割り当て、イベントタイプと期限を選択する

    Learn more about the [Basics step](#step-2a-set-up-your-canvas-basics).
  {% endtab %}
  {% tab エントリスケジュール %}
    ここでは、ユーザーがどのようにキャンバスに入るかを決定します。
    \- スケジュール: これは時間ベースのキャンバスエントリです。
    \- アクションベース: ユーザーは定義されたアクションを実行した後、キャンバスに入ります。
    \- API トリガー: API リクエストを使用してキャンバスにユーザーを入れます。

    Learn more about the [Entry Schedule step](#step-2b-determine-your-canvas-entry-schedule).
  {% endtab %}
  {% tab ターゲットオーディエンス %}
    ここでは、ターゲットオーディエンスを選択します。
    \- セグメントとフィルターを追加してオーディエンスを作成する
    \- キャンバスの再エントリとエントリ制限を微調整する
    \- ターゲットオーディエンスの要約を見る

    Learn more about the [Target Audience step](#step-2c-set-your-target-entry-audience).
  {% endtab %}
  {% tab 送信設定 %}
    ここでは、キャンバスの送信設定を選択します。
    \- サブスクリプションの設定を選択する
    \- キャンバスメッセージの送信レート制限を設定する
    \- サイレント時間の有効化と設定を行う

    Learn more about the [Send Settings step](#step-2d-select-your-send-settings).
  {% endtab %}
  {% tab キャンバスの作成 %}
    ここでは、キャンバスを作成します。

    Learn how to [build your Canvas](#step-3-build-your-canvas) using the Canvas builder.
  {% endtab %}
  {% tab まとめ %}
    ここでは、キャンバスの詳細のまとめが表示されます。[キャンバスの承認ワークフロー]({{site.baseurl}}/canvas_approval/)をオンにしている場合は、一覧されたキャンバスの詳細を承認してからキャンバスを開始することができます。

  {% endtab %}
{% endtabs %}

### ステップ 2a: キャンバスの基本情報から始める

ここでは、キャンバスに名前を付け、[チーム]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/#teams)を割り当て、[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/tags/#tags)を作成または追加します。キャンバスのコンバージョンイベントを割り当てることもできます。

{% alert tip %}
キャンバスにタグを付けることで、検索とレポートの作成が簡単に行えるようになります。例えば、[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)を使用する場合、特定のタグでフィルタリングできます。
{% endalert %}

![][53]

#### コンバージョンイベントを選択する

コンバージョンイベントのタイプを選択し、記録するコンバージョンを選択します。これらの[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/)によって、キャンバスの効果を測定します。 

![「購入」のイベントタイプを持つ 1 次コンバージョンイベント A。3 日間のコンバージョン期限内に何かを購入したユーザーの会話を記録します。][52]

キャンバスに複数のバリアントやコントロールグループがある場合、Braze はこのコンバージョンイベントを使用して、このコンバージョン目標を達成するための最適なバリアントを決定します。同じロジックを使用して、複数のコンバージョンイベントを作成できます。

### ステップ 2b: キャンバスのエントリスケジュールを決める

ユーザーがキャンバスに入ることのできる 3 つの方法のいずれかを選択できます。 

#### エントリスケジュールのタイプ

{% tabs local %}
  {% tab スケジュールされた配信 %}
    スケジュールされた配信では、ユーザーのエントリが時間のスケジュールに従って決まります。これは、キャンペーンをスケジュールする方法と似ています。キャンバスを開始してすぐにユーザーを登録し、将来のある時点でジャーニーにエントリさせたり、定期的に (毎日、毎週、毎月など) エントリさせたりできます。 

    In this example, based on the time-based options, users will enter this Canvas every Tuesday at 12 pm in their local time zone every week, beginning November 14, 2023 until December 31, 2023.

    ![]({% image_buster /assets/img_archive/Canvas_Scheduled_Delivery.png %})
  {% endtab %}
  {% tab アクションベースの配信 %}
    アクションベースの配信では、ユーザーはキャンバスに入り、アプリを開いたり、購入したり、カスタムイベントをトリガーしたりといった特定のアクションを行った後、メッセージを受け取り始めます。

    You can control other aspects of the Canvas behavior from the **Entry Audience** window, including rules for re-eligibility and frequency capping settings. Note that action-based delivery is unavailable for Canvas components with in-app messages.

    ![An example of action-based delivery. Users will enter the Canvas if they make a purchase with an entry window beginning at 1:30 pm on June 10, 2023.]({% image_buster /assets/img_archive/Canvas_Action_Based_Delivery.png %})

  {% endtab %}
  {% tab API トリガー配信 %}
    API トリガー配信では、ユーザーがキャンバスに入り、API 経由で [`/canvas/trigger/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)を使用してメッセージが追加されると、メッセージを受け取り始めます。ダッシュボードには、これを行い、[キャンバスエントリのプロパティオブジェクト]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)を使用してオプションの [`canvas_entry_properties`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/) も割り当てる、cURL リクエストの例があります。 

    ![An example of API-triggered delivery with a Canvas ID and an example of a cURL request.]({% image_buster /assets/img_archive/Canvas_API_Triggered_Delivery.png %})

    You can use the following endpoints for API-triggered delivery:
    - [POST: Send Canvas Messages via API-Triggered Delivery]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
    - [POST: Schedule API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)
    - [POST: Update Scheduled API-Triggered Canvases]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_update_scheduled_triggered_canvases/)

  {% endtab %}
{% endtabs %}

配信方法を選択したら、ユースケースに合わせて設定を調整し、続いてターゲットオーディエンスを設定します。

{% details 元のエディターを使用したキャンバスの重複動作 %}
再適格性の期間がキャンバスの最大継続時間よりも短い場合、ユーザーに再エントリが許可され、複数のコンポーネントメッセージを受信することが可能です。ユーザーの再エントリが前のエントリと同じコンポーネントに到達したエッジケースでは、Braze がそのコンポーネントのメッセージの重複を除外します。 

キャンバスに再エントリし、前回のエントリと同じコンポーネントに到達したユーザーに、エントリごとにアプリ内メッセージを受け取る資格がある場合、セッションを 2 回再開封すれば、ユーザーは (アプリ内メッセージの優先度に応じて) メッセージを 2 回受け取る可能性があります。
{% enddetails %}

### ステップ 2c: エントリのターゲットオーディエンスを設定する

**ターゲットオーディエンス**ステップでキャンバスのターゲットオーディエンスを設定できます。ジャーニーに参加できるのは、定義した条件に一致するユーザーだけです。つまり、Braze は、ユーザーがキャンバスジャーニーに入る前に、まずターゲットオーディエンスの適格性を評価します。 

[**エントリコントロール**] では、キャンバスの実行がスケジュールされるたびに、ユーザーの数を制限できます。API トリガーベースのキャンバスの場合、この制限は UTC で 1 時間ごとに発生します。例えば、新規ユーザーをターゲットとする場合は、特定のジャーニーを過去 3 週間以内にアプリを初めて使用したユーザーに限定することができます。通知をサブスクリプション登録したりオプトインしているユーザーにメッセージを送信するかどうかなどの設定も制御できます。

{% alert warning %}
オーディエンスフィルターと同じトリガー (属性の変更やカスタムイベントの実行など) でアクションベースのキャンペーンやキャンバスを設定しないでください。ユーザーがトリガーイベントを行った時点でオーディエンスに含まれないという競合状態が発生する可能性があり、そうするとユーザーはキャンペーンを受け取れず、キャンバスにも入ることができません。  
{% endalert %}

#### オーディエンスをテストする

ターゲットオーディエンスにセグメントとフィルターを追加した後、[ユーザーを検索]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup/)してオーディエンス基準に一致しているかを確認することで、オーディエンスが期待どおりに設定されているかどうかをテストできます。

![\]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:50%;"}

#### エントリコントロールを調整する

エントリコントロールは、ユーザーがキャンバスに再エントリできるかどうかを決定します。また、このキャンバスにエントリできる人数を制限することもできます。例えば、[**このキャンバスにエントリする可能性のある最大ユーザー数**] フィールドを 1,000 人に設定し、[**キャンバスがスケジュールされるたびに制限する**] チェックボックスをオンにすると、キャンバスは 1 日あたり 1,000 人のユーザーに送信を行います。

![\]({% image_buster /assets/img_archive/entry_controls.png %}){: style="max-width:50%;"}

#### 終了条件を設定する

[終了条件]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria)を設定すると、キャンバスを退出するユーザーが決まります。ユーザーが例外イベントを実行するか、セグメントとフィルターに一致した場合、それ以降のメッセージを受け取らなくなります。

### ステップ 2d: 送信設定を選択する

[**送信設定**] をクリックして、サブスクリプション設定を選択し、レート制限をオンにし、待機時間を有効にします。[レート制限][6b] または [フリークエンシーキャップ][6c] をオンにすることで、ユーザーにかかるマーケティングの圧力を軽減し、過剰なメッセージングを避けることができます。

メールチャネルとプッシュ通知チャネルをターゲットにしたキャンバスの場合、明示的にオプトインしているユーザーのみがメッセージを受け取るようにキャンバスを制限できます (配信登録済みユーザーまたは配信停止済みユーザーを除く)。例えば、オプトインステータスの異なる 3 人のユーザーがいるとします。

- **ユーザー A** はメールを購読しており、プッシュ通知が有効です。このユーザーはメールを受信しませんが、プッシュ通知は受信します。
- **ユーザー B** はメールにオプトインしていますが、プッシュ通知を有効にしていません。このユーザーはメールを受信しますが、プッシュ通知は受信しません。
- **ユーザー C** はメールにオプトインしており、プッシュ通知が有効です。このユーザーはメールとプッシュ通知の両方を受け取ります。

これを行うには、このキャンバスを「オプトインユーザーのみ」に送信するように、[**サブスクリプション設定**] を設定します。このオプションを選択すると、オプトインしたユーザーのみがメールを受信し、Braze は、デフォルトでプッシュ通知が有効になっているユーザーにのみプッシュ通知を送ります。 

これらのサブスクリプション設定はステップごとに適用されるため、エントリオーディエンスへの影響はありません。したがって、この設定は、ユーザーがキャンバスの各ステップを受け取るための適格性を評価するために使用されます。

{% alert important %}
この設定では、**ターゲットユーザー**ステップに、オーディエンスを 1 つのチャネルに制限するフィルターを含めないでください (`Push Enabled = True` や `Email Subscription = Opted-In` など)。
{% endalert %}

必要に応じて、キャンバスにサイレント時間 (メッセージを送信しない時間帯) を指定します。[**送信設定**] で [**サイレント時間を有効にする**] をオンにします。次に、ユーザーの現地時間でサイレント時間を選択し、そのサイレント時間内にメッセージがトリガーされた場合の後続のアクションを選択します。

![][50]

## ステップ 3: キャンバスを作成する

### バリアントを追加する

![][11]{: style="float:right;max-width:35%;margin-left:15px;"}

[**バリアントを追加**] をクリックし、キャンバスに新しいバリアントを追加するオプションを選択します。バリアントはユーザーがたどるジャーニーを表し、複数のステップや分岐を含めることができます。

<i class="fas fa-plus-circle"></i> プラスボタンをクリックすると、さらにバリアントを追加できます。新しいバリアントを追加すると、ユーザーの配分方法を調整できるため、さまざまなエンゲージメント戦略の効果を相互比較して分析できます。

![][12]

{% alert tip %}
デフォルトでは、ユーザーがキャンバスに入るときにキャンバスバリアントの割り当てがロックされます。つまり、ユーザーが最初にバリアントに入った場合、キャンバスに再エントリするたびにそのバリアントが使用されます。ただし、この動作を回避する方法があります。<br><br>これを行うには、Liquid を使用して乱数ジェネレーターを作成します。これを各ユーザーのキャンバスエントリの先頭で実行し、値をカスタム属性として保存してから、その属性を使用してユーザーをランダムに分けることができます。

{% details ステップを展開する %}

1. 乱数を保存するカスタム属性を作成します。「lottery\_number」や「random\_assignment」など、見つけやすい名前を付けます。属性は[ダッシュボードで]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data/)作成するか、[`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)への API 呼び出しを通じて作成できます。<br><br>
2. キャンバスの始めに Webhook キャンペーンを作成します。このキャンペーンは、そこに乱数を作成し、カスタム属性として保存する媒体となります。詳細は、「[Webhook の作成]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/#step-1-set-up-a-webhook)」を参照してください。URL を `/users/track` エンドポイントに設定します。<br><br>
3. 乱数ジェネレーターを作成します。これを行うには、[ここで説明](https://community.shopify.com/c/technical-q-a/is-there-any-way-to-generate-random-number-with-liquid-shopify/m-p/1595486)されているコードを使用できます。このコードは、各ユーザーに固有のエントリ時刻を利用して乱数を作成します。Webhook キャンペーン内で、結果の数値を Liquid 変数として設定します。<br><br>
4. Webhook キャンペーンの `/users/track` 呼び出しをフォーマットして、ステップ 1 で作成したカスタム属性を、現在のユーザーのプロファイルで生成した乱数に設定します。このステップを実行すると、ユーザーがキャンペーンに入るたびに変化する乱数を作成することができます。<br><br>
5. キャンバスの分岐を調整して、ランダムに選んだバリアントで分けるのではなく、オーディエンスルールに基づいて分けるように設定します。各分岐のオーディエンスルールで、カスタム属性に応じてオーディエンスフィルターを設定します。<br><br>例えば、ある分岐でオーディエンスフィルターを「lottery\_number が 3 未満」に設定し、別の分岐では「lottery\_number が 3 以上 6 未満」に設定します。

{% enddetails %}
{% endalert %}

### ステップを追加する

キャンバスワークフローにさらにステップを追加するには、[**コンポーネント**] サイドバーからコンポーネントをドラッグ＆ドロップします。または、<i class="fas fa-plus-circle"></i>プラスボタンをクリックして、ポップアップメニューでコンポーネントを追加することもできます。

{% alert tip %}
ステップを追加し始めると、ズームレベルを切り替えて、詳細にフォーカスしたり、ユーザージャーニー全体を表示したりできます。<kbd>Shift</kbd> + <kbd>+</kbd> でズームイン、<kbd>Shift</kbd> + <kbd>-</kbd> でズームアウトします。
{% endalert %}

![\]({% image_buster /assets/img_archive/add_components_flow.png %})

{% alert warning %}
キャンバスフローを使用して構築されたキャンバスには、最大 200 ステップを含めることができます。キャンバスが 200 ステップを超えると読み込みに問題が発生します。
{% endalert %}

#### 最大期間

キャンバスジャーニーのステップが増えるにつれて、最大所要時間はユーザーがこのキャンバスを完成させるために費やせる最長時間となります。これは、最長パスのバリアントごとの各ステップの延期期間とトリガー期間を加算して計算されます。例えば、キャンバスに延期期間が 3 日の延期期間ステップと、メッセージステップが 1 つずつある場合、キャンバスの最大期間は 3 日になります。

### ステップを編集する

ユーザージャーニーのステップを編集したいことがあります。キャンバスのワークフローに応じた方法を以下で確認してください。

コンポーネントのいずれかをクリックすることで、キャンバスフローワークフローの任意のステップを編集できます。例えば、ワークフローの最初のステップである[遅延]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/)コンポーネントを特定の日に変更したいとします。ステップをクリックして設定を表示し、延期期間を 3 月 1 日に調整します。すると、ユーザーは 3 月 1 日にキャンバスの次のステップに移行します。

![\]({% image_buster /assets/img_archive/edit_delay_flow.png %})

または、[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)ステップの [**アクション設定**] をすばやく編集・調整して、ユーザーを一定の期間留めておくこともできます。これは、この評価期間中のアクションに基づいて、次のパスに優先順位を付けます。

![\]({% image_buster /assets/img_archive/action_paths_flow.png %})

キャンバスの軽量コンポーネントによってシンプルな編集が可能になり、キャンバスの細かい調整を簡単に行うことができます。 

#### キャンバスのメッセージ

キャンバスコンポーネント内のメッセージを編集して、特定のステップで送信されるメッセージを制御します。キャンバスはメール、モバイル、Web プッシュメッセージを送信でき、他のシステムと統合するための Webhook も送信できます。キャンペーンと同様に、特定の [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/) テンプレートを使用してメッセージをパーソナライズできます。

{% alert tip %}
メッセージやリンクテンプレートにキャンバスコンポーネント名を含めることができるようになりました。<br>
キャンバスで `campaign.${name}` Liquid タグを使用すると、現在のキャンバスコンポーネント名が表示されます。
{% endalert %}

メッセージコンポーネントは、ユーザーに送信されるメッセージを管理します。[**メッセージングチャネル**] を選択し、[**配信設定**] を調整してキャンバスメッセージングを最適化できます。このコンポーネントの詳細については、「[メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)」を参照してください。

![\]({% image_buster /assets/img_archive/message_setup_settings_flow.png %})

キャンバスコンポーネントの設定が完了したら、[**完了**] をクリックします。

{% tabs local %}
{% tab キャンバスエントリのプロパティ %}

`canvas_entry_properties` はキャンバスの作成のエントリスケジュールステップで設定され、キャンバスにユーザーを入れるトリガーを指定します。これらのプロパティは、API トリガーキャンバスのエントリペイロードのプロパティにもアクセスできます。`canvas_entry_properties` オブジェクトの最大サイズは 50 KB であることに注意してください。 

キャンバスフローの場合、任意のメッセージステップでエントリプロパティを Liquid で使用できます。これらのエントリプロパティを参照する場合は、「{% raw %}``canvas_entry_properties${property_name}``{% endraw %}」という Liquid を使用します。このように使用するには、イベントがカスタムイベントまたは購入イベントでなければなりません。

これらのエントリプロパティを参照する場合は、「{% raw %}``canvas_entry_properties${property_name}``{% endraw %}」という Liquid を使用します。このように使用するには、イベントがカスタムイベントまたは購入イベントでなければならないことに注意してください。

{% raw %}
例えば、`\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` というリクエストがあるとします。``{{canvas_entry_properties.${product_name}}}`` という Liquid でメッセージに「shoes」という単語を追加できます。
{% endraw %}

{% endtab %}

{% tab イベントプロパティ %}
イベントプロパティは、カスタムイベントや購入イベントの発生時に設定できるプロパティです。これらの `event_properties` は、キャンバスと同様にアクションベースの配信を使ったキャンペーンで使用できます。 

キャンバスフローでは、アクションパスステップに続く任意のメッセージステップで、カスタムイベントと購入イベントのプロパティを Liquid で使用できます。これらの `event_properties` を参照する場合は、{% raw %} ``{{event_properties.${property_name}}}``{% endraw %} という Liquid を使用します。メッセージコンポーネントでこのように使用するには、これらのイベントがカスタムイベントまたは購入イベントである必要があります。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されるイベントに関連する `event_properties` を使用できます。このアクションパスステップとメッセージステップの間に、他のステップ (別のアクションパスやメッセージステップではないステップ) があってもかまいません。なお、`event_properties` にアクセスできるのは、メッセージステップが、アクションパスステップの「その他のユーザー」以外のパスに遡ることができる場合のみです。

{% endtab %}
{% endtabs %}

### 接続を編集する

ステップ間で接続を移動するには、2 つのコンポーネントを接続する矢印をクリックし、別のコンポーネントを選択します。接続を切断するには、矢印をクリックし、キャンバス作成画面のフッターにある [**接続をキャンセル**] をクリックします。

## ステップ 4: キャンバスを用いた多変量テストを使用する

プラスボタン <i class="fas fa-plus-circle"></i> をクリックして新しいバリアントを追加することで、キャンバスにコントロールグループを追加できます。 

Braze は、コントロールグループに含まれるユーザーのコンバージョンを追跡します。ただし、これらのユーザーにはメッセージは届きません。正確なテストを行うため、コンバージョンイベント選択画面に示されているのと同じ長さの期間、バリアントとコントロールグループのコンバージョン数が追跡されます。 

[**バリアント名**] のヘッダーをダブルクリックするとメッセージの分配を調整できます。

この例では、キャンバスを 2 つのバリアントに分割しています。1 つ目のバリアントには、ユーザーの 70% が含まれています。2 つ目のバリアントは、残りの 30% のユーザーが含まれるコントロールグループです。

![\]({% image_buster /assets/img_archive/Canvas_Multivariate_Flow.png %})

### キャンバスのインテリジェントセレクション

インテリジェントセレクション機能が多変量キャンバス内で使用できるようになりました。多変量キャンペーンの [インテリジェントセレクション][18a] 機能と同様に、キャンバスのインテリジェントセレクション機能は、各キャンバスバリアントのパフォーマンスを分析し、各バリアントを経由して目標達成プロセスをたどるユーザーの割合を調整します。この配分は各バリアントのパフォーマンス指標に基づいて、予想される合計コンバージョン数を最大化します。

多変量キャンバスを使用すると、コピーだけでなく、タイミングやチャネルもテストできることに留意してください。インテリジェントセレクションにより、キャンバスをより効率的にテストでき、ユーザーを可能な限り最適なキャンバスジャーニーに送ることができるようになります。

![][18b]

キャンバスのインテリジェントセレクションは、並べ替えで各バリアントに分けられるユーザーの分布を段階的にリアルタイムで調整することで、キャンバスの結果を最適化します。統計アルゴリズムがバリアントの中で決定的な勝者を決定すると、パフォーマンスの低いバリアントを除外し、キャンバスのすべての将来の適格な受信者を勝者バリアントに割り当てます。 

このため、新規ユーザーが頻繁に入るキャンバスではインテリジェントセレクションが最適です。

## ステップ 5: キャンバスを保存して開始する

キャンバスの作成が完了したら、[**キャンバスを開始**] をクリックしてキャンバスを保存し、開始します。キャンバスを開始した後、[**キャンバスの詳細**] ページで、ジャーニーの分析結果をリアルタイムで確認できるようになります。 

後で見直す必要がある場合は、キャンバスを下書きとして保存することもできます。

![][19]

{% alert tip %}
キャンバスを開始した後で変更したい場合もあります。その場合には編集が可能です。詳細は、「[開始後にキャンバスを編集する]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/)」を参照してください。
{% endalert %}


[1]:{% image_buster /assets/img_archive/canvas_dropdown.png %}
[3]: {% image_buster /assets/img_archive/choose_canvas_experience.png %}
[6b]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting-and-canvas-components
[6c]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting#frequency-capping
[11]:{% image_buster /assets/img_archive/canvas_add_variant.gif %}
[12]:{% image_buster /assets/img_archive/Canvas_Multiple_Variants.png %}
[13]:{% image_buster /assets/img_archive/Canvas_One_Day.png %}
[14]:{% image_buster /assets/img_archive/Canvas_Exception_Events.png %}
[15]:{% image_buster /assets/img_archive/Canvas_Additional_Engagement.png %}
[17]:{% image_buster /assets/img_archive/Canvas_More_Step.png %}
[18a]: {{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_selection/
[18b]: {% image_buster /assets/img_archive/canvas_intelligent_selection.png %}
[19]:{% image_buster /assets/img_archive/Canvas_Analytics.png %}
[50]: {% image_buster /assets/img/quiet_hours.png %}
[52]: {% image_buster /assets/img/add_canvas_conversions.png %}
[53]: {% image_buster /assets/img/canvas_details.png %}
