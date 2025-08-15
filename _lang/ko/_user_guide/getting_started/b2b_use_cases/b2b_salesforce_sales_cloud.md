---
nav_title: Salesforce Sales Cloud
article_title: Salesforce Sales Cloud로 리드 관리
page_order: 3
page_type: reference
description: "Braze 웹훅을 사용하여 Salesforce 개체/리드 엔드포인트를 통해 Salesforce Sales Cloud에서 리드를 생성하고 업데이트하는 방법을 알아보세요."
---

# Salesforce Sales Cloud로 리드 관리

> [Salesforce는](https://www.salesforce.com/) 기업이 리드 생성, 기회 추적, 계정 관리 등 전체 영업 프로세스를 관리할 수 있도록 설계된 세계 최고의 클라우드 기반 고객 관계 관리(CRM) 플랫폼 중 하나입니다.<br><br>이 페이지에서는 커뮤니티에서 제출한 통합을 통해 Braze 웹훅을 사용하여 Salesforce Sales Cloud에서 리드를 생성하고 업데이트하는 방법을 보여줍니다.

{% alert important %}
이 기능은 커뮤니티에서 제출한 통합 기능이며 Braze에서 직접 지원하지 않습니다. Braze에서 제공하는 공식 웹훅 템플릿만 지원됩니다.
{% endalert %}

## 작동 방식

Braze와 Salesforce Sales Cloud 통합은 Braze 웹훅을 사용하여 Salesforce [개체/리드](https://developer.salesforce.com/docs/atlas.en-us.object_reference.meta/object_reference/sforce_api_objects_lead.html) 엔드포인트를 통해 Salesforce Sales Cloud에서 리드를 생성하고 업데이트합니다.

Braze는 현재 다음과 같은 사용 사례를 위한 두 가지 통합 기능을 Salesforce Sales Cloud에 제공합니다:
1. [Salesforce Sales Cloud에서 리드 만들기](#creating-lead)
2. [Salesforce Sales Cloud에서 리드 업데이트하기](#updating-lead)

{% alert note %}
이 통합은 순전히 리드 확보 및 육성 노력의 일환으로 Braze에서 Salesforce를 업데이트하기 위한 것입니다. Salesforce에서 Braze로 데이터를 다시 동기화하려면 [B2B 데이터 모델을]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models/) 확인하거나 [기술 파트너]({{site.baseurl}}/partners/home/) 중 한 곳에 문의하세요.
{% endalert %}

## 필수 조건

이 통합을 사용하려면 Salesforce 문서에 나와 있는 단계에 따라 Salesforce Sales Cloud에서 연결된 앱을 만들어야 합니다: [OAuth 2.0 클라이언트 자격 증명 흐름에 대해 연결된 앱을 구성합니다](https://help.salesforce.com/s/articleView?id=sf.connected_app_client_credentials_setup.htm&type=5).

연결된 앱에 필요한 OAuth 설정을 구성할 때 다음을 제외한 모든 oAuth 설정을 기본값과 선택 항목으로 유지합니다:
1. **장치 흐름에 사용을** 선택합니다. **콜백 URL은** 기본적으로 자리 표시자로 사용되므로 비워 둘 수 있습니다.
2. 선택한 **OAuth 범위에** 대해 API를 **통한 사용자 데이터 관리(api)를** 추가합니다.
3. **클라이언트 자격 증명 흐름 사용을** 선택합니다.

## Salesforce Sales Cloud에서 리드 만들기 {#creating-lead}

고객 참여 플랫폼인 Braze는 랜딩 페이지에서 양식을 작성하는 등의 사용자 흐름을 기반으로 새로운 리드를 생성할 수 있습니다. 이 경우 Braze Salesforce Sales Cloud 웹훅을 사용하여 Salesforce에서 해당 리드를 생성할 수 있습니다.

### 1단계: `client_id` 및 `client_secret`

1. Salesforce에서 **플랫폼 도구** > **앱** > **앱 관리자로** 이동합니다.
2. 새로 생성한 Braze 앱을 찾아 **보기를** 선택합니다.
3. **소비자 키 및 비밀번호** 아래에서 **소비자 세부 정보 관리를** 선택합니다.
4. 결과 페이지에서 **소비자 키와** **소비자 비밀** 번호를 기록합니다. **소비자 키는** `client_id`, **소비자 비밀은** `client_secret` 입니다.

### 2단계: 웹훅 템플릿을 설정하세요

템플릿을 사용하여 Braze 플랫폼에서 이 웹훅을 빠르게 재사용할 수 있습니다. 

1. Braze에서 **템플릿으로** 이동하여 **웹훅 템플릿을** 선택한 다음 **\+ 웹훅 템플릿 만들기를** 선택합니다.
2. 템플릿의 이름(예: "Salesforce Sales Cloud > 리드 만들기")을 입력합니다.
3. **작성** 탭에서 다음 세부 정보를 입력합니다:

#### 웹훅 작성 

| 필드 | 세부 정보 |
| --- | --- |
| 웹훅 URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/`{% endraw %} |
| HTTP 메서드 | `POST` |
| 요청 본문 | JSON 키/값 쌍 |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### 본문 속성 키 값

Braze에서 Salesforce로 매핑하려는 각 키/값 쌍에 대해 **\+ 새 본문 속성 추가를** 선택합니다. 원하는 모든 필드에 매핑할 수 있으므로 다음 표는 한 가지 예일 뿐입니다.

| 키 | 값 |
| --- | --- |
| 이름 | {% raw %}`{{${first_name}}}`{% endraw %} |
| 성 | {% raw %}`{{${last_name}}}`{% endraw %} |
| 이메일 | {% raw %}`{{${email_address}}}`{% endraw %} |
| 회사 | {% raw %}`{{custom_attribute.${company}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### 요청 헤더

다음 요청 헤더 각각에 대해 **\+ 새 헤더 추가를** 선택합니다.

| 키 | 값 |
| --- | --- |
| 승인 | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| 콘텐츠-유형 | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4" }
4\. **템플릿 저장을** 선택합니다.

![리드를 생성하기 위해 작성된 웹훅 템플릿입니다.][6]{: style="max-width:70%;"}
 
## Salesforce Sales Cloud에서 리드 업데이트하기 {#updating-lead}

세일즈포스에서 리드를 업데이트하는 Braze 세일즈포스 세일즈 클라우드 웹훅을 설정하려면 세일즈포스 세일즈 클라우드와 브레이즈 간의 공통 식별자가 필요합니다. 아래 예제에서는 Salesforce `lead_id` 를 Braze `external_id` 로 사용하지만 `user_alias` 를 사용하여 이 작업을 수행할 수도 있습니다. 이에 대한 자세한 내용은 [B2B 데이터를]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_data_models) 참조하세요.

이 예에서는 리드가 특정 리드 임계값을 넘은 후 리드의 리드 단계를 'MQL(마케팅 적격 리드)'로 업데이트하는 방법을 구체적으로 보여 줍니다. 이는 [B2B 리드 스코어링 워크플로]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/) 사용 사례의 핵심 부분입니다.

### 1단계: `client_id` 및 `client_secret`

1. Salesforce에서 **플랫폼 도구** > **앱** > **앱 관리자로** 이동합니다.
2. 새로 생성한 Braze 앱을 찾아 **보기를** 선택합니다.
3. **소비자 키 및 비밀번호** 아래에서 **소비자 세부 정보 관리를** 선택합니다.
4. 결과 페이지에서 **소비자 키와** **소비자 비밀** 번호를 기록합니다.
    - **소비자 키는** `client_id`, **소비자 비밀은** `client_secret` 입니다.

### 2단계: 웹훅 템플릿을 설정하세요

1. Braze에서 **템플릿으로** 이동하여 **웹훅 템플릿을** 선택한 다음 **\+ 웹훅 템플릿 만들기를** 선택합니다.
2. 템플릿의 이름(예: "Salesforce Sales Cloud > 리드를 MQL로 업데이트")을 입력합니다.
3. **작성** 탭에서 다음 세부 정보를 입력합니다:

#### 웹훅 작성 

| 필드 | 세부 정보 |
| --- | --- |
|웹훅 URL | {% raw %}`https://[insert_instance_name].my.salesforce.com/services/data/v60.0/sobjects/Lead/{{${user_id}}}`{% endraw %} |
| HTTP 메서드 | `PATCH` |
| 요청 본문 | JSON 키/값 쌍 |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### 본문 속성 키 값

다음 키/값 쌍에 대해 **\+ 새 본문 속성 추가를** 선택합니다. `Lead_Stage__c` 은 예시 이름입니다. Salesforce에서 MQL을 추적하는 데 사용하는 사용자 지정 필드의 이름이 다를 수 있으므로 이름이 일치하는지 확인하세요.

| 키 | 값 |
| --- | --- |
| `Lead_Stage__c` | `MQL` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

#### 요청 헤더

다음 요청 헤더 각각에 대해 **\+ 새 헤더 추가를** 선택합니다.

| 키 | 값 |
| --- | --- |
| 승인 | {% raw %}`{% connected_content https://[insert_instance_name].my.salesforce.com/services/oauth2/token     :method post     :body client_id=[insert_client_id]&client_secret=[insert_client_secret]&grant_type=client_credentials     :save result %}Bearer {{result.access_token}}`{% endraw %} |
| 콘텐츠-유형 | `application/json` |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

{: start="4"}
4\. **템플릿 저장을** 선택합니다.

![리드를 업데이트하기 위해 작성된 웹훅 템플릿입니다.][7]{: style="max-width:70%;"}

## 운영 워크플로우에서 이러한 웹훅 사용

다음과 같이 Braze의 운영 워크플로에 템플릿을 빠르게 추가할 수 있습니다:

1. Salesforce에서 리드를 생성하는 [신규 사용자 캠페인의](#new-lead) 일부입니다.
2. MQL 임계값을 넘은 사용자를 "MQL"로 업데이트하고 동일한 정보로 Salesforce Sales Cloud를 업데이트하는 [리드 스코어링 캔버스의](#lead-scoring) 일부입니다.

### 새로운 리드 캠페인 {#new-lead}

사용자가 이메일 주소를 제공할 때 Salesforce에서 리드를 생성하려면 '리드 업데이트' 웹훅 템플릿을 사용하여 사용자가 이메일 주소를 추가할 때(예: 웹 양식 작성) 트리거되는 캠페인을 만들 수 있습니다.

![액션 기반이며 트리거 액션이 '이메일 주소 추가'인 캠페인을 만드는 2단계입니다.][1]{: style="max-width:70%;"}

### MQL(마케팅 적격 리드) 임계값을 넘기 위한 리드 스코어링 캔버스 {#lead-scoring}

이 웹후크는 [리드 스코어링]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/lead_scoring/#lead-handoff) 사용 사례에서 다루고 있지만, 별도의 웹후크 캠페인을 만드는 대신 리드 스코어링 캔버스 내에서 MQL을 확인하고 Salesforce를 직접 업데이트할 수도 있습니다(별도의 웹후크 캠페인을 만들지 않고): 

사용자 업데이트에 후속 단계를 추가하여 사용자가 정의한 MQL 임계값을 넘었는지 확인하세요. 교차된 경우 사용자의 상태를 "MQL"로 업데이트한 다음 이 웹훅 템플릿을 사용하여 동일한 "MQL" 상태로 Salesforce를 업데이트하세요. Salesforce는 정의된 리드 라우팅 규칙에 따라 이 리드를 적절한 영업 팀으로 라우팅하여 나머지 작업을 처리합니다.  

#### 캔버스 단계를 추가하여 MQL 임계값을 통과한 사용자를 확인합니다. 

1. 두 그룹으로 **대상 경로** 단계를 추가합니다: "MQL 임계값" 및 "기타 모든 사용자".
2. 'MQL 임계값' 그룹에서 현재 'MQL' 상태(예: `lead_stage` = '리드')는 아니지만 리드 점수가 정의한 임계값(예: `lead_score` = 50 이상)을 초과하는 사용자를 찾습니다. 그렇다면 다음 단계로 이동하고, 그렇지 않으면 종료합니다.

![`lead_stage` 은 "리드"와 같고 `lead_score` 은 "50"보다 큰 필터가 있는 "MQL 임계값" 대상 경로 그룹입니다.][2]{: style="max-width:70%;"}

{: start="3" }
3\. 사용자의 `lead_stage` 속성 값을 "MQL"로 업데이트하는 **사용자 업데이트** 단계를 추가합니다.

![`lead_stage` 속성이 "MQL" 값을 갖도록 업데이트하는 "MQL로 업데이트" 사용자 업데이트 단계입니다.][3]{: style="max-width:70%;"}

{: start="4" }
4\. 새 MQL 단계로 Salesforce를 업데이트하는 웹후크 단계를 추가합니다.

![완료된 세부 정보가 포함된 'Salesforce 업데이트' 웹훅 단계입니다.][4]{: style="max-width:70%;"}

이제 캔버스 흐름이 MQL 임계값을 넘은 사용자를 업데이트합니다!

![사용자가 MQL 임계값을 통과하는지 확인하고, 통과할 경우 Salesforce를 업데이트하는 Canvas 사용자 업데이트 단계입니다.][5]{: style="max-width:50%;"}

## 문제 해결

이러한 워크플로에는 Salesforce 내에서 디버깅 기능이 제한되어 있으므로 Braze [메시지 활동 로그를]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab#message-activity-log) 참조하여 웹훅이 실패한 이유와 오류가 발생했는지 확인하는 것이 좋습니다.

예를 들어, oAuth 토큰 검색에 사용된 잘못된 URL로 인해 발생한 오류는 `https://[insert_instance_name].my.salesforce.com/services/oauth2/token is not a valid URL` 로 표시됩니다.

![URL이 유효한 URL이 아님을 나타내는 오류 응답 본문입니다.][8]

[1]: {% image_buster /assets/img/b2b/salesforce_create_campaign.png %}
[2]: {% image_buster /assets/img/b2b/salesforce_check_mql.png %}
[3]: {% image_buster /assets/img/b2b/salesforce_update_mql.png %}
[4]: {% image_buster /assets/img/b2b/salesforce_webhook.png %}
[5]: {% image_buster /assets/img/b2b/salesforce_canvas.png %}
[6]: {% image_buster /assets/img/b2b/create_lead_webhook.png %}
[7]: {% image_buster /assets/img/b2b/update_lead_webhook.png %}
[8]: {% image_buster /assets/img/b2b/error_message_invalid_url.png %}