---
nav_title: Typeform
article_title:タイプフォーム
description:"この記事では、データやフィードバックなどを収集するための使いやすいツールであるBrazeとTypeformのパートナーシップについて概説する。"
alias: /partners/typeform/
page_type: partner
search_tag:Partner
---

# タイプフォーム

> [Typeformは](https://www.typeform.com/)、データやフィードバックなどを収集するための使いやすいツールだ。

BrazeとTypeformを統合することで、以下のことが可能になる：

- BrazeのユーザープロファイルをTypeformのレスポンスから収集したデータで更新する。
- ユーザーとtypeformのエンゲージメントに基づいてBrazeでメッセージをトリガーする
- ユーザーのTypeformのレスポンシブに基づいて、Brazeのメッセージをパーソナライズする。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Typeformアカウント | このパートナーシップを利用するには、WebhookにアクセスできるTypeformアカウントが必要である。 |
| Braze データ変換 | Typeformからデータを受け取るには、[データ変換URLが]({{site.baseurl}}/data_transformation/)必要である。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Brazeデータ変換がTypeformのWebhookを受け入れるように設定する。 {#step-1}

{% multi_lang_include create_transformation.md location="typeform" %}

### ステップ2:TypeformのWebhookを設定する

[TypeformのWebhookドキュメントの](https://www.typeform.com/help/a/webhooks-360029573471/)ステップに従ってWebhookを設定する。

ステップ4では、Data Transformation WebhookのURLを送信**先URLとして**追加する。

![\]({% image_buster /assets/img/typeform/typeform_add_webhook.png %}){: style="max-width:50%" }

**View deliveriesを**クリックし、**Send test requestを**クリックして、データ変換にテストイベントを送信する。

![\]({% image_buster /assets/img/typeform/typeform_test_request.png %})

### ステップ3:選択したTypeformのイベントを受け入れる変換コードを書く

このステップでは、Typeformから送信されるWebhookペイロードをJavaScriptオブジェクトの戻り値に変換する。

1. Data Transformationを更新し、**Webhook Detailsに**Typeformのテストペイロードが表示されていることを確認する。
2. 選択したTypeformのイベントをサポートするように、データ変換コードを更新する。
3. **Validateを**クリックすると、コードの出力のプレビューが表示され、`/users/track` リクエストとして受け入れられるかどうかがチェックされる。
4. データ変換を保存して有効にする。

![\]({% image_buster /assets/img/typeform/typeform_test_result.png %})

#### リクエスト・ボディのフォーマット

この戻り値は、Brazeの `/users/track` リクエストの本文フォーマットに準拠しなければなりません。

- 変換コードは JavaScript プログラミング言語で受け入れられます。if/else ロジックなど、標準的な JavaScript 制御フローがすべてサポートされています。
- 変換コードは、payload 変数を介して Webhook リクエスト本体にアクセスする。この変数は、リクエスト本文の JSON を解析して読み込まれたオブジェクトです。
- `/users/track` エンドポイントでサポートされるすべてのフィーチャーがサポートされています。例を示します。
    - ユーザー属性オブジェクト、イベントオブジェクト、購入オブジェクト
    - 階層化属性と階層化カスタムイベントプロパティ
    - サブスクリプショングループの更新
    - 識別子としてのメールアドレス

## TypeformのWebhookペイロードの例

```json
Content-Type: application/json

{
  "event_id": "01HC3PTZN05GJWT0QDXXB2QV8F",
  "event_type": "form_response",
  "form_response": {
    "form_id": "uaIA4a7Y",
    "token": "7pctqdoqxg41to97pctqdibhqn6hqvto",
    "landed_at": "2023-10-06T23:57:52Z",
    "submitted_at": "2023-10-06T23:58:18Z",
    "hidden": { 
		"user_id": "hidden_value" 
    },
    "definition": {
      "id": "uaIA4a7Y",
      "title": "Project Feedback Survey",
      "fields": [
        {
          "id": "G0IbXtfvsfjV",
          "ref": "814b9fc2-e6d2-4672-accf-22f754b84f20",
          "type": "email",
          "title": "Please provide your email",
          "properties": {}
        },
        {
          "id": "lg82q3t0rK03",
          "ref": "e1503b62-0241-4269-9902-5c539abf305e",
          "type": "short_text",
          "title": "What was your role in the project?",
          "properties": {}
        },
        {
          "id": "UXftY0tSmuDV",
          "ref": "5b839dbb-566b-47de-a47e-b0914d9ccf7c",
          "type": "opinion_scale",
          "title": "How would you rate the overall performance of the team?",
          "properties": {}
        },
        {
          "id": "fE17bXVUEB4E",
          "ref": "fd6be99d-1ed1-4a4d-b811-f6ecdd8fa9b6",
          "type": "yes_no",
          "title": "Did the project meet its intended outcomes?",
          "properties": {}
        },
        {
          "id": "NmVOQFuI0vv9",
          "ref": "cd2b4176-db9a-49bb-a918-4463720bbc79",
          "type": "multiple_choice",
          "title": "Which area of the project do you think went well?",
          "properties": {},
          "choices": [
            {
              "id": "RvV3LaMEQ2eK",
              "ref": "2d5e0913-afe9-491c-b31c-0648dd397d56",
              "label": "Communication"
            },
            {
              "id": "7iXmfpPMeQvz",
              "ref": "7a7749d2-5cd6-4bf7-9726-65c7ab11ec83",
              "label": "Planning"
            },
            {
              "id": "1No85DZlvP6f",
              "ref": "d7b7304a-776b-4630-8bee-7dc7ef9c9404",
              "label": "Execution"
            },
            {
              "id": "ruMnsZWjyalW",
              "ref": "41dc926a-85af-4625-8a61-725fda35afda",
              "label": "Problem Solving"
            },
            {
              "id": "CexnFN3roprG",
              "ref": "cfdd2da4-8c57-4ff1-b4c0-1a5262e2ff84",
              "label": "Other"
            }
          ]
        },
        {
          "id": "ZJop9pvoObzk",
          "ref": "ce903cda-7e27-4b4c-9fa8-0623c47c61b4",
          "type": "multiple_choice",
          "title": "Which area of the project do you think could be improved?",
          "properties": {},
          "choices": [
            {
              "id": "YQLArFf0Wks5",
              "ref": "09fa30c7-7bdc-4753-971e-0d922638d023",
              "label": "Communication"
            },
            {
              "id": "iGjaELgfnChw",
              "ref": "61820c89-3426-464d-b031-c06de5125fd5",
              "label": "Planning"
            },
            {
              "id": "2EyI5tozFxro",
              "ref": "c35f71b2-2a6d-4488-a1ba-87c2e711ce19",
              "label": "Execution"
            },
            {
              "id": "VGtsIHBLAhME",
              "ref": "6c171a9a-9324-4f7d-adb9-290bd701efe9",
              "label": "Problem Solving"
            },
            {
              "id": "lVdV7MIL1anS",
              "ref": "faba551f-4e6b-4377-9f74-11ca4fcc8ed5",
              "label": "Other"
            }
          ]
        },
        {
          "id": "hcCNsLUHGXgv",
          "ref": "d1ae8537-0d5a-4ca8-bb6b-f8057f04d7e2",
          "type": "opinion_scale",
          "title": "How satisfied were you with the level of communication during the project?",
          "properties": {}
        },
        {
          "id": "dBqPlgeKejN2",
          "ref": "e2c884c1-0d92-4f18-9833-79dff0b3eef2",
          "type": "nps",
          "title": "How likely are you to recommend Braze for customer engagement services?",
          "properties": {}
        },
        {
          "id": "vLdpFmCmulF5",
          "ref": "a86e48ec-6d10-49fc-ac03-4ac1aad4bfec",
          "type": "dropdown",
          "title": "In which country was the project executed?",
          "properties": {}
        }
      ],
      "endings": [
        {
          "id": "LUpVm67y72vb",
          "ref": "30c03bdf-80b3-45f5-8307-df8ca49046b1",
          "title": "Thank you for taking the time to complete our survey!",
          "type": "thankyou_screen",
          "properties": {
            "button_text": "Create a typeform",
            "show_button": true,
            "share_icons": true,
            "button_mode": "default_redirect"
          }
        }
      ]
    },
    "answers": [
      {
        "type": "email",
        "email": "typeformintegration@example.com",
        "field": {
          "id": "G0IbXtfvsfjV",
          "type": "email",
          "ref": "814b9fc2-e6d2-4672-accf-22f754b84f20"
        }
      },
      {
        "type": "text",
        "text": "Project",
        "field": {
          "id": "lg82q3t0rK03",
          "type": "short_text",
          "ref": "e1503b62-0241-4269-9902-5c539abf305e"
        }
      },
      {
        "type": "number",
        "number": 9,
        "field": {
          "id": "UXftY0tSmuDV",
          "type": "opinion_scale",
          "ref": "5b839dbb-566b-47de-a47e-b0914d9ccf7c"
        }
      },
      {
        "type": "boolean",
        "boolean": true,
        "field": {
          "id": "fE17bXVUEB4E",
          "type": "yes_no",
          "ref": "fd6be99d-1ed1-4a4d-b811-f6ecdd8fa9b6"
        }
      },
      {
        "type": "choice",
        "choice": {
          "id": "ruMnsZWjyalW",
          "label": "Problem Solving",
          "ref": "41dc926a-85af-4625-8a61-725fda35afda"
        },
        "field": {
          "id": "NmVOQFuI0vv9",
          "type": "multiple_choice",
          "ref": "cd2b4176-db9a-49bb-a918-4463720bbc79"
        }
      },
      {
        "type": "choice",
        "choice": {
          "id": "lVdV7MIL1anS",
          "label": "Other",
          "ref": "faba551f-4e6b-4377-9f74-11ca4fcc8ed5"
        },
        "field": {
          "id": "ZJop9pvoObzk",
          "type": "multiple_choice",
          "ref": "ce903cda-7e27-4b4c-9fa8-0623c47c61b4"
        }
      },
      {
        "type": "number",
        "number": 8,
        "field": {
          "id": "hcCNsLUHGXgv",
          "type": "opinion_scale",
          "ref": "d1ae8537-0d5a-4ca8-bb6b-f8057f04d7e2"
        }
      },
      {
        "type": "number",
        "number": 6,
        "field": {
          "id": "dBqPlgeKejN2",
          "type": "nps",
          "ref": "e2c884c1-0d92-4f18-9833-79dff0b3eef2"
        }
      },
      {
        "type": "choice",
        "choice": {
          "id": "KESjdqLseWmC",
          "label": "Brazil",
          "ref": "250210d9-33f6-4734-8ec6-06005a8ef66d"
        },
        "field": {
          "id": "vLdpFmCmulF5",
          "type": "dropdown",
          "ref": "a86e48ec-6d10-49fc-ac03-4ac1aad4bfec"
        }
      }
    ],
    "ending": {
      "id": "LUpVm67y72vb",
      "ref": "30c03bdf-80b3-45f5-8307-df8ca49046b1"
    }
  }
}
```

## データ変換のユースケース

以下は、[TypeformのWebhookペイロードを使って](#example-typeform-webhook-payload)作成したテンプレートの例である。これらのテンプレートは出発点として使うことができる。ゼロから始めることも、適当に特定のコンポーネントを削除することもできる。

これらのテンプレート例では、Brazeプロファイルにカスタムイベントをロギングしている。Typeformのタイトルはカスタムイベント名として渡され、Typeformの結果はイベントプロパティとして渡される。これらのテンプレート例では、TypeformのCalendly、ファイルアップロード、支払いの質問タイプは考慮されていない。

### ユースケース:識別子としてのメール

このテンプレート例では、メールアドレス（タイプフォーム内のメールアドレスの質問から取得）を識別子として使用している。

{% alert note %}
メールアドレスを識別子として使用する場合は、`/users/track` エンドポイントに関する[よくある質問を]({{site.baseurl}}/api/endpoints/user_data/post_user_track#frequently-asked-questions)参照し、期待される動作の詳細を確認すること。
{% endalert %}

{% tabs local %}
{% tab Input %}

```javascript
/* In the Typeform webhook payload each question is stored as a “title” within each object of the “fields” array. Our code defines a “title” variable where we store the value of each field title. */
const titles = payload.form_response.definition.fields.map(field => field.title);

/* The answers array is saved to a “tfAnswers” variable so this can be iterated through */
const tfAnswers = payload.form_response.answers;

/* The value of a response will change based on the type of question, to account for this we have created a function that iterates through the answers, determines what the answer type is and then, based on the type, adds the associated response to an extractedValues array. */
const extractValues = (tfAnswers) => {
	const extractedValues = [];

	tfAnswers.forEach((tfAnswer) => {
		let result = null;

		if (tfAnswer.type === 'choices') {
			if (tfAnswer.choices) {
				// Multiple choices
				let labels = tfAnswer.choices.labels || [];
				if (tfAnswer.choices.other) {
					labels.push(tfAnswer.choices.other);
				}
				result = labels;
			}
		} else if (tfAnswer.type === 'choice' && Object.keys(tfAnswer.choice).length > 1) {
			// Single choice
			result = tfAnswer.choice && tfAnswer.choice.other ?
				tfAnswer.choice.other.toString() :
				tfAnswer.choice.label.toString();
		} else if (tfAnswer.type === 'dropdown') {
			// Dropdown
			result = tfAnswer.text;
		} else {
			// For other types, use the type-specific value
			result = tfAnswer[tfAnswer.type];
		}

		extractedValues.push(result);
	});

	return extractedValues;
};

/* We use the above defined function, passing it the “tfAnswers” variable that holds the answers portion of the Typeform webhook payload and save the output to a ”values” variable */
const values = extractValues(tfAnswers);

/* Finally, the values within the previously assigned “titles” variable and “values” variable are paired together in an object as the values to a “question” key and “answer” key in a “responses” array of objects variable. */
const results = titles.map((title, index) => {
	return {
		question: title,
		answer: values[index],
	};
});

/* The code defines a variable, "brazecall", to build a /users/track request. Within the request, the typeform title is populated as the event name, and our “results” variable (where all of our question/answer pairs are stored), is assigned as the event’s properties. */
let brazecall = {
	"events": [{
		"email": payload.form_response.answers.find(answer => answer.type === 'email').email,
		"name": payload.form_response.definition.title,
		"time": new Date().toISOString(),
		"properties": {
			"responses": results
		}
	}]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return “brazecall” to create an output
return brazecall;
```

{% endtab %}
{% tab Output %}

```json
{
  "events": [
    {
      "email": "an_account@example.com",
      "name": "Project Feedback Survey",
      "time": "2023-10-17T18:21:39.527Z",
      "properties": {
        "responses": [
          {
            "question": "Please provide your email",
            "answer": "an_account@example.com"
          },
          {
            "question": "What was your role in the project?",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "How would you rate the overall performance of the team?",
            "answer": 5
          },
          {
            "question": "Did the project meet its intended outcomes?",
            "answer": true
          },
          {
            "question": "If you answered \"No\" to the previous question, please explain why. If you answered \"Yes\", skip this question.",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "Which area of the project do you think went well?",
            "answer": "Communication"
          },
          {
            "question": "Which area of the project do you think could be improved?",
            "answer": "Communication"
          },
          {
            "question": "How satisfied were you with the level of communication during the project?",
            "answer": 5
          },
          {
            "question": "How likely are you to recommend Braze for customer engagement services?",
            "answer": 5
          },
          {
            "question": "In which country was the project executed?",
            "answer": "United States"
          }
        ]
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### ユースケース:隠しフィールドで渡された識別子を使う

Typeform Hidden Fieldsを利用することで、ユーザーIDなどのデータを、Typeformのレスポンスで渡すことなく、TypeformのWebhookペイロードに渡すことができる。

このテンプレート例では、"user_id "隠しフィールドを使用し、これを`/users/track` リクエストのペイロードに`external_id` として渡している。ここでは "user_id "を使用しているが、フィールドは必要に応じて変更することができる。

{% tabs local %}
{% tab Input %}

```javascript
/* In the Typeform webhook payload each question is stored as a “title” within each object of the “fields” array. Our code defines a “title” variable where we store the value of each field title. */
const titles = payload.form_response.definition.fields.map(field => field.title);

/* The answers array is saved to a “tfAnswers” variable so this can be iterated through */
const tfAnswers = payload.form_response.answers;

/* The value of a response will change based on the type of question, to account for this we have created a function that iterates through the answers, determines what the answer type is and then, based on the type, adds the associated response to an extractedValues array. */
const extractValues = (tfAnswers) => {
	const extractedValues = [];

	tfAnswers.forEach((tfAnswer) => {
		let result = null;

		if (tfAnswer.type === 'choices') {
			if (tfAnswer.choices) {
				// Multiple choices
				let labels = tfAnswer.choices.labels || [];
				if (tfAnswer.choices.other) {
					labels.push(tfAnswer.choices.other);
				}
				result = labels;
			}
		} else if (tfAnswer.type === 'choice' && Object.keys(tfAnswer.choice).length > 1) {
			// Single choice
			result = tfAnswer.choice && tfAnswer.choice.other ?
				tfAnswer.choice.other.toString() :
				tfAnswer.choice.label.toString();
		} else if (tfAnswer.type === 'dropdown') {
			// Dropdown
			result = tfAnswer.text;
		} else {
			// For other types, use the type-specific value
			result = tfAnswer[tfAnswer.type];
		}

		extractedValues.push(result);
	});

	return extractedValues;
};

/* We use the above defined function, passing it the “tfAnswers” variable that holds the answers portion of the Typeform webhook payload and save the output to a ”values” variable */
const values = extractValues(tfAnswers);

/* Finally, the values within the previously assigned “titles” variable and “values” variable are paired together in an object as the values to a “question” key and “answer” key in a “responses” array of objects variable. */
const results = titles.map((title, index) => {
	return {
		question: title,
		answer: values[index],
	};
});

/* The code defines a variable, "brazecall", to build a /users/track request. Within the request, the typeform title is populated as the event name, and our “results” variable (where all of our question/answer pairs are stored), is assigned as the event’s properties. */
let brazecall = {
	"events": [{
		"external_id": payload.form_response.hidden.user_id,
		"name": payload.form_response.definition.title,
		"time": new Date().toISOString(),
		"properties": {
			"responses": results
		}
	}]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return “brazecall” to create an output
return brazecall;
```

{% endtab %}
{% tab Output %}

```json
{
  "events": [
    {
      "external_id": "hidden_value",
      "name": "Project Feedback Survey",
      "time": "2023-10-17T18:27:22.209Z",
      "properties": {
        "responses": [
          {
            "question": "Please provide your email",
            "answer": "an_account@example.com"
          },
          {
            "question": "What was your role in the project?",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "How would you rate the overall performance of the team?",
            "answer": 5
          },
          {
            "question": "Did the project meet its intended outcomes?",
            "answer": true
          },
          {
            "question": "If you answered \"No\" to the previous question, please explain why. If you answered \"Yes\", skip this question.",
            "answer": "Lorem ipsum dolor"
          },
          {
            "question": "Which area of the project do you think went well?",
            "answer": "Communication"
          },
          {
            "question": "Which area of the project do you think could be improved?",
            "answer": "Communication"
          },
          {
            "question": "How satisfied were you with the level of communication during the project?",
            "answer": 5
          },
          {
            "question": "How likely are you to recommend Braze for customer engagement services?",
            "answer": 5
          },
          {
            "question": "In which country was the project executed?",
            "answer": "United States"
          }
        ]
      }
    }
  ]
}
```

{% endtab %}
{% endtabs %}

### ステップ 4:TypeformのWebhookを公開する

データ変換を書いたら、**Validateを**クリックして、データ変換コードが正しくフォーマットされ、期待通りに動作することを確認する。その後、データ変換を保存してアクティブにする。

一度アクティブにすると、カスタムイベントデータはユーザーがフォームに入力した際にユーザープロファイルに記録される。

![\]({% image_buster /assets/img/typeform/typeform_custom_event.png %})

## モニタリングとトラブルシューティング

トランスフォーメーションのモニタリングとトラブルシューティングの詳細については、[トランスフォーメーションのモニタリングの]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#step-5-monitor-your-transformation)セクションを参照のこと。