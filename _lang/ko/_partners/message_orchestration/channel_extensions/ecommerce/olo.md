---
nav_title: Olo
article_title: Olo
description: "이 문서에서는 모든 접점에서 접객 서비스를 제공하는 선도적인 레스토랑용 개방형 SaaS 플랫폼인 Braze와 Olo의 파트너십에 대해 설명합니다."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> [Olo][1]는 모든 터치포인트에서 접객 서비스를 제공하는 레스토랑을 위한 선도적인 개방형 SaaS 플랫폼입니다.

Olo와 Braze를 통합하면 다음과 같이 할 수 있습니다:

- Braze에서 사용자 프로필을 업데이트하여 Olo 사용자 프로필과 일관성 유지
- Olo 이벤트에 기반하여 Braze에서 적절한 차선책 메시지 보내기

## 전제 조건

| 요구 사항 | 설명 |
| ----------- | ----------- |
| Olo 계정 | 이 파트너십을 이용하려면 웹훅에 액세스할 수 있는 Olo 계정이 필요합니다. Olo 대시보드 내의 [셀프 서비스 웹훅 도구를](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) 통해 웹훅 구독을 설정하세요. |
| Braze 데이터 변환 | Olo에서 데이터를 받으려면 [데이터 변환 URL]({{site.baseurl}}/data_transformation/)이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

웹훅은 주문 완료, 게스트 옵트인, 주문 수령 등과 같은 이벤트를 포함하여 사용자 및 사용자의 행동에 대한 이벤트 기반 정보를 Olo가 Braze에 전송하는 방법입니다. Olo 웹훅은 일반적으로 작업을 수행한 후 몇 초 내에 이벤트를 Braze에 전달합니다.

## 면책 조항

Olo에서는 승인된 각 브랜드에 대해 환경당 하나의 웹훅으로 제한되며, 모두 동일한 **대상 URL**로 전송됩니다. 브랜드마다 다른 URL을 사용할 수 있지만 동일한 브랜드의 이벤트는 URL을 공유해야 합니다. Braze에서는 Olo에서 사용할 수 있는 변환을 한 번만 만들 수 있다는 뜻입니다.

이 단일 변환 내에서 여러 개의 Olo 이벤트를 처리하려면 각 웹훅에서 `X-Olo-Event-Type` 헤더를 찾아보세요. 이 헤더를 사용하면 다양한 Olo 이벤트를 조건부로 처리할 수 있습니다.

## 통합

### 1단계: Olo의 테스트 이벤트를 허용하도록 Braze 데이터 변환 설정 {#step-1}

{% multi_lang_include create_transformation.md location="default" %}

### 2단계: Olo 웹훅 설정

Olo 대시보드 내의 [셀프 서비스 웹훅 툴][2]을 사용하여 데이터 변환에 보낼 웹훅을 설정합니다.

