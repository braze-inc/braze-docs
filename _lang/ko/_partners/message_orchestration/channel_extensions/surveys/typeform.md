---
nav_title: Typeform
article_title: Typeform
description: "이 문서에서는 데이터, 피드백 등을 수집하는 사용하기 쉬운 툴인 Typeform과 Braze의 파트너십을 간략하게 설명합니다."
alias: /partners/typeform/
page_type: partner
search_tag: Partner
---

# Typeform

> [Typeform](https://www.typeform.com/)을 데이터, 피드백 등을 수집하는 사용하기 쉬운 툴입니다.

Braze와 Typeform을 통합하면 다음과 같이 할 수 있습니다:

- 유형 양식 응답에서 수집된 데이터로 Braze에서 사용자 프로필 업데이트하기
- Typeform에서 사용자의 인게이지먼트에 따라 Braze에서 메시징 트리거
- 사용자의 유형 양식 응답을 기반으로 Braze 메시징 개인화하기

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Typeform 계정 | 이 파트너십을 활용하려면 웹훅에 액세스할 수 있는 Typeform 계정이 필요합니다. |
| Braze 데이터 변환 | Typeform에서 데이터를 받으려면 [데이터 변환 URL]({{site.baseurl}}/data_transformation/)이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Typeform의 웹훅을 허용하도록 Braze 데이터 변환 설정 {#step-1}

{% multi_lang_include create_transformation.md location="typeform" %}

### 2단계: Typeform 웹훅 설정

웹훅을 설정하려면 [Typeform 웹훅 설명서](https://www.typeform.com/help/a/webhooks-360029573471/)의 단계를 따르세요.

4단계에서 데이터 변환 웹훅 URL을 **대상 URL**로 추가합니다.

![]({% image_buster /assets/img/typeform/typeform_add_webhook.png %}){: style="max-width:50%" }

**전달 보기**를 클릭하고 **테스트 요청 전송**을 클릭하여 데이터 변환에 테스트 이벤트를 보냅니다.

![]({% image_buster /assets/img/typeform/typeform_test_request.png %})

### 3단계: 선택한 Typeform 이벤트를 수락하도록 변환 코드를 작성합니다.

이 단계에서는 Typeform에서 전송할 웹훅 페이로드를 JavaScript 객체 반환 값으로 변환합니다.

1. 데이터 변환을 새로 고치고 **웹훅 세부 정보**에서 Typeform 테스트 페이로드를 볼 수 있는지 확인합니다.
2. 선택한 Typeform 이벤트를 지원하도록 데이터 변환 코드를 업데이트합니다.
3. **유효성 검사**를 클릭하여 코드 출력의 미리 보기를 반환하고 허용되는 `/users/track` 요청인지 확인합니다.
4. 데이터 변환을 저장하고 활성화하세요.

![]({% image_buster /assets/img/typeform/typeform_test_result.png %})

#### 요청 본문 형식

이 반환 값은 Braze의 `/users/track` 요청 본문 형식을 준수해야 합니다:

- 변환 코드는 자바스크립트 프로그래밍 언어로 사용할 수 있습니다. if/else 로직과 같은 모든 표준 자바스크립트 제어 흐름이 지원됩니다.
- 변환 코드는 페이로드 변수를 통해 웹훅 요청 본문에 액세스합니다. 이 변수는 요청 본문 JSON을 파싱하여 채워지는 객체입니다.
- `/users/track` 엔드포인트에서 지원되는 모든 기능이 지원됩니다:
    - 사용자 속성 개체, 이벤트 개체 및 구매 개체
    - 중첩된 속성 및 중첩된 사용자 지정 이벤트 속성
    - 구독 그룹 업데이트
    - 식별자로서의 이메일 주소

## Typeform 웹훅 페이로드 예시

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

## 데이터 혁신 사용 사례

다음은 [예제 Typeform 웹훅 페이로드](#example-typeform-webhook-payload)를 사용하여 빌드된 예제 템플릿입니다. 이러한 템플릿은 시작점으로 사용할 수 있습니다. 원하는 대로 처음부터 시작하거나 특정 구성 요소를 삭제할 수 있습니다.

이 예제 템플릿에서는 커스텀 이벤트를 Braze 프로필에 기록합니다. 유형 양식의 제목은 사용자 지정 이벤트 이름으로 전달되고 유형 양식 결과는 이벤트 속성으로 전달됩니다. 이 예제 템플릿은 Typeform의 캘린더, 파일 업로드 또는 결제 문제 유형을 다루지 않습니다.

### 사용 사례: 식별자로 이메일 사용

이 예제 템플릿에서는 이메일 주소(유형 양식 내의 이메일 주소 질문에서 캡처함)를 식별자로 사용합니다.

{% alert note %}
이메일 주소를 식별자로 사용하려는 경우 `/users/track` 엔드포인트에 대한 [자주 묻는 질문을]({{site.baseurl}}/api/endpoints/user_data/post_user_track#frequently-asked-questions) 검토하여 예상되는 동작에 대한 자세한 내용을 확인하세요.
{% endalert %}

{% tabs local %}
{% tab 입력 %}

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
{% tab 출력 %}

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

### 사용 사례: 숨겨진 필드에 전달된 식별자 사용

Typeform 숨겨진 필드를 사용하면 Typeform 응답에서 이 정보를 전달할 필요 없이 사용자 ID와 같은 데이터를 Typeform 웹훅 페이로드에서 전달할 수 있습니다.

이 예제 템플릿에서는 'user_id' 숨겨진 필드를 사용하고 이를 `/users/track` 요청 페이로드에 `external_id`로 전달합니다. 'user_id'를 사용하고 있지만 필요에 따라 필드를 수정할 수 있습니다.

{% tabs local %}
{% tab 입력 %}

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
{% tab 출력 %}

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

### 4단계: Typeform 웹훅 게시

데이터 변환을 작성한 후 **유효성 검사**를 클릭하여 데이터 변환 코드의 형식이 올바르게 지정되고 예상대로 작동하는지 확인합니다. 그런 다음, 데이터 변환을 저장하고 활성화합니다.

활성화되면 사용자가 양식을 작성할 때 커스텀 이벤트 데이터가 고객 프로필에 기록됩니다.

![]({% image_buster /assets/img/typeform/typeform_custom_event.png %})

## 모니터링 및 문제 해결

변환 모니터링 및 문제 해결에 대한 자세한 내용은 [변환 모니터링]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation/#step-5-monitor-your-transformation) 섹션을 참조하세요.