---
nav_title: "サブスクリプショングループ"
article_title: WhatsApp サブスクリプショングループ
page_order: 1
description: "この記事では、WhatsAppのサブスクリプショングループの概要、提供されるサブスクリプションの状態、サブスクリプショングループの設定方法について説明する。"
page_type: reference
channel:
  - WhatsApp
 
---

# サブスクリプショングループ

> WhatsAppのサブスクリプショングループは、**テクノロジーパートナーポータルを通して**WhatsAppとアプリを統合することで作成される。

## WhatsAppの契約状態

WhatsApp ユーザーには`subscribed` と`unsubscribed` の2つの契約状態がある。

| 状態 | 定義 |
| --- | --- |
| サブスクリプション登録済み | ユーザーが特定の企業からのWhatsAppメッセージを受信したいと明示的に確認した。WhatsAppのガイドラインに従って、BrazeのサブスクリプションAPIを通じてサブスクリプションの状態を更新するか、オプトイン戦略を導入することで、ユーザーをサブスクライブさせることができる。 |
| 配信停止済み | ユーザーがオプトインに明示的に同意していないか、オプトインのステータスが明示的に削除されている。<br><br> WhatsApp購読グループから退会したユーザーは、その購読グループに属する電話番号からのWhatsAppメッセージを受信できなくなる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

### ユーザーのWhatsApp購読グループを設定する

- **Rest API:**ユーザープロファイルは、Braze REST APIを使用して\[`/subscription/status/set` endpoint][4] ]によってプログラムで設定できる。
- **ウェブSDK：**[Android](https://braze-inc.github.io/braze-android-sdk/javadocs/com/braze/BrazeUser.html#addToSubscriptionGroup-java.lang.String-)、[iOS](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_user.html#a74092a50fcda364bb159013d0222e287)、\[Web][11]]の`addToSubscriptionGroup` メソッドを使って、Eメール、SMS、WhatsAppの購読グループにユーザーを追加できる。
- **ユーザー輸入**：ユーザは、**Import Users（ユーザのインポート**）により、EメールまたはSMS購読グループに追加することができる。サブスクリプション・グループのステータスを更新する場合、CSVに次の2つのカラムが必要である：`subscription_group_id` と`subscription_state` 。詳しくは[ユーザーインポートを]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#updating-subscription-group-status)参照のこと。

### ユーザーのWhatsApp購読グループを確認する

- **ユーザープロフィール:**個々のユーザープロフィールは、Brazeダッシュボードの**Audience**>**Search Usersから**アクセスできる。ここでは、電子メールアドレス、電話番号、外部ユーザーIDでユーザープロファイルを検索できる。ユーザープロフィールの\[**Engagement]**タブで、そのユーザーのWhatsApp購読グループとステータスを確認できる。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、**ユーザー**>**ユーザー検索で**このページを見つけることができる。
{% endalert %}

- **Rest API:**個々のユーザープロファイル購読グループは、BrazeのREST APIを使用して、\[List user's subscription groups endpoint][9] ]または\[List user's subscription group status endpoint][8] ]で確認できる。 

## WhatsAppオプトイン・プロセス

現在、ユーザーは[SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal)、ウェブサイト、WhatsAppスレッド、電話、対面など様々な方法でWhatsAppメッセージングに登録し、[オプトインする]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/opt-ins_and_opt-outs/)ことができる。なお、オプトインは必須である。

オプトインキーワードは現在WhatsAppチャンネルではサポートされていないため、ユーザーリストの管理はユーザー次第となる。WhatsAppはオプトインとレート制限に遡及的なアプローチを採用しており、ユーザーが報告やブロックを始めるとレート制限が引き下げられる。 

## WhatsAppキャンバスの購読ステータスを更新する {#update-subscription-status}

使用するオプトインおよびオプトアウトの方法にかかわらず、以下の更新方法のいずれかを使用してユーザープロファイルの購読ステータスを更新することができる：

- 以下の例のように、REST API経由で購読ステータスを更新する[Braze-to-Braze webhookを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/#things-to-know)作成する：

![][1]{: style="max-width:90%;"}

レースコンディションを避けるために、Webhook後のフォローアップメッセージングは、最初のキャンバスの結果（例えば、ユーザーがキャンバスのバリエーションを入力し、WhatsAppの購読グループに入っているなど）によってトリガーされる2番目のキャンバスに含まれるべきである。

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

![][2]{: style="max-width:90%;"}

{% alert note %}
ユーザーの購読ステータスの更新には最大60秒かかる場合がある。
{% endalert %}

[1]: {% image_buster /assets/img/whatsapp/whatsapp118.png %}
[2]: {% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}
[4]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups/
[11]: https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup
