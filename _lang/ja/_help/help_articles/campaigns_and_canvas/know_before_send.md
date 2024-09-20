---
nav_title: 送信する前に知っておくべきこと
article_title: 送信する前に知っておくべきこと
description: "事前ローンチガイドを訪問した後、コンテンツカード、メール、アプリ内メッセージ、プッシュ、SMSの最終チェックリストまたは「落とし穴」を参照してください。"
alias: /know_before_send/

---

# 送信する前に知っておくべきこと: チャンネル

自信を持ってキャンペーンとキャンバスを開始しましょう！コンテンツカード、メール、アプリ内メッセージ、プッシュ、SMSの最終チェックリストまたは「注意点」を参照してください。

{% alert note %}
私たちは送信前に参照するための豊富なリソースリストを提供していますが、各チャネルには個別のニュアンスがあり、製品の進化に伴って成長し続けています。以下にリストされているチェックは役立つ提案であり、送信する前にキャンペーンや大規模な送信を徹底的にテストすることをお勧めします。
{% endalert %}

## 全般的な質問

#### 確認すること
- [**APIレート制限**](https://braze.com/resources/articles/whats-rate-limiting):ワークスペースでエラーが発生しないように、Braze API [レート制限]({{site.baseurl}}/api/api_limits/) を確認してください。レート制限を増やしたい場合（すでにリクエストをバッチ処理している場合）、顧客成功マネージャーに連絡してください。このプロセスにはリードタイムが必要であることを念頭に置いて、計画を立ててください。
- [**必要なフリークエンシーキャップのオーバーライド**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping):いくつかのキャンペーン、例えばトランザクションメッセージなどは、たとえ頻度制限に達していても、常にユーザーに届くようにしたいものです（例えば、配達通知）。特定のキャンペーンがフリークエンシーキャップのルールを上書きするようにしたい場合は、そのキャンペーンの配信をスケジュールする際にBrazeダッシュボードでフリークエンシーキャップをオフに切り替えることで設定できます。

#### 知っておくべきこと
- [**グローバルコントロールグループ**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group):グローバルコントロールグループを使用している場合、ユーザーの一部はキャンペーンやキャンバスを受け取りません。（[除外設定]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)で例外を作成できます）。これらのユーザーのリストを表示するには、CSVまたは[API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)経由でエクスポートします。
- [**キャンバスレート制限**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting):キャンバスでは、レート制限は個々のステップではなく、キャンバス全体に適用されます。例えば、複数のステップを持つキャンバスに1分あたり10,000メッセージのレート制限を設定した場合でも、最初のステップで制限に達するため、メッセージは10,000に制限されます。
- **フリークエンシーキャップ**: 
  - フリークエンシーキャップのルールはプッシュ、メール、SMS、およびwebhookに適用されますが、アプリ内メッセージとコンテンツカードには適用されません。
  - グローバルフリークエンシーキャップはユーザーのタイムゾーンに基づいてスケジュールされ、24時間ではなくカレンダーデイによって計算されます。例えば、1日に1回以上キャンペーンを送信しないというフリークエンシーキャップのルールを設定した場合、ユーザーはローカルタイムゾーンで午後11時にメッセージを受信し、1時間後に別のメッセージを受信する資格があります。

{% alert tip %}
キャンバスおよびキャンペーンのトラブルシューティングに関するさらなる支援については、問題が発生してから30日以内にBrazeサポートに連絡してください。診断ログは過去30日分しか保存されていません。
{% endalert %}

## メール

#### 確認すること
- **顧客の同意**:最初のメールを送信する前に、まず顧客の許可を得ることが重要です。[同意とアドレスの収集]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/)および当社の[Braze許容使用ポリシー](https://www.braze.com/company/legal/aup)についての詳細をご参照ください。
- **予想されるボリューム**:1日あたり200万通のメールを1つのIPで送信することは、そのボリュームが[適切にウォームアップされている]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming)限り、一般的に推奨されます。 
  - もしこれよりも多くのメールを定期的に送信する予定がある場合、プロバイダーがメールの受信を制限し、ソフトバウンスの増加、配信率の低下、IPの評判の低下を避けるために、複数のIPアドレスをIPプールにまとめて使用することを検討してください。 
  - 短期間で送信したい場合は、異なるプロバイダーがメールを受け入れる速度を調べて、送信元のIP数を適切に判断することをお勧めします。 

#### 知っておくべきこと
- **送信量の要因**:IP の送信可能なボリュームを決定する要因には次のものがあります:
  - メールボックス:大手のメールプロバイダーは、単一のIPから1日に数百万通を処理できる可能性がありますが、地域の小規模なメールボックスプロバイダーやインフラが小規模なプロバイダーは、その量を処理できないかもしれません。
  - 送信者の評判:送信者がそのボリュームに増加し、各メールボックスまたはドメインでの送信者の評判が十分に強ければ、単一のIPから1日により多くのボリュームを送信できる可能性があります。
- **ベストプラクティス**:Braze [メールのベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)を確認し、配信サービスについて詳しく知りたい場合は、Brazeアカウントチームにお問い合わせください。

## プッシュ

#### 確認すること
- [**オプトイン/サブスクライブおよびプッシュ有効**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/):ユーザーがBrazeからプッシュメッセージを受信するには、サブスクリプションステータスがオプトイン（iOS）またはサブスクライブ（Android）である必要があり、`Push Enabled = True`。Android 13では、プッシュ通知を送信するアプリの管理方法に大きな変更が導入されていることに注意してください。Braze [Android 13 SDK アップグレードガイド]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/) は、新しい Android 13 ベータ版がリリースされるたびに更新され続けます。

