---
nav_title: DOTS.ECO
article_title: DOTS.ECO
description: "이 참조 문서에서는 Braze와 DOTS.ECO 통합에 대해 설명합니다."
alias: /partners/dots.eco/
page_type: partner
search_tag: Partner
---

# DOTS.ECO

> [DOTS.ECO](https://dots.eco) 를 사용하면 추적 가능한 디지털 인증서를 통해 실제 환경에 미치는 영향에 대해 사용자에게 보상할 수 있습니다. 각 인증서는 공유 가능한 인증서 URL 및 이미지 URL과 같은 메타데이터를 포함할 수 있으므로 사용자는 자신의 영향력 증명을 보고 다시 방문할 수 있습니다.

_This integration is maintained by DOTS.ECO._

## 이 통합 정보

Braze와 DOTS.ECO 는 고객 참여 여정을 실제 임팩트 보상으로 연결합니다. Braze 캔버스 또는 캠페인 단계에서 연결된 콘텐츠를 사용하여 DOTS.ECO 인증서 만들기 요청을 트리거할 수 있습니다. DOTS.ECO 인증서 메타데이터(예: `certificate_url` 및 `certificate_image_url`)를 반환하여 사용자 프로필에 커스텀 속성으로 저장하고 인앱 메시지, 콘텐츠 카드 및 푸시 알림과 같은 채널에서 재사용할 수 있습니다.

## 사용 사례

- 사용자가 주요 이벤트(구매, 레벨 완료, 구독, 추천)를 완료하면 임팩트 인증서를 트리거합니다.
- 연결된 콘텐츠 단계가 성공한 후 인앱 메시지에 개인화된 인증서 이미지를 표시합니다.
- 나중에 액세스할 수 있도록 인증서 URL이 포함된 '인증서 보기' 콘텐츠 카드를 추가합니다.
- 인증서 메타데이터(예: `certificate_url`, `certificate_image_url`, `certificate_header`, `greeting`)를 커스텀 속성으로 저장하여 향후 메시징에서 재사용할 수 있도록 합니다.
- 원격 사용자 ID를 사용하여 인증서를 할당하면 사용자가 나중에 영향을 청구하고 확인할 수 있습니다.
- 동일한 DOTS.ECO 사용자 업데이트 흐름을 유지하면서 영향 메시징(다른 카피/이미지)에 대해 A/B 테스트를 실행합니다.


## 필수 조건

시작하기 전에 다음이 필요합니다:

| Prerequisite | 설명 |
|---|---|
| DOTS.ECO account | DOTS.ECO 계정 액세스. |
| DOTS.ECO 자격 증명 | 이 문서의 요청에는 DOTS.ECO 앱 토큰, API 키 및 할당 ID가 필요합니다. 이를 검색하려면 DOTS.ECO 고객 성공 매니저에게 문의하세요. |
| Braze REST API key | A Braze REST API key with `users.track` permissions. 이 키는 Braze 대시보드의 **설정** > **API 키에서** 생성하세요. |
| Braze REST endpoint | [Your REST endpoint URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합 DOTS.ECO

### 1단계: 캔버스 생성 및 사용자 업데이트 단계 추가하기

Braze 대시보드에서 사용자가 주요 이벤트(예: 구매, 구독 또는 마일스톤)를 완료할 때 트리거되는 새 캔버스를 만듭니다.

입력 단계 바로 뒤에 사용자 업데이트 단계를 추가합니다. 이 단계는 연결된 콘텐츠를 통해 DOTS.ECO API를 호출하고 반환된 인증서 데이터를 사용자 프로필에 저장하는 데 사용됩니다.

이 단계를 사용하여 연결된 콘텐츠를 통해 DOTS.ECO API를 호출하고 반환된 인증서 데이터를 사용자 프로필에 저장합니다.

### 2단계: 고급 JSON을 작성합니다: 연결된 콘텐츠를 사용하여 DOTS.ECO 에 POST 요청을 합니다.

**사용자 업데이트** 단계에서 **고급 JSON 편집기로** 전환하고 연결된 콘텐츠를 사용하여 DOTS.ECO 인증서 API에 POST 요청을 합니다.

`capture` 태그 및 연결된 콘텐츠 요청을 사용하여 DOTS.ECO 의 인증서 엔드포인트를 호출합니다. 그런 다음 고객 프로필에 대한 응답을 커스텀 속성으로 저장합니다.

**연결된 콘텐츠 및 사용자 업데이트 예제**  
{% raw %}
```  
{% capture post_body %} 
{  
  "remote_user_email": "{{${email_address} | default: 'braze+nadav@dots.eco'}}",  
  "app_token": "YOUR_DOTS.ECO_APP_TOKEN",  
  "impact_qty": 1,  
  "remote_user_id": "{{${user_id} | default: ${braze_id}}}",  
  "allocation_id": "YOUR_DOTS.ECO_ALLOCATION_ID"  
}  
{% endcapture %}

{% connected_content https://impact.dots.eco/api/v1/certificate/add?format=sdk  
  :method post  
  :headers { "auth-token": "YOUR_DOTS.ECO_AUTH_TOKEN" }  
  :body {{post_body}}  
  :content_type application/json  
  :save result  
%}

{  
  "attributes": [  
    {  
      "certificate_image_url": "{{result.certificate_image_url}}",  
      "certificate_url": "{{result.certificate_url}}",  
      "certificate_id": "{{result.certificate_id}}"  
    }  
  ]  
}  
```
{% endraw %}

`https://impact.dots.eco/api/v1/certificate/add?format=sdk` 으로 요청을 보냅니다.

![DOTS.ECO 사용자 업데이트 단계.]({% image_buster /assets/img/dots_eco/dotseco_user_update.png %})

{% alert important %}  
이 통합은 캔버스 **사용자 업데이트** 단계 내에서 연결된 콘텐츠를 사용하여 DOTS.ECO API를 호출합니다. 먼저 API 클라이언트(예: Postman)로 요청을 테스트하여 토큰과 페이로드의 유효성을 검사하세요.  
{% endalert %}

### 3단계: 메시징에 인증서 표시하기

인증서 속성이 고객 프로필에 저장되면 다운스트림 캔버스 메시지 단계에서 참조할 수 있습니다.

![DOTS.ECO 흐름.]({% image_buster /assets/img/dots_eco/dots.eco_flow.png %})

![DOTS.ECO 메시지 단계.]({% image_buster /assets/img/dots_eco/dotseco_messages.png %})

![DOTS.ECO 메시지 작성기 섹션으로 이동합니다.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose.png %})

For example:  
- 다음을 사용하여 인앱 메시지에 인증서 이미지를 표시합니다. {% raw %}`{{custom_attribute.${certificate_image_url}}}`{% endraw %}  
- 다음을 사용하여 호스팅된 인증서에 연결합니다. {% raw %}`{{custom_attribute.${certificate_url}}}`{% endraw %}

![DOTS.ECO 메시지 온클릭 동작.]({% image_buster /assets/img/dots_eco/dotseco_messages_compose_onclickbehavior.png %})


이를 통해 인앱 메시지, 콘텐츠 카드 또는 영향력 확인 푸시 알림을 개인화할 수 있습니다.

## 문제 해결

**설정** > **메시지 활동 로그의** Braze 대시보드에서 연결된 콘텐츠 오류를 검토합니다.

- **연결된 콘텐츠가 비어** 있습니다: `:save result` 이 설정되어 있고 예상 응답 필드를 참조하고 있는지 확인합니다.
- **속성이 메시지 단계에 표시되지 않습니다**:
  - Braze의 커스텀 속성 이름이 사용자 업데이트 단계에서 설정한 속성과 정확히 일치하는지 확인합니다.
  - 사용자 업데이트 단계에서 **미리 보기 및 테스트** 탭을 사용하여 속성이 채워지는지 확인합니다. 그런 다음 사용자에게 테스트를 전송하고 속성이 사용자 프로필에 저장되었는지 확인합니다.
- **`422` 오류(처리할 수 없는 엔터티**)가 발생했습니다: 앱 토큰과 임팩트 수량이 유효한지 확인합니다.
- **`401` 오류입니다**: 인증 토큰이 있고 올바른지 확인합니다.
- **메시지 단계에 이미지 미리보기가 없습니다**: **사용자** 업데이트 단계에서 **사용자에게 테스트 보내기를** 선택한 다음 동일한 사용자를 사용하여 메시지를 미리 봅니다.