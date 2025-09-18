---
nav_title: Zendesk
article_title: Zendesk
description: "이 참조 문서에서는 Zendesk와 Braze 간의 파트너십을 간략히 설명합니다. Zendesk는 인기 있는 지원 스위트로, Braze 웹훅을 활용해 두 플랫폼 간의 지원 데이터를 동기화할 수 있습니다."
alias: /partners/zendesk/
page_type: partner
search_tag: Partner

---

# Zendesk

> [Zendesk Support Suite](https://www.zendesk.com/support-suite/) (ZSS)는 이메일, 웹챗, 음성 또는 소셜 메시징 앱을 사용한 옴니채널 지원을 통해 고객과 자연스러운 대화를 나눌 수 있는 기능을 기업에 제공합니다. Zendesk는 추적 및 상호 작용의 우선 순위를 중요시하는 간소화된 티켓 시스템을 제공하여 기업이 고객의 통합된 역사적 관점을 가질 수 있도록 합니다.

Braze 및 Zendesk 서버-투-서버 통합을 통해 다음을 활용할 수 있습니다: 
- Braze 웹훅을 사용하여 Braze에서 사용자 여정의 메시지 인게이지먼트로 인해 Zendesk에서 지원 티켓 생성을 자동화합니다. 예를 들어, 통합을 성공적으로 구현하고 테스트한 후, Braze는 '앱을 잘 사용하고 계신가요?' 인앱 메시지에 부정적으로 답한 사용자의 지원 티켓을 생성하여 지원 팀이 고객에게 후속 조치를 취할 수 있도록 합니다.
- Zendesk 웹훅을 사용하여 Zendesk의 활동으로 인해 Braze에서 고객 프로필을 업데이트하는 등의 양방향 사용 사례를 지원합니다. 예를 들어, 티켓이 해결된 후 Braze의 고객 프로필에 이벤트를 기록합니다.

## 전제 조건

| 요구 사항 | 설명 |
|---|---|
| Zendesk 계정 | 이 파트너십을 활용하려면 [Zendesk 관리자 계정](https://`<your-zendesk-instance>`.zendesk.com/agent/admin)이 필요합니다. |
| Zendesk API 토큰 | Braze에서 Zendesk 티켓 엔드포인트로 요청을 보내려면 Zendesk [API 토큰][2]이 필요합니다. |
| 일반 식별자 (권장됨) | Braze와 Zendesk 간의 [공통 식별자](#common-identifier)를 권장합니다. |
| Braze API 키 | Zendesk에서 Braze 엔드포인트로 요청을 보내려면 Braze API 키가 필요합니다. 사용하는 API 키가 Zendesk 웹훅에서 사용하는 Braze 엔드포인트에 대한 올바른 권한을 가지고 있는지 확인합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Braze에서 Zendesk로의 통합

### 1단계: Braze 웹훅 생성

웹훅을 만들려면:

- **캠페인:** Braze 대시보드에서 **캠페인** 페이지로 이동하세요. **캠페인 생성**을 클릭하고 **웹훅**을 선택합니다.
- **캔버스:** 새 캔버스 또는 기존 캔버스의 캔버스 빌더에서 전체 단계 또는 메시지 단계를 생성합니다. 다음으로, **메시지**를 클릭하고 메시지 옵션에서 **웹훅**을 선택합니다.

웹훅에서 다음 필드를 입력합니다:
- **웹훅 URL**: `<your-zendesk-instance>.zendesk.com/api/v2/tickets.json`
- **요청 본문**: 원시 텍스트

추가 사용 사례는 웹훅 URL 끝에 `/api/v2/` 엔드포인트를 적절히 변경하는 [Zendesk 지원 API][4]]를 통해 처리할 수 있습니다.

#### 요청 헤더 및 메서드

Zendesk는 권한 부여를 위해 HTTP 헤더와 HTTP 메서드를 요구합니다. **설정** 탭에서 <email_address>을 Zendesk 관리자 이메일로, <api_token>을 Zendesk API 토큰으로 교체하십시오.

- **HTTP 메서드**: POST
- **요청 헤더**:
  - **권한 부여**: 기본 {% raw %} `{{ '<email_address>/token:<api_token>' | base64_encode }}` {% endraw %}
  - **Content-Type**: application/json

![][3]{: style="max-width:70%;"}

#### 요청 본문

웹훅 페이로드에 유형, 제목 및 상태와 같은 티켓 세부 정보를 정의합니다. 티켓 세부 정보는 [Zendesk 티켓 API][6]]를 기반으로 확장 가능하고 사용자 정의됩니다. 다음 예제를 사용하여 페이로드를 구조화하고 원하는 필드를 입력하십시오.

{% raw %}
```json
{% assign ticket_type = 'question/incident/task/problem' %} << Choose one >>
{% assign ticket_subject = '' %}
{% capture ticket_body %}
<< Your message here >>
{% endcapture %}
{% assign ticket_subject_tag = '' %}
{% assign ticket_status = 'New' %}

{
"ticket": {
"requester_id": "{{${user_id}}}", 
"requester": { "name": "{{${first_name}}} {{${last_name}}}", "email": "{{${email_address}}}", "phone": "{{${phone_number}}}"},
"type": "{{ ticket_type }}",
"subject":  "{{ticket_subject}}",
"comment":  { "body": "{{ticket_body}}" },
"priority": "urgent",
"status": "{{ ticket_status }}"
  }
}
```
{% endraw %}

### 2단계: 요청 미리보기

원시 텍스트가 적용 가능한 Braze 태그인 경우 자동으로 강조 표시됩니다.

**미리보기** 패널에서 요청을 미리 보거나 **테스트** 탭으로 이동하여 무작위 사용자 또는 기존 사용자를 선택하거나 직접 사용자 정의하여 웹훅을 테스트할 수 있습니다.

마지막으로, 티켓이 Zendesk 측에 생성되었는지 확인하십시오.

## 일반 식별자

Braze 및 Zendesk 간에 공통 식별자가 있는 경우 이를 `requester_id`로 활용하는 것이 좋습니다. 이것은 두 사용자 집합을 통합하는 데 도움이 될 것입니다. 또는 이 경우가 아니라면 이름, 이메일 주소, 전화번호 또는 기타 식별 속성 세트를 전달하는 것이 좋습니다.

## Zendesk에서 Braze로의 통합

### 1단계: 웹훅 생성

1. [관리 센터](https://support.zendesk.com/hc/en-us/articles/4581766374554#topic_hfg_dyz_1hb)에서 사이드바의 **앱 및 통합**을 클릭한 다음 **웹훅 > 웹훅**을 선택합니다.<br><br>
2. **웹훅 생성**을 클릭합니다.<br><br>
3. **트리거** 또는 **자동화**를 선택하고 **다음**을 클릭합니다.<br>![][9]{: style="max-width:70%;"}<br><br>
4. 웹훅에 다음 정보를 제공하십시오:
- 웹훅의 이름과 설명을 입력하세요.
- 웹훅에서 사용할 Braze 엔드포인트 URL을 입력하세요. {% raw %}우리의 예는 `https://{{instance_url}}/users/track`.{% endraw %}을 사용할 것입니다
- 웹훅의 요청 메서드로 POST를 선택하고 요청 형식을 JSON으로 설정합니다.
- 웹훅에 대한 베어러 토큰 인증 방법을 선택하고 [Braze API 키]({{site.baseurl}}/api/basics/#creating-and-managing-rest-api-keys)를 제공하십시오.
  - 사용 중인 API 키에 웹훅이 사용하는 Braze 엔드포인트에 대한 [올바른 권한]({{site.baseurl}}/api/basics/#rest-api-key-permissions)이 있는지 확인하세요.<br><br>
5. (권장) 웹훅을 테스트하여 제대로 작동하는지 확인하세요.<br><br>
6. 트리거 및 자동화 웹훅의 경우 설정을 완료하기 전에 웹훅을 트리거 또는 자동화에 연결해야 합니다. 웹훅에 대한 트리거를 만드는 예제는 다음 단계를 참조하세요. 트리거가 생성된 후 이 페이지로 돌아와 **설정 완료를** 선택할 수 있습니다.

### 2단계: 트리거 또는 자동화를 생성

웹훅을 트리거 또는 자동화에 연결하는 방법은 [Zendesk의 지침](https://support.zendesk.com/hc/en-us/articles/4408839108378#topic_bwm_1tv_dpb)을 따르세요.

다음 예제에서는 지원 사례 상태가 '해결됨' 또는 '마감됨'으로 변경될 때 웹훅을 호출하기 위해 트리거를 사용합니다. 

1. **관리 센터**에서 사이드바의 **개체 및 규칙**을 클릭한 다음 **비즈니스 규칙 > 트리거**을 선택합니다.<br><br>
2. **트리거 추가를** 선택합니다.<br><br>
3. 트리거의 이름을 지정하고 카테고리를 선택하세요.<br><br>
4. **조건 추가를** 선택하여 웹훅을 트리거할 조건을 설정합니다. 예를 들어, '상태 범주가 마감됨으로 변경됨' 또는 '상태 범주가 해결됨으로 변경됨'과 같습니다.![][8]{: style="max-width:70%;"}<br><br>
5. **작업 추가를** 선택하고 **활성 웹훅 알림을** 선택한 다음 드롭다운에서 이전 단계에서 만든 웹훅을 선택합니다.<br><br>
6. Braze 엔드포인트에 맞게 JSON 본문을 정의하고, 관련 필드를 동적으로 채우기 위해 Zendesk 변수 자리 표시자를 사용합니다.<br>![][10]{: style="max-width:70%;"}<br><br>
7. **만들기**를 선택합니다.<br><br>
8. 웹훅으로 돌아가서 **설정을 완료**를 클릭하십시오.

[1]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[2]: https://support.zendesk.com/hc/en-us/articles/226022787-Generating-a-new-API-token-\
[3]: {% image_buster /assets/img_archive/zendesk_step1.gif %}
[4]:https://developer.zendesk.com/rest_api/docs/support/introduction
[5]: {% image_buster /assets/img_archive/zendesk_step2.png %}
[6]:https://developer.zendesk.com/rest_api/docs/support/tickets#create-ticket
[7]: {% image_buster /assets/img_archive/zdfinal.gif %}

[8]: {% image_buster /assets/img_archive/zendesk1.png %}
[9]: {% image_buster /assets/img_archive/zendesk2.png %}
[10]: {% image_buster /assets/img_archive/zendesk3.png %}
