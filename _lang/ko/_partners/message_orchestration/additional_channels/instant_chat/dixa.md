---
nav_title: Dixa
article_title: Dixa
description: "이 문서에서는 Braze와 Dixa의 파트너십에 대해 간략하게 설명합니다."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [딕사는](https://www.dixa.com/) 채팅, 이메일, 전화, 소셜 미디어 등의 커뮤니케이션 채널을 단일 인터페이스로 통합하여 지원 경험을 향상하도록 설계된 고객 서비스 플랫폼입니다. 지능형 라우팅, 자동화, 실시간 성능 인사이트를 통해 기업이 고객 만족도와 효율성을 개선할 수 있도록 지원합니다.

브레이즈와 딕사의 통합은 고객 서비스 상담원에게 실시간 브레이즈 데이터를 제공함으로써 모든 사용자에 대한 더 나은 시각을 제공합니다.

## 필수 조건

시작하기 전에 다음이 필요합니다:

| 전제 조건          | 설명                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 딕사 계정        | 이 파트너십을 이용하려면 딕사 관리자 계정이 필요합니다.                                                                                           |
| Braze REST API 키  | `users.export.ids` 및 `email.status` 권한이 있는 Braze REST API 키.<br><br> 이는 **설정** > **API 키**에서 Braze 대시보드에서 생성할 수 있습니다. |
| Braze REST 엔드포인트 | [REST 엔드포인트 URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). 사용자의 엔드포인트는 인스턴스를 위한 Braze URL에 따라 달라집니다.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
[이전 탐색]({{site.baseurl}}/navigation)을 사용하는 경우 **개발자 콘솔** > **API 설정**에서 API 키를 생성할 수 있습니다.
{% endalert %}

## 사용 사례

이메일, 메신저, 채팅 등 다양한 커뮤니케이션 채널에서 사용자와 소통하면서 고객 서비스 상담원 보기에 Surface Braze 데이터를 표시하세요.

## 통합

딕사 내에서 연동 기능을 구성하려면 딕사 관리자 권한이 있어야 합니다. Braze 연동은 Dixa에서 **설정** > **연동** > **Braze로** 이동합니다.

![][1]{: style="width:450px;"}

### 1단계: Dixa에서 통합 생성

**Braze 위젯 만들기** 페이지에서 다음 필수 필드를 입력하여 연동 기능을 생성합니다:

- **위젯 이름:** 나중에 대화 사이드바에서 제목으로 사용될 통합의 이름입니다.
- **API URL:** 인스턴스에 대한 Braze REST API 엔드포인트 URL입니다.
- **API 키:** 필수 구성 요소에서 생성한 Braze API 키입니다.

### 2단계: 통합 구성

다음으로 Braze와 Dixa 통합을 구성합니다. 다음 옵션 중에서 선택하여 대화 사이드바에서 Braze 위젯의 보기를 조정할 수 있습니다.

#### 대화 사이드바에 위젯 표시

이 설정은 딕사의 대화 사이드바에서 전체 통합 기능을 표시하거나 숨깁니다. 

통합을 적극적으로 구성하는 경우 필수 입력란을 작성하는 동안 이 기능을 해제하는 것이 좋습니다. 구성이 완료되면 다시 켜면 딕사 상담원이 통합 기능을 사용할 수 있습니다.

#### 고객 세부 정보 표시

사용자의 세부 정보를 표시하거나 숨기도록 선택합니다. 세부 정보에는 위치, 이메일, 전화번호, 이메일 구독 상태, 푸시 알림 구독 상태, Braze 회원 가입 기간에 대한 데이터가 포함됩니다. 

#### 이메일 구독 상태를 변경하는 버튼을 표시합니다.

버튼은 Braze의 세 가지 구독 상태 중 하나를 기반으로 합니다: `subscribed`, `opted-in`, `unsubscribed`. 사용자가 `subscribed` 인 경우 상담원은 `opt-in` 또는 `unsubscribe` 으로 선택할 수 있습니다. 사용자가 `opted-in` 또는 `unsubscribed` 인 경우 두 사용자 사이만 전환할 수 있습니다.

#### 사용자 지정 속성 목록 표시

사용자의 사용자 지정 Braze 속성을 표시하거나 숨기도록 선택합니다.

#### 사용자 지정 이벤트 목록 표시

사용자의 사용자 지정 Braze 이벤트를 표시하거나 숨기도록 선택합니다.

#### 구매 목록 표시

사용자가 구매한 제품 목록을 표시하거나 숨기도록 선택합니다. 여기에서 구매 횟수를 확인할 수 있습니다. 첫 구매 날짜와 마지막 구매 날짜를 보려면 항목 위로 마우스를 가져갑니다. 

### 통합 예시

다음은 통합의 예를 보여줍니다:

![사용자의 이메일 구독 상태, 사용자 지정 속성, 사용자 지정 이벤트 및 구매를 표시하는 Braze와 Dixa의 통합 기능입니다.][2]{: style="width:350px;"}

[1]: {% image_buster /assets/img/dixa/dixa-create-integration.png %}
[2]: {% image_buster /assets/img/dixa/dixa-braze-integration.png %}