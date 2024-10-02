---
nav_title: オロ
article_title: オロ
description: "この記事では、Brazeと、あらゆるタッチポイントでホスピタリティを実現するレストラン向けオープンSaaSプラットフォームのリーディングカンパニーであるOlo社との提携について概説する。"
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# オロ

> [Oloは][1]、あらゆるタッチポイントでホスピタリティを実現する、レストラン向けの主要なオープンSaaSプラットフォームである。

OloとBrazeを統合することで、それが可能になる：

- Brazeのユーザープロファイルを更新し、Oloのユーザープロファイルとの一貫性を保つ。
- Oloのイベントに基づいて、Brazeから適切な次善のメッセージを送る

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| オロ口座 | このパートナーシップを利用するには、ウェブフックにアクセスできるOloアカウントが必要である。Oloダッシュボード内の[セルフサービスWebhooksツールで](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks)Webhookサブスクリプションを設定する。 |
| ブレイズデータ変換 | Oloからデータを受け取るには、[データ変換URLが]({{site.baseurl}}/data_transformation/)必要である。 |
{: .reset-td-br-1 .reset-td-br-2}

Webhookとは、OloがBrazeにユーザーとそのアクションに関するイベントドリブンな情報を送信する方法であり、Order Placed（注文の発注）、Guest Opt In（ゲストのオプトイン）、Order Picked Up（注文の受け取り）などのイベントを含む。Olo Webhookは、一般的にアクションが実行されてから数秒以内にBrazeにイベントを配信する。

## 免責事項

Oloでは、承認されたブランドごとに1環境につき1つのウェブフックに制限され、すべて同じ**宛先**URLに送信される。異なるブランドは異なるURLを持つことができるが、同じブランドのイベントはURLを共有しなければならない。Brazeでは、これはOloで使用するための変身を1つしか作れないことを意味する。

この1つの変換で複数のOloイベントを処理するには、各ウェブフックの`X-Olo-Event-Type` ヘッダーを探す。このヘッダーによって、異なるOloイベントを条件付きで処理することができる。

## 統合

### ステップ1:Oloのテストイベントを受け入れるようにBrazeデータ変換をセットアップする。 {#step-1}

{% multi_lang_include create_transformation.md location="default" %}

### ステップ2:Oloウェブフックを設定する

Oloダッシュボード内の[セルフサービスウェブフックツールを][2]使用して、データ変換に送信するウェブフックを設定する。

1. Brazeに送信するイベントを選択する
2. **宛先URLを**設定する。これは[ステップ](#step-1)1で作成したデータ変換URLになる。

{% alert note %}
`OAuth` と`X-Olo-Signature` ヘッダー共有秘密は変換に必要ない。
{% endalert %}

{:start="3"}
3\.[Test Eventを][3]Data Transformationに送信して、Webhookが正しく設定されていることを確認する。テストイベントを送信できるのは、[Developer Tools 権限を][4]持つ Olo Dashboard ユーザのみである。

Olo は、Olo ウェブフック設定プロセスを完了する前に、Test Event ウェブフックからの成功応答を必要とする。

### ステップ3:選んだOloイベントを受け入れる変換コードを書く

このステップでは、ソース・プラットフォームから送信されるウェブフック・ペイロードを、JavaScriptオブジェクトの戻り値に変換する。

1. データ変換 URL に、サポートする予定の Olo イベントのサンプルイベントペイロードを添えてリクエストを送信する。リクエストの書式については、[リクエストボディの書式を](#request-body-format)参照のこと。
2. Data Transformationをリフレッシュし、**Webhook Detailsに**サンプルのイベントペイロードが表示されていることを確認する。
3. データ変換コードを更新して、選択したOloイベントをサポートする。
4. **Validateを**クリックすると、コードの出力のプレビューが返され、それが受け入れ可能な`/users/track` リクエストかどうかがチェックされる。
5. データ変換を保存して有効にする。

#### リクエスト・ボディのフォーマット

この戻り値は、Brazeの `/users/track` リクエストの本文フォーマットに準拠しなければなりません。

- 変換コードは JavaScript プログラミング言語で受け入れられます。if/else ロジックなど、標準的な JavaScript 制御フローがすべてサポートされています。
- 変換コードは、ペイロード変数を通じてウェブフック・リクエスト・ボディにアクセスする。この変数は、リクエスト本文の JSON を解析して読み込まれたオブジェクトです。
- `/users/track` エンドポイントでサポートされるすべてのフィーチャーがサポートされています。例を示します。
    - ユーザー属性オブジェクト、イベントオブジェクト、購入オブジェクト
    - 階層化属性と階層化カスタムイベントプロパティ
    - サブスクリプショングループの更新
    - 識別子としてのメールアドレス

## Oloウェブフックのデータ変換の例

このセクションには、出発点として使用できるテンプレートの例が含まれている。ゼロから始めるのも、特定のコンポーネントを削除するのも自由だ。

各テンプレートでは、`/users/track` リクエストを構築するために、`brazecall` という変数を定義している。

`/users/track `リクエストが`brazecall` に割り当てられた後、出力を作成するために明示的に`brazecall` を返す。

### 単一イベント変換

もしあなたが一つのOloイベントだけをサポートしようとしているなら、`/users/track` リクエストペイロードを条件付きで生成するために`X-Olo-Event-Type` ヘッダーを使う必要はない。例えば、Olo Order PlacedウェブフックがBrazeに送信されたときに、購入イベントやカスタムイベントをユーザープロファイルに記録する。

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

### カスタムイベントをログに記録する

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

Olo は、各 webhook の`X-Olo-Event-Type` ヘッダー内にイベントタイプを送信する。単一の変換内で複数の Olo webhook イベントをサポートするには、条件付きロジックを使用して、このヘッダー型の値に基づいて webhook ペイロードを変換する。  

以下の変換例では、JavaScriptは`UserSignedUp` と`OrderPlaced` のイベントに対して特定のペイロードを作成している。さらに、`else` の条件は、`UserSignedUp` と`OrderPlaced` のX-Olo-Event-TypeヘッダーのないBrazeに送られたOloイベントのペイロードを処理する。

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

### ステップ 4:Oloウェブフックを公開する

BrazeでData Transformationを有効化したら、Oloダッシュボード内の[セルフサービスwebhooksツールを使って][2]webhookを公開する。ウェブフックがパブリッシュされると、データ変換はOloウェブフックのイベントメッセージを受信し始める。

## 知っておくべきこと

### リトライ

Oloは、HTTPレスポンスステータスコードが`429 - Too Many Requests` 、または`5xx` （ゲートウェイのタイムアウトやサーバーエラーなど）の範囲になったWebhookコールを、リクエストをドロップする前に、24時間以内に50回まで再試行する。

### 少なくとも1回の配達

ウェブフック呼び出しの結果、HTTPレスポンスステータスコードが`429 - Too Many Requests` 、または`5xx` （ゲートウェイのタイムアウトやサーバーエラーなど）の範囲になった場合、Oloは24時間以内に50回までメッセージを再試行してからあきらめる。

したがって、Webhookはサブスクライバーによって複数回受信される可能性がある。`X-Olo-Message-Id` ヘッダーをチェックすることで、重複を無視するのは購読者次第である。


[1]: https://www.olo.com/
[2]: https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks
[3]: https://developer.olo.com/docs/load/webhooks#operation/test
[4]: https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions