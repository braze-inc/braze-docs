---
nav_title: SalesWings
article_title: SalesWings
description: "이 참조 문서에서는 점수 및 등급, 영업 인사이트 및 알림, 마케팅 조정, B2B 어트리뷰션 보고를 추적하는 데 도움이 되는 분석 플랫폼인 Braze와 SalesWings의 파트너십에 대해 설명합니다."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings][1]는 마케팅 및 영업 팀을 위해 빌드된 B2B SaaS 리드 프로파일링 추가 기능으로, 긴밀한 Salesforce CRM 통합과 함께 리드 점수 및 등급 지정, 영업 인사이트 및 알림, 마케팅 조정, B2B 기여도 보고 기능을 사용하여 리드 및 계정 자격을 관리할 수 있도록 지원합니다.

_This integration is maintained by SalesWings._

## 통합 정보

SalesWings를 사용하면 마케팅 팀과 마케팅 운영 관리자가 영업팀의 리드와 계정을 검증할 수 있어 영업과 마케팅의 연계 및 효율성에 필수적입니다. 또한 SalesWings는 Braze와 함께 리드의 고객 여정과 Braze 마케팅 캠페인 인게이지먼트 데이터를 영업 담당자에게 제시할 수 있으므로 보다 교육적인 대화를 통해 리드 자격 비율을 높일 수 있습니다.

## 전제 조건
 
| 요구 사항 | 설명 |
| ----------- | ----------- |
| SalesWings 계정 | 이 파트너십을 이용하려면 [SalesWings][1] 계정이 필요합니다. |
| Braze REST API 키 | `users.export.ids` 권한이 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL][2]. 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다. |
| Segment.com 계정(선택 사항) | Segment.com 사용자라면 리드 프로파일링을 위해 Segment.com 을 통해 모든 리드 참여 및 프로필 데이터를 전송하고 이벤트를 식별할 수 있습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

{% tabs %}
{% tab 리드 점수 %}

SalesWings는 [최신 리드 점수 지정](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs) 및 리드 등급 지정 기능을 통해 Braze 고객에게 리드, 담당자 및 계정을 검증할 수 있는 유연한 방법을 제공합니다. 모든 리드 자격 데이터는 기본적으로 리드, 담당자, 계정 및 기회에서 관리하고 보고하려는 Salesforce CRM 및 기타 시스템으로 푸시됩니다.

![SalesWings의 간단한 코드 없는 클릭 기반 리드 스코어링 모델 예시]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_SalesWings의 간단한 코드 없는 클릭 기반 리드 스코어링 모델 예시_
{% endtab %}
{% tab 영업 및 마케팅 조정 %}
SalesWings를 사용하면 마케팅 팀이 마케팅 적격 리드를 추적하고 자격을 검증하며 영업 팀에 인계할 수 있습니다. 모든 SalesWings 데이터는 기본적으로 Salesforce에 푸시되며, 이를 활용하여 기존 프로세스를 미세 조정하거나 목록, 보고서, 흐름 등을 통해 새로운 프로세스를 생성할 수 있습니다.

![Salesforce 내에서 기본적으로 리드 또는 담당자 목록의 우선순위를 정하는 SalesWings 리드 점수 지정 기능 예제]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Salesforce 내에서 기본적으로 리드 또는 담당자 목록의 우선순위를 정하는 SalesWings 리드 점수 지정 기능 예제_

![Salesforce 내에서 기본적으로 계정 목록의 우선순위를 정하는 SalesWings 리드 점수 지정 기능 예제]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Salesforce 내에서 기본적으로 계정 목록의 우선순위를 정하는 SalesWings 리드 점수 지정 기능 예제_
{% endtab %}
{% tab 리드 및 계정 등급 %}
SalesWings를 통해 Braze 고객은 프로필 데이터(일반적으로 CRM 데이터)를 기반으로 리드와 계정의 자격을 검증할 수 있습니다. 이를 '리드 등급 지정', '적합도 점수 지정' 또는 '퍼모그래픽 점수 지정'이라고도 합니다. Braze 고객은 속성 데이터를 SalesWings로 직접 전송할 수 있으며, SalesWings는 모든 Salesforce CRM 표준 또는 사용자 지정 개체 데이터와 기록을 읽어 전체적인 프로필 스코어링을 수행할 수 있습니다.
{% endtab %}
{% tab 영업 담당자를 위한 영업 인사이트 %}
SalesWings를 사용하면 영업 담당자에게 리드, 담당자 및 계정에 대한 영업 인사이트를 표시할 수 있습니다(Marketo Sales Insights 대체 기능). 기본적으로 영업 팀에 모든 Braze 및 웹 인게이지먼트 데이터를 제시할 수 있습니다. 인사이트는 기본적으로 Salesforce CRM에 포함되어 있으며, 다른 CRM이나 시스템으로 푸시하거나 Braze 이메일을 통해 '영업 알림'으로 전송할 수 있습니다.

![Salesforce 내 영업 담당자를 위한 영업 인사이트 보기 예제(다른 CRM 시스템에서도 사용 가능)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Salesforce 내 영업 담당자를 위한 영업 인사이트 보기 예제(다른 CRM 시스템에서도 사용 가능)_
{% endtab %}
{% tab 판매 알림 %}
SalesWings는 기본 이메일 및 Slack 알림을 제공하며, 영업팀이 액세스하여 일일, 주간 및 월간 이메일 보고서를 받을 수 있도록 Salesforce에서 보고서 구독을 설정할 수 있습니다. 또한 Zapier 통합을 통해 SalesWings 리드 자격 데이터를 기반으로 추가 워크플로를 빌드할 수 있습니다.

![Slack 채널을 통한 판매 알림 예시]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Slack 채널을 통한 판매 알림 예시_
{% endtab %}
{% tab Salesforce CRM에서 보고 %}
SalesWings와 Salesforce의 통합을 통해 웹 인게이지먼트 데이터 및 Braze 캠페인 인게이지먼트를 기반으로 리드, 담당자, 계정, 기회에 대한 자동화된 보고 기능을 빌드할 수 있습니다. 예를 들어, 특정 이메일 캠페인을 클릭하거나 앱 또는 웹사이트에서 특정 작업을 수행한 모든 사람의 핫 리드 목록을 영업팀에 표시할 수 있습니다.

![Braze 캠페인이 영업 결과 및 성과에 미치는 영향을 살펴보는 Salesforce 내 Braze 이메일 및 마케팅 인게이지먼트에 연결된 대시보드 예제]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Braze 캠페인이 영업 결과 및 성과에 미치는 영향을 살펴보는 Salesforce 내 Braze 이메일 및 마케팅 참여에 연결된 대시보드의 예시입니다._
{% endtab %}
{% endtabs %}

## 통합

### 1단계: SalesWings 계정 및 구성

친절한 SalesWings 팀과 [데모를 예약하여][4] SalesWings에 대해 자세히 알아보세요.

### 2단계: 웹사이트 또는 앱에 행동 추적 설치하기

현재 SalesWings에서 리드 점수 지정 및 영업 인사이트를 위해 행동 데이터를 수집하는 두 가지 방법이 있습니다.
* 리드를 추적하고 식별하려는 웹사이트 및 앱에 [SalesWings 추적 JavaScript를 배포합니다][5].
* Segment.com과 SalesWings 통합을 통해 행동 리드 활동 데이터 및 리드 프로필 데이터를 전송

### 3단계: SalesWings와 Braze 연결

[**SalesWings 설정** 페이지로][6] 이동하여 **Braze 통합** 섹션을 확장합니다.

![SalesWings 설정 페이지의 Braze 통합 섹션입니다.][7]

새로 생성된 키의 **식별자** 열 값을 복사하여 SalesWings **Braze 통합** 섹션의 **Braze API 키** 필드에 붙여넣습니다.

[API 및 SDK 엔드포인트 문서][8]에 설명된 대로 Braze API 엔드포인트를 추가하고 **Braze API 엔드포인트** 필드에 입력합니다. **REST 엔드포인트** 열의 값을 복사하여 SalesWings **Braze 통합** 섹션의 **Braze API 엔드포인트** 필드에 입력합니다.

그런 다음, SalesWings 설정에서 **변경 사항 저장**을 클릭합니다.

### 4단계: Braze, CRM 통합 등을 위한 SalesWings 리드 스코어링 구성하기

[웹사이트][1]를 통해 전체 온보딩 지원을 받으려면 SalesWings 서비스 팀에 문의하세요.

## 이 통합 사용 

리드 점수 지정을 트리거하고 영업 인사이트를 생성하려면 SalesWings가 웹사이트 또는 앱에서 사용자를 식별해야 합니다. 이는 다음과 같은 방식으로 발생할 수 있습니다:

- **양식 제출:** 사용자가 웹 양식을 제출하면 SalesWings는 모든 웹 양식 유형(로그인, 다운로드, 문의 등)을 자동으로 식별하고 사용자가 양식을 제출할 때 사용자의 ID를 확인합니다. 
- **Braze ID 또는 외부 ID로 URL을 클릭합니다:** 사용자가 일반적으로 이메일 클릭, 배너 클릭 등의 Braze 마케팅 작업을 클릭하면 SalesWings로 추적하는 페이지로 연결됩니다.
- **Gmail 및 Outlook 플러그인을 통한 영업 이메일 추적(선택 사항):** 이메일 추적 플러그인을 통해 영업 담당자에게 권한을 부여하기로 결정한 경우 추적 가능한 링크를 전송하여 사용자의 전체 웹사이트 추적을 트리거할 수 있습니다.
- **Segment.com 이벤트 식별(선택 사항):** Segment.com 사용자라면 Segment.com 통합을 통해 사용자의 ID를 확인할 수도 있습니다.

### URL 클릭을 통한 사용자 식별

추적 가능한 URL(예: 이메일 폭발, URL이 포함된 배너)을 클릭하면 사용자를 자동으로 식별할 수 있습니다. URL을 추적 가능하게 만들려면 링크 끝에 매개변수와 ID를 추가하여 이메일, 배너 또는 SMS에서 웹사이트 URL을 수정하는 두 가지 방법이 있습니다.

1. `?braze_id=` 뒤에 {% raw %}`{{${braze_id}}}`{% endraw %} 추가 
  - **링크 예제:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. `?br_user_id=` 뒤에 {% raw %}`{{${user_id}}}`{% endraw %} 추가
  - **링크 예제:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

`braze_id` 변수는 Braze에서 생성한 사용자 식별자로 설정되며 항상 사용할 수 있습니다. `br_user_id` 변수는 시스템에서 사용자의 식별자로 설정되며 특정 시나리오에서는 누락될 수 있습니다(예: Braze SDK에서 생성한 익명 사용자의 경우). 링크에 `braze_id` 및 `br_user_id`를 모두 사용하는 경우 SalesWings는 `braze_id` 매개변수만 고려합니다.

구성 및 추가 문제 해결에 대한 자세한 내용은 [SalesWings 서비스 팀에][1] 문의하여 온보딩 지원을 받으십시오.


[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[5]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[6]: https://helium.saleswings.pro/settings
[7]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[8]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
