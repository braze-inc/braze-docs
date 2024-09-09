---
nav_title: キャンペーンとキャンバス
article_title: "開始:キャンペーンとキャンバス"
page_order: 3
page_type: reference
description: "この記事では、Braze でメッセージを送信するさまざまな方法の概要を説明します。"

---

# はじめに: キャンペーンとキャンバス

Braze では、[キャンペーン](#campaigns)または[キャンバス](#canvas-flow)を介してメッセージを送信できます。

- ターゲットを絞った1つのメッセージをユーザーのグループに送信するには、キャンペーンを選択します。キャンペーンは、さまざまなメッセージングチャネルでユーザーとつながるための単一のメッセージステップです。
- 包括的なカスタマージャーニーで一連の継続的なメッセージを送信するには、キャンバスフローを選択してください。キャンバスフローは当社のジャーニーオーケストレーションツールです。キャンペーンはシンプルでターゲットを絞ったメッセージを送信するのに適していますが、キャンバスは顧客との関係を次のレベルに引き上げる場所です。

## キャンペーン

キャンペーンはチャネルに応じて独自に構築できますが、Braze に用意されている次の主な4種類のキャンペーンについて知っておく必要があります。

| キャンペーン種別        | 説明                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 通常              | これは最も一般的なキャンペーンです。メッセージの目標に応じて1つまたは複数のチャネルをターゲットに設定し、Braze のビジュアルエディターを使用してコンテンツを Braze 上で直接デザイン、カスタマイズ、テストできます。[ キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) を作成する方法について説明します。 |
| A/B テスト          | キャンペーン s が1 つのチャネルをターゲットにしている場合、同じキャンペーンの複数のバージョンを送信し、上に表示されるバージョンを確認できます。[多変量 キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) を使用して、最大8 つのさまざまなバージョンのコピー、パーソナライゼーションなどをテストできます。 |
| API                  | [API キャンペーン s]({{site.baseurl}}/api/api_campaigns/) を使用すると、できるだけ早くタイムリーなメッセージを送信できます。他のキャンペーンタイプとは異なり、Braze ダッシュボードではメッセージ、受信者、スケジュールを指定しません。代わりに、これらの識別子を API 呼び出しに渡します。これらは、通常、リアルタイム・トランス・アクションのメッセージングやニュースの更新に使用されます。  |
| アクションメールを送信する | Braze [Trans アクション al メール s]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/) は、お客様と顧客との間で合意されたトランスアクションを容易にするために、自動化された非プロモーションメールを送信する目的で構築されています。ビジネスクリティカルな通知を、スピードが最も重要な1人のユーザーに送信します。*選択したパッケージで使用できます。* |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
定期的なキャンペーンや AB テストキャンペーンをスケジュールすることも (予定されているイベントについてユーザーのリストに通知するなど)、ユーザーのアクションに応じて自動的に送信する (ニュースレターを購読したときにメールを送信するなど) こともできます。[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types)の詳細をご覧ください。
{% endalert %}

作成するキャンペーンの種類にかかわらず、キャンペーンはユーザーのニーズに耳を傾け、思慮深くパーソナライズされた対応を提供できます。キャンペーンを送信したら、[組み込みの分析ツール]({{site.baseurl}}/user_guide/data_and_analytics/reporting)を使用して、キャンペーンのパフォーマンスと、[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)に基づいてコンバージョンしたユーザーの数を確認します。

Braze のキャンペーンの詳細については、以下の追加リソースをご覧ください。

- Braze Learning: [キャンペーン設定](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [キャンペーンを作成する]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign)
- [アイデアと戦略]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)

## キャンバスフロー

キャンバスを使うと、複数のキャンペーンで散発的にメッセージを送るのではなく、ユーザーとの継続的なスムーズな会話を生み出すことができます。これは、ユーザーがキャンバスを利用するジャーニーが、ブランドに対するアクション (または非アクション) に応じて異なるパスに分割されるため、特定のフローをリアルタイムで自動的に進めることができるからです。

![][2]

このように、キャンバスはネットを張ってコンバージョンへの道から外れたユーザーを獲得し、最も効果的なアウトリーチ活動に参加してもらうのに最適です。

キャンバスを作成するときは、キャンペーンの設定と同じステップの多くに従います。つまり、オーディエンス全体、応募条件、送信設定を指定します。キャンバスは、誰かがトリガー条件に一致したときに起動します。その後、終了条件を満たすまで、キャンバス内のパス内を移動します。

キャンバスには、[メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)、[遅延]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/)、[実験]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/)などを自由に組み合わせることができます。サポートされているすべてのメッセージングチャネルで送信でき、Facebook、Google、TikTok などの[ソーシャルプラットフォームや広告プラットフォームと統合する]({{site.baseurl}}/partners/canvas_steps/overview/)こともできます。

キャンバスフローの詳細については、以下の追加リソースをご覧ください。

- Braze Learning: [キャンバスフローによるジャーニーオーケストレーション](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [キャンバスを作成する]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- [キャンバスの概要]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_outlines/)

## メッセージングチャネル

メッセージングチャネルは、顧客と交流し、ターゲットを絞ったメッセージを配信するためのさまざまなコミュニケーションチャネルです。 

![][1]

次の表は、サポートされているチャネルの概要です。

| Channel                                                                                              | 説明                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [メール]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)                        | パーソナライズされた メールs をユーザーの受信トレイes に送信します。                                                                                                       |
| [モバイルプッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)                   | ユーザーの携帯電話に通知で送る。                                                                                   |
| [Web プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)                         | Web サイトでアクティブでない場合でも、通知をユーザーのウェブブラウザに配信します。                                                         |
| [アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)    | ユーザー s が積極的に使用している間、モバイルアプリ内のメールを表示します。                                                                             |
| [SMS/MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/about_sms/)*                   | ユーザーの携帯電話にメールを送信します。                                                                                                            |
| [WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)*              | 人気のメッセージング プラットフォームであるWhatsAppを通じて、ユーザーsに手を差し伸べ、エンゲージするように伝言を送る。                                                   |
| [コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)*       | ユーザー s がメッセージを受信して操作したり、バナーとしてカルーセルにメッセージを表示したりできるように、アプリまたはWeb サイト内に受信トレイを提供します。 |
| [接続したテレビ]({{site.baseurl}}/developer_guide/platform_wide/tv_and_ott/)                           | 接続されたTV プラットフォームでユーザーS を操作します。                                                                                                   |
| [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | カスタムHTTPコールバックを使用して、外部システムとのリアルタイム通信および統合を有効にします。                                                    |
{: .reset-td-br-1 .reset-td-br-2}

<sup>\*\*アドオン機能として利用できます。*</sup>

{% alert tip %}
ほとんどのチャネル (メール、SMS、プッシュ) で送信できる短くて緊急のメッセージについては、[インテリジェントチャネル]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/)フィルターを利用して、各ユーザーに最適なチャネルを介してメッセージを自動的に送信します。
{% endalert %}

[1]: {% image_buster /assets/img/getting_started/channels.png %}
[2]: {% image_buster /assets/img/getting_started/canvas_flow.png %}