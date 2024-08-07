---
nav_title: キャンバスの基本
article_title: キャンバスの基本
page_order: 1
page_type: reference
description: "この参照記事では、キャンバスの基本について説明し、初めてキャンバスを設定する際に確認すべきさまざまな質問を取り上げています。"
tool: Canvas

---

# キャンバスの基本

> この参照記事では、キャンバスの基本について説明し、初めてキャンバスを設定する際に確認すべきさまざまな質問を取り上げています。

## キャンバスの構造について

[キャンバスのセットアップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)の詳細に取り組む前に、キャンバスを構成する主要なパーツを確認しておきましょう。

{% tabs %}
  {% tab Canvas %}
  キャンバスは、マーケターが複数のメッセージとステップでキャンペーンを設定し、一貫性のあるジャーニーを形成するための統合インターフェイスです。

  {% endtab %}

  {% tab Journey %}

  ジャーニー (一般にユーザージャーニーと呼ばれる) は、キャンバス内での個々のユーザーエクスペリエンスです。<br><br> ![\]({% image_buster /assets/img_archive/Journey_2.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Entry Wizard %}
  エントリウィザードには、キャンバスを作成する最初のステップが含まれています。これには、キャンバスに名前を付けたり、チームを追加するなどの基本操作が含まれます。エントリウィザードは基本的に、キャンバスの作成を開始する前に必要となる重要なセットアップです。ここでは、[エントリスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule)、[ターゲットオーディエンス]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2c-set-your-target-entry-audience)の編集、[設定の送信]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2d-select-your-send-settings)などのオプションを使用して、ユーザーのカスタマージャーニーの開始と履行方法をコントロールできます。<br><br> ![\]({% image_buster /assets/img_archive/canvas_flow_entry_wizard.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Variants %}
  バリアントとは、各顧客がたどるジャーニーを指します。キャンバスは、コントロールグループで最大 8 つのバリアントをサポートします。各バリアントに名前を付け、各バリアントをたどるターゲットオーディエンスの分布をコントロール できます。<br><br> ![\]({% image_buster /assets/img_archive/canvas_flow_variants.png %}){: style="max-width:90%;"}

  {% endtab %}

  {% tab Steps %}
  キャンバスのステップは、ユーザージャーニーを決定するマーケティング上の意思決定ポイントです。[キャンバスコンポーネント]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/#about-canvas-components)を活用して、ユーザージャーニーのステップを構築できます。<br>ステップ内では、トリガーの設定や配信の予約、フィルターの追加や[例外イベント]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/)のマーキングによるターゲットの絞り込み、メールからチャネルを追加してWebhookへプッシュするなどができます。<br><br> ![\]({% image_buster /assets/img_archive/canvas_flow_step.png %}){: style="max-width:90%;"}

  {% endtab %}
{% endtabs %}

## カスタマージャーニーを構築する

視覚化の 5 つの W を使用することで、ユーザーごとにパーソナライズされたメッセージジャーニーを作成する方法について、顧客エンゲージメント戦略を特定できます。この 5 つの W とは、「何を」、「いつ」、「誰が」、「なぜ」、「どこで」を意味します。 

### 「何を」：キャンバスに名前を付ける

> ユーザーに何を行い、何を理解してもらいたいか。

名前の力をあなどってはいけません。Braze はコラボレーションのために作られているので、この機会に基礎を固めて、チームに目標を伝える方法を考えましょう。 

キャンバス内でタグを追加して、ステップとバリアントの両方に名前を付けることができます。カスタマージャーニーの詳細については、Brazeラーニングコース「[ユーザーのライフサイクルをマッピングする](https://learning.braze.com/mapping-customer-lifecycles)」をご覧ください。

### 「なぜ」：コンバージョンイベントを特定する

> 「何を」を土台に、なぜこのキャンバスを作るのか? 

常に明確な目標を持つことが重要であり、キャンバスは、セッションのエンゲージメント、購入、カスタムイベントなどの KPIs におけるパフォーマンスを理解するのに役立ちます。

少なくとも 1 つの[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)を選択することで、キャンバス内でパフォーマンスを最適化する方法を把握することができます。また、キャンバスに複数のバリエーションやコントロールグループがある場合、Braze はコンバージョンイベントを使用して、この目標を達成するのに最適なバリエーションを決定します。

* **セッションを開始**:ユーザーに再度アプリを使ってもらいたい。
* **購入**:ユーザーに購入してもらいたい。
* **カスタムイベントを実行**:カスタムイベントとして追跡している特定のアクションをユーザーに実行してもらいたい。
* **アプリをアップグレードする**:ユーザーにアプリのバージョンをアップグレードしてもらいたい。

### 「いつ」：開始条件を作成する

> ユーザーはいつ、この体験を開始するか?

あなたの回答によって、キャンバスがいつ、どのようにお客様に届けられるかの詳細が決まります。ユーザーは、スケジュールトリガーまたはアクションベースのトリガーのいずれかの方法でキャンバスに入れます。

{% alert tip %}
さらに多くの戦略や一般的な質問への回答については、キャンバスの[時間ベースの機能]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/)を参照してください。
{% endalert %}

予約配信では、ターゲットオーディエンスにキャンバスをすぐに送信できます。定期的に送信したり、将来の特定の時間を予約することもできます。アクションベースのキャンバスは、特定の顧客行動にその時点で反応します。例えば、アクションベースのトリガーには、アプリを開く、購入する、別のキャンペーンと接する、カスタムイベントをトリガーするなどが含まれます。アクションが発生した時点で、キャンバスをユーザーに送信できます。

### 「誰が」: オーディエンスを選択する

> 誰にリーチしようとしているのか? 

「誰が」を定義するには、キャンバスで利用可能な定義済みセグメントを使用できます。さらにフィルターを追加して、ターゲットオーディエンスとのつながりをさらに絞り込むこともできます。これらのセグメントを構築すると、ターゲットオーディエンスの条件に一致するユーザーのみがキャンバスジャーニーに入れるので、よりパーソナライズされた体験につながります。利用可能なフィルターと、ユースケースに応じてユーザーをセグメント化する方法については、この表を参照してください。

|フィルター|説明|
|---|---|
| カスタムデータ | 定義したイベントや属性に基づいてユーザーをセグメント化する。製品固有の機能を使用できる。 |
| ユーザーアクティビティ | アクションと購入に基づいて顧客をセグメント化する。 |
| リターゲティング | 過去にキャンバスを送信、受信、またはインタラクションした顧客をセグメントする。 |
| マーケティングアクティビティ | 前回のエンゲージメントなど、普遍的な行動に基づいて顧客をセグメント化する。 |
| ユーザー属性 | 一定の属性と特性で顧客をセグメント化する。 |
| インストールアトリビューション | 最初のソース、広告グループ、キャンペーン、広告で顧客をセグメント化する。 |
{: .reset-td-br-1 .reset-td-br-2}

### 「どこで」: オーディエンスを見つける

> どこでオーディエンスにリーチするのがベストなのか? 

ここで、ユーザージャーニーにとってどのメッセージングチャネルが最も理にかなっているかを判断します。理想としては、ユーザーが最もアクセスしやすい場所でリーチするのが最適です。その点を考慮して、キャンバスでは次のチャンネルのいずれかを使用できます。
* [メール]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)
* [プッシュ通知]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)
* [アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)
* [コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)
* [SMS または MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/about_sms/)
* [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/)

