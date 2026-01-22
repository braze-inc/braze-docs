---
nav_title: 데이터 혁신
article_title: 데이터 혁신
page_order: 0.3
layout: dev_guide
guide_top_header: "데이터 혁신"
guide_top_text: "Braze 데이터 트랜스포메이션을 사용하면 웹훅 통합을 구축 및 관리하여 외부 플랫폼에서 Braze로 데이터 흐름을 자동화할 수 있습니다. 이렇게 새롭게 통합된 사용자 데이터는 더욱 정교한 마케팅 사용 사례에 활용될 수 있습니다. Braze 데이터 트랜스포메이션은 코딩 경험이 거의 없더라도 데이터 통합을 신속하게 진행할 수 있으며, 수동 API 호출, 서드파티 통합 도구, 심지어 고객 데이터 플랫폼에 대한 팀의 의존성을 대체할 수 있습니다."
page_type: landing
description: "이 랜딩 페이지에는 데이터 변환을 만드는 방법과 사용 사례 등 Braze 데이터 변환에 관한 문서가 있습니다."
alias: /data_transformation/

guide_featured_title: "섹션 기사"
guide_featured_list:
  - name: 변환 만들기
    link: /docs/user_guide/data/unification/data_transformation/creating_a_transformation/
    image: /assets/img/braze_icons/flip-forward.svg
  - name: 사용 사례
    link: /docs/user_guide/data/unification/data_transformation/use_cases/
    image: /assets/img/braze_icons/users-01.svg
---

## 작동 방식

오늘날의 많은 플랫폼에는 새로운 이벤트나 새로운 데이터에 대한 정보를 한 플랫폼에서 다른 플랫폼으로 전송하는 '웹훅' 또는 실시간 API 알림이 있습니다. 데이터 트랜스포메이션이 제공합니다:

* 이러한 웹훅을 수신할 Braze URL 주소입니다.
* 웹훅 페이로드를 자바스크립트 코드로 변환하여 Braze `/users/track` 또는 `/catalogs` 를 포함한 다양한 Braze API 엔드포인트에 유효한 요청을 생성하는 기능. 예를 들어 `/users/track` 대상의 경우 웹훅에서 어떤 정보를 사용할지, 사용자 속성, 이벤트 또는 구매 등 데이터를 Braze 사용자 프로필에 어떻게 표시할지 선택할 수 있습니다.
* 로깅을 통해 품질 보증을 수행하고, 문제 해결 및 변환의 성능/성과를 모니터링할 수 있습니다.

최종 결과는 웹훅 통합으로, 선택한 소스 플랫폼의 웹훅을 Braze 업데이트로 전환하여 연결할 수 있습니다.

{% details More on webhooks %}
웹훅은 HTTP POST 요청을 통해 특정 대상에게 보내는 실시간 알림입니다. 웹훅은 종종 한 지점에서 다른 지점으로 데이터를 전송하는 데 사용되며, 웹훅은 발생한 작업과 해당 작업에 참여한 사람에 대한 데이터를 전달할 수 있습니다.

예를 들어 설문조사 플랫폼은 온라인 양식에 대한 설문조사 응답이 수신될 때마다 선택한 대상에게 웹훅을 보낼 수 있습니다. 또는 고객 서비스 플랫폼에서 고객 서비스 티켓이 생성될 때마다 원하는 대상에게 웹훅을 보낼 수 있습니다.
{% enddetails %}

## 데이터 혁신 계층

다음 표에서는 무료 버전과 프로 버전의 데이터 트랜스포메이션의 차이점을 설명합니다.

| 영역 | 무료 버전 | 데이터 트랜스포메이션 프로 |
|----|----|----|
| 능동적 변환 | 회사당 최대 5개 | 회사당 최대 55개 |
| 월별 | 월 30만 건의 수신 요청 | 월 10,300,000건의 수신 요청 건수 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
데이터 트랜스포메이션 프로로 업그레이드를 요청하려면, Braze 계정 매니저에게 문의하거나 Braze 대시보드에서 **업그레이드 요청** 버튼을 선택하세요.
{% endalert %}

### 요금 제한

Braze 데이터 변환의 속도 제한은 워크스페이스당 분당 1,000건의 수신 요청입니다. Data Transformation Pro를 사용 중이고 더 높은 요금 한도가 필요한 경우 Braze 계정 매니저에게 문의하세요.

## 자주 묻는 질문

### Braze 데이터 트랜스포메이션과 동기화되는 항목은 무엇인가요?

외부 플랫폼에서 웹훅으로 제공하는 모든 데이터를 Braze에 동기화할 수 있습니다. 외부 플랫폼이 웹훅을 통해 전송하는 것이 많을수록 동기화할 항목을 선택할 수 있는 옵션이 많아집니다.

### 저는 마케터입니다. Braze 데이터 트랜스포메이션을 사용하려면 개발자 리소스가 필요하나요?

개발자분들도 이 기능을 사용해 주시면 좋겠지만, 꼭 개발자가 아니어도 사용할 수 있습니다! 마케터는 개발자 리소스 없이도 성공적으로 전환을 설정할 수 있습니다.

### 외부 플랫폼에서 이메일 주소나 전화번호만 식별자로 제공하는 경우에도 Braze 데이터 트랜스포메이션을 사용할 수 있나요?

예. [이메일 주소 또는 전화번호를 식별자로]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address) 사용하여 `/users/track` 엔드포인트를 업데이트하는 변환을 수행할 수 있습니다.

이는 `external_id` 또는 `braze_id` 대신 `email` 또는 `phone` 을 변환 코드의 식별자 속성으로 사용하면 작동합니다. 예제 [변환 코드는]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/use_cases/#example-transformation-code) 이 기능을 사용합니다.

{% alert note %}
2023년 4월 이전에 시작한 Braze 데이터 트랜스포메이션의 얼리 액세스 사용자는 이 사용 사례에 도움이 된 `get_user_by_email` 기능에 익숙하실 것입니다. 해당 기능은 더 이상 사용되지 않습니다.
{% endalert %}

### Braze 데이터 트랜스포메이션은 데이터 포인트를 기록하나요?

예, 대부분의 경우입니다. Braze 데이터 변환은 결국 원하는 속성, 이벤트 및 구매를 기록하는 `/users/track` 호출을 생성합니다. 이렇게 하면 `/users/track` 호출이 독립적으로 이루어진 것과 동일한 방식으로 데이터 포인트가 기록됩니다. 변환을 작성하는 방식에 따라 기록되는 데이터 포인트 수를 제어할 수 있습니다.

### 사용 사례 설정이나 변환 코드에 대한 도움을 받으려면 어떻게 해야 하나요?

추가 도움이 필요하면 Braze 계정 매니저에게 문의하세요.
