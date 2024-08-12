---
nav_title: "サブスクリプショングループ"
article_title: WhatsApp サブスクリプショングループ
page_order: 1
description: "この記事では、WhatsAppサブスクリプショングループ、提供されるサブスクリプション状態、およびサブスクリプショングループの設定方法について概説します。"
page_type: reference
channel:
  - WhatsApp
 
---

# サブスクリプショングループ

> WhatsAppサブスクリプショングループは、**テクノロジーパートナーポータルを通じてWhatsAppをアプリに統合したときに作成されます**。

## WhatsApp サブスクリプションステータス

WhatsAppユーザーには、`subscribed`とという2つのサブスクリプション状態があります`unsubscribed`。WhatsAppには、ワークスペースごとに1つのサブスクリプショングループがあります。

| 状態| 定義|
| --- | --- |
| 購読中 | ユーザーは、特定の会社からWhatsAppメッセージを受信したいことを明示的に確認しました。ユーザーは、BrazeサブスクリプションAPIを使用してサブスクリプション状態を更新するか、WhatsAppのガイドラインに従ってオプトイン戦略を導入することでサブスクライブできます。|
| 登録解除 | ユーザーがオプトインに明示的に同意していないか、オプトインステータスが明示的に削除されています。<br><br> WhatsAppサブスクリプショングループからサブスクライブ解除されたユーザーは、サブスクリプショングループに属する送信電話番号からのWhatsAppメッセージを受信しなくなります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### ユーザーの WhatsApp サブスクリプショングループの設定

- **Rest API:**ユーザープロファイルは [\`でプログラム的に設定できます/subscription/status/set` endpoint][4] using the Braze REST API.
- **ウェブ SDK:**[Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-)、[iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)、または [ウェブ] [11] `addToSubscriptionGroup` の方法を使用して、電子メール、SMS、または WhatsApp サブスクリプショングループにユーザーを追加できます。
- **ユーザー輸入**：ユーザーは、「**ユーザーのインポート**」を使用して電子メールまたは SMS 購読グループに追加できます。サブスクリプショングループのステータスを更新する場合、CSV `subscription_group_id` にはとの 2 つの列が必要です`subscription_state`。詳細については、「[ユーザーインポート]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status)」を参照してください。

### ユーザーの WhatsApp サブスクリプショングループの確認

- **ユーザープロフィール:**個々のユーザープロファイルには、Braze ダッシュボードの [**オーディエンス**] > [**ユーザー検索**] からアクセスできます。ここでは、メールアドレス、電話番号、または外部ユーザーIDでユーザープロファイルを検索できます。ユーザープロファイル内の [**エンゲージメント**] タブでは、ユーザーのWhatsAppサブスクリプショングループとそのステータスを確認できます。

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、このページを [**ユーザー**] > [**ユーザー検索**] にあります。
{% endalert %}

- **Rest API:**個々のユーザープロファイルのサブスクリプショングループは、BrazeのREST APIを使用して [ユーザーのサブスクリプショングループを一覧表示エンドポイント] [9] または [ユーザーのサブスクリプショングループステータスエンドポイントを一覧表示] [8] で表示できます。 

## WhatsApp オプトインプロセス

現在、ユーザーは、Webサイト、WhatsAppスレッド、電話、または対面で、[[SMSを含むさまざまな方法でWhatsAppメッセージングを購読およびオプトインできます](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)。オプトインが必要であることに注意してください。

オプトインキーワードは現在WhatsAppチャンネルではサポートされていないため、ユーザーリストを管理するのはあなた次第です。WhatsAppはオプトインとレート制限に対して遡及的アプローチを採用しており、ユーザーがあなたを報告したりブロックしたりすると、レート制限が引き下げられます。 

## WhatsApp Canvasへのユーザーのサブスクリプションステータスの更新 {#update-subscription-status}

使用するオプトインおよびオプトアウトの方法に関係なく、次のいずれかの更新方法でユーザープロファイルのサブスクリプションステータスを更新できます。

- 次の例のように、REST API 経由でサブスクリプションステータスを更新する [Braze To-Braze ウェブフックを作成します]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know)。

![][1]{: style="max-width:90%;"}

競合状態を避けるため、Webhook後のフォローアップメッセージは、最初のCanvasからの結果（ユーザーがCanvasのバリエーションを入力してWhatsAppサブスクリプショングループに入っているなど）によってトリガーされる2つ目のCanvasに含まれる必要があります。

- 高度な JSON エディターを使用して、次のテンプレートを使用してユーザープロファイルを更新します。 

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

![][2]{: style="max-width:90%;"}

{% alert note %}
ユーザーのサブスクリプションステータスの更新には、最大60秒かかる場合があります。
{% endalert %}

[1]: {% image_buster /assets/img/whatsapp/whatsapp118.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}
[4]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
