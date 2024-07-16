---
nav_title: Olo
article_title:オロ
description:この記事では、あらゆる接点でホスピタリティを可能にするレストラン向けの主要なオープンSaaSプラットフォームであるOloとBrazeの提携について概説しています。
alias: /partners/olo/
page_type: partner
search_tag:Partner
---

# オロ

> [Olo][1] は、あらゆる接点でホスピタリティを可能にするレストラン向けの主要なオープンSaaSプラットフォームです。

OloとBrazeを統合することで、次のことができます:

- Brazeのユーザープロファイルを更新して、Oloのユーザープロファイルと一貫性を保ちます
- Oloイベントに基づいてBrazeから次の最適なメッセージを送信する

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| オロアカウント | このパートナーシップを利用するには、WebhookにアクセスできるOloアカウントが必要です。Oloダッシュボード内の[セルフサービスWebhookツール](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks)を使用して、Webhookサブスクリプションを設定します。 |
| Braze データ変換 | Oloからデータを受信するには[データ変換URL]({{site.baseurl}}/data_transformation/)が必要です。 |
{: .reset-td-br-1 .reset-td-br-2}

Webhookは、Oloがユーザーとその行動に関するイベント駆動型の情報をBrazeに送信する方法です。これには、注文が確定したとき、ゲストがオプトインしたとき、注文がピックアップされたときなどのイベントが含まれます。Olo Webhookは、アクションが実行されてから通常数秒以内にイベントをBrazeに配信します。

## 免責事項

Oloでは、承認されたブランドごとに環境ごとに1つのWebhookに制限されており、すべて同じ**宛先URL**に送信されます。異なるブランドは異なるURLを持つことができますが、同じブランドのイベントはURLを共有する必要があります。Brazeでは、Oloで使用するための変換を1つだけ行うことができます。

この単一の変換内で複数のOloイベントを処理するには、各Webhookの`X-Olo-Event-Type`ヘッダーを探します。このヘッダーを使用すると、さまざまなOloイベントを条件付きで処理できます。

## 統合

### ステップ1:Brazeデータ変換を設定して、Oloのテストイベント{#step-1}を受け入れる

{% multi_lang_include create_transformation.md location="default" %}

### ステップ2:Oloのウェブフックを設定する

Oloダッシュボード内の[セルフサービスWebhooksツール][2]を使用して、データ変換に送信するWebhooksを設定します。

