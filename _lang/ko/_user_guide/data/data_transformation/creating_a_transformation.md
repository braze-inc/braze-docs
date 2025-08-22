---
nav_title: 변환 만들기
article_title: 변환 만들기
page_order: 1
page_type: reference
description: "이 참조 문서에서는 Braze 데이터 변환을 사용하여 변환을 만드는 단계를 설명합니다."
---

# 변환 만들기

> Braze 데이터 트랜스포메이션을 사용하면 웹훅 통합을 구축 및 관리하여 외부 플랫폼에서 Braze로 데이터 흐름을 자동화할 수 있습니다. 이러한 웹훅 통합을 통해 더욱 정교한 마케팅 사용 사례를 지원할 수 있습니다. 기본 코드에서 데이터 변환을 구축하거나 특정 외부 플랫폼에서 시작하는 데 도움이 되는 전용 템플릿 라이브러리를 사용하여 데이터 변환을 구축할 수 있습니다.

## 필수 조건 

| 요구 사항 | 설명 |
| --- | --- |
| 2단계 인증 또는 SSO | 계정에 2단계 [인증]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#two-factor-authentication) (2FA) 또는 [싱글사인온]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#single-sign-on-sso-authentication) (SSO)을 사용하도록 설정해야 합니다. |
| 올바른 권한 | 계정 매니저 또는 워크스페이스 매니저이거나 "변환 관리" 사용자 권한이 있어야 합니다. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 1단계: 소스 플랫폼 식별

Braze에 연결하려는 외부 플랫폼을 식별하고 해당 플랫폼이 웹훅을 지원하는지 확인합니다. 이러한 설정을 "API 알림" 또는 "웹 서비스 요청"이라고도 합니다.

다음은 해당 플랫폼에 로그인하여 구성할 수 있는 [Typeform 웹훅의](https://www.typeform.com/help/a/webhooks-360029573471/) 예시입니다:

![]({% image_buster /assets/img/data_transformation/data_transformation8.png %})

## 2단계: 변환 만들기

{% multi_lang_include create_transformation.md location="default" %}

## 3단계: 테스트 웹훅 보내기(권장)

이 단계는 선택 사항이지만 소스 플랫폼에서 새로 만든 변환으로 테스트 웹훅을 전송하는 것이 좋습니다.

1. 변환의 URL을 복사합니다.
2. 소스 플랫폼에서 '테스트 보내기' 기능을 찾아 이 URL로 전송할 샘플 웹훅을 생성하도록 합니다. 
- 소스 플랫폼에서 요청 유형을 묻는 메시지가 표시되면 **POST**를 선택합니다.
- 소스 플랫폼에서 인증 옵션을 제공하는 경우 **인증 안 함**을 선택합니다.
- 소스 플랫폼에서 비밀번호를 요청하는 경우 **비밀번호 없음**을 선택합니다.
3. Braze 대시보드에서 페이지를 새로고침하여 웹훅이 수신되었는지 확인합니다. 수신된 경우 **가장 최근 웹훅** 아래에 웹훅 페이로드가 표시될 것입니다.

Typeform의 모습은 다음과 같습니다:

![Example Data Transformation code that maps the webhook to Braze user profiles.]({% image_buster /assets/img/data_transformation/data_transformation11.png %})

{% alert note %}
Braze 데이터 트랜스포메이션은 아직 웹훅에 대한 특별한 확인이나 인증이 필요한 외부 플랫폼을 지원하지 않을 수 있습니다. Braze 데이터 트랜스포메이션에 이러한 유형의 플랫폼을 사용하는 데 관심이 있다면 [제품 피드백]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)을 남겨 주세요.
{% endalert %}

## 4단계: 변환 코드 작성

자바스크립트 코드에 대한 경험이 거의 없거나 더 자세한 지침을 원하시면 **무경험자 - POST를 참조하세요: 사용자 추적** 또는 **초급 - PUT: 여러 카탈로그 항목 업데이트** 탭에서 변환 코드를 작성합니다.

개발자이거나 자바스크립트 코드에 대한 상당한 경험이 있는 경우 **고급 - POST를 참조하세요: 사용자 추적** 탭에서 변환 코드 작성에 대한 자세한 지침을 확인하세요.

{% alert tip %}
Braze 데이터 트랜스포메이션에는 ChatGPT에 코드 작성을 도와달라고 요청하는 AI 보조 조종사가 있습니다. AI 코파일럿에 액세스하려면 <i class="fa-solid fa-wand-magic-sparkles"></i> **변환 코드 생성을** 선택합니다. 이를 사용하려면 웹훅을 변환에 전송해야 합니다. **코드 삽입** > **템플릿 삽입**을 선택하여 템플릿 라이브러리에 액세스할 수도 있습니다.

