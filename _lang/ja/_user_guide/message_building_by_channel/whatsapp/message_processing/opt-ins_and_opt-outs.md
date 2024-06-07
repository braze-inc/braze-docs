---
nav_title: オプトインとオプトアウト
article_title: WhatsAppのオプトインとオプトアウト
description: "この参考記事ではWhatsAppのオプトインとオプトアウトの様々な方法をご紹介します。"
page_type: partner
search_tag: Partner
page_order: 5
channel:
  - WhatsApp
alias: /user_guide/message_building_by_channel/whatsapp/opt-ins_and_opt-outs/
---

# オプトインとオプトアウト

> WhatsAppのオプトインとオプトアウトは非常に重要です。WhatsAppはお客様の[電話番号の品質評価を](https://www.facebook.com/business/help/896873687365001)監視しており、評価が低いとメッセージの上限が減る可能性があります。質の高い評価を保証する一つの方法は、ユーザーによるブロックや報告を防ぐことです。これは、[質の高いメッセージング](https://developers.facebook.com/docs/whatsapp/messaging-limits#quality-rating-and-messaging-limits)（ユーザーにとっての価値など）を提供し、メッセージの頻度をコントロールし、顧客が今後のコミュニケーション受信をオプトアウトできるようにすることで実現できる。 

オプトインは、外部ソースから、またはSMSやアプリ内メッセージ、ブラウザ内メッセージなどのBrazeの方法から得ることができます。オプトアウトは、Brazeで設定したキーワードとWhatsAppのマーケティングボタンで対応できます。オプトインとオプトアウトの設定方法については、以下の方法を参照してください。 

#### オプトイン方法
- [外部からのオプトイン方式](#external-to-braze-opt-in-methods)
  - [外部オプトインリスト](#externally-built-opt-in-list)
  - [カスタマーサポートWhatsAppチャンネルのアウトバウンドメッセージ](#outbound-message-in-customer-support-whatsapp-channel)
  - [WhatsAppメッセージ](#inbound-whatsapp-message)
- [ブレーズを利用したオプトイン・メソッド](#braze-powered-opt-in-methods)

#### オプトアウトの方法
- [一般的なオプトアウト・キーワード](#general-opt-out-keywords)
- [マーケティング・オプトアウトの選択](#marketing-opt-out-selection)

## Braze WhatsAppチャンネルのオプトイン設定

WhatsAppオプトインについては、[WhatsAppの要件に](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/)準拠する必要があります。また、Brazeに以下の情報を提供する必要があります：
\- 各ユーザーの`external_id` 、[電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/)、最新の購読状況。これは、[SDKを](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)使用するか、[`/users/track` エンドポイントを](https://www.braze.com/docs/api/endpoints/user_data/post_user_track/)使用して、電話番号とサブスクリプションのステータスを更新することによって行うことができます。 

{% alert note %}
Brazeは、[サブスクリプショングループで]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)知ることができるサブスクリプションステータスの更新を可能にする`/users/track` エンドポイントの改善をリリースしました。ただし、[`/v2/subscription/status/set` エンド]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)ポイントを使用してすでにオプトイン・プロトコルを作成している場合は、引き続きそちらで作成することができます。
{% endalert %}

### 外部からのオプトイン方式

お客様のアプリまたはウェブサイト（アカウント登録、チェックアウトページ、アカウント設定、クレジットカード端末）をBrazeに送信します。

既にEメールやテキストでのマーケティング同意を得ている場合は、WhatsApp用の追加セクションを設けてください。ユーザーがオプトインした後、`external_id` 、[電話番号]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/)、更新された購読ステータスが必要となる。これを行うには、Brazeのインストール方法に応じて、[`/subscription/status/set` エンドポイントを]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)活用するか、[SDKを](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)使用します。

#### 外部オプトインリスト

以前にWhatsAppをご利用になったことがある場合、WhatsAppの要件に沿ったオプトインを含むユーザーリストを既に作成済みかもしれません。この場合、[以下の情報を]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#csv)CSVまたはAPIでBrazeにアップロードしてください。

#### カスタマーサポートWhatsAppチャンネルのアウトバウンドメッセージ

カスタマーサポートチャネルでは、解決した問題を自動メッセージでフォローアップし、マーケティングメッセージングのオプトインを希望するかどうかを尋ねます。ここでの機能は、選択したカスタマーサポートツールで利用可能な機能と、ユーザー情報を保存する場所に依存します。

1. WhatsApp Businessの電話番号から[メッセージリンクを](https://business.facebook.com/business/help/890732351439459?ref=search_new_0)送信します。
2. 顧客がオプトインを示すために「はい」と答える[クイック返信アクションを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages/#quick-replies)提供する。
3. カスタムキーワードトリガーを設定します。
4. どちらを選ぶにしても、おそらく次のようなパスが必要だろう：
	- [`/users/track` エンドポイントを]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)呼び出し、ユーザーを更新または作成する。 
	- [`/subscription/status/set` のエンドポイントを]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)利用するか、[SDK を](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)使用する。 

#### WhatsAppメッセージ 

WhatsApp番号にインバウンドメッセージを送信してもらいます。

これは、新しいチャンネルでユーザーに確認メッセージを受け取らせるかどうかによって、キャンバスまたはキャンペーンとして設定することができます。

1. インバウンドメッセージのアクションベースの配信トリガーでキャンペーンを作成する。
2. ウェブフックキャンペーンを作成する。Webhook の例については、[Subscription groups]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/#update-subscription-status) を参照してください。

{% alert tip %}
WhatsAppチャンネルに参加するためのURLやQRコードは、[WhatsAppマネージャーの](https://business.facebook.com/wa/manage/phone-numbers/)「**電話番号**」>「**メッセージリンク**」から作成できます。<br>![\]({% image_buster /assets/img/whatsapp/whatsapp115.png %}){: style="max-width:55%;"}
{% endalert %}

### ブレーズを利用したオプトイン・メソッド 

#### SMSメッセージ

CANVASでキャンペーンを設定し、以下のいずれかの方法でWhatsAppメッセージの受信をオプトインするかどうかを顧客に尋ねます：
\- 顧客セグメント：米国外の購読マーケティンググループ
\- カスタム・キーワード・トリガーの設定

[サブスクリプション]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status) グループを表示して、ユーザー プロファイルのサブスクリプション ステータスを更新する方法について説明します。

#### アプリ内またはブラウザ内のメッセージ

アプリ内メッセージまたはブラウザ内ポップアップを作成し、WhatsAppの利用をオプトインするよう促す。

BrazeSDKとのインターフェースには、[JavaScriptの「ブリッジ」を]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge)使用した[HTMLアプリ内](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)メッセージを使用します。WhatsApp購読グループIDを使用してください。 

#### 電話番号取得フォーム

アプリ内メッセージのドラッグ＆ドロップエディターで[電話番号取得フォーム]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/)テンプレートを使用すると、ユーザーの電話番号を収集し、WhatsApp購読グループを増やすことができます。

## Braze WhatsAppチャンネルのオプトアウト設定

### 一般的なオプトアウト・キーワード

キャンペーンやキャンバスを設定することで、特定の単語でメッセージを送ったユーザーが、今後のメッセージングをオプトアウトできるようにすることができます。キャンバスは、オプトアウトの成功を確認するフォローアップメッセージを含めることができるので、特に有益です。 

#### ステップ 1:トリガー "Inbound WhatsApp Message "でキャンバスを作成します。
 
![][6]{: style="max-width:85%;"}

キーワードトリガーを選択する際には、「Stop」や「No Message」といった単語を含める。この方法を選択する場合は、顧客がオプトアウトの言葉を知っていることを確認してください。例えば、最初のオプトインを受け取った後、「これらのメッセージをオプトアウトするには、いつでも "Stop "とメッセージしてください」というようなフォローアップの返答を含める。 

![][7]

#### ステップ 2:ユーザーのプロフィールを更新する

[サブスクリプション グループで]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)説明されている方法のいずれかを使用して、ユーザーのプロファイルを更新します。

### マーケティング・オプトアウトの選択

WhatsAppメッセージテンプレートには「マーケティングオプトアウト」オプションがあります。これを含むときはいつでも、テンプレートがサブスクリプショングループ変更のための後続ステップを持つキャンバスで使用されていることを確認してください。 

1. マーケティングオプトアウト」クイック返信でメッセージテンプレートを作成する。<br>![][11]<br><br>![][12]<br><br>
2. このメッセージテンプレートを使用してキャンバスを作成します。<br><br>
3. 前の例のステップに従いますが、トリガーテキストは "STOP PROMOTIONS "です。<br><br>
4. [サブスクリプション・グループで]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/#update-subscription-status)説明されている方法のいずれかを使用して、ユーザーのサブスクリプション・ステータスを更新します。



[1]: {% image_buster /assets/img/whatsapp/whatsapp111.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp112.png %}
[3]: {% image_buster /assets/img/whatsapp/whatsapp113.png %}
[4]: {% image_buster /assets/img/whatsapp/whatsapp114.png %}
[5]: {% image_buster /assets/img/whatsapp/whatsapp115.png %}
[6]: {% image_buster /assets/img/whatsapp/whatsapp116.png %}
[7]: {% image_buster /assets/img/whatsapp/whatsapp117.png %}
[8]: {% image_buster /assets/img/whatsapp/whatsapp118.png %}
[9]: {% image_buster /assets/img/whatsapp/whatsapp119.png %}
[10]: {% image_buster /assets/img/whatsapp/whatsapp120.png %}
[11]: {% image_buster /assets/img/whatsapp/whatsapp121.png %}
[12]: {% image_buster /assets/img/whatsapp/whatsapp122.png %} 
