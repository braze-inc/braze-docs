---
nav_title: Adikteev
article_title: Adikteev 고객이탈 예측
description: "이 참조 문서에서는 Braze와 Adikteev 간의 파트너십을 간략히 설명합니다. Adikteev는 고객이탈 예측과 풀 서비스 앱 리타겟팅을 결합한 사용자 유지 엔진입니다."
alias: /partners/adikteev/
page_type: partner
search_tag: Partner

---

# Adikteev 고객이탈 예측

> [Adikteev](https://www.adikteev.com/churn-prediction)는 고객이탈 예측과 풀 서비스 앱 리타겟팅을 결합한 사용자 유지 엔진입니다.

Braze와 Adikteev 통합을 통해 Adikteev의 고객이탈 예측 기술을 Braze CRM 캠페인 내에서 활용하여 우선적으로 고위험 사용자 세그먼트를 타겟팅함으로써 사용자 유지율을 높일 수 있습니다.

## 필수 조건

| 요구 사항 | 설명 |
| --- | --- |
| Adikteev 계정 | Adikteev 계정이 있어야 이 파트너십을 활용할 수 있습니다. |
| Braze REST API 키 | 권한 `users.track`이(가) 있는 Braze REST API 키. <br><br> 이는 **설정** > **API 및 식별자**의 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [당신의 REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 사용 사례

{% tabs %}
{% tab 오디언스 필터링 %}
고객이탈 위험에 따른 오디언스 세그먼트의 정제.<br> Adikteev에서 전송한 커스텀 속성의 이름과 값은 구성 가능합니다.

![Adikteev에서 보낸 커스텀 속성을 오디언스 세그먼트 필터로 사용하는 예제를 보여주는 스크린샷.]({% image_buster /assets/img/adikteev/audience.png %})
{% endtab %}
{% tab 메시지 타겟팅 %}
수신자의 고객이탈 위험에 따라 Braze 메시징 캠페인을 맞춤화합니다.

![Adikteev에서 캠페인 타겟팅 필터로 보낸 커스텀 속성을 사용하는 예제를 보여주는 스크린샷.]({% image_buster /assets/img/adikteev/campaign.png %})
{% endtab %}
{% endtabs %}

## 통합

### 1단계: 앱의 이벤트 스트림 공유

앱 오디언스에서 고객이탈 예측 실행을 시작하려면 Adikteev는 모바일 측정 플랫폼에서 이벤트 포스트백을 활성화해야 합니다. 이 기능을 설정하려면 [Adikteev 지원 웹사이트](https://help.adikteev.com/hc/en-us/sections/8185123408914-Data-stream-activation)의 지침을 따르세요.

### 2단계: Braze REST API 키를 생성하세요

Braze에서 **설정** > **API 및 식별자**로 이동합니다. **Create New API Key**을 선택하고 원하는 API 키 이름을 입력한 다음 다음 권한이 추가되었는지 확인하십시오:

- `users.track`

### 3단계: Adikteev 팀에 정보 제공

통합을 완료하려면 Adikteev 계정 매니저에게 REST API 키와 REST 엔드포인트 URL을 제공해야 합니다. Adikteev는 연결을 설정하고 설정이 완료된 후 연락하여 통합의 유효성을 검증합니다.

## 배치 처리 및 사용량 제한

`user.track` 엔드포인트는 사용자에 대한 세부 정보를 업데이트하는 데 사용됩니다. 엔드포인트의 사용량 제한, 배치 처리 요청 및 요청 세부 정보에 대한 전체 세부 정보는 [API 설명서]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)를 참조하세요.

{% alert tip %}
API 호출은 전체 API 호출 수를 줄이기 위해 변경된 데이터만 업데이트하도록 수행해야 합니다. 즉, 고객이탈 세그먼트가 변경된 사용자만 업데이트합니다.
{% endalert %}

## 사용자 및 기기 식별자

Braze의 고객 프로필은 모든 유형의 사용자 또는 기기 식별자와 연결될 수 있습니다. 사용 가능한 옵션 목록은 Braze와 데이터 수집을 통합한 방법에 따라 다릅니다. Adikteev의 경우 고객이탈 세그먼트 정보를 올바르게 전송하려면 MMP와 Braze의 고객 프로필 간에 공통 식별자를 찾아야 합니다.

## 데이터 보존 및 삭제

업데이트가 없으면 속성과 해당 값은 Braze 고객 프로필에 무기한으로 유지됩니다.

프로필 속성을 제거하려면 `null`으로 설정하십시오.

## 요청 페이로드

Adikteev에서 Braze로 전송된 페이로드는 사용자 지정 가능하며 고객의 요구에 맞게 구성할 수 있습니다. 여기에는 사용되는 식별자 구성, 커스텀 속성의 이름, Adikteev가 Braze에서 새로운 사용자를 생성할 수 있는지 아니면 기존 사용자를 업데이트할 수 있는지 여부가 포함됩니다.


## 지원 및 문제 해결

통합 또는 사용 사례에 대한 지원이 필요한 경우 Adikteev 계정 매니저에게 문의하세요.