### 「どのように」: 完全なエクスペリエンスを構築する

> 5 つの W を特定した後、どのようにキャンバスを構築するのか?

「どのように」には、キャンバスを作成する方法と、メッセージでユーザーにリーチする方法が含まれます。例えば、メッセージを効果的にするには、異なるユーザー間のタイムゾーンに応じて、メッセージングのタイミングを最適化する必要があります。

「どのように」に答えることで、オーディエンスにキャンバスを送る頻度 (週 1 回、隔週など) も決まります。 

## 一般的なヒント

### ステップとバリアントを使用するタイミングと方法を決定する

各キャンバスにはバリエーションとステップが少なくとも 1 つずつ必要です。上限はありません。では、キャンバスの形はどのように決めればよいのでしょうか。ここで、目標、データ、仮説を考えます。「どのように 」と「 どこで」を考えるブレインストーミングは、キャンバスの適切な形と構造を描くのに役立ちます。

### 逆算する

目標には、より小さなサブ目標があるものもあります。たとえば、無料で利用しているユーザーをサブスクリプションにコンバートすることを目指す場合は、サブスクリプションサービスの概要を記載したページが必要です。ユーザーは購入前にこのページでオプションを確認します。チェックアウトページの前に、ユーザーにこのページを見せることをメッセージングの主な目標とすることもできます。顧客をあなたの目標に導く経路を逆算して理解することで、コンバージョンを実現する鍵となります。

### メッセージングを混在させる

過去に同様のキャンペーンを実施したことはありますか? あるいは、現在キャンペーンを実行中ですか?その 1 つのメッセージを使って、さらにパーソナライズしてみてください。新しいフィルターを試すか、フォローアップメッセージを追加します。メッセージング手法を混在させる場合は、パフォーマンスを監視しながら、段階的に変更を加えて最適化してください。