#### 知っておくべきこと
- **Web プッシュ**:Braze [Web SDK のセットアップ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) がある場合は、ユーザーを引き付けるために Web プッシュを利用することを検討してください。Web プッシュは、アプリのプッシュ通知があなたの電話で動作するのと同じ方法で動作します。Web プッシュの作成に関する詳細については、[プッシュ通知の作成]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)をチェックしてください。
- **単一のアプリをターゲットにする**:セグメンテーションの[違い]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app)を確認して、Singularアプリとそのユーザーをターゲットにします。

## SMS

#### 確認すること
- **割り当てとスループット**:現在アカウントに割り当てられているSMSの割り当て（ショートコード、ロングコードなど）と[それが提供するスループットの量]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_setup/short_and_long_codes/)を理解して、希望する時間内に送信するのに十分なスループットがあることを確認してください。
- **SMSコピーからセグメントを見積もる**:[SMS Segment 計算機]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy)でSMSコピーをテストします。SMSセグメントの数は、スループット能力を考慮する必要があります。(Audience * SMS segments = Throughput needed).SMS FAQの[超過料金を回避する方法]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/#how-can-i-avoid-overages)を参照してください。
- **SMSの法律と規制**:[SMSの法律、規制、および乱用防止を確認して]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)、すべての適用法に準拠してSMSサービスを使用していることを確認してください。送信する前に、必ず法律顧問の助言を求めてください。

#### 知っておくべきこと
- **SMSメッセージのデフォルト設定**:SMSメッセージは通常、送信者プールのショートコードから送信されるようにデフォルト設定されています。
- **英数字送信者ID**:双方向メッセージングは、英数字の送信者IDを使用すると機能しなくなります。これらは現在、片方向のみです。
- **米国のスループットが更新されました**:米国では、米国[A2P 10DLC登録](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US)によりスループットが変更されました。交通渋滞やキャリアの問題など、実際の配信率に影響を与える複数の要因により、送信速度のSLAを契約上保証することはありませんのでご注意ください。
- **サブスクリプショングループ**:Brazeを通じてSMSキャンペーンを開始するには、サブスクリプショングループを選択する必要があります。また、国際的な[電気通信のコンプライアンスとガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/)に従うために、Brazeは選択されたサブスクリプショングループに[登録していない]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group)ユーザーにSMSを送信することはありません。

## WhatsApp

#### 知っておくべきこと

- [**ベストプラクティス**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/):WhatsAppのベストプラクティスを確認してください。

## コンテンツカードによって促進された

#### 確認すること
- **コンテンツカード size**:コンテンツカードメッセージフィールドは、次のフィールドのバイトサイズ長を合計して計算した場合、圧縮前のサイズが2 KBに制限されています: タイトル、メッセージ、画像URL、リンクテキスト、リンクURL、およびキーと値のペア。このサイズを超えるメッセージは送信されません。このサイズには画像のサイズではなく、画像URLの長さが含まれます。
- **送信後のコピーを更新**:カードが送信された後、同じカードのコピーを更新することはできません。[送信済みカードの更新]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards)を参照して、このシナリオにどのように対処するかを理解してください。

#### 知っておくべきこと
- **アクティブなコンテンツカードキャンペーンの制限**:アクティブなコンテンツカードキャンペーンは最大500件まで作成できます。このカウントには、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)オプションのいずれかで送信されたコンテンツカードが含まれます。  
- [**報告用語**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/):総インプレッション数、ユニークインプレッション数、ユニーク受信者などの用語を確認してください。定義が混乱を招くことがあります。
- **コンテンツカードの更新**:デフォルトでは、Brazeはセッション開始時、フィードの下スワイプ（モバイル）、および最後の更新が1分以上前である場合にカードビューが開かれたときに、コンテンツカードリクエストを同期して更新します。
- **コンテンツカードのキャッシュ**:コンテンツカードのキャッシュオプションは、当社の[Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android)および[Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards)のドキュメントにあります。 
- **フリークエンシーキャップ**:フリークエンシーキャップはコンテンツカードには適用されません。
- **印象**:インプレッションは通常、カードが表示されたときに記録されます。例えば、受信トレイがコンテンツカードでいっぱいの場合、ユーザーが特定のコンテンツカードまでスクロールするまでインプレッションは記録されません。Web、Android、iOSプラットフォームの間にはいくつかのニュアンスがあります。  

## アプリ内メッセージ

#### 知っておくべきこと
- **アプリ内メッセージトリガー**:セッションの開始時に、SDKはすべての対象となるアプリ内メッセージをトリガーとともにデバイスに送信するよう要求します。そのため、セッション中にイベントを実行すると、アプリ内メッセージを迅速かつ確実に受信できます。このため、キャンバス内のカスタムイベントによってアプリ内メッセージをトリガーすることはできません。
- **送信対インプレッション**:アプリ内メッセージの場合、「送信済み」の概念は他の利用可能なチャネルとは異なります。アプリ内メッセージを見るには、ユーザーがセッションを開始し、対象のオーディエンスに属し、トリガーを実行する必要があります。このため、「インプレッション」を追跡しています。これはより明確です。
- **トリガー**:デフォルトでは、アプリ内メッセージは SDK によって記録されるイベントによってトリガーされます。サーバー送信イベントによってアプリ内メッセージをトリガーしたい場合、[iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/custom_triggering/)および[Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization)向けのこれらのガイドを通じてこれを達成することもできます。
- [**アプリ内メッセージのキャンバス**]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options):これらのメッセージは、スケジュールされたメッセージがキャンバスコンポーネントで送信された後、ユーザーがアプリを初めて開いたとき（セッションの開始によってトリガーされます）に表示されます。
