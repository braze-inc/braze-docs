---
nav_title: 送る前に知っておこう
article_title: 送る前に知っておこう
description: "私たちのプレローンチガイドを訪問した後、コンテンツカード、メール、アプリ内メッセージ、プッシュ、SMSについては、この最終的なチェックリストまたは「gotcha」を参照してください。"
alias: /know_before_send/
page_order: 10.2
tool:
    - Campaigns
    - Canvas
---

# 送信する前に知っておくべきこと: チャンネル

キャンペーンとキャンバスを自信を持って開始しましょう。コンテンツカード、メール、アプリ内メッセージ、プッシュ、SMSの最終チェックリストまたは「注意点」を参照してください。

{% alert note %}
私たちは送信前に参照するための豊富なリソースリストを提供していますが、各チャネルには個別のニュアンスがあり、製品の進化に伴って成長し続けています。以下のチェックを参考にして、キャンペーンと大量の送信を徹底的にテストしてから送信することをお勧めします。
{% endalert %}

## 全般的な質問

#### 確認事項
- [**API レート制限**](https://braze.com/resources/articles/whats-rate-limiting): ワークスペースでエラーが発生しないように、Braze API [レート制限]({{site.baseurl}}/api/api_limits/) を確認してください。レート制限の引き上げを検討している （すでにリクエストをバッチ処理している) 場合は、カスタマーサクセスマネージャーにお問い合わせください。このプロセスにはリードタイムが必要であることを念頭に置いて、計画を立ててください。
- [**必要なフリークエンシーキャップの無効化**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): いくつかのキャンペーン、例えばトランザクションメッセージなどは、たとえ頻度制限に達していても、常にユーザーに届くようにしたいものです（例えば、配達通知）。特定のキャンペーンでフリークエンシーキャップルールを無効にしたい場合は、フリークエンシーキャップをオフに切り替えて、そのキャンペーンの配信をスケジュールするときに Braze ダッシュボードで設定できます。

#### 知っておくべきこと
- [**グローバルコントロールグループ**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group):グローバルコントロールグループを使用している場合、ユーザーの一部はキャンペーンやキャンバスを受け取りません。（[除外設定]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)で例外を作成できます）。これらのユーザーの一覧を表示するには、CSV または [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/) でエクスポートします。
- [**キャンバスレート制限**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): キャンバスでは、レート制限は個々のステップではなく、キャンバス全体に適用されます。例えば、複数のステップを持つキャンバスに1分あたり10,000メッセージのレート制限を設定した場合でも、最初のステップで制限に達するため、メッセージは10,000に制限されます。
- **フリークエンシーキャップ**: 
  - フリークエンシーキャップのルールはプッシュ、メール、SMS、およびwebhookに適用されますが、アプリ内メッセージとコンテンツカードには適用されません。
  - グローバルフリークエンシーキャップはユーザーのタイムゾーンに基づいてスケジュールされ、24時間単位ではなく暦日単位で計算されます。例えば、1日に1回以上キャンペーンを送信しないというフリークエンシーキャップのルールを設定した場合、ユーザーはローカルタイムゾーンで午後11時にメッセージを受信し、1時間後に別のメッセージを受信する資格があります。

{% alert tip %}
キャンバスおよびキャンペーンのトラブルシューティングに関する詳細については、過去30日間の診断ログしかないため、問題が発生してから30日間以内にBrazeサポートに連絡してください。
{% endalert %}

## メール

#### 確認事項
- **顧客の同意**: 最初のメールを送信する前に、まず顧客の許可を得ることが重要です。[同意とアドレスの収集]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/)および当社の[Braze許容使用ポリシー](https://www.braze.com/company/legal/aup)についての詳細をご参照ください。
- **推奨ボリューム**: [適切にウォームアップされている]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming)場合、1つのIPに対して1日あたり200万通のメールが一般的な推奨値になります。 
  - これよりも大量のメールを継続的に送信する予定がある場合は、プロバイダーがメールの受信を制限して大量のソフトバウンスや配信可能性および IP レピュテーションの低下が発生しないよう、複数の IP アドレスを IP プールにバンドルすることを検討してください。 
  - より短い期間内でのみ送信する予定の場合は、さまざまなプロバイダーがメールを受け入れる速度を調べ、送信元として適切な IP の数を判断することをお勧めします。 