![]({% image_buster /assets/img/data_transformation/data_transformation3.png %})
{% endalert %}

{% tabs %}
{% tab 초급 - 사용자 추적 %}

여기에서 다양한 웹훅 값을 Braze 사용자 프로필에 매핑하는 방법을 정의하는 변환 코드를 작성합니다.

1. 새 트랜스폼에는 **트랜스폼 코드** 섹션에 이 기본 템플릿이 있습니다:

```java
// Here, we will define a variable, "brazecall", to build up a `/users/track` request
// Everything from the incoming webhook is accessible via the special variable "payload"
// So you can template in desired values in your `/users/track` request with dot notation, such as payload.x.y.z

let brazecall = {
  "attributes": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "attribute_1": payload.attribute_1
    }
  ],
  "events": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "name": payload.event_1,
      "time": new Date(),
      "properties": {
        "property_1": payload.event_1.property_1
      }
    }
  ],
  "purchases": [
    {
      "external_id": payload.user_id,
      "_update_existing_only": true,
      "product_id": payload.product_id,
      "currency": payload.currency,
      "price": payload.price,
      "quantity": payload.quantity,
      "time": payload.timestamp,
      "properties": {
        "property_1": payload.purchase_1.property_1
      }
    }
  ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\. 변환 호출에 사용자 지정 속성, 사용자 지정 이벤트 및 구매를 포함하려면 3단계로 건너뛰세요. 그렇지 않으면 필요하지 않은 섹션을 삭제하세요.<br><br>
3\. 각 속성, 이벤트 및 구매 개체에는 `external_id`, `user_alias`, `braze_id`, `email` 또는 `phone`과 같은 사용자 식별자가 필요합니다. 들어오는 웹훅의 페이로드에서 사용자 식별자를 찾은 다음, 페이로드 줄을 통해 변환 코드의 해당 값에 템플릿을 입력합니다. 점 표기법을 사용하여 페이로드 개체 속성에 액세스합니다. <br><br>
4\. 속성, 이벤트 또는 구매로 표현하려는 웹훅 값을 찾아 페이로드 줄을 통해 변환 코드에서 해당 값을 템플릿화합니다. 점 표기법을 사용하여 페이로드 개체 속성에 액세스합니다.<br><br>
5\. 각 속성, 이벤트 및 구매 개체에 대해 `_update_existing_only` 값을 검토합니다. 존재하지 않을 수 있는 새 사용자를 생성하려면 `false`로 설정합니다. 기존 프로필만 업데이트하려면 `true` 으로 그대로 둡니다.<br><br>
6\. **유효성 검사**를 클릭하여 코드 출력의 미리 보기를 반환하고 허용되는 `/users/track` 요청인지 확인합니다.<br><br>
7\. 변환을 활성화하세요. 코드를 활성화하기 전에 코드에 대한 추가 도움이 필요하면 Braze 계정 관리자에게 문의하세요.<br><br>
7\. 소스 플랫폼에서 웹훅 전송을 시작하도록 합니다. 들어오는 각 웹훅에 대해 변환 코드가 실행되고 사용자 프로필이 업데이트되기 시작합니다. 

이제 웹훅 통합이 완료되었습니다!

{% endtab %}
{% tab 초급 - 카탈로그 항목 업데이트 %}

여기에서 다양한 웹훅 값을 Braze 카탈로그 항목 업데이트에 매핑하는 방법을 정의하는 변환 코드를 작성할 수 있습니다.

1. 새 변환에는 **변환 코드** 섹션에 이 기본 템플릿이 포함됩니다:

```java
// This is a default template that you can use as a starting point
// Feel free to delete this entirely to start from scratch, or to edit specific components

// First, this code defines a variable, "brazecall", to build a PUT /catalogs/{catalog_name}/items request
// Everything from the incoming webhook is accessible via the special variable "payload"
// As such, you can template in desired values in your request with JS dot notation, such as payload.x.y.z

let brazecall = {
  // For Braze Data Transformation to update Catalog items, the special variable "catalog_name" is required
  // This variable is used to specify the catalog name which would otherwise go in the request URL
  "catalog_name": "catalog_name",
  
  // After defining "catalog name", construct the Update Multiple Catalog Items request as usual below
  // Documentation for the destination endpoint: https://www.braze.com/docs/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/
  "items": [
    {
      "id": payload.item_id_1,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_2,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    },
    {
      "id": payload.item_id_3,
      "catalog_column1": "string",
      "catalog_column2": 1,
      "catalog_column3": true,
      "catalog_column4": "2021-09-03T09:03:19.967+00:00",
      "catalog_column5": {
        "Latitude": 33.6112,
        "Longitude": -117.8711
      }
    }
  ]
};

