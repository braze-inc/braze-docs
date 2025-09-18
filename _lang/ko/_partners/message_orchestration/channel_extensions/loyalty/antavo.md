---
nav_title: Antavo
article_title: Antavo Loyalty Cloud
description: "이 참고 문서에서는 구매 보상을 넘어선 차세대 로열티 프로그램인 Braze와 Antavo의 파트너십에 대해 설명합니다."
alias: /partners/antavo/
page_type: partner
search_tag: Partner
---

# Antavo Loyalty Cloud

> [Antavo는](https://antavo.com/) 브랜드 사랑을 촉진하고 고객 행동을 변화시키기 위한 포괄적인 로열티 프로그램을 구축하는 엔터프라이즈급 SaaS 로열티 기술 제공업체입니다.

_이 통합은 Antavo에서 유지 관리합니다._

## 통합 정보

Antavo와 Braze의 통합을 통해 로열티 프로그램 관련 데이터를 사용하여 고객 경험을 향상시키는 개인화된 캠페인을 구축할 수 있습니다. Antavo는 두 플랫폼 간의 로열티 데이터 동기화를 지원하며, 이때 Antavo에서 Braze로의 단방향 데이터 동기화만 수행됩니다. 이 통합은 Antavo가 로열티 회원 ID를 동기화하는 데 사용하는 `external_id` Braze 필드를 지원합니다.

## 전제 조건

| 요구 사항          | 설명                                                                                                                                                                   |
| -------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------  |
| Antavo 계정       | 이 파트너십을 이용하려면 Braze 통합이 활성화된 [Antavo](https://antavo.com/) 계정이 필요합니다.                                                |
| Braze REST API 키   | 다음 권한이 있는 Braze REST API 키입니다: `users.track`, `events.list`, `events.data_series`, `events.get`.<br><br>이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다.  |
| Braze REST 엔드포인트  | [당신의 REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 엔드포인트는 인스턴스의 Braze URL에 따라 달라집니다.                |
| Braze 앱 식별자 | 앱 식별자 키. <br><br>Braze 대시보드에서 이 키를 찾으려면 **설정** > **API 키로** 이동하여 **식별** 섹션을 찾습니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 통합

### 1단계: Antavo에서 Braze 연결

Antavo에서 **모듈** > **Braze로** 이동하여 **구성을** 클릭합니다. Antavo에서 Braze 통합 구성 페이지로 처음 이동하면 인터페이스에서 두 시스템을 연결하라는 프롬프트가 표시됩니다.

다음 자격 증명을 입력합니다:

- **인스턴스 URL:** 프로비저닝된 인스턴스의 Braze REST 엔드포인트.
- **API 토큰(식별자):** Antavo가 Braze에 요청을 보낼 때 사용해야 하는 Braze REST API 키.
- **앱 식별자:** Braze 앱 식별자입니다.

자격 증명을 입력한 후 **연결**을 클릭합니다.

![인스턴스 URL, API 토큰 및 앱 식별자를 사용하여 Antavo에서 Braze 화면을 연결합니다.][1]

### 2단계: 필드 매핑 구성

연결이 설정되면 두 시스템 간의 필드 동기화를 구성하기 위해 Antavo에서 자동으로 **필드 동기화** 페이지로 리디렉션됩니다.   이 페이지는 **모듈** > **Braze를** 통해 언제든지 액세스할 수 있습니다.

Antavo에서 필드 매핑을 구성하려면:

1. **새 필드 추가** <i class="fas fa-plus" alt=""></i> 를 클릭합니다.
2. 드롭다운 필드를 사용하여 Braze와 동기화할 Antavo **로열티 필드**를 선택합니다.
3. 데이터를 채울 Braze의 동등한 커스텀 속성을 나타내는 **원격 필드**를 입력합니다.  

{% alert note %}
사용자 지정 속성 목록은 Braze의 **데이터 설정** > **사용자 지정 속성**에서 찾을 수 있습니다. 입력한 필드가 Braze에 정의되지 않은 경우, 첫 동기화 시 새 필드가 자동으로 생성됩니다.
{% endalert %}

{:start="4"}
4\. 필드 페어링을 추가하려면 1~3단계를 반복합니다.
5\. 동기화된 데이터 목록에서 필드를 제거하려면 행 끝에서 <i class="fa-solid fa-rectangle-xmark" title="삭제"></i>를 클릭합니다.
6\. **저장**을 클릭합니다.

Antavo에서 구성된 필드의 값이 변경되면 해당 단일 값의 동기화가 트리거될 뿐만 아니라 필드 매핑에 추가된 모든 필드가 요청에 포함됩니다.

![Antavo의 필드 동기화 페이지.][2]

{% alert important %}
데이터 포인트 소비를 최소화하려면 Braze 내에서 작업할 필드만 매핑하는 것이 좋습니다.
{% endalert %}

#### 지원되는 데이터 유형

이 통합은 숫자(정수, 플로트), 문자열, 배열, 부울, 오브젝트, 오브젝트 배열, 날짜 등 모든 Braze 커스텀 속성 [데이터 유형]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage)을 지원합니다.

![다양한 커스텀 속성을 보여주는 Braze 프로필.][3]

데이터 필드는 구성된 필드 매핑에 따라 채워집니다.

## 트리거

필드 매핑을 구성하는 것 외에도, 이 통합은 Antavo의 [워크플로](https://antavo.atlassian.net/wiki/spaces/AUM/pages/581402629) 도구에 내장된 기능을 통해 추가 기능을 제공합니다. 모든 Braze 사용자 지정 속성 [데이터 유형]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-storage) 과 사용자 지정 이벤트 속성 [데이터 유형도]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events#expected-format) 워크플로우를 통해 동기화할 수 있습니다.

### 종종 로열티 데이터 동기화

데이터가 Antavo의 로열티 필드에 저장되어 있지 않거나 매핑된 필드 목록에 데이터가 추가되지 않은 경우 이 옵션을 사용합니다. 요청된 데이터의 동기화는 구성된 워크플로 기준이 충족되면 트리거됩니다.

단계별 가이드를 참조하여 [마지막 구매와 관련된 로열티 데이터](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Sync-data-related-to-the-customer%E2%80%99s-last-purchase)의 동기화를 구성하는 방법을 알아보세요.

### 로열티 프로그램 이벤트 동기화

Antavo에서 동기화된 이벤트를 사용하여 실행 기반 Braze 캔버스에 로열티 회원을 입력합니다. 통합을 통해 Braze에 사용자 지정 이벤트로 표시되는 모든 Antavo 이벤트(구매 이벤트 포함)를 동기화할 수 있습니다.

단계별 가이드를 방문하여 [로열티 프로그램 등록 이벤트](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) 동기화 및 [로열티 프로그램 혜택 적립 이벤트](https://antavo.atlassian.net/wiki/spaces/AUM/pages/812056598/Braze#Use-case----Welcome-to-the-loyalty-program!) 동기화를 구성하는 방법을 알아보세요.


[1]: {% image_buster /assets/img/antavo/connect_braze.png %}
[2]: {% image_buster /assets/img/antavo/data_field_mapping.png %}
[3]: {% image_buster /assets/img/antavo/braze_profile.png %}