1. Braze로 전송할 이벤트 선택
2. **대상 URL**을 구성합니다. [1단계에서](#step-1) 생성한 데이터 변환 URL이 됩니다.

{% alert note %}
`OAuth` 및 `X-Olo-Signature` 헤더 공유 비밀은 변환에 필요하지 않습니다.
{% endalert %}

{:start="3"}
3\. 데이터 변환에 [테스트 이벤트][3]를 전송하여 웹훅이 올바르게 구성되었는지 확인합니다. [개발자 도구 권한이][4] 있는 Olo 대시보드 사용자만 테스트 이벤트를 보낼 수 있습니다.

Olo 웹훅 구성 프로세스를 완료하려면 테스트 이벤트 웹훅에서 성공적인 응답이 있어야 합니다.

### 3단계: 선택한 Olo 이벤트를 수락하도록 변환 코드 작성

이 단계에서는 소스 플랫폼에서 전송할 웹훅 페이로드를 자바스크립트 객체 반환 값으로 변환합니다.

1. 지원하려는 Olo 이벤트의 샘플 이벤트 페이로드와 함께 데이터 변환 URL로 요청을 전송합니다.. 요청 서식에 도움이 필요하면 [요청 본문 형식](#request-body-format)을 참조하세요.
2. 데이터 변환을 새로고침하고 **웹훅 세부 정보**에서 샘플 이벤트 페이로드를 볼 수 있는지 확인합니다.
3. 선택한 Olo 이벤트를 지원하도록 데이터 변환 코드를 업데이트합니다.
4. **유효성 검사**를 클릭하여 코드 출력의 미리 보기를 반환하고 허용되는 `/users/track` 요청인지 확인합니다.
5. 데이터 변환을 저장하고 활성화하세요.

#### 요청 본문 형식

이 반환 값은 Braze의 `/users/track` 요청 본문 형식을 준수해야 합니다:

- 변환 코드는 자바스크립트 프로그래밍 언어로 사용할 수 있습니다. if/else 로직과 같은 모든 표준 자바스크립트 제어 흐름이 지원됩니다.
- 변환 코드는 페이로드 변수를 통해 웹훅 요청 본문에 액세스합니다. 이 변수는 요청 본문 JSON을 파싱하여 채워지는 객체입니다.
- `/users/track` 엔드포인트에서 지원되는 모든 기능이 지원됩니다:
    - 사용자 속성 개체, 이벤트 개체 및 구매 개체
    - 중첩된 속성 및 중첩된 사용자 지정 이벤트 속성
    - 구독 그룹 업데이트
    - 식별자로서의 이메일 주소

## Olo 웹훅의 데이터 변환 예제

이 섹션에는 시작점으로 사용할 수 있는 예제 템플릿이 포함되어 있습니다. 처음부터 시작하거나 원하는 대로 특정 구성요소를 삭제할 수 있습니다.

각 템플릿에서 코드는 `/users/track` 요청을 구축하기 위한 변수(`brazecall`)를 정의합니다.

`/users/track ` 요청이 `brazecall`에 할당된 후 명시적으로 `brazecall`을 반환하여 출력을 생성합니다.

### 단일 이벤트 변환

단일 Olo 이벤트만 지원하려는 경우 `X-Olo-Event-Type` 헤더를 사용하여 `/users/track` 요청 페이로드를 조건부로 생성할 필요가 없습니다. 예를 들어, 구매 이벤트 또는 사용자 지정 이벤트를 사용자 프로필에 기록하는 경우 Olo 주문 완료 웹훅이 Braze로 전송됩니다.

### 각 제품을 구매로 기록

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

### 사용자 지정 이벤트 로깅하기

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

## 다중 이벤트 변환

Olo는 각 웹훅의 `X-Olo-Event-Type` 헤더 내에 이벤트 유형을 전송합니다. 단일 변환 내에서 여러 개의 Olo 웹훅 이벤트를 지원하려면 조건부 논리를 사용하여 이 헤더 유형의 값을 기반으로 웹훅 페이로드를 변환하세요.  

아래 변환 예제에서 JavaScript는 `UserSignedUp` 및 `OrderPlaced`의 이벤트에 대한 특정 페이로드를 생성합니다. 또한 `else` 조건은 `UserSignedUp` 및 `OrderPlaced`의 X-Olo-Event-Type 헤더 없이 Braze로 전송된 모든 Olo 이벤트에 대한 페이로드를 처리합니다.

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

### 4단계: Olo 웹훅 게시

Braze에서 데이터 변환을 활성화한 후, Olo 대시보드 내 [셀프 서비스 웹훅 툴][2]을 사용하여 웹훅을 게시합니다. 웹훅이 게시되면 데이터 변환이 Olo 웹훅 이벤트 메시지를 수신하기 시작합니다.

## 알아두어야 할 사항

### 재시도

Olo는 24시간 동안 최대 50회의 웹훅 호출을 재시도하여 HTTP 응답 상태 코드가 `429 - Too Many Requests` 또는 `5xx` 범위(예: 게이트웨이 시간 초과 또는 서버 오류로 인해 발생)인 경우 요청을 삭제하기 전에 웹훅 호출을 삭제합니다.

### 최소 1회 전달

웹훅 호출로 인해 HTTP 응답 상태 코드가 `429 - Too Many Requests` 또는 `5xx` 범위인 경우(예: 게이트웨이 시간 초과 또는 서버 오류로 인해 발생) Olo는 24시간 동안 최대 50회까지 메시지를 다시 시도한 후 포기합니다.

따라서 구독자는 웹훅을 여러 번 수신할 수 있습니다. `X-Olo-Message-Id` 헤더를 확인하여 중복을 무시하는 작업은 가입자가 수행해야 합니다.


[1]: https://www.olo.com/
[2]: https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks
[3]: https://developer.olo.com/docs/load/webhooks#operation/test
[4]: https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions