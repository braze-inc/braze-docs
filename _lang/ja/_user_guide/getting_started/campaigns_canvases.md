---
nav_title: キャンペーンとキャンバス
article_title: "開始:キャンペーンとキャンバス"
page_order: 3
page_type: reference
description: "この記事では、Braze でメッセージを送信するさまざまな方法の概要を説明します。"

---

# 開始:キャンペーンとキャンバス

Braze では、[キャンペーン](#campaigns)または[キャンバス](#canvas)を介してメッセージを送信できます。

- ターゲットを絞った1つのメッセージをユーザーのグループに送信するには、キャンペーンを選択します。キャンペーンは、さまざまなメッセージングチャネルでユーザーとつながるための単一のメッセージステップです。
- 進行中の一連のメッセージを包括的なカスタマージャーニーで送信するには、ジャーニーオーケストレーションツールの「キャンバス」を選択します。キャンペーンはシンプルでターゲットを絞ったメッセージを送信するのに適していますが、キャンバスは顧客との関係を次のレベルに引き上げる場所です。

## キャンペーン

キャンペーンはチャネルに応じて独自に構築できますが、Braze に用意されている次の主な4種類のキャンペーンについて知っておく必要があります。

| キャンペーン種別        | 説明                                                                                                                                                                                                                                                                                              |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 通常              | これは最も一般的なキャンペーンです。メッセージの目標に応じて1つまたは複数のチャネルをターゲットに設定し、Braze のビジュアルエディターを使用してコンテンツを Braze 上で直接デザイン、カスタマイズ、テストできます。[ キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign) を作成する方法について説明します。 |
| A/B テスト          | 1 つのチャネルをターゲットとするキャンペーンの場合、同じキャンペーンの複数のバージョンを送信して、どれが一番効果が上がるかを確認できます。[多変量 キャンペーン]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) を使用して、最大8 つのさまざまなバージョンのコピー、パーソナライゼーションなどをテストできます。 |
| API                  | [API キャンペーン]({{site.baseurl}}/api/api_campaigns/)では、タイムリーなメッセージをできるだけ早く送信できます。他のキャンペーンタイプとは異なり、Braze ダッシュボードではメッセージ、受信者、スケジュールを指定しません。代わりに、これらの識別子を API 呼び出しに渡します。これらは通常、リアルタイムトランザクションメッセージングや最新ニュースに使用されます。  |
| トランザクションメール | Braze [トランザクションメール]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)は、お客様とお客様の顧客との間で合意したトランザクションを円滑に進めるために、自動化されたプロモーション以外のメールメッセージを送信することを目的としています。ビジネスクリティカルな通知を、スピードが最も重要な1人のユーザーに送信します。*一部のパッケージでご利用いただけます。* |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
定期的なキャンペーンや AB テストキャンペーンをスケジュールすることも (予定されているイベントについてユーザーのリストに通知するなど)、ユーザーのアクションに応じて自動的に送信する (ニュースレターを購読したときにメールを送信するなど) こともできます。[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types)の詳細をご覧ください。
{% endalert %}

作成するキャンペーンの種類にかかわらず、キャンペーンはユーザーのニーズに耳を傾け、思慮深くパーソナライズされた対応を提供できます。キャンペーンを送信したら、[組み込みの分析ツール]({{site.baseurl}}/user_guide/analytics/reporting/)を使用して、キャンペーンのパフォーマンスと、[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)に基づいてコンバージョンしたユーザーの数を確認します。

Braze のキャンペーンの詳細については、以下の追加リソースをご覧ください。

- Braze Learning: [キャンペーン設定](https://learning.braze.com/campaign-setup-delivery-targeting-conversions)
- [キャンペーンを作成する]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign)
- [アイデアと戦略]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies)

## キャンバス

キャンバスを使うと、複数のキャンペーンで散発的にメッセージを送るのではなく、ユーザーとの継続的なスムーズな会話を生み出すことができます。これは、ユーザーがキャンバスを利用するジャーニーが、ブランドに対するアクション (または非アクション) に応じて異なるパスに分割されるため、特定のフローをリアルタイムで自動的に進めることができるからです。

![]({% image_buster /assets/img/getting_started/canvas_flow.png %})

このように、キャンバスはネットを張ってコンバージョンへの道から外れたユーザーを獲得し、最も効果的なアウトリーチ活動に参加してもらうのに最適です。

キャンバスを作成するときは、キャンペーンの設定と同じステップの多くに従います。つまり、オーディエンス全体、応募条件、送信設定を指定します。キャンバスは、誰かがトリガー条件に一致したときに起動します。その後、終了条件を満たすまで、キャンバス内のパス内を移動します。

キャンバスには、[messages]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)、[delays]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/)、[experiments]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/)などを自由に組み合わせることができます。サポートされているすべてのメッセージングチャネルで送信でき、Facebook、Google、TikTok などの[ソーシャルプラットフォームや広告プラットフォームと統合する]({{site.baseurl}}/partners/canvas_audience_sync/overview/)こともできます。

キャンバスの詳細については、次の追加リソースを参照してください。

- Braze Learning: [キャンバスフローによるジャーニーオーケストレーション](https://learning.braze.com/path/journey-orchestration-with-canvas-flow)
- [キャンバスを作成する]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)
- [キャンバスの概要]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_outlines/)

## メッセージングチャネル

メッセージングチャネルは、顧客と交流し、ターゲットを絞ったメッセージを配信するためのさまざまなコミュニケーションチャネルです。 

![]({% image_buster /assets/img/getting_started/channels.png %})

次の表は、サポートされているチャネルの概要です。

| チャネル                                                                                              | 説明                                                                                                                                            |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [メール]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/)                        | パーソナライズされたメールをユーザーの受信トレイに送信します。                                                                                                       |
| [モバイルプッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/)                   | メッセージをユーザーのモバイルデバイスに通知として直接配信します。                                                                                   |
| [Web プッシュ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)                         | Web サイトでアクティブでない場合でも、通知をユーザーのウェブブラウザに配信します。                                                         |
| [アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/)    | ユーザーがモバイルアプリをアクティブに使用している間に、モバイルアプリ内にメッセージを表示します。                                                                             |
| [SMS、MMS、および RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/)*                   | ユーザーの携帯電話にメールを送信します。                                                                                                            |
| [WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/)*              | 人気のメッセージング プラットフォームであるWhatsAppを通じて、ユーザーに手を差し伸べ、エンゲージするように伝言を送る。                                                   |
| [バナー]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)*       | メッセージをアプリまたは Web サイトに直接埋め込みます。 |
| [コンテンツカード]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)*       | ユーザーがメッセージを受信して操作したり、カルーセルにメッセージを表示したり、バナーとしてメッセージを表示したりできる受信トレイをアプリや Web サイト内に用意します。 |
| [コネクテッド TV]({{site.baseurl}}/developer_guide/platforms/tv_and_ott/)                           | コネクテッド TV プラットフォームでユーザーと交流します。                                                                                                   |
| [Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/) | カスタムHTTPコールバックを使用して、外部システムとのリアルタイム通信および統合を有効にします。                                                    |
| [LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/) | 日本で最も人気のあるメッセージングアプリLINEでユーザーとエンゲージします。                                                    |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

<sup>\*\*アドオン機能として利用できます。*</sup>

{% alert tip %}
ほとんどのチャネル (メール、SMS、プッシュ) で送信できる短くて緊急のメッセージについては、[インテリジェントチャネル]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/)フィルターを利用して、各ユーザーに最適なチャネルを介してメッセージを自動的に送信します。
{% endalert %}

