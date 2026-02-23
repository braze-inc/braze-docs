---
nav_title: Splio
article_title: Splio
alias: /partners/splio/
description: "이 참조 기사는 Braze와 Splio 간의 파트너십을 설명하며, 이를 통해 보다 타겟팅된 캠페인을 전송하고, 새로운 제품 기회를 찾고, 매출을 높일 수 있습니다."
page_type: partner
search_tag: Partner

---

# Splio

> [Splio](https://splio.com/)는 고객 경험을 해치지 않으면서 캠페인 수와 매출을 증가시킬 수 있는 오디언스 구축 도구이며, 온라인 및 오프라인 CRM 캠페인의 성과를 추적할 수 있는 분석을 제공합니다.

Braze와 Splio 통합을 통해 더 나은 CRM 전략을 계획하고 실행하며, 보다 타겟팅된 캠페인을 전송하고, 새로운 제품 기회를 찾고, 매출을 높일 수 있습니다.

## 필수 조건

| Requirement | 설명 |
|---|---|
| Splio 계정 | 이 파트너십을 위해서는 Splio 계정이 필요합니다. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Data import integration

Braze와 Splio를 통합하려면 Splio 플랫폼을 구성하고, 기존 Splio 캠페인을 내보내며, 향후 캠페인에서 사용자를 타겟팅하기 위해 Braze에서 코호트 세그먼트를 생성해야 합니다.

### 1단계: Get the Braze data import key

Braze에서 **Partner Integrations** > **Technology Partners**로 이동하여 **Splio**를 선택합니다.

REST 엔드포인트를 찾고 Braze 데이터 가져오기 키를 생성합니다. 키를 생성한 후, 새 키를 만들거나 기존 키를 무효화할 수 있습니다.<br><br>![REST 엔드포인트와 데이터 가져오기 키가 포함된 Splio 기술 파트너 페이지입니다.]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"}

통합을 완료하려면 데이터 가져오기 키와 REST 엔드포인트를 Splio 데이터 운영 팀에 제공해야 합니다. Splio는 연결을 설정하고 설정이 완료된 후에 연락을 드립니다.

### 2단계: Splio 플랫폼에서 캠페인을 내보냅니다.

Braze에서 Splio 사용자 코호트를 생성하려면 매번 먼저 Splio 플랫폼에서 내보내야 합니다.

Splio에서 내보낼 캠페인을 선택하고 **Export Campaigns**를 클릭합니다. 내보낸 후, 오디언스가 자동으로 Braze 계정에 업로드됩니다.

![Splio 플랫폼에서 캠페인을 내보내는 중입니다.]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### 3단계: Splio 맞춤 오디언스에서 세그먼트를 생성합니다.

Braze에서 **Segments**로 이동하여 Splio 코호트 세그먼트의 이름을 지정하고 필터로 **Splio Cohorts**를 선택합니다. 여기에서 포함할 Splio 코호트를 선택하세요. Splio 코호트 세그먼트를 생성한 후, 캠페인이나 캔버스를 만들 때 오디언스 필터로 선택할 수 있습니다.

![Braze에서 Splio 코호트 세그먼트를 생성하는 중입니다.]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![Braze 세그먼트 빌더에서 사용자 속성 필터 "Splio 코호트"는 "포함" 및 "주요 코호트"로 설정되어 있습니다.]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

Having trouble locating your cohort? 지침을 보려면 [문제 해결](#troubleshooting) 섹션을 확인하세요.

{% alert important %}
Braze에 이미 존재하는 사용자만 코호트에 추가되거나 제거됩니다. 코호트 가져오기는 Braze에서 새로운 사용자를 생성하지 않습니다.
{% endalert %}

## Using this integration

Splio 세그먼트를 사용하려면 Braze 캠페인이나 캔버스를 생성하고 세그먼트를 타겟 오디언스로 선택하세요.

![타겟팅 단계의 Braze 캠페인 빌더에서 "세그먼트별 타겟 사용자" 필터는 "Splio 코호트"로 설정되어 있습니다.]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## 사용자 일치

Braze는 식별된 사용자를 `external_id` 또는 `alias`로 일치시킵니다. 익명 사용자는 `device_id`로 일치됩니다. 원래 익명 사용자로 생성된 식별된 사용자는 `device_id`로 일치할 수 없으며, `external_id` 또는 `alias`로 일치해야 합니다.

## 문제 해결

목록에서 올바른 코호트를 찾을 수 없는 경우, Splio에서 캠페인 세부정보를 확인하고 **내보내기 파일 이름**을 확인하여 이름을 확인하세요.

![캠페인 세부 정보 페이지 하단에 코호트 이름이 표시됩니다.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

오디언스를 검색하는 데 문제가 있는 경우, 지원을 위해 [Splio 팀](mailto:support-team@splio.com)에 문의하세요.