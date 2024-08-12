---
nav_title: SMS メッセージの作成
article_title: SMS メッセージの作成
page_order: 5
description: "この参考記事では、SMS メッセージの作成と作成に必要な手順について説明しています。"
page_type: reference
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# SMS メッセージの作成

> SMSキャンペーンは、顧客と直接連絡を取り、プログラムで会話するのに最適です。Liquidやその他の動的コンテンツを使用して、ユーザーとの個人的な体験を創出し、ブランドでの目立たないユーザー体験を促進および強化する環境を作成できます。 

## ステップ 1:メッセージを作成する場所を選択してください

メッセージをキャンペーンとキャンバスのどちらを使用して送信すべきかわからない?キャンペーンは単一のシンプルなメッセージキャンペーンに適していますが、キャンバスは複数段階のユーザージャーニーに適しています。

{% tabs %}
{% tab Campaign %}

**ステップ:**

1. [**メッセージング**] > [**キャンペーン**] に移動し、[<i class=「fas fa-plus」> </i> **キャンペーンを作成**] をクリックします。
{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、[**エンゲージメント**] に [**キャンペーン**] が表示されます。
{% endalert %}

{:start=“2"}
2\.[**SMS**] を選択します。複数のチャネルをターゲットとするキャンペーンの場合は [**マルチチャネルキャンペーン**] を選択します。
3\.キャンペーンには明確で意味のある名前を付けてください。
4\.[[必要に応じてチームとタグを追加します]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/)。
   \* タグを使うと、キャンペーンを簡単に見つけてレポートを作成できます。たとえば、[レポートビルダーを使用する場合]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)、特定のタグでフィルタリングできます。
5\.キャンペーンに必要な数だけバリエーションを追加して名前を付けてください。追加したバリアントごとに、さまざまなプラットフォーム、メッセージタイプ、およびレイアウトを選択できます。このトピックの詳細については、「[多変量分析と]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) A/B テスト」を参照してください。
6\.[購読グループを選択して]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/)、メッセージを適切なユーザーに送信するようにしてください。サブスクリプショングループを選択すると、Brazeは自動的にセグメントフィルターを追加し、サブスクライブしたユーザーのみがキャンペーンを受け取れるようにします。対象ユーザーへのSMS送信には、そのサブスクリプショングループに属するロングコードとショートコードのみが使用されます。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似または同じ内容になる場合は、バリエーションを追加する前にメッセージを作成してください。次に、「**バリエーションを追加**」**ドロップダウンから「バリアントからコピー**」を選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}

**ステップ:**

1. [Canvas コンポーザーを使用して Canvas を作成します]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに明確で意味のある名前を付けてください。
3. [ステップスケジュールを選択し]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)、必要に応じて遅延を指定します。
4. このステップでは、必要に応じてオーディエンスを絞り込んでください。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込みます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. [昇進行動を選択してください]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)。
6. メッセージとペアリングしたい他のメッセージングチャネルを選択してください。

{% endtab %}
{% endtabs %}

## ステップ 2:SMS を作成

必要に応じて、言語とパーソナライズ（Liquid、コネクテッドコンテンツ、絵文字）を使用してメッセージを書きます。超過料金が発生する可能性を減らすため、メッセージコピーの制限を必ず守ってください。

{% alert important %}
先に進む前に、[SMS メッセージセグメントとコピー制限に関するガイドラインをお読みください]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/)。SMS メッセージセグメントは、電話会社がテキストメッセージの測定に使用する文字バッチです。メッセージはメッセージセグメントごとに課金されるため、メッセージがどのように分割されるかの微妙な違いを理解しておくとよいでしょう。
{% endalert %}

![SMS composer in Braze with the message "Hi first_name, we appreciate your support! Why not stop by one of our stores and show them this SMS for an exclusive discount? Reply STOP to stop receiving messages from us."]({% image_buster /assets/img/sms_campaign_compose.png %})

{% alert tip %}
{% raw %}
Liquidを使用する予定の場合は、選択したパーソナライゼーションのデフォルト値を必ず含めてください。そうすれば、受信者のユーザープロファイルが不完全な場合でも、`Hi, !`名前や一貫した文章の代わりに空白のプレースホルダーが届きません。
{% endraw %}
{% endalert %}