1. どのイベントをBrazeに送信するかを選択してください
2. **宛先URL**を構成します。これは[ステップ1](#step-1)で作成されたデータ変換URLです。

{% alert note %}
`OAuth` と `X-Olo-Signature` ヘッダー共有シークレットは変換に必要ありません。
{% endalert %}

{:start="3"}
3\.Webhook が正しく構成されていることを確認するには、[テストイベント][3] をデータ変換に送信します。Oloダッシュボードのユーザーのみが[開発者ツールの権限][4]を持っている場合、テストイベントを送信できます。

Oloは、Olo webhook構成プロセスを完了する前に、Test Event webhookからの成功応答を必要とします。

### ステップ3:選択したOloイベントを受け入れる変換コードを書いてください

このステップでは、ソースプラットフォームから送信されるWebhookペイロードをJavaScriptオブジェクトの戻り値に変換します。

1. サンプルイベントペイロードを含むOloイベントをサポートするために、データ変換URLにリクエストを送信してください。リクエストの書式設定については[リクエスト本文の形式](#request-body-format)を参照してください。
2. データ変換を更新し、**Webhookの詳細**でサンプルイベントペイロードを確認できるようにしてください。
3. 選択したOloイベントをサポートするようにデータ変換コードを更新してください。
4. **検証**をクリックして、コードの出力のプレビューを返し、それが許容される`/users/track`リクエストであるかどうかを確認します。
5. データ変換を保存して有効化します。

#### リクエストボディ形式

この戻り値は、Brazeの `/users/track` リクエストの本文フォーマットに準拠しなければなりません。

- 変換コードは JavaScript プログラミング言語で受け入れられます。if/else ロジックなど、標準的な JavaScript 制御フローがすべてサポートされています。
- 変換コードは、ペイロード変数を介してWebhookリクエストボディにアクセスします。この変数は、リクエスト本文の JSON を解析して読み込まれたオブジェクトです。
- `/users/track` エンドポイントでサポートされるすべてのフィーチャーがサポートされています。例を示します。
    - ユーザー属性オブジェクト、イベントオブジェクト、購入オブジェクト
    - 階層化属性と階層化カスタムイベントプロパティ
    - サブスクリプショングループの更新
    - 識別子としてのメールアドレス

## Olo Webhookの例データ変換

このセクションには、出発点として使用できる例のテンプレートが含まれています。最初から始めても、必要に応じて特定のコンポーネントを削除しても構いません。

各テンプレートでは、コードは変数`brazecall`を定義して、`/users/track`リクエストを構築します。

`/users/track `リクエストが`brazecall`に割り当てられた後、出力を作成するために`brazecall`を明示的に返します。

### 単一イベント変換

単一のOloイベントのみをサポートする場合、`X-Olo-Event-Type`ヘッダーを使用して`/users/track`リクエストペイロードを条件付きで作成する必要はありません。例えば、Olo Order Placed webhookがBrazeに送信されたときに、購入イベントやカスタムイベントをユーザープロファイルに記録することです。

### 各製品を購入として記録する

```javascript
// iterate through the items included within the order

const purchases = payload.items.map((item) => {
 return {
   external_id: payload.customer.customerId.toString(),
   product_id: item.productId.toString(),
   currency: 'USD',
   price: item.sellingPrice,
   time: new Date().toISOString(),
   quantity: item.quantity,
   properties: {
     customValues: item.customValues
   }
 };
});

// log a purchase per item in the order

let brazecall = {
 "purchases": purchases
};

return brazecall;
```

### カスタムイベントの記録

```javascript
// log an event “Order Placed” to the profile that includes all items in the order as event properties.

let brazecall = { 
"events": [
   {
     "external_id": payload.customer.customerId.toString(),
     "_update_existing_only": false,
     "name": "Order Placed",
     "time": new Date().toISOString(),
     "properties": {
       "Delivery Method": payload.deliveryMethod,
       "Items": payload.items,
       "Total": payload.totals.total,
       "Location": payload.location.name
     }
   }
 ]
};

return brazecall;
```

## マルチイベント変換

Oloは各Webhookの`X-Olo-Event-Type`ヘッダー内にイベントタイプを送信します。単一の変換内で複数のOlo Webhookイベントをサポートするには、このヘッダータイプの値に基づいてWebhookペイロードを変換するための条件ロジックを使用します。  

以下の変換例では、私たちのJavaScriptは`UserSignedUp`と`OrderPlaced`のイベントのために特定のペイロードを作成します。さらに、`else`条件は、`UserSignedUp`および`OrderPlaced`のX-Olo-Event-TypeヘッダーなしでBrazeに送信されたOloイベントのペイロードを処理します。

```javascript
// captures the value within the X-Olo-Event-Type header for use in the conditional logic

let event_type = headers["X-Olo-Event-Type"];

// defines a variable 'brazecall' that will hold the request payload for the /users/track request

let brazecall;

// if the X-Olo-Event-Type header is 'UserSignedUp', define a variable for the different subscription statuses that could be included within the Olo event payload

if (event_type == "UserSignedUp") {
	let emailSubscribe;
	let emailSubscriptionGroup;
	let smsSubscriptionGroup;


// determine if the user has opted into marketing emails


	if (payload.allowEmail) {
		emailSubscribe = "opted_in";
		emailSubscriptionGroup = "subscribed";
	} else {
		emailSubscribe = "unsubscribed";
		emailSubscriptionGroup = "unsubscribed";
	}


	// determine if the user has opted into SMS


	if (payload.allowMarketingSms) {
		smsSubscriptionGroup = "subscribed";
	} else {
		smsSubscriptionGroup = "unsubscribed";
	}

	// build the /users/track request and pass in the appropriate subscription statuses


	brazecall = {
		"attributes": [{
			"external_id": payload.id.toString(),
			"_update_existing_only": false,
			"email": payload.emailAddress,
			"first_name": payload.firstName,
			"last_name": payload.lastName,
			"email_subscribe": emailSubscribe,
			"phone": payload.contactNumber,
			"subscription_groups": [{
					"subscription_group_id": "57e5307f-9084-490d-9d6d-8244dc919a48",
					"subscription_state": emailSubscriptionGroup
				},
				{
					"subscription_group_id": "6440ba26-86ea-47db-a935-6647941dc78b",
					"subscription_state": smsSubscriptionGroup
				}
			]
		}]
	}; // if the X-Olo-Event-Type header is 'OrderPlaced', build the /users/track request to log an event to the user profile
} else if (event_type == "OrderPlaced") {
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": false,
			"name": "Order Placed",
			"time": new Date().toISOString(),
			"properties": {
				"Delivery Method": payload.deliveryMethod,
				"Items": payload.items,
				"Total": payload.totals.total,
				"Location": payload.location.name
			}
		}]
	};
} else { // if the X-Olo-Event-Type header is anything else, build the /users/track request to log an event to the user profile
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": true,
			"name": "Another Event",
			"time": new Date().toISOString()
		}]

	};
}

// return `brazecall` to create an output.

return brazecall;
```

### ステップ 4:OloのWebhookを公開する

Brazeでデータ変換を有効にした後、Oloダッシュボード内の[セルフサービスウェブフックツール][2]を使用してウェブフックを公開します。Webhookが公開されると、データ変換はOlo webhookイベントメッセージの受信を開始します。

## 知っておくべきこと

### 再試行

Oloは、HTTP応答ステータスコードが`429 - Too Many Requests`または`5xx`範囲内（例えば、ゲートウェイタイムアウトやサーバーエラーのため）である場合、リクエストを削除する前に24時間以内に最大50回までWebhookコールを再試行します。

### 少なくとも一度の配達

Webhook 呼び出しが HTTP 応答ステータス コード `429 - Too Many Requests` または `5xx` 範囲 (たとえば、ゲートウェイ タイムアウトやサーバー エラーが原因) になると、Olo は 24 時間以内に最大 50 回メッセージの再試行を行い、諦めます。

ウェブフックは、サブスクライバーによって複数回受信されることがあります。重複を無視するかどうかは、`X-Olo-Message-Id`ヘッダーを確認することで加入者に委ねられています。


[1]: https://www.olo.com/
[2]: https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks
[3]: https://developer.olo.com/docs/load/webhooks#operation/test
[4]: https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions