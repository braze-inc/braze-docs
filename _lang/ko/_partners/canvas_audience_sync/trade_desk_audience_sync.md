---
nav_title: The Trade Desk
article_title: The Trade Desk로 Canvas 오디언스 동기화
description: "이 참조 문서에서는 The Trade Desk와 Braze 오디언스 동기화를 사용하여 행동 트리거, 세분화 등을 기반으로 광고를 전달하는 방법을 다룹니다."
alias: /trade_desk_audience_sync/
Tool:
  - Canvas
page_order: 7
---

# The Trade Desk로 오디언스 동기화

> Braze 오디언스 동기화를 The Trade Desk와 함께 사용하면 Braze의 퍼스트파티 사용자 데이터를 The Trade Desk로 직접 동적으로 동기화하여 광고 리타겟팅, 유사 모델링 및 제외에 활용할 수 있습니다.

**오디언스 동기화의 일반적인 활용 사례는 다음과 같습니다:**

- The Trade Desk에서 기존 사용자를 개인화된 캠페인으로 리타겟팅합니다.
- 제외 타겟팅을 위해 퍼스트파티 데이터를 The Trade Desk로 전송합니다.
- 사용자를 신규 또는 기존 오디언스 또는 CRM 데이터 세그먼트에 동기화합니다.

## 필수 조건

Canvas에서 The Trade Desk와의 오디언스 동기화 단계를 설정하기 전에 다음 항목이 생성, 완료 또는 수락되었는지 확인하세요.

| 요구 사항 | 출처 | 설명 |
| --- | --- | --- |
| API 토큰 | [The Trade Desk](https://partner.thetradedesk.com/v3/portal/api/doc/Authentication#ui-method-create) | The Trade Desk 플랫폼에서 생성된 표준 API 토큰입니다. The Trade Desk 오디언스 동기화를 사용하는 캔버스의 중단을 최소화하기 위해 API 토큰 수명을 최대 1년으로 설정하는 것을 권장합니다. |
| The Trade Desk 약관 및 정책 | The Trade Desk | The Trade Desk로 데이터를 전송하려면 UID2/CRM 참여 정책에 동의해야 합니다. The Trade Desk 담당자에게 연락하여 The Trade Desk로의 데이터 전달을 활성화하기 위한 적절한 서명이 완료되었는지 확인하세요.<br><br> {::nomarkdown}<ul><li>계정에서 CRM 데이터 관리 액세스가 활성화되어 있는지 확인하세요&#8212;The Trade Desk 담당자가 도움을 줄 수 있습니다. 광고주 ID가 필요합니다.</li><li>표준 API 토큰을 준비하세요. 이 페이지의 안내에 따라 생성할 수 있습니다.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 통합

### 1단계: The Trade Desk 계정 연결

시작하려면 **파트너 통합** > **기술 파트너** > **The Trade Desk**로 이동하세요. Trade Desk 계정에서 다음 세부 정보를 입력합니다:

- **API 토큰**
- **광고주 ID 이름** (이 선택 사항 이름은 오디언스 동기화 캔버스 단계에서 참조할 광고주 계정을 식별합니다)
- **광고주 ID**

그런 다음 **연결**을 선택합니다.

![The Trade Desk에 대한 연결되지 않은 오디언스 동기화의 예시.]({% image_buster /assets/img/audience_sync/trade_desk/connect_sync.png %}){: style="max-width:90%;"}

### 2단계: The Trade Desk와 오디언스 동기화 단계 추가

캔버스에 구성요소를 추가하고 **오디언스 동기화**를 선택합니다. 그런 다음 오디언스 동기화 파트너로 **The Trade Desk**를 선택합니다.

![오디언스 동기화 단계에서 동기화할 파트너를 선택하는 옵션.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step.png %}){: style="max-width:90%;"}

### 3단계: 동기화 설정

다음으로 동기화 세부 정보를 구성합니다:

1. 광고 계정을 선택합니다.
2. 기존 오디언스를 선택하거나 새 오디언스를 생성합니다.

![오디언스 필드에 "valentines2025"라는 이름이 포함된 오디언스 동기화 설정.]({% image_buster /assets/img/audience_sync/trade_desk/choose_audience.png %}){: style="max-width:90%;"}

{: start="3"}
3. **오디언스에 사용자 추가** 또는 **오디언스에서 사용자 제거** 동작을 선택합니다.

![오디언스에 사용자를 추가하는 오디언스 동기화 설정.]({% image_buster /assets/img/audience_sync/trade_desk/audience_sync_step2.png %}){: style="max-width:90%;"}

{: start="4"}
4. 매칭할 필드를 선택합니다: **이메일**, **전화번호** 또는 **모바일 광고주 ID**.

{% alert note %}
EU 지역으로 설정된 The Trade Desk의 오디언스에 동기화하는 경우, The Trade Desk에서 전화번호를 지원하지 않습니다. EU 지역에서의 전화번호 지원에 대해서는 The Trade Desk에 문의하세요.
{% endalert %}

### 4단계: 캔버스 시작

The Trade Desk로의 오디언스 동기화를 구성한 후 캔버스를 시작할 준비가 되었습니다! 새 오디언스가 생성되고, 오디언스 동기화 단계를 통과하는 사용자가 The Trade Desk의 이 오디언스에 전달됩니다. 캔버스에 후속 구성요소가 포함되어 있으면 사용자는 사용자 여정의 다음 단계로 진행합니다.

## 자주 묻는 질문

### The Trade Desk에서 오디언스 크기가 채워지는 데 얼마나 걸리나요?

최대 24시간이 소요될 수 있습니다.

### 광고 계정 내에서 The Trade Desk가 채우는 최소 오디언스 크기는 얼마인가요?

The Trade Desk의 CRM 오디언스에는 최소 오디언스 크기가 없습니다.

### The Trade Desk로 사용자를 전달한 후 사용자가 매칭되었는지 어떻게 알 수 있나요?

The Trade Desk에서 수신된 ID가 세그먼트 옆에 표시됩니다.

- 수신된 ID는 지난 30일 동안 수신한 ID 수입니다.
- 활성 ID는 지난 7일 동안 입찰에서 확인된 ID 수입니다.

### The Trade Desk에서 지원할 수 있는 오디언스 수는 얼마나 되나요?

The Trade Desk에서 지원할 수 있는 오디언스 수에는 제한이 없습니다.