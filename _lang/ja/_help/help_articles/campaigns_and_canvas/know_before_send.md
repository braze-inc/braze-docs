---
nav_title: 送る前に知っておこう
article_title: 送る前に知っておこう
description: "プレローンチ・ガイドをご覧になった後は、コンテンツカード、メール、アプリ内メッセージ、プッシュ、SMSの最終チェックリストや \"gotchas \"をご参照いただきたい。"
alias: /know_before_send/

---

# 送信する前に知っておこう：チャネル

キャンペーンとキャンバスを自信を持って立ち上げよう！コンテンツカード、メール、アプリ内メッセージ、プッシュ、SMSに関する最後のチェックリストや "gotchas "を参照のこと。

{% alert note %}
送信前に参照できるリソースの広範なリストを提供しているが、各チャネルには個別のニュアンスがあり、製品を進化させるにつれて増え続けている。以下に挙げるチェックは参考となる提案であり、送信前にキャンペーンや大量送信を徹底的にテストすることをお勧めする。
{% endalert %}

## 全般的な質問

#### チェックすべきこと
- [**APIレート制限**](https://braze.com/resources/articles/whats-rate-limiting):エラーにならないように、ワークスペースのBraze API[レート制限を]({{site.baseurl}}/api/api_limits/)確認する。レート制限を増やしたいとお考えの場合（すでにバッチ処理をしている場合）、カスタマー・サクセス・マネージャーにご相談いただきたい。このプロセスにはリードタイムが必要であることを念頭に置き、それなりの計画を立てること。
- [**必要なフリークエンシーキャップオーバーライド**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping):トランザクションメッセージのように、すでにフリークエンシーキャップに達していても、常にユーザーに届けたいキャンペーンもある（例えば、配送通知）。特定のキャンペーンでフリークエンシーキャップルールを無効にしたい場合は、ダッシュボードでフリークエンシーキャップオフを設定することで、そのキャンペーンの配信スケジュールされた際に設定できる。

#### 知っておくべきこと
- [**グローバルコントロールグループ**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group):グローバルコントロールグループを使用している場合、何パーセントかのユーザーはキャンペーンやキャンバスを受け取らない。[(除外]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)設定で例外を作ることができる）。これらのユーザーのリストを見るには、CSVまたは[API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)経由でエクスポートする。
- [**キャンバスレート制限**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting):キャンバスでは、レート制限は個々のステップではなく、キャンバス全体に適用される。例えば、複数のステップを持つキャンバスに1分あたり10,000メッセージのレート制限を設定しても、最初のステップで制限に達しているため、10,000メッセージに制限される。
- **フリークエンシーキャップ**： 
  - フリークエンシーキャップルールは、プッシュ、メール、SMS、Webhookにはアプリ内メッセージとコンテンツカードには適用されない。
  - グローバルフリークエンシーキャップは、ユーザーのタイムゾーンに基づいてスケジュールされ、24時間ではなく暦日で計算される。例えば、1日に1回までしかキャンペーンを送信しないというフリークエンシーキャップ・ルールを設定した場合、ユーザーはローカルタイムゾーンで午後11時にメッセージを受信し、その1時間後に別のメッセージを受信することができる。

{% alert tip %}
キャンバスやキャンペーンのトラブルシューティングについては、過去30日分の診断ログしか残っていないため、問題発生から30日以内に必ずBrazeサポートまでご連絡ください。
{% endalert %}

## メール

#### チェックすべきこと
- **顧客の同意**：最初のメールを送る前に、まず顧客の同意を得ることが重要だ。詳細については、「[同意とアドレスの収集]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/)」および「[Braze Acceptable Use Policy](https://www.braze.com/company/legal/aup)」を参照のこと。
- **予想される数量**単一IPで1日200万メールは、そのボリュームが[適切にウォームアップ]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming)されている限り、一般的な推奨である。 
  - これ以上の量をコンスタントに送信する場合は、プロバイダーがメールの受信を制限し、ソフトバウンスの多発、メールの信頼度および到達配信性の低下、IPレピュテーションの低下を招かないよう、複数のIPアドレスをIPプールにバンドルして使用することを検討する。 
  - 短時間での送信を考えているのであれば、送信元IPの適切な数を測るために、さまざまなプロバイダーがどのくらい早くメールを受け付けるかを調べることをお勧めする。 

#### 知っておくべきこと
- **送信量係数**：IPの送信可能量を決定する要因には、以下のようなものがある：
  - メールボックス大手のメールプロバイダーは、1つのIPから1日に数百万件のメールを処理できるだろうが、地方の小規模なメールボックスプロバイダーやインフラが小さいプロバイダーは、その量を処理できないかもしれない。
  - 送信者の評判送信者がその量まで増員され、送信先のメールボックスやドメインごとに送信者のレピュテーションが十分に高ければ、1つのIPから1日に大量のメールを送信できるかもしれない。
- **ベストプラクティス**だ：Braze[メールのベストプラクティスを]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)学習し、配信サービスについて詳しく知りたい場合は、Brazeアカウントチームに連絡する。

## プッシュ

#### チェックすべきこと
- [**オプトイン/サブスクライバーとプッシュを有効にする**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/):ユーザーがBrazeからのプッシュメッセージを受信するには、サブスクリプションのステータスがオプトイン（iOS）またはサブスクライブ（Android）であり、`Push Enabled = True` 。なお、Android 13では、プッシュ通知を送信するアプリをユーザーが管理する方法に大きな変更が加えられている。Braze[Android 13 SDKアップグレードガイドは]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/)、新しいAndroid 13ベータ版がリリースされるたびに更新され続ける。

