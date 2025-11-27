---
nav_title: "サブスクリプショングループ"
article_title: WhatsApp サブスクリプショングループ
page_order: 1
description: "この記事では、WhatsAppのサブスクリプショングループの概要、提供されるサブスクリプションの状態、サブスクリプショングループの設定方法について説明する。"
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp
 
---

# サブスクリプショングループ

> WhatsApp の購読グループは、**テクノロジーパートナーポータル**経由で WhatsApp とアプリを連携すると作成されます。

## WhatsApp の購読状態

WhatsApp のユーザーには、`subscribed` と `unsubscribed` の 2 つの購読状態があります。

| 状態 | 定義 |
| --- | --- |
| サブスクリプション登録済み | ユーザーが特定の企業からのWhatsAppメッセージを受信したいと明示的に確認した。WhatsAppのガイドラインに従って、BrazeのサブスクリプションAPIを通じてサブスクリプションの状態を更新するか、オプトイン戦略を導入することで、ユーザーをサブスクライブさせることができる。 |
| 配信停止済み | ユーザーがオプトインに明示的に同意していないか、ユーザーのオプトインステータスが明示的に削除されています。<br><br> WhatsApp の購読グループのユーザーが購読解除すると、その購読グループに属する送信電話番号から WhatsApp のメッセージを受信しなくなります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

### ユーザーのWhatsApp購読グループを設定する

- **Rest API:**Braze REST API を使用することで、ユーザープロファイルは [`/subscription/status/set` エンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)によってプログラムで設定できます。
- **Web SDK:**[Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html)、[iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:))、[Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup) の場合、`addToSubscriptionGroup` メソッドを使って、メール、SMS、WhatsAppの購読グループにユーザーを追加できます。
- **ユーザー輸入**：ユーザは、**Import Users（ユーザのインポート**）により、EメールまたはSMS購読グループに追加することができる。購読グループのステータスを更新する場合、CSV には `subscription_group_id` と `subscription_state` の 2 列が必要です。詳細については、[「ユーザーインポート」]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status)を参照してください。

### ユーザーのWhatsApp購読グループを確認する

- **ユーザープロフィール:**個々のユーザープロファイルには、Braze ダッシュボードの [**オーディエンス**] > [**ユーザーを検索**] からアクセスできます。ここでは、電子メールアドレス、電話番号、外部ユーザーIDでユーザープロファイルを検索できる。ユーザープロフィールの[**Engagement]**タブで、そのユーザーのWhatsApp購読グループとステータスを確認できる。

- **Rest API:**Braze REST API を使用することで、[ユーザーの購読グループをリストするエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/)または[ユーザーの購読グループのステータスをリストするエンドポイント]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/)で、個々のユーザープロファイルの購読グループを確認できます。 

## WhatsAppのオプトインとオプトアウトのプロセス

現在、ユーザーは[SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)、Web サイト、WhatsApp スレッド、電話、対面などさまざまな方法で WhatsApp メッセージングに登録し、[オプトインおよびオプトアウト]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)することができます。オプトインは必須である点に注意してください。

オプトインキーワードは現在WhatsAppチャンネルではサポートされていないため、ユーザーリストの管理はユーザー次第となる。WhatsAppはオプトインとレート制限に遡及的なアプローチを採用しており、ユーザーが報告やブロックを始めるとレート制限が引き下げられる。 

## ユーザーの WhatsApp キャンバスの購読ステータスの更新{#update-subscription-status}

使用するオプトインおよびオプトアウトの方法にかかわらず、以下の更新方法のいずれかを使用してユーザープロファイルの購読ステータスを更新できます。

- 次の例のように、REST API を介して購読ステータスを更新する [Braze-to-Braze Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know) を作成します。

![POST メソッドを使用したメッセージが表示されている Webhook 作成画面。]({% image_buster /assets/img/whatsapp/whatsapp118.png %})({: style="max-width:90%;"})

競合を回避するため、Webhook の後のフォローアップメッセージングは、最初のキャンバスの結果 (ユーザーがキャンバスのバリエーションに入って、現在 WhatsApp の購読グループに属している、など) によってトリガーされる 2 番目のキャンバスに含める必要があります。

- アドバンスドJSONエディターを使用して、以下のテンプレートでユーザープロファイルを更新する： 

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

![「高度なJSONエディター」ステップが選択されているユーザー更新ステップ。]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %})({: style="max-width:90%;"})

{% alert note %}
ユーザーの購読ステータスの更新には最大 60 秒かかることがあります。
{% endalert %}

