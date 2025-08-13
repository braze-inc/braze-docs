---
nav_title: 활용 사례
article_title: Braze 데이터 혁신 사용 사례
page_order: 2
page_type: reference
description: "이 참조 문서에서는 Braze 데이터 변환의 몇 가지 사용 사례를 제공합니다."
---

# 데이터 혁신 사용 사례

> 예시 외부 플랫폼의 웹훅과 Braze 데이터 트랜스포메이션의 조합으로 다음과 같은 사용 사례를 고려해 보세요.

## 리드 생성

웹사이트에 리드 생성 Typeform 양식을 호스팅합니다. 신규 사용자가 이 양식을 작성하면 됩니다:
- Braze에서 새 사용자를 생성합니다.
- Braze 이메일 목록에 추가하세요.
- 응답자의 답변은 향후 개인화된 메시징 경험을 강화할 수 있는 귀중한 퍼스트파티 데이터이므로 일부 응답을 Braze에서 커스텀 속성으로 동기화하세요.

## 서비스 티켓 열기

고객이 Zendesk와 같은 플랫폼에서 고객 서비스 티켓을 열면 다음과 같이 할 수 있습니다:
- Zendesk 티켓이 만들어질 때 Braze에서 사용자 지정 이벤트를 작성하세요.
- Zendesk에 부정적인 CSAT 등급이 제공되면 Braze에서 이벤트 속성을 사용하여 사용자 지정 이벤트를 작성하세요.

## Braze와 통합

Braze has an integration with [Iterate]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/surveys/iterate/), a customer insights and survey platform. 데이터 변환을 사용하면 여러 개의 사용자 지정 속성을 저장하는 기존 통합 대신 하나의 중첩된 사용자 지정 속성 아래에 여러 개의 설문조사 응답을 저장할 수 있습니다.

## 변환 코드 예시

설문조사 응답이 수신될 때마다 전송하는 설문조사 플랫폼인 Typeform의 페이로드 샘플을 살펴보세요.

![]({% image_buster /assets/img/data_transformation/data_transformation2.png %})

{% tabs local %}
{% tab 기본 변환 %}

이 예에서는 설문조사 응답을 속성으로 사용하여 설문조사가 완료되었음을 나타내는 이벤트를 작성합니다:

```
return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_rating": payload.form_response.answers[1].number
    }
  ],
  "events": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
}
```

{% endtab %}
{% tab 고급 변환 %}

기본 변환 예제에서 더 나아가 `if` 문을 도입하여 사용자를 답변 중 하나로 분류해 보겠습니다.

```
let nps_category;
let nps_number = payload.form_response.answers[1].number;
if (nps_number < 7) {
  nps_category = "Detractor";
} else if (nps_number == 7 || nps_number == 8) {
  nps_category = "Passive";
} else if (nps_number > 8) {
  nps_category = "Promoter";
}

return {
  "attributes": [ 
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "home_city": payload.form_response.answers[0].text,
      "home_weather_NPS_category": nps_category
    }
  ],
  "events": [
    {
      "email": payload.form_response.hidden.email_address,
      "_update_existing_only": true,
      "name": "weather_survey_completed",
      "time": new Date(),
      "properties": {
        "form_id": payload.form_response.form_id
      }
    }
  ]
};
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/data_transformation/data_transformation2.png %}