#### 知っておくべきこと
- **送信ボリュームの決定要素**: IP に対応する送信ボリュームを決定する要素には、次のものがあります。
  - メールボックス:大手のメールプロバイダーは、単一のIPから1日に数百万通を処理できる可能性がありますが、地域の小規模なメールボックスプロバイダーやインフラが小規模なプロバイダーは、その量を処理できないかもしれません。
  - 送信者レピュテーション: 送信者が送信ボリュームを増やし、送信先の各メールボックスまたはドメインでの送信者のレピュテーションが十分に高い場合は、単一 IP からの1日あたりの送信ボリュームを増やせる可能性があります。
- **ベストプラクティス**: Braze の[メールのベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices)を確認し、配信サービスについて詳しく知りたい場合は Braze アカウントチームにお問い合わせください。

## プッシュ

#### 確認事項
- [**Opted-in/subscribed and push enabled**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/):ユーザーが Braze からプッシュメッセージを受信するには、サブスクリプションステータスがオプトイン済み (iOS) またはサブスクリプション登録済み (Android) および `Push Enabled = True` になっている必要があります。Android 13では、ユーザーsがプッシュ通知sを送信するアプリsを管理する方法に大きな変更を導入していることに注意してください。Braze [Android 13 SDK アップグレードガイド]({{site.baseurl}}/developer_guide/platforms/android/android_13/) は、新しい Android 13 ベータ版がリリースされるたびに更新され続けます。

#### 知っておくべきこと
- **Web プッシュ**:Braze [Web SDK のセットアップ]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) がある場合は、ユーザーを引き付けるために Web プッシュを利用することを検討してください。Web プッシュは、スマートフォンでのアプリのプッシュ通知と同様に機能します。Web プッシュの作成に関する詳細については、[プッシュ通知の作成]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)をチェックしてください。
- **単一アプリのターゲット設定**: 単一アプリとそのユーザーをターゲットに設定するため、[セグメンテーションの違い]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app)を確認します。

## SMS

#### 確認事項
- **割り当てとスループット**: 現在アカウントに割り当てられているSMSの割り当て（ショートコード、ロングコードなど）と[それが提供するスループットの量]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/)を理解して、希望する時間内に送信するのに十分なスループットがあることを確認してください。
- **SMS コピーからのセグメント推定**: [SMS Segment 計算機]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy)でSMSコピーをテストします。SMS セグメントの数はスループット能力と合わせて考慮する必要があることに注意してください。(Audience * SMS segments = Throughput needed).SMS FAQの[超過料金を回避する方法]({{site.baseurl}}/sms_faq/)を参照してください。
- **SMSの法律と規制**:[SMSの法律、規制、および乱用防止を確認して]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)、すべての適用法に準拠してSMSサービスを使用していることを確認してください。送信する前に、必ず法律顧問の助言を求めてください。

#### 知っておくべきこと
- **SMS メールデフォルト**: SMSメッセージは通常、送信者プールのショートコードから送信されるようにデフォルト設定されています。
- **英数字の送信者 ID**: 双方向メッセージングは、英数字の送信者IDを使用すると機能しなくなります。これらは現在、片方向のみです。
- **米国でのスループット更新**: 米国では、米国[A2P 10DLC登録](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US)によりスループットが変更されました。トラフィックの輻輳やキャリアの問題など、実際の配信レートに影響を与える可能性がある複数の要因があるため、SLAの送信速度を契約で決定することはありません。
- **サブスクリプショングループ**:Brazeを通じてSMSキャンペーンを開始するには、サブスクリプショングループを選択する必要があります。また、国際的な[電気通信のコンプライアンスとガイドライン]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/)に従うために、Brazeは選択されたサブスクリプショングループに[登録していない]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group)ユーザーにSMSを送信することはありません。

## WhatsApp

#### 知っておくべきこと

- [**ベストプラクティス**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/):提案されたWhatsAppのベストプラクティスを確認します。

## バナー

#### 確認事項
- **バナーの寸法:**固定寸法のエレメントを使ってバナーを作り、エディターでテストする。
- **優先度:**複数のバナーを起動する場合には、各バナーの表示方法の優先度を手動で設定できます。

