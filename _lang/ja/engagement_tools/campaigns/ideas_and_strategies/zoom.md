---
nav_title: Zoom の登録を自動化する
article_title: Zoom の登録を自動化する
page_order: 1
page_type: tutorial
description: "この記事では、メール、プッシュ、アプリ内メッセージのキャンペーンで Zoom の参加者登録を自動化する方法について説明します。"
channel: 
  - email
  - push
  - in-app messages

---

# Zoom の登録を自動化する

> Braze の顧客がウェビナーを主催することは、ここ数年で一般的になりました。Zoom ウェビナーを開催する場合、ユーザーは Zoom のランディングページに自分の情報を入力して登録する必要があります。 

推奨されるユーザーフローの概要は次のとおりです。
1. Zoom でウェビナーをスケジュールし、`webinarId` を生成します。
2. Braze を使用して、メール、プッシュ、アプリ内メッセージのチャネルで Zoom ウェビナーを宣伝します。 
3. これらのコミュニケーションには、ユーザーを自動的にウェビナーに追加する「CTA (call-to-action)」ボタンを含めます。

これは、[Zoom API](https://marketplace.zoom.us/docs/api-reference/zoom-api/methods/#operation/meetingRegistrantCreate) を使用して、メール、プッシュ、またはアプリ内メッセージ内のボタンクリックを通じて、ユーザーを自動的にウェビナーに追加することで実現できます。API リクエストのウェビナー ID を置き換えて、以下のエンドポイントを使用します。 

POST: `/meetings/{webinarId}/registrants`

詳細については、Zoom の「[ウェビナー登録者エンドポイントの追加](https://developers.zoom.us/docs/api/rest/reference/zoom-api/methods/#operation/webinarRegistrantCreate)」を参照してください。<br><br>

{% tabs %}
{% tab Email %}

メッセージ本文内に CTA ボタンを含むメールキャンペーンを作成します。ユーザーがボタンをクリックすると、ウェビナーのランディングページにリダイレクトされます (リダイレクトリンクには適切なパラメーターが含まれています)。 

URL のパラメーターを使用してユーザーデータを渡し、ページの読み込み時に実行される API 呼び出しを作成して、ユーザーをウェビナーに追加します。

![メールメッセージ (名、姓、メールアドレス、および市区町村を含めるために使用される Liquid テンプレート付き)。]({% image_buster /assets/img/zoom/zoom1.png %})()

これで、ユーザーが Braze プロファイルにすでに存在する詳細でウェビナーに登録されます。

{% endtab %}
{% tab Push %}

1. プッシュキャンペーンを作成します。<br><br>

	ウェビナーのランディングページにリンクアウトするボタンのクリック時動作を設定します。<br>

	![ボタンをクリックしたときのウェビナーへのリンク]({% image_buster /assets/img/zoom/zoom2.png %})()<br><br>

	プッシュからボタンクリックで登録するユーザーのためのランディングページの簡単な例です。登録した内容をユーザーに知らせ、登録を確認します。<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>


2. アプリ内メッセージやボタンクリックによってトリガーされる Webhook キャンペーンを作成します。<br><br>
 	Braze プロファイルの既存のユーザーデータを使用して、ユーザーをウェビナーに登録します。<br>

	![特定のキャンペーンのボタンをクリックしたユーザーに送信されるアクションベースのキャンペーン。]({% image_buster /assets/img/zoom/zoom6.png %})()<br><br>

	Zoom エンドポイントへの Webhook 呼び出しの例。<br>
	{% raw %}
	```json
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}

3. これで、ユーザーが Braze プロファイルにすでに存在する詳細でウェビナーに登録されます。

{% endtab %}
{% tab In-app message %}

1. アプリ内メッセージキャンペーンを作成する<br><br>

	ウェビナー・ランディング・ページにリンクするボタンのクリック時の動作を設定する。<br>

	![ボタンをクリックしたときのウェビナーへのリンク]({% image_buster /assets/img/zoom/zoom3.png %})()<br><br>

	アプリ内メッセージからボタンクリックで登録するユーザーのためのランディングページの簡単な例です。登録した内容をユーザーに知らせ、登録を確認します。<br>

	![]({% image_buster /assets/img/zoom/zoom4.png %})<br><br>

2. アプリ内メッセージやボタンクリックによってトリガーされる Webhook キャンペーンを作成します。<br><br>
	Braze プロファイルの既存のユーザーデータを使用して、ユーザーをウェビナーに登録します。<br>

	![指定したキャンペーンのボタンをクリックしたユーザーに送信されるアクションベースのキャンペーン。]({% image_buster /assets/img/zoom/zoom5.png %})()<br><br>

	Zoom エンドポイントへの Webhook 呼び出しの例。<br>
	{% raw %}
	```json
	POST https://api.zoom.com/meetings/{webinarId}/registrants

	{
		"email": "{{${email_addresses}}}",
		"first_name": "{{${first_name}}}",
		"last_name": "{{${last_name}}}",
		"city": "{{${city}}}",
		"country": "{{${country}}}",
		"phone": "{{${phone_number}}}"
	}
	```
	{% endraw %}
3. これで、ユーザーが Braze プロファイルにすでに存在する詳細でウェビナーに登録されます。

{% endtab %}
{% endtabs %}
