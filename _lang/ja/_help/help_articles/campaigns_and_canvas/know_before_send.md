---
nav_title: 送信前の確認
article_title: 送信前の確認
description: "プレローンチガイドをご覧になった後、コンテンツカード、メール、アプリ内メッセージ、プッシュ、SMSのチェックまたは「gotchas」の最終リストをご覧ください。"
alias: /know_before_send/

---

# 送信前に知る: チャンネル

自信を持ってキャンペーンとキャンバスを起動しましょう![プレローンチガイド](https://labplaybooks.braze.com/canvas-playbooks#/subpage/b2rj8)を訪問した後、このチェックまたは"gotchas&quot の最終リストを参照してください。コンテンツカード、メール、アプリ内メッセージ、プッシュ、SMS 用です。

{% alert note %}
事前送信を参照するためのリソースの広範なリストを提供していますが、各チャネルには個々のニュアンスがあり、製品の進化に伴って成長し続けています。下記のチェックは有益な提案であり、あなたのキャンペーンと大規模な送信を送信前に徹底的にテストすることをお勧めします。
{% endalert %}

## 一般

#### 確認事項
- [**API レート制限**](https://braze.com/resources/articles/whats-rate-limiting):エラーが発生しないように、ワークスペースのブレーズAPI [レート制限]({{site.baseurl}}/api/api_limits/) を確認します。レート制限を増やしたい(すでにリクエストをバッチ処理している)場合は、カスタマーサクセスマネージャーに連絡してください。このプロセスにはリードタイムが必要であることに留意してください。したがって、計画を立ててください。
- [**必要な周波数上限オーバーライド**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping):トランザクションメッセージのように、既に頻度の上限(配信通知など)に達している場合でも、常にユーザに到達したいキャンペーンがいくつかあります。特定のキャンペーンで頻度上限ルールを上書きする場合は、頻度上限をオフに切り替えることで、キャンペーンの配信をスケジュールするときにBraze ダッシュボードでこれを設定できます。

#### 知っておくべきこと
- [**グローバルコントロールグループ**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group):グローバルコントロールグループを使用している場合、パーセンテージのユーザーはキャンペーンまたはキャンバスを受信しません。([除外設定]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)で例外を作成できます)。これらのユーザーのリストを表示するには、CSV または[API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) でエクスポートします。
- [**キャンバスレート制限**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting):キャンバスでは、レート制限は個々のステップではなく、キャンバス全体に適用されます。たとえば、複数のステップを含むキャンバスで1 分あたり10,000 メッセージのレート制限を設定した場合、最初のステップで制限に達するため、メッセージは10,000 メッセージに制限されます。
- **周波数キャッピング**: 
  - 頻度上限ルールは、プッシュ、メール、SMS、およびウェブフックに適用されますが、アプリ内メッセージおよびコンテンツカードには適用されません。
  - グローバル周波数上限は、ユーザのタイムゾーンに基づいてスケジュールされ、24 時間ではなく、カレンダ日によって計算されます。たとえば、1 日に複数のキャンペーンを送信しないという頻度上限ルールを設定した場合、ユーザはローカルタイムゾーンの午後11 時にメッセージを受け取ることができ、1 時間後に別のメッセージを受け取ることができます。

## メール

#### 確認事項
- **お客様の同意**:最初のメールを送信する前に、まず顧客から許可を得ることが重要です。詳細については、[同意およびアドレス収集]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/)および[ブレーズ受け入れ可能使用ポリシー](https://www.braze.com/company/legal/aup)を参照してください。
- **予期ボリューム**:1 つの IP の 1 日あたり 200万 件の E メールは、そのボリュームが [ 適切にウォームアップされている ]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming) である限り、一般的な推奨事項です。 
  - これよりも高いボリュームを常に送信することを計画している場合は、プロバイダがメールの受信をスロットリングして、大量のソフトバウンス、配信可能率の低下、IP レピュテーションの低下を招くことを避けるために、IP プールにバンドルされた複数のIP アドレスの使用を検討してください。 
  - より短い期間のみで送信する場合は、さまざまなプロバイダーがメールを受け入れる速度を調べて、送信元のIP の適切な数を測定することをお勧めします。 

#### 知っておくべきこと
- **送信量係数**:IP に対応する送信ボリュームを決定する要素には、次のものがあります。
  - メールボックス:大規模なメールプロバイダは、1 つのIP から1 日あたり数百万件の処理を行う可能性がありますが、小規模な地域のメールボックスプロバイダまたはインフラストラクチャを備えたプロバイダは、その量を処理できない可能性があります。
  - 送信者の評価:送信者がそのボリュームに上がり、送信者のレピュテーションが送信先のメールボックスまたはドメインごとに十分に強ければ、1 つのIP から1 日に大きなボリュームを送信できます。
- **ベストプラクティス**:Braze [電子メールのベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)を確認し、配信可能サービスの詳細を知りたい場合は、Brazeアカウントチームに連絡してください。

## プッシュ通知

#### 確認事項
- [**Opted-in/subscribed and push enabled**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/):ユーザがBraze からプッシュメッセージを受信するには、ユーザのサブスクリプションステータスがopted-in (iOS) またはsubscribed (Android) および`Push Enabled = True` のいずれかである必要があります。Android 13 では、ユーザがプッシュ通知を送信するアプリを管理する方法に大きな変更が加えられていることに注意してください。Braze [Android 13 SDKアップグレードガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/)は、新しいAndroid 13ベータ版がリリースされるに従い、引き続き更新されます。

#### 知っておくべきこと
- **Web プッシュ**:Braze [Web SDK セットアップ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)を使用している場合は、Web プッシュを使用してユーザーをエンゲージすることを検討してください。Web プッシュは、スマートフォンでアプリプッシュ通知を操作するのと同じように機能します。Web プッシュの作成の詳細については、[プッシュ通知の作成]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)を参照してください。
- **特異なアプリをターゲットにする**:セグメンテーション の[ の違いを確認して、単独のアプリとそのユーザをターゲットにします。

## SMS

#### 確認事項
- **割り当てとスループット**:現在、アカウントにアタッチされている SMS 割り当て (ショートコード、ロングコードなど) と [ のスループットを理解し、必要な時間に送信するのに十分なスループットがあることを確認します。
- **SMSコピーからのセグメントの見積もり**:[SMSセグメント計算機]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy)でSMSコピーをテストします。スループット機能では、SMS セグメントの数を考慮する必要があることに注意してください。(対象読者* SMSセグメント= 必要なスループット)。[オーバーエージを避けるSMS FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/#how-can-i-avoid-overages)を参照してください。
- **SMS法規**:[SMSの法律、規制、および不正使用防止]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)を確認し、適用されるすべての法律に準拠してSMSサービスを使用していることを確認します。送付する前に、必ず弁護士の助言を求めてください。

#### 知っておくべきこと
- **SMSメッセージデフォルト**:通常、SMSメッセージは、送信者プールのショートコードから送信されるようにデフォルト設定されます。
- **英数字送信者ID**:英数字の送信者ID を使用すると、双方向メッセージングは機能しなくなります。これらは現在、一方向のみです。
- **US**で更新されたスループット:米国でスループットが変更されました。[A2P 10DLC 登録](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US)。トラフィックの輻輳やキャリアの問題など、実際の配信レートに影響を与える可能性がある複数の要因があるため、SLAの送信速度を契約で決定することはありません。
- **サブスクリプショングループ**:ブレーズを使用してSMSキャンペーンを起動するには、サブスクリプショングループを選択する必要があります。また、国際的な[電気通信コンプライアンスとガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)を順守するために、Brazeは選択されたサブスクリプショングループに[サブスクライブしていないユーザにSMSを送信することはありません。

## WhatsApp

#### 知っておくべきこと

- [**ベストプラクティス**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/):提案されたWhatsAppのベストプラクティスを確認します。

## コンテンツカード

#### 確認事項
- **コンテンツカードサイズ**:コンテンツカードメッセージフィールドは、タイトル、メッセージ、イメージURL、リンクテキスト、リンクURL、およびキーと値のペアのバイトサイズの長さを加算して計算される、圧縮前のサイズで2KB に制限されます。このサイズを超えるメッセージは送信されません。これには、イメージのサイズではなく、イメージURL の長さが含まれることに注意してください。
- **送信後のコピーの更新**:カードを送信した後、同じカード上のコピーを更新することはできません。このシナリオへのアプローチ方法については、[送信カードの更新]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards)を参照してください。

#### 知っておくべきこと
- **アクティブコンテンツカードキャンペーン制限**:アクティブなコンテンツカードキャンペーンは最大500 件まで設定できます。このカウントには、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)オプションのいずれかで送信されたコンテンツカードが含まれます。  
- [**報告条件**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/):総インプレッション、ユニークなインプレッション、ユニークなレシピエントなどの用語を定義としてレビューすると、混乱を招くことがあります。
- **コンテンツカードリフレッシュ**:デフォルトでは、Brazeは、セッション開始時、フィードダウン時(モバイル)、最後の更新が1分以上前の場合、カードビューが開かれたときに、コンテンツカード要求を更新します。
- **コンテンツカードのキャッシュ**:コンテンツカードのキャッシュオプションは、[Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android)および[Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards)のドキュメントにあります。 
- **周波数キャッピング**:周波数キャッピングは、コンテンツカードには適用されません。
- **印象**:印象は、通常、カードが表示されたときに記録されます。たとえば、コンテンツカードのフル受信ボックスがある場合、ユーザが特定のコンテンツカードにスクロールするまで、インプレッションは記録されません。Web、Android、iOSプラットフォームの間にはいくつかのニュアンスがあります。  

## アプリ内メッセージ

#### 知っておくべきこと
- **アプリ内メッセージトリガ**:セッションの開始時に、SDK は、すべての適格なアプリ内メッセージをトリガーとともにデバイスに送信するよう要求します。そのため、セッション中にイベントを実行すると、アプリ内メッセージを迅速かつ確実に受信できます。このため、アプリ内メッセージはCanvas のカスタムイベントによってトリガーできません。
- **Sent vs. impressions**:アプリ内メッセージの場合、"sented" の概念は、他の使用可能なチャネルとは異なります。アプリ内メッセージを表示するには、ユーザーがセッションを開始し、適格な視聴者にいる必要があり、トリガーを実行する必要があります。このため、"impressions"がより明確になるように追跡します。
- **トリガ**:デフォルトでは、アプリ内メッセージはSDKによってログに記録されたイベントによってトリガーされます。サーバーから送信されたイベントによってアプリ内メッセージをトリガーする場合は、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/custom_triggering/) および[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization) のこれらのガイドを使用してこれを実行することもできます。
- [**アプリ内のメッセージ**]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options):これらのメッセージは、キャンバスコンポーネントでスケジュールされたメッセージが送信された後、ユーザーがアプリを初めて開いたときに表示されます(開始セッションによってトリガーされます)。