#### 知っておくべきこと
- **Liquid のパーソナライゼーション:**リキッドパーソナライゼーションは、リフレッシュリクエストごとにリフレッシュされる。
- **配置とバナーの比率:**各バナーの配置は、ワークスペース内の最大10件のキャンペーンで使用できます。  
- **クリック数とインプレッション数:**バナーのクリック数とインプレッション数は SDK で自動的に追跡されます。
- **制限事項:** 現在サポートされていない機能はキャンバスとの統合、APIトリガーおよびアクションベースのキャンペーン、コネクテッドコンテンツ、プロモーションコード、ユーザーコントロールによる解除、[`:rerender` タグを]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid)使用した`catalog_items` 。
- **テスト:**テストバナーを表示するには、使用しているデバイスがフォアグラウンドプッシュ通知を受信できる必要があります。
- **カスタムHTML：**リンクやボタンなどのクリックアクションを定義するためにカスタムHTMLを使用する場合、[JSブリッジを]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge)活用してクリックを記録する。クリックアクションが自動的に記録されるのは、ドラッグ＆ドロップエディターで作成済みのコンポーネントを使用する場合に限られます。
- **配置の要求:**1回のリフレッシュ・リクエストで、SDKに最大10個のプレースメントを返すことができる。各配置には、ユーザーに対して表示できる優先度が最も高いバナーが含まれます。

## コンテンツカードによって促進された

#### 確認事項
- **コンテンツカードのサイズ**: コンテンツカードのメッセージフィールドは、圧縮前のサイズが2 KB に制限されています。この値は、タイトル、メッセージ、画像 URL、リンクテキスト、リンク URL、キーと値のペアの各フィールドのバイトサイズの長さを加算して計算されます。このサイズを超えるメッセージは送信されません。このサイズには画像のサイズではなく、画像URLの長さが含まれます。
- **送信後のコピーの更新**:カードが送信された後、同じカードのコピーを更新することはできません。このシナリオへのアプローチ方法については、「[送信されたカードの更新]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards)」を参照してください。

#### 知っておくべきこと
- **アクティブコンテンツカードキャンペーンの制限**: アクティブコンテンツカードキャンペーンの上限は500件です。このカウントには、[カード作成]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/)オプションのいずれかで送信されたコンテンツカードが含まれます。  
- [**レポート条件**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): 総インプレッション数、ユニークインプレッション数、ユニーク受信者などの用語を確認してください。定義が混乱を招くことがあります。
- **コンテンツカードの更新**: デフォルトでは、Braze は、セッション開始時、フィードダウンスワイプ時 (モバイル)、および最後の更新が1分以上前の場合はカードビューが開かれたときに、コンテンツ カードリクエストを同期して更新します。
- **コンテンツカードのキャッシュ**: コンテンツカードのキャッシュオプションは、当社の[Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android)および[Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards)のドキュメントにあります。 
- **フリークエンシーキャップ**:フリークエンシーキャップは、コンテンツカードには適用されません。
- **インプレッション**: 印象は一般的にカードが見られたときに記録されます。例えば、受信トレイがコンテンツカードでいっぱいの場合、ユーザーが特定のコンテンツカードまでスクロールするまでインプレッションは記録されません。Web、Android、iOS の各プラットフォームには若干の違いがあります。  

## アプリ内メッセージ

#### 知っておくべきこと
- **アプリ内メッセージトリガー**: セッションの開始時に、SDK は、すべての適格アプリ内メッセージをトリガーとともにデバイスに送信するように要求します。そのため、セッション中にイベントを実行すると、アプリ内メッセージを迅速かつ確実に受信できます。
- **送信済みとインプレッション**: アプリ内メッセージの場合、「送信済み」の概念は他の利用可能なチャネルとは異なります。アプリ内メッセージを表示するには、ユーザーがセッションを開始し、適格オーディエンスに含まれ、トリガーを実行する必要があります。このため、「インプレッション」を追跡しています。これはより明確です。
- **トリガー**:デフォルトでは、アプリ内メッセージは SDK によって記録されるイベントによってトリガーされます。サーバー送信イベントによってアプリ内メッセージをトリガーしたい場合、[iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift)および[Android]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android)向けのこれらのガイドを通じてこれを達成することもできます。
- [キャンバスのアプリ内メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options):キャンバスコンポーネントでスケジュールされたメッセージがユーザーに送信された後、ユーザーが (開始セッションによってトリガーされて) 初めてアプリを開いたときに、これらのメッセージが表示されます。
- **コネクテッドコンテンツ呼び出し**:コネクテッドコンテンツを使えば、メッセージングでダイナミックなコンテンツを送ることができます。アプリ内メッセージのようなチャネルを通じてメッセージを送信する場合、ユーザーのデバイスにより多くの同時接続を作り出すことができる（メッセージはバッチではなく1つずつ送信される）。これを管理するには、メッセージの[レート制限をする]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting)ことをお勧めします。