素晴らしいコピーを作成するのに助けが必要ですか？[AIコピーライティングアシスタントを使ってみてください]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/)。商品名または説明を入力すると、AIが人間のようなマーケティングコピーを生成し、メッセージングに使用できます。

![Launch AI Copywriter button, located in the Message field of the SMS composer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

### 連絡先カード

必要に応じて、SMSメッセージに連絡先カードを追加して、顧客が連絡先にビジネス情報や連絡先情報を簡単に追加できるようにすることができます。これらのカードには、会社の名前、電話番号、住所、電子メール、小さな写真などの一般的なプロパティを割り当てることができます。詳細については、「[連絡先カード]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/)」を参照してください。

## ステップ 3:メッセージをプレビューしてテストする

Braze では、送信前にメッセージをプレビューしてテストすることを常に推奨しています。**テストタブに切り替えて**、[コンテンツテストグループまたは個々のユーザーにテスト]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) SMS を送信したり、メッセージをユーザーとして Braze で直接プレビューしたりできます。

![Previewing SMS copy from the Test tab of the composer. In the profile section, the First Name field is set to "James". In the preview section, the SMS now reads "Hi James, we appreciate your support!"]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
SMSが分割されるセグメント数をテストしたい場合は、[SMSセグメント計算ツールでコピーの長さをテストしてください]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator)。
{% endalert %}

## ステップ 4: 残りのキャンペーンやキャンバスを作成

{% tabs %}
{% tab Campaign %}

次に、残りのキャンペーンを作成します。当社のツールを最大限に活用して SMS メッセージを作成する方法の詳細については、以下のセクションを参照してください。

#### 配送スケジュールまたはトリガーを選択

SMS メッセージは、スケジュールされた時間、アクション、または API トリガーに基づいて配信できます。詳細については、「[キャンペーンのスケジュール]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)」を参照してください。

アクションベースの配信では、[キャンペーンの期間と待機時間を設定することもできます]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)。

このステップでは、[ユーザーにキャンペーンの再受領を許可したり]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)、[フリークエンシーキャップルールを有効にするなどの配信制御を指定することもできます]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)。

#### ターゲットにするユーザーを選択

次に、[セグメントまたはフィルターを選択してユーザーをターゲットにし]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)、オーディエンスを絞り込む必要があります。購読グループはすでに選択されているはずです。これにより、ユーザーが希望するコミュニケーションのレベルまたはカテゴリでユーザーが絞り込まれます。このステップでは、セグメントからより多くのオーディエンスを選択し、必要に応じてフィルターを使用してそのセグメントをさらに絞り込みます。現在のおおよそのセグメント人口がどのようになっているかのスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

{% alert tip %}
SMSリターゲティングに興味がありますか？詳しくは、[SMSリターゲティングの記事をご覧ください]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/)。
{% endalert %}

#### コンバージョンイベントを選択する

Brazeでは、キャンペーンを受け取った後、[ユーザーが特定のアクションやコンバージョンイベントを実行する頻度を追跡できます]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間を最大 30 日間設定できます。

コンバージョンイベントは、キャンペーンの成功を測定するのに役立ちます。例えば:

- ジオターゲティングを使用して、ユーザーが購入することを最終目標とする SMS メッセージをトリガーする場合は、コンバージョンイベントをに設定します。`Purchase`
- ユーザーをアプリに誘導しようとする場合は、コンバージョンイベントをに設定します`Starts Session`。

特定のユースケースに基づいてカスタムコンバージョンイベントを設定することもできます。クリエイティブになって、このキャンペーンの成功を本当にどのように測定したいかを考えてください。

{% endtab %}

{% tab Canvas %}

まだ行っていない場合は、Canvas コンポーネントの残りのセクションを完了してください。Canvasの残りの部分を構築する方法、多変量分析テストやインテリジェントセレクションを実装する方法などの詳細については、[Canvasドキュメントの「キャンバスの構築]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)」ステップを参照してください。

{% endtab %}
{% endtabs %}

## ステップ 5: 確認とデプロイ

最後のキャンペーンやキャンバスの作成が終わったら、詳細を確認してテストし、送信しましょう！

次に、[SMSレポートを確認して]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/)、SMSキャンペーンの結果にアクセスする方法を確認してください。