#### 知っておくべきこと
- **Web プッシュ**:Braze[Web SDKをセットアップして]({{site.baseurl}}/user_guide/message_building_by_channel/push/web)いる場合は、ユーザーをエンゲージするためにWebプッシュを利用することを検討する。Webプッシュは、携帯電話のアプリ・プッシュ通知と同じように機能する。Webプッシュの作成については、[プッシュ通知の]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)作成を参照のこと。
- Singular**アプリをターゲットにする**：Singularアプリとそのユーザーをターゲットとする[セグメンテーションの違いを]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app)確認する。

## SMS

#### チェックすべきこと
- **割り当てと処理能力**現在アカウントに割り当てられているSMS（ショートコード、ロングコード、その他類似のもの）と、[そのスループットを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/)把握し、希望する時間帯に送信するのに十分なスループットがあることを確認する。
- **SMSのコピーからセグメンテーションを推定**する：SMS[セグメント計算機で]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy)SMSコピーをテストする。SMSのセグメンテーションの数は、スループット能力を考慮する必要があることに留意されたい。(Audience * SMS segments = Throughput needed).[超過料金の回避については]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/#how-can-i-avoid-overages)、SMS FAQを参照のこと。
- **SMSに関する法律と規制**：[SMSに関する法律、規制、および悪用防止を確認]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)し、適用されるすべての法律を遵守してSMSサービスを使用していることを確認する。発送前に必ず法律顧問の助言を求めること。

#### 知っておくべきこと
- **SMSメッセージのデフォルト**：SMSメッセージは通常、デフォルトで送信者プールのショートコードから送信される。
- **英数字の送信者ID**：英数字の送信者IDを使用した場合、双方向メッセージングは機能しなくなる。
- **米国での処理能力を更新**した：米国の[A2P 10DLC登録により](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US)、スループットが変化した。トラフィックの混雑やキャリアの問題など、実際の配信速度に影響を与える可能性のある複数の要因があるため、契約上、送信速度のSLAを約束するものではないことに留意されたい。
- **サブスクリプショングループ**：Brazeを通じてSMSキャンペーンを開始するには、サブスクリプショングループを選択する必要がある。また、国際[通信コンプライアンスとガイドラインを]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)遵守するため、Brazeは[選択したサブスクリプショングループに加入して]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group)いないユーザーにSMSを送信することはない。

## WhatsApp

#### 知っておくべきこと

- [**ベストプラクティス**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/):WhatsAppのベストプラクティスを確認する。

## コンテンツカードによって促進された

#### チェックすべきこと
- **コンテンツカードのサイズ**：コンテンツカードのメッセージフィールドの圧縮前のサイズは、タイトル、メッセージ、画像URL、リンクテキスト、リンクURL、キーと値のペアなどのフィールドのバイトサイズを足した2KBに制限されている。このサイズを超えるメッセージングは送信されない。これは画像サイズではなく、画像URLの長さである。
- **送信後にコピーを更新**する：カードが送信された後、同じカードのコピーを更新することはできない。このシナリオへのアプローチ方法については、「[送られたカードの更新]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards)」を参照のこと。

#### 知っておくべきこと
- **アクティブコンテンツカードキャンペーンの制限**：コンテンツカードキャンペーンは最大500件まで有効である。このカウントには、いずれかの[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)オプションで送信されたコンテンツカードが含まれる。  
- [**レポート用語**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/):総インプレッション数、ユニークインプレッション数、ユニーク受信者数といった用語の定義が混乱を招くことがあるため、その定義を確認すること。
- **コンテンツカードを一新した**：デフォルトでは、Brazeは、セッション開始時、フィードダウンスワイプ時（モバイル）、および前回の更新が1分以上前であれば、カードビュー開封時に、コンテンツカードリクエストを同期しながら更新する。
- **コンテンツカードをキャッシュ**する：コンテンツカードのキャッシングオプションは、[Android/FireOSと]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) [Webの](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards)ドキュメントに記載されている。 
- **フリークエンシーキャップ**：フリークエンシーキャップはコンテンツカードには適用されない。
- **インプレッション**だ：インプレッションは通常、カードを見たときに記録される。例えば、コンテンツカードの受信トレイがいっぱいにある場合、ユーザーが特定のコンテンツカードまでスクロールするまで、インプレッションは記録されない。Web、Android、iOSの各プラットフォームには微妙な違いがある。  

## アプリ内メッセージ

#### 知っておくべきこと
- **アプリ内メッセージトリガー**：セッション開始時に、SDKはすべての適格なアプリ内メッセージをトリガーとともにデバイスに送信するよう要求する。そのため、セッション中にイベントを実行すれば、迅速かつ確実にアプリ内メッセージを受け取ることができる。このため、アプリ内メッセージをキャンバスのカスタムイベントでトリガーすることはできない。
- **送信対インプレッション**：アプリ内メッセージの場合、「送信」の概念は他の利用可能なチャネルとは異なる。アプリ内メッセージを見るためには、ユーザーはセッションを開始し、対象となるオーディエンスに属し、トリガーを実行する必要がある。そのため、より明確な「インプレッション」を追跡している。
- **トリガー**:デフォルトでは、アプリ内メッセージは SDK によって記録されるイベントによってトリガーされます。サーバーから送信されるイベントによってアプリ内メッセージをトリガーしたい場合は、[iOSと]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/custom_triggering/) [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization)用の以下のガイドを参照することでも実現できる。
- [**アプリ内キャンバスメッセージ**]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options):これらのメッセージは、キャンバスコンポーネント内のスケジュールされたメッセージがユーザーに送信された後、ユーザーがアプリを初めて開封した時（スタートセッションがトリガー）に表示される。
