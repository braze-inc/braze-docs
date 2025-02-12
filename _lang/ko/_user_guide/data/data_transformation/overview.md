---
nav_title: 개요
article_title: Braze 데이터 혁신 개요
page_order: 0
page_type: reference
alias: /data_transformation/
description: "이 참조 문서에서는 Braze 데이터 변환에 대한 개요, 자주 묻는 질문, 제품 제한 사항을 설명합니다."
---

# Braze 데이터 트랜스포메이션 개요

> Braze 데이터 변환을 사용하면 웹훅 통합을 구축 및 관리하여 외부 플랫폼에서 Braze로 데이터 흐름을 자동화할 수 있습니다. 이렇게 새롭게 통합된 사용자 데이터는 더욱 정교한 마케팅 사용 사례를 뒷받침할 수 있습니다. 브레이즈 데이터 변환은 귀하의 데이터 통합을 가속화할 수 있으며, 코딩 경험이 거의 없더라도 팀의 수동 API 호출, 타사 통합 도구 또는 고객 데이터 플랫폼에 대한 의존성을 대체하는 데 도움을 줄 수 있습니다.

## 작동 방식

오늘날의 많은 플랫폼에는 '웹훅' 또는 실시간 API 알림을 통해 한 플랫폼에서 다른 플랫폼으로 새로운 이벤트나 새로운 데이터에 대한 정보를 전송하는 기능이 있습니다. 데이터 변환 패키지

* 해당 웹훅을 수신할 Braze URL 주소입니다.
* 웹훅 페이로드를 자바스크립트 코드로 변환하여 Braze `/users/track` 또는 `/catalogs`를 포함한 다양한 Braze API 엔드포인트에 유효한 요청을 생성하는 기능. 예를 들어 `/users/track` 대상의 경우 웹훅에서 어떤 정보를 사용할지, 데이터를 사용자 속성, 이벤트 또는 구매로 Braze 고객 프로필에 어떻게 표시할지 선택할 수 있습니다.
* 로깅을 통해 품질 보증을 수행하고, 문제를 해결하고, 변환의 성능을 모니터링합니다.

최종 결과는 웹훅 통합으로, 선택한 소스 플랫폼의 웹훅을 Braze 업데이트로 전환하여 연결합니다.

{% details 웹훅에 대해 자세히 알아보기 %}
웹훅은 HTTP POST 요청을 통해 특정 대상에게 전송되는 실시간 알림입니다. 웹훅은 종종 한 지점에서 다른 지점으로 데이터를 전송하는 데 사용되며, 웹훅은 발생한 작업과 해당 작업에 참여한 사람에 대한 데이터를 전달할 수 있습니다.

예를 들어, 설문조사 플랫폼은 온라인 양식에 대한 설문조사 응답이 수신될 때마다 원하는 대상에게 웹훅을 보낼 수 있습니다. 또는 고객 서비스 플랫폼에서 고객 서비스 티켓이 생성될 때마다 원하는 대상으로 웹훅을 보낼 수 있습니다.
{% enddetails %}

## 데이터 변환 계층

다음 표에서는 무료 버전과 프로 버전의 데이터 변환의 차이점을 설명합니다.

| 영역 | 무료 버전 | 데이터 변환 프로 |
|----|----|----|
| 활성 변환 | 회사당 최대 5개 | 회사당 최대 55개 |
| 월별 | 월 30만 건의 수신 요청 | 월 10,300,000건의 수신 요청 건수 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert important %}
데이터 변환 프로로 업그레이드를 요청하려면 Braze 계정 매니저에게 문의하거나 Braze 대시보드에서 **업그레이드 요청** 버튼을 선택하세요.
{% endalert %}

### 요금 제한

Braze 데이터 변환의 사용량 제한은 분당 1,000건의 수신 요청입니다. 데이터 변환 프로를 사용 중이고 더 높은 사용량 제한이 필요한 경우 Braze 계정 매니저에게 문의하세요.

## 자주 묻는 질문

### Braze 데이터 변환과 동기화되는 항목은 무엇인가요?

외부 플랫폼이 웹훅으로 제공하는 모든 데이터를 Braze에 동기화할 수 있습니다. 외부 플랫폼이 웹훅을 통해 전송하는 것이 많을수록 동기화할 항목을 선택할 수 있는 옵션이 많아집니다.

### 저는 마케터입니다. Braze 데이터 변환을 사용하려면 개발자 리소스가 필요한가요?

개발자도 이 기능을 사용하면 좋겠지만, 꼭 개발자가 아니어도 이 기능을 사용할 수 있습니다! 마케터는 개발자 리소스 없이도 성공적으로 전환을 설정할 수 있습니다.

### 외부 플랫폼에서 이메일 주소나 전화번호만 식별자로 제공하는 경우에도 Braze 데이터 변환을 사용할 수 있나요?

예. [이메일 주소 또는 전화번호를 식별자로]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#example-request-for-updating-a-user-profile-by-email-address) 사용하여 `/users/track` 엔드포인트를 업데이트하도록 변환을 설정할 수 있습니다.

변환 코드에서 `external_id` 또는 `braze_id` 대신 `email` 또는 `phone`을 식별자 속성으로 사용하면 됩니다. 예제 [변환 코드에서는]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/use_cases/#example-transformation-code) 이 기능을 사용합니다.

{% alert note %}
2023년 4월 이전에 Braze 데이터 변환을 시작한 얼리 액세스 사용자는 이 사용 사례에 도움이 되는 `get_user_by_email` 기능에 익숙하실 것입니다. 해당 기능은 더 이상 사용되지 않습니다.
{% endalert %}

### Braze 데이터 트랜스포메이션은 데이터 포인트를 소비하나요?

대부분의 경우 그렇습니다. Braze 데이터 변환은 결국 원하는 속성, 이벤트 및 구매를 기록하는 `/users/track` 호출을 생성합니다. 이는 `/users/track` 호출이 독립적으로 이루어진 것과 동일한 방식으로 데이터 포인트를 소비합니다. 변환을 작성하는 방식에 따라 얼마나 많은 데이터 포인트를 작성할지 제어할 수 있습니다.

### 사용 사례 설정이나 변환 코드에 대한 도움을 받으려면 어떻게 해야 하나요?

추가 지원이 필요하면 Braze 계정 관리자에게 문의하세요.


[1]: {% image_buster /assets/img_archive/data_transformation1.png %}
[2]: {% image_buster /assets/img/data_transformation/data_transformation1.jpg %}