// After the request body is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{:start="2"}
2\. `/catalogs` 대상에 대한 변환에는 업데이트할 특정 카탈로그를 정의하는 `catalog_name` 이 필요합니다. 이 필드를 하드 코딩하거나 페이로드 라인을 통해 웹훅 필드로 필드를 템플릿화할 수 있습니다. 점 표기법을 사용하여 페이로드 개체 속성에 액세스합니다.<br><br>
3\. 항목 배열의 `id` 필드를 사용하여 카탈로그에서 업데이트할 항목을 정의합니다. 이러한 필드를 하드 코딩하거나 페이로드 라인을 통해 웹훅 필드에 템플릿을 만들 수 있습니다. <br><br> `catalog_column` 는 자리 표시자 값입니다. 항목 객체에는 카탈로그에 존재하는 필드만 포함되어 있는지 확인합니다.<br><br>
4\. **유효성 검사를** 선택하여 코드 출력의 미리 보기를 반환하고 [여러 카탈로그 항목 업데이트 엔드포인트에]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items) 대한 허용 가능한 요청인지 확인합니다.<br><br>
5\. 변환을 활성화하세요. 코드를 활성화하기 전에 코드에 대한 추가 도움이 필요하면 Braze 계정 관리자에게 문의하세요.<br><br>
6\. 소스 플랫폼에 웹훅 전송을 시작하도록 설정되어 있는지 확인하세요. 들어오는 각 웹훅에 대해 변환 코드가 실행되고 카탈로그 항목이 업데이트되기 시작합니다.

이제 웹훅 통합이 완료되었습니다!

{% endtab %}
{% tab 고급 - 사용자 추적 %}

이 단계에서는 소스 플랫폼에서 웹훅 페이로드를 자바스크립트 객체 반환 값으로 변환합니다. 이 반환 값은 `/users/track` 엔드포인트 요청 본문 형식을 따라야 합니다:

- 변환 코드는 자바스크립트 프로그래밍 언어로 사용할 수 있습니다. if/else 로직과 같은 모든 표준 자바스크립트 제어 흐름이 지원됩니다.
- 변환 코드는 `payload` 변수를 통해 웹훅 요청 본문에 액세스합니다. 이 변수는 요청 본문 JSON을 파싱하여 채워지는 객체입니다.
- `/users/track` 엔드포인트에서 지원되는 모든 기능이 지원됩니다:
  - 사용자 속성 개체, 이벤트 개체 및 구매 개체
  - 중첩된 속성 및 중첩된 사용자 지정 이벤트 속성
  - 구독 그룹 업데이트
  - 식별자로서의 이메일 주소

**유효성 검사**를 선택하여 코드 출력의 미리 보기를 반환하고 허용되는 `/users/track` 요청인지 확인합니다.

{% alert note %}
외부 네트워크 요청, 타사 라이브러리 및 비 JSON 웹훅은 현재 지원되지 않습니다.
{% endalert %}

{% endtab %}
{% endtabs %}

## 5단계: 변환 모니터링

변환을 활성화한 후 기본 **변환** 페이지의 애널리틱스에서 성과 요약을 참조하세요.

* **수신 요청:** 이 변환의 URL에서 수신된 웹훅의 수입니다. 수신 요청이 0이면 소스 플랫폼에서 웹훅을 전송하지 않았거나 연결할 수 없는 것입니다.
* **배송:** 수신 요청을 받은 후 데이터 변환은 변환 코드를 적용하여 선택한 Braze 대상에 전송합니다.

수신 요청의 100%가 배달로 이어지는 것은 좋은 목표입니다. 배달 횟수는 수신 요청 횟수를 초과하지 않습니다.

### 문제 해결

자세한 모니터링 및 문제 해결 방법은 특정 로그 페이지에서 워크스페이스 전반의 모든 변환에 대한 마지막 1,000건의 수신 요청이 기록되는 **로그를** 참조하세요. 각 로그를 선택하여 들어오는 요청 본문, 변환 출력 및 변환 대상의 응답 본문을 볼 수 있습니다.

배달되지 않으면 변환 코드에 구문 오류가 있는지 확인하고 코드가 컴파일되는지 확인합니다. 그런 다음 출력이 유효한 대상 요청인지 확인합니다.

수신 요청 수보다 적은 전송은 적어도 일부 웹훅이 성공적으로 전송되었음을 의미합니다. 예를 들어 오류는 변환 로그를 참조하여 예상되는 변환 출력이 있는지 확인하세요. 변환 코드가 수신된 웹훅의 모든 배리언트를 설명하지 못할 수 있습니다.